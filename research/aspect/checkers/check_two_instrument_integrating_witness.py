#!/usr/bin/env python3
"""Finite integrating witness for two instrument occurrences."""

import itertools
import json
from pathlib import Path

OCCURRENCES = ("L", "R")
VALID_EDGE = ("L", "R")
MALFORMED_EDGE = ("L", "missing")
LOCAL_STATES = tuple(itertools.product((0, 1), repeat=2))
ATTACHMENTS = {"S0": ("bare0", "joint0"), "S1": ("bare1", "joint1")}


def pullback(attachment):
    return {"bare1": "bare0", "joint1": "joint0"}[attachment]


def edge_well_typed(edge):
    return edge[0] in OCCURRENCES and edge[1] in OCCURRENCES


def continuation_coherent(state):
    left, right = state
    return left == right


def readout(state):
    left, right = state
    return left ^ right


def extra_probe(state):
    return state[0]


def combined(state):
    return readout(state), extra_probe(state)


MATCHING = tuple(state for state in LOCAL_STATES if continuation_coherent(state))
readout_fibers = {}
combined_fibers = {}
for state in MATCHING:
    readout_fibers.setdefault(readout(state), []).append(state)
    combined_fibers.setdefault(combined(state), []).append(state)
kernel_pair = tuple((left, right) for left in MATCHING for right in MATCHING if readout(left) == readout(right))
checks = {
    "two_occurrences_are_distinct": len(set(OCCURRENCES)) == 2,
    "valid_continuation_edge_is_typed": edge_well_typed(VALID_EDGE),
    "malformed_edge_is_rejected_structurally": not edge_well_typed(MALFORMED_EDGE),
    "joint_attachment_reindexes": pullback("joint1") == "joint0",
    "bare_attachment_reindexes": pullback("bare1") == "bare0",
    "cross_system_joint_transport_exists": "joint0" == pullback("joint1"),
    "cross_system_incompatible_transport_rejected": "joint0" != pullback("bare1"),
    "local_product_has_four_states": len(LOCAL_STATES) == 4,
    "matching_object_has_two_states": set(MATCHING) == {(0, 0), (1, 1)},
    "locally_admissible_incoherent_state_rejected": (0, 1) in LOCAL_STATES and (0, 1) not in MATCHING,
    "coarse_readout_is_constant_on_matching_object": set(readout_fibers) == {0},
    "coarse_readout_has_unresolved_two_state_fiber": len(readout_fibers[0]) == 2,
    "kernel_pair_has_off_diagonal_pair": any(left != right for left, right in kernel_pair),
    "combined_probe_is_monic_on_matching_object": len(combined_fibers) == len(MATCHING) and all(len(value) == 1 for value in combined_fibers.values()),
    "coherence_precedes_readout": all(state in MATCHING for states in readout_fibers.values() for state in states),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.two-instrument-integrating-witness.v1", "status": "passed", "checks": checks, "local_states": LOCAL_STATES, "matching_states": MATCHING, "readout_fibers": readout_fibers, "kernel_pair": kernel_pair, "claim_boundary": "Finite integrating diagnostic; no general existence, physical realization, selection, or physical-time claim."}
output = Path(__file__).parents[1] / "results" / "two_instrument_integrating_witness.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "local_size": len(LOCAL_STATES), "matching_size": len(MATCHING), "coarse_fiber_size": len(readout_fibers[0])}, sort_keys=True))
