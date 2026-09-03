from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/finite-difference-complete-monotonicity-gate-v1.json")


def difference(H: sp.Expr, t: sp.Symbol, h: sp.Symbol, order: int) -> sp.Expr:
    return sp.simplify(sum(
        (-1) ** j * sp.binomial(order, j) * H.subs(t, t + j * h)
        for j in range(order + 1)
    ))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, h, lam = sp.symbols("t h lam", positive=True, real=True)
    atom = sp.exp(-t * lam)

    for order in range(7):
        observed = difference(atom, t, h, order)
        expected = sp.exp(-t * lam) * (1 - sp.exp(-h * lam)) ** order
        assert sp.simplify(observed - expected) == 0
        derivative_limit = sp.limit(observed / h**order, h, 0, dir="+")
        expected_derivative = (-1) ** order * sp.diff(atom, t, order)
        assert sp.simplify(derivative_limit - expected_derivative) == 0

    # Scalar positivity alone misses a negative spectral atom.
    hostile = 1 - sp.Rational(1, 2) * sp.exp(-sp.pi**2 * t)
    assert sp.limit(hostile, t, 0, dir="+") == sp.Rational(1, 2)
    assert sp.diff(hostile, t).is_positive
    first_difference = sp.simplify(difference(hostile, t, h, 1))
    hostile_expected = -sp.Rational(1, 2) * sp.exp(-sp.pi**2 * t) * (1 - sp.exp(-sp.pi**2 * h))
    assert sp.simplify(first_difference - hostile_expected) == 0

    # The positive two-atom fixture has explicitly positive factors at every checked order.
    positive = 1 + sp.Rational(1, 2) * sp.exp(-sp.pi**2 * t)
    positive_differences = [difference(positive, t, h, order) for order in range(7)]
    assert positive_differences[0].is_positive
    for order in range(1, 7):
        expected = sp.Rational(1, 2) * sp.exp(-sp.pi**2 * t) * (1 - sp.exp(-sp.pi**2 * h)) ** order
        assert sp.simplify(positive_differences[order] - expected) == 0

    status = contract["status"]
    assert status["explicit_arithmetic_difference_positivity"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.finite-difference-complete-monotonicity-gate-check.v1",
        "status":"difference_hierarchy_verified",
        "spectral_factor_orders_checked":7,
        "derivative_limits_checked":7,
        "positive_scalar_hostile_fails_first_difference":True,
        "positive_atomic_fixture_orders_checked":7,
        "explicit_arithmetic_difference_positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
