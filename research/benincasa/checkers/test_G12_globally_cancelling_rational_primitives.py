#!/usr/bin/env python3
"""VC1: minimal existing-support rational primitives with global quartic cancellation."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text());a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};K=s.sympify(data['K0'],locals=L)
qs=[b+c+1,a+c+1,b+c+2,a+c+2];names=['g1','g2','s23','s31'];P=s.expand(s.prod(qs));vq=[-1,1,-1,1]
N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);N=s.expand(N23*qs[3]**3-N31*qs[2]**3);target=s.expand(N*P)
def V(f):return s.diff(f,a)-s.diff(f,b)
cof=[s.expand(s.prod(qs[j] for j in range(4) if j!=i)) for i in range(4)]
def Op(i,h):
 qi=qs[i]
 return s.expand(K*qi*P*V(h)-s.Rational(3,2)*h*V(K)*qi*P-2*h*K*vq[i]*P-3*h*K*qi*sum(vq[j]*cof[j] for j in range(4) if j!=i))
mons=[a**i*b**j*c**(d-i-j) for d in range(14) for i in range(d+1) for j in range(d-i+1)]
def vec(poly,p):return {e:(int(x.p)%p)*pow(int(x.q),-1,p)%p for e,x in s.Poly(poly,a,b,c,domain=s.QQ).terms() if x}
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
 ok,res=add(vec(target,prime),basis,prime,False)
 rows.append({'prime':prime,'columns':4*len(mons),'rank':len(basis),'target_in_image':ok,'residual_support':len(res),'residual_pivot':None if ok else list(max(res))})
checks={'minimal_budget_existing_support_only':set(names)=={'g1','g2','s23','s31'},'degree_thirteen_forced':s.Poly(target,a,b,c).total_degree()-8==13,'ansatz_dimension_560':len(mons)==560,'two_prime_stability':len({(r['rank'],r['target_in_image'],r['residual_support']) for r in rows})==1,'target_outside_image':all(not r['target_in_image'] for r in rows)}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-globally-cancelling-rational-primitives.v1','prospective_action':'VC1_controlled_rational_primitive_enlargement','pole_budget':'one additional simple pole, only on existing cubic walls; use common quartic denominator and require cancellation globally','common_test_denominator':'target denominator times P=g1*g2*s23*s31','target_numerator':'N_odd*P','primitive_components':names,'polynomial_coefficient_degree_bound':13,'modular_tests':rows,'VC1_resolution':'-+','reason':'Even after allowing fourth-order contributions from individual primitives to cancel only in the global sum, the target remains outside the enlarged image at both primes with the same rank and residual profile.','implication':{'premise':'VC1 bounded existing-support rational image test returns nonmembership at two primes','relation':'entails','conclusion':'VC1_pole_budget_obstructed'},'remaining_scope':'This rejects the frozen minimal rational pole budget. It does not reject higher pole budgets or new-support rational coefficients, which would require a new prospectively priced action.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_globally_cancelling_rational_primitives.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'VC1':out['VC1_resolution'],'rows':rows,'conclusion':out['implication']['conclusion']}))
