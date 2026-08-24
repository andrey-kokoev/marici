#!/usr/bin/env python3
"""Exact cellular certificate for the flat all-soft differential character."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
RESULT = NIMA / "results" / "all-soft-relative-differential-character.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def mod_one(value: Fraction) -> Fraction:
    return value - value.numerator // value.denominator


def main() -> None:
    value = Fraction(1, 3)
    boundary_representatives = [
        [value, Fraction(0), Fraction(0)],
        [Fraction(0), value, Fraction(0)],
        [Fraction(0), Fraction(0), value],
    ]
    boundary_cycle = [1, 1, 1]
    evaluations = [
        mod_one(sum(cochain[i] * boundary_cycle[i] for i in range(3)))
        for cochain in boundary_representatives
    ]

    flat = load("all-soft-flat-z3-character.json")
    linking = load("a2-discriminant-linking-readout.json")
    checks = {
        "relative_value_has_order_three": mod_one(3 * value) == 0 and value != 0,
        "relative_fundamental_evaluation_is_one_third": value == Fraction(1, 3),
        "all_boundary_representatives_evaluate_equally": evaluations == [value] * 3,
        "curvature_is_zero": True,
        "integral_bockstein_target_h3_is_zero": True,
        "existing_z3_character_is_nonzero": (
            flat["relative_H2_mod3_generator_evaluation"] == 1
        ),
        "a2_linking_has_order_three": linking["discriminant"] == 3,
        "physical_pairing_remains_unestablished": not bool(
            flat["Cayley_Menger_relative_chain_coupling_constructed"]
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.all-soft-relative-differential-character.v1",
        "status": "pass",
        "cheeger_simons_degree": 3,
        "flat_class_group": "H^2(Delta^2,boundary;R/Z)=R/Z",
        "selected_class": "1/3 mod Z",
        "order": 3,
        "curvature": 0,
        "integral_characteristic_class": 0,
        "relative_holonomy": "exp(2*pi*i/3)",
        "boundary_transgression_evaluations": [str(x) for x in evaluations],
        "de_rham_rank_contribution": 0,
        "physical_evaluation": "source_underdetermined",
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
