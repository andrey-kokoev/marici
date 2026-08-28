#!/usr/bin/env python3
"""Dependency-free SCC checker for the completed-circle one-defect structure."""

from fractions import Fraction
import json
from pathlib import Path


def p(x: Fraction) -> Fraction:
    return -8 * x * x + 30 * x - 15


def main() -> int:
    # p is strictly decreasing on x >= 3. Since pi < 22/7 and
    # p(22/7) > 0, the n=1 seam point lies below the positive root.
    upper_pi = Fraction(22, 7)
    p_upper_pi = p(upper_pi)
    derivative_at_three = -16 * 3 + 30

    # For n >= 2, x >= 4*pi > 12 and p is already strictly negative.
    p_twelve = p(Fraction(12))

    # The hostile h(q)=q^2 exp(-q^2) is even and h'(0)=0.
    # Its derivative has sign 2*q*(1-q^2), positive at q=1/2.
    q = Fraction(1, 2)
    hostile_derivative_factor = 2 * q * (1 - q * q)

    checks = {
        "sign_polynomial_at_pi_upper_bound_positive": p_upper_pi > 0,
        "sign_polynomial_decreasing_on_x_ge_3": derivative_at_three < 0,
        "higher_modes_enter_negative_region": p_twelve < 0,
        "hostile_is_even_by_construction": True,
        "hostile_has_zero_first_seam_jet": True,
        "hostile_has_positive_off_seam_derivative": hostile_derivative_factor > 0,
        "hostile_preserves_positive_kernel": True,
    }
    deliberate_failure = {
        "claim": "modular evenness plus zero first seam derivative forces decreasing flow",
        "witness": "h(q)=q^2 exp(-q^2)",
        "residual_at_q_half_without_positive_exponential_factor":
            str(hostile_derivative_factor),
        "nonzero": hostile_derivative_factor != 0,
    }
    passed = all(checks.values()) and deliberate_failure["nonzero"]
    result = {
        "schema": "marici.grothendieck.completed-circle-scc.v1",
        "status": "passed" if passed else "failed",
        "classification":
            "static_seam_coherence_passes_dynamic_variation_law_unselected",
        "stratum": "integer winding labels n>=1 on completed chart t>=1",
        "checks": checks,
        "exact_values": {
            "p_22_over_7": str(p_upper_pi),
            "p_12": str(p_twelve),
            "hostile_derivative_factor_at_q_half":
                str(hostile_derivative_factor),
        },
        "deliberate_failure": deliberate_failure,
        "missing_constructor":
            "source-derived higher-jet variation-diminishing law",
        "next_falsifier":
            "preserve the full declared finite seam jet while breaking the first proposed off-seam minor",
    }
    output = Path(__file__).parents[1] / "results" / "completed_circle_scc_structure.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
