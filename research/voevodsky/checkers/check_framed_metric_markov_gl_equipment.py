from __future__ import annotations

import json

import sympy as sp


def product(edges: list[sp.Matrix]) -> sp.Matrix:
    value = sp.eye(2)
    for edge in edges:
        value *= edge
    return value


def normalized_kernel(edges: list[sp.Matrix]) -> sp.Matrix:
    count = len(edges) + 1
    blocks = []
    for i in range(count):
        row = []
        for j in range(count):
            block = sp.eye(2) if i == j else product(edges[i:j]) if i < j else product(edges[j:i]).T
            row.append(block)
        blocks.append(row)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in blocks))


def main() -> None:
    a = sp.diag(sp.Rational(1, 3), sp.Rational(1, 4))
    b = sp.Matrix([[sp.Rational(1, 4), 0], [sp.Rational(1, 6), sp.Rational(1, 3)]])
    base = normalized_kernel([a, b])
    assert base.is_positive_semidefinite

    frames = [sp.eye(2), sp.Matrix([[1, 1], [0, 1]]), sp.diag(2, sp.Rational(1, 2))]
    frame_sum = sp.diag(*frames)
    framed = frame_sum * base * frame_sum.T
    assert framed.is_positive_semidefinite
    assert framed[:2, :2] == frames[0] * frames[0].T
    assert framed[2:4, 2:4] == frames[1] * frames[1].T
    restricted_frames = sp.diag(*frames[:2])
    assert framed[:4, :4] == restricted_frames * normalized_kernel([a]) * restricted_frames.T

    changes = [sp.Matrix([[1, 2], [0, 1]]), sp.diag(3, sp.Rational(1, 3)), sp.Matrix([[2, 1], [1, 1]])]
    assert all(change.det() != 0 for change in changes)
    changed_frames = [change * frame for change, frame in zip(changes, frames)]
    change_sum = sp.diag(*changes)
    changed_frame_sum = sp.diag(*changed_frames)
    assert changed_frame_sum * base * changed_frame_sum.T == change_sum * framed * change_sum.T

    for change in changes:
        companion = change
        conjoint = change.inv()
        assert conjoint * companion == sp.eye(2)
        assert companion * conjoint == sp.eye(2)
        assert companion * conjoint * companion == companion
        assert conjoint * companion * conjoint == conjoint

    rotation = sp.Matrix([[0, -1], [1, 0]])
    assert frames[1] * frames[1].T == (frames[1] * rotation) * (frames[1] * rotation).T
    assert frames[1] != frames[1] * rotation

    result = {
        "schema": "marici.voevodsky.framed-metric-markov-gl-equipment.v1",
        "status": "finite_framed_GL_equipment_fragment_verified",
        "framed_kernel_positive": True,
        "shear_and_scaling_targets_admitted": True,
        "metric_congruence_natural": True,
        "GL_companions_conjoints": True,
        "inverse_triangle_identities": True,
        "contiguous_beck_chevalley": True,
        "metric_only_descent_verified": False,
        "frame_nonuniqueness_witnessed": True,
        "infinite_completion_verified": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
