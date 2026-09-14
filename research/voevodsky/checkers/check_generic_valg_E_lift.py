#!/usr/bin/env python3
"""Verify the generic E-lift and its parity properties from source formulas."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
a,b,x,y,E=s.symbols('a b x y E')
coeff=[(x**2-y**2)*(x**2*y**2-E**4),2*x**2*(E**2+y**2),-2*y**2*(E**2+x**2)]
N=s.expand(coeff[0]+coeff[1]*a**2+coeff[2]*b**2)
N0=s.factor(N.subs(E,0))
expected0=x**2*y**2*(x**2-y**2+2*a**2-2*b**2)
checks={
 "central_specialization":s.expand(N0-expected0)==0,
 "E_even":s.expand(N.subs(E,-E)-N)==0,
 "first_E_jet_zero":s.diff(N,E).subs(E,0)==0,
 "second_E_jet_nonzero":s.diff(N,E,2).subs(E,0)!=0,
 "b_even":s.expand(N.subs(b,-b)-N)==0,
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.generic-valg-E-lift.v1",
 "passed":True,
 "coefficients_e7_e8_e9":[str(s.factor(c)) for c in coeff],
 "numerator":str(s.factor(N)),
 "central_numerator":str(N0),
 "E_parity":"even",
 "first_E_numerator_jet":"0",
 "consequence":"linear antisymmetric collision response cannot originate in the v_alg numerator; cycle marking or K_E transport must supply it",
 "typing":"absolute Picard pairing; ordinary relative boundary residue is insufficient",
 "checks":checks,
}
p=ROOT/"research/voevodsky/results/generic_valg_E_lift.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"E_parity":"even","first_E_jet":0}))
