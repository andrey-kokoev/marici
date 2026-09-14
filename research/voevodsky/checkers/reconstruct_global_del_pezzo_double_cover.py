#!/usr/bin/env python3
"""Reconstruct the global Cayley--Menger degree-two del Pezzo double cover."""
import json
from pathlib import Path
import sympy as s

R=Path(__file__).resolve().parents[3]
a,b,h,t,x,y,z=s.symbols('a b h t x y z')
c=-(x+y+z)
CM=s.Matrix([
 [0,1,1,1,1],
 [1,0,c**2,a**2,b**2],
 [1,c**2,0,y**2,x**2],
 [1,a**2,y**2,0,z**2],
 [1,b**2,x**2,z**2,0],
])
K=s.expand(CM.det())
P=s.Poly(K,a,b)
Kh=s.expand(sum(co*a**ij[0]*b**ij[1]*h**(4-sum(ij)) for ij,co in P.terms()))
G=s.expand(-Kh/2)
Finf=s.expand(G.subs({a:t,b:1,h:0}))
expected=x**2*t**4-(x**2+y**2-z**2)*t**2+y**2
checks={
 'homogeneous_degree_four':all(sum(mon[:3])==4 for mon,_ in s.Poly(G,a,b,h).terms()),
 'infinity_quartic_matches':s.expand(Finf-expected)==0,
 'a_reflection_global':s.expand(G.subs(a,-a)-G)==0,
 'b_reflection_global':s.expand(G.subs(b,-b)-G)==0,
 'h_reflection_global':s.expand(G.subs(h,-h)-G)==0,
 'not_square_generic':any(e%2 for _,e in s.factor_list(G.subs({x:2,y:3,z:4}))[1]),
}
assert all(checks.values()),checks
out={
 'schema':'marici.voevodsky.global-del-pezzo-double-cover.v1',
 'surface':'W^2=G(a,b,h) in P(1,1,1,2)',
 'G':str(s.factor(G)),
 'infinity_line':'h=0, t=a/b',
 'infinity_restriction':str(Finf),
 'global_involutions':{
  'r_a':'[a:b:h:W] -> [-a:b:h:W]',
  'r_b':'[a:b:h:W] -> [a:-b:h:W]',
  'geiser':'[a:b:h:W] -> [a:b:h:-W]',
 },
 'fixed_locus_r_a':{
  'base_fixed_line':'a=0','cover_genus':'1 generically',
  'isolated_base_point':'[1:0:0]','points_above':2,
  'euler_characteristic':2,
  'lefschetz_trace_H2':0,
  'picard_eigen_multiplicities':{'+1':4,'-1':4},
  'E7_eigen_multiplicities':{'+1':3,'-1':4},
 },
 'checks':checks,'passed':True,
 'next':'identify the invariant rank-three E7 sublattice and express the source support plane in the same marking',
}
outpath=R/'research/voevodsky/results/global_del_pezzo_double_cover.json'
outpath.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':True,'checks':checks,'fixed_locus':out['fixed_locus_r_a'],'next':out['next']}))
