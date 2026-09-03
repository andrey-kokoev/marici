#!/usr/bin/env python3
"""Test the first unverified cutoff for tau nonvanishing."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r7=g['construct'](7);r8=g['construct'](8);assert all(k in r8 and r8[k]==v for k,v in r7.items());complete=g['g'];complete['exact_rows'].__globals__['A']=8;m=complete['configure'](P);_,cols=m.column_packet();basis={}
def proj(v):return v.numerator*pow(v.denominator,-1,P)%P
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
for row in r8.values():reduce({grade*len(cols)+cols[label]:proj(v) for (grade,label),v in row.items()},True)
base=(0,1,1,1,1,1,(0,0));res=reduce({len(cols)+cols[base]:3});assert res
out={'schema':'marici.benincasa.cosmology-rees-tau-q8-falsifier.v1','A7_to_A8_relation_inclusion_exact':True,'A8_relation_rank_mod101':len(basis),'A8_tau_residual_nnz_mod101':len(res),'A8_tau_nonzero':True,'tested_prime':101,'uniform_nonvanishing_proved':False,'exact_residual':'tau remains nonzero at the first new cutoff Q8, but finite modular survival supplies no all-A dual functional','next_acceptance_test':'construct a cutoff-independent dual cocycle evaluating nontrivially on tau and vanishing on all three parametric relation families','passed':True};(R/'cosmology_rees_tau_q8_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
