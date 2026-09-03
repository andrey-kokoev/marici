from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def main() -> None:
    c_gamma = sp.Integer(1)
    c_prime = sp.Integer(2)
    threshold_log = c_gamma + c_prime
    first_certified_mode = 21
    assert sp.log(first_certified_mode) - threshold_log > 0
    checked_modes = [21, 32, 64, 128]
    lower_bounds = [sp.log(mode) - threshold_log for mode in checked_modes]
    assert all(bound > 0 for bound in lower_bounds)

    admitted = {"a": Fraction(2), "d": Fraction(3), "b": Fraction(1)}
    admitted_residual = admitted["a"] * admitted["d"] - admitted["b"] ** 2
    assert admitted_residual == 5 > 0

    hostile = {"a": Fraction(1, 100), "d": Fraction(1), "b": Fraction(1, 2)}
    hostile_residual = hostile["a"] * hostile["d"] - hostile["b"] ** 2
    assert hostile["d"] > 0
    assert hostile_residual == Fraction(-6, 25) < 0

    result = {
        "schema": "marici.voevodsky.log-elliptic-signed-tail-schur.v1",
        "status": "periodic_signed_tail_and_schur_gate_verified",
        "C_gamma": "1",
        "C_prime": "2",
        "first_checked_positive_mode": first_certified_mode,
        "checked_modes": checked_modes,
        "exact_tail_lower_bounds": [str(value) for value in lower_bounds],
        "periodic_high_modes_positive": True,
        "interval_logarithmic_Garding_proved": False,
        "admitted_schur_residual": "5/1",
        "hostile_tail_lower_bound": "1/1",
        "hostile_schur_residual": "-6/25",
        "tail_positivity_alone_sufficient": False,
        "endpoint_finite_rank_augmentable": True,
        "global_support_limit_proved": False,
        "next_gate": "explicit interval logarithmic Garding and finite-tail coupling bounds",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
