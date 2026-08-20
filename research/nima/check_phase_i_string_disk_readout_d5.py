#!/usr/bin/env python3
"""Exact D5 character audit for the source-normalized five-point disk readout."""

import json
from pathlib import Path


N = 5


def compose(g, h):
    """Permutation g after h."""
    return tuple(g[h[i]] for i in range(N))


identity = tuple(range(N))
rotation = tuple((i + 1) % N for i in range(N))
reflection = tuple((-i) % N for i in range(N))


def power(g, exponent):
    out = identity
    for _ in range(exponent):
        out = compose(g, out)
    return out


elements = []
normal_forms = {}
for parity in (0, 1):
    for exponent in range(N):
        g = power(rotation, exponent)
        if parity:
            g = compose(reflection, g)
        elements.append(g)
        normal_forms[g] = (exponent, parity)

assert len(set(elements)) == 2 * N


def character(g):
    """Open-string color-order reversal character: rotations +1, reflections (-1)^N."""
    _, parity = normal_forms[g]
    return (-1) ** (N * parity)


homomorphism_checks = 0
for g in elements:
    for h in elements:
        assert character(compose(g, h)) == character(g) * character(h)
        homomorphism_checks += 1

commutators = set()
for g in elements:
    for h in elements:
        gi = power(g, next(k for k in range(1, 2 * N + 1) if power(g, k) == identity) - 1)
        hi = power(h, next(k for k in range(1, 2 * N + 1) if power(h, k) == identity) - 1)
        commutators.add(compose(compose(compose(g, h), gi), hi))

rotation_subgroup = {power(rotation, k) for k in range(N)}
assert commutators == rotation_subgroup
assert all(character(g) == 1 for g in commutators)

result = {
    "schema": "marici.nima.phase_i_string_disk_readout_d5.v1",
    "arity": N,
    "group_order": len(elements),
    "commutator_subgroup_order": len(commutators),
    "commutator_subgroup": "C5 rotations",
    "rotation_character": character(rotation),
    "reflection_character": character(reflection),
    "homomorphism_checks": homomorphism_checks,
    "all_commutators_killed": True,
    "factors_through_abelianization": "D5_ab = C2",
    "scope": "simultaneous source-label transport of chamber, Parke-Taylor cocycle, and Koba-Nielsen loading",
    "passed": True,
}

out = Path(__file__).with_name("results") / "phase-i-string-disk-readout-d5.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

