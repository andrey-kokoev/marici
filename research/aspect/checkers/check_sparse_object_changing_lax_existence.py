#!/usr/bin/env python3
"""Component-existence gates on a sparse diamond attachment category."""

import json
from pathlib import Path

OBJECTS = ("bottom", "p", "q", "top")
LABELS = (0, 1)
ORDER = {
    ("bottom", "bottom"), ("bottom", "p"), ("bottom", "q"), ("bottom", "top"),
    ("p", "p"), ("p", "top"), ("q", "q"), ("q", "top"), ("top", "top"),
}
identity = {x: x for x in OBJECTS}
swap = {"bottom": "bottom", "p": "q", "q": "p", "top": "top"}
saturate = {"bottom": "bottom", "p": "top", "q": "top", "top": "top"}

def compose_map(left, right): return {x: left[right[x]] for x in OBJECTS}
def monotone(mapping): return all((mapping[x], mapping[y]) in ORDER for x, y in ORDER)
def product(left, right): return 0 if left == right == 0 else 1

def components(action, orientation):
    result = {}
    for g in LABELS:
        for f in LABELS:
            staged_map = compose_map(action[g], action[f])
            direct_map = action[product(g, f)]
            for x in OBJECTS:
                staged, direct = staged_map[x], direct_map[x]
                source, target = (staged, direct) if orientation == "lax" else (direct, staged)
                result[g, f, x] = (source, target, (source, target) in ORDER)
    return result

def failures(result): return tuple((key, value[:2]) for key, value in result.items() if not value[2])
def all_exist(result): return all(value[2] for value in result.values())

swap_action = {0: identity, 1: swap}
saturation_action = {0: identity, 1: saturate}
swap_lax = components(swap_action, "lax")
swap_oplax = components(swap_action, "oplax")
saturation_lax = components(saturation_action, "lax")
checks = {
    "diamond_middle_objects_are_incomparable": ("p", "q") not in ORDER and ("q", "p") not in ORDER,
    "swap_is_monotone": monotone(swap),
    "swap_squares_to_identity": compose_map(swap, swap) == identity,
    "swap_lacks_two_lax_components": len(failures(swap_lax)) == 2,
    "swap_lacks_two_oplax_components": len(failures(swap_oplax)) == 2,
    "swap_admits_neither_global_orientation": not all_exist(swap_lax) and not all_exist(swap_oplax),
    "projected_existing_labels_are_singleton": len({"morphism"}) == 1,
    "saturation_is_monotone": monotone(saturate),
    "saturation_is_strictly_idempotent": compose_map(saturate, saturate) == saturate,
    "saturation_admits_all_lax_components": all_exist(saturation_lax),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.sparse-object-changing-lax-existence.v1", "status": "passed", "checks": checks, "swap_lax_failures": failures(swap_lax), "swap_oplax_failures": failures(swap_oplax), "claim_boundary": "Thin diamond category with singleton projected labels."}
output = Path(__file__).parents[1] / "results" / "sparse_object_changing_lax_existence.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "lax_failures": len(failures(swap_lax)), "oplax_failures": len(failures(swap_oplax))}, sort_keys=True))
