"""Reusable GB-DATA-001 county-estimate input, validation and output helpers.

Supports API, CSV, XLSX, and pandas DataFrame. Local modes NEVER call the API.
This module analyzes county-level *estimates*, NOT individual household incomes.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
from datetime import datetime, timezone
import platform
import pandas as pd
import numpy as np
import requests

STATE_FIPS = {'Alabama':'01','Alaska':'02','Arizona':'04','Arkansas':'05','California':'06','Colorado':'08','Connecticut':'09','Delaware':'10','District of Columbia':'11','Florida':'12','Georgia':'13','Hawaii':'15','Idaho':'16','Illinois':'17','Indiana':'18','Iowa':'19','Kansas':'20','Kentucky':'21','Louisiana':'22','Maine':'23','Maryland':'24','Massachusetts':'25','Michigan':'26','Minnesota':'27','Mississippi':'28','Missouri':'29','Montana':'30','Nebraska':'31','Nevada':'32','New Hampshire':'33','New Jersey':'34','New Mexico':'35','New York':'36','North Carolina':'37','North Dakota':'38','Ohio':'39','Oklahoma':'40','Oregon':'41','Pennsylvania':'42','Rhode Island':'44','South Carolina':'45','South Dakota':'46','Tennessee':'47','Texas':'48','Utah':'49','Vermont':'50','Virginia':'51','Washington':'53','West Virginia':'54','Wisconsin':'55','Wyoming':'56'}

REQUIRED_ACS = {'NAME','state','county','B19013_001E','B19013_001M'}
REQUIRED_TIDY = {'NAME','state_name','GEOID','median_income','moe_90'}


def fetch_counties(state: str, year: int, api_key: str = '', request_get=None) -> pd.DataFrame:
    """Census API mode only; never put key or URL with credential in errors or logs."""
    if state not in STATE_FIPS:
        raise ValueError(f'Unknown state: {state}')
    getter = request_get or requests.get
    url = f'https://api.census.gov/data/{year}/acs/acs5'
    params = {'get':'NAME,B19013_001E,B19013_001M', 'for':'county:*', 'in':f'state:{STATE_FIPS[state]}'}
    if api_key: params['key'] = api_key
    try:
        response = getter(url, params=params, timeout=45)
    except requests.RequestException as exc:
        raise RuntimeError(f'Census API connection failed for {state}; check internet access and credentials.') from None
    if response.status_code != 200:
        raise RuntimeError(f'Census API HTTP {response.status_code} for {state}; check endpoint, release year and credentials.')
    try:
        rows = response.json()
    except ValueError:
        raise RuntimeError(f'Census API did not return valid JSON for {state}; check API response and credentials.') from None
    if not isinstance(rows, list) or len(rows)<2 or not isinstance(rows[0],list):
        raise RuntimeError(f'Unexpected Census API data structure for {state}')
    header=rows[0]
    if len(header)!=len(set(header)) or not REQUIRED_ACS.issubset(header) or any(len(r)!=len(header) for r in rows[1:]):
        raise RuntimeError(f'Census API columns/rows missing or invalid for {state}')
    df=pd.DataFrame(rows[1:], columns=header)
    df['state_name']=state
    return df


def load_counties(source: str, *, states: list[str], year: int=2024, input_file=None,
                  dataframe=None, api_key: str='', request_get=None) -> pd.DataFrame:
    """Normalize county rows using input shape: ACS variable codes or analyst tidy format.

    Tidy columns: NAME, state_name, GEOID, median_income, moe_90, year.
    ACS columns: NAME, state, county, state_name, B19013_001E, B19013_001M, year.
    The local year must match requested year; no implicit mixing of releases.
    """
    source=source.lower().strip()
    if source not in {'api','csv','excel','dataframe'}:
        raise ValueError('source must be api, csv, excel, or dataframe')
    states=list(dict.fromkeys(states))
    if not states or len(states)>12:
        raise ValueError('Specify 1 to 12 states')
    if not isinstance(year,int) or not 2010<=year<=2024:
        raise ValueError('Example mappings cover ACS 5-year through 2024; validate later year metadata before extension')
    if source=='api':
        frames=[fetch_counties(s,year,api_key,request_get=request_get) for s in states]
        df=pd.concat(frames,ignore_index=True)
        df['year']=year
    elif source=='dataframe':
        if not isinstance(dataframe,pd.DataFrame): raise TypeError('source=dataframe requires a pandas DataFrame')
        df=dataframe.copy(deep=True)
    else:
        if input_file is None: raise ValueError('CSV/Excel mode requires input_file')
        path=Path(input_file).expanduser()
        if not path.is_file(): raise FileNotFoundError(f'Data file not found: {path}')
        if source=='csv':
            df=pd.read_csv(path, dtype={'state':str,'county':str,'GEOID':str})
        else:
            df=pd.read_excel(path, dtype={'state':str,'county':str,'GEOID':str})
    if 'year' not in df.columns: raise ValueError('Missing required year column; local file must document ACS release year')
    year_column=pd.to_numeric(df['year'], errors='coerce')
    if year_column.isna().any() or (year_column!=year).any():
        raise ValueError(f'All input rows must have year={year}; multi-year county distributions require separate runs')
    if REQUIRED_ACS.issubset(df.columns) and 'state_name' in df.columns:
        selected=df.loc[df['state_name'].isin(states)].copy()
        selected['GEOID']=selected['state'].astype(str).str.zfill(2)+selected['county'].astype(str).str.zfill(3)
        selected['median_income']=pd.to_numeric(selected['B19013_001E'],errors='coerce')
        selected['moe_90']=pd.to_numeric(selected['B19013_001M'],errors='coerce')
    elif REQUIRED_TIDY.issubset(df.columns):
        selected=df.loc[df['state_name'].isin(states)].copy()
        selected['GEOID']=selected['GEOID'].astype(str).str.zfill(5)
        selected['median_income']=pd.to_numeric(selected['median_income'],errors='coerce')
        selected['moe_90']=pd.to_numeric(selected['moe_90'],errors='coerce')
    else:
        raise ValueError('Expected ACS columns with state_name or tidy columns NAME, state_name, GEOID, median_income, moe_90 and year')
    missing=[s for s in states if s not in set(selected['state_name'])]
    if missing: raise ValueError(f'Missing requested states: {missing}')
    if selected.duplicated(['state_name','GEOID']).any():
        raise ValueError('Duplicate county GEOID within state; observations must be unique')
    if selected['GEOID'].isna().any() or not selected['GEOID'].str.fullmatch(r'\d{5}').all():
        raise ValueError('GEOID must be a five-digit county geographic identifier')
    if selected['NAME'].isna().any(): raise ValueError('NAME is required for each county')
    selected['valid_income']=np.isfinite(selected['median_income']) & (selected['median_income']>0)
    selected['valid_moe']=np.isfinite(selected['moe_90']) & (selected['moe_90']>=0)
    # Exclude missing/suppressed values, including all negative Census sentinel estimates.
    return selected.reset_index(drop=True)


def output_paths(output_dir):
    path=Path(output_dir).expanduser().resolve(); path.mkdir(parents=True,exist_ok=True); return path


def record_manifest(out: Path, name: str, *, source, input_file, year, states, rows, valid, extra):
    manifest={'visualization':name,'input_mode':source,'input_file':str(Path(input_file).expanduser()) if source in {'csv','excel'} else None,
              'source_metadata':'Analyst-provided local dataset; provenance must be verified' if source!='api' else f'{year} ACS 5-Year Detailed Tables Census API',
              'dataset_year':year,'states':states,'observation_unit':'county',
              'metric':'county median household income estimate (not individual household income)',
              'county_rows':int(rows),'valid_county_rows':int(valid),'excluded_count':int(rows-valid),
              'python':platform.python_version(),'pandas':pd.__version__,'numpy':np.__version__,
              'timestamp_utc':datetime.now(timezone.utc).isoformat(),'api_key_saved':False,
              'manual_section_508_verification':'not performed',**extra}
    (out/f'{name}_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return manifest


def table_html(title: str, description: str, tables: list[tuple[str,pd.DataFrame]]):
    from html import escape
    body=''.join(f'<h2>{escape(label)}</h2>'+df.to_html(index=False,escape=True,border=1) for label,df in tables)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>'+escape(title)+
            '</title></head><body><h1>'+escape(title)+'</h1><p>'+escape(description)+'</p>'+body+'</body></html>')
