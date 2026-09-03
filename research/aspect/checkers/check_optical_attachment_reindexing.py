#!/usr/bin/env python3
"""Finite typed-port derivation and obstruction diagnostic for optical attachments."""

import json
from pathlib import Path

H = ("out", "visible", 1, "H")
V = ("out", "visible", 1, "V")
TARGET_PORTS = {"pH": H, "pV": V}
ATTACHMENT = {"detH": ("pH", H), "detV": ("pV", V)}


def pullback_attachment(source_ports, port_map, attachment=ATTACHMENT):
    pulled = {}
    obstructions = []
    for occurrence, (target_port, acceptance) in attachment.items():
        preimages = [source_port for source_port, image in port_map.items() if image == target_port and source_port in source_ports]
        if not preimages:
            obstructions.append((occurrence, "deletion"))
            continue
        if len(preimages) != 1:
            obstructions.append((occurrence, "branch_ambiguity"))
            continue
        source_port = preimages[0]
        if source_ports[source_port] != TARGET_PORTS[target_port] or source_ports[source_port] != acceptance:
            obstructions.append((occurrence, "mode_mismatch"))
            continue
        pulled[occurrence] = (source_port, acceptance)
    return pulled, tuple(obstructions)


source_ok = {"aH": H, "aV": V}
map_ok = {"aH": "pH", "aV": "pV"}
pulled_ok, errors_ok = pullback_attachment(source_ok, map_ok)

source_deleted = {"aH": H}
map_deleted = {"aH": "pH"}
_, errors_deleted = pullback_attachment(source_deleted, map_deleted)

source_branched = {"aH1": H, "aH2": H, "aV": V}
map_branched = {"aH1": "pH", "aH2": "pH", "aV": "pV"}
_, errors_branched = pullback_attachment(source_branched, map_branched)

source_mismatch = {"aH": V, "aV": V}
map_mismatch = {"aH": "pH", "aV": "pV"}
_, errors_mismatch = pullback_attachment(source_mismatch, map_mismatch)

# Composition of two admissible renamings.
middle_ports = {"mH": H, "mV": V}
map_middle_target = {"mH": "pH", "mV": "pV"}
left_ports = {"lH": H, "lV": V}
map_left_middle = {"lH": "mH", "lV": "mV"}
map_left_target = {source: map_middle_target[middle] for source, middle in map_left_middle.items()}
direct, direct_errors = pullback_attachment(left_ports, map_left_target)
middle, middle_errors = pullback_attachment(middle_ports, map_middle_target)
renamed_middle_attachment = {occurrence: (map_left_middle_inv, acceptance) for occurrence, (middle_port, acceptance) in middle.items() for map_left_middle_inv, image in map_left_middle.items() if image == middle_port}

checks = {
    "typed_bijective_map_admits_pullback": not errors_ok and set(pulled_ok) == set(ATTACHMENT),
    "occurrence_labels_are_preserved": set(pulled_ok) == {"detH", "detV"},
    "pulled_loci_are_unique": pulled_ok["detH"][0] == "aH" and pulled_ok["detV"][0] == "aV",
    "deletion_obstruction_detected": ("detV", "deletion") in errors_deleted,
    "branch_ambiguity_detected": ("detH", "branch_ambiguity") in errors_branched,
    "mode_mismatch_detected": ("detH", "mode_mismatch") in errors_mismatch,
    "hostile_maps_fail_distinct_gates": {errors_deleted[0][1], errors_branched[0][1], errors_mismatch[0][1]} == {"deletion", "branch_ambiguity", "mode_mismatch"},
    "admissible_renaming_composition_has_no_error": not direct_errors and not middle_errors,
    "direct_and_iterated_pullback_agree": direct == renamed_middle_attachment,
    "detector_acceptance_is_source_typed": all(TARGET_PORTS[target] == acceptance for target, acceptance in ATTACHMENT.values()),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.optical-attachment-reindexing.v1", "status": "passed", "checks": checks, "admissible_pullback": pulled_ok, "deletion_obstructions": errors_deleted, "branch_obstructions": errors_branched, "mode_obstructions": errors_mismatch, "claim_boundary": "Finite typed-port optical model; no continuous-field or laboratory realization theorem."}
output = Path(__file__).parents[1] / "results" / "optical_attachment_reindexing.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "obstruction_kinds": 3}, sort_keys=True))
