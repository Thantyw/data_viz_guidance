"""Visualizing uncertainty: 2024 ACS 1-Year B19013 estimate ± published 90% MOE.
Supports --source api|csv|excel; run(source='dataframe', dataframe=your_df).
"""
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common.data_input import load,require_numeric,InputError
from common.publish import prepare,table_and_manifest

VARS=['B19013_001E','B19013_001M']
def run(source='csv',input_file=None,dataframe=None,output_dir='./uncertainty_outputs',states=None,year=2024):
    if year!=2024: raise InputError('This example is documented for 2024 ACS 1-Year; verify metadata before changing year')
    frame=load(source,input_file,dataframe,year=year,variables=VARS,states=states)
    frame=require_numeric(frame,VARS,allow_zero=True)
    if (frame['B19013_001E']<=0).any(): raise InputError('Income estimates must be strictly positive')
    if frame.NAME.duplicated().any(): raise InputError('Expected one record per geography')
    frame=frame.sort_values('NAME').copy()
    frame['ci_lower_90']=frame.B19013_001E-frame.B19013_001M
    frame['ci_upper_90']=frame.B19013_001E+frame.B19013_001M
    assert ((frame.ci_lower_90<=frame.B19013_001E)&(frame.B19013_001E<=frame.ci_upper_90)).all()
    out=prepare(output_dir)
    fig,ax=plt.subplots(figsize=(10,max(4,0.47*len(frame)+2)))
    yy=np.arange(len(frame))
    ax.errorbar(frame.B19013_001E,yy,xerr=frame.B19013_001M,fmt='o',color='#174C67',ecolor='#333333',capsize=4)
    ax.set_yticks(yy,frame.NAME);ax.set_xlabel('Median household income (2024 inflation-adjusted dollars)')
    ax.set_title('2024 ACS: median household income with 90% margins of error',loc='left')
    ax.grid(axis='x',alpha=.25);fig.tight_layout()
    fig.savefig(out/'uncertainty_acs.png',dpi=160);fig.savefig(out/'uncertainty_acs.svg');plt.close(fig)
    desc=(f'Dot-and-whisker chart of {len(frame)} geographies, showing 2024 ACS B19013 median household income '
          'and its published 90% margin of error. Each horizontal interval is estimate plus or minus MOE; '
          'consult the accompanying table for exact values. Intervals alone do not establish significance.')
    table_and_manifest(frame[['NAME',*VARS,'ci_lower_90','ci_upper_90']],out,'uncertainty_acs',title='ACS income estimates and intervals',description=desc,metadata={'source_mode':source,'year':year,'states':frame.NAME.tolist(),'variables':VARS,'confidence_level':'90%','api_key_saved':False})
    return frame

def main():
    p=argparse.ArgumentParser();p.add_argument('--source',choices=['api','csv','excel'],default='csv');p.add_argument('--input-file');p.add_argument('--out',default='./uncertainty_outputs');p.add_argument('--states',default='Florida,Georgia');p.add_argument('--year',type=int,default=2024)
    a=p.parse_args();run(a.source,a.input_file,output_dir=a.out,states=a.states.split(','),year=a.year)
if __name__=='__main__':main()
