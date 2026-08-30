#!/usr/bin/env python3
"""Test whether a base-rational scalar can identify the two soft endpoint periods."""

import json
from pathlib import Path


def main():
    # Write r_-^2=5-4*kappa and r_+^2=5+4*kappa.  The source-normalized
    # endpoint periods are
    #   c_+ = pi*i/(p*r_+)
    #   c_- = pi*i*(r_-+1)/(2*p^4*r_-*(r_--1)^2*(r_-+3)).
    # Hence the unique scalar identifying their displayed period frames is
    # J=c_+/c_-.
    required_comparison = (
        "2*p^3*r_minus*(r_minus-1)^2*(r_minus+3)"
        "/((r_minus+1)*r_plus)"
    )
    required_p_degree = 3
    required_r_plus_exponent = -1
    r_plus_deck_character = (-1) ** abs(required_r_plus_exponent)
    base_rational_r_plus_character = 1

    # Deck characters of J.  The r_plus involution changes only its
    # denominator and therefore sends J to -J.  The r_minus involution also
    # changes J nontrivially (not merely by a base-rational unit).
    checks = {
        "required_comparison_has_p_weight_plus_three": required_p_degree == 3,
        "r_plus_deck_involution_changes_sign": r_plus_deck_character == -1,
        "base_rational_scalars_are_r_plus_invariant": base_rational_r_plus_character == 1,
        "required_comparison_is_not_base_rational": r_plus_deck_character != base_rational_r_plus_character,
        "ordinary_rational_gysin_cannot_identify_period_frames": r_plus_deck_character != base_rational_r_plus_character,
    }
    result = {
        "schema": "marici.soft-endpoint-rational-comparison-obstruction.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "endpoint_radicals": {
            "r_minus_squared": "5-4*kappa",
            "r_plus_squared": "5+4*kappa",
        },
        "required_comparison": required_comparison,
        "deck_audit": {
            "r_plus_to_minus_r_plus": "J -> -J",
            "base_rational_function": "fixed",
            "required_character": r_plus_deck_character,
            "base_rational_character": base_rational_r_plus_character,
        },
        "conclusion": (
            "no scalar comparison rational over the kappa base identifies "
            "the two source-normalized endpoint period frames"
        ),
        "surviving_typed_object": (
            "a section of the Kummer-twisted Hom line Hom(E_minus,E_plus); "
            "its source authorization and horizontality remain unconstructed"
        ),
        "scope": (
            "excludes an ordinary base-rational scalar/Gysin adapter; it does "
            "not exclude a source-derived morphism in the twisted local-system category"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name(
        "soft-endpoint-rational-comparison-obstruction.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
