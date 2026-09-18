#!/usr/bin/env python3
"""Exhaust terminal-ket lowering patterns in the ordinary R denominator."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import adjugate2,angle,momentum_conserving_kinematics,x_interval
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes);_,meta=generalized_r(lam,x,6,(),(2,5),lam[1].T,lam[5].T)
eps=s.Matrix([[0,1],[-1,0]]);a,b,n=2,5,6;xi=lam[n].T;scale=s.Rational(-16,77);five_pref=s.Rational(1,14852791800)
def sw(left,middle,ket):return s.simplify((xi*x_interval(x,*left)*adjugate2(x_interval(x,*middle))*ket)[0])
kets=(lam[b],lam[b-1],lam[a],lam[a-1]);chains=(((n,a),(a,b)),((n,a),(a,b)),((n,b),(b,a)),((n,b),(b,a)));rows=[]
for mask in itertools.product((0,1),repeat=4):
 vals=[sw(*chains[i],eps*kets[i] if mask[i] else kets[i]) for i in range(4)];pref=s.factor(angle(lam,a,a-1)*angle(lam,b,b-1)/(x_interval(x,a,b).det()*s.prod(vals)));ratio=s.factor(pref*scale**4/five_pref);rows.append({'lower_mask':list(mask),'ratio':str(ratio),'exact':ratio==1,'sandwiches':[str(v) for v in vals]})
exact=[r for r in rows if r['exact']]
checks={'all_sixteen_patterns_tested':len(rows)==16,'unique_exact_pattern':len(exact)==1}
out={'schema':'marici.nima.dual-r-terminal-ket-conventions.v1','ket_order':['b','b-1','a','a-1'],'exact_patterns':exact,'patterns':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact exhaustive terminal-ket lowering test with fixed fermionic convention and original x-adjugate chain.'}
p=ROOT/'research/nima/results/dual-r-terminal-ket-conventions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'exact_patterns':exact,'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
