#!/usr/bin/env python3
"""VC1b: sparse finite-field test without per-column symbolic expansion."""
import json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text());a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};K=s.sympify(data['K0'],locals=L)
qs=[b+c+1,a+c+1,b+c+2,a+c+2];names=['g1','g2','s23','s31'];P=s.expand(s.prod(qs));vq=[-1,1,-1,1];cof=[s.expand(s.prod(qs[j] for j in range(4) if j!=i)) for i in range(4)]
N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);target=s.expand((N23*qs[3]**3-N31*qs[2]**3)*P);VK=s.diff(K,a)-s.diff(K,b)
A=[s.expand(K*q*P) for q in qs];B=[s.expand(-s.Rational(3,2)*VK*qs[i]*P-2*K*vq[i]*P-3*K*qs[i]*sum(vq[j]*cof[j] for j in range(4) if j!=i)) for i in range(4)]
mons=[(i,j,d-i-j) for d in range(14) for i in range(d+1) for j in range(d-i+1)]
def coeffs(poly,p):return {e:(int(x.p)%p)*pow(int(x.q),-1,p)%p for e,x in s.Poly(poly,a,b,c,domain=s.QQ).terms() if x}
def column(exp,aa,bb,p):
 out={};i,j,k=exp
 for base,coef in bb.items():out[tuple(base[t]+exp[t] for t in range(3))]=(out.get(tuple(base[t]+exp[t] for t in range(3)),0)+coef)%p
 for deriv,fac in (((i-1,j,k),i),((i,j-1,k),-j)):
  if fac:
   for base,coef in aa.items():
    e=tuple(base[t]+deriv[t] for t in range(3));out[e]=(out.get(e,0)+fac*coef)%p
 return {e:x for e,x in out.items() if x}
def add(v,basis,p,insert):
 while v:
  z=max(v)
  if z not in basis:
   if not insert:return False,v
   inv=pow(v[z],-1,p);basis[z]={e:x*inv%p for e,x in v.items()};return True,{}
  t=v[z]
  for e,x in basis[z].items():
   y=(v.get(e,0)-t*x)%p
   if y:v[e]=y
   else:v.pop(e,None)
 return True,{}
rows=[]
for prime in (32003,32009):
 start=time.perf_counter();As=[coeffs(x,prime) for x in A];Bs=[coeffs(x,prime) for x in B];basis={}
 for idx in range(4):
  for exp in mons:add(column(exp,As[idx],Bs[idx],prime),basis,prime,True)
 ok,res=add(coeffs(target,prime),basis,prime,False)
 rows.append({'prime':prime,'columns':4*len(mons),'rank':len(basis),'target_in_image':ok,'residual_support':len(res),'elapsed_seconds':round(time.perf_counter()-start,3)})
stable=len({(r['rank'],r['target_in_image'],r['residual_support']) for r in rows})==1
resolution='++' if all(r['target_in_image'] for r in rows) else '-+'
checks={'sparse_columns_2240':4*len(mons)==2240,'two_primes':len(rows)==2,'stable_profile':stable,'bounded_runtime':all(r['elapsed_seconds']<120 for r in rows)};assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-VC1b-sparse-membership.v1','prospective_action':'VC1b_sparse_finite_field_membership','implementation':'direct sparse monomial shifts for A_i*V(h)+B_i*h; no per-column symbolic expansion','pole_budget':'one additional simple pole on existing cubic walls with global quartic cancellation','tests':rows,'VC1b_resolution':resolution,'implication':{'premise':f'VC1b outcome {resolution}','relation':'entails','conclusion':'VC1_bounded_membership' if resolution=='++' else 'VC1b_sparse_budget_obstructed'},'mathematical_parent_VC1_status':'unresolved' if resolution!='++' else 'advance to exact reconstruction','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_VC1b_sparse_membership.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':resolution,'tests':rows,'parent':out['mathematical_parent_VC1_status']}))
