#!/usr/bin/env python3
"""Reduce the tensor-weighted infinity residue to the elliptic H1 basis."""

import json
from pathlib import Path

import sympy as sp


a, b, c, t, s = sp.symbols("a b c t s")
x, y, z, E = sp.symbols("x y z E", nonzero=True)

CM = sp.Matrix(
    [
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, y**2, x**2],
        [1, a**2, y**2, 0, z**2],
        [1, b**2, x**2, z**2, 0],
    ]
)
K = sp.factor(-CM.det() / 2)
Lambda = sp.factor((x-y-z)*(x-y+z)*(x+y-z)*(x+y+z))
N = sp.expand(
    2*x**2*(c**2+y**2-a**2)
    - (c**2+x**2-b**2)*(x**2+y**2-z**2)
)
Q = sp.cancel(-(N**2+4*x**2*K)/(4*x**2*Lambda))

# q_G12 residue and b-infinity chart: b=1/s, a=t/s, c=-E.
chart = {a: t/s, b: 1/s, c: -E}
K_bar = sp.cancel(s**4*K.subs(chart))
Q_bar = sp.cancel(s**4*Q.subs(chart))
F = sp.factor(sp.expand(K_bar).coeff(s, 0))
G = sp.factor(sp.expand(K_bar).coeff(s, 2))
H = sp.factor(sp.expand(K_bar).coeff(s, 4))
q4 = sp.factor(sp.expand(Q_bar).coeff(s, 0))
q2 = sp.factor(sp.expand(Q_bar).coeff(s, 2))
q0 = sp.factor(sp.expand(Q_bar).coeff(s, 4))

assert sp.factor(F-(x**2*t**4-(x**2+y**2-z**2)*t**2+y**2)) == 0
assert sp.factor(K_bar-F-s**2*G-s**4*H) == 0
assert sp.factor(Q_bar-q4-s**2*q2-s**4*q0) == 0

# The logarithmic coefficient of
# Q da db/w = Q (ds/s) dt/sqrt(F+s^2G+s^4H)
# after removing s^-5 and s^-3 normal poles.
numerator = sp.cancel(
    q0*F**2 - sp.Rational(1, 2)*q2*G*F
    + q4*(-sp.Rational(1, 2)*H*F+sp.Rational(3, 8)*G**2)
)

c0, c2 = sp.symbols("c0 c2")
r = sp.symbols("r0:5")
R = sum(r[i]*t**(2*i+1) for i in range(5))
reduction_polynomial = sp.Poly(
    sp.together(
        numerator-(c0+c2*t**2)*F**2-sp.diff(R,t)*F
        +sp.Rational(3, 2)*R*sp.diff(F,t)
    ),
    t,
)
equations = [reduction_polynomial.coeff_monomial(t**(2*i)) for i in range(7)]
solution = sp.solve(equations, [c0,c2,*r], dict=True, simplify=False, rational=False)[0]
c0_value = sp.factor(solution[c0])
c2_value = sp.factor(solution[c2])
assert sp.factor(reduction_polynomial.as_expr().subs(solution)) == 0

# Exact support audit.  These are the complete denominators of the reduced
# elliptic coefficients, before imposing E=x+y+z.
assert sp.factor(sp.denom(c0_value)/(32*x**2*y**2*Lambda)) == 1
assert sp.factor(sp.denom(c2_value)/(16*y**4*Lambda)) == 1
physical_c0 = sp.factor(c0_value.subs(E, x+y+z))
physical_c2 = sp.factor(c2_value.subs(E, x+y+z))
assert sp.factor(sp.denom(physical_c0)/(32*x**2*y**2*Lambda)) == 1
assert sp.factor(sp.denom(physical_c2)/(16*y**4*Lambda)) == 1
assert physical_c0.subs({x:2,y:3,z:4}) != 0
assert physical_c2.subs({x:2,y:3,z:4}) != 0

packet = {
    "schema": "marici.benincasa.tensor-infinity-gysin-elliptic.v1",
    "status": "passed",
    "boundary_curve": str(F),
    "tensor_growth": "Q=s^-4*q4+s^-2*q2+q0",
    "logarithmic_coefficient": "numerator/F^(5/2) dt",
    "exact_reduction": "(c0+c2*t^2)dt/sqrt(F) + d(R/F^(3/2))",
    "elliptic_basis": ["omega0=dt/W", "omega2=t^2 dt/W"],
    "c0": str(c0_value),
    "c2": str(c2_value),
    "denominator_support": ["x=0", "y=0", "Lambda(x,y,z)=0"],
    "physical_specialization": "E=x+y+z",
    "generic_image_rank_from_this_generator": 1,
    "target_coefficient_rank": 2,
    "new_elliptic_block": False,
    "new_carrier_support": False,
    "classification": (
        "the tensor-weighted logarithmic infinity residue is an explicit class "
        "in the existing rank-two elliptic H1 quotient"
    ),
    "scope_warning": (
        "This is one source-normalized generator. Cyclic tensor vertices follow "
        "by occurrence transport; the full physical period pairing is still to be audited."
    ),
}

output = Path(__file__).with_name("tensor-infinity-gysin-elliptic.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
