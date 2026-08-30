#!/usr/bin/env python3
"""Exact bounded census supporting the all-finite-order seam-jet hostile."""

from fractions import Fraction
import json
from pathlib import Path


def main() -> int:
    rows = []
    passed = True
    for m in range(65):
        k = m // 2 + 1
        exponent = 2 * k
        derivative_factor = (
            Fraction(2)
            * Fraction(1, 2) ** (2 * k - 1)
            * (Fraction(k) - Fraction(1, 4))
        )
        row = {
            "jet_order": m,
            "k": k,
            "vanishing_order": exponent,
            "vanishes_through_declared_jet": exponent > m,
            "derivative_factor_at_q_half": str(derivative_factor),
            "positive_off_seam_direction": derivative_factor > 0,
        }
        passed = passed and all(
            [
                row["vanishes_through_declared_jet"],
                row["positive_off_seam_direction"],
            ]
        )
        rows.append(row)

    result = {
        "schema": "marici.grothendieck.finite-seam-jet-nonselection.v1",
        "status": "passed" if passed else "failed",
        "classification": "every_finite_static_germ_leaves_dynamic_flow_unselected",
        "checked_orders": [0, 64],
        "rows": rows,
        "general_proof":
            "h_K=q^(2K)exp(-q^2), K=floor(m/2)+1, has zero derivatives through m and positive derivative on 0<q<sqrt(K)",
        "deliberate_failure": {
            "claim": "some finite seam jet plus positivity and evenness selects global nonincrease",
            "witness_family": "h_K(q)=q^(2K)exp(-q^2)",
            "nonzero_obstruction_at_every_checked_order": passed,
        },
        "missing_constructor":
            "source-derived closure of the entire theta jet tower",
        "next_falsifier":
            "preserve a proposed all-order recurrence while changing the first off-seam variation minor",
    }
    output = (
        Path(__file__).parents[1]
        / "results"
        / "finite_seam_jet_nonselection.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "classification": result["classification"],
        "checked_count": len(rows),
        "first": rows[0],
        "last": rows[-1],
    }, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
