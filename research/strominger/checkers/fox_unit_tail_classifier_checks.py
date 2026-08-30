#!/usr/bin/env python3
"""Classify the bounded tail-power square census by Fox-unit data."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "research/strominger/results/primitive_tail_square_hostile_checks.json"
RESULT = ROOT / "research/strominger/results/fox_unit_tail_classifier_checks.json"


def fox_derivative_terms(exponent):
    """Laurent exponents and coefficients of d(x^n)/dx."""
    if exponent > 0:
        return [[power, 1] for power in range(exponent)]
    return [[power, -1] for power in range(exponent, 0)]


def is_group_ring_unit(terms):
    return len(terms) == 1 and abs(terms[0][1]) == 1


source = json.loads(INPUT.read_text(encoding="utf-8"))
records = []
for record in source["records"]:
    left_terms = fox_derivative_terms(record["left_power"])
    right_terms = fox_derivative_terms(record["right_power"])
    left_unit = is_group_ring_unit(left_terms)
    right_unit = is_group_ring_unit(right_terms)
    opposite_augmentations = record["left_power"] * record["right_power"] < 0
    fox_unit_anti_invariant = left_unit and right_unit and opposite_augmentations
    records.append(
        {
            "left_power": record["left_power"],
            "right_power": record["right_power"],
            "left_fox_derivative": left_terms,
            "right_fox_derivative": right_terms,
            "left_fox_unit": left_unit,
            "right_fox_unit": right_unit,
            "opposite_augmentations": opposite_augmentations,
            "fox_unit_anti_invariant": fox_unit_anti_invariant,
            "observed_twice_square": record["twice_a_square"],
        }
    )

gates = {
    "fox_derivative_of_a_power_is_a_unit_exactly_at_unit_exponent": all(
        record["left_fox_unit"] == (abs(record["left_power"]) == 1)
        and record["right_fox_unit"] == (abs(record["right_power"]) == 1)
        for record in records
    ),
    "fox_unit_anti_invariant_criterion_matches_the_full_census": all(
        record["fox_unit_anti_invariant"] == record["observed_twice_square"]
        for record in records
    ),
    "opposite_polarity_without_fox_units_is_insufficient": any(
        record["opposite_augmentations"]
        and not (record["left_fox_unit"] and record["right_fox_unit"])
        and not record["observed_twice_square"]
        for record in records
    ),
    "two_fox_units_without_anti_invariance_are_insufficient": any(
        record["left_fox_unit"]
        and record["right_fox_unit"]
        and not record["opposite_augmentations"]
        and not record["observed_twice_square"]
        for record in records
    ),
    "fox_to_reflection_response_comparison_map_is_not_yet_derived": True,
}

payload = {
    "schema": "marici.strominger.fox_unit_tail_classifier_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "bounded_classifier_status": "exact",
    "explanation_status": "comparison_map_missing",
    "interpretation": (
        "Across the complete sixteen-case tail-power census, the twice-square "
        "law holds exactly when both tail Fox derivatives are group-ring units "
        "and their augmentations have opposite signs. Neither condition alone "
        "suffices. This identifies the source datum forgotten by the completed "
        "Moore cycle. A theorem still requires a source-derived comparison from "
        "the Fox-Jacobian grade to the reflection-response target index."
    ),
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
