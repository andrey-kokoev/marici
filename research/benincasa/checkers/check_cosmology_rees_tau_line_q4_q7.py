#!/usr/bin/env python3
"""Verify the source-inclusion subsystem on the tau_p line through Q7."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r6=g['construct'](6);r7=g['construct'](7);assert all(k in r7 and r7[k]==v for k,v in r6.items())
complete=g['g'];complete['exact_rows'].__globals__['A']=7;m=complete['configure'](P);_,cols=m.column_packet();basis={}
def project(v):return v.numerator*pow(v.denominator,-1,P)%P
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
for row in r7.values():reduce({grade*len(cols)+cols[label]:project(v) for (grade,label),v in row.items()},True)
base=(0,1,1,1,1,1,(0,0));res=reduce({len(cols)+cols[base]:3});assert res and len(basis)==10245
prior=json.loads((R/'cosmology_rees_ambient_transition_coherence.json').read_text());assert prior['strongest_falsification_attempt']['ambient_six']['residual_nnz']==315
out={'schema':'marici.benincasa.cosmology-rees-tau-line-q4-q7.v1','A6_to_A7_relation_inclusion_exact':True,'A7_relation_rank_mod101':len(basis),'A7_tau_residual_nnz_mod101':len(res),'A7_tau_nonzero':True,'prior_tau_nonzero_cutoffs':[4,5,6],'tau_line_maps':'each source-labelled inclusion fixes the tau representative','restricted_monicity':'a nonzero linear map between the one-dimensional tau spans is injective','result_strength':'coherent monic finite subsystem on span(tau_p) through Q7','scope':'Q4 through Q7 only; no eventual stabilization, global monicity, colimit, or physical readout','passed':True};(R/'cosmology_rees_tau_line_q4_q7.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
