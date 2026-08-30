#!/usr/bin/env python3
"""Derive the two-occurrence marked residue packet at xi=-1."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    def residue(a, p):
        return (a + p) / (2 * p * (a - p) ** 2 * (a + 3 * p))

    def f_plus(r, p):
        return residue(p * r, p)

    def f_minus(r, p):
        return residue(-p * r, p)

    def marked_plus(r, p):
        return f_plus(r, p) / (p * r)

    def marked_minus(r, p):
        return -f_minus(r, p) / (p * r)

    samples = [
        (Fraction(2), Fraction(1)),
        (Fraction(1, 2), Fraction(3)),
        (Fraction(4), Fraction(2)),
        (Fraction(-2), Fraction(5)),
    ]
    plus_formula = "(r+1)/(2*p^4*r*(r-1)^2*(r+3))"
    minus_formula = "(r-1)/(2*p^4*r*(r+1)^2*(3-r))"
    sample_rows = []
    for r, p in samples:
        plus = marked_plus(r, p)
        minus = marked_minus(r, p)
        sample_rows.append({
            "r": str(r),
            "p": str(p),
            "plus": str(plus),
            "minus": str(minus),
            "plus_after_deck_equals_minus": marked_plus(-r, p) == minus,
            "minus_after_deck_equals_plus": marked_minus(-r, p) == plus,
            "symmetric_nonzero": plus + minus != 0,
            "antisymmetric_nonzero": plus - minus != 0,
        })

    checks = {
        "plus_residue_formula": all(
            f_plus(r, p) == (r + 1) / (2 * p**3 * (r - 1) ** 2 * (r + 3))
            for r, p in samples
        ),
        "minus_residue_formula": all(
            f_minus(r, p) == (1 - r) / (2 * p**3 * (r + 1) ** 2 * (3 - r))
            for r, p in samples
        ),
        "deck_sends_plus_entry_to_minus_entry": all(row["plus_after_deck_equals_minus"] for row in sample_rows),
        "deck_sends_minus_entry_to_plus_entry": all(row["minus_after_deck_equals_plus"] for row in sample_rows),
        "packet_has_symmetric_component": all(row["symmetric_nonzero"] for row in sample_rows),
        "packet_has_antisymmetric_component": all(row["antisymmetric_nonzero"] for row in sample_rows),
    }
    result = {
        "schema": "marici.soft-endpoint-full-marked-occurrence-packet.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "collision_parameter": "r^2=5-4*kappa",
        "ordered_occurrences": ["a=+p*r", "a=-p*r"],
        "residue_coefficients_without_pi_i": [
            "(r+1)/(2*p^3*(r-1)^2*(r+3))",
            "(1-r)/(2*p^3*(r+1)^2*(3-r))",
        ],
        "marked_period_entries_without_pi_i": [plus_formula, minus_formula],
        "deck_transport": "r -> -r exchanges the two entries",
        "character_components_without_pi_i": {
            "symmetric": "marked_plus+marked_minus (generically nonzero)",
            "antisymmetric": "marked_plus-marked_minus (generically nonzero)",
        },
        "exact_samples": sample_rows,
        "conclusion": (
            "the full marked packet is deck-covariant and generically occupies both "
            "the invariant and anti-invariant occurrence characters"
        ),
        "next_gate": (
            "derive the physical-chain covector before selecting either character or "
            "comparing with the unmarked positive-endpoint packet"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-full-marked-occurrence-packet.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
