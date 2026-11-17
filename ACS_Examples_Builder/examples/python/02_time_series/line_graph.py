"""Public ACS line-graph example: 2021-2024 median household income in 2024 dollars.

Install: pip install requests pandas matplotlib
Configure: LINEGRAPH_STATES, LINEGRAPH_YEARS, LINEGRAPH_OUTPUT_DIR, optional CENSUS_API_KEY.
Usage: python line_graph.py   or   python line_graph.py --self-test
"""
from __future__ import annotations
import html
import argparse
from common.data_input import yearly_frames, source_description
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
import re
import requests
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Census-recommended adjacent-year R-CPI-U-RS multipliers for ACS income comparisons.
# https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/2022.html
# https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/2023.html
# https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/2024.html
ADJACENT_FACTORS = {2021: 1.08091182, 2022: 1.04125145, 2023: 1.02937903}
SUPPORTED_YEARS = (2021, 2022, 2023, 2024)
VARIABLES = ('NAME', 'B19013_001E', 'B19013_001M')
SPECIAL = {-666666666, -555555555, -333333333, -222222222, -999999999, -888888888}

def parse_config():
    years = sorted(set(int(x.strip()) for x in os.getenv('LINEGRAPH_YEARS', '2021,2022,2023,2024').split(',') if x.strip()))
    if not years or any(y not in SUPPORTED_YEARS for y in years):
        raise ValueError('LINEGRAPH_YEARS supports only 2021,2022,2023,2024; check comparison factors before adding another year.')
    states = [x.strip() for x in os.getenv('LINEGRAPH_STATES', 'Florida,Georgia,Maryland,Texas,Virginia').split(',') if x.strip()]
    if not states or len(set(s.casefold() for s in states)) != len(states):
        raise ValueError('Supply unique state names in LINEGRAPH_STATES.')
    path = Path(os.path.expanduser(os.getenv('LINEGRAPH_OUTPUT_DIR', './linegraph_outputs'))).resolve()
    return years, states, path, os.getenv('CENSUS_API_KEY', '').strip()

def api_data(year, api_key='', session=None):
    url = f'https://api.census.gov/data/{year}/acs/acs1'
    params = {'get': ','.join(VARIABLES), 'for': 'state:*'}
    if api_key: params['key'] = api_key
    response = (session or requests).get(url, params=params, timeout=45)
    if response.status_code >= 400:
        # Never display full URL, because it may contain a secret query parameter.
        raise RuntimeError(f'ACS {year} returned HTTP {response.status_code}; check dataset, network, and your API credentials. Response preview: {response.text[:150]!r}')
    try: payload = response.json()
    except ValueError as exc:
        raise RuntimeError(f'ACS {year} sent non-JSON content; HTTP {response.status_code}, Content-Type {response.headers.get("Content-Type", "unknown")}. Preview: {response.text[:150]!r}') from exc
    if not isinstance(payload, list) or len(payload) < 2 or not isinstance(payload[0], list):
        raise RuntimeError(f'ACS {year} returned an unexpected JSON structure.')
    columns = payload[0]
    needed = set(VARIABLES) | {'state'}
    if not needed.issubset(columns):
        raise RuntimeError(f'ACS {year} response lacks fields: {needed-set(columns)}')
    out = [dict(zip(columns, vals)) for vals in payload[1:] if len(vals) == len(columns)]
    return out, url

def number_or_none(x):
    try:
        v = int(x)
        return None if v in SPECIAL or v < 0 else v
    except (TypeError, ValueError): return None

def factor_to_2024(year):
    factor = 1.0
    for y in range(year, 2024): factor *= ADJACENT_FACTORS[y]
    return factor

def make_data(years, states, api_key='', session=None, *, source='api', input_file=None, dataframe=None):
    state_lookup = {s.casefold() for s in states}
    result, urls = [], []
    frames = yearly_frames(source, years, list(VARIABLES)+['state'],
         api_loader=lambda y: api_data(y,api_key,session)[0],
         input_file=input_file, dataframe=dataframe)
    for year, frame in zip(years, frames):
        rows = frame.to_dict('records')
        url = f'https://api.census.gov/data/{year}/acs/acs1' if source=='api' else 'analyst-provided'
        urls.append(url)
        found = set()
        for r in rows:
            name = r['NAME']
            if name.casefold() not in state_lookup: continue
            found.add(name.casefold())
            val, moe = number_or_none(r['B19013_001E']), number_or_none(r['B19013_001M'])
            factor = factor_to_2024(year)
            result.append({'year':year, 'state':name, 'fips':r['state'], 'estimate_release_dollars':val,
                           'moe_90_release_dollars':moe, 'to_2024_factor':factor,
                           'estimate_2024_dollars':val*factor if val is not None else None,
                           'moe_90_2024_dollars':moe*factor if moe is not None else None,
                           'source_url':url})
        absent = state_lookup-found
        if absent: raise ValueError(f'State name(s) not found in ACS {year}: {", ".join(sorted(absent))}. Use full state names.')
    df = pd.DataFrame(result).sort_values(['state','year']).reset_index(drop=True)
    if df.duplicated(['state','year']).any(): raise AssertionError('Duplicate state-year rows')
    assert (df['to_2024_factor'] > 0).all()
    valid = df.dropna(subset=['estimate_2024_dollars','moe_90_2024_dollars'])
    assert (valid['moe_90_2024_dollars'] >= 0).all()
    return df, urls

def write_outputs(df, urls, years, states, folder):
    folder.mkdir(parents=True, exist_ok=True)
    csv_path = folder/'linegraph_acs_income_2024_dollars.csv'
    df.to_csv(csv_path, index=False)
    fig, ax = plt.subplots(figsize=(10.5,6.2))
    patterns = ['-','--',':','-.']
    markers = ['o','s','^','D','v','P','X']
    used = 0
    for state, part in df.groupby('state',sort=True):
        part = part.sort_values('year').set_index('year').reindex(range(min(years), max(years)+1))
        # Reindex all calendar years; a skipped release visibly breaks the line.
        y = pd.to_numeric(part['estimate_2024_dollars'], errors='coerce')
        ax.plot(part.index.to_numpy(), y.to_numpy(), label=state,
                linestyle=patterns[used%len(patterns)], marker=markers[used%len(markers)],
                linewidth=2.1, markersize=6)
        used += 1
    ax.set(xlabel='ACS 1-year release',ylabel='Median household income (2024 dollars)',
           title='ACS median household income by state, 2021–2024')
    ax.set_xticks(list(range(min(years), max(years)+1)))
    ax.grid(axis='y', alpha=.25)
    ax.legend(title='State',loc='best')
    fig.text(.1,.01,'Sources: U.S. Census Bureau ACS 1-year B19013; R-CPI-U-RS comparison factors.\n'
             'Estimates are not significance-tested; ACS income reference periods can overlap.',fontsize=8)
    fig.tight_layout(rect=(0,.075,1,1))
    fig.savefig(folder/'linegraph_acs_income.png',dpi=180)
    fig.savefig(folder/'linegraph_acs_income.svg')
    plt.close(fig)
    rows_html = []
    for row in df.itertuples(index=False):
        fmt = lambda v: 'Unavailable' if pd.isna(v) else f'{v:,.0f}'
        rows_html.append('<tr>'+''.join('<td>'+html.escape(str(v))+'</td>' for v in
            (row.state,row.year,fmt(row.estimate_2024_dollars),fmt(row.moe_90_2024_dollars),f'{row.to_2024_factor:.8f}'))+'</tr>')
    table = '''<!doctype html><html lang="en"><meta charset="utf-8"><title>ACS income data table</title><body>
<h1>Median household income by state, ACS 2021–2024 (2024 dollars)</h1>
<p>Source: U.S. Census Bureau ACS 1-year B19013. All values converted using Census-recommended R-CPI-U-RS adjacent-year factors. Margins of error are at the 90 percent confidence level. Estimates are not significance-tested.</p>
<table border="1"><caption>Income estimates, 90% MOEs, and conversion factors by state and year</caption><thead><tr><th scope="col">State</th><th scope="col">Year</th><th scope="col">Median income (2024 dollars)</th><th scope="col">MOE (2024 dollars)</th><th scope="col">Factor</th></tr></thead><tbody>''' + ''.join(rows_html) + '</tbody></table></body></html>'
    (folder/'linegraph_accessible_table.html').write_text(table,encoding='utf-8')
    lines = ['Median household income by state, 2021–2024, in 2024 dollars.',
             'Each state is shown as a time series; a missing estimate produces a break in its line.',
             'Values and margins of error appear in the accompanying accessible table.',
             'No significance test of changes was performed.']
    (folder/'linegraph_alt_text.txt').write_text(' '.join(lines)+'\n',encoding='utf-8')
    manifest = {'dataset':'ACS 1-year detailed tables B19013', 'years':years, 'states':states,
      'source_urls':urls,'price_year':2024,'inflation_index':'R-CPI-U-RS, Census ACS comparison factors',
      'adjacent_factors':{str(k):v for k,v in ADJACENT_FACTORS.items()},
      'factor_sources':[f'https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/{y}.html' for y in (2022,2023,2024)],
      'retrieved_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version.split()[0],
      'pandas':pd.__version__,'matplotlib':matplotlib.__version__,
      'checks':{'unique_state_year':True,'positive_factors':True,'nonnegative_valid_moes':True},
      'limitations':['2020 standard ACS 1-year excluded','Adjacent ACS periods share reference months',
                     'MOEs plotted in table only; no significance tests','Public data; manual accessibility testing of published page required']}
    (folder/'linegraph_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    return list(folder.glob('linegraph_*'))

def self_test():
    class FakeResponse:
        status_code=200
        headers={'Content-Type':'application/json'}
        text='synthetic test data'
        def __init__(self,year): self.year=year
        def json(self):
            return [['NAME','B19013_001E','B19013_001M','state'],
                    ['Florida',str(61000+(self.year-2021)*2000),'1200','12'],
                    ['Georgia',str(64000+(self.year-2021)*1900),'1100','13']]
    class FakeSession:
        def get(self,url,params,timeout): return FakeResponse(int(re.search(r'/data/(\d{4})/',url).group(1)))
    df, urls = make_data([2021,2022,2024],['Florida','Georgia'],session=FakeSession())
    assert len(df)==6 and factor_to_2024(2024)==1
    assert abs(factor_to_2024(2023)-1.02937903) < 1e-12
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        files=write_outputs(df,urls,[2021,2022,2024],['Florida','Georgia'],Path(d))
        assert len(files)>=6 and all(p.stat().st_size>0 for p in files)
        assert 'scope="col"' in (Path(d)/'linegraph_accessible_table.html').read_text()
    print('PASS: synthetic API, inflation factors, state selection, output redirection, and 6 output artifacts.')

def main():
    if '--self-test' in sys.argv: return self_test()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',choices=['api','csv','excel'],default='api')
    parser.add_argument('--input-file')
    parser.add_argument('--states',default=os.getenv('LINEGRAPH_STATES','Florida,Georgia,Maryland,Texas,Virginia'))
    parser.add_argument('--years',default=os.getenv('LINEGRAPH_YEARS','2021,2022,2023,2024'))
    parser.add_argument('--out',default=os.getenv('LINEGRAPH_OUTPUT_DIR','./linegraph_outputs'))
    args=parser.parse_args()
    os.environ['LINEGRAPH_STATES']=args.states
    os.environ['LINEGRAPH_YEARS']=args.years
    os.environ['LINEGRAPH_OUTPUT_DIR']=args.out
    years, states, folder, key = parse_config()
    df, urls = make_data(years,states,key,source=args.source,input_file=args.input_file)
    files=write_outputs(df,urls,years,states,folder)
    mf=folder/'linegraph_manifest.json'
    metadata=json.loads(mf.read_text());metadata.update(source_description(args.source,args.input_file));mf.write_text(json.dumps(metadata,indent=2))
    print(f'Saved {len(files)} files to {folder}')
    print(df[['state','year','estimate_2024_dollars','moe_90_2024_dollars']].to_string(index=False))

if __name__=='__main__': main()
