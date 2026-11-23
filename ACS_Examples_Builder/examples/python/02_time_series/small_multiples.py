"""Portable ACS small-multiples example. Requires requests, pandas, matplotlib.

Usage: python small_multiples.py --states Florida,Georgia,Texas,Virginia --years 2021,2022,2023,2024 --output-dir ./outputs
Optional environment variable: CENSUS_API_KEY. No project-local data files needed.
"""
import argparse
import json
import os
import platform
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import requests
from common.data_input import yearly_frames, source_description

API = 'https://api.census.gov/data/{year}/acs/acs1'
VARS = ['NAME', 'B17001_001E', 'B17001_002E', 'B17001_001M', 'B17001_002M']
DEFAULT_STATES = ['Florida', 'Georgia', 'Texas', 'Virginia']
DEFAULT_YEARS = [2021, 2022, 2023, 2024]


def fetch_year(year, session=None, api_key=None):
    if year < 2021 or year > 2024:
        raise ValueError('This documented release supports 2021–2024 only; validate variable mappings before extending.')
    client = session or requests
    params = {'get': ','.join(VARS), 'for': 'state:*'}
    if api_key:
        params['key'] = api_key
    try:
        response = client.get(API.format(year=year), params=params, timeout=35)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f'ACS {year} request failed: {exc}') from exc
    try:
        body = response.json()
    except (ValueError, requests.exceptions.JSONDecodeError) as exc:
        preview = response.text[:150].replace('\n', ' ')
        raise RuntimeError(f'ACS {year} did not return JSON (HTTP {response.status_code}): {preview}') from exc
    if not isinstance(body, list) or len(body) < 2 or not isinstance(body[0], list):
        raise ValueError(f'ACS {year} response was not a Census API tabular array')
    frame = pd.DataFrame(body[1:], columns=body[0])
    if not set(VARS + ['state']).issubset(frame.columns):
        raise ValueError(f'ACS {year} response missing required columns')
    frame['year'] = year
    return frame


def prepare(frames, states):
    if not frames:
        raise ValueError('No data returned')
    df = pd.concat(frames, ignore_index=True)
    for field in VARS[1:]:
        df[field] = pd.to_numeric(df[field], errors='coerce')
    df = df[df['NAME'].isin(states)].copy()
    if df.empty:
        raise ValueError('No requested states in API response; check C02_STATES/--states spelling')
    absent = set(states) - set(df['NAME'])
    if absent:
        raise ValueError(f'States not returned: {sorted(absent)}')
    # Census special/suppression values are not substantive counts.
    req = VARS[1:]
    df = df.dropna(subset=req)
    df = df[(df['B17001_001E'] > 0) & (df['B17001_002E'] >= 0)]
    if df.empty or (df['B17001_002E'] > df['B17001_001E']).any():
        raise ValueError('Invalid ACS numerator / denominator')
    if (df[['B17001_001M', 'B17001_002M']] < 0).any().any():
        raise ValueError('Negative ACS margin of error')
    df['poverty_pct'] = 100 * df['B17001_002E'] / df['B17001_001E']
    if not df['poverty_pct'].between(0, 100).all():
        raise ValueError('Derived poverty percentage outside 0–100')
    if df.duplicated(['NAME', 'year']).any():
        raise ValueError('Duplicate state–year records')
    df = df.sort_values(['NAME', 'year'])
    return df


def draw(df, states, years, png, svg):
    import math
    cols = 2 if len(states) > 1 else 1
    rows = math.ceil(len(states) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(10, max(3.6, 3.3 * rows)), sharex=True, sharey=True, squeeze=False)
    axes_flat = axes.ravel()
    upper = min(100, max(5, math.ceil(df['poverty_pct'].max() / 5) * 5 + 5))
    for ax, state in zip(axes_flat, states):
        sub = df.loc[df['NAME'] == state].set_index('year').reindex(years)
        # NaNs deliberately break gaps, rather than implying continuity.
        ax.plot(years, sub['poverty_pct'], marker='o', color='#205781', linewidth=2.0, markersize=5)
        ax.set_title(state, loc='left', fontsize=12, fontweight='bold')
        ax.set_ylim(0, upper)
        ax.set_xlim(min(years) - .2, max(years) + .2)
        ax.set_xticks(years)
        ax.grid(axis='y', color='#BBBBBB', linewidth=.6)
        ax.tick_params(axis='x', labelbottom=True)
        ax.tick_params(axis='y', labelleft=True)
    for ax in axes_flat[len(states):]:
        ax.set_visible(False)
    fig.supxlabel('ACS 1-Year release year')
    fig.supylabel('People below poverty threshold (% of poverty-status universe)')
    fig.suptitle('Poverty percentages by state, 2021–2024', fontsize=15, fontweight='bold')
    fig.text(.5, .016, 'Source: U.S. Census Bureau, ACS 1-Year B17001. Same y-axis scale in every panel.\n'
             'Points are estimates; MOEs for the underlying counts are in the accompanying CSV.',
             ha='center', fontsize=8)
    fig.tight_layout(rect=[.035, .075, 1, .94])
    fig.savefig(png, dpi=170, bbox_inches='tight')
    fig.savefig(svg, bbox_inches='tight')
    plt.close(fig)
    return upper


def run(states=None, years=None, output_dir=None, session=None, api_key=None, *, source='api', input_file=None, dataframe=None):
    states = list(states or DEFAULT_STATES)
    years = sorted(set(years or DEFAULT_YEARS))
    if not states or len(states) > 12 or len(set(states)) != len(states):
        raise ValueError('Select between 1 and 12 unique states')
    if any(y not in DEFAULT_YEARS for y in years):
        raise ValueError('Supported release years: 2021, 2022, 2023, 2024')
    if years != list(range(min(years), max(years) + 1)):
        raise ValueError('Select consecutive years; missing years must not be connected')
    output_dir = Path(output_dir or os.environ.get('SMALL_MULTIPLES_OUTPUT_DIR', './small_multiples_outputs')).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)
    api_key = api_key or os.environ.get('CENSUS_API_KEY') or None
    frames = yearly_frames(source, years, VARS+['state'],
        api_loader=lambda y: fetch_year(y, session, api_key),
        input_file=input_file,dataframe=dataframe)
    for y, frame in zip(years,frames): frame['year']=y
    data = prepare(frames, states)
    # Requiring all rows prevents silent loss of a geography/year. Missing year cells are never interpolated.
    expected = {(s, y) for s in states for y in years}
    observed = set(zip(data['NAME'], data['year']))
    if expected != observed:
        raise ValueError(f'Missing or suppressed state-year observations: {sorted(expected - observed)}')
    csv_path = output_dir / 'small_multiples_acs_data.csv'
    png = output_dir / 'small_multiples_acs.png'
    svg = output_dir / 'small_multiples_acs.svg'
    html = output_dir / 'small_multiples_acs_table.html'
    alt = output_dir / 'small_multiples_alt_text.txt'
    manifest = output_dir / 'small_multiples_manifest.json'
    data.to_csv(csv_path, index=False)
    axis_top = draw(data, states, years, png, svg)
    cols = ['NAME', 'year', 'B17001_001E', 'B17001_002E', 'B17001_001M', 'B17001_002M', 'poverty_pct']
    table = data[cols].rename(columns={'NAME': 'State', 'year': 'Year', 'B17001_001E': 'Poverty-status universe',
        'B17001_002E': 'Below-poverty count', 'B17001_001M': 'Universe count MOE (90%)',
        'B17001_002M': 'Below-poverty count MOE (90%)', 'poverty_pct': 'Derived poverty percent (no MOE provided)'})
    html.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>ACS poverty data table</title></head><body>\n'
        '<h1>ACS 1-Year poverty data by state and year</h1><p>Below-poverty count divided by poverty-status universe × 100. '
        'Published 90% margins of error apply to counts, not the derived percentage.</p>\n'
        + table.to_html(index=False, border=1, na_rep='Not available') + '\n</body></html>', encoding='utf-8')
    desc = ('Small multiples: one line panel for each state (' + ', '.join(states) + '). '
      + 'Each panel shows ' + ', '.join(map(str, years)) + ' ACS 1-Year poverty percentages on the same 0 to '
      + str(axis_top) + ' percent y-axis. Points are connected only for consecutive available years; '
      + 'consult the adjacent table for exact estimates and published count margins of error. '
      + 'Differences are descriptive, not significance-tested.')
    alt.write_text(desc + '\n', encoding='utf-8')
    info = {'source': 'ACS 1-Year Detailed Table B17001', 'dataset_url_pattern': API, 'years': years,
      'states': states, 'denominator': 'B17001_001E', 'numerator': 'B17001_002E',
      'margins_of_error': ['B17001_001M', 'B17001_002M'],
      'rate_moe': 'NOT ESTIMATED; count MOEs are not a ratio MOE', 'shared_y_limits': [0, axis_top],
      'python': sys.version.split()[0], 'pandas': pd.__version__, 'matplotlib': matplotlib.__version__,
      'requests': requests.__version__, 'output_dir': str(output_dir.resolve()),
      'manual_accessibility_verification': 'NOT TESTED', 'input_metadata':source_description(source,input_file),
      'live_api': source=='api'}
    manifest.write_text(json.dumps(info, indent=2), encoding='utf-8')
    return data, info


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--states', default=os.environ.get('SMALL_MULTIPLES_STATES', ','.join(DEFAULT_STATES)))
    p.add_argument('--years', default=os.environ.get('SMALL_MULTIPLES_YEARS', ','.join(map(str, DEFAULT_YEARS))))
    p.add_argument('--output-dir', default=os.environ.get('SMALL_MULTIPLES_OUTPUT_DIR', './small_multiples_outputs'))
    p.add_argument('--source',choices=['api','csv','excel'],default='api')
    p.add_argument('--input-file')
    args = p.parse_args()
    data, info = run([s.strip() for s in args.states.split(',') if s.strip()],
                     [int(y.strip()) for y in args.years.split(',') if y.strip()], args.output_dir,
                     source=args.source,input_file=args.input_file)
    print(f"Saved {len(data)} observations to {info['output_dir']}")

if __name__ == '__main__':
    main()
