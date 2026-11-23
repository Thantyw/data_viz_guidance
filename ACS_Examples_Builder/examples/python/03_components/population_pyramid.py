"""Portable ACS B01001 age-sex population pyramid; supports API, CSV, Excel and DataFrame."""
import argparse
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common.data_input import load,require_numeric,InputError
from common.publish import prepare,table_and_manifest
BINS=[('0–4',[3]),('5–9',[4]),('10–14',[5]),('15–19',[6,7]),('20–24',[8,9,10]),('25–29',[11]),('30–34',[12]),('35–39',[13]),('40–44',[14]),('45–49',[15]),('50–54',[16]),('55–59',[17]),('60–64',[18,19]),('65–69',[20,21]),('70–74',[22]),('75–79',[23]),('80–84',[24]),('85+',[25])]
VARS=sorted({f'B01001_{i:03d}E' for k in (1,2,26) for i in [k]}|{f'B01001_{i+off:03d}E' for _,ns in BINS for i in ns for off in (0,24)})
def run(source='csv',input_file=None,dataframe=None,output_dir='./pyramid_outputs',states=None,year=2024,mode='percent'):
    if year!=2024:raise InputError('Demonstration validated for 2024 ACS 1-Year; check metadata for other years')
    if mode not in ('percent','count'):raise InputError('mode must be percent or count')
    frame=load(source,input_file,dataframe,year=year,variables=VARS,states=states)
    frame=require_numeric(frame,VARS)
    if frame.NAME.duplicated().any():raise InputError('Expected unique geographic records')
    records=[];checks=[]
    for _,row in frame.iterrows():
        name=row.NAME;total=row.B01001_001E;male=row.B01001_002E;female=row.B01001_026E
        if total<=0 or male+female!=total:raise InputError(f'{name}: male + female does not equal total')
        sums={'Male':0,'Female':0}
        for label,indices in BINS:
            for sex,offset in [('Male',0),('Female',24)]:
                cnt=int(sum(row[f'B01001_{i+offset:03d}E'] for i in indices))
                sums[sex]+=cnt
                records.append({'NAME':name,'year':year,'age_group':label,'sex':sex,'count':cnt,'percent_of_total':100*cnt/total,'denominator':total})
        if sums['Male']!=male or sums['Female']!=female:raise InputError(f'{name}: age groups do not reconcile to sex totals')
        checks.append({'NAME':name,'total':total,'male':male,'female':female,'age_bins_reconciled':True})
    data=pd.DataFrame(records);out=prepare(output_dir)
    geos=list(data.NAME.unique());fig,axes=plt.subplots(len(geos),1,figsize=(10,5*len(geos)),squeeze=False)
    col='percent_of_total' if mode=='percent' else 'count';mx=float(data[col].max())*1.15
    for ax,name in zip(axes.flat,geos):
        sub=data[data.NAME==name];m=sub[sub.sex=='Male'].set_index('age_group').reindex([b for b,_ in BINS]);f=sub[sub.sex=='Female'].set_index('age_group').reindex([b for b,_ in BINS]);y=np.arange(len(BINS))
        ax.barh(y,-m[col],color='#174C67',label='Male');ax.barh(y,f[col],color='#B96C2A',hatch='//',label='Female')
        ax.set_yticks(y,[b for b,_ in BINS]);ax.set_xlim(-mx,mx);ax.axvline(0,color='black',lw=.8)
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v,p:f'{abs(v):,.1f}%' if mode=='percent' else f'{abs(v):,.0f}'))
        ax.set_title(f'{name} — 2024 ACS population by age and sex');ax.set_xlabel('Percent of total population' if mode=='percent' else 'Population count');ax.legend()
    fig.tight_layout();fig.savefig(out/'population_pyramid_acs.png',dpi=150);fig.savefig(out/'population_pyramid_acs.svg');plt.close(fig)
    desc=('Mirrored population pyramids with male on left and female on right, 18 common age groups (85+ open-ended). '
          'Both sexes share one scale; percentages, when selected, use the entire state population as denominator, '
          'so all male and female cells sum to 100 percent per geography. See accompanying table.')
    table_and_manifest(data,out,'population_pyramid_acs',title='ACS age-sex population table',description=desc,metadata={'source_mode':source,'year':year,'geographies':geos,'mode':mode,'validation':checks,'api_key_saved':False})
    return data

def main():
    p=argparse.ArgumentParser();p.add_argument('--source',choices=['api','csv','excel'],default='csv');p.add_argument('--input-file');p.add_argument('--out',default='./pyramid_outputs');p.add_argument('--states',default='Florida,Georgia');p.add_argument('--year',type=int,default=2024);p.add_argument('--mode',choices=['percent','count'],default='percent');a=p.parse_args()
    run(a.source,a.input_file,output_dir=a.out,states=a.states.split(','),year=a.year,mode=a.mode)
if __name__=='__main__':main()
