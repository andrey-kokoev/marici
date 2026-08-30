#!/usr/bin/env python3
"""Finite reversibility and balanced-residue audit for pilot generators."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "interaction-net-reversible-lift-census.v1.json"
RESULT = ASPECT / "results" / "interaction_net_reversible_lift_census.json"

def injective(mapping):
    return len(set(mapping.values())) == len(mapping)

def compose(left, right, state):
    return left(right(state))

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    occurrence_total = {0: 1, 1: 1}
    occurrence_partial = {0: 1}
    depth = range(7)
    successor = {k: k + 1 for k in depth}
    target_depth = set(range(7))

    def o1(state):
        a, b = state
        return (1, b)

    def o2(state):
        a, b = state
        return (a, 1)

    boolean_states = [(a, b) for a in (0, 1) for b in (0, 1)]
    branch_equal = all(compose(o1, o2, s) == compose(o2, o1, s) for s in boolean_states)

    # A reversible dilation of totalized set-bit must retain the input bit.
    dilated = {(bit, 0): (1, bit) for bit in (0, 1)}
    garbage_distinguishes_input = dilated[(0, 0)][1] != dilated[(1, 0)][1]

    hostiles = {
        "totalized_occurrence_noninjective": not injective(occurrence_total),
        "partial_occurrence_only_proper_subspace": injective(occurrence_partial) and set(occurrence_partial) != {0, 1},
        "successor_not_surjective_on_declared_finite_target": set(successor.values()) != target_depth,
        "dilation_retains_environment_record": garbage_distinguishes_input,
        "minimal_balanced_pair_collapses_after_square": branch_equal,
        "physical_instantiation_not_promoted": contract["verdict"].startswith("balanced_word_theorem_not_physically")
    }
    passed = all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-reversible-lift-census-result.v1",
        "passed": passed,
        "occurrence_total_injective": injective(occurrence_total),
        "occurrence_partial_injective": injective(occurrence_partial),
        "successor_injective": injective(successor),
        "successor_surjective_on_declared_target": set(successor.values()) == target_depth,
        "dilation_garbage_distinguishes_input": garbage_distinguishes_input,
        "O1O2_equals_O2O1_on_all_boolean_states": branch_equal,
        "hostiles": hostiles,
        "verdict": contract["verdict"]
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
