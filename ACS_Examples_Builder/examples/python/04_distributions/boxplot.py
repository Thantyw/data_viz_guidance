"""GB-DATA-001 portable Boxplot: distributions of county median-income estimates.

Usage: python boxplot.py --source csv --input-file counties.csv --states Florida Georgia
Optional: --source api (uses CENSUS_API_KEY, if configured).
Requires: pandas numpy matplotlib requests openpyxl (Excel mode only).
"""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common.county_income import load_counties, output_paths, record_manifest, table_html


def summarize_county_distribution(df:pd.DataFrame, states:list[str]):
    stats=[]
    for state in states:
        vals=df.loc[(df.state_name==state)&df.valid_income,'median_income'].astype(float).to_numpy()
        if len(vals)<4: raise ValueError(f'{state}: need at least 4 valid county observations; found {len(vals)}')
        q1,med,q3=np.percentile(vals,[25,50,75]); iqr=q3-q1
        low=q1-1.5*iqr; high=q3+1.5*iqr
        whisker_low=float(min(v for v in vals if v>=low))
        whisker_high=float(max(v for v in vals if v<=high))
        stats.append({'state':state,'valid_counties':int(len(vals)), 'q1':float(q1),'median':float(med),
                      'q3':float(q3),'whisker_low':whisker_low,'whisker_high':whisker_high,
                      'outlier_count':int(((vals<whisker_low)|(vals>whisker_high)).sum())})
    return pd.DataFrame(stats)


def make_figure(df,states,year,out):
    vals=[df.loc[(df.state_name==s)&df.valid_income,'median_income'].astype(float).to_numpy() for s in states]
    fig,ax=plt.subplots(figsize=(max(9,1.5*len(states)+4),5.7))
    ax.boxplot(vals,orientation='horizontal',tick_labels=states,whis=1.5,patch_artist=True,
               boxprops={'facecolor':'#BDD7E7','edgecolor':'#153D58','linewidth':1.4},
               medianprops={'color':'#80350C','linewidth':2.5},
               whiskerprops={'color':'#153D58'},capprops={'color':'#153D58'},
               flierprops={'marker':'o','markersize':5,'markerfacecolor':'white','markeredgecolor':'#153D58'})
    ax.set(xlabel=f'County median household-income estimate ({year} inflation-adjusted USD)',
           ylabel='State',title='Distributions of county median household-income estimates')
    ax.grid(axis='x',alpha=.20);ax.set_axisbelow(True)
    fig.text(.12,.02,'Each point summarizes a county estimate; not household-level incomes. Whiskers: 1.5×IQR; circles: outlier counties.',fontsize=8)
    fig.tight_layout(rect=(0,.07,1,1))
    fig.savefig(out/'boxplot_acs.png',dpi=180)
    fig.savefig(out/'boxplot_acs.svg');plt.close(fig)


def run(source='api', *, states=None, year=2024, input_file=None, dataframe=None,
        output_dir='./boxplot_outputs',api_key=None,request_get=None):
    states=list(dict.fromkeys(states or ['Florida','Georgia','Texas','Virginia']))
    df=load_counties(source,states=states,year=year,input_file=input_file,dataframe=dataframe,
                     api_key=api_key or '',request_get=request_get)
    summary=summarize_county_distribution(df,states)
    assert (summary.q1<=summary['median']).all() and (summary['median']<=summary.q3).all()
    out=output_paths(output_dir)
    df.to_csv(out/'boxplot_county_data.csv',index=False)
    summary.to_csv(out/'boxplot_summary.csv',index=False)
    make_figure(df,states,year,out)
    description=(f'County median household-income estimates for {", ".join(states)} in {year} ACS 5-year. '
                 'Boxes show the 25th–75th percentiles, central lines the medians, and whiskers the most extreme '
                 'counties within 1.5 times the interquartile range; circles identify outlier counties. '
                 'One county is one observation. These are not individual household-income distributions.')
    (out/'boxplot_alt_text_draft.txt').write_text(description+'\n',encoding='utf-8')
    (out/'boxplot_data_table.html').write_text(table_html('County income boxplot data',description,
         [('Distribution summaries',summary),('County estimate records and published 90% MOEs',
           df[['NAME','state_name','GEOID','median_income','moe_90','valid_income','valid_moe']])]),encoding='utf-8')
    return record_manifest(out,'boxplot',source=source,input_file=input_file,year=year,states=states,
        rows=len(df),valid=int(df.valid_income.sum()),extra={'whisker_rule':'1.5*IQR; outliers shown',
        'published_MOE_use':'retained for individual county estimates; boxplot quartiles are not uncertainty limits'})


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',choices=['api','csv','excel'],default='api')
    p.add_argument('--input-file',default=None)
    p.add_argument('--states',nargs='+',default=['Florida','Georgia','Texas','Virginia'])
    p.add_argument('--year',type=int,default=2024)
    p.add_argument('--output-dir',default='./boxplot_outputs')
    a=p.parse_args()
    result=run(source=a.source,input_file=a.input_file,states=a.states,year=a.year,
               output_dir=a.output_dir,api_key=os.getenv('CENSUS_API_KEY',''))
    print('Saved',result['valid_county_rows'],'valid county estimates to',Path(a.output_dir).resolve())

if __name__=='__main__':main()
