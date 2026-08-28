#!/usr/bin/env python3
"""Exact checker for the WP982 one-coupling balance gate."""

from fractions import Fraction
import json
from pathlib import Path


def exponent(s, p, q, r):
    return 2 * s + 4 * p - q - 5 * r


def rho_hat(prefactor, g, e):
    return prefactor * g**e


crossing = Fraction(24696)
prefactor = Fraction(8**2 * 5**4)

natural = (0, 1, 2, 2)
balanced = (0, 1, 4, 0)
e_natural = exponent(*natural)
e_balanced = exponent(*balanced)

natural_g1 = rho_hat(prefactor, Fraction(1), e_natural)
natural_g2 = rho_hat(prefactor, Fraction(2), e_natural)
balanced_g1 = rho_hat(prefactor, Fraction(1), e_balanced)
balanced_g7 = rho_hat(prefactor, Fraction(7), e_balanced)

alternative_prefactor = Fraction(8**2 * 4**4)

checks = {
    "natural_same_coupling_pattern_has_exponent_minus_eight": e_natural == -8,
    "natural_g1_is_40000": natural_g1 == 40000,
    "natural_g2_is_625_over_4": natural_g2 == Fraction(625, 4),
    "natural_pair_straddles_crossing": natural_g2 < crossing < natural_g1,
    "balanced_pattern_has_zero_exponent": e_balanced == 0,
    "balanced_pattern_removes_g_dependence": balanced_g1 == balanced_g7,
    "zero_exponent_does_not_fix_prefactor": prefactor != alternative_prefactor,
}

result = {
    "schema": "marici.flavor.one-coupling-balance-gate.v1",
    "work_package": "WP982",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "exponent": "E=2s+4p-q-5r",
    "necessary_gate": "E=0",
    "second_gate": "source fixes Gamma^2*A^4/(B*C^5) independently",
    "hostile_pattern": {
        "s_p_q_r": list(natural),
        "E": str(e_natural),
        "rho_hat_g_1": str(natural_g1),
        "rho_hat_g_2": str(natural_g2),
        "crossing": str(crossing),
    },
    "balanced_pattern": {
        "s_p_q_r": list(balanced),
        "E": str(e_balanced),
        "shared_value_for_selected_prefactor": str(balanced_g1),
    },
    "classification": "one-coupling origin is not a selector without exponent balance and fixed prefactor",
    "remaining_gate": (
        "derive both balance and prefactor from an admitted source completion, "
        "then pass coupled-vacuum and instrument tests"
    ),
}

out = Path("research/flavor/results/wp982_one_coupling_balance_gate.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
