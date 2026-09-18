#!/usr/bin/env python3
"""Validate a little-group invariant normalization of a full history sum."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]])
def full_sum(lam,til,n):
 x={1:s.zeros(2)}
 for j in range(1,n+1):x[j+1]=s.simplify(x[j]-lam[j]*til[j].T)
 assert x[n+1]==x[1];cache={};total=s.Integer(0)
 for h in compile_nnmhv_histories(n):
  if h.outer_pair not in cache:cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
  o=cache[h.outer_pair];st=terminal_r_state(h);i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))[1];w=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0);total+=o['prefactor']*i['prefactor']*w**4
 return s.factor(total),s.factor(total/angle(lam,2,3)**4)
n=8;lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)]);base_raw,base_norm=full_sum(lam,til,n);rows=[]
for t2,t3 in ((1,1),(2,1),(1,3),(2,3)):
 lr={j:lam[j] for j in lam};tr={j:til[j] for j in til};lr[2]=t2*lr[2];tr[2]=tr[2]/t2;lr[3]=t3*lr[3];tr[3]=tr[3]/t3;raw,norm=full_sum(lr,tr,n);expected=s.Integer(t2*t3)**4;rows.append({'t2':t2,'t3':t3,'raw_over_base':str(s.factor(raw/base_raw)),'expected_raw_weight':str(expected),'normalized_over_base':str(s.factor(norm/base_norm))})
checks={'raw_coefficient_has_expected_leg_weights':all(r['raw_over_base']==r['expected_raw_weight'] for r in rows),'angle_normalized_coefficient_invariant':all(r['normalized_over_base']=='1' for r in rows),'uses_complete_eight_point_history_sum':len(compile_nnmhv_histories(n))==20}
out={'schema':'marici.nima.nnmhv-full-sum-little-group-normalization.v1','observable_raw':'coefficient product_A eta_2^A eta_3^A','observable_normalized':'raw/<23>^4','base_raw':str(base_raw),'base_normalized':str(base_norm),'rescalings':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact little-group covariance test of the complete eight-point NNMHV history sum.'}
p=ROOT/'research/nima/results/nnmhv-full-sum-little-group-normalization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
