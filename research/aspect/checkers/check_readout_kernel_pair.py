#!/usr/bin/env python3
"""Finite readout-fiber, joint-monicity, and functor-faithfulness diagnostic."""

import itertools
import json
from pathlib import Path

STATES = ("a0", "a1", "b0", "b1")


def coarse(state):
    return state[0]


def index(state):
    return state[1]


def combined(state):
    return coarse(state), index(state)


def fibers(mapping):
    values = {}
    for state in STATES:
        values.setdefault(mapping(state), []).append(state)
    return values


def discrete_hom(source, target):
    return (f"id:{source}",) if source == target else ()


coarse_fibers = fibers(coarse)
index_fibers = fibers(index)
combined_fibers = fibers(combined)
kernel_pair = tuple((left, right) for left, right in itertools.product(STATES, repeat=2) if coarse(left) == coarse(right))
diagonal = tuple((state, state) for state in STATES)
# For a functor between discrete categories, every source hom-set has size zero or one;
# mapping two objects together does not make any individual hom-set map noninjective.
faithful_hom_maps = all(len(discrete_hom(left, right)) <= len(discrete_hom(coarse(left), coarse(right))) for left in STATES for right in STATES)
checks = {
    "coarse_readout_has_two_records": len(coarse_fibers) == 2,
    "coarse_readout_has_two_element_fibers": all(len(value) == 2 for value in coarse_fibers.values()),
    "index_probe_has_two_element_fibers": all(len(value) == 2 for value in index_fibers.values()),
    "coarse_readout_is_not_monic": len(kernel_pair) > len(diagonal),
    "kernel_pair_contains_off_diagonal_ambiguity": any(left != right for left, right in kernel_pair),
    "combined_probe_family_is_monic": len(combined_fibers) == len(STATES) and all(len(value) == 1 for value in combined_fibers.values()),
    "individual_nonmonic_probes_can_be_jointly_monic": max(map(len, coarse_fibers.values())) == 2 and max(map(len, index_fibers.values())) == 2 and len(combined_fibers) == 4,
    "coarse_discrete_functor_is_faithful_on_hom_sets": faithful_hom_maps,
    "faithful_functor_is_not_injective_on_objects": len({coarse(state) for state in STATES}) < len(STATES),
    "faithfulness_does_not_imply_state_reconstruction": faithful_hom_maps and len(kernel_pair) > len(diagonal),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.readout-kernel-pair.v1", "status": "passed", "checks": checks, "coarse_fibers": coarse_fibers, "index_fibers": index_fibers, "combined_fibers": {str(key): value for key, value in combined_fibers.items()}, "kernel_pair_size": len(kernel_pair), "diagonal_size": len(diagonal), "claim_boundary": "Finite set/discrete-category diagnostic; no physical record or selection claim."}
output = Path(__file__).parents[1] / "results" / "readout_kernel_pair.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "kernel_pair_size": len(kernel_pair), "combined_fiber_count": len(combined_fibers)}, sort_keys=True))
