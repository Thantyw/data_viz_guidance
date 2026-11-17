"""Accessible ACS state-level scatter plot; portable public multi-source example.

Install: python -m pip install requests pandas matplotlib
Run: python scatter_plot.py --states Florida,Georgia,Texas,Virginia --out ./scatter_outputs
Optional: set CENSUS_API_KEY in your environment. Do not store keys in source.
"""
import argparse
import json
import os
import platform
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

YEAR = 2024  # ACS 1-year Detailed Tables; validate variable mappings before adapting to another year.
BASE = f'https://api.census.gov/data/{YEAR}/acs/acs1'
FIELDS = ['NAME','B19013_001E','B19013_001M','B17001_001E','B17001_002E','B17001_002M','B01003_001E']
DEFAULT_STATES = 'Florida,Georgia,Maryland,Texas,Virginia'


def fetch_data(session=None, key=None):
    if not key:
        raise RuntimeError('Census API key required. Set CENSUS_API_KEY in your own environment or notebook secrets.')
    client = session if session is not None else requests
    params = {'get': ','.join(FIELDS), 'for': 'state:*'}
    if key:
        params['key'] = key
    try:
        response = client.get(BASE, params=params, timeout=45)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f'Census API network/HTTP error: {exc}') from exc
    try:
        payload = response.json()
    except ValueError as exc:
        raise RuntimeError(f'Census API returned non-JSON content (HTTP {response.status_code}, '
                           f'content-type {response.headers.get("Content-Type", "unknown")}); '
                           'verify API access, key activation, and endpoint.') from exc
    if not isinstance(payload, list) or len(payload) < 2 or not isinstance(payload[0], list):
        raise ValueError('Unexpected Census API response structure')
    header, *rows = payload
    if len(header) != len(set(header)) or not set(FIELDS+['state']).issubset(header):
        raise ValueError('Missing or repeated required Census API fields')
    if any(len(r)!=len(header) for r in rows):
        raise ValueError('Inconsistent row width in Census API response')
    return pd.DataFrame(rows, columns=header)


def prepare(data, states):
    if not states or len(set(states)) != len(states):
        raise ValueError('Choose one or more unique state names')
    selected = data.loc[data['NAME'].isin(states)].copy()
    if len(selected) != len(states) or selected['NAME'].duplicated().any():
        missing = sorted(set(states)-set(selected['NAME']))
        raise ValueError(f'Unknown or missing states: {missing}; use full Census state names')
    values = FIELDS[1:]
    for field in values:
        selected[field] = pd.to_numeric(selected[field], errors='coerce')
        if selected[field].isna().any() or (selected[field] < 0).any():
            raise ValueError(f'Missing, suppressed, or invalid {field} for selected states')
    if (selected['B17001_001E'] <= 0).any() or (selected['B01003_001E'] <= 0).any():
        raise ValueError('Population denominator and total population must be positive')
    if (selected['B17001_002E'] > selected['B17001_001E']).any():
        raise ValueError('Poverty numerator cannot exceed poverty-universe denominator')
    # Exclude invalid Census sentinel estimates (negative values), enforce sensible MOEs.
    result = pd.DataFrame({
        'state': selected['NAME'].to_numpy(),
        'median_household_income_usd': selected['B19013_001E'].to_numpy(float),
        'income_moe_90_usd': selected['B19013_001M'].to_numpy(float),
        'poverty_universe': selected['B17001_001E'].to_numpy(float),
        'below_poverty_count': selected['B17001_002E'].to_numpy(float),
        'below_poverty_count_moe_90': selected['B17001_002M'].to_numpy(float),
        'total_population': selected['B01003_001E'].to_numpy(float),
    })
    result['poverty_percent'] = 100.0 * result['below_poverty_count'] / result['poverty_universe']
    result['year'] = YEAR
    result['source_dataset'] = '2024 ACS 1-year Detailed Tables'
    if not result['poverty_percent'].between(0, 100).all():
        raise ValueError('Poverty percentage outside 0-100')
    # No MOE for the derived ratio is asserted by this demonstration.
    # Published numerator and income MOEs are retained for downstream evaluation.
    return result.sort_values('state').reset_index(drop=True)


def draw_chart(frame, out):
    """Plot two continuous variables; uniform marker area deliberately excludes population."""
    fig, ax = plt.subplots(figsize=(10.5, 7.3))
    vals = frame.sort_values('state')
    ax.scatter(vals['median_household_income_usd'], vals['poverty_percent'],
               s=90, marker='o', facecolor='#bed9ea', edgecolor='#153b56',
               linewidth=1.4, zorder=3)
    for _, rec in vals.iterrows():
        ax.annotate(rec['state'],
                    (rec['median_household_income_usd'], rec['poverty_percent']),
                    xytext=(6, 6), textcoords='offset points', fontsize=9,
                    color='#183246')
    ax.set(xlabel='Median household income (2024 inflation-adjusted dollars)',
           ylabel='People below poverty threshold (% of poverty-status universe)',
           title='State median household income and poverty percentage, 2024 ACS')
    ax.grid(alpha=.3, linestyle=':', zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlim(left=max(0, vals['median_household_income_usd'].min()*.82))
    ax.set_ylim(bottom=0, top=max(1, vals['poverty_percent'].max()*1.28))
    fig.text(.5, .012, 'Source: 2024 ACS 1-year Detailed Tables B19013 and B17001. '
             'Poverty percentage = 100 × below-poverty count / poverty-status universe. '
             'Association does not demonstrate causation.',
             ha='center', fontsize=8, wrap=True)
    fig.tight_layout(rect=[0,.06,1,1])
    fig.savefig(out/'scatter_plot.png', dpi=180, bbox_inches='tight')
    fig.savefig(out/'scatter_plot.svg', bbox_inches='tight')
    plt.close(fig)


def save_outputs(df, out, states):
    out.mkdir(parents=True,exist_ok=True)
    csv_path = out/'scatter_plot_data.csv'
    df.to_csv(csv_path,index=False)
    accessible = df[['state','median_household_income_usd','income_moe_90_usd',
                     'poverty_percent','below_poverty_count','below_poverty_count_moe_90',
                     'poverty_universe','total_population']].copy()
    html = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            '<title>2024 ACS scatter plot data</title></head><body>'
            '<h1>2024 ACS: state income, poverty, and population</h1>'
            '<p>The poverty percentage is a derived point estimate. The displayed MOEs refer to '
            'published income and below-poverty counts, not to the derived percentage. '
            'All points use the same marker size; population is not encoded.</p>' +
            '<table><caption>ACS 2024 scatter plot source values</caption>' + accessible.to_html(index=False, border=0, classes='data-table', escape=True).replace('<table border="0" class="dataframe data-table">', '').replace('</table>', '') + '</table></body></html>')
    (out/'scatter_plot_table.html').write_text(html,encoding='utf-8')
    # An individualized alternative-text DRAFT; manual editorial assessment needed.
    txt = ('Scatter plot of 2024 ACS 1-year estimates for '+', '.join(states)+'. '
           'Horizontal axis: median household income in dollars. Vertical axis: estimated '
           'percentage of people below poverty threshold among the poverty-status universe. '
           'Point size is constant; state names identify '
           'the points. Full values and published margins of error are in the accompanying table. '
           'The chart does not establish causation or statistical significance.\n')
    (out/'scatter_plot_alt_text_draft.txt').write_text(txt,encoding='utf-8')
    draw_chart(df,out)
    checks = {
        'required_state_rows':bool(len(df)==len(states)),
        'one_row_per_state':bool(not df['state'].duplicated().any()),
        'nonnegative_population':bool((df['total_population']>0).all()),
        'valid_poverty_fraction':bool(df['poverty_percent'].between(0,100).all()),
        'uniform_point_size':True,
        'moe_for_derived_ratio_claimed':False,
    }
    assert all(v for k,v in checks.items() if k!='moe_for_derived_ratio_claimed')
    manifest={'source':BASE,'year':YEAR,'variables':FIELDS,'states':states,
              'point_estimate_definition':'100 * B17001_002E / B17001_001E',
              'size_encoding':'constant marker size; no third variable encoded',
              'moe_note':'No derived poverty percentage MOE computed; published count and income MOEs retained.',
              'python':platform.python_version(),'pandas':pd.__version__,
              'matplotlib':matplotlib.__version__,'checks':checks,
              'manual_accessibility_verification':'NOT PERFORMED',
              'live_census_api_execution':'requires analyst run'}
    (out/'scatter_plot_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    return checks


# GB-DATA-001: source-independent adapter. Preserve original Census field identifiers.
NORMALIZED_TO_CENSUS = {
    'state': 'NAME',
    'median_household_income_usd': 'B19013_001E',
    'income_moe_90_usd': 'B19013_001M',
    'poverty_universe': 'B17001_001E',
    'below_poverty_count': 'B17001_002E',
    'below_poverty_count_moe_90': 'B17001_002M',
    'total_population': 'B01003_001E',
}


def standardize_input(frame):
    """Accept Census raw or a documented normalized analytical schema."""
    if not isinstance(frame, pd.DataFrame):
        raise TypeError('Provide a Pandas DataFrame')
    result = frame.copy()
    if set(NORMALIZED_TO_CENSUS).issubset(result.columns):
        # The normalized columns are not a new data source; preserve their measure definitions.
        result = result.rename(columns=NORMALIZED_TO_CENSUS)
    if 'year' in result.columns and not pd.to_numeric(result['year'], errors='coerce').eq(YEAR).all():
        raise ValueError('This example expects reference year 2024; revise the code and source labels for another year')
    required = set(FIELDS)
    missing = sorted(required.difference(result.columns))
    if missing:
        raise ValueError('Missing required input fields: ' + ', '.join(missing))
    if result['NAME'].isna().any() or result['NAME'].astype(str).str.strip().eq('').any():
        raise ValueError('Missing geography names')
    return result


def read_input_file(path, sheet=0):
    p = Path(path).expanduser()
    if not p.is_file():
        raise FileNotFoundError(f'Input file does not exist: {p}')
    if p.suffix.lower() == '.csv':
        data = pd.read_csv(p, dtype={'state': 'string'}, low_memory=False)
    elif p.suffix.lower() == '.xlsx':
        data = pd.read_excel(p, sheet_name=sheet, engine='openpyxl')
    else:
        raise ValueError('Only .csv and .xlsx input files are supported')
    return standardize_input(data)


def run(*, source='csv', input_file=None, dataframe=None, states=None,
        output_dir='./scatter_outputs', sheet=0, session=None, api_key=None):
    """Run the same validation and chart generation for all input modes.

    `source='dataframe'` does not require a file; API credentials are used only in `api` mode.
    """
    if source not in {'api', 'csv', 'excel', 'dataframe'}:
        raise ValueError('source must be api, csv, excel or dataframe')
    if source == 'api':
        if not (api_key or os.getenv('CENSUS_API_KEY', '').strip()):
            raise RuntimeError('API mode requires CENSUS_API_KEY or the api_key argument')
        data = standardize_input(fetch_data(session=session, key=api_key or os.environ['CENSUS_API_KEY']))
    elif source == 'dataframe':
        data = standardize_input(dataframe)
    else:
        if not input_file:
            raise ValueError(f'{source} mode requires input_file')
        if source == 'csv' and Path(input_file).suffix.lower() != '.csv':
            raise ValueError('CSV mode requires a .csv file')
        if source == 'excel' and Path(input_file).suffix.lower() != '.xlsx':
            raise ValueError('Excel mode requires a .xlsx file')
        data = read_input_file(input_file, sheet=sheet)
    if states is None:
        states = sorted(data['NAME'].astype(str).unique().tolist())
    elif isinstance(states, str):
        states = [v.strip() for v in states.split(',') if v.strip()]
    if not states:
        raise ValueError('No states available after filtering')
    validated = prepare(data, states)
    out = Path(output_dir).expanduser().resolve()
    checks = save_outputs(validated, out, states)
    manifest_path = next(out.glob('*manifest.json'))
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    manifest.update({'source': BASE if source == 'api' else 'analyst-provided dataset (metadata must be verified)',
                     'input_mode': source,
                     'source_file': str(Path(input_file).name) if input_file else None,
                     'api_used': source == 'api',
                     'user_provided_data': source != 'api',
                     'input_schema': 'Census raw or normalized',
                     'manual_accessibility_verification': 'NOT PERFORMED'})
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Created outputs in {out} from {source}; checks: {checks}')
    return validated


def main(argv=None, session=None):
    parser = argparse.ArgumentParser(description='Multi-source scatter chart (GB-DATA-001)')
    parser.add_argument('--source', choices=['api', 'csv', 'excel'], default='csv',
                        help='CSV default; API must be explicitly chosen')
    parser.add_argument('--input', default=None, help='CSV/XLSX input file; not used in API mode')
    parser.add_argument('--sheet', default='0', help='Excel sheet index or name')
    parser.add_argument('--states', default=None, help='Optional comma-separated full state names')
    parser.add_argument('--out', default='./scatter_outputs', help='User-chosen output directory')
    args = parser.parse_args(argv)
    sheet = int(args.sheet) if args.sheet.isdigit() else args.sheet
    return run(source=args.source, input_file=args.input, sheet=sheet,
               states=args.states, output_dir=args.out, session=session)


if __name__ == '__main__':
    main()
