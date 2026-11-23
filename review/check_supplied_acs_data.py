import json
from pathlib import Path
import numpy as np,pandas as pd
p=Path(__file__).resolve().parents[1]/'assets/examples'
read=lambda k,n:pd.read_csv(p/k/n)
checks={}
u=read('uncertainty','uncertainty_acs.csv')
checks['uncertainty_endpoints']=bool(np.allclose(u.ci_lower_90,u.B19013_001E-u.B19013_001M) and np.allclose(u.ci_upper_90,u.B19013_001E+u.B19013_001M))
s=read('scatter_plot','scatter_plot_data.csv');b=read('bubble_chart','bubble_chart_data.csv');checks['scatter_bubble_identical_values']=s.equals(b)
checks['poverty_percentage']=bool(np.allclose(s.poverty_percent,100*s.below_poverty_count/s.poverty_universe))
checks['income_cross_page_consistency']=bool(np.allclose(s.set_index('state').median_household_income_usd,u.set_index('NAME').B19013_001E))
l=read('line_graph','linegraph_acs_income_2024_dollars.csv');m=json.loads((p/'line_graph/linegraph_manifest.json').read_text())
factors={y:np.prod([v for k,v in m['adjacent_factors'].items() if int(k)>=y]) for y in range(2021,2025)}
checks['line_inflation_multiplication']=bool(np.allclose(l.to_2024_factor,l.year.map(factors)) and np.allclose(l.estimate_2024_dollars,l.estimate_release_dollars*l.to_2024_factor) and np.allclose(l.moe_90_2024_dollars,l.moe_90_release_dollars*l.to_2024_factor))
checks['line_2024_income_matches']=bool(np.allclose(l[l.year==2024].set_index('state').estimate_2024_dollars,s.set_index('state').median_household_income_usd))
a=read('area_chart','area_chart_data.csv');checks['area_intervals']=bool(np.allclose(a.lower_90_display,np.maximum(0,a.persons_below_poverty-a.moe_90)) and np.allclose(a.upper_90,a.persons_below_poverty+a.moe_90))
checks['area_2024_count_matches_scatter']=bool(np.allclose(a[a.year==2024].set_index('state').persons_below_poverty,s.set_index('state').loc[a[a.year==2024].state].below_poverty_count))
st=read('stacked_area','stacked_area_acs_data.csv');checks['stacked_population_partition']=bool((st.B01001_001E==st.B01001_002E+st.B01001_026E).all() and np.allclose(st.male_pct+st.female_pct,100))
py=read('population_pyramid','population_pyramid_acs.csv');checks['pyramid_population_partition']=bool(py['count'].sum()==23372215 and np.isclose(py.percent_of_total.sum(),100) and np.allclose(py.percent_of_total,100*py['count']/py.denominator))
checks['pyramid_sex_totals']=bool(py.groupby('sex')['count'].sum().to_dict()=={'Male':11488598,'Female':11883617})
n=read('nested_categories','nested_categories_acs.csv');checks['nested_origin_percentage_partition']=bool(np.allclose(n.not_hispanic_pct+n.hispanic_pct,100))
checks['nested_coverage_percent_ranges']=bool(n[['private_pct','public_pct']].ge(0).all().all() and n[['private_pct','public_pct']].le(100).all().all())
box=read('boxplot','boxplot_county_data.csv');summ=read('boxplot','boxplot_summary.csv');ok=True
for _,r in summ.iterrows():
 v=box.loc[(box.state_name==r.state)&box.valid_income,'median_income'].to_numpy();q=np.quantile(v,[.25,.5,.75],method='linear');iqr=q[2]-q[0];inc=v[(v>=q[0]-1.5*iqr)&(v<=q[2]+1.5*iqr)]
 ok &= len(v)==r.valid_counties and np.allclose(q,[r.q1,r['median'],r.q3]) and np.allclose([inc.min(),inc.max()],[r.whisker_low,r.whisker_high]) and len(v)-len(inc)==r.outlier_count
checks['boxplot_county_summaries']=bool(ok)
h=read('histogram','histogram_county_data.csv');bins=read('histogram','histogram_bins.csv');ok=True
for name,d in bins.groupby('state',sort=False):
 edges=list(d.bin_lower_inclusive)+[d.bin_upper_exclusive_except_last.iloc[-1]];v=h.loc[(h.state_name==name)&h.valid_income,'median_income']
 counts,_=np.histogram(v,bins=edges);ok &= np.array_equal(counts,d.county_count) and counts.sum()==len(v)
checks['histogram_counts_and_boundaries']=bool(ok)
checks['boxplot_histogram_shared_counties_match']=bool(box[box.GEOID.isin(h.GEOID)].sort_values('GEOID').reset_index(drop=True).equals(h.sort_values('GEOID').reset_index(drop=True)))
report={'checks':checks,'passed':all(checks.values()),'limitations':['Nested export omits raw B03002 children and raw DP03 coverage counts: full raw category and intersection checks cannot be independently rerun from saved CSV.','Checks establish arithmetic consistency of supplied files; no fresh API query or independent source audit performed.','Chart appearance, published-page accessibility, and R parity require separate review.']}
(Path(__file__).resolve().parent/'ACS_DATA_CHECKS.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
assert all(checks.values())
