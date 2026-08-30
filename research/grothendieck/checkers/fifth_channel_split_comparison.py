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


def split_transfer(j):
    tail_determinant = sp.Rational(3, 2) * (j + sp.Rational(5, 4))
    return sp.diag(transfer(j), 1 / tail_determinant, 1 / c)


relative = sp.simplify(split_transfer(1) * split_transfer(0).inv())
expected = sp.Matrix(
    [
        [sp.Rational(9, 5), -sp.Rational(14, 5), -sp.Rational(4, 5) / c, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, sp.Rational(5, 9), 0],
        [0, 0, 0, 0, 1],
    ]
)

variables = sp.symbols("q0:15")
Q = sp.zeros(5)
cursor = 0
for row in range(5):
    for column in range(row, 5):
        Q[row, column] = variables[cursor]
        Q[column, row] = variables[cursor]
        cursor += 1

solution = list(sp.linsolve(list(relative.T * Q * relative - Q), variables))[0]
invariant_form = sp.simplify(Q.subs(dict(zip(variables, solution))))
invariant_determinant = sp.factor(invariant_form.det())

# One exact nondegenerate specialization.
free_symbols = sorted(
    invariant_determinant.free_symbols - {c}, key=lambda symbol: symbol.name
)
specialization = {symbol: index + 1 for index, symbol in enumerate(free_symbols)}
specialized_determinant = sp.factor(invariant_determinant.subs(specialization))

x = sp.symbols("x")
checks = {
    "relative_matrix_exact": relative == expected,
    "reciprocal_characteristic_polynomial": sp.expand(
        relative.charpoly(x).as_expr()
        - (x - 1) ** 3 * (x - sp.Rational(9, 5)) * (x - sp.Rational(5, 9))
    )
    == 0,
    "invariant_form_exact": sp.simplify(
        relative.T * invariant_form * relative - invariant_form
    )
    == sp.zeros(5),
    "determinant_not_identically_zero": invariant_determinant != 0,
    "nondegenerate_specialization_exists": specialized_determinant != 0,
}

result = {
    "schema": "marici.fifth_channel_split_comparison.v1",
    "checks": checks,
    "exact": {
        "relative_matrix": str(relative),
        "relative_spectrum": ["1", "1", "1", "9/5", "5/9"],
        "invariant_form_determinant": str(invariant_determinant),
        "specialized_determinant": str(specialized_determinant),
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/fifth_channel_split_comparison.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
