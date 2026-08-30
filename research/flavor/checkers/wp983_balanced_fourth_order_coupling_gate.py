#!/usr/bin/env python3
"""Exact checker for the WP983 balanced fourth-order coupling gate."""

from fractions import Fraction
import json
from pathlib import Path


crossing = 24696


def exponent(s):
    return 2 * s - 8


balanced_s = 4
unit_prefactor = Fraction(1)
wp977_prefactor = Fraction(8**2)
lower_integer = 157
first_passing_integer = 158

checks = {
    "s_four_is_balanced": exponent(balanced_s) == 0,
    "neighbor_s_three_is_not_balanced": exponent(3) == -2,
    "neighbor_s_five_is_not_balanced": exponent(5) == 2,
    "unit_prefactor_is_below_crossing": unit_prefactor < crossing,
    "wp977_prefactor_is_64_and_below_crossing": (
        wp977_prefactor == 64 and wp977_prefactor < crossing
    ),
    "integer_157_fails_strict_crossing": lower_integer**2 == 24649 < crossing,
    "integer_158_is_first_strict_crossing": (
        first_passing_integer**2 == 24964 > crossing
        and lower_integer + 1 == first_passing_integer
    ),
}

result = {
    "schema": "marici.flavor.balanced-fourth-order-coupling-gate.v1",
    "work_package": "WP983",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "natural_mass_pattern": {"p": 1, "q": 2, "r": 2},
    "balance_equation": "E=2s-8=0",
    "unique_balanced_s": balanced_s,
    "post_balance_coordinate": "rho_hat=Gamma^2*A^4/(B*C^5)",
    "crossing": str(crossing),
    "unit_prefactor_value": str(unit_prefactor),
    "wp977_prefactor_value": str(wp977_prefactor),
    "smallest_integer_Gamma_for_unit_A_B_C": first_passing_integer,
    "classification": "fourth-order generation rigidifies the coupling exponent but does not select the prefactor",
    "remaining_gate": (
        "derive the balanced exponent and a crossing-sized prefactor from an "
        "explicit source model, then pass coupled-vacuum and instrument tests"
    ),
}

out = Path("research/flavor/results/wp983_balanced_fourth_order_coupling_gate.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
