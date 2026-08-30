import json
from pathlib import Path

import sympy as sp


c = sp.symbols("c", positive=True)
q11, q12, q13, q22, q23, q33 = sp.symbols(
    "q11 q12 q13 q22 q23 q33", real=True
)
Q0 = sp.Matrix(
    [
        [q11, q12, q13],
        [q12, q22, q23],
        [q13, q23, q33],
    ]
)


def transfer(j):
    return sp.Matrix(
        [
            [j + sp.Rational(19, 4), -sp.Rational(3, 2) * (j + sp.Rational(5, 4)), 1],
            [1, 0, 0],
            [0, 0, c],
        ]
    )


M0 = transfer(0)
M1 = transfer(1)
Q1 = sp.simplify(M0.inv().T * Q0 * M0.inv())
Q2 = sp.simplify(M1.inv().T * Q1 * M1.inv())
P2 = M1 * M0
Q2_closed = sp.simplify(P2.inv().T * Q0 * P2.inv())

d = sp.Integer(3)
det0 = sp.factor(M0.det())
normalized_det_cubed = sp.simplify(
    (det0 ** (-sp.Rational(1, 3))) ** d * det0
)

checks = {
    "first_pullback_identity": sp.simplify(M0.T * Q1 * M0 - Q0) == sp.zeros(3),
    "second_pullback_identity": sp.simplify(M1.T * Q2 * M1 - Q1) == sp.zeros(3),
    "closed_transport_formula": sp.simplify(Q2 - Q2_closed) == sp.zeros(3),
    "determinant_congruence": sp.simplify(
        Q1.det() - Q0.det() / M0.det() ** 2
    ) == 0,
    "special_linear_normalization": normalized_det_cubed == 1,
}

result = {
    "schema": "marici.moving_metric_chain_tautology.v1",
    "checks": checks,
    "exact": {
        "det_M0": str(det0),
        "det_Q1_over_Q0": str(sp.factor(Q1.det() / Q0.det())),
        "free_initial_metric_parameters": 6,
        "carrier_dimension": 3,
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/moving_metric_chain_tautology.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
