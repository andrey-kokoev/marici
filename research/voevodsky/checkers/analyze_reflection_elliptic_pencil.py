#!/usr/bin/env python3
"""Analyze the elliptic pencil fixed fiberwise by the global a-reflection."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
a,b,h,A,q,x,y,z=s.symbols('a b h A q x y z');c=-(x+y+z)
CM=s.Matrix([[0,1,1,1,1],[1,0,c**2,a**2,b**2],[1,c**2,0,y**2,x**2],[1,a**2,y**2,0,z**2],[1,b**2,x**2,z**2,0]])
K=s.expand(-CM.det()/2); P=s.Poly(K,a,b)
G=s.expand(sum(co*a**ij[0]*b**ij[1]*h**(4-sum(ij)) for ij,co in P.terms()))
g=s.expand(G.subs({b:q,h:1})); Q=s.Poly(g.subs(a**2,A),A)
disc=s.factor(s.discriminant(Q.as_expr(),A))
triangle=(x-y-z)*(x-y+z)*(x+y-z)*(x+y+z)
basefactor=(q-y-z)*(q+y+z)*(q-2*x-y-z)*(q+2*x+y+z)
critical=[y+z,-y-z,2*x+y+z,-2*x-y-z]
squares=[]
for v in critical:
 f=s.factor(g.subs(q,v)); fac=s.factor_list(f)
 squares.append({'q':str(v),'factorization':str(f),'all_exponents_even':all(e%2==0 for _,e in fac[1])})
checks={'quadratic_in_a_squared':Q.degree()==2,'discriminant_factorization':s.factor(disc-triangle*basefactor)==0,'four_critical_values':len(set(map(str,critical)))==4,'all_four_fibers_split_as_squares':all(r['all_exponents_even'] for r in squares),'paired_types':s.factor(g.subs(q,critical[0])-g.subs(q,critical[1]))==0 and s.factor(g.subs(q,critical[2])-g.subs(q,critical[3]))==0}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.reflection-elliptic-pencil.v1','pencil':'lines [b:h] through [1:0:0]','fiber':'W^2=G(a,q,1), a quartic even in a','reflection':'a -> -a, fiberwise elliptic inversion','quadratic_discriminant_in_a2':str(disc),'genericity_factor':str(triangle),'critical_base_values':[str(v) for v in critical],'split_fibers':squares,'geometry':'Each critical fiber is W^2=Q(a^2)^2 and splits into W=+Q and W=-Q. The four component-difference roots have one global fiber relation, explaining the invariant E7 rank three.','checks':checks,'passed':True,'next':'match the source node-to-e6 Gysin center to one split-fiber component difference, then do the same for v_alg'}
(R/'research/voevodsky/results/reflection_elliptic_pencil.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'checks':checks,'critical_values':out['critical_base_values'],'next':out['next']}))
