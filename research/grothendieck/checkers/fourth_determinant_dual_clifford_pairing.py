import json
from pathlib import Path

import sympy as sp


c = sp.symbols("c", positive=True)
a, b, d, u = sp.symbols("a b d u", real=True)


def transfer(j):
    return sp.Matrix(
        [
            [j + sp.Rational(19, 4), -sp.Rational(3, 2) * (j + sp.Rational(5, 4)), 1],
            [1, 0, 0],
            [0, 0, c],
        ]
    )


def completed_transfer(j):
    matrix = transfer(j)
    return sp.diag(matrix, 1 / matrix.det())


relative = sp.simplify(completed_transfer(1) * completed_transfer(0).inv())
expected_relative = sp.Matrix(
    [
        [sp.Rational(9, 5), -sp.Rational(14, 5), -sp.Rational(4, 5) / c, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, sp.Rational(5, 9)],
    ]
)
Q = sp.Matrix(
    [
        [0, 0, 0, -c * u],
        [0, a, b, sp.Rational(7, 2) * c * u],
        [0, b, d, u],
        [-c * u, sp.Rational(7, 2) * c * u, u, 0],
    ]
)

# Audit a common invariant form for the individual completed steps.
variables = sp.symbols("q0:10")
Q_general = sp.zeros(4)
cursor = 0
for row in range(4):
    for column in range(row, 4):
        Q_general[row, column] = variables[cursor]
        Q_general[column, row] = variables[cursor]
        cursor += 1
step_equations = []
for degree in (0, 1):
    step = completed_transfer(degree)
    step_equations.extend(list(step.T * Q_general * step - Q_general))
common_step_forms = sp.linsolve(step_equations, variables)

x = sp.symbols("x")
checks = {
    "completed_steps_have_unit_determinant": all(
        sp.simplify(completed_transfer(j).det() - 1) == 0 for j in (0, 1)
    ),
    "relative_matrix_exact": relative == expected_relative,
    "reciprocal_characteristic_polynomial": sp.expand(
        relative.charpoly(x).as_expr()
        - (x - 1) ** 2 * (x - sp.Rational(9, 5)) * (x - sp.Rational(5, 9))
    )
    == 0,
    "relative_form_invariant": sp.simplify(relative.T * Q * relative - Q)
    == sp.zeros(4),
    "relative_form_determinant": sp.factor(
        Q.det() + c**2 * u**2 * (a * d - b**2)
    )
    == 0,
    "no_common_stepwise_invariant_form": common_step_forms
    == sp.FiniteSet(tuple(sp.Integer(0) for _ in variables)),
}

result = {
    "schema": "marici.fourth_determinant_dual_clifford_pairing.v1",
    "checks": checks,
    "exact": {
        "relative_matrix": str(relative),
        "relative_spectrum": ["1", "1", "9/5", "5/9"],
        "invariant_form_determinant": str(sp.factor(Q.det())),
        "common_stepwise_forms": str(common_step_forms),
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path(
    "research/grothendieck/results/fourth_determinant_dual_clifford_pairing.json"
)
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
