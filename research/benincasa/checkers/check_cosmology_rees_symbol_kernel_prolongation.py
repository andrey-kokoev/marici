#!/usr/bin/env python3
"""Reduce the first gradient-symbol syzygy against multiplication images."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r=g['construct'](4);lev=(1,1,1,1,1);a=r[('shift2',('twisted_derivative',0,lev,0,(0,1)))];b=r[('shift2',('twisted_derivative',0,lev,1,(1,0)))]
def mod(v):return v.numerator*pow(v.denominator,-1,P)%P
target={}
for row,c in [(a,2),(b,1)]:
 for k,v in row.items():target[k]=(target.get(k,0)+c*mod(v))%P
target={k:v for k,v in target.items() if v};basis={}
def reduce(row,insert=False):
 while row:
  q=min(row);x=row[q]
  if q not in basis:
   if insert:
    z=pow(x,-1,P);basis[q]={k:v*z%P for k,v in row.items() if v*z%P}
   return row
  for k,v in basis[q].items():row[k]=(row.get(k,0)-x*v)%P
  row={k:v for k,v in row.items() if v}
 return {}
for (kind,label),row in r.items():
 if kind=='shift2' and label[0] in ('K_multiplication','q_multiplication'):reduce({k:mod(v) for k,v in row.items()},True)
res=reduce(dict(target));assert res
out={'schema':'marici.benincasa.cosmology-rees-symbol-kernel-prolongation.v1','field_prime':P,'symbol_input':'g=1 with derivative inputs (2Y,X) at k=0 and all q levels 1','highest_dK_terms_cancel':True,'multiplication_image_rank_Q4_shift2':len(basis),'full_combination_nnz':len(target),'residual_nnz_after_K_q_reduction':len(res),'first_prolongation_zero':False,'disposition':'the primitive gradient-symbol syzygy does not lift through the lower-order operator modulo admitted K/q multiplication images','scope':'g=1 at Q4 shift2 only; no injectivity theorem for arbitrary g','next_test':'parameterize monomial g, compute the induced residual family, and test whether its leading map has a polynomial kernel','passed':True};(R/'cosmology_rees_symbol_kernel_prolongation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
