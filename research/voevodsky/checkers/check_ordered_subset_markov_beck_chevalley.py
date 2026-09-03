from __future__ import annotations

import json

import sympy as sp


def long_block(metrics: list[sp.Matrix], edges: list[sp.Matrix], i: int, j: int) -> sp.Matrix:
    value = edges[i]
    for k in range(i + 1, j):
        value = value * metrics[k].inv() * edges[k]
    return value


def kernel(metrics: list[sp.Matrix], edges: list[sp.Matrix]) -> sp.Matrix:
    count = len(metrics)
    rows = []
    for i in range(count):
        blocks = []
        for j in range(count):
            block = metrics[i] if i == j else long_block(metrics, edges, i, j) if i < j else long_block(metrics, edges, j, i).T
            blocks.append(block)
        rows.append(blocks)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in rows))


def restrict(metrics: list[sp.Matrix], edges: list[sp.Matrix], vertices: list[int]) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    assert all(left < right for left, right in zip(vertices, vertices[1:]))
    return [metrics[i] for i in vertices], [long_block(metrics, edges, i, j) for i, j in zip(vertices, vertices[1:])]


def block_indices(vertices: list[int]) -> list[int]:
    return [coordinate for vertex in vertices for coordinate in (2 * vertex, 2 * vertex + 1)]


def main() -> None:
    frames = [sp.diag(i + 1, sp.Rational(1, i + 1)) for i in range(6)]
    transfers = [sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 8)], [0, sp.Rational(1, 4)]]) for _ in range(5)]
    metrics = [frame * frame.T for frame in frames]
    edges = [frames[i] * transfers[i] * frames[i + 1].T for i in range(5)]
    full = kernel(metrics, edges)

    vertices = [0, 2, 5]
    restricted_metrics, effective_edges = restrict(metrics, edges, vertices)
    restricted_kernel = kernel(restricted_metrics, effective_edges)
    assert restricted_kernel == full.extract(block_indices(vertices), block_indices(vertices))

    second_vertices_local = [0, 2]
    twice_metrics, twice_edges = restrict(restricted_metrics, effective_edges, second_vertices_local)
    direct_metrics, direct_edges = restrict(metrics, edges, [0, 5])
    assert twice_metrics == direct_metrics
    assert twice_edges == direct_edges
    assert kernel(twice_metrics, twice_edges) == kernel(direct_metrics, direct_edges)

    duplicate_rejected = reversed_rejected = False
    try:
        restrict(metrics, edges, [0, 2, 2])
    except AssertionError:
        duplicate_rejected = True
    try:
        restrict(metrics, edges, [0, 3, 1])
    except AssertionError:
        reversed_rejected = True
    assert duplicate_rejected and reversed_rejected

    naive_edges = [edges[0], edges[2]]
    assert kernel([metrics[i] for i in vertices], naive_edges) != restricted_kernel

    result = {
        "schema": "marici.voevodsky.ordered-subset-markov-beck-chevalley.v1",
        "status": "ordered_subset_beck_chevalley_verified",
        "effective_covariances_source_derived": True,
        "comparison_identity_invertible": True,
        "noncontiguous_compression_exact": True,
        "nested_subset_pasting_strict": True,
        "naive_retained_edge_list_rejected": True,
        "duplicate_vertex_map_rejected": True,
        "reversed_vertex_map_rejected": True,
        "branching_nonmonic_pullbacks": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
