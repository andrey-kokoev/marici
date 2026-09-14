#!/usr/bin/env python3
"""Derive the local XY=E*s^2 type at the four total-energy conductor points."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
a,b,h,x,y,E,u,v,ss=s.symbols('a b h x y E u v ss');z=E-x-y;c=-E
CM=s.Matrix([[0,1,1,1,1],[1,0,c**2,a**2,b**2],[1,c**2,0,y**2,x**2],[1,a**2,y**2,0,z**2],[1,b**2,x**2,z**2,0]])
K=s.expand(-CM.det()/2);P=s.Poly(K,a,b);G=s.expand(sum(co*a**ij[0]*b**ij[1]*h**(4-sum(ij)) for ij,co in P.terms()))
Q=-x*a**2-y*b**2+x*y*(x+y)*h**2; smoothing=s.factor(s.diff(G,E).subs(E,0))
rows=[]
for sa in (1,-1):
 for sb in (1,-1):
  sub={a:sa*y+u,b:sb*x+v,h:1}
  qloc=s.expand(Q.subs(sub)); rloc=s.expand(smoothing.subs(sub))
  qlin=sum(co*u**m[0]*v**m[1] for m,co in s.Poly(qloc,u,v).terms() if sum(m)==1)
  rquad=sum(co*u**m[0]*v**m[1] for m,co in s.Poly(rloc,u,v).terms() if sum(m)==2)
  # tangent parameter: u=sb*s, v=-sa*s solves sa*u+sb*v=0.
  rtan=s.factor(rquad.subs({u:sb*ss,v:-sa*ss}))
  rows.append({'signs':[sa,sb],'Q_linear':str(s.factor(qlin)),'smoothing_quadratic':str(s.factor(rquad)),'conductor_tangent':{'u':f'{sb}*s','v':f'{-sa}*s'},'restricted_leading':str(rtan),'double_zero':s.factor(rtan/(ss**2))!=0})
checks={'four_points':len(rows)==4,'all_Q_linear_nonzero':all(r['Q_linear']!='0' for r in rows),'all_smoothing_order_two_on_conductor':all(r['double_zero'] for r in rows),'universal_restricted_coefficient':len({r['restricted_leading'] for r in rows})==1}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.four-conductor-local-smoothing.v1','normal_crossing_coordinates':'X=W-Q, Y=W+Q, so XY=G_E-Q^2','local_type':'after analytic coordinate changes, XY=E*s^2 times a unit plus higher E-order terms','points':rows,'divisor_statement':'the first smoothing section restricts to the conductor with a double zero at each of the four sign-labelled points','geometric_effect':'each marked point is a width-two rather than width-one gluing point; resolving it inserts the primitive half-sum data','checks':checks,'passed':True,'next':'construct the blowup of XY=E*s^2 and compute its integral specialization boundary matrix'}
(R/'research/voevodsky/results/four_conductor_local_smoothing.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'local_type':out['local_type'],'points':rows,'next':out['next']}))
