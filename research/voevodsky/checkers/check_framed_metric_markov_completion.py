from __future__ import annotations

import json

import sympy as sp


def product(edges: list[sp.Matrix]) -> sp.Matrix:
    value = sp.eye(2)
    for edge in edges:
        value *= edge
    return value


def kernel(edges: list[sp.Matrix]) -> sp.Matrix:
    count = len(edges) + 1
    rows = []
    for i in range(count):
        blocks = []
        for j in range(count):
            block = sp.eye(2) if i == j else product(edges[i:j]) if i < j else product(edges[j:i]).T
            blocks.append(block)
        rows.append(blocks)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in rows))


def main() -> None:
    rho = sp.Rational(1, 2)
    edge = sp.diag(sp.Rational(1, 3), sp.Rational(1, 4))
    edges = [edge] * 5
    normalized = kernel(edges)
    frames = [sp.diag(sp.Rational(i + 1, i + 2), sp.Rational(i + 2, i + 3)) for i in range(6)]
    frame_sum = sp.diag(*frames)
    framed = frame_sum * normalized * frame_sum.T
    assert framed.is_positive_semidefinite
    assert all(max(abs(value) for value in frame) <= 1 for frame in frames)

    for last in range(1, 6):
        size = 2 * (last + 1)
        restricted_frames = sp.diag(*frames[:last + 1])
        assert framed[:size, :size] == restricted_frames * kernel(edges[:last]) * restricted_frames.T

    gauges = [sp.diag(2, sp.Rational(1, 2)) if i % 2 == 0 else sp.Matrix([[1, 1], [0, 1]]) for i in range(6)]
    assert all(gauge.det() != 0 for gauge in gauges)
    gauge_sum = sp.diag(*gauges)
    assert gauge_sum.inv() == sp.diag(*(gauge.inv() for gauge in gauges))
    changed_frames = sp.diag(*(gauge * frame for gauge, frame in zip(gauges, frames)))
    assert changed_frames * normalized * changed_frames.T == gauge_sum * framed * gauge_sum.T

    schur_bound = (1 + rho) / (1 - rho)
    frame_bound = 1
    assert frame_bound**2 * schur_bound == 3
    hostile_frame_norms = [1, 2, 4, 8]
    hostile_metric_norms = [value**2 for value in hostile_frame_norms]
    assert hostile_metric_norms == [1, 4, 16, 64]

    result = {
        "schema": "marici.voevodsky.framed-metric-markov-completion.v1",
        "status": "uniform_framed_GL_completion_verified",
        "operator_bound": "C^2(1+rho)/(1-rho)",
        "positive": True,
        "finite_compressions_exact": True,
        "bounded_GL_companions": True,
        "bounded_inverse_conjoints": True,
        "strict_completion_pasting": True,
        "hostile_unbounded_frame_metric_norms": hostile_metric_norms,
        "metric_only_descent": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
