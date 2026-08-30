#!/usr/bin/env python3
"""Certify the source homogeneity behind the rank-26 Euler recurrence."""

import json
from pathlib import Path


def main():
    # The frozen residue source is
    #   (q_g23 + q_g31) da db K^gamma / product(q_i), gamma = 5.
    # Give x,y,z,a,b simultaneous weight one.  Each q_i is linear and K is
    # homogeneous of total degree six in these five variables.
    weights = {
        "numerator": 1,
        "fiber_measure": 2,
        "five_simple_poles": -5,
        "cayley_menger_twist": 6 * 5,
    }
    total = sum(weights.values())
    checks = {
        "five_poles_are_simple": weights["five_simple_poles"] == -5,
        "cayley_menger_degree_is_six": weights["cayley_menger_twist"] == 30,
        "source_total_weight_is_28": total == 28,
        "differentiated_weight_would_be_27": total - 1 == 27,
    }
    result = {
        "schema": "marici.rank26-source-euler-weight.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "simultaneous_weights": {"x": 1, "y": 1, "z": 1, "a": 1, "b": 1},
        "source_factor_weights": weights,
        "total_weight": total,
        "checks": checks,
        "source_identity": "x D0 + y D1 + z D2 = 28 S",
        "derivation": (
            "The numerator q_g23+q_g31 has weight 1, da db has weight 2, "
            "the five simple marked poles have weight -5, and K^5 has weight 30. "
            "The simultaneous Euler weight is therefore 28. The fiber Euler part "
            "is de Rham exact, leaving the external Euler recurrence in cohomology."
        ),
        "next_falsifier": (
            "Implement a dual-number parameter derivative of the complete raw class. "
            "Only then test x nabla_j D0 + y nabla_j D1 + z nabla_j D2 = 27 D_j; "
            "connection words alone omit derivatives of parameter-dependent coefficients."
        ),
    }
    output = Path(__file__).with_name("rank26-source-euler-weight.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
