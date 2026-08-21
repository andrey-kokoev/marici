#!/usr/bin/env python3
"""Exact second sectorwise readout composition square: five-site cosmology."""

import json
from pathlib import Path


G = range(32)  # (C2)^5 in bit coordinates


def quotient_pair(pair):
    g, h = pair
    return g ^ h


def identity_idempotent(difference):
    return int(difference == 0)


def direct_pairing(pair):
    g, h = pair
    return int(g == h)


composition_checks = 0
deck_invariance_checks = 0
orbit_fiber_checks = 0
for g in G:
    for h in G:
        pair = (g, h)
        assert identity_idempotent(quotient_pair(pair)) == direct_pairing(pair)
        composition_checks += 1
        difference = quotient_pair(pair)
        fiber = {(x, x ^ difference) for x in G}
        assert len(fiber) == 32
        assert pair in fiber
        orbit_fiber_checks += 1
        for k in G:
            transported = (g ^ k, h ^ k)
            assert quotient_pair(transported) == difference
            assert direct_pairing(transported) == direct_pairing(pair)
            deck_invariance_checks += 1

result = {
    "schema": "marici.nima.cosmology_readout_composition.v1",
    "group": "G=(C2)^5",
    "constructor_F": "diagonal-deck orbit quotient (g,h) -> g xor h",
    "constructor_E": "identity primitive idempotent delta_0 on Fun(G,Q)",
    "direct_physical_pairing": "delta_(g,h)",
    "composition_identity": "delta_0(g xor h) = delta_(g,h)",
    "composition_checks": composition_checks,
    "orbit_fiber_checks": orbit_fiber_checks,
    "deck_invariance_checks": deck_invariance_checks,
    "passed": True,
}
out = Path(__file__).with_name("results") / "cosmology-readout-composition.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

