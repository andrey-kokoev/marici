"""Exact five-label census of supported clique-homology cycle ports."""

from __future__ import annotations

import collections
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/five-occurrence-clique-homology.json"
VERTICES = tuple(range(5))
EDGES = tuple(itertools.combinations(VERTICES, 2))


def support(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(edge for bit, edge in enumerate(EDGES) if mask & (1 << bit))


def h1_dimension(mask: int) -> int:
    edges = support(mask)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d1 = sp.zeros(len(VERTICES), len(edges))
    for column, (i, j) in enumerate(edges):
        d1[i, column] = -1
        d1[j, column] = 1
    triangles = tuple(
        triple
        for triple in itertools.combinations(VERTICES, 3)
        if all(edge in edge_index for edge in itertools.combinations(triple, 2))
    )
    d2 = sp.zeros(len(edges), len(triangles))
    for column, (i, j, k) in enumerate(triangles):
        d2[edge_index[(j, k)], column] = 1
        d2[edge_index[(i, k)], column] = -1
        d2[edge_index[(i, j)], column] = 1
    return len(edges) - d1.rank() - d2.rank()


dimensions = {mask: h1_dimension(mask) for mask in range(1 << len(EDGES))}
positive = {mask: dim for mask, dim in dimensions.items() if dim > 0}
minimal = {
    mask: dim
    for mask, dim in positive.items()
    if all(
        dimensions[mask & ~(1 << bit)] == 0
        for bit in range(len(EDGES))
        if mask & (1 << bit)
    )
}
distribution = collections.Counter(dimensions.values())
edge_distribution = collections.Counter(
    (len(support(mask)), dim) for mask, dim in dimensions.items()
)

# Minimal nonzero supports must be bare chordless C4 or C5 graphs.
minimal_shapes = collections.Counter(
    (len(support(mask)), tuple(sorted(sum(edge.count(v) for edge in support(mask)) for v in VERTICES)))
    for mask in minimal
)
expected_shapes = {
    (4, (0, 2, 2, 2, 2)): 15,
    (5, (2, 2, 2, 2, 2)): 12,
}

gates = {
    "all_1024_labelled_supports_audited": len(dimensions) == 1024,
    "complete_k5_clique_has_no_supported_h1": dimensions[(1 << 10) - 1] == 0,
    "supported_h1_occurs": bool(positive),
    "minimal_support_count_is_27": len(minimal) == 27,
    "minimal_supports_are_exactly_c4_or_c5": dict(minimal_shapes) == expected_shapes,
    "every_minimal_support_has_one_cycle": all(dim == 1 for dim in minimal.values()),
    "maximum_supported_dimension_is_two": max(dimensions.values()) == 2,
}
assert all(gates.values()), {"gates": gates, "minimal_shapes": minimal_shapes}

result = {
    "schema": "marici.nima.five-occurrence-clique-homology.v1",
    "support_count": len(dimensions),
    "positive_support_count": len(positive),
    "dimension_distribution": {str(k): v for k, v in sorted(distribution.items())},
    "edge_dimension_distribution": {
        f"edges_{edge_count}_h1_{dim}": count
        for (edge_count, dim), count in sorted(edge_distribution.items())
    },
    "minimal_support_count": len(minimal),
    "minimal_shapes": {
        "four_cycle_plus_isolated_vertex": minimal_shapes[(4, (0, 2, 2, 2, 2))],
        "five_cycle": minimal_shapes[(5, (2, 2, 2, 2, 2))],
    },
    "maximum_supported_dimension": max(dimensions.values()),
    "gates": gates,
    "conclusion": (
        "On five labels, the primitive Carrier supports for cyclic memory are "
        "exactly chordless C4 and C5 graphs.  More complicated supports may "
        "carry up to two H1 directions, but complete K5 support fills them all."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
