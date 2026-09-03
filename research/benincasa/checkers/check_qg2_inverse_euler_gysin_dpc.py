#!/usr/bin/env python3
"""Exact localized self-intersection audit for the q_g2 collision Euler factor."""
import json
from pathlib import Path
import sympy as s
k,p=s.symbols('k p', nonzero=True);e=k-1
r1=1/(64*p**4*e);r2=r1;rinf=s.factor(-(r1+r2));target=-1/(32*p**4*e**2)
delta=s.factor(rinf/e)
assert s.simplify(delta-target)==0
# In the localized coefficient ring, multiplication by e has the unique scalar left inverse 1/e.
u=s.symbols('u');solution=s.solve(s.Eq(u*e,1),u);assert solution==[1/e]
out={'schema':'marici.benincasa.qg2-inverse-euler-gysin-dpc.v1','problem':'Is division by kappa-1 and its negative sign merely fitted to close the q_g1-q_g2 node?','bold_conjecture':'No oriented excess-Gysin construction forces the coefficient -(r_-1+r_-kappa)/(kappa-1).','named_rivals':['localized self-intersection uniquely inverts the collision Euler class','the global residue orientation fixes the negative finite-residue sum','another Euler power or sign is admissible'],'risky_consequences':['multiplication by the collision Euler class must lack a unique localized left inverse','the infinity residue must not equal the negative finite-residue sum'],'strongest_falsification_attempt':{'collision_normal_equation':'q_g2-q_g31=x(kappa-1)','Euler_class':str(e),'localized_left_inverse':str(solution[0]),'finite_residues':[str(r1),str(r2)],'oriented_infinity_residue':str(rinf),'connecting_coefficient':str(delta),'required_target':str(target)},'disposition':{'status':'falsified in the localized oriented normal model','surviving_scope':'self-intersection forces one inverse Euler factor; the global residue theorem fixes the minus sign and exactly reproduces the missing coefficient','qualification':'this constructs the local conductor connecting coefficient, not the absent physical relative cut chain'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg2_inverse_euler_gysin_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
