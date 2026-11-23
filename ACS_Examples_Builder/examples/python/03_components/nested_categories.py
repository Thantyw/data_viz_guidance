"""C02-STAT-001: hierarchical/disjoint B03002 categories and overlapping DP03 coverage.
API mode pulls both tables; CSV/Excel/DataFrame need the joined ACS-named columns.
"""
import argparse
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common.data_input import load,require_numeric,InputError
from common.publish import prepare,table_and_manifest
import requests,os
B=[f'B03002_{i:03d}E' for i in list(range(1,10))+[12]]
D=[f'DP03_{i:04d}E' for i in range(95,100)]

def _profile(year,states):
    url=f'https://api.census.gov/data/{year}/acs/acs1/profile'
    params={'get':','.join(['NAME']+D),'for':'state:*'}
    if os.getenv('CENSUS_API_KEY'):params['key']=os.environ['CENSUS_API_KEY']
    try:r=requests.get(url,params=params,timeout=60)
    except requests.RequestException as e:raise RuntimeError(f'Census profile request failed: {type(e).__name__}') from None
    if not r.ok:raise RuntimeError(f'Census profile API HTTP {r.status_code}')
    try:payload=r.json()
    except ValueError as e:raise RuntimeError('Census profile response not valid JSON') from e
    if not isinstance(payload,list) or len(payload)<2:raise InputError('Empty profile response')
    f=pd.DataFrame(payload[1:],columns=payload[0]);f=f[f.NAME.isin(states)].copy()
    return f[['NAME',*D]]

def run(source='csv',input_file=None,dataframe=None,output_dir='./nested_outputs',states=None,year=2024):
    if year!=2024:raise InputError('This demonstration is documented for 2024 ACS 1-Year; verify variable definitions for other years')
    if source=='api':
        frame=load('api',year=year,variables=B,states=states)
        frame=frame.merge(_profile(year,frame.NAME.tolist()),on='NAME',how='inner',validate='one_to_one')
        if states and {s.strip().lower() for s in states}!={n.lower() for n in frame.NAME}: raise InputError('DP03 profile did not return every selected state')
    else:frame=load(source,input_file,dataframe,year=year,states=states)
    frame=require_numeric(frame,B+D)
    if frame.NAME.duplicated().any():raise InputError('Duplicate geography rows')
    if (frame['B03002_001E']<=0).any() or (frame['DP03_0095E']<=0).any():raise InputError('Denominators must be positive')
    partition=frame.B03002_002E+frame.B03002_012E
    nested=frame[[f'B03002_{i:03d}E' for i in range(3,10)]].sum(axis=1)
    if not (partition==frame.B03002_001E).all():raise InputError('B03002: origin groups do not sum to total')
    if not (nested==frame.B03002_002E).all():raise InputError('B03002: nested non-Hispanic subgroups do not reconcile')
    if not (frame.DP03_0096E+frame.DP03_0099E==frame.DP03_0095E).all():raise InputError('DP03: insured plus uninsured must equal universe')
    if not ((frame.DP03_0097E<=frame.DP03_0096E)&(frame.DP03_0098E<=frame.DP03_0096E)).all():raise InputError('DP03: coverage types must be contained within insured')
    # Private + public is NOT a valid partition. Derive intersection only when category arithmetic is interpretable.
    frame['not_hispanic_pct']=100*frame.B03002_002E/frame.B03002_001E
    frame['hispanic_pct']=100*frame.B03002_012E/frame.B03002_001E
    frame['private_pct']=100*frame.DP03_0097E/frame.DP03_0095E
    frame['public_pct']=100*frame.DP03_0098E/frame.DP03_0095E
    frame['overlap_count_derived']=frame.DP03_0097E+frame.DP03_0098E-frame.DP03_0096E
    if (frame.overlap_count_derived<0).any():raise InputError('DP03 published values imply negative coverage overlap; inspect definitions')
    out=prepare(output_dir);frame=frame.sort_values('NAME')
    fig,ax=plt.subplots(figsize=(10,max(4,0.65*len(frame)+2)))
    y=np.arange(len(frame));ax.barh(y,frame.not_hispanic_pct,label='Not Hispanic or Latino',color='#174C67')
    ax.barh(y,frame.hispanic_pct,left=frame.not_hispanic_pct,label='Hispanic or Latino',color='#DCA34A',hatch='//')
    ax.set_yticks(y,frame.NAME);ax.set_xlim(0,100);ax.set_xlabel('Percent of total population')
    ax.set_title('Mutually exclusive Hispanic-origin groups (nested race categories not plotted)',loc='left');ax.legend(loc='lower right')
    fig.tight_layout();fig.savefig(out/'nested_b03002.png',dpi=160);fig.savefig(out/'nested_b03002.svg');plt.close(fig)
    fig,ax=plt.subplots(figsize=(10,max(4,0.65*len(frame)+2)))
    ax.barh(y-.18,frame.private_pct,height=.32,color='#174C67',label='Private coverage')
    ax.barh(y+.18,frame.public_pct,height=.32,color='#B96C2A',hatch='//',label='Public coverage')
    ax.set_yticks(y,frame.NAME);ax.set_xlim(left=0);ax.set_xlabel('Percent of civilian noninstitutionalized population')
    ax.set_title('Non-mutually exclusive health insurance coverage types',loc='left');ax.legend();fig.tight_layout()
    fig.savefig(out/'nested_dp03.png',dpi=160);fig.savefig(out/'nested_dp03.svg');plt.close(fig)
    description=('Two ACS 2024 category examples. B03002 Hispanic and non-Hispanic groups are mutually exclusive, '
                 'with race subgroups nested within non-Hispanic origin. DP03 private and public health insurance '
                 'categories overlap and must not be stacked or summed as a partition. See the data table for values and denominators.')
    names=['NAME','B03002_001E','not_hispanic_pct','hispanic_pct','DP03_0095E','private_pct','public_pct','overlap_count_derived']
    table_and_manifest(frame[names],out,'nested_categories_acs',title='ACS nested and overlapping categories',description=description,metadata={'source_mode':source,'year':year,'states':frame.NAME.tolist(),'category_relationships':['B03002: partition with nested subgroups','DP03: overlapping coverage types'],'api_key_saved':False})
    return frame

def main():
    p=argparse.ArgumentParser();p.add_argument('--source',choices=['api','csv','excel'],default='csv');p.add_argument('--input-file');p.add_argument('--out',default='./nested_outputs');p.add_argument('--states',default='Florida,Georgia');p.add_argument('--year',type=int,default=2024)
    a=p.parse_args();run(a.source,a.input_file,output_dir=a.out,states=a.states.split(','),year=a.year)
if __name__=='__main__':main()
