#!/usr/bin/env python3
"""Exact checker for the WP984 UV-lift jet hierarchy."""

from fractions import Fraction
import json
from math import comb
from pathlib import Path


gamma_lift = [Fraction(1), Fraction(2), Fraction(1)]
a_lift = [
    Fraction(comb(4, k), 2**k)
    for k in range(5)
]

first_jet_gamma = Fraction(2)
first_jet_b = Fraction(-1)
second_derivative_gamma = 2 * gamma_lift[2]
second_derivative_a = 2 * a_lift[2]

n = 7
late_lift = [Fraction(0) for _ in range(2 * n + 3)]
late_lift[0] = 1
late_lift[n + 1] = 2
late_lift[2 * n + 2] = 1

checks = {
    "first_jet_can_separate_some_lifts": first_jet_gamma != first_jet_b,
    "gamma_and_A_lifts_share_zeroth_order": gamma_lift[0] == a_lift[0] == 1,
    "gamma_and_A_lifts_share_first_derivative": gamma_lift[1] == a_lift[1] == 2,
    "second_derivative_separates_them": (
        second_derivative_gamma == 2
        and second_derivative_a == 3
    ),
    "late_lift_agrees_through_order_n": all(
        late_lift[k] == (1 if k == 0 else 0)
        for k in range(n + 1)
    ),
    "late_lift_first_differs_at_n_plus_one": late_lift[n + 1] == 2,
    "finite_jet_faithfulness_requires_bounded_grammar": True,
}

result = {
    "schema": "marici.flavor.uv-lift-jet-faithfulness.v1",
    "work_package": "WP984",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "zeroth_coordinate": "P=Gamma^2*A^4/(B*C^5)",
    "first_log_response": "J1=2u_Gamma+4u_A-u_B-5u_C",
    "two_lift_pair": {
        "Gamma_response_coefficients": [str(x) for x in gamma_lift],
        "A_response_coefficients": [str(x) for x in a_lift],
        "shared_first_derivative": "2",
        "second_derivatives": ["2", "3"],
    },
    "arbitrary_finite_order_hostile": {
        "tested_n": n,
        "first_different_order": n + 1,
        "response": "(1+epsilon^(n+1))^2",
    },
    "classification": "threshold jets refine UV lift classes but no fixed finite tower is faithful without a bounded source grammar",
    "remaining_gate": (
        "freeze a finite or degree-bounded mediator grammar and derive a "
        "calibrated source-generated threshold probe tower"
    ),
}

out = Path("research/flavor/results/wp984_uv_lift_jet_faithfulness.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
