#!/usr/bin/env python3
"""Verify opposite primitive v_alg coefficients of the two universal wall tails."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
x,y=s.symbols('x y', nonzero=True);den=4*x**3*y**3*(x+y)
# Coefficients relative to v0.
t=s.Matrix([[-1/den,1/den]])
cleared=s.simplify(den*t)
q=s.Matrix([-1,1]);kernel=s.Matrix([1,1])
checks={
 'opposite_tails':s.simplify(t[0,0]+t[0,1])==0,
 'cleared_primitive_covector':cleared==q.T,
 'primitive':s.gcd_list(list(q))==1,
 'sum_kernel':(q.T*kernel)[0]==0,
 'kernel_primitive':s.gcd_list(list(kernel))==1,
 'odd_route_maps_to_two':(q.T*s.Matrix([-1,1]))[0]==2,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.one-wall-valg-covector.v1','passed':True,'wall_basis':['w101','w110'],'tail_coefficients_over_v0':['-1/(4*x^3*y^3*(x+y))','1/(4*x^3*y^3*(x+y))'],'cleared_covector':[-1,1],'kernel_generator':[1,1],'image_saturated':True,'odd_eigenvector_image':2,'picard_marking_status':'not serialized; alpha13/alpha14 identification remains conditional','checks':checks}
p=ROOT/'research/voevodsky/results/one_wall_valg_covector.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'covector':[-1,1],'kernel':[1,1]}))
