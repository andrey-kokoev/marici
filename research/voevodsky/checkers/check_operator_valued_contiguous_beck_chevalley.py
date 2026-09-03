from __future__ import annotations

import json

import sympy as sp


def product(edges: list[sp.Matrix]) -> sp.Matrix:
    value = sp.eye(edges[0].rows) if edges else sp.eye(2)
    for edge in edges:
        value *= edge
    return value


def kernel(edges: list[sp.Matrix]) -> sp.Matrix:
    count = len(edges) + 1
    blocks = []
    for i in range(count):
        row = []
        for j in range(count):
            if i == j:
                block = sp.eye(2)
            elif i < j:
                block = product(edges[i:j])
            else:
                block = product(edges[j:i]).T
            row.append(block)
        blocks.append(row)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


def block_indices(vertices: list[int]) -> list[int]:
    return [coordinate for vertex in vertices for coordinate in (2 * vertex, 2 * vertex + 1)]


def main() -> None:
    a = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4)], [0, sp.Rational(1, 3)]])
    b = sp.Matrix([[sp.Rational(1, 3), 0], [sp.Rational(1, 5), sp.Rational(1, 2)]])
    c = sp.Matrix([[0, sp.Rational(1, 4)], [sp.Rational(1, 3), 0]])
    d = sp.Matrix([[sp.Rational(1, 5), sp.Rational(1, 6)], [0, sp.Rational(1, 4)]])
    edges = [a, b, c, d]
    full = kernel(edges)

    interval = [1, 2, 3, 4]
    assert full.extract(block_indices(interval), block_indices(interval)) == kernel(edges[1:4])
    nested = [2, 3]
    direct = full.extract(block_indices(nested), block_indices(nested))
    first = full.extract(block_indices(interval), block_indices(interval))
    pasted = first.extract(block_indices([1, 2]), block_indices([1, 2]))
    assert direct == pasted == kernel(edges[2:3])

    gauges = [sp.eye(2), sp.diag(1, -1), sp.Matrix([[0, 1], [1, 0]]), -sp.eye(2), sp.diag(-1, 1)]
    block_gauge = sp.diag(*gauges)
    gauged = block_gauge * full * block_gauge.T
    restricted_gauge = sp.diag(*gauges[1:5])
    assert gauged.extract(block_indices(interval), block_indices(interval)) == restricted_gauge * kernel(edges[1:4]) * restricted_gauge.T

    noncontiguous = [0, 2, 4]
    compressed = full.extract(block_indices(noncontiguous), block_indices(noncontiguous))
    naive_retained_edge_chain = kernel([a, c])
    assert compressed != naive_retained_edge_chain

    result = {
        "schema": "marici.voevodsky.operator-valued-contiguous-beck-chevalley.v1",
        "status": "noncommutative_contiguous_beck_chevalley_verified",
        "comparison_cell": "identity",
        "comparison_invertible": True,
        "nested_pasting_strict": True,
        "orthogonal_gauge_naturality": True,
        "noncontiguous_equal_cardinality_rejected": True,
        "general_pullback_beck_chevalley": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
