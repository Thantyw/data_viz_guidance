"""Rebuild four reviewed ACS figures from the supplied CSVs, without API access.

Run from any directory: python review/rebuild_reviewed_acs_layouts.py
The notebook's unchanged originals remain in review/evidence/ACS_Actual_Results.
Only layout, labels and common comparison scales are changed; values are retained.
"""
from pathlib import Path
import json
import platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/examples'
plt.rcParams.update({'font.size': 11, 'svg.fonttype': 'none'})

def save(fig, key, stem):
    for extension in ['png', 'svg']:
        fig.savefig(ASSETS/key/f'{stem}.{extension}', dpi=180, facecolor='white')
    plt.close(fig)

def rebuild():
    b = pd.read_csv(ASSETS/'bubble_chart/bubble_chart_data.csv')
    fig, ax = plt.subplots(figsize=(11, 7.5))
    fig.subplots_adjust(left=.11, right=.97, top=.88, bottom=.20)
    area = b.total_population / b.total_population.max() * 1050
    ax.scatter(b.median_household_income_usd, b.poverty_percent, s=area,
               color='#B7D3DF', edgecolor='#174C67', linewidth=1.3)
    offsets = {'Florida':(-12, -23), 'Georgia':(20, -10), 'Texas':(8, 18), 'Virginia':(-16, 15)}
    for _, r in b.iterrows():
        ax.annotate(r.state, (r.median_household_income_usd, r.poverty_percent),
                    xytext=offsets[r.state], textcoords='offset points',
                    ha='right' if r.state in ['Florida', 'Virginia'] else 'left',
                    color='#162C3C', fontsize=11)
    for value in [5_000_000, 15_000_000, 30_000_000]:
        ax.scatter([], [], s=value/b.total_population.max()*1050,
                   color='#B7D3DF', edgecolor='#174C67', label=f'{value/1e6:g} million people')
    ax.legend(title='Bubble area: total population', loc='upper right', labelspacing=1.5, borderpad=1)
    ax.set(xlim=(65000, 97000), ylim=(0, 18), xlabel='Median household income (2024 dollars)',
           ylabel='Below poverty threshold (% of poverty-status universe)',
           title='Income, poverty percentage and population — 2024 ACS 1-Year')
    ax.xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
    ax.grid(axis='y', color='#D5D5D5', linewidth=.6)
    ax.set_axisbelow(True)
    fig.text(.11, .065, 'Source: U.S. Census Bureau, 2024 ACS 1-Year, B19013, B17001 and B01003.\n'
             'Poverty percentage is derived. Published income/count MOEs are in the table; no ratio MOE is calculated.\n'
             'Bubble area is proportional to population. Four state estimates do not establish causation.', fontsize=9)
    save(fig, 'bubble_chart', 'bubble_chart')

    n = pd.read_csv(ASSETS/'nested_categories/nested_categories_acs.csv')
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    fig.subplots_adjust(left=.12, right=.97, top=.78, bottom=.25)
    y = np.arange(len(n))
    ax.barh(y, n.not_hispanic_pct, color='#174C67', label='Not Hispanic or Latino')
    ax.barh(y, n.hispanic_pct, left=n.not_hispanic_pct, color='#E1B66D',
            edgecolor='#513715', hatch='///', label='Hispanic or Latino')
    for i, r in n.iterrows():
        ax.text(r.not_hispanic_pct/2, i, f'{r.not_hispanic_pct:.2f}%',
                color='white', ha='center', va='center', fontweight='bold')
        ax.text(r.not_hispanic_pct+r.hispanic_pct/2, i, f'{r.hispanic_pct:.2f}%',
                color='black', ha='center', va='center', fontweight='bold',
                bbox={'facecolor':'#FBE8C5', 'edgecolor':'none', 'pad':2})
    ax.set(yticks=y, yticklabels=n.NAME, xlim=(0,100), xlabel='Percent of total population',
           title='Hispanic-origin groups form a 100% partition — 2024 ACS 1-Year')
    ax.set_title('')
    fig.suptitle('Hispanic-origin groups form a 100% partition — 2024 ACS 1-Year', y=.96)
    ax.legend(loc='lower left', bbox_to_anchor=(0,1.02), ncol=2, fontsize=10)
    fig.text(.12, .08, 'Source: U.S. Census Bureau, 2024 ACS 1-Year, B03002.\n'
             'Race subgroups nested within the non-Hispanic group are not plotted.\n'
             'Percentages are point estimates; this figure does not show sampling uncertainty.', fontsize=9)
    save(fig, 'nested_categories', 'nested_b03002')

    st = pd.read_csv(ASSETS/'stacked_area/stacked_area_acs_data.csv')
    for name, d in st.groupby('state', sort=True):
        d = d.sort_values('year')
        years = d.year.to_numpy()
        male = d.B01001_002E.to_numpy()/1e6
        female = d.B01001_026E.to_numpy()/1e6
        fig, ax = plt.subplots(figsize=(10, 6.5))
        fig.subplots_adjust(left=.11, right=.97, top=.81, bottom=.24)
        ax.fill_between(years, 0, male, color='#23607B', label='Male')
        ax.fill_between(years, male, male+female, color='#E2B26B', hatch='///',
                        edgecolor='#71512C', linewidth=1, label='Female (hatched)')
        ax.plot(years, male+female, color='#252525', linewidth=1.5, label='Total population')
        ax.set(xlabel='ACS 1-Year release year', ylabel='Estimated population (millions)',
               title=f'{name}: population by sex — 2021–2024 ACS 1-Year',
               xticks=years, xlim=(2021,2024), ylim=(0,25))
        ax.set_title('')
        fig.suptitle(f'{name}: population by sex — 2021–2024 ACS 1-Year', y=.96)
        ax.legend(loc='lower left', bbox_to_anchor=(0,1.02), ncol=3, fontsize=10)
        ax.grid(axis='y', color='#D5D5D5', linewidth=.6)
        ax.set_axisbelow(True)
        fig.text(.11, .075, 'Source: U.S. Census Bureau, ACS 1-Year, B01001, 2021–2024.\n'
                 'Male + female estimates reconcile to total in each year. Both state charts use a 0–25 million scale.\n'
                 'Published sex-category count MOEs are in the table; changes are not significance-tested.', fontsize=9)
        save(fig, 'stacked_area', 'stacked_area_'+name.lower().replace(' ','_'))
    manifest = {
        'data_source':'Supplied November 10, 2026 run; saved CSVs only; no API query',
        'figures_rebuilt': ['bubble_chart/bubble_chart', 'nested_categories/nested_b03002',
                            'stacked_area/stacked_area_florida', 'stacked_area/stacked_area_georgia'],
        'changes':['Separate labels and legends from plotted marks', 'Reserve footer space',
                   'Use shared zero-based population scale for the two stacked-area charts'],
        'data_values_changed':False, 'python':platform.python_version(),
        'pandas':pd.__version__, 'matplotlib':matplotlib.__version__,
        'manual_published_page_accessibility':'not performed'
    }
    (ROOT/'review/ACS_LAYOUT_REVIEW.json').write_text(json.dumps(manifest,indent=2)+'\n')

if __name__ == '__main__':
    rebuild()
