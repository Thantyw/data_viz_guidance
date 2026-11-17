"""Portable ACS 1-year non-stacked area chart: persons below poverty threshold.

Install: pip install requests pandas matplotlib
Run: python area_chart.py --states Florida,Georgia,Virginia --out ./area_outputs
Set optional Census API key as CENSUS_API_KEY; do not store credentials in source.
"""
import argparse
import json
import os
import platform
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import requests
from common.data_input import yearly_frames, source_description

API_BASE = 'https://api.census.gov/data'
FIELDS = ['NAME', 'B17001_001E', 'B17001_002E', 'B17001_002M']
DEFAULT_STATES = 'Florida,Georgia,Virginia'
DEFAULT_YEARS = '2021,2022,2023,2024'


def parse_years(value):
    years = [int(x.strip()) for x in value.split(',') if x.strip()]
    if not years or len(set(years)) != len(years) or not all(2021 <= y <= 2024 for y in years):
        raise ValueError('Use unique ACS 1-year release years from 2021 through 2024 for this example.')
    years = sorted(years)
    if years != list(range(min(years), max(years)+1)):
        raise ValueError('Area chart requires consecutive years; do not bridge unobserved periods with filled areas.')
    return years


def get_api_rows(year, key=None, session=None):
    params = {'get': ','.join(FIELDS), 'for': 'state:*'}
    if key:
        params['key'] = key
    session = session or requests
    url = f'{API_BASE}/{year}/acs/acs1'
    try:
        response = session.get(url, params=params, timeout=45)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f'Census API HTTP or network error for {year}: {exc}') from exc
    try:
        payload = response.json()
    except ValueError as exc:
        raise RuntimeError(f'Census API returned non-JSON content for {year}; HTTP {response.status_code}; '
                           f'content-type={response.headers.get("Content-Type", "unknown")}; '
                           f'response excerpt={response.text[:180]!r}') from exc
    if not isinstance(payload, list) or len(payload) < 2 or not isinstance(payload[0], list):
        raise ValueError(f'Unexpected Census API payload for {year}: {str(payload)[:180]}')
    header, *values = payload
    missing = set(FIELDS + ['state']) - set(header)
    if missing:
        raise ValueError(f'Missing expected Census fields for {year}: {sorted(missing)}')
    return pd.DataFrame(values, columns=header)


def validate_and_prepare(frames, states, years):
    all_rows = []
    for year, frame in zip(years, frames):
        df = frame.copy()
        df['year'] = year
        df = df[df['NAME'].isin(states)]
        for _, row in df.iterrows():
            try:
                universe = int(row['B17001_001E'])
                estimate = int(row['B17001_002E'])
                moe = int(row['B17001_002M'])
            except (ValueError, TypeError) as exc:
                raise ValueError(f'Missing/suppressed or nonnumeric estimate/MOE for {row["NAME"]}, {year}') from exc
            if not (0 <= estimate <= universe and 0 <= moe < 100_000_000):
                raise ValueError(f'Invalid poverty estimate/universe/MOE for {row["NAME"]}, {year}')
            all_rows.append({'state': row['NAME'], 'year': year, 'persons_below_poverty': estimate,
                             'poverty_status_universe': universe, 'moe_90': moe,
                             'lower_90_display': max(0, estimate - moe), 'upper_90': estimate + moe,
                             'source': f'{API_BASE}/{year}/acs/acs1', 'table': 'B17001'})
    result = pd.DataFrame(all_rows)
    expected = {(s, y) for s in states for y in years}
    observed = set(zip(result['state'], result['year'])) if not result.empty else set()
    if expected != observed:
        raise ValueError(f'Missing requested state-year combinations: {sorted(expected-observed)}')
    if result.duplicated(['state', 'year']).any():
        raise ValueError('Duplicate state-year rows found')
    return result.sort_values(['state', 'year']).reset_index(drop=True)


def make_chart(df, states, years, outdir):
    # Small multiples deliberately avoid overlapping opaque areas; this is NOT a stacked area chart.
    n = len(states)
    fig, axs = plt.subplots(n, 1, figsize=(9, 3.1*n + 1), sharex=True, sharey=True, squeeze=False)
    y_max = float(df['persons_below_poverty'].max()) * 1.12
    for ax, state in zip(axs[:, 0], states):
        sub = df[df.state == state].sort_values('year')
        x = sub['year'].to_numpy(dtype=float)
        y = sub['persons_below_poverty'].to_numpy(dtype=float)
        ax.fill_between(x, 0, y, color='#21618C', alpha=.38)
        ax.plot(x, y, color='#163A54', linewidth=2.2, marker='o', markersize=5)
        ax.set_title(state, loc='left', fontsize=11, fontweight='bold')
        ax.set_ylim(0, y_max)
        ax.set_ylabel('People (count)')
        ax.grid(axis='y', linestyle=':', alpha=.45)
        ax.ticklabel_format(axis='y', style='plain', useOffset=False)
    axs[-1, 0].set_xticks(years)
    axs[-1, 0].set_xlabel('ACS 1-year release year')
    fig.suptitle('People below poverty threshold, ACS 1-year estimates', fontweight='bold')
    fig.text(.5, .008, 'Filled areas begin at zero; panels use the same y-axis. Shading is not additive.\n'
             '2021–2024 ACS B17001_002E; 90% MOEs in companion data table. Estimates do not establish significant changes.',
             ha='center', va='bottom', fontsize=9)
    fig.tight_layout(rect=[0, .045, 1, .97])
    fig.savefig(outdir / 'area_chart.png', dpi=190, bbox_inches='tight')
    fig.savefig(outdir / 'area_chart.svg', bbox_inches='tight')
    plt.close(fig)


def main(args=None, dataframe=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--states', default=os.getenv('AREA_STATES', DEFAULT_STATES),
                   help='Comma-separated full state names (default: Florida,Georgia,Virginia)')
    p.add_argument('--years', default=os.getenv('AREA_YEARS', DEFAULT_YEARS),
                   help='Comma-separated years in 2021–2024')
    p.add_argument('--out', default=os.getenv('AREA_OUTPUT_DIR', './area_chart_outputs'),
                   help='Analyst-owned output directory')
    p.add_argument('--source', choices=['api','csv','excel','dataframe'],default='api')
    p.add_argument('--input-file',help='CSV or Excel file for local mode')
    p.add_argument('--api-key', default=None, help='Optional key; prefer CENSUS_API_KEY env var for security')
    opt = p.parse_args(args)
    states = [s.strip() for s in opt.states.split(',') if s.strip()]
    if not states or len(set(states)) != len(states):
        raise ValueError('Select one or more unique state names')
    years = parse_years(opt.years)
    outdir = Path(opt.out).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    key = opt.api_key or os.getenv('CENSUS_API_KEY', '').strip() or None
    frames = yearly_frames(opt.source, years, FIELDS+['state'],
       api_loader=lambda y: get_api_rows(y,key=key),input_file=opt.input_file, dataframe=dataframe)
    df = validate_and_prepare(frames, states, years)
    df.to_csv(outdir / 'area_chart_data.csv', index=False)
    make_chart(df, states, years, outdir)
    # HTML table is a supplemental accessible alternative; accessibility needs manual review.
    table = df[['state', 'year', 'persons_below_poverty', 'moe_90', 'poverty_status_universe']]
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<title>ACS area-chart source data</title></head><body>'
            '<h1>People below poverty threshold: source data</h1>'
            '<p>ACS 1-year B17001 estimates, 2021–2024. MOE is the published 90% margin of error. '
            'Counts are not poverty rates; differences have not been tested for significance.</p>'
            + table.to_html(index=False, border=1, classes='data-table') + '</body></html>')
    (outdir / 'area_chart_table.html').write_text(html, encoding='utf-8')
    alt = ('Small-multiple area charts showing the estimated number of people below the poverty threshold '
           f'in {", ".join(states)} across ACS 1-year releases {years[0]}–{years[-1]}. '
           'All panels use a common zero-based vertical scale. Refer to the accompanying table for '
           'exact values and 90% margins of error; no significance test of year-to-year changes is implied.')
    (outdir / 'area_chart_alt_text.txt').write_text(alt, encoding='utf-8')
    manifest = {'dataset': 'ACS 1-year Detailed Tables', 'table': 'B17001',
                'measure': 'B17001_002E', 'moe': 'B17001_002M',
                'states': states, 'years': years, 'output_directory': str(outdir),
                'python': platform.python_version(), 'pandas': pd.__version__,
                'matplotlib': matplotlib.__version__, 'requests': requests.__version__,
                'credentials_included': False, 'execution_mode': opt.source, 'input_metadata':source_description(opt.source,opt.input_file),
                'manual_508_testing': 'not performed by code'}
    (outdir / 'area_chart_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Saved 6 output files to {outdir}')
    return df


if __name__ == '__main__':
    main()
