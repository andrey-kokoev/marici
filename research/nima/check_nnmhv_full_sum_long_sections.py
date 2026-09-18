#!/usr/bin/env python3
"""Longer exact sections for cross-family NNMHV full-sum tail diagnostics."""
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]]);families={'quadratic_cubic':(lambda j:j*j+j+1,lambda j:j**3+2*j+1),'quadratic_quartic':(lambda j:j*j+2*j+2,lambda j:j**4+j+1),'cubic_quadratic':(lambda j:j**3+j+1,lambda j:j*j+3*j+1)}
def val(n,lf,tf):
 lam,til,x=momentum_conserving_kinematics([(1,lf(j)) for j in range(1,n+1)],[(1,tf(j)) for j in range(1,n-1)]);hs=[h for h in compile_nnmhv_histories(n) if h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3];cache={};total=s.Integer(0)
 for h in hs:
  if h.outer_pair not in cache:cache[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
  o=cache[h.outer_pair];st=terminal_r_state(h);i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))[1];w=o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0);total+=o['prefactor']*i['prefactor']*w**4
 return float(s.N(s.factor(total/angle(lam,2,3)**4),16))
def fit(rows):
 best=None
 for k in range(10,501):
  a=k/100;xs=[r['n']**(-a) for r in rows];ys=[r['value'] for r in rows];N=len(rows);sx=sum(xs);sy=sum(ys);sxx=sum(x*x for x in xs);sxy=sum(x*y for x,y in zip(xs,ys));d=N*sxx-sx*sx;c=(N*sxy-sx*sy)/d;L=(sy-c*sx)/N;rss=sum((y-L-c*x)**2 for x,y in zip(xs,ys));q=(rss,a,L,c)
  if best is None or q<best:best=q
 return {'alpha':best[1],'L':best[2],'c':best[3],'rss':best[0]}
old=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-cross-family-exponents.json').read_text());qold=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-extended-sections.json').read_text());outf={};t0=time.time()
for name,(lf,tf) in families.items():
 if name=='quadratic_cubic':base=[{'n':r['n'],'value':r['normalized_value']} for r in qold['sections']]
 else:base=old['extended_families'][name]['sections']
 extra=[{'n':n,'value':val(n,lf,tf)} for n in range(17,23)];rows=base+extra;outf[name]={'new_sections':extra,'late_profile_n16_to22':fit([r for r in rows if r['n']>=16])}
alphas=[d['late_profile_n16_to22']['alpha'] for d in outf.values()];limits=[d['late_profile_n16_to22']['L'] for d in outf.values()];checks={'all_families_reach_n22':all(d['new_sections'][-1]['n']==22 for d in outf.values()),'late_exponents_positive':all(a>0 for a in alphas),'late_exponents_cluster_within_point_one':max(alphas)-min(alphas)<0.1,'limits_still_nonuniversal':max(limits)/min(limits)>2}
out={'schema':'marici.nima.nnmhv-full-sum-long-sections.v1','families':outf,'late_alpha_mean':sum(alphas)/3,'late_alpha_spread':max(alphas)-min(alphas),'late_limit_ratio':max(limits)/min(limits),'checks':checks,'passed':all(checks.values()),'elapsed_seconds':time.time()-t0,'scope':'Support-reduced exact sums through n=22; nonlinear tail fits remain exploratory.'}
p=ROOT/'research/nima/results/nnmhv-full-sum-long-sections.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
