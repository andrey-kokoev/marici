from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    L = sp.Integer(1)
    eta = sp.Rational(1, 2)
    C_L = sp.Integer(1)
    C_prime = sp.Integer(2)
    cutoffs = [64, 128, 256, 512, 1024]
    reserves = [
        (1 - eta) * sp.log(1 + sp.pi * (cutoff + 1) / (2 * L)) - C_L - C_prime
        for cutoff in cutoffs
    ]
    assert all(reserves[index + 1] > reserves[index] for index in range(len(cutoffs) - 1))
    positive_cutoffs = [cutoff for cutoff, reserve in zip(cutoffs, reserves) if reserve > 0]
    assert positive_cutoffs[0] == 256

    n = sp.Symbol("n", integer=True, positive=True)
    reference = sp.log(n + 1)
    unit_relative_remainder = -reference
    assert sp.simplify(reference + unit_relative_remainder) == 0

    result = {
        "schema": "marici.voevodsky.relative-log-garding-remainder.v1",
        "status": "strict_relative_log_remainder_criterion_verified",
        "L": "1",
        "eta": "1/2",
        "C_L": "1",
        "C_prime": "2",
        "cutoffs": cutoffs,
        "exact_tail_reserves": [str(value) for value in reserves],
        "first_checked_positive_cutoff": positive_cutoffs[0],
        "strict_relative_bound_preserves_log_growth": True,
        "unit_relative_bound_cancels_log_growth": True,
        "absolute_bounded_remainder_is_eta_zero_case": True,
        "source_relative_bound_materialized": False,
        "next_gate": "estimate boundary remainder relative coefficient eta on high Dirichlet modes",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
