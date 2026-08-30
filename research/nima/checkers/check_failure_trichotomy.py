"""Exact invariant audit for chart, support, and transport failures."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/failure-trichotomy.json"


def clique_h1(vertices: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> int:
    edges = tuple(tuple(sorted(edge)) for edge in edges)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d1 = sp.zeros(len(vertices), len(edges))
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
    for column, (i, j) in enumerate(edges):
        d1[vertex_index[i], column] = -1
        d1[vertex_index[j], column] = 1
    triangles = tuple(
        triple
        for triple in itertools.combinations(vertices, 3)
        if all(tuple(sorted(edge)) in edge_index for edge in itertools.combinations(triple, 2))
    )
    d2 = sp.zeros(len(edges), len(triangles))
    for column, (i, j, k) in enumerate(triangles):
        d2[edge_index[tuple(sorted((j, k)))], column] = 1
        d2[edge_index[tuple(sorted((i, k)))], column] = -1
        d2[edge_index[tuple(sorted((i, j)))], column] = 1
    return len(edges) - d1.rank() - d2.rank()


t = sp.symbols("t")

# Type I: one projective coordinate dies, but the represented line survives.
line = sp.Matrix([t, 1])
line_at_boundary = line.subs(t, 0)
line_rechart = sp.Matrix([[1, 1], [1, 2]]) * line_at_boundary

# Type II: removal of coherence fillers changes supported homology.
vertices = (0, 1, 2, 3)
k4_edges = tuple(itertools.combinations(vertices, 2))
c4_edges = ((0, 1), (1, 2), (2, 3), (0, 3))
k4_h1 = clique_h1(vertices, k4_edges)
c4_h1 = clique_h1(vertices, c4_edges)
permuted_c4_h1 = []
for permutation in itertools.permutations(vertices):
    relabel = {old: new for old, new in zip(vertices, permutation)}
    edges = tuple(tuple(sorted((relabel[i], relabel[j]))) for i, j in c4_edges)
    permuted_c4_h1.append(clique_h1(vertices, edges))

# Type III: the full exterior section dies and a kernel is born.
transport = sp.diag(1, t)
transport_boundary = transport.subs(t, 0)
left = sp.Matrix([[1, 1], [0, 1]])
right = sp.Matrix([[2, 0], [1, 1]])
transformed_transport = left * transport * right

gates = {
    "chart_coordinate_can_vanish_while_object_survives": (
        line_at_boundary[0] == 0 and line_at_boundary.rank() == 1
    ),
    "invertible_rechart_preserves_chart_case_rank": line_rechart.rank() == 1,
    "complete_support_cycles_are_filled": k4_h1 == 0,
    "chordless_support_births_one_cycle": c4_h1 == 1,
    "supported_birth_is_label_invariant": all(value == 1 for value in permuted_c4_h1),
    "transport_exterior_section_vanishes_at_true_birth": (
        sp.det(transport) == t and sp.det(transport_boundary) == 0
    ),
    "true_birth_has_kernel": len(transport_boundary.nullspace()) == 1,
    "invertible_presentation_changes_preserve_degeneracy_locus": (
        sp.factor(transformed_transport.det()) == sp.factor(left.det() * right.det() * t)
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.failure-trichotomy.v1",
    "chart_boundary": {
        "preferred_coordinate": "t",
        "boundary_vector": [str(value) for value in line_at_boundary],
        "invariant_rank": line_at_boundary.rank(),
    },
    "supported_birth": {
        "complete_support_h1": k4_h1,
        "chordless_support_h1": c4_h1,
        "relabelled_h1_values": sorted(set(permuted_c4_h1)),
    },
    "transport_birth": {
        "exterior_section": str(transport.det()),
        "boundary_rank": transport_boundary.rank(),
        "boundary_kernel_dimension": len(transport_boundary.nullspace()),
    },
    "gates": gates,
    "falsifier": (
        "Find one source-admissible presentation change that alters whether "
        "a failure is rank-preserving recharting, support-homology birth, or "
        "full exterior-section degeneration."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
