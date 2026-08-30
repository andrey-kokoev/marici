import json
from pathlib import Path

import sympy as sp


y, c, j = sp.symbols("y c j", positive=True)
a = sp.Rational(3, 2)
x = c * sp.exp(y)


def source(degree):
    return x ** (degree + sp.Rational(5, 4)) * (x - a) * sp.exp(-x)


f0 = source(j)
f1 = source(j + 1)
f2 = source(j + 2)
g = sp.simplify(f1 - a * f0)
pearson = sp.simplify(
    f2
    - (j + sp.Rational(19, 4)) * f1
    + a * (j + sp.Rational(5, 4)) * f0
)
derivative_residual = sp.simplify(pearson + sp.diff(g, y))
wall = sp.simplify(g.subs(y, 0))
expected_wall = c ** (j + sp.Rational(5, 4)) * (c - a) ** 2 * sp.exp(-c)

hostile = sp.simplify(
    f2
    - (j + sp.Rational(18, 4)) * f1
    + a * (j + sp.Rational(5, 4)) * f0
    + sp.diff(g, y)
)

checks = {
    "source_derivative_identity": derivative_residual == 0,
    "wall_value_exact": sp.simplify(wall - expected_wall) == 0,
    "hostile_coefficient_detected": hostile != 0,
}
weyl = {}

for order in range(13):
    dimension = order + 1
    multiply = sp.zeros(dimension)
    derivative = sp.zeros(dimension)
    for column in range(dimension):
        if column + 1 < dimension:
            multiply[column + 1, column] = 1
        if column:
            derivative[column - 1, column] = column
    top = sp.zeros(dimension)
    top[-1, -1] = 1
    commutator = derivative * multiply - multiply * derivative
    expected_commutator = sp.eye(dimension) - dimension * top
    checks[f"jet_{order}_weyl_cutoff_anomaly"] = (
        commutator == expected_commutator
    )
    weyl[str(order)] = str(commutator)

result = {
    "schema": "marici.pearson_relative_derham_boundary.v1",
    "checks": checks,
    "exact": {
        "wall_current": str(wall),
        "hostile_residual": str(hostile),
        "weyl_commutators_0_through_12": weyl,
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/pearson_relative_derham_boundary.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
