#!/usr/bin/env python3
"""DPC audit: can the two displayed wall equations derive the required node Jacobian?"""
import json
from pathlib import Path
import sympy as s
x,xi,k,p=s.symbols('x xi k p')
f=x*(xi+1);g=x*(k-1);coords=(x,xi,k)
J=s.Matrix([[s.diff(f,z) for z in coords],[s.diff(g,z) for z in coords]])
minors=[s.factor(J[:,[i,j]].det().subs(x,0)) for i,j in ((0,1),(0,2),(1,2))]
assert minors==[0,0,0]
required=s.factor(-(k-3)/(4*p));assert required!=0
out={'schema':'marici.benincasa.qg2-excess-gysin-normal-bundle-dpc.v1','problem':'Can the displayed two-wall normal equations independently derive the nonzero node Jacobian required for q_g1-q_g2 closure?','bold_conjecture':'The complete-intersection Jacobian of q_g1=x(xi+1) and q_g2-q_g31=x(kappa-1), restricted to x=0, yields -(kappa-3)/(4p).','named_rivals':['the two equations have a common exceptional factor and conormal rank one','an additional source equation or excess-bundle quotient is required','the fitted residue ratio is not a geometric Jacobian'],'risky_consequences':['some two-by-two Jacobian minor must remain nonzero on x=0','the surviving minor must equal the required factor without residue fitting'],'strongest_falsification_attempt':{'jacobian_matrix':str(J),'two_by_two_minors_on_exceptional_divisor':[str(z) for z in minors],'conormal_rank_upper_bound':1,'required_nonzero_factor':str(required)},'disposition':{'status':'falsified from the displayed two-wall equations','residual':'their conormal wedge vanishes on x=0, while the required factor is generically nonzero','reopening_test':'supply a source-derived excess normal-bundle quotient, additional transverse equation, and its Gysin orientation whose determinant computes -(kappa-3)/(4p)'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg2_excess_gysin_normal_bundle_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
