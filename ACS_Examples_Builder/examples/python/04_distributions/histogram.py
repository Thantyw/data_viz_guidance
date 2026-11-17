"""GB-DATA-001 portable Histogram: county median-income estimates, NOT household incomes.

Usage: python histogram.py --source csv --input-file counties.csv --states Florida Georgia --bin-width 10000
Supports optional Census API mode and in-memory Pandas DataFrame via run().
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


def build_histogram_bins(df,states,bin_width):
    valid=df.loc[df.valid_income].copy()
    if not isinstance(bin_width,(int,float)) or not np.isfinite(bin_width) or bin_width<=0:
        raise ValueError('bin_width must be a positive finite amount in dollars')
    for state in states:
        n=int(((valid.state_name==state)).sum())
        if n<5:raise ValueError(f'{state}: need at least five valid county estimates; got {n}')
    low=np.floor(valid.median_income.min()/bin_width)*bin_width
    high=np.ceil(valid.median_income.max()/bin_width)*bin_width
    if high<=low:high=low+bin_width
    edges=np.arange(low,high+bin_width*1.01,bin_width,dtype=float)
    if len(edges)>150 or len(edges)<2:raise ValueError('Invalid bin count; choose a different width')
    bins=[]
    for state in states:
        vals=valid.loc[valid.state_name==state,'median_income'].to_numpy(float)
        counts,_=np.histogram(vals,bins=edges)
        if int(counts.sum())!=len(vals):raise AssertionError('Bin counts must reconcile to valid county observations')
        for i,count in enumerate(counts):
            bins.append({'state':state,'bin_lower_inclusive':edges[i],
                         'bin_upper_exclusive_except_last':edges[i+1], 'county_count':int(count)})
    return valid,edges,pd.DataFrame(bins)


def make_figure(valid,states,year,edges,out):
    fig,axes=plt.subplots(len(states),1,figsize=(10,3.0*len(states)),sharex=True,squeeze=False,layout='constrained')
    for ax,state in zip(axes[:,0],states):
        vals=valid.loc[valid.state_name==state,'median_income'].to_numpy(float)
        ax.hist(vals,bins=edges,color='#BDD7E7',edgecolor='#153D58',linewidth=.9)
        ax.set_ylabel('Number of counties')
        ax.set_title(f'{state} (n={len(vals)} counties)',loc='left')
        ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    axes[-1,0].set_xlabel(f'County median household-income estimate ({year} inflation-adjusted USD)')
    fig.suptitle('Distribution of county income estimates (not household incomes)')
    fig.savefig(out/'histogram_acs.png',dpi=180)
    fig.savefig(out/'histogram_acs.svg');plt.close(fig)


def run(source='api', *, states=None, year=2024, input_file=None, dataframe=None,
        output_dir='./histogram_outputs',bin_width=10000,api_key=None,request_get=None):
    states=list(dict.fromkeys(states or ['Florida','Georgia','Virginia']))
    if len(states)>6: raise ValueError('Use at most six states for readable histogram panels')
    df=load_counties(source,states=states,year=year,input_file=input_file,dataframe=dataframe,
                     api_key=api_key or '',request_get=request_get)
    valid,edges,bins=build_histogram_bins(df,states,bin_width)
    out=output_paths(output_dir)
    df.to_csv(out/'histogram_county_data.csv',index=False)
    bins.to_csv(out/'histogram_bins.csv',index=False)
    summary=pd.DataFrame([{'state':s,'total_counties':int((df.state_name==s).sum()),
               'valid_counties':int((valid.state_name==s).sum()),
               'excluded_counties':int(((df.state_name==s)&(~df.valid_income)).sum())} for s in states])
    summary.to_csv(out/'histogram_summary.csv',index=False)
    make_figure(valid,states,year,edges,out)
    description=(f'Histograms show counts of counties across {bin_width:,.0f}-dollar-wide bins of county median '
                 f'household-income estimates from {year} ACS 5-year for {", ".join(states)}. '
                 'These are county estimates, not household-level incomes. Shared bin boundaries allow comparisons. '
                 'Published 90% margins of error are available in the county data table.')
    (out/'histogram_alt_text_draft.txt').write_text(description+'\n',encoding='utf-8')
    (out/'histogram_data_table.html').write_text(table_html('County income histogram data',description,
          [('County summary',summary),('Histogram bins',bins),
           ('County records and published 90% MOEs',df[['NAME','state_name','GEOID','median_income','moe_90','valid_income','valid_moe']])]),encoding='utf-8')
    return record_manifest(out,'histogram',source=source,input_file=input_file,year=year,states=states,
        rows=len(df),valid=len(valid),extra={'bin_width_usd':float(bin_width),
        'bin_count_reconciled':True,'common_bins_all_states':True,
        'last_bin_right_endpoint_included':True})


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',choices=['api','csv','excel'],default='api')
    p.add_argument('--input-file',default=None)
    p.add_argument('--states',nargs='+',default=['Florida','Georgia','Virginia'])
    p.add_argument('--year',type=int,default=2024)
    p.add_argument('--bin-width',type=float,default=10000)
    p.add_argument('--output-dir',default='./histogram_outputs')
    a=p.parse_args()
    result=run(source=a.source,input_file=a.input_file,states=a.states,year=a.year,
               bin_width=a.bin_width,output_dir=a.output_dir,api_key=os.getenv('CENSUS_API_KEY',''))
    print('Saved',result['valid_county_rows'],'valid county estimates to',Path(a.output_dir).resolve())

if __name__=='__main__':main()
