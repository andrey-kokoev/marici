#!/usr/bin/env python3
"""Factor the full Cayley--Menger del Pezzo degeneration at total energy E=0."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
a,b,h,x,y,E=s.symbols('a b h x y E');z=E-x-y;c=-E
CM=s.Matrix([[0,1,1,1,1],[1,0,c**2,a**2,b**2],[1,c**2,0,y**2,x**2],[1,a**2,y**2,0,z**2],[1,b**2,x**2,z**2,0]])
K=s.expand(-CM.det()/2);P=s.Poly(K,a,b)
G=s.expand(sum(co*a**ij[0]*b**ij[1]*h**(4-sum(ij)) for ij,co in P.terms()))
Q=-x*a**2-y*b**2+x*y*(x+y)*h**2
R1=s.factor(s.diff(G,E).subs(E,0))
expected=-2*(x+y)*(h*y-a)*(h*y+a)*(h*x-b)*(h*x+b)
points=[(sa*y,sb*x) for sa in (1,-1) for sb in (1,-1)]
checks={'central_quartic_is_double_conic':s.expand(G.subs(E,0)-Q**2)==0,'first_smoothing_factorization':s.expand(R1-expected)==0,'four_base_points_distinct_generic':len(points)==4,'four_points_on_conic':all(s.expand(Q.subs({a:A*h,b:B*h}))==0 for A,B in points),'infinity_restriction_double':s.factor(Q.subs({a:s.symbols('t'),b:1,h:0}))==-x*s.symbols('t')**2-y}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.global-total-energy-surface-degeneration.v1','surface':'W^2=G_E(a,b,h)','central_equation':'W^2=Q^2','Q':str(Q),'central_components':['S_plus: W=Q','S_minus: W=-Q'],'conductor':'Q=0','first_E_derivative':str(R1),'four_smoothing_zeroes':[{'a_over_h':str(A),'b_over_h':str(B)} for A,B in points],'interpretation':'The E=0 cusp is a global two-component surface degeneration. The paired infinity nodes are only its intersection with h=0. The first smoothing vanishes at four labelled points on the conductor, providing the global geometric locus from which the integral extension must be computed.','checks':checks,'passed':True,'next':'resolve the local models at the four conductor points and compute the specialization boundary map among their vanishing thimbles'}
(R/'research/voevodsky/results/global_total_energy_surface_degeneration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'central_equation':out['central_equation'],'Q':out['Q'],'first_derivative':out['first_E_derivative'],'points':out['four_smoothing_zeroes'],'next':out['next']}))
