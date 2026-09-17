#!/usr/bin/env python3
"""Exact finite-dimensional fixture for the coercive Schur reduction."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages')); import sympy as s
m,c,d=s.symbols('m c delta',positive=True)
W=s.Matrix([[m,c],[c,d]])
schur=m-c**2/d
assert s.factor(W.det()-d*schur)==0
# Under c^2 <= m*d the scalar Schur complement is nonnegative.
fixture={m:s.Rational(3,2),d:s.Rational(5,4),c:s.Rational(1,2)}
assert schur.subs(fixture)>0 and all(v>0 for v in W.subs(fixture).eigenvals())
out={'schema':'marici.voevodsky.log-elliptic-schur-reduction.v1','checks':{'block_determinant_identity':True,'coercive_fixture_positive':True},'conclusion':'A positive high-frequency block reduces negativity to the finite low-frequency Schur complement.','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'log_elliptic_schur_reduction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
