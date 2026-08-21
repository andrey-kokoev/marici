#!/usr/bin/env python3
"""Exact refinement obstruction to entropy descent from a positive scalar period."""

import json
from pathlib import Path

import sympy as sp


def main():
    # Generic positive normalized weights. The argument is independent of
    # their values and therefore applies to the 180 positive C5 summands.
    p, q = sp.symbols("p q", positive=True)
    coarse = [p, q]
    refined = [p / 2, p / 2, q / 2, q / 2]

    h_coarse = -sum(x * sp.log(x) for x in coarse)
    h_refined = -sum(x * sp.log(x) for x in refined)
    shift = sp.simplify((h_refined - h_coarse).subs(q, 1 - p))

    checks = {
        "refinement_preserves_total_weight": sp.simplify(sum(refined) - sum(coarse)) == 0,
        "uniform_refinement_preserves_label_symmetry": refined[0] == refined[1] and refined[2] == refined[3],
        "entropy_shift_is_log_two": sp.simplify(shift - sp.log(2)) == 0,
        "scalar_sum_does_not_determine_entropy": sp.simplify(shift) != 0,
    }

    payload = {
        "schema": "marici.cosmology-entropy-descent-obstruction.v1",
        "coarse_entropy": str(h_coarse),
        "refined_entropy": str(h_refined),
        "normalized_entropy_shift": str(shift),
        "checks": checks,
        "all_passed": all(checks.values()),
        "verdict": (
            "The positive scalar period C5 does not determine a Shannon entropy. "
            "A symmetry-preserving refinement leaves the period unchanged while "
            "shifting entropy by log(2). A source-declared outcome/effect algebra "
            "is required before the positive summands become probabilities."
        ),
    }

    out = Path(__file__).parents[1] / "results" / "cosmology-entropy-descent-obstruction.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
