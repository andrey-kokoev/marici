from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/order-two-stieltjes-divided-difference-bridge-v1.json")


def principal_nonnegative(matrix: sp.Matrix) -> bool:
    for size in range(1, matrix.rows + 1):
        for subset in itertools.combinations(range(matrix.rows), size):
            if matrix.extract(subset, subset).det() < 0:
                return False
    return True


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    x, tau = sp.symbols("x tau", positive=True, real=True)
    r_values = [sp.Rational(0), sp.Rational(2)]
    weights = [sp.Rational(3), sp.Rational(5)]

    H_prime = sum(weight / (x + r) ** 2 for r, weight in zip(r_values, weights))
    q = []
    for order in range(7):
        derivative_moment = sp.simplify(
            (-1) ** order * sp.diff(H_prime, x, order) / sp.factorial(order + 1)
        )
        direct_moment = sum(
            weight / (x + r) ** (order + 2)
            for r, weight in zip(r_values, weights)
        )
        assert sp.simplify(derivative_moment - direct_moment) == 0
        q.append(direct_moment)

    size = 3
    M0 = sp.Matrix(size, size, lambda i, j: q[i + j])
    My = sp.Matrix(size, size, lambda i, j: q[i + j + 1])
    Mloc = sp.simplify(M0 / x - My)
    y_values = [1 / (x + r) for r in r_values]
    V = sp.Matrix([[value**i for value in y_values] for i in range(size)])
    W2 = sp.diag(*(weight * value**2 for value, weight in zip(y_values, weights)))
    Y = sp.diag(*y_values)
    assert sp.simplify(M0 - V * W2 * V.T) == sp.zeros(size)
    assert sp.simplify(My - V * W2 * Y * V.T) == sp.zeros(size)
    assert sp.simplify(Mloc - V * W2 * (sp.eye(2) / x - Y) * V.T) == sp.zeros(size)

    # Exact rational x fixture verifies all principal minors of the three cones.
    for matrix in (M0, My, Mloc):
        assert principal_nonnegative(matrix.subs(x, sp.Rational(3, 2)))

    # Taylor identity for the divided difference through order five.
    H = sum(-weight / (x + r) for r, weight in zip(r_values, weights))
    divided = sp.simplify((H - H.subs(x, x - tau)) / tau)
    series = sp.series(divided, tau, 0, 6).removeO()
    expected_series = sum(q[k] * tau**k for k in range(6))
    assert sp.simplify(series - expected_series) == 0

    status = contract["status"]
    assert status["source_positive_measure"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.order-two-stieltjes-divided-difference-bridge-check.v1",
        "status":"stieltjes_hausdorff_bridge_verified",
        "factorial_moment_orders_checked":7,
        "three_cone_atomic_factorizations":True,
        "divided_difference_orders_checked":6,
        "scaled_positive_contraction_support":True,
        "source_positive_measure":False,
        "positive_J_fraction":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
