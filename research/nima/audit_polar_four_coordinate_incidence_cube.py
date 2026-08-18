#!/usr/bin/env python3
"""Enumerate the complete E,P3,a,b normal-jet cube of Q_±."""

import itertools
import json
from pathlib import Path


VARIABLES = ("E", "P3", "a", "b")


def main():
    strata = []
    for size in range(5):
        for subset in itertools.combinations(VARIABLES, size):
            vanished = set(subset)
            complement = [v for v in VARIABLES if v not in vanished]
            anti_jet = "2" if not complement else "2*" + "*".join(complement)
            # Differentiating 2*E*P3*a*b in every vanished normal leaves
            # twice the product of the complementary coordinates.
            assert len(vanished) + len(complement) == 4

            if not {"a", "b"}.issubset(vanished):
                diagonal_jet = "restriction of C"
                diagonal_order = 0
            elif "E" in vanished:
                diagonal_jet = "d_a^2 C=-2*P1^2 (or d_b^2 C=2*P2^2)"
                diagonal_order = 2
            else:
                diagonal_jet = "d_a^2 C=2*(E^2-P1^2) (or d_b^2 C=2*(P2^2-E^2))"
                diagonal_order = 2

            strata.append({
                "vanished": list(subset),
                "codimension": size,
                "diagonal_jet": diagonal_jet,
                "diagonal_order": diagonal_order,
                "anti_diagonal_mixed_jet": anti_jet,
                "anti_diagonal_order": size,
                "generic_rank": 2,
            })

    assert len(strata) == 16
    assert strata[-1]["anti_diagonal_mixed_jet"] == "2"
    assert all(row["generic_rank"] == 2 for row in strata)

    packet = {
        "variables": VARIABLES,
        "labelled_decomposition": {
            "common": "C=E^2*(a^2-b^2)-P1^2*a^2+P2^2*b^2",
            "odd": "M=2*E*P3*a*b",
            "factors": ["Q_+=C+M", "Q_-=C-M"],
        },
        "stratum_count": len(strata),
        "all_strata_generic_rank": 2,
        "deepest_anti_diagonal_jet": "d_E d_P3 d_a d_b M=2",
        "deepest_diagonal_jet": "d_a^2 C=-2*P1^2 or d_b^2 C=2*P2^2",
        "generic_total_cone_dimension": 0,
        "remaining_failure_support": ["P1=0 and P2=0", "signed endpoints E^2=P1^2 or E^2=P2^2 when only one diagonal jet is used"],
        "strata": strata,
    }
    out = Path(__file__).with_name("polar-four-coordinate-incidence-cube.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
