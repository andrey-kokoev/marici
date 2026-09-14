#!/usr/bin/env python3
"""Test the forced scalar Hermite equation for polynomial h through the required degree."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};K=s.sympify(data['K0'],locals=L)
g1=b+c+1;g2=a+c+1;g3=a+b+1;s23=b+c+2;s31=a+c+2;P=s.expand(g1*g2*s23*s31)
N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);N=s.expand(N23*s31**3-N31*s23**3)
def V(f):return s.diff(f,a)-s.diff(f,b)
cofactor=s.expand(-g2*s23*s31 + g1*s23*s31 - g1*g2*s31 + g1*g2*s23)
def Op(h):return s.expand(K*P*V(h)-s.Rational(3,2)*h*V(K)*P-2*h*K*cofactor)
mons=[a**i*b**j*c**k for total in range(11) for i in range(total+1) for j in range(total-i+1) for k in [total-i-j]]
def vec(poly,p):
 d={}
 for exp,coef in s.Poly(poly,a,b,c,domain=s.QQ).terms():d[exp]=(int(coef.p)%p)*pow(int(coef.q),-1,p)%p
 return {k:v for k,v in d.items() if v}
def reduce_add(v,basis,p,add):
 while v:
  pivot=max(v)
  if pivot not in basis:
   if not add:return False,v
   inv=pow(v[pivot],-1,p);v={k:(x*inv)%p for k,x in v.items()};basis[pivot]=v;return True,{}
  z=v[pivot];row=basis[pivot]
  for k,x in row.items():
   nv=(v.get(k,0)-z*x)%p
   if nv:v[k]=nv
   elif k in v:del v[k]
 return True,{}
rows=[]
for prime in (32003,32009):
 basis={}
 for m in mons:reduce_add(vec(Op(m),prime),basis,prime,True)
 ok,res=reduce_add(vec(N,prime),basis,prime,False)
 rows.append({'prime':prime,'ansatz_dimension':len(mons),'operator_rank':len(basis),'target_in_image':ok,'residual_pivot':None if ok else list(max(res)),'residual_support_size':len(res)})
checks={'degree_ten_forced_by_homogeneity':s.Poly(N,a,b,c).total_degree()-7==10,'ansatz_dimension_286':len(mons)==286,'two_primes':len(rows)==2,'target_outside_image_both_primes':all(not r['target_in_image'] for r in rows),'stable_rank':len({r['operator_rank'] for r in rows})==1}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-scalar-polynomial-Hermite-equation.v1','operator':'L(h)=K0*P*V(h)-(3/2)h*V(K0)*P-2h*K0*(-P/g1+P/g2-P/s23+P/s31)','P':'g1*g2*s23*s31','V':'partial_a-partial_b','target':'N23*s31^3-N31*s23^3','homogeneous_degree_bound':10,'modular_image_tests':rows,'polynomial_solution_exists':False,'result':'The actual odd numerator is outside the scalar twisted-divergence image for every polynomial h of the only degree allowed by homogeneity, independently at two primes.','scope':'Rejects polynomial h for the uniform one-step primitive with K0 exponent 3/2 and all four cubic-wall exponents lowered to two. Rational h with controlled poles and multi-stage primitives are not excluded.','next_task':'Allow a direct sum of primitives lowering one cubic divisor at a time, each still tangent to B12 and g3, and solve the resulting four-component sparse image problem.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_scalar_polynomial_Hermite_equation.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'rows':rows,'polynomial_solution':False}))
