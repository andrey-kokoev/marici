#!/usr/bin/env python3
"""Test the prolonged gradient-symbol map on all g of degree at most three."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g0=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r=g0['construct'](4);lev=(1,1,1,1,1)
def mod(v):return v.numerator*pow(v.denominator,-1,P)%P
def reducer(basis,row,insert=False):
 while row:
  q=min(row);x=row[q]
  if q not in basis:
   if insert:
    z=pow(x,-1,P);basis[q]={k:v*z%P for k,v in row.items() if v*z%P}
   return row
  for k,v in basis[q].items():row[k]=(row.get(k,0)-x*v)%P
  row={k:v for k,v in row.items() if v}
 return {}
mult={}
for (kind,label),row in r.items():
 if kind=='shift2' and label[0] in ('K_multiplication','q_multiplication'):reducer(mult,{k:mod(v) for k,v in row.items()},True)
kerbasis={};tests=[]
for d in range(4):
 for i in range(d+1):
  j=d-i;row={}
  for src,c in [(r[('shift2',('twisted_derivative',0,lev,0,(i,j+1)))],2),(r[('shift2',('twisted_derivative',0,lev,1,(i+1,j)))],1)]:
   for k,v in src.items():row[k]=(row.get(k,0)+c*mod(v))%P
  row={k:v for k,v in row.items() if v};nf=reducer(mult,dict(row));new=reducer(kerbasis,dict(nf),True);ind=bool(new);tests.append({'g_exp':[i,j],'normal_nnz':len(nf),'normal_lead':repr(min(nf)),'independent_pivot':repr(min(new)) if new else None,'independent':ind})
assert len(kerbasis)==len(tests)==10
out={'schema':'marici.benincasa.cosmology-rees-prolongation-parametric-kernel.v1','prime':P,'cutoff':4,'g_degree_max':3,'domain_dimension':len(tests),'image_rank':len(kerbasis),'kernel_dimension':len(tests)-len(kerbasis),'multiplication_image_rank':len(mult),'tests':tests,'disposition':'the first prolonged map is injective on every polynomial g of degree at most three','scope':'finite Q4/mod-101 evidence only; no arbitrary-degree theorem','next_test':'repeat at Q10 for g degree at most nine and identify a leading-coordinate triangularity pattern that can be proved for all degrees','passed':True};(R/'cosmology_rees_prolongation_parametric_kernel.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
