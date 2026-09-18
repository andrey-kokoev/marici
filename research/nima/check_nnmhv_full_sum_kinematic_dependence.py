#!/usr/bin/env python3
"""Compare full NNMHV history-sum finite sections across coherent families."""
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]])
families={'quadratic_cubic':(lambda j:j*j+j+1,lambda j:j**3+2*j+1),'quadratic_quartic':(lambda j:j*j+2*j+2,lambda j:j**4+j+1),'cubic_quadratic':(lambda j:j**3+j+1,lambda j:j*j+3*j+1)}
def value(n,lf,tf):
 lam,til,x=momentum_conserving_kinematics([(1,lf(j)) for j in range(1,n+1)],[(1,tf(j)) for j in range(1,n-1)]);cache={};total=s.Integer(0);nonzero=0
 for h in compile_nnmhv_histories(n):
  if h.outer_pair not in cache:cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
  o=cache[h.outer_pair];st=terminal_r_state(h);i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))[1];w=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0);term=s.factor(o['prefactor']*i['prefactor']*w**4);nonzero+=term!=0;total+=term
 return float(s.N(total,16)),nonzero
def fit(rows):
 # Exact normal equations for L+a/n+b/n^2, reported numerically.
 A=s.Matrix([[1,s.Rational(1,r['n']),s.Rational(1,r['n']**2)] for r in rows[-4:]]);y=s.Matrix([s.Float(r['value'],30) for r in rows[-4:]]);c=(A.T*A).inv()*A.T*y;return [float(v) for v in c]
outrows={};t0=time.time()
for name,(lf,tf) in families.items():
 rows=[]
 for n in range(6,12):
  v,nz=value(n,lf,tf);rows.append({'n':n,'history_count':len(compile_nnmhv_histories(n)),'nonzero_contributions':nz,'value':v})
 coeff=fit(rows);outrows[name]={'sections':rows,'fit_L_plus_a_over_n_plus_b_over_n2':{'L':coeff[0],'a':coeff[1],'b':coeff[2]}}
limits=[v['fit_L_plus_a_over_n_plus_b_over_n2']['L'] for v in outrows.values()];spread=max(limits)-min(limits);checks={'three_coherent_families':len(outrows)==3,'all_full_sums_nonzero':all(r['value']!=0 for f in outrows.values() for r in f['sections']),'multiple_histories_contribute':all(f['sections'][-1]['nonzero_contributions']>1 for f in outrows.values()),'raw_limit_is_not_universal':spread>0.05}
out={'schema':'marici.nima.nnmhv-full-sum-kinematic-dependence.v1','observable':'coefficient product_A eta_2^A eta_3^A of complete P_n^{N2MHV}','families':outrows,'fitted_limit_spread':spread,'checks':checks,'passed':all(checks.values()),'elapsed_seconds':time.time()-t0,'scope':'Exploratory finite-section fits n=6..11; establishes raw-observable kinematic dependence, not convergent asymptotics.'}
p=ROOT/'research/nima/results/nnmhv-full-sum-kinematic-dependence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
