from __future__ import annotations

import json

import sympy as sp


def product(edges: list[sp.Matrix], identity_size: int) -> sp.Matrix:
    value = sp.eye(identity_size)
    for edge in edges:
        value *= edge
    return value


def kernel(edges: list[sp.Matrix], dimensions: list[int]) -> sp.Matrix:
    blocks: list[list[sp.Matrix]] = []
    for i, di in enumerate(dimensions):
        row = []
        for j, dj in enumerate(dimensions):
            if i == j:
                block = sp.eye(di)
            elif i < j:
                block = product(edges[i:j], di)
            else:
                block = product(edges[j:i], dj).T
            assert block.shape == (di, dj)
            row.append(block)
        blocks.append(row)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


def coordinates(dimensions: list[int], vertices: list[int]) -> list[int]:
    offsets = [0]
    for dimension in dimensions:
        offsets.append(offsets[-1] + dimension)
    return [coordinate for vertex in vertices for coordinate in range(offsets[vertex], offsets[vertex + 1])]


def main() -> None:
    dimensions = [2, 3, 2, 1]
    a = sp.Matrix([[sp.Rational(1, 3), 0, sp.Rational(1, 4)], [0, sp.Rational(1, 5), 0]])
    b = sp.Matrix([[sp.Rational(1, 4), 0], [0, sp.Rational(1, 3)], [sp.Rational(1, 6), 0]])
    c = sp.Matrix([[sp.Rational(1, 3)], [sp.Rational(1, 4)]])
    edges = [a, b, c]
    assert [edge.shape for edge in edges] == [(2, 3), (3, 2), (2, 1)]
    assert all((sp.eye(edge.cols) - edge.T * edge).is_positive_semidefinite for edge in edges)

    full = kernel(edges, dimensions)
    assert full.is_positive_semidefinite
    assert (a * b) * c == a * (b * c)

    gauges = [sp.diag(1, -1), sp.diag(-1, 1, 1), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[-1]])]
    transformed = [gauges[i] * edge * gauges[i + 1].T for i, edge in enumerate(edges)]
    block_gauge = sp.diag(*gauges)
    assert kernel(transformed, dimensions) == block_gauge * full * block_gauge.T

    interval = [1, 2, 3]
    selected = coordinates(dimensions, interval)
    assert full.extract(selected, selected) == kernel(edges[1:3], dimensions[1:4])

    mismatch_rejected = False
    try:
        _ = a * c
    except sp.ShapeError:
        mismatch_rejected = True
    assert mismatch_rejected

    result = {
        "schema": "marici.voevodsky.varying-fiber-markov-green.v1",
        "status": "finite_varying_fiber_coherence_verified",
        "fiber_dimensions": dimensions,
        "rectangular_contractions": True,
        "typed_block_kernel_positive": True,
        "strict_associator_pentagon": True,
        "orthogonal_gauge_interchange": True,
        "contiguous_beck_chevalley": True,
        "dimension_mismatched_seam_rejected": True,
        "infinite_completion": False,
        "arbitrary_fiber_changing_vertical_arrows": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
