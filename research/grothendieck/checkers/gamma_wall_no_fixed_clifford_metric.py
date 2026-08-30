import json
from pathlib import Path

import sympy as sp


c = sp.symbols("c", positive=True)


def transfer(j):
    return sp.Matrix(
        [
            [j + sp.Rational(19, 4), -sp.Rational(3, 2) * (j + sp.Rational(5, 4)), 1],
            [1, 0, 0],
            [0, 0, c],
        ]
    )


relative = sp.simplify(transfer(1) * transfer(0).inv())
expected = sp.Matrix(
    [
        [sp.Rational(9, 5), -sp.Rational(14, 5), -sp.Rational(4, 5) / c],
        [0, 1, 0],
        [0, 0, 1],
    ]
)
x = sp.symbols("x")
characteristic = sp.factor(relative.charpoly(x).as_expr())
expected_characteristic = (x - 1) ** 2 * (x - sp.Rational(9, 5))

# If relative.T * Q * relative = mu * Q for nondegenerate Q, then the spectrum
# must be invariant under alpha -> mu/alpha. The determinant fixes mu^3.
mu = (sp.Rational(9, 5)) ** sp.Rational(2, 3)
spectrum = {sp.Integer(1), sp.Rational(9, 5)}
paired_candidates = {sp.simplify(mu), sp.simplify(mu / sp.Rational(9, 5))}

checks = {
    "relative_matrix_exact": relative == expected,
    "relative_independent_of_wall_except_shear": all(
        not entry.has(c) for entry in [relative[0, 0], relative[1, 1], relative[2, 2]]
    ),
    "characteristic_polynomial_exact": sp.expand(characteristic - expected_characteristic) == 0,
    "determinant_is_nine_fifths": sp.factor(relative.det() - sp.Rational(9, 5)) == 0,
    "conformal_factor_not_in_spectrum": all(
        sp.simplify(candidate - eigenvalue) != 0
        for candidate in paired_candidates
        for eigenvalue in spectrum
    ),
}

result = {
    "schema": "marici.gamma_wall_no_fixed_clifford_metric.v1",
    "checks": checks,
    "exact": {
        "relative_matrix": str(relative),
        "characteristic_polynomial": str(characteristic),
        "determinant": str(relative.det()),
        "forced_conformal_factor": str(mu),
        "spectrum": ["1", "1", "9/5"],
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/gamma_wall_no_fixed_clifford_metric.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
