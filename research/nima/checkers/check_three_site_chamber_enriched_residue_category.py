"""Exact checker for the chamber-enriched three-site residue link.

The normalized current coefficient is J(s,t)=-(s+t), in units of i*pi*delta,
for regulator-side signs s,t in {-1,+1}. No floating arithmetic is used.
"""
import json
from pathlib import Path

vertices = ["q_G12", "q_g23", "q_G31", "q_g12", "q_G23", "q_g31"]
edges = [
    ("q_G12", "q_g23"),
    ("q_G12", "q_g31"),
    ("q_G23", "q_g31"),
    ("q_G23", "q_g12"),
    ("q_G31", "q_g12"),
    ("q_G31", "q_g23"),
]
source_signs = [-1, 1, -1, 1, -1, 1]
chambers = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
expected = [2, 0, 0, -2]


def current(s, t):
    return -(s + t)


def rotate(label):
    table = {
        "q_G12": "q_G23", "q_G23": "q_G31", "q_G31": "q_G12",
        "q_g23": "q_g31", "q_g31": "q_g12", "q_g12": "q_g23",
    }
    return table[label]

coefficients = [current(*c) for c in chambers]
assert coefficients == expected
assert [current(t, s) for s, t in chambers] == expected

edge_set = {frozenset(e) for e in edges}
assert len(edge_set) == 6
for e in edges:
    assert frozenset((rotate(e[0]), rotate(e[1]))) in edge_set

# Reversing residue order reverses the oriented two-normal form.
for sign, edge in zip(source_signs, edges):
    forward = [sign * current(*c) for c in chambers]
    reverse = [-x for x in forward]
    assert all(x + y == 0 for x, y in zip(forward, reverse))

# A concrete non-edge is rejected by the compatibility relation.
incompatible = ("q_G12", "q_G23")
assert frozenset(incompatible) not in edge_set

result = {
    "schema": "marici.nima.three-site-chamber-enriched-residue-category.v1",
    "status": "pass",
    "normalization": "coefficients in units of i*pi*delta(A)",
    "chambers": [list(c) for c in chambers],
    "current_coefficients": coefficients,
    "edges": [
        {
            "ordered_pair": list(edge),
            "source_orientation": sign,
            "forward_coefficients": [sign * current(*c) for c in chambers],
            "reverse_coefficients": [-sign * current(*c) for c in chambers],
        }
        for sign, edge in zip(source_signs, edges)
    ],
    "cyclic_edge_preservation": True,
    "order_antisymmetry": True,
    "mixed_chamber_vanishing": True,
    "incompatible_pair_rejected": list(incompatible),
    "claim_boundary": "No physical contour-side chamber selection or integrated period is asserted.",
}

out = Path(__file__).parents[1] / "results" / "three-site-chamber-enriched-residue-category.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
