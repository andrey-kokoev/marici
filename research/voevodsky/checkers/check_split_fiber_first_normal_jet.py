#!/usr/bin/env python3
"""Exact Cayley-Menger first normal jets along colliding split fibers."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
c,a,b,x,y,E=s.symbols('c a b x y E');z=E-x-y
CM=s.Matrix([[0,1,1,1,1],[1,0,c**2,a**2,b**2],[1,c**2,0,y**2,x**2],[1,a**2,y**2,0,z**2],[1,b**2,x**2,z**2,0]])
K=s.expand(-s.Rational(1,2)*CM.det().subs(c,-E))
R=x*a**2+y*b**2-x*y*(x+y)
KE0=s.factor(s.diff(K,E).subs(E,0))
expected=-2*(x+y)*(a-y)*(a+y)*(b-x)*(b+x)
rows=[]
for center,vel,label in [(x,-1,'q2'),(x,1,'q3'),(-x,1,'q1'),(-x,-1,'q4')]:
 total=s.factor(s.diff(K.subs(b,center+vel*E),E).subs(E,0))
 r0=s.factor(R.subs(b,center))
 sqrtjet=s.factor(total/(2*r0))
 rows.append({'label':label,'center':str(center),'velocity':vel,'K_jet':str(total),'sqrt_jet':str(sqrtjet)})
checks={
 'central_square':s.expand(K.subs(E,0)-R**2)==0,
 'fixed_E_jet_factorization':s.expand(KE0-expected)==0,
 'fixed_jet_zero_both_walls':KE0.subs(b,x)==0 and KE0.subs(b,-x)==0,
 'moving_sqrt_jets':[s.simplify(r['sqrt_jet']) for r in rows]==[s.sympify('-2*x*y'),s.sympify('2*x*y'),s.sympify('-2*x*y'),s.sympify('2*x*y')],
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.split-fiber-first-normal-jet.v1','passed':True,'K_E_first_at_zero':str(KE0),'moving_fibers':rows,'normalized_pair_differences':{'q3_minus_q2':'1 after division by 4*x*y','q4_minus_q1':'1 after division by 4*x*y'},'scope':'geometric normal-jet unit, not yet an absolute v_alg period','checks':checks}
p=ROOT/'research/voevodsky/results/split_fiber_first_normal_jet.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'sqrt_jets':[r['sqrt_jet'] for r in rows]}))
