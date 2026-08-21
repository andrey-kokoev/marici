#!/usr/bin/env python3
"""Centralizer census for equivariant K_{2,3} edge identifications."""

import itertools
import json
from pathlib import Path


states = tuple((s, k) for s in range(2) for k in range(3))
index = {state: i for i, state in enumerate(states)}


def action(state, core_swap, road_perm):
    s, k = state
    return (s ^ core_swap, road_perm[k])


road_perms = tuple(itertools.permutations(range(3)))
group_actions = []
for swap in (0, 1):
    for road_perm in road_perms:
        group_actions.append(tuple(index[action(x, swap, road_perm)] for x in states))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(states)))


centralizer = []
for candidate in itertools.permutations(range(6)):
    if all(compose(candidate, g) == compose(g, candidate) for g in group_actions):
        centralizer.append(candidate)

identity = tuple(range(6))
global_core_swap = tuple(index[(s ^ 1, k)] for s, k in states)
assert centralizer == [identity, global_core_swap]

result = {
    "status": "PASS",
    "state_count": 6,
    "tested_bijections": 720,
    "group_action_count": 12,
    "equivariant_automorphism_count": len(centralizer),
    "equivariant_automorphisms": ["identity", "global core/helicity-sector swap"],
    "conclusion": "one anchored branch-sector helicity evaluation determines all six entries up to global parity",
}

out = Path(__file__).resolve().parents[1] / "results" / "k23_helicity_bridge_uniqueness.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
