"""Portable ACS stacked-area example. Python 3.10+, requests, pandas, matplotlib.
Configuration: CENSUS_API_KEY (optional), STACKED_STATES (comma-separated names/FIPS),
STACKED_YEARS (2021,2022,2023,2024 by default), STACKED_OUTPUT_DIR.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from html import escape

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import requests
import argparse
from common.data_input import yearly_frames, source_description

STATES = {'Alabama':'01','Alaska':'02','Arizona':'04','Arkansas':'05','California':'06',
 'Colorado':'08','Connecticut':'09','Delaware':'10','District of Columbia':'11',
 'Florida':'12','Georgia':'13','Hawaii':'15','Idaho':'16','Illinois':'17','Indiana':'18',
 'Iowa':'19','Kansas':'20','Kentucky':'21','Louisiana':'22','Maine':'23','Maryland':'24',
 'Massachusetts':'25','Michigan':'26','Minnesota':'27','Mississippi':'28','Missouri':'29',
 'Montana':'30','Nebraska':'31','Nevada':'32','New Hampshire':'33','New Jersey':'34',
 'New Mexico':'35','New York':'36','North Carolina':'37','North Dakota':'38','Ohio':'39',
 'Oklahoma':'40','Oregon':'41','Pennsylvania':'42','Rhode Island':'44','South Carolina':'45',
 'South Dakota':'46','Tennessee':'47','Texas':'48','Utah':'49','Vermont':'50',
 'Virginia':'51','Washington':'53','West Virginia':'54','Wisconsin':'55','Wyoming':'56'}
REVERSE = {v:k for k,v in STATES.items()}
VARIABLES = ['NAME','B01001_001E','B01001_002E','B01001_026E','B01001_002M','B01001_026M']

def parse_settings():
    raw = os.getenv('STACKED_STATES','Florida,Georgia').split(',')
    selected = []
    for v in raw:
        x = v.strip()
        if not x: continue
        match = next((k for k in STATES if k.lower()==x.lower()), None)
        fips = STATES[match] if match else x.zfill(2)
        if fips not in REVERSE: raise ValueError(f'Unsupported state name or FIPS: {x!r}')
        if fips not in selected: selected.append(fips)
    if not selected: raise ValueError('Choose at least one state')
    years = [int(x.strip()) for x in os.getenv('STACKED_YEARS','2021,2022,2023,2024').split(',') if x.strip()]
    if not years or len(set(years))!=len(years) or years!=sorted(years):
        raise ValueError('STACKED_YEARS must be unique, increasing years')
    if 2020 in years or any(y<2010 or y>2024 for y in years):
        raise ValueError('This example supports 2010–2019 and 2021–2024; 2020 ACS 1-year is not standard. Confirm variable comparability before changing years.')
    if len(years)<2: raise ValueError('At least two years are needed to display a trend')
    # A filled area must not interpolate across years that are absent from the series.
    if any(b-a!=1 for a,b in zip(years,years[1:])): raise ValueError('Use consecutive years only; do not bridge missing annual periods')
    output=Path(os.path.expanduser(os.getenv('STACKED_OUTPUT_DIR','./stacked_area_outputs'))).resolve()
    return selected, years, output

def request_acs(year, state, session=None):
    endpoint=f'https://api.census.gov/data/{year}/acs/acs1'
    params={'get': ','.join(VARIABLES), 'for':f'state:{state}'}
    key=os.getenv('CENSUS_API_KEY','').strip()
    if key: params['key']=key
    client=session or requests
    try:
        response=client.get(endpoint, params=params, timeout=35)
    except requests.RequestException as e:
        raise RuntimeError(f'Unable to connect to Census API for {year}: {e}') from e
    if response.status_code != 200:
        raise RuntimeError(f'Census API returned HTTP {response.status_code} for {year}, {REVERSE[state]}. Check year, network and your own API key if required. Response: {response.text[:260]!r}')
    try:
        data=response.json()
    except (ValueError, requests.exceptions.JSONDecodeError) as e:
        raise RuntimeError(f'Census API did not return JSON for {year}. Content type: {response.headers.get("content-type", "unknown")}; preview: {response.text[:200]!r}') from e
    if not isinstance(data,list) or len(data)!=2:
        raise ValueError(f'Unexpected Census response row count for {year}, {REVERSE[state]}')
    fields, record=data
    values=dict(zip(fields,record))
    if not set(VARIABLES).issubset(values):
        raise ValueError(f'Missing required B01001 fields in {year} API response')
    result={'state': REVERSE[state], 'state_fips':state, 'year':year,
            'source_url': f'{endpoint}?get={",".join(VARIABLES)}&for=state:{state}'}
    for variable in VARIABLES[1:]:
        raw=values[variable]
        if raw in (None,'','-666666666','-999999999','-888888888'):
            raise ValueError(f'{variable} unavailable/suppressed in {year} for {REVERSE[state]}')
        try: result[variable]=int(raw)
        except (ValueError,TypeError): raise ValueError(f'Noninteger {variable} for {year}: {raw!r}')
    return result

def validate(rows, years, states):
    df=pd.DataFrame(rows)
    if len(df)!=len(years)*len(states): raise ValueError('State-year grid is incomplete')
    if df.duplicated(['state_fips','year']).any(): raise ValueError('Duplicate state-years')
    if (df[['B01001_001E','B01001_002E','B01001_026E']]<0).any().any():
        raise ValueError('Negative populations are invalid')
    if (df[['B01001_002M','B01001_026M']]<0).any().any(): raise ValueError('Invalid negative margins of error')
    if not (df.B01001_001E==df.B01001_002E+df.B01001_026E).all():
        raise ValueError('Non-additive population categories: male + female must equal total')
    df['male_pct']=100*df.B01001_002E/df.B01001_001E
    df['female_pct']=100*df.B01001_026E/df.B01001_001E
    if (df.B01001_001E<=0).any() or ((df.male_pct+df.female_pct-100).abs()>1e-8).any():
        raise ValueError('Invalid percentage denominator or category total')
    return df.sort_values(['state','year']).reset_index(drop=True)

def draw_and_save(df, state, out):
    d=df[df.state==state].sort_values('year')
    years=d.year.to_numpy(dtype=int)
    male=d.B01001_002E.to_numpy(dtype=float)/1e6
    female=d.B01001_026E.to_numpy(dtype=float)/1e6
    fig,ax=plt.subplots(figsize=(9.5,5.8),layout='constrained')
    ax.fill_between(years,0,male,color='#23607B',alpha=0.95,label='Male')
    ax.fill_between(years,male,male+female,color='#E2B26B',alpha=0.95,hatch='//',edgecolor='#71512C',linewidth=0.8,label='Female (hatched)')
    ax.plot(years,male+female,color='#252525',linewidth=1.7,label='Total population')
    ax.set(xlabel='ACS 1-year release year',ylabel='Estimated population (millions)',title=f'{state}: population by sex, {years.min()}–{years.max()}')
    ax.set_ylim(bottom=0)
    ax.set_xticks(years)
    ax.grid(axis='y',alpha=0.26)
    ax.legend(loc='upper left',frameon=True)
    fig.text(0.01,0.01,'Source: U.S. Census Bureau, ACS 1-Year B01001. Counts are estimates; see accompanying MOE table.',fontsize=8)
    slug=state.lower().replace(' ','_')
    plt.rcParams['svg.fonttype']='none'
    fig.savefig(out/f'stacked_area_{slug}.png',dpi=170)
    fig.savefig(out/f'stacked_area_{slug}.svg')
    plt.close(fig)
    starting=d.iloc[0]
    ending=d.iloc[-1]
    alt=(f'Stacked area chart of estimated male and female populations in {state} from {years.min()} to {years.max()}. '
         f'Male is the lower solid area; female is the upper hatched area. '
         f'Total population rises from {starting.B01001_001E:,.0f} to {ending.B01001_001E:,.0f}. '
         'See the accompanying annual data table for exact values and published 90% margins of error.')
    (out/f'stacked_area_{slug}_alt.txt').write_text(alt+'\n',encoding='utf-8')

def main(session=None, *, source='api', input_file=None, dataframe=None):
    states,years,out=parse_settings()
    out.mkdir(parents=True, exist_ok=True)
    if source == 'api':
        rows=[request_acs(y,s,session) for s in states for y in years]
    else:
        frames=yearly_frames(source,years,VARIABLES+['state'],
              input_file=input_file,dataframe=dataframe)
        rows=[]
        for year,frame in zip(years,frames):
            for _,rec in frame.iterrows():
                state_name=str(rec['NAME'])
                fips = str(rec.get('state_fips',rec.get('state',''))).zfill(2)
                if not fips.strip('0') and state_name in STATES: fips=STATES[state_name]
                if fips not in REVERSE or REVERSE[fips]!=state_name: raise ValueError(f'Incorrect state FIPS/name: {state_name} / {fips}')
                if fips not in states: continue
                vals={v:pd.to_numeric(rec[v],errors='raise') for v in VARIABLES[1:]}
                if any(pd.isna(v) or v%1 for v in vals.values()): raise ValueError('Missing or noninteger ACS population/MOE values')
                rows.append({'state':state_name,'state_fips':fips,'year':year,
                             'source_url':'analyst-provided',**{k:int(v) for k,v in vals.items()}})
    df=validate(rows,years,states)
    df.to_csv(out/'stacked_area_acs_data.csv',index=False)
    table=df[['state','year','B01001_001E','B01001_002E','B01001_026E','B01001_002M','B01001_026M','male_pct','female_pct']]
    human=table.rename(columns={'B01001_001E':'Total population estimate','B01001_002E':'Male estimate','B01001_026E':'Female estimate','B01001_002M':'Male MOE (90%)','B01001_026M':'Female MOE (90%)','male_pct':'Male share (%)','female_pct':'Female share (%)'})
    html=('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>ACS population by sex data</title></head><body>'
          '<h1>ACS population by sex — underlying data</h1><p>2021–2024 ACS 1-Year B01001. Counts are estimates; margins of error are published at 90% confidence. '
          'Each year, male and female counts sum to the total population estimate.</p>'+
          human.to_html(index=False,border=1,classes=['data-table'])+'</body></html>')
    (out/'stacked_area_data_table.html').write_text(html,encoding='utf-8')
    for state in [REVERSE[s] for s in states]: draw_and_save(df,state,out)
    manifest={'source':'U.S. Census Bureau ACS 1-Year Detailed Table B01001','years':years,
              'states':[REVERSE[s] for s in states], 'categories':'male/female; exclusive, exhaustive partition of total',
              'total_reconciliation':'passed', 'unit':'population count, millions for chart',
              'python':sys.version.split()[0], 'pandas':pd.__version__, 'matplotlib':matplotlib.__version__,
              'run_utc':datetime.now(timezone.utc).isoformat(), 'api_key_saved':False,
              'input_metadata':source_description(source,input_file),
              'note':'All outputs require source and accessibility review before publication.'}
    (out/'execution_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print('Saved outputs to',out)
    return df

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',choices=['api','csv','excel'],default='api')
    parser.add_argument('--input-file')
    parser.add_argument('--states',default=os.getenv('STACKED_STATES','Florida,Georgia'))
    parser.add_argument('--years',default=os.getenv('STACKED_YEARS','2021,2022,2023,2024'))
    parser.add_argument('--out',default=os.getenv('STACKED_OUTPUT_DIR','./stacked_area_outputs'))
    args=parser.parse_args()
    os.environ['STACKED_STATES']=args.states; os.environ['STACKED_YEARS']=args.years;os.environ['STACKED_OUTPUT_DIR']=args.out
    main(source=args.source,input_file=args.input_file)
