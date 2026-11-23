"""Common output files; accessibility outputs are drafts pending manual review."""
import json,sys
from html import escape
from pathlib import Path
import pandas as pd

def prepare(output_dir):
    p=Path(output_dir).expanduser().resolve();p.mkdir(parents=True,exist_ok=True)
    return p

def table_and_manifest(frame,out,stem,*,title,description,metadata):
    frame.to_csv(out/f'{stem}.csv',index=False)
    tab=frame.to_html(index=False,escape=True,border=0)
    tab=tab.replace('<th>','<th scope="col">')
    doc=('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title></head><body><main><h1>'+escape(title)+'</h1><p>'+escape(description)+'</p>'+tab+'</main></body></html>')
    (out/f'{stem}.html').write_text(doc,encoding='utf-8')
    (out/f'{stem}_alt_text_draft.txt').write_text(description+'\n',encoding='utf-8')
    info={**metadata,'note':'Manual Section 508/WCAG testing required; statistical results require source review.','python':sys.version.split()[0]}
    (out/f'{stem}_manifest.json').write_text(json.dumps(info,indent=2,default=str),encoding='utf-8')
