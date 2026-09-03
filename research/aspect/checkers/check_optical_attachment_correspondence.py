#!/usr/bin/env python3
"""Finite relational composition diagnostic for optical attachment lifts."""

import json
from pathlib import Path

MODE = ("out", "visible", "H")


def lifts(source_ports, port_map, target_attachment):
    occurrence, target_port, acceptance = target_attachment
    return frozenset(
        (occurrence, source_port, acceptance)
        for source_port, mode in source_ports.items()
        if port_map.get(source_port) == target_port and mode == acceptance
    )


def lift_attachment(source_ports, port_map, intermediate_attachment):
    occurrence, intermediate_port, acceptance = intermediate_attachment
    return lifts(source_ports, port_map, (occurrence, intermediate_port, acceptance))


def compose_maps(left_to_middle, middle_to_target):
    return {left: middle_to_target[middle] for left, middle in left_to_middle.items() if middle in middle_to_target}


TARGET_ATTACHMENT = ("det", "p", MODE)
MIDDLE_PORTS = {"a": MODE, "b": MODE}
MIDDLE_TO_TARGET = {"a": "p", "b": "p"}
LEFT_PORTS = {"x": MODE, "y": MODE}
LEFT_TO_MIDDLE = {"x": "a", "y": "b"}
DIRECT_MAP = compose_maps(LEFT_TO_MIDDLE, MIDDLE_TO_TARGET)

middle_lifts = lifts(MIDDLE_PORTS, MIDDLE_TO_TARGET, TARGET_ATTACHMENT)
iterated = frozenset(
    left_lift
    for middle_lift in middle_lifts
    for left_lift in lift_attachment(LEFT_PORTS, LEFT_TO_MIDDLE, middle_lift)
)
direct = lifts(LEFT_PORTS, DIRECT_MAP, TARGET_ATTACHMENT)

deletion_lifts = lifts({}, {}, TARGET_ATTACHMENT)
cartesian_lifts = lifts({"u": MODE}, {"u": "p"}, TARGET_ATTACHMENT)
fabricated_choice = frozenset(sorted(middle_lifts)[:1])
replicated_attachment = frozenset({("det-copy-1", "a", MODE), ("det-copy-2", "b", MODE)})

checks = {
    "branching_retains_two_middle_lifts": len(middle_lifts) == 2,
    "no_branch_is_selected": {lift[1] for lift in middle_lifts} == {"a", "b"},
    "direct_transport_retains_two_left_lifts": {lift[1] for lift in direct} == {"x", "y"},
    "relational_composition_equals_direct_transport": iterated == direct,
    "deletion_is_empty_correspondence": deletion_lifts == frozenset(),
    "cartesian_map_is_singleton_correspondence": len(cartesian_lifts) == 1,
    "fabricated_choice_loses_lawful_support": fabricated_choice < middle_lifts,
    "branching_does_not_create_replication": all(lift[0] == "det" for lift in middle_lifts) and replicated_attachment != middle_lifts,
    "occurrence_identity_survives_composition": all(lift[0] == "det" for lift in direct),
    "composition_preserves_acceptance_type": all(lift[2] == MODE for lift in direct),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.optical-attachment-correspondence.v1", "status": "passed", "checks": checks, "middle_lifts": sorted(middle_lifts), "direct_lifts": sorted(direct), "iterated_lifts": sorted(iterated), "deletion_lifts": sorted(deletion_lifts), "cartesian_lifts": sorted(cartesian_lifts), "claim_boundary": "Finite discrete correspondence witness; replication and continuous optical modes are outside scope."}
output = Path(__file__).parents[1] / "results" / "optical_attachment_correspondence.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "branch_count": len(middle_lifts), "direct_count": len(direct)}, sort_keys=True))
