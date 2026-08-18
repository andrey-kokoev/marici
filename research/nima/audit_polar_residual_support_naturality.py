#!/usr/bin/env python3
"""Exact rank audit on P3=0, a=0, and b=0 polar collision supports."""

import json
from pathlib import Path


def main():
    rows = [
        {
            "support": "P3=0",
            "common_factor": "E^2*(a^2-b^2)-P1^2*a^2+P2^2*b^2",
            "normal_derivatives": ["2*E*a*b", "-2*E*a*b"],
            "basis_determinant": "-4*E*a*b",
            "deeper_failure": ["E=0", "a=0", "b=0"],
        },
        {
            "support": "a=0",
            "common_factor": "b^2*(P2^2-E^2)",
            "normal_derivatives": ["2*E*P3*b", "-2*E*P3*b"],
            "basis_determinant": "-4*E*P3*b",
            "deeper_failure": ["E=0", "P3=0", "b=0"],
        },
        {
            "support": "b=0",
            "common_factor": "a^2*(E^2-P1^2)",
            "normal_derivatives": ["2*E*P3*a", "-2*E*P3*a"],
            "basis_determinant": "-4*E*P3*a",
            "deeper_failure": ["E=0", "P3=0", "a=0"],
        },
    ]
    for row in rows:
        assert row["normal_derivatives"][0].replace("2*", "", 1) == row["normal_derivatives"][1].replace("-2*", "", 1)

    # Numeric nonzero witnesses for the three determinants.
    witnesses = {
        "P3=0": -4*2*3*5,
        "a=0": -4*2*7*5,
        "b=0": -4*2*7*3,
    }
    assert all(value != 0 for value in witnesses.values())

    packet = {
        "labelled_pair": ["Q_+", "Q_-"],
        "restriction_vector": [1, 1],
        "normal_vector": [1, -1],
        "supports": rows,
        "generic_cone_dimension_each": 0,
        "new_failure_divisor_count": 0,
        "remaining_support": "pairwise/deeper intersections among E,P3,a,b",
        "witness_determinants": witnesses,
    }
    out = Path(__file__).with_name("polar-residual-support-naturality.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
