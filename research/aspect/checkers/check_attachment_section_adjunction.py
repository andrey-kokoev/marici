#!/usr/bin/env python3
"""Finite attachment-section and adjunction diagnostic."""

import json
from pathlib import Path

BASE_OBJECTS = ("S0", "S1")
BASE_HOMS = {("S0", "S0"): 1, ("S0", "S1"): 1, ("S1", "S1"): 1, ("S1", "S0"): 0}
FIBER = (0, 1)  # poset 0 < 1


def fiber_hom(source, target):
    return 1 if source <= target else 0


def reindex(_source, _target, attachment):
    return attachment


def total_hom(source_base, source_attachment, target_base, target_attachment):
    if BASE_HOMS[(source_base, target_base)] == 0:
        return 0
    pulled = reindex(source_base, target_base, target_attachment)
    return fiber_hom(source_attachment, pulled)


def section(choice):
    return {base: choice for base in BASE_OBJECTS}


free = section(0)
cofree = section(1)
free_adjunction = all(
    total_hom(source, free[source], target, attachment) == BASE_HOMS[(source, target)]
    for source in BASE_OBJECTS for target in BASE_OBJECTS for attachment in FIBER
)
cofree_adjunction = all(
    total_hom(source, attachment, target, cofree[target]) == BASE_HOMS[(source, target)]
    for source in BASE_OBJECTS for target in BASE_OBJECTS for attachment in FIBER
)
noninitial_free_counterexample = {
    "total_hom": total_hom("S0", cofree["S0"], "S0", 0),
    "base_hom": BASE_HOMS[("S0", "S0")],
}
checks = {
    "initial_choice_is_section": all(free[source] <= reindex(source, target, free[target]) for source, target in BASE_HOMS if BASE_HOMS[(source, target)]),
    "terminal_choice_is_section": all(cofree[source] <= reindex(source, target, cofree[target]) for source, target in BASE_HOMS if BASE_HOMS[(source, target)]),
    "initial_section_left_adjoint_to_projection": free_adjunction,
    "stable_terminal_section_right_adjoint_to_projection": cofree_adjunction,
    "noninitial_section_fails_free_adjunction": noninitial_free_counterexample == {"total_hom": 0, "base_hom": 1},
    "functoriality_does_not_imply_left_adjunction": cofree["S0"] == 1 and not bool(noninitial_free_counterexample["total_hom"]),
    "initial_is_not_terminal": fiber_hom(1, 0) == 0,
    "terminal_receives_unique_map": all(fiber_hom(value, 1) == 1 for value in FIBER),
    "initial_emits_unique_map": all(fiber_hom(0, value) == 1 for value in FIBER),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.attachment-section-adjunction.v1", "status": "passed", "checks": checks, "noninitial_free_counterexample": noninitial_free_counterexample, "claim_boundary": "Finite strict indexed-poset witness; no canonical physical instrument."}
output = Path(__file__).parents[1] / "results" / "attachment_section_adjunction.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "counterexample": noninitial_free_counterexample}, sort_keys=True))
