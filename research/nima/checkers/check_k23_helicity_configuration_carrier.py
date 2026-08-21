#!/usr/bin/env python3
"""Equivariant identification of K_{2,3} edges with 3-point helicity states."""

import itertools
import json
from pathlib import Path


cores = ("MHV", "anti-MHV")
legs = (0, 1, 2)
edges = tuple(itertools.product(cores, legs))


def helicities(edge):
    sector, exceptional = edge
    ordinary, special = ((-1, +1) if sector == "MHV" else (+1, -1))
    return tuple(special if i == exceptional else ordinary for i in legs)


def parity(edge):
    sector, exceptional = edge
    return ("anti-MHV" if sector == "MHV" else "MHV", exceptional)


def permute(edge, permutation):
    sector, exceptional = edge
    return sector, permutation[exceptional]


states = {edge: helicities(edge) for edge in edges}
assert len(set(states.values())) == 6
assert all(sorted((hs.count(-1), hs.count(+1))) == [1, 2] for hs in states.values())
assert all(tuple(-h for h in states[e]) == states[parity(e)] for e in edges)

permutations = tuple(itertools.permutations(legs))
for edge in edges:
    for p in permutations:
        transformed = tuple(states[edge][p.index(i)] for i in legs)
        assert transformed == states[permute(edge, p)]

result = {
    "status": "PASS",
    "carrier_edges": [list(edge) for edge in edges],
    "helicity_states": {f"{s}:{k}": list(h) for (s, k), h in states.items()},
    "cardinality": 6,
    "symmetry": "S2(parity/core) x S3(label/road)",
    "equivariant_bijection": True,
    "interpretation": "the full labelled three-point helicity packet has the K_{2,3} polarity-road incidence shape",
    "caveat": "the physical identification of Carrier cores with MHV/anti-MHV still requires a source map",
}

out = Path(__file__).resolve().parents[1] / "results" / "k23_helicity_configuration_carrier.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
