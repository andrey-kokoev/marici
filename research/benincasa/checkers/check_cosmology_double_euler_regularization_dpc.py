#!/usr/bin/env python3
"""Audit whether discriminant times collision Euler is a sourced rank-two Euler class."""
import json
from pathlib import Path
import sympy as s
x,xi,k=s.symbols('x xi k');f=x*(xi+1);g=x*(k-1);J=s.Matrix([[s.diff(f,z) for z in (x,xi,k)],[s.diff(g,z) for z in (x,xi,k)]])
minors=[s.factor(J[:,[i,j]].det().subs(x,0)) for i,j in ((0,1),(0,2),(1,2))]
assert minors==[0,0,0]
assert -2+1+1==0
out={'schema':'marici.benincasa.cosmology-double-euler-regularization-dpc.v1','problem':'Can the full discriminant times a second collision Euler factor be interpreted as a canonical rank-two excess Euler class that regularizes kappa=1?','bold_conjecture':'The product discriminant times (kappa-1) is the top Chern class of the displayed two-wall normal bundle and canonically cancels the conductor double pole.','named_rivals':['the product regularizes only algebraically by double-counting one normal direction','the displayed conormal map has rank at most one on x=0','an independent transverse equation is required for a rank-two Euler class'],'risky_consequences':['the two-wall conormal wedge must be nonzero','some two-by-two Jacobian minor must survive on x=0'],'strongest_falsification_attempt':{'algebraic_total_valuation':0,'two_wall_jacobian':str(J),'two_by_two_minors_on_x0':[str(z) for z in minors],'conormal_rank_upper_bound':1,'rank_two_top_Chern_authorized':False},'disposition':{'status':'falsified as a geometric construction','residual':'the product cancels the pole numerically but is not the Euler class of the displayed rank-one conormal data; it double-counts the collision direction','reopening_test':'supply an independent transverse source equation whose conormal wedge is nonzero and whose oriented top Chern class equals the order-two factor'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_double_euler_regularization_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
