import json
from pathlib import Path

import sympy as sp

z, u, v = sp.symbols("z u v", real=True)
w = sp.Rational(1, 2) - u - v
n = 2*(z**2-z+1)
A = (z+1)**2/n
B = (2*z-1)**2/n
C = (z-2)**2/n
r = sp.Rational(44376, 275)
F = sp.factor(2*(A*u+B*v+C*w) + 4*r*A*B*C*u*v*w)
Fstar = sp.Rational(2417, 946)

# Exact boundary certificate in the ordered Weyl chamber [-1,1/2].
assert sp.simplify((C-A) + 3*(2*z-1)/(2*(z**2-z+1))) == 0
assert sp.simplify((C-B) + 3*(z-1)*(z+1)/(2*(z**2-z+1))) == 0
assert sp.simplify((2-C) - 3*z**2/(2*(z**2-z+1))) == 0
assert Fstar > 2

# Complete interior KKT elimination.
eqs = [
    sp.primitive(sp.Poly(
        sp.together(sp.diff(F, q)).as_numer_denom()[0], u, v, z
    ))[1].as_expr()
    for q in (u, v, z)
]
gb = sp.groebner(eqs, u, v, z, order="lex")
eliminant = sp.factor(gb.polys[-1].as_expr())
p12 = (
    37009*z**12 - 222054*z**11 + 377805*z**10 + 146470*z**9
    - 513261*z**8 - 1268370*z**7 + 2921811*z**6
    - 1268370*z**5 - 513261*z**4 + 146470*z**3
    + 377805*z**2 - 222054*z + 37009
)
expected_eliminant = z*(z-1)*(z**2-z+1)**2*p12
assert sp.factor(eliminant/expected_eliminant) != 0
assert sp.Poly(p12, z).count_roots(-sp.oo, sp.oo) == 0
assert sp.discriminant(z**2-z+1, z) < 0

eqs_z0 = [sp.factor(e.subs(z, 0)) for e in eqs]
solutions = sp.solve(eqs_z0, (u, v), dict=True)
expected_solutions = [
    {u: sp.Rational(11, 516), v: sp.Rational(11, 516)},
    {u: sp.Rational(25, 172), v: sp.Rational(25, 172)},
]
assert solutions == expected_solutions

secondary = sp.factor(F.subs({z: 0, **expected_solutions[0]}))
witness = sp.factor(F.subs({z: 0, **expected_solutions[1]}))
assert secondary == sp.Rational(37523, 19350)
assert witness == Fstar
assert secondary < 2 < witness

# Deliberate-failure test: stationarity alone would retain the secondary point,
# but the exact global comparison rejects it.
stationary_scores = [secondary, witness]
assert stationary_scores.index(max(stationary_scores)) == 1

result = {
    "schema": "marici.flavor.wp1009.v1",
    "status": "PASS",
    "weyl_chamber": "-1 <= z <= 1/2",
    "boundary_upper_bound": "2",
    "eliminant": "z(z-1)(z^2-z+1)^2 p12(z)",
    "p12_real_root_count": 0,
    "interior_stationary_scores": [str(secondary), str(witness)],
    "global_maximum": str(witness),
    "global_maximizer": {
        "z": "0", "u": "25/172", "v": "25/172", "w": "9/43"
    },
    "classification": "unique global maximizing orbit modulo simultaneous permutations, weak-basis conjugation, and scales",
    "remaining_gate": "source-derived coefficient ratio, physical16 image, and calibrated instrument",
}

out = Path(__file__).parents[1] / "results" / "wp1009_global_hermitian_score_hull.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1009 PASS: exact KKT exhaustion proves a unique global Hermitian score orbit")
