#!/usr/bin/env python3
"""Sparse mod-101 Q9 tau nonmembership test."""
import contextlib,io,json,runpy,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101;t=time.time()
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r9=g['construct'](9);complete=g['g'];complete['exact_rows'].__globals__['A']=9;m=complete['configure'](P);_,cols=m.column_packet();width=len(cols);basis={}
def proj(v):return v.numerator*pow(v.denominator,-1,P)%P
def reduce(row,insert=False):
 while row:
  q=min(row);a=row[q]
  b=basis.get(q)
  if b is None:
   if insert:
    z=pow(a,-1,P);basis[q]={k:v*z%P for k,v in row.items() if v*z%P}
   return row
  for k,v in b.items():
   x=(row.get(k,0)-a*v)%P
   if x:row[k]=x
   else:row.pop(k,None)
 return {}
for row in r9.values():reduce({grade*width+cols[label]:proj(v) for (grade,label),v in row.items() if proj(v)},True)
base=(0,1,1,1,1,1,(0,0));res=reduce({width+cols[base]:3});out={'schema':'marici.benincasa.cosmology-rees-tau-q9.v1','prime':P,'relation_rows':len(r9),'relation_rank':len(basis),'tau_residual_nnz':len(res),'tau_nonzero':bool(res),'elapsed_seconds':time.time()-t,'passed':bool(res)};assert res;(R/'cosmology_rees_tau_q9.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
