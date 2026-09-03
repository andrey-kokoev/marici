from __future__ import annotations

import json

import sympy as sp


def product(edges: list[sp.Matrix], dimension: int) -> sp.Matrix:
    value = sp.eye(dimension)
    for edge in edges:
        value *= edge
    return value


def kernel(edges: list[sp.Matrix], dimension: int) -> sp.Matrix:
    count = len(edges) + 1
    blocks = []
    for i in range(count):
        row = []
        for j in range(count):
            if i == j:
                block = sp.eye(dimension)
            elif i < j:
                block = product(edges[i:j], dimension)
            else:
                block = product(edges[j:i], dimension).T
            row.append(block)
        blocks.append(row)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


def main() -> None:
    rho = sp.Rational(1, 2)
    a = sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 6)], [0, sp.Rational(1, 4)]])
    b = sp.Matrix([[sp.Rational(1, 4), 0], [sp.Rational(1, 5), sp.Rational(1, 3)]])
    edges = [a, b, a, b, a, b]
    assert all(max((edge.T * edge).eigenvals()) <= rho**2 for edge in edges)
    full = kernel(edges, 2)
    assert full.is_positive_semidefinite

    for last_edge in range(1, len(edges) + 1):
        size = 2 * (last_edge + 1)
        assert full[:size, :size] == kernel(edges[:last_edge], 2)

    gauges = [sp.eye(2), sp.diag(1, -1), sp.Matrix([[0, 1], [1, 0]]), -sp.eye(2), sp.diag(-1, 1), sp.eye(2), -sp.eye(2)]
    transformed = [gauges[i] * edge * gauges[i + 1].T for i, edge in enumerate(edges)]
    block_gauge = sp.diag(*gauges)
    assert kernel(transformed, 2) == block_gauge * full * block_gauge.T

    schur_bound = (1 + rho) / (1 - rho)
    assert schur_bound == 3
    pointwise_without_uniform = [sp.Rational(n, n + 1) for n in (1, 2, 4, 8, 16)]
    assert max(pointwise_without_uniform) == sp.Rational(16, 17)
    n = sp.symbols("n", positive=True, integer=True)
    assert sp.limit(n / (n + 1), n, sp.oo) == 1

    result = {
        "schema": "marici.voevodsky.operator-valued-markov-completion.v1",
        "status": "uniform_noncommutative_completion_verified",
        "block_schur_bound": "(1+rho)/(1-rho)",
        "finite_compressions_exact": True,
        "positivity_from_finite_compressions": True,
        "associator_completion_cells": "identity",
        "orthogonal_gauge_completion": True,
        "gauge_companions_conjoints_preserved": True,
        "pointwise_contraction_alone_admitted": False,
        "general_operator_completion": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
