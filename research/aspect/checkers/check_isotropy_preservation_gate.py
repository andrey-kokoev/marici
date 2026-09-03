#!/usr/bin/env python3
"""Finite isotropy audit for action groupoids versus coarse orbit sets."""

import json
from itertools import product
from pathlib import Path

GROUP = ("id", "swap")
M = tuple(product((0, 1), repeat=2))
N = ("a", "b", "c")


def swap_action(element, point):
    return point if element == "id" else (point[1], point[0])


def trivial_action(_element, point):
    return point


def orbit(action, point):
    return frozenset(action(element, point) for element in GROUP)


def stabilizer(action, point):
    return tuple(element for element in GROUP if action(element, point) == point)


def representatives(action, points):
    seen = set()
    result = []
    for point in points:
        component = orbit(action, point)
        if component in seen:
            continue
        seen.add(component)
        result.append(point)
    return tuple(result)


swap_reps = representatives(swap_action, M)
trivial_reps = representatives(trivial_action, N)
swap_profile = sorted((len(stabilizer(swap_action, point)) for point in swap_reps), reverse=True)
trivial_profile = sorted((len(stabilizer(trivial_action, point)) for point in trivial_reps), reverse=True)
fixed_M = tuple(point for point in M if all(swap_action(element, point) == point for element in GROUP))
checks = {
    "swap_action_has_three_coarse_orbits": len(swap_reps) == 3,
    "trivial_three_point_action_has_three_coarse_orbits": len(trivial_reps) == 3,
    "coarse_orbit_cardinalities_agree": len(swap_reps) == len(trivial_reps),
    "swap_action_stabilizer_profile_is_221": swap_profile == [2, 2, 1],
    "trivial_action_stabilizer_profile_is_222": trivial_profile == [2, 2, 2],
    "equal_orbit_counts_do_not_preserve_isotropy": swap_profile != trivial_profile,
    "swap_fixed_point_set_has_two_points": set(fixed_M) == {(0, 0), (1, 1)},
    "fixed_points_omit_nonfixed_mixed_orbit": all(point not in fixed_M for point in ((0, 1), (1, 0))),
    "action_groupoid_retains_four_source_objects": len(M) == 4,
    "coarse_orbit_projection_forgets_stabilizer_profile": len(swap_reps) < len(M) and swap_profile != trivial_profile,
}
assert all(checks.values()), checks
result = {
    "schema": "marici.aspect.isotropy-preservation-gate.v1",
    "status": "passed",
    "checks": checks,
    "swap_action": {"object_count": len(M), "component_count": len(swap_reps), "stabilizer_profile": swap_profile, "fixed_points": fixed_M},
    "trivial_action": {"object_count": len(N), "component_count": len(trivial_reps), "stabilizer_profile": trivial_profile},
    "gate": "retain action-groupoid or stabilizer evidence only for isotropy-sensitive claims",
    "claim_boundary": "Finite action-groupoid audit; no groupoid-valued matching or homotopy-limit construction."
}
output = Path(__file__).parents[1] / "results" / "isotropy_preservation_gate.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "swap_profile": swap_profile, "trivial_profile": trivial_profile}, sort_keys=True))
