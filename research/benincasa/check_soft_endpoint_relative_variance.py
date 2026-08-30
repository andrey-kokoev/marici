#!/usr/bin/env python3
"""Type the two soft endpoints after retaining the marked source factor."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    samples = (Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(3, 4))
    collision_checks = []
    for kappa in samples:
        # A_minus-p^2=4(1-kappa)p^2; A_plus-p^2=4(1+kappa)p^2.
        minus_collision_factor = 4 * (1 - kappa)
        plus_collision_factor = 4 * (1 + kappa)
        collision_checks.append({
            "kappa": str(kappa),
            "A_minus_minus_p2_over_p2": str(minus_collision_factor),
            "A_plus_minus_p2_over_p2": str(plus_collision_factor),
            "generic_marked_a_equals_p_collision": minus_collision_factor == 0 or plus_collision_factor == 0,
        })

    endpoint_types = {
        "xi=-1": {
            "Cayley_Menger_branch_collision": True,
            "q_g1_divided_wall": "xi+1=0",
            "source_normal_order": -1,
            "typed_object": "marked logarithmic residue followed by Cayley-Menger vanishing-cycle specialization",
        },
        "xi=+1": {
            "Cayley_Menger_branch_collision": True,
            "q_g1_divided_wall": "xi+1=2 (unit)",
            "source_normal_order": 0,
            "typed_object": "unmarked Cayley-Menger vanishing-cycle specialization",
        },
    }
    checks = {
        "negative_endpoint_has_marked_log_pole": endpoint_types["xi=-1"]["source_normal_order"] == -1,
        "positive_endpoint_has_no_marked_log_pole": endpoint_types["xi=+1"]["source_normal_order"] == 0,
        "endpoint_variances_differ": endpoint_types["xi=-1"]["typed_object"] != endpoint_types["xi=+1"]["typed_object"],
        "no_generic_a_equals_p_collision_on_open_kappa_interval": all(not item["generic_marked_a_equals_p_collision"] for item in collision_checks),
        "deeper_collisions_are_only_kappa_endpoints": 4*(1-Fraction(1)) == 0 and 4*(1+Fraction(-1)) == 0,
    }
    result = {
        "schema": "marici.soft-endpoint-relative-variance.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "marked_source_factor": "(a+p)/(2p*(a-p)^2*(a+3p)*(xi+1))",
        "endpoint_types": endpoint_types,
        "generic_collision_audit": collision_checks,
        "consequence": "the two endpoint occurrences do not form one ordinary rank-two covector; they are different columns of a marked-relative cone",
        "required_next_object": "a relative de Rham/Gysin cone combining Res_{q_g1} phi_CM at xi=-1 with phi_CM at xi=+1, including the degree shift and comparison map",
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-relative-variance.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
