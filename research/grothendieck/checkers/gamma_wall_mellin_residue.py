import json
from pathlib import Path

import sympy as sp


c, j, y, q = sp.symbols("c j y q", positive=True)
a = sp.Rational(3, 2)
x = c * sp.exp(y)
f_j = x ** (j + sp.Rational(5, 4)) * (x - a) * sp.exp(-x)
f_j_wall = sp.simplify(f_j.subs(y, 0))
expected_f_j_wall = c ** (j + sp.Rational(5, 4)) * (c - a) * sp.exp(-c)

f_j_plus_one_wall = sp.simplify(f_j_wall.subs(j, j + 1))
shifted_residue = sp.factor(f_j_plus_one_wall - a * f_j_wall)
expected_wall_current = c ** (j + sp.Rational(5, 4)) * (c - a) ** 2 * sp.exp(-c)

k_minus_one, k0, k1, k2 = sp.symbols("k_minus_one k0 k1 k2")
laurent = k_minus_one / q + k0 + k1 * q + k2 * q**2
regularized = sp.expand(q * laurent)
expected_regularized = k_minus_one + k0 * q + k1 * q**2 + k2 * q**3

wrong_a = sp.Integer(1)
wrong_residue = sp.factor(f_j_plus_one_wall - wrong_a * f_j_wall - expected_wall_current)

result = {
    "schema": "marici.gamma_wall_mellin_residue.v1",
    "checks": {
        "wall_value_identity": sp.simplify(f_j_wall - expected_f_j_wall) == 0,
        "shifted_residue_equals_wall_current": sp.simplify(
            shifted_residue - expected_wall_current
        )
        == 0,
        "four_term_laurent_regularization": sp.simplify(
            regularized - expected_regularized
        )
        == 0,
        "wrong_wall_coefficient_residual_nonzero": wrong_residue != 0,
    },
    "exact": {
        "wall_value": str(f_j_wall),
        "shifted_residue": str(shifted_residue),
        "wall_current": str(expected_wall_current),
        "regularized_laurent": str(regularized),
        "wrong_wall_residual": str(wrong_residue),
    },
}

if not all(result["checks"].values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/gamma_wall_mellin_residue.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

