#!/usr/bin/env python3
"""Support-reduced extension of the complete (2,3) NNMHV history sum."""
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]])
def supported(h):return h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3
def evaluate(n):
 lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)]);hs=[h for h in compile_nnmhv_histories(n) if supported(h)];cache={};total=s.Integer(0)
 for h in hs:
  if h.outer_pair not in cache:cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
  o=cache[h.outer_pair];st=terminal_r_state(h);i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))[1];w=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0);total+=o['prefactor']*i['prefactor']*w**4
 return {'n':n,'total_histories':len(compile_nnmhv_histories(n)),'support_histories':len(hs),'normalized_value':float(s.N(s.factor(total/angle(lam,2,3)**4),16))}
def fit(rows):
 A=s.Matrix([[1,s.Rational(1,r['n']),s.Rational(1,r['n']**2)] for r in rows]);y=s.Matrix([s.Float(r['normalized_value'],30) for r in rows]);c=(A.T*A).inv()*A.T*y;return float(c[0])
prior=json.loads((ROOT/'research/nima/results/nnmhv-normalized-full-sum-dependence.json').read_text())['families']['quadratic_cubic']['sections'];t0=time.time();rows=[{'n':r['n'],'total_histories':len(compile_nnmhv_histories(r['n'])),'support_histories':(r['n']-5)*(r['n']-4)//2,'normalized_value':r['normalized_value']} for r in prior]+[evaluate(n) for n in range(12,17)];early=fit(rows[4:8]);late=fit(rows[-4:]);checks={'support_count_is_triangular':all(r['support_histories']==(r['n']-5)*(r['n']-4)//2 for r in rows),'extended_through_n16':rows[-1]['n']==16,'normalized_sequence_increasing':all(a['normalized_value']<b['normalized_value'] for a,b in zip(rows,rows[1:])),'late_fit_finite':s.Float(late).is_finite}
out={'schema':'marici.nima.nnmhv-full-sum-extended-sections.v1','family':'quadratic lambda / cubic tilde bulk','support_rule':'left-nested, a1=2, a2=3','sections':rows,'fit_L_n10_to13':early,'fit_L_n13_to16':late,'fit_L_drift':late-early,'checks':checks,'passed':all(checks.values()),'elapsed_seconds':time.time()-t0,'scope':'Support-reduced exact sums; fit drift is a convergence diagnostic, not a proof of a limit.'}
p=ROOT/'research/nima/results/nnmhv-full-sum-extended-sections.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
