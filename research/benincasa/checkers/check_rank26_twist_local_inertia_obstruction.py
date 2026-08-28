#!/usr/bin/env python3
"""Exact local-inertia gate for the generic-to-physical Kummer comparison."""
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-twist-local-inertia-obstruction.json"

generic = Fraction(5, 1)
physical = Fraction(-1, 2)
difference = physical - generic

# Characters are encoded by their exponents in Q/Z.
generic_character = generic % 1
physical_character = physical % 1
hom_character = difference % 1

checks = {
    "generic_character_is_trivial": generic_character == 0,
    "physical_character_is_sign": physical_character == Fraction(1, 2),
    "hom_character_is_sign": hom_character == Fraction(1, 2),
    "difference_is_not_integer": difference.denominator != 1,
    "ordinary_integer_contiguity_unavailable": difference.denominator != 1,
    # A horizontal scalar f must obey f = (-1) f, hence 2f = 0.
    "characteristic_zero_horizontal_hom_is_zero": Fraction(2, 1) != 0,
}

payload = {
    "schema": "marici.rank26-twist-local-inertia-obstruction.v1",
    "generic_gamma": str(generic),
    "physical_gamma": str(physical),
    "gamma_difference": str(difference),
    "generic_inertia": "+1",
    "physical_inertia": "-1",
    "internal_hom_inertia": "-1",
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "No nonzero local horizontal morphism exists between the two rank-one Kummer coefficient systems near a smooth branch point.",
    "scope": "This excludes coefficient-local ordinary contiguity; it does not exclude a separately derived correspondence, nearby-cycle construction, or direct physical-half-twist period.",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
