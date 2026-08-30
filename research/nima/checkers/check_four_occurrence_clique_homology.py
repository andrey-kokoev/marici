"""Exact census of triangle reconstruction defects on four labelled supports."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/four-occurrence-clique-homology.json"
VERTICES = tuple(range(4))
EDGES = tuple(itertools.combinations(VERTICES, 2))


def boundary_one(edges: tuple[tuple[int, int], ...]) -> sp.Matrix:
    matrix = sp.zeros(len(VERTICES), len(edges))
    for column, (i, j) in enumerate(edges):
        matrix[i, column] = -1
        matrix[j, column] = 1
    return matrix


def triangle_boundary(
    edges: tuple[tuple[int, int], ...],
) -> tuple[sp.Matrix, tuple[tuple[int, int, int], ...]]:
    edge_index = {edge: index for index, edge in enumerate(edges)}
    triangles = tuple(
        triple
        for triple in itertools.combinations(VERTICES, 3)
        if all(edge in edge_index for edge in itertools.combinations(triple, 2))
    )
    matrix = sp.zeros(len(edges), len(triangles))
    for column, (i, j, k) in enumerate(triangles):
        # Boundary [j,k] - [i,k] + [i,j].
        matrix[edge_index[(j, k)], column] = 1
        matrix[edge_index[(i, k)], column] = -1
        matrix[edge_index[(i, j)], column] = 1
    return matrix, triangles


def census_row(mask: int) -> dict[str, object]:
    edges = tuple(edge for bit, edge in enumerate(EDGES) if mask & (1 << bit))
    d1 = boundary_one(edges)
    d2, triangles = triangle_boundary(edges)
    cycle_dim = len(edges) - d1.rank()
    triangle_rank = d2.rank()
    h1 = cycle_dim - triangle_rank
    return {
        "mask": mask,
        "edges": [list(edge) for edge in edges],
        "edge_count": len(edges),
        "triangle_count": len(triangles),
        "cycle_dimension": cycle_dim,
        "triangle_boundary_rank": triangle_rank,
        "supported_cycle_dimension": h1,
    }


rows = [census_row(mask) for mask in range(1 << len(EDGES))]
survivors = [row for row in rows if row["supported_cycle_dimension"]]
survivor_edge_sets = {
    tuple(tuple(edge) for edge in row["edges"]) for row in survivors
}
expected_cycles = {
    tuple(sorted(cycle))
    for cycle in (
        ((0, 1), (1, 2), (2, 3), (0, 3)),
        ((0, 1), (1, 3), (2, 3), (0, 2)),
        ((0, 2), (1, 2), (1, 3), (0, 3)),
    )
}
complete = rows[-1]

gates = {
    "all_64_labelled_support_graphs_audited": len(rows) == 64,
    "complete_support_has_cycle_rank_three": complete["cycle_dimension"] == 3,
    "complete_support_triangles_fill_all_cycles": (
        complete["triangle_boundary_rank"] == 3
        and complete["supported_cycle_dimension"] == 0
    ),
    "exactly_three_supports_retain_unfilled_cycles": len(survivors) == 3,
    "survivors_are_exactly_the_three_chordless_four_cycles": (
        survivor_edge_sets == expected_cycles
    ),
    "each_survivor_has_one_supported_cycle": all(
        row["supported_cycle_dimension"] == 1 for row in survivors
    ),
    "no_graph_with_a_triangle_has_supported_cycle": all(
        row["triangle_count"] == 0 for row in survivors
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.four-occurrence-clique-homology.v1",
    "graph_count": len(rows),
    "survivor_count": len(survivors),
    "complete_support": complete,
    "survivors": survivors,
    "gates": gates,
    "conclusion": (
        "The information not reconstructible from triangle Bargmann ports is "
        "H_1 of the support graph's clique complex.  On four labels it "
        "vanishes for every support except the three chordless Hamiltonian "
        "cycles, where it is one-dimensional."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
