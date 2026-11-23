"""GB-DATA-001 shared input adapter. Analyst data never requires a Census API key."""
from pathlib import Path
import os
import pandas as pd
import requests

class InputError(ValueError):
    pass

def load(source='csv', input_file=None, dataframe=None, *, year=2024, dataset='acs1', variables=(), states=None, timeout=45):
    source=source.lower()
    if source=='dataframe':
        if not isinstance(dataframe,pd.DataFrame): raise InputError('dataframe mode requires a pandas DataFrame')
        frame=dataframe.copy()
    elif source in ('csv','excel'):
        if not input_file: raise InputError('input_file is required for CSV/Excel')
        path=Path(input_file).expanduser()
        if not path.is_file(): raise FileNotFoundError(f'Input file not found: {path}')
        frame=pd.read_csv(path, dtype={'state':str}) if source=='csv' else pd.read_excel(path,dtype={'state':str})
    elif source=='api':
        if not variables: raise InputError('API mode requires a list of variables')
        url=f'https://api.census.gov/data/{int(year)}/acs/{dataset}'
        params={'get':','.join(['NAME']+list(variables)),'for':'state:*'}
        key=os.getenv('CENSUS_API_KEY','').strip()
        if key: params['key']=key
        try:
            response=requests.get(url,params=params,timeout=timeout,headers={'Accept':'application/json'})
        except requests.RequestException as exc:
            raise RuntimeError(f'Census API request failed: {type(exc).__name__}; check connectivity and credentials') from None
        if not response.ok:
            raise RuntimeError(f'Census API HTTP {response.status_code}; check year, variable IDs, and credentials')
        try: payload=response.json()
        except ValueError as exc:
            raise RuntimeError('Census API response was not JSON; check credentials and endpoint') from exc
        if not isinstance(payload,list) or len(payload)<2 or not isinstance(payload[0],list):
            raise InputError('Unexpected or empty Census API response')
        frame=pd.DataFrame(payload[1:],columns=payload[0]); frame['year']=int(year)
    else:
        raise InputError('source must be api, csv, excel, or dataframe')
    if 'NAME' not in frame: raise InputError('Input requires NAME geography column')
    if states:
        wanted={s.strip().lower() for s in states}
        frame=frame[frame.NAME.astype(str).str.strip().str.lower().isin(wanted)].copy()
        found={x.lower() for x in frame.NAME.astype(str)}
        if wanted!=found: raise InputError(f'Geographies not found: {sorted(wanted-found)}')
    if 'year' in frame:
        frame['year']=pd.to_numeric(frame['year'],errors='raise').astype(int)
        frame=frame[frame.year==int(year)].copy()
    if frame.empty: raise InputError('No records after geography/year filtering')
    return frame.reset_index(drop=True)

def require_numeric(frame,columns,*,allow_zero=True):
    missing=[x for x in columns if x not in frame.columns]
    if missing: raise InputError(f'Missing input variables: {missing}')
    out=frame.copy()
    for col in columns:
        out[col]=pd.to_numeric(out[col],errors='coerce')
        # Treat ACS negative sentinel values and invalid values as missing, never zero.
        if out[col].isna().any() or (~out[col].map(lambda v: v>=0 if allow_zero else v>0)).any():
            raise InputError(f'{col}: missing, suppressed, nonnumeric or negative data; inspect input')
    return out
