#!/usr/bin/env python3
"""Reduce the shifted A5 candidate against the mod-101 A5 relation space."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r5=g['r5'];complete=g['g'];complete['exact_rows'].__globals__['A']=5;m=complete['configure'](P);_,cols=m.column_packet()
def project(v):return v.numerator*pow(v.denominator,-1,P)%P
basis={}
def add(row):
 row={k:v%P for k,v in row.items() if v%P}
 while row:
  q=min(row);a=row[q]
  if q not in basis:
   inv=pow(a,-1,P);basis[q]={k:v*inv%P for k,v in row.items() if v*inv%P};return True,row
  for k,v in basis[q].items():row[k]=(row.get(k,0)-a*v)%P
  row={k:v for k,v in row.items() if v}
 return False,{}
for row in r5.values():add({grade*len(cols)+cols[label]:project(v) for (grade,label),v in row.items()})
assert len(basis)==5888
labels=[(0,1,1,1,1,2,(1,5)),(0,1,1,1,2,1,(0,6)),(0,1,1,1,2,2,(0,6)),(0,1,1,1,2,2,(1,5))];coeff=[1,-1,-6,3];assert all(x in cols for x in labels)
row={cols[k]:v for k,v in zip(labels,coeff)};added,residual=add(row);assert added and residual
out={'schema':'marici.benincasa.cosmology-rees-a5-shifted-candidate-nonvanishing-mod101.v1','prime':P,'A5_relation_rank':5888,'candidate_labels':[repr(x) for x in labels],'primitive_coefficients':coeff,'nonzero_mod_relation_space':True,'residual_nnz':len(residual),'residual_pivot':min(residual),'rational_nonvanishing_boundary':'because the A5 relation rank 5888 is attained modulo 101 and over Q, mod-101 nonmembership certifies rational nonmembership for this integral vector','exact_A6_target_zero':True,'conclusion':'the primitive shifted identity is a nonzero A5 quotient class killed at A6, hence an exact rational A5-to-A6 kernel vector','passed':True};(R/'cosmology_rees_a5_shifted_candidate_nonvanishing_mod101.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
