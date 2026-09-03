from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    r0 = sp.Matrix([[1, 1], [0, 1]])
    r1 = sp.diag(2, 1)
    r2 = sp.Matrix([[1, 0], [1, 1]])
    a0 = sp.diag(sp.Rational(1, 3), sp.Rational(1, 4))
    a1 = sp.Matrix([[sp.Rational(1, 4), 0], [sp.Rational(1, 6), sp.Rational(1, 3)]])
    frames = [r0, r1, r2]
    transfers = [a0, a1]
    metrics = [r * r.T for r in frames]
    covariances = [frames[i] * transfers[i] * frames[i + 1].T for i in range(2)]

    rotations = [sp.Matrix([[0, -1], [1, 0]]), sp.diag(1, -1), -sp.eye(2)]
    changed_frames = [r * o for r, o in zip(frames, rotations)]
    changed_transfers = [rotations[i].T * transfers[i] * rotations[i + 1] for i in range(2)]
    assert [r * r.T for r in changed_frames] == metrics
    assert [changed_frames[i] * changed_transfers[i] * changed_frames[i + 1].T for i in range(2)] == covariances

    reconstructed = [frames[i].inv() * covariances[i] * frames[i + 1].inv().T for i in range(2)]
    assert reconstructed == transfers
    reconstructed_changed = [changed_frames[i].inv() * covariances[i] * changed_frames[i + 1].inv().T for i in range(2)]
    assert reconstructed_changed == changed_transfers

    residuals = [metrics[i + 1] - covariances[i].T * metrics[i].inv() * covariances[i] for i in range(2)]
    assert all(residual.is_positive_semidefinite for residual in residuals)

    long_from_quotient = covariances[0] * metrics[1].inv() * covariances[1]
    long_from_frames = frames[0] * transfers[0] * transfers[1] * frames[2].T
    assert long_from_quotient == long_from_frames

    hostile_covariance = changed_frames[0] * transfers[0] * changed_frames[1].T
    assert hostile_covariance != covariances[0]

    result = {
        "schema": "marici.voevodsky.framed-to-metric-markov-descent.v1",
        "status": "finite_metric_transition_quotient_verified",
        "metric_and_edge_covariance_invariant": True,
        "quotient_coordinate_faithful": True,
        "reconstruction_choice_independent_modulo_orthogonal_action": True,
        "contraction_condition_descends": True,
        "long_block_reconstruction": True,
        "uncoupled_frame_change_rejected": True,
        "infinite_completion_descent": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
