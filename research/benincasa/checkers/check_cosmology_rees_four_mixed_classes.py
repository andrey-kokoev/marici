#!/usr/bin/env python3
"""Extract four mixed residual classes completing the D=26 quotient."""
import contextlib,io,json,runpy
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_levelwise_residual_classes.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(src))
g=h['g'];B=h['B'];ins=g['ins'];labels=g['labels'];cols=g['cols'];P=101
def image(v,lev):
 r={}
 for j,c in v.items():
  if labels[j][0]!=lev:continue
  for m,a in cols[j].items():r[m]=(r.get(m,0)+c*a)%P
 return {m:a for m,a in r.items() if a}
mixed=[]
for v in g['null']:
 if ins(B,dict(v)):
  im0=image(v,0);im1=image(v,1);cancel=all((im0.get(k,0)+im1.get(k,0))%P==0 for k in set(im0)|set(im1))
  mixed.append({'terms':[{'input':list(labels[j]),'coefficient':c} for j,c in sorted(v.items())],'level_support':[any(labels[j][0]==q and c for j,c in v.items()) for q in (0,1)],'level_output_support_size':[len(im0),len(im1)],'nonzero_cross_level_cancellation':bool(im0) and bool(im1) and cancel})
out={'schema':'marici.benincasa.cosmology-rees-four-mixed-classes.v1','prime':P,'D':26,'mixed_class_count':len(mixed),'all_bilevel':all(all(x['level_support']) for x in mixed),'all_outputs_cancel_nontrivially':all(x['nonzero_cross_level_cancellation'] for x in mixed),'completed_quotient_rank':6+len(mixed),'representatives':mixed};R=HERE.parents[1]/'results';(R/'cosmology_rees_four_mixed_classes.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['mixed_class_count','all_bilevel','all_outputs_cancel_nontrivially','completed_quotient_rank']},indent=2))
