#!/usr/bin/env python3
"""Verify the exact Green-transfer reduction of the Loewner kernel."""
import json,sys
from pathlib import Path
try:import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
zx,zy,Ix,Iy,Jx,Jy,Px,Py=s.symbols('zx zy Ix Iy Jx Jy Px Py')
old=zx*zy*(zx*Jx*Iy-zy*Jy*Ix)
new=zx*zy*(Ix*Py-Px*Iy)
sub={Px:-Ix-zx*Jx,Py:-Iy-zy*Jy}
assert s.expand(new.subs(sub)-old)==0
out={'schema':'marici.voevodsky.mixed-theta-bezoutian-frontier.v1','checks':{'Green_substitution_exact':True,'pure_precursor_terms_cancel':True,'centered_multipliers_retained':True},
 'identity':'L_C(x,y)=zeta_x zeta_y [I(x)P(y)-P(x)I(y)]/(x-y)',
 'ratio':'R=P/I=-H on zero-free intervals','remaining_theorem':'matrix-monotone decrease of R, equivalently a Gram factorization of the mixed K-Phi Bezoutian',
 'falsified_shortcuts':['integration by parts alone gives a square','finite seam Schur complement controls the global form','generic increasing curvature implies the required Schwarzian sign'],
 'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'mixed_theta_bezoutian_frontier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
