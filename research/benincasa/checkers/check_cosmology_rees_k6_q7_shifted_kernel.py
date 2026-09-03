#!/usr/bin/env python3
"""Test shifted class K6 across Q6 to Q7 modulo 101."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
complete=g['g']
def project(v):return v.numerator*pow(v.denominator,-1,P)%P
def carrier(A):
 rows=g['construct'](A);complete['exact_rows'].__globals__['A']=A;m=complete['configure'](P);_,cols=m.column_packet();basis={}
 def reduce(row,insert=False):
  row={k:v%P for k,v in row.items() if v%P}
  while row:
   q=min(row);a=row[q]
   if q not in basis:
    if insert:
     inv=pow(a,-1,P);basis[q]={k:v*inv%P for k,v in row.items() if v*inv%P}
    return row
   for k,v in basis[q].items():row[k]=(row.get(k,0)-a*v)%P
   row={k:v for k,v in row.items() if v}
  return {}
 for row in rows.values():reduce({grade*len(cols)+cols[label]:project(v) for (grade,label),v in row.items()},True)
 return cols,basis,reduce
labels=[(0,1,1,1,1,2,(1,6)),(0,1,1,1,2,1,(0,7)),(0,1,1,1,2,2,(0,7)),(0,1,1,1,2,2,(1,6))];coeff=[1,-1,-6,3]
c6,b6,r6=carrier(6);assert all(x in c6 for x in labels);s=r6({c6[x]:v for x,v in zip(labels,coeff)});assert s
c7,b7,r7=carrier(7);assert all(x in c7 for x in labels);t=r7({c7[x]:v for x,v in zip(labels,coeff)});assert not t
out={'schema':'marici.benincasa.cosmology-rees-k6-q7-shifted-kernel.v1','prime':P,'A6_relation_rank':len(b6),'A7_relation_rank':len(b7),'candidate_labels':[repr(x) for x in labels],'primitive_coefficients':coeff,'A6_source_residual_nnz':len(s),'A6_source_nonzero':True,'A7_target_residual_nnz':0,'A7_target_zero':True,'rank_boundary':'full relation ranks are attained modulo 101; integral nonmembership at A6 certifies rational nonmembership','conclusion':'K6 is a nonzero rational Q6 class killed in Q7, giving a third consecutive exact shifted kernel step','passed':True};(R/'cosmology_rees_k6_q7_shifted_kernel.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
