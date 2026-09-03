#!/usr/bin/env python3
"""Exact finite presentation-preserving action-groupoid rewrite witness."""

import json
from itertools import product
from pathlib import Path

G = ("e", "s")
H = ("E", "T")
M = tuple(product((0, 1), repeat=2))
N = ("A", "B", "C", "D")
PHI = {"e": "E", "s": "T"}
F = {(0, 0): "A", (0, 1): "B", (1, 0): "C", (1, 1): "D"}


def act_G(g, point):
    return point if g == "e" else (point[1], point[0])


def act_H(h, point):
    if h == "E": return point
    return {"A": "A", "B": "C", "C": "B", "D": "D"}[point]


def hom_G(source, target):
    return tuple(g for g in G if act_G(g, source) == target)


def hom_H(source, target):
    return tuple(h for h in H if act_H(h, source) == target)


def orbit(action, group, point):
    return frozenset(action(g, point) for g in group)


def reps(action, group, points):
    seen, result = set(), []
    for point in points:
        component = orbit(action, group, point)
        if component not in seen:
            seen.add(component); result.append(point)
    return tuple(result)


equivariance = all(F[act_G(g, point)] == act_H(PHI[g], F[point]) for g in G for point in M)
hom_bijections = all(
    set(PHI[g] for g in hom_G(source, target)) == set(hom_H(F[source], F[target]))
    for source in M for target in M
)
orbit_transport = all(
    {F[value] for value in orbit(act_G, G, point)} == set(orbit(act_H, H, F[point]))
    for point in M
)
stabilizer_transport = all(
    {PHI[g] for g in hom_G(point, point)} == set(hom_H(F[point], F[point]))
    for point in M
)
source_reps = reps(act_G, G, M)
target_reps = reps(act_H, H, N)
source_profile = sorted((len(hom_G(point, point)) for point in source_reps), reverse=True)
target_profile = sorted((len(hom_H(point, point)) for point in target_reps), reverse=True)

# Same orbit count, inequivalent isotropy hostile.
TRIVIAL = ("x", "y", "z")
def trivial_action(_g, point): return point
trivial_reps = reps(trivial_action, G, TRIVIAL)
trivial_profile = sorted((len(tuple(g for g in G if trivial_action(g, point) == point)) for point in trivial_reps), reverse=True)

# Bijective but non-equivariant object relabelling hostile.
F_BAD = dict(F); F_BAD[(0, 0)], F_BAD[(0, 1)] = F_BAD[(0, 1)], F_BAD[(0, 0)]
bad_equivariance = all(F_BAD[act_G(g, point)] == act_H(PHI[g], F_BAD[point]) for g in G for point in M)
checks = {
    "group_map_is_bijective": set(PHI) == set(G) and set(PHI.values()) == set(H),
    "matching_map_is_bijective": set(F) == set(M) and set(F.values()) == set(N),
    "core_equivariance_holds": equivariance,
    "all_action_groupoid_hom_sets_transport_bijectively": hom_bijections,
    "orbit_transport_is_derived": orbit_transport,
    "stabilizer_transport_is_derived": stabilizer_transport,
    "positive_stabilizer_profiles_agree": source_profile == target_profile == [2, 2, 1],
    "positive_action_groupoids_have_three_components": len(source_reps) == len(target_reps) == 3,
    "same_orbit_count_hostile_has_different_stabilizers": len(trivial_reps) == 3 and trivial_profile == [2, 2, 2] and trivial_profile != source_profile,
    "bijective_nonlinear_relabelling_hostile_breaks_equivariance": set(F_BAD.values()) == set(N) and not bad_equivariance,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.finite-action-groupoid-rewrite-equivalence.v1", "status": "passed", "checks": checks, "positive": {"source_profile": source_profile, "target_profile": target_profile, "component_count": len(source_reps)}, "hostiles": {"same_orbit_count_profile": trivial_profile, "bad_equivariance": bad_equivariance}, "claim_boundary": "Finite presentation-preserving action-groupoid isomorphism; no homotopy or physical symmetry claim."}
output = Path(__file__).parents[1] / "results" / "finite_action_groupoid_rewrite_equivalence.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "component_count": len(source_reps), "stabilizer_profile": source_profile}, sort_keys=True))
