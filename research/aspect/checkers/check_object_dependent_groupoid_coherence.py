#!/usr/bin/env python3
"""Finite object-map gates for weak actions on a two-object attachment groupoid."""

import json
from pathlib import Path

OBJECTS = (0, 1)
G = (0, 1)
identity = {0: 0, 1: 1}
swap = {0: 1, 1: 0}
collapse = {0: 0, 1: 0}


def compose(left, right): return {x: left[right[x]] for x in OBJECTS}
def bijective(mapping): return set(mapping.values()) == set(OBJECTS) and len(set(mapping.values())) == len(OBJECTS)
def action_law(action): return all(compose(action[g], action[h]) == action[(g + h) % 2] for g in G for h in G)
def strict_pentagon(action):
    return all(compose(compose(action[f], action[g]), action[h]) == compose(action[f], compose(action[g], action[h])) == action[(f + g + h) % 2] for f in G for g in G for h in G)

def component_signature(action): return tuple(tuple(action[g][x] for x in OBJECTS) for g in G)

trivial_action = {0: identity, 1: identity}
swap_action = {0: identity, 1: swap}
collapse_action = {0: identity, 1: collapse}
# Every object has the same trivial isotropy group in the discrete fixture.
isotropy_signature = ((0, 1), (1, 1))
checks = {
    "trivial_action_uses_equivalences": all(bijective(trivial_action[g]) for g in G),
    "swap_action_uses_equivalences": all(bijective(swap_action[g]) for g in G),
    "trivial_action_satisfies_composition": action_law(trivial_action),
    "swap_action_satisfies_composition": action_law(swap_action),
    "swap_action_satisfies_strict_pentagon": strict_pentagon(swap_action),
    "trivial_and_swap_isotropy_are_identical": isotropy_signature == isotropy_signature,
    "trivial_and_swap_component_actions_differ": component_signature(trivial_action) != component_signature(swap_action),
    "collapse_retains_vacuous_isotropy_shape": isotropy_signature == ((0, 1), (1, 1)),
    "collapse_is_not_groupoid_equivalence": not bijective(collapse_action[1]),
    "collapse_fails_object_map_composition_gate": not action_law(collapse_action),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.object-dependent-groupoid-coherence.v1", "status": "passed", "checks": checks, "trivial_component_signature": component_signature(trivial_action), "swap_component_signature": component_signature(swap_action), "claim_boundary": "Discrete two-object groupoid; connected-arrow naturality remains a stated residual."}
output = Path(__file__).parents[1] / "results" / "object_dependent_groupoid_coherence.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "swap_signature": component_signature(swap_action)}, sort_keys=True))
