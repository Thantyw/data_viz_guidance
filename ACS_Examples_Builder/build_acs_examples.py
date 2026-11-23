#!/usr/bin/env python3
"""Build 11 ACS chart examples from Census API using the supplied public chart implementations.

No synthetic estimates are ever written as Census figures. API credentials are read from
CENSUS_API_KEY only, and never written to manifest files or displayed in logs.
"""
from __future__ import annotations
import argparse, csv, json, os, shutil, subprocess, sys, re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE / 'examples' / 'python'
DEFAULT_STATES = 'Florida,Georgia,Texas,Virginia'

def sanitize(text):
    """Prevent API key leakage in public notebook logs."""
    if not text: return ''
    secret = os.getenv('CENSUS_API_KEY','')
    if secret: text = text.replace(secret, '[REDACTED]')
    return re.sub(r'(?i)([?&]key=)[^&\s\"\']+', r'\1[REDACTED]', text)


# Page keys and image names are deliberately explicit; original Census images remain distinct.
JOBS = [
 ('uncertainty', 'Visualizing Uncertainty', '03_components/uncertainty.py',
  ['--source','api','--year','2024','--states','Florida,Georgia,Texas,Virginia'], ['uncertainty_acs.png']),
 ('nested_categories', 'Nested or Non-Mutually Exclusive Categories', '03_components/nested_categories.py',
  ['--source','api','--year','2024','--states','Florida,Georgia'], ['nested_b03002.png','nested_dp03.png']),
 ('line_graph', 'Line Graph', '02_time_series/line_graph.py',
  ['--source','api','--years','2021,2022,2023,2024','--states','Florida,Georgia,Texas,Virginia'], ['linegraph_acs_income.png']),
 ('area_chart', 'Area Chart', '02_time_series/area_chart.py',
  ['--source','api','--years','2021,2022,2023,2024','--states','Florida,Georgia,Virginia'], ['area_chart.png']),
 ('bubble_chart', 'Bubble Chart', '01_bubble_scatter/bubble_chart.py',
  ['--source','api','--states','Florida,Georgia,Texas,Virginia'], ['bubble_chart.png']),
 ('scatter_plot', 'Scatter Plot', '01_bubble_scatter/scatter_plot.py',
  ['--source','api','--states','Florida,Georgia,Texas,Virginia'], ['scatter_plot.png']),
 ('small_multiples', 'Small Multiples', '02_time_series/small_multiples.py',
  ['--source','api','--years','2021,2022,2023,2024','--states','Florida,Georgia,Texas,Virginia'], ['small_multiples.png']),
 ('population_pyramid', 'Population Pyramid', '03_components/population_pyramid.py',
  ['--source','api','--year','2024','--states','Florida','--mode','percent'], ['population_pyramid_acs.png']),
 ('boxplot', 'Boxplot', '04_distributions/boxplot.py',
  ['--source','api','--year','2024','--states','Florida','Georgia','Texas','Virginia'], ['boxplot.png']),
 ('stacked_area', 'Stacked Area Chart', '02_time_series/stacked_area.py',
  ['--source','api','--years','2021,2022,2023,2024','--states','Florida,Georgia'], ['stacked_area.png']),
 ('histogram', 'Histogram', '04_distributions/histogram.py',
  ['--source','api','--year','2024','--states','Florida','Georgia','Virginia'], ['histogram.png']),
]

OUTPUT_FLAGS = {'uncertainty':'--out','nested_categories':'--out','line_graph':'--out',
 'area_chart':'--out','bubble_chart':'--out','scatter_plot':'--out','small_multiples':'--output-dir',
 'population_pyramid':'--out','boxplot':'--output-dir','stacked_area':'--out','histogram':'--output-dir'}

DATASET = {
 'uncertainty':'2024 ACS 1-Year; B19013 state estimates and 90% MOEs',
 'nested_categories':'2024 ACS 1-Year; B03002 state categories plus ACS profile DP03 coverage',
 'line_graph':'2021–2024 ACS 1-Year; B19013 state median income, adjusted to 2024 dollars',
 'area_chart':'2021–2024 ACS 1-Year; B17001 state poverty counts',
 'bubble_chart':'2024 ACS 1-Year; B19013, B17001, B01003 state estimates',
 'scatter_plot':'2024 ACS 1-Year; B19013 and B17001 state estimates',
 'small_multiples':'2021–2024 ACS 1-Year; B17001 state poverty percentages',
 'population_pyramid':'2024 ACS 1-Year; B01001 state sex-by-age',
 'boxplot':'2020–2024 ACS 5-Year; B19013 county median income estimates',
 'stacked_area':'2021–2024 ACS 1-Year; B01001 state male/female population',
 'histogram':'2020–2024 ACS 5-Year; B19013 county median income estimates',
}

def main(argv=None):
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output-root',default='./acs_generated_examples',help='All resulting files are stored here')
 parser.add_argument('--only',nargs='*',help='Optional page keys to run')
 parser.add_argument('--dry-run',action='store_true',help='Print planned work; do not use API or create figures')
 parser.add_argument('--continue-on-error',action='store_true',help='Run remaining charts if one fails')
 args=parser.parse_args(argv)
 output=Path(args.output_root).expanduser().resolve()
 chosen=set(args.only or [j[0] for j in JOBS]); valid={j[0] for j in JOBS}
 if unknown:=chosen-valid: parser.error('Unknown pages: '+', '.join(sorted(unknown)))
 if not args.dry_run and not os.environ.get('CENSUS_API_KEY','').strip():
  parser.error('Set CENSUS_API_KEY to your own activated key. Do not write it into the notebook or files.')
 if not args.dry_run:
  (output/'outputs').mkdir(parents=True,exist_ok=True)
  (output/'assets'/'examples').mkdir(parents=True,exist_ok=True)
 record=[]
 for key,title,script,flags,expected in JOBS:
  if key not in chosen:continue
  dest=output/'outputs'/key
  cmd=[sys.executable,str(SCRIPTS/script),*flags,OUTPUT_FLAGS[key],str(dest)]
  if args.dry_run:
   print(f'{key}: {DATASET[key]}')
   print('  script:',script)
   print('  expected output:', ', '.join(expected))
   record.append({'key':key,'title':title,'status':'planned','dataset':DATASET[key]})
   continue
  print(f'\n=== {title} — {DATASET[key]} ===', flush=True)
  # Avoid exposing the key in command arguments or logs.
  # Run each chart in its own folder so imports of the chart-specific `common` resolve.
  working_dir = (SCRIPTS / script).parent
  try:
   proc=subprocess.run(cmd,cwd=working_dir,capture_output=True,text=True,timeout=240)
   log=sanitize((proc.stdout or '')+'\n'+(proc.stderr or ''))
   rc=proc.returncode
  except subprocess.TimeoutExpired as exc:
   log=sanitize(f'Timeout after 240 seconds: {exc}')
   rc=124
  except Exception as exc:
   log=sanitize(f'{type(exc).__name__}: {exc}')
   rc=125
  (dest).mkdir(parents=True, exist_ok=True)
  (dest/'execution.log').write_text(log[-15000:],encoding='utf-8')
  if rc:
   lines=[v.strip() for v in log.splitlines() if v.strip()]
   short = next((v for v in reversed(lines) if any(x in v for x in ('Error:', 'Exception:', 'error:', 'HTTP ', 'Traceback'))), None)
   reason=(short or (lines[-1] if lines else f'No process output (code {rc})'))[:350]
   print(f'FAILED [{key}] (exit {rc}): {reason}',flush=True)
   record.append({'key':key,'title':title,'status':'failed','dataset':DATASET[key],
                  'reason':reason,'log_file':f'outputs/{key}/execution.log'})
   if not args.continue_on_error:break
   continue
  images=sorted(dest.glob('*.png'))
  if not images:
   record.append({'key':key,'title':title,'status':'failed','dataset':DATASET[key],
                  'reason':'Script finished without a PNG; inspect output files', 'log_file':f'outputs/{key}/execution.log'})
   if not args.continue_on_error:break
   continue
  print('Generated:',', '.join(p.name for p in images),flush=True)
  for p in dest.iterdir():
   if p.suffix.lower() in ('.png','.svg','.csv','.html','.txt','.json'):
    # Each page has a unique folder to avoid filename collision.
    target=output/'assets'/'examples'/key
    target.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,target/p.name)
  record.append({'key':key,'title':title,'status':'generated_unreviewed',
                 'dataset':DATASET[key],'images':';'.join(p.name for p in images),
                 'note':'Must review data, output captions, and Section 508 prior to publication', 'log_file':f'outputs/{key}/execution.log'})
 if not args.dry_run:
  with (output/'execution_status.csv').open('w',newline='',encoding='utf8') as f:
   fields=['key','title','status','dataset','images','note','reason','log_file'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(record)
  snippets=['# Insert these examples into the matching public Markdown pages',
            '', 'Images are generated from Census API responses only after a successful run.',
            'For GitHub Pages, use Jekyll `relative_url`. For GitHub source preview, use',
            '`../assets/examples/<page>/<image.png>` relative to `visualization_type/` or `component/`.',
            'Review each image and write data-specific alt text before publication.','']
  for row in record:
   if row.get('status')!='generated_unreviewed':continue
   snippets += [f"## {row['title']}", '',DATASET[row['key']], '']
   for fn in row['images'].split(';'):
    path=f"/assets/examples/{row['key']}/{fn}"
    snippets += ["![ACS-based {} example — update description after checking the chart]({{{{ '{}' | relative_url }}}})".format(row["title"],path), '']
   snippets += ['See the corresponding `assets/examples/` directory for the numerical data files.', '']
  (output/'MARKDOWN_IMAGE_SNIPPETS.md').write_text('\n'.join(snippets),encoding='utf8')
  (output/'execution_manifest.json').write_text(json.dumps({'generated_at_utc':datetime.now(timezone.utc).isoformat(),
   'data_source':'U.S. Census Bureau API','all_acs_values_retrieved_at_runtime':True,
   'api_key_saved':False,'records':record},indent=2),encoding='utf8')
  if any(r['status']=='failed' for r in record):return 1
 return 0

if __name__=='__main__':sys.exit(main())
