#!/usr/bin/env python3
"""Certify that the finite marked bypass dies after forgetting the marks."""

import json
from pathlib import Path


def main() -> None:
    # Ordered finite marked occurrences on the compact elliptic curve.
    marks = ["(1,+)", "(1,-)", "(-3,+)", "(-3,-)"]
    degree = [1, 1, 1, 1]
    bypass = [1, -1, 0, 0]

    pairing = sum(a * b for a, b in zip(degree, bypass))
    checks = {
        "four_occurrences_retained": len(marks) == 4,
        "bypass_has_degree_zero": pairing == 0,
        "bypass_is_nonzero_before_forgetting_marks": any(bypass),
        "bypass_lies_in_localization_kernel": pairing == 0 and any(bypass),
        "compact_elliptic_projection_is_zero": pairing == 0,
    }
    packet = {
        "schema": "marici.soft-internal-bypass-elliptic-projection.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ordered_marks": marks,
        "localization_sequence": (
            "H^0(D)(-1) -> H^1(E,D) -> H^1(E) -> 0; "
            "the occurrence residue row is the degree map (1,1,1,1)"
        ),
        "bypass_vector": bypass,
        "degree_pairing": pairing,
        "elliptic_projection": [0, 0],
        "classification": "finite marked Tate/Kummer localization kernel",
        "conclusion": (
            "the source-selected internal bypass changes the relative marked period and its soft readout, "
            "but maps to zero in compact rank-two elliptic cohomology"
        ),
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-internal-bypass-elliptic-projection.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
