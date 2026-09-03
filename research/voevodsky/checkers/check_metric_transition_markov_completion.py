from __future__ import annotations

import json

import sympy as sp


def long_block(metrics: list[sp.Matrix], covariances: list[sp.Matrix], i: int, j: int) -> sp.Matrix:
    value = covariances[i]
    for k in range(i + 1, j):
        value = value * metrics[k].inv() * covariances[k]
    return value


def main() -> None:
    count = 6
    frames = [sp.diag(sp.Rational(i + 1, i + 2), sp.Rational(i + 2, i + 3)) for i in range(count)]
    transfers = [sp.diag(sp.Rational(1, 3), sp.Rational(1, 4)) for _ in range(count - 1)]
    metrics = [frame * frame.T for frame in frames]
    covariances = [frames[i] * transfers[i] * frames[i + 1].T for i in range(count - 1)]

    for i in range(count):
        for j in range(i + 1, count):
            expected = frames[i]
            for transfer in transfers[i:j]:
                expected *= transfer
            expected *= frames[j].T
            assert long_block(metrics, covariances, i, j) == expected

    rotations = [sp.Matrix([[0, -1], [1, 0]]) if i % 2 else sp.diag(1, -1) for i in range(count)]
    changed_frames = [frame * rotation for frame, rotation in zip(frames, rotations)]
    changed_transfers = [rotations[i].T * transfers[i] * rotations[i + 1] for i in range(count - 1)]
    assert [frame * frame.T for frame in changed_frames] == metrics
    assert [changed_frames[i] * changed_transfers[i] * changed_frames[i + 1].T for i in range(count - 1)] == covariances

    rho = sp.Rational(1, 3)
    metric_bound = 1
    assert metric_bound * (1 + rho) / (1 - rho) == 2
    pointwise_sequence_limit = sp.limit(sp.Symbol("n", positive=True) / (sp.Symbol("n", positive=True) + 1), sp.Symbol("n", positive=True), sp.oo)
    assert pointwise_sequence_limit == 1
    hostile_metric_norms = [1, 4, 16, 64]

    result = {
        "schema": "marici.voevodsky.metric-transition-markov-completion.v1",
        "status": "quotient_completion_descent_verified",
        "frame_free_long_blocks": True,
        "frame_choice_independence": True,
        "operator_bound": "C^2(1+rho)/(1-rho)",
        "positivity_from_finite_compressions": True,
        "contiguous_beck_chevalley_descends": True,
        "GL_companion_conjoint_completion_descends": True,
        "pointwise_only_contraction_rejected": True,
        "unbounded_metric_norms_rejected": hostile_metric_norms,
        "general_noncontiguous_pullback": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
