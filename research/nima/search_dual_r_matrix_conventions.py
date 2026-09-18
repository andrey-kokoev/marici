#!/usr/bin/env python3
"""Finite search for the matrix-index convention realizing R=[five-bracket]."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import theta_coefficients,theta_interval
from dual_spinor_kinematics import adjugate2,angle,momentum_conserving_kinematics,x_interval
from momentum_twistor_constructors import four_bracket
from momentum_twistor_super import SuperTwistor
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes);theta=theta_coefficients(lam,6);eps=s.Matrix([[0,1],[-1,0]])
ops={'x':lambda m:m,'xt':lambda m:m.T,'adj':adjugate2,'adjt':lambda m:adjugate2(m).T};a,b,n=2,5,6
# Independent five-bracket linear form and prefactor.
labels5=(6,1,2,4,5);S={}
for i in range(1,7):
 li=eps*lam[i];S[i]=SuperTwistor(lam[i].col_join(x[i].T*li),{j:s.simplify((li.T*v)[0]) for j,v in theta[i].items() if s.simplify((li.T*v)[0])!=0})
V=tuple(S[i] for i in labels5);qs=[four_bracket(V[(i+1)%5].z,V[(i+2)%5].z,V[(i+3)%5].z,V[(i+4)%5].z) for i in range(5)];fq={}
for q,v in zip(qs,V):
 for j,c in v.chi.items():fq[j]=s.simplify(fq.get(j,0)+q*c)
fq={j:v for j,v in fq.items() if v!=0};fp=s.factor(1/s.prod(qs));ta=theta_interval(theta,a,n);tb=theta_interval(theta,b,n);rows=[]
for op1,op2,bra_lower,ket_lower,x2sign in itertools.product(ops,ops,(0,1),(0,1),(1,-1)):
 bra=lam[n].T*(eps if bra_lower else s.eye(2));F=ops[op1];G=ops[op2]
 left=bra*F(x_interval(x,n,a))*G(x_interval(x,a,b));right=bra*F(x_interval(x,n,b))*G(x_interval(x,b,a));q={j:s.simplify((left*tb.get(j,s.zeros(2,1)))[0]+(right*ta.get(j,s.zeros(2,1)))[0]) for j in set(ta)|set(tb)};q={j:v for j,v in q.items() if v!=0}
 if set(q)!=set(fq):continue
 scales={s.factor(q[j]/fq[j]) for j in q}
 if len(scales)!=1:continue
 scale=next(iter(scales));K=lambda v:(eps*v if ket_lower else v)
 sandwiches=[(bra*F(x_interval(x,n,a))*G(x_interval(x,a,b))*K(lam[b]))[0],(bra*F(x_interval(x,n,a))*G(x_interval(x,a,b))*K(lam[b-1]))[0],(bra*F(x_interval(x,n,b))*G(x_interval(x,b,a))*K(lam[a]))[0],(bra*F(x_interval(x,n,b))*G(x_interval(x,b,a))*K(lam[a-1]))[0]]
 if any(v==0 for v in sandwiches):continue
 pref=s.factor(angle(lam,a,a-1)*angle(lam,b,b-1)/(x2sign*x_interval(x,a,b).det()*s.prod(sandwiches)));ratio=s.factor(pref*scale**4/fp);rows.append({'op1':op1,'op2':op2,'bra_lower':bool(bra_lower),'ket_lower':bool(ket_lower),'x2_sign':x2sign,'xi_scale':str(scale),'ratio':str(ratio),'exact':ratio==1})
exact=[r for r in rows if r['exact']];checks={'search_has_proportional_candidates':len(rows)>0,'unique_exact_convention':len(exact)==1}
out={'schema':'marici.nima.dual-r-matrix-convention-search.v1','searched':4*4*2*2*2,'proportional_candidates':len(rows),'exact_conventions':exact,'checks':checks,'passed':all(checks.values()),'scope':'Finite exact search against R_{6;25}=[6,1,2,4,5] at one rational dual polygon.'}
p=ROOT/'research/nima/results/dual-r-matrix-convention-search.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
