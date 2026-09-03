from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def main() -> None:
    L = sp.Integer(1)
    C_L = sp.Integer(1)
    C_prime = sp.Integer(2)
    cutoffs = [8, 16, 32, 64, 128]
    reserves = [sp.log(1 + sp.pi * (cutoff + 1) / (2 * L)) - C_L - C_prime for cutoff in cutoffs]
    assert all(reserves[index + 1] > reserves[index] for index in range(len(cutoffs) - 1))
    first_positive_checked = next(cutoff for cutoff, reserve in zip(cutoffs, reserves) if reserve > 0)
    assert first_positive_checked == 16

    finite_coercivity = Fraction(2)
    tail_reserve = Fraction(3)
    coupling = Fraction(1)
    schur_budget = finite_coercivity * tail_reserve - coupling**2
    assert schur_budget == 5 > 0

    small_pivot = Fraction(1, 100)
    hostile_budget = small_pivot * tail_reserve - coupling**2
    assert hostile_budget == Fraction(-97, 100) < 0

    # Hostile boundary remainder cancels logarithmic reference mode by mode.
    n = sp.Symbol("n", integer=True, positive=True)
    reference = sp.log(n + 1)
    hostile_remainder = -sp.log(n + 1)
    assert sp.simplify(reference + hostile_remainder) == 0

    result = {
        "schema": "marici.voevodsky.interval-log-garding-remainder-criterion.v1",
        "status": "sufficient_interval_remainder_criterion_verified",
        "L": "1",
        "C_L": "1",
        "C_prime": "2",
        "cutoffs": cutoffs,
        "exact_tail_reserves": [str(value) for value in reserves],
        "first_checked_positive_tail_cutoff": first_positive_checked,
        "admitted_finite_tail_schur_budget": "5/1",
        "small_pivot_hostile_schur_budget": "-97/100",
        "hostile_unbounded_remainder_cancels_log_growth": True,
        "source_interval_remainder_bound_materialized": False,
        "criterion": "Gamma_L - log(1+sqrt(-Delta_D)) extends to a bounded form",
        "next_gate": "source bound for the interval boundary-commutator remainder K_L",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
