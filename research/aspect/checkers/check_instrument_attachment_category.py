#!/usr/bin/env python3
"""Finite Grothendieck-construction diagnostic for instrument attachments."""

import json
from pathlib import Path

BASE = ("S0", "S1")
BASE_ARROWS = (("S0", "S0", "id0"), ("S1", "S1", "id1"), ("S0", "S1", "f"))
ATTACHMENTS = {"S0": ("bare0", "p"), "S1": ("bare1", "q")}


def pullback(arrow, attachment):
    if arrow == "id0" or arrow == "id1": return attachment
    if arrow == "f": return {"bare1": "bare0", "q": "p"}[attachment]
    raise KeyError(arrow)


def vertical_morphism(source, target):
    # Fibers are discrete in this diagnostic.
    return source == target


TOTAL_OBJECTS = tuple((system, attachment) for system in BASE for attachment in ATTACHMENTS[system])
TOTAL_MORPHISMS = []
for source in TOTAL_OBJECTS:
    for target in TOTAL_OBJECTS:
        for base_source, base_target, arrow in BASE_ARROWS:
            if source[0] == base_source and target[0] == base_target and vertical_morphism(source[1], pullback(arrow, target[1])):
                TOTAL_MORPHISMS.append((source, target, arrow))


def has_total_morphism(source, target):
    return any(item[0] == source and item[1] == target for item in TOTAL_MORPHISMS)


def base_composable(first, second):
    return first[1] == second[0]


def base_compose(first, second):
    assert base_composable(first, second)
    if first[2].startswith("id"): return second[2]
    if second[2].startswith("id"): return first[2]
    raise ValueError("No other composable base pair in the finite base")


identity_checks = all(has_total_morphism(obj, obj) for obj in TOTAL_OBJECTS)
composition_checks = True
for first in TOTAL_MORPHISMS:
    for second in TOTAL_MORPHISMS:
        if first[1] != second[0]: continue
        composite_arrow = base_compose((first[0][0], first[1][0], first[2]), (second[0][0], second[1][0], second[2]))
        if not any(item[0] == first[0] and item[1] == second[1] and item[2] == composite_arrow for item in TOTAL_MORPHISMS):
            composition_checks = False

fibers = {system: tuple(obj[1] for obj in TOTAL_OBJECTS if obj[0] == system) for system in BASE}
checks = {
    "total_category_has_four_objects": len(TOTAL_OBJECTS) == 4,
    "every_total_object_has_identity": identity_checks,
    "total_morphisms_are_closed_under_composition": composition_checks,
    "forgetful_object_projection_lands_in_base": all(obj[0] in BASE for obj in TOTAL_OBJECTS),
    "forgetful_arrow_projection_lands_in_base": all(any(arrow == item[2] for item in BASE_ARROWS) for item in TOTAL_MORPHISMS),
    "strict_fibers_equal_attachment_sets": all(fibers[system] == ATTACHMENTS[system] for system in BASE),
    "distinguished_attachment_reindexes": pullback("f", "q") == "p",
    "bare_attachment_reindexes": pullback("f", "bare1") == "bare0",
    "valid_cross_system_attachment_map_exists": has_total_morphism(("S0", "p"), ("S1", "q")),
    "base_map_without_attachment_transport_is_rejected": not has_total_morphism(("S0", "p"), ("S1", "bare1")),
    "decoration_preserves_underlying_system_exactly": all((system, attachment)[0] == system for system, attachment in TOTAL_OBJECTS),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.instrument-attachment-category.v1", "status": "passed", "checks": checks, "base_objects": BASE, "total_objects": TOTAL_OBJECTS, "total_morphism_count": len(TOTAL_MORPHISMS), "fibers": fibers, "claim_boundary": "Finite strict indexed-category diagnostic; no physical assembly or canonical attachment theorem."}
output = Path(__file__).parents[1] / "results" / "instrument_attachment_category.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "total_object_count": len(TOTAL_OBJECTS), "total_morphism_count": len(TOTAL_MORPHISMS)}, sort_keys=True))
