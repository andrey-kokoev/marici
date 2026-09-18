#!/usr/bin/env python3
"""Search nested-xi and Urep transport conventions against six-point anti-MHV."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r,theta_coefficients,theta_interval
from dual_spinor_kinematics import adjugate2,angle,momentum_conserving_kinematics,x_interval
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes);eps=s.Matrix([[0,1],[-1,0]]);theta=theta_coefficients(lam,6)
_,outer=generalized_r(lam,x,6,(),(2,5),lam[1].T*eps,lam[5].T*eps);ops={'x':lambda m:m,'xt':lambda m:m.T,'adj':adjugate2,'adjt':lambda m:adjugate2(m).T};target=(2,3,4,5)
def sw(xi,left,middle,ket):return s.simplify((xi*x_interval(x,*left)*adjugate2(x_interval(x,*middle))*ket)[0])
# independent anti-MHV component
def sq(a,b):return s.det(s.Matrix.hstack(til[a],til[b]))
pt_sq=s.prod(sq(i,1 if i==6 else i+1) for i in range(1,7));anti=s.factor(sq(1,6)**4/pt_sq);pt_ang=s.prod(angle(lam,i,1 if i==6 else i+1) for i in range(1,7));rows=[]
for f_name,g_name,upper_mode in itertools.product(ops,ops,('eps','direct')):
 F,G=ops[f_name],ops[g_name];bra=lam[6].T*eps;xi=bra*F(x_interval(x,6,5))*G(x_interval(x,5,2));upper_bra=bra*F(x_interval(x,6,2))*G(x_interval(x,2,5));upper_ket=(eps*upper_bra.T if upper_mode=='eps' else upper_bra.T);a,b,anchor=3,5,2
 den=[x_interval(x,a,b).det(),sw(xi,(anchor,a),(a,b),upper_ket),sw(xi,(anchor,a),(a,b),lam[b-1]),sw(xi,(anchor,b),(b,a),lam[a]),sw(xi,(anchor,b),(b,a),lam[a-1])]
 if any(v==0 for v in den):continue
 pref=s.factor(angle(lam,a,a-1)*angle(lam,b,b-1)/s.prod(den));tb=theta_interval(theta,b,anchor);ta=theta_interval(theta,a,anchor);left=xi*x_interval(x,anchor,a)*adjugate2(x_interval(x,a,b));right=xi*x_interval(x,anchor,b)*adjugate2(x_interval(x,b,a));q={i:s.simplify((left*tb.get(i,s.zeros(2,1)))[0]+(right*ta.get(i,s.zeros(2,1)))[0]) for i in set(tb)|set(ta)}
 M=s.Matrix([[lam[i][0] for i in target],[lam[i][1] for i in target],[outer['xi_coefficients'].get(i,0) for i in target],[q.get(i,0) for i in target]]);full=s.factor(outer['prefactor']*pref*M.det()**4/pt_ang);ratio=s.factor(full/anti);rows.append({'prefix_op1':f_name,'prefix_op2':g_name,'upper_ket':upper_mode,'ratio':str(ratio),'exact':ratio==1})
exact=[r for r in rows if r['exact']];checks={'all_nonsingular_candidates_evaluated':len(rows)>0,'unique_exact_nested_convention':len(exact)==1}
out={'schema':'marici.nima.nested-r-transport-convention-search.v1','searched':4*4*2,'nonsingular':len(rows),'exact_conventions':exact,'checks':checks,'passed':all(checks.values()),'scope':'Exact finite search against one degree-16 six-point anti-MHV component with ordinary R convention fixed.'}
p=ROOT/'research/nima/results/nested-r-transport-convention-search.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
