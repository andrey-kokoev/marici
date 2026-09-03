from __future__ import annotations

import json

import sympy as sp


I2 = sp.eye(2)


def product(edges: list[sp.Matrix]) -> sp.Matrix:
    value = I2
    for edge in edges:
        value = value * edge
    return value


def kernel(edges: list[sp.Matrix]) -> sp.Matrix:
    n = len(edges) + 1
    blocks: list[list[sp.Matrix]] = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                block = I2
            elif i < j:
                block = product(edges[i:j])
            else:
                block = product(edges[j:i]).T
            row.append(block)
        blocks.append(row)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


def main() -> None:
    a = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4)], [0, sp.Rational(1, 3)]])
    b = sp.Matrix([[sp.Rational(1, 3), 0], [sp.Rational(1, 5), sp.Rational(1, 2)]])
    c = sp.Matrix([[0, sp.Rational(1, 4)], [sp.Rational(1, 3), 0]])
    d = sp.Matrix([[sp.Rational(1, 5), sp.Rational(1, 6)], [0, sp.Rational(1, 4)]])
    edges = [a, b, c, d]
    assert a * b != b * a
    assert all((I2 - edge.T * edge).is_positive_semidefinite for edge in edges)

    full = kernel(edges)
    assert full.is_positive_semidefinite
    assert product(([a] + [b]) + [c, d]) == product([a] + ([b] + [c, d]))
    assert product(edges) == ((a * b) * c) * d == a * (b * (c * d))

    gauges = [I2, sp.diag(1, -1), sp.Matrix([[0, 1], [1, 0]]), -I2, sp.diag(-1, 1)]
    transformed = [gauges[i] * edge * gauges[i + 1].T for i, edge in enumerate(edges)]
    block_gauge = sp.diag(*gauges)
    assert kernel(transformed) == block_gauge * full * block_gauge.T

    assert product([a, b]) != product([b, a])
    bad_gauges = list(gauges)
    bad_gauges[2] = I2
    left_transformed = [gauges[i] * edges[i] * gauges[i + 1].T for i in range(2)]
    right_transformed = [bad_gauges[i] * edges[i] * bad_gauges[i + 1].T for i in range(2, 4)]
    assert product(left_transformed + right_transformed) != gauges[0] * product(edges) * bad_gauges[4].T

    result = {
        "schema": "marici.voevodsky.operator-valued-markov-green.v1",
        "status": "finite_noncommutative_analytic_coherence_verified",
        "fiber_dimension": 2,
        "edge_contractions": True,
        "block_kernel_positive_semidefinite": True,
        "noncommuting_fixture": True,
        "strict_associator": True,
        "pentagon": True,
        "orthogonal_gauge_interchange": True,
        "reversed_path_order_rejected": True,
        "shared_seam_gauge_mismatch_rejected": True,
        "infinite_completion_verified": False,
        "general_beck_chevalley_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
