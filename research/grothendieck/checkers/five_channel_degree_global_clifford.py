import json
from pathlib import Path

import sympy as sp


j, c = sp.symbols("j c", nonnegative=True)
a, b, d, e, f, g, u = sp.symbols("a b d e f g u", real=True)


def transfer(degree):
    return sp.Matrix(
        [
            [degree + sp.Rational(19, 4), -sp.Rational(3, 2) * (degree + sp.Rational(5, 4)), 1],
            [1, 0, 0],
            [0, 0, c],
        ]
    )


def split_transfer(degree):
    tail_determinant = sp.Rational(3, 2) * (degree + sp.Rational(5, 4))
    return sp.diag(transfer(degree), 1 / tail_determinant, 1 / c)


relative = sp.simplify(split_transfer(j + 1) * split_transfer(j).inv())
ratio = (4 * j + 9) / (4 * j + 5)
expected = sp.Matrix(
    [
        [ratio, -14 / (4 * j + 5), -4 / (c * (4 * j + 5)), 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1 / ratio, 0],
        [0, 0, 0, 0, 1],
    ]
)
Q = sp.Matrix(
    [
        [0, 0, 0, -c * u, 0],
        [0, a, b, sp.Rational(7, 2) * c * u, d],
        [0, b, e, u, f],
        [-c * u, sp.Rational(7, 2) * c * u, u, 0, 0],
        [0, d, f, 0, g],
    ]
)

x = sp.symbols("x")
expected_characteristic = (x - 1) ** 3 * (x - ratio) * (x - 1 / ratio)
specialization = {a: 1, b: 2, d: 3, e: 4, f: 5, g: 6, u: 7}
R0 = sp.simplify(relative.subs(j, 0))
R1 = sp.simplify(relative.subs(j, 1))
two_step = sp.simplify(R1 * R0)

checks = {
    "relative_matrix_symbolic": sp.simplify(relative - expected) == sp.zeros(5),
    "reciprocal_characteristic_polynomial": sp.factor(
        relative.charpoly(x).as_expr() - expected_characteristic
    )
    == 0,
    "one_form_invariant_for_all_degrees": sp.simplify(relative.T * Q * relative - Q)
    == sp.zeros(5),
    "nondegenerate_specialization": sp.factor(Q.det().subs(specialization)) != 0,
    "finite_product_invariant": sp.simplify(two_step.T * Q * two_step - Q)
    == sp.zeros(5),
}

result = {
    "schema": "marici.five_channel_degree_global_clifford.v1",
    "checks": checks,
    "exact": {
        "relative_matrix": str(relative),
        "eigenvalue_ratio": str(ratio),
        "invariant_form_determinant": str(sp.factor(Q.det())),
        "specialized_determinant": str(sp.factor(Q.det().subs(specialization))),
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/five_channel_degree_global_clifford.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
