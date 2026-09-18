#!/usr/bin/env python3
"""First finite-section pilot for a complete NNMHV history sum."""
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]])
def section(n):
 # Coherent bulk sequence; only the final two anti-spinors close each polygon.
 lams=[(1,j*j+j+1) for j in range(1,n+1)];tildes=[(1,j**3+2*j+1) for j in range(1,n-1)];return momentum_conserving_kinematics(lams,tildes)
def evaluate(n):
 lam,til,x=section(n);histories=compile_nnmhv_histories(n);outer_cache={};total=s.Integer(0);nonzero=0;t0=time.time()
 for h in histories:
  if h.outer_pair not in outer_cache:outer_cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
  o=outer_cache[h.outer_pair];state=terminal_r_state(h);im=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,state.lower_spinor.vertices),transport_spinor(lam,x,state.upper_spinor.vertices))[1]
  # Coefficient product_A eta_2^A eta_3^A in the degree-eight ratio function.
  wedge=s.factor(o['xi_coefficients'].get(2,0)*im['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*im['xi_coefficients'].get(2,0));term=s.factor(o['prefactor']*im['prefactor']*wedge**4)
  if term!=0:nonzero+=1
  total=s.factor(total+term)
 return {'n':n,'history_count':len(histories),'nonzero_history_contributions':nonzero,'coefficient':str(total),'coefficient_float':float(total.evalf()),'elapsed_seconds':time.time()-t0}
rows=[evaluate(n) for n in range(6,10)];checks={'all_sections_use_complete_history_set':all(r['history_count']==s.binomial(r['n']-2,4)+s.binomial(r['n']-3,4) for r in rows),'more_than_one_history_from_n7':all(r['history_count']>1 for r in rows[1:]),'full_sums_nonzero':all(r['coefficient']!='0' for r in rows),'multiple_histories_contribute_by_n9':rows[-1]['nonzero_history_contributions']>1}
out={'schema':'marici.nima.nnmhv-full-history-sum-pilot.v1','observable':'coefficient product_A eta_2^A eta_3^A of P_n^{N2MHV}','kinematics':'lambda_i=(1,i^2+i+1), tilde_lambda_i=(1,i^3+2i+1) for coherent bulk i<=n-2; final two tilde spinors fixed by momentum closure','sections':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite-section pilot; no asymptotic fit or universality claim.'}
p=ROOT/'research/nima/results/nnmhv-full-history-sum-pilot.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
