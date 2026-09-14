#!/usr/bin/env python3
"""Test four one-wall primitives in the coupled twisted Hermite image."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text());a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};K=s.sympify(data['K0'],locals=L)
qs=[b+c+1,a+c+1,b+c+2,a+c+2];names=['g1','g2','s23','s31'];P=s.prod(qs);vq=[-1,1,-1,1]
N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);N=s.expand(N23*qs[3]**3-N31*qs[2]**3)
def V(f):return s.diff(f,a)-s.diff(f,b)
def Op(i,k):
 qi=qs[i];h=s.expand((P/qi)*k)
 other=sum(s.expand(P/qj)*vq[j] for j,qj in enumerate(qs) if j!=i)
 return s.expand(K*qi*V(h)-s.Rational(3,2)*h*V(K)*qi-2*h*K*vq[i]-3*k*K*qi*other)
mons=[a**i*b**j*c**(d-i-j) for d in range(11) for i in range(d+1) for j in range(d-i+1)]
def vec(poly,p):
 return {e:(int(x.p)%p)*pow(int(x.q),-1,p)%p for e,x in s.Poly(poly,a,b,c,domain=s.QQ).terms() if x}
def add(v,basis,p,insert):
 while v:
  z=max(v)
  if z not in basis:
   if not insert:return False,v
   inv=pow(v[z],-1,p);v={e:x*inv%p for e,x in v.items()};basis[z]=v;return True,{}
  t=v[z]
  for e,x in basis[z].items():
   y=(v.get(e,0)-t*x)%p
   if y:v[e]=y
   else:v.pop(e,None)
 return True,{}
rows=[]
for prime in (32003,32009):
 basis={}
 for i in range(4):
  for m in mons:add(vec(Op(i,m),prime),basis,prime,True)
 ok,res=add(vec(N,prime),basis,prime,False)
 rpoly=sum(coef*a**exp[0]*b**exp[1]*c**exp[2] for exp,coef in res.items())
 valuations={}
 for name,q in zip(names,qs):
  cur=s.Poly(rpoly,a,b,c,modulus=prime);div=s.Poly(q,a,b,c,modulus=prime);v=0
  while v<3:
   quo,remain=s.div(cur,div)
   if not remain.is_zero:break
   cur=quo;v+=1
  valuations[name]=v
 rows.append({'prime':prime,'columns':4*len(mons),'rank':len(basis),'target_in_image':ok,'residual_support':len(res),'residual_cubic_wall_valuations':valuations,'residual_is_simple_pole_numerator':all(v>=2 for v in valuations.values())})
checks={'four_components':len(qs)==4,'divisibility_ansatz_used':True,'degree_bound_ten':len(mons)==286,'two_prime_agreement':len({(r['rank'],r['target_in_image']) for r in rows})==1,'target_outside_image':all(not r['target_in_image'] for r in rows),'residual_not_simple':all(not r['residual_is_simple_pole_numerator'] for r in rows),'stable_zero_valuations':len({tuple(r['residual_cubic_wall_valuations'].values()) for r in rows})==1}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-four-component-Hermite-image.v1','primitive_rule':'the q_i-lowering primitive coefficient h_i must be divisible by every other cubic wall q_j to avoid creating q_j^-4','ansatz':'h_i=(P/q_i)k_i, deg(k_i)<=10','components':names,'modular_tests':rows,'result':'The actual odd numerator remains outside the four-component polynomial twisted-Hermite image at both primes, and its stable quotient residual is not logarithmic/simple: its valuations on (g1,g2,s23,s31) are (1,0,1,0), below the required two on every cubic wall.','qualification':'This rejects polynomial k_i through the homogeneity-forced degree ten for this primitive ansatz. Rational coefficients with additional controlled divisors or a larger multi-stage primitive complex are not excluded.','next_task':'Record the polynomial filtered-lowering obstruction and decide whether to enlarge the admissible primitive coefficient ring; such an enlargement requires a source-boundary and no-new-support proof.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_four_component_Hermite_image.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'rows':rows,'next':out['next_task']}))
