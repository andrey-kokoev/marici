#!/usr/bin/env python3
"""Check whether the fixed-coordinate antisymmetric double poles survive a wall-horizontal GM lift."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];sys.path.insert(0,str(R/'research/benincasa/.tmp_sympy'))
import sympy as sp
prev=json.loads((R/'research/voevodsky/results/exchange_odd_physical_shape_response.json').read_text())
coh=json.loads((R/'research/benincasa/physical-normal-lift-cech-coherence.json').read_text())
poles=json.loads((R/'research/benincasa/results/relative-shape-pole-depth.json').read_text())
a,b,x,y,t=sp.symbols('a b x y t')
f=lambda aa,bb,xx,yy:1/(bb-xx)+1/(aa-yy)
fixed=sp.diff(f(a,b,x+t,y-t),t).subs(t,0)
# Horizontal lift: delta a=-1, delta b=+1, preserving both moving wall coordinates.
lifted_expr=f(a-t,b+t,x+t,y-t)
lifted=sp.diff(lifted_expr,t).subs(t,0)
q23=(b+t)-(x+t);q31=(a-t)-(y-t)
checks={'fixed_derivative_antisymmetric':sp.simplify(fixed-(1/(b-x)**2-1/(a-y)**2))==0,'lift_preserves_q23':sp.diff(q23,t)==0,'lift_preserves_q31':sp.diff(q31,t)==0,'lifted_pole_sum_constant':sp.simplify(lifted_expr-f(a,b,x,y))==0,'lifted_double_pole_response_zero':sp.simplify(lifted)==0,'Cech_lifts_glue_mod_exact':coh['cech_class']=='local contact-weighted responses glue modulo exact meromorphic forms','simple_residue_matrix_pending':poles['simple_residue_matrix_constructed'] is False}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.exchange-odd-response-GM-lift-audit.v1','base_tangent':'partial_x-partial_y','fixed_coordinate_response':str(sp.factor(fixed)),'wall_horizontal_lift':'partial_x-partial_y-partial_a+partial_b','lifted_paths':{'x':'x+t','y':'y-t','a':'a-t','b':'b+t'},'preserved_walls':['q23=b-x','q31=a-y'],'lifted_principal_response':str(lifted),'disposition':'The antisymmetric doubled-wall covector is a fixed-coordinate principal part and vanishes under the wall-horizontal Gauss-Manin lift.','C15b_prior_status':'withdrawn','surviving_question':'The full lifted integrand also contains Cayley-Menger and remaining-wall factors. Its resulting simple mixed residue requires the pending IBP/simple-residue reduction.','required_next':'Apply the global contact-weighted Gauss-Manin adapter to the six-term relative shape jet, reduce by IBP, and project its simple residue matrix onto g101-g110.','checks':checks,'passed':True}
(R/'research/voevodsky/results/exchange_odd_response_GM_lift_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'fixed':out['fixed_coordinate_response'],'lifted':out['lifted_principal_response'],'disposition':out['disposition'],'C15b':out['C15b_prior_status'],'next':out['required_next']}))
