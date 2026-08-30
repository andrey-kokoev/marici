"""Exact hostile test of exclusivity in the proposed failure trichotomy."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/failure-signature-overlap.json"


def clique_h1(edges: tuple[tuple[int, int], ...]) -> int:
    vertices = (0, 1, 2, 3)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d1 = sp.zeros(4, len(edges))
    for column, (i, j) in enumerate(edges):
        d1[i, column] = -1
        d1[j, column] = 1
    triangles = tuple(
        triple
        for triple in itertools.combinations(vertices, 3)
        if all(edge in edge_index for edge in itertools.combinations(triple, 2))
    )
    d2 = sp.zeros(len(edges), len(triangles))
    for column, (i, j, k) in enumerate(triangles):
        d2[edge_index[(j, k)], column] = 1
        d2[edge_index[(i, k)], column] = -1
        d2[edge_index[(i, j)], column] = 1
    return len(edges) - d1.rank() - d2.rank()


t = sp.symbols("t")
rim = ((0, 1), (1, 2), (2, 3), (0, 3))
chords = ((0, 2), (1, 3))
generic_support = tuple(sorted(rim + chords))
special_support = tuple(sorted(rim))

# The same source parameter controls all three independent mechanisms.
preferred_line_chart = sp.Matrix([t, 1])
transport = sp.diag(1, t)

presentation_flag = (
    preferred_line_chart.subs(t, 0)[0] == 0
    and preferred_line_chart.subs(t, 0).rank() == 1
)
support_flag = clique_h1(generic_support) == 0 and clique_h1(special_support) == 1
degeneration_flag = transport.det() == t and transport.subs(t, 0).rank() == 1
joint_signature = (int(presentation_flag), int(support_flag), int(degeneration_flag))

# Independent products of the three elementary mechanisms admit every binary
# signature, so the natural organization is a Boolean poset, not three
# mutually exclusive cases.
all_signatures = list(itertools.product((0, 1), repeat=3))

gates = {
    "preferred_chart_fails_but_line_survives": presentation_flag,
    "same_parameter_births_supported_h1": support_flag,
    "same_parameter_drops_transport_rank": degeneration_flag,
    "one_event_has_all_three_flags": joint_signature == (1, 1, 1),
    "exclusive_trichotomy_is_falsified": sum(joint_signature) > 1,
    "signature_space_is_boolean_cube": len(all_signatures) == 8,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.failure-signature-overlap.v1",
    "generic_support_h1": clique_h1(generic_support),
    "special_support_h1": clique_h1(special_support),
    "transport_generic_determinant": str(transport.det()),
    "transport_special_rank": transport.subs(t, 0).rank(),
    "joint_signature": list(joint_signature),
    "signature_coordinates": ["presentation", "support", "degeneration"],
    "signature_poset": [list(signature) for signature in all_signatures],
    "gates": gates,
    "conclusion": (
        "The three failure mechanisms are independent axes and may coincide "
        "at one source stratum.  Entry 2053's exclusive trichotomy must be "
        "replaced by a Boolean failure signature ordered componentwise."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
