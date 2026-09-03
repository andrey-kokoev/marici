from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    cutoffs = [sp.Integer(2) ** exponent for exponent in range(1, 11)]
    admitted_residuals = [sp.log(M) / M - sp.Integer(1) / M**2 for M in cutoffs]
    hostile_residuals = [sp.log(M) / M**3 - sp.Integer(1) / M**2 for M in cutoffs]
    assert all(residual > 0 for residual in admitted_residuals)
    assert all(residual < 0 for residual in hostile_residuals)

    M = sp.Symbol("M", positive=True)
    p, q = sp.symbols("p q", real=True)
    ratio_shape = M ** (p - 2 * q) / sp.log(M)

    result = {
        "schema": "marici.voevodsky.finite-tail-schur-rate-criterion.v1",
        "status": "finite_tail_rate_gate_verified",
        "cutoffs": [int(value) for value in cutoffs],
        "admitted_exponents": {"p": 1, "q": 1, "two_q_minus_p": 1},
        "admitted_residuals": [str(value) for value in admitted_residuals],
        "admitted_all_positive": True,
        "hostile_exponents": {"p": 3, "q": 1, "two_q_minus_p": -1},
        "hostile_residuals": [str(value) for value in hostile_residuals],
        "hostile_all_negative": True,
        "schur_ratio_shape": str(ratio_shape),
        "asymptotic_success_condition": "2*q >= p",
        "sobolev_coupling_rate_available_conditionally": True,
        "finite_pivot_decay_rate_materialized": False,
        "next_gate": "certified Galerkin estimates for finite pivot decay exponent p",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
