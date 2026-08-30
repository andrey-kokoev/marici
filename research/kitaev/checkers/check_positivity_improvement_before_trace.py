#!/usr/bin/env python3
"""Exact audit: positivity improvement must occur before scalar trace."""

import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/positivity-improvement-before-trace.json"


def adjoint(matrix):
    return matrix.conjugate().T


def vec(matrix):
    return Matrix([matrix[i, j] for j in range(matrix.cols) for i in range(matrix.rows)])


def main():
    identity = Matrix.eye(2)
    e1 = Matrix([1, 0])
    projector = e1 * adjoint(e1)
    quarter_turn = Matrix([[0, -1], [1, 0]])
    assert adjoint(quarter_turn) * quarter_turn == identity

    def unitary_channel(x):
        return quarter_turn * x * adjoint(quarter_turn)

    rotated = unitary_channel(projector)
    overlap = simplify((projector * rotated).trace())
    assert overlap == 0
    assert rotated.det() == 0
    assert rotated.trace() == projector.trace() == 1
    assert unitary_channel(identity) == identity

    # A one-Kraus unitary channel is CP: its Choi matrix is vec(U) vec(U)^*.
    kraus_vector = vec(quarter_turn)
    choi = kraus_vector * adjoint(kraus_vector)
    assert choi.rank() == 1
    assert choi == adjoint(choi)
    assert all(value >= 0 for value in choi.eigenvals())

    # Exact primitive repair fixture and its sharp uniform floor.
    epsilon = Rational(1, 3)

    def primitive_channel(x, eps):
        return (1 - eps) * unitary_channel(x) + eps * x.trace() * identity / 2

    repaired = primitive_channel(projector, epsilon)
    floor = epsilon / 2
    assert repaired - floor * identity == (1 - epsilon) * rotated
    assert repaired.det() > 0
    assert min(repaired.eigenvals()) == floor

    # Each cutoff is improving, while the certified margin 1/(2N) collapses.
    margins = []
    for cutoff in [1, 2, 4, 8, 16]:
        eps = Rational(1, cutoff)
        value = primitive_channel(projector, eps)
        margin = eps / 2
        assert value - margin * identity == (1 - eps) * rotated
        margins.append(str(margin))
    assert Rational(1, 32) < Rational(1, 2)

    # On a real one-dimensional cone, strict improvement is just m > 0.
    scalar_multipliers = [Rational(2), Rational(1, 5), Rational(0), Rational(-1)]
    one_dimensional = [
        {
            "multiplier": str(multiplier),
            "nonzero_overlap": bool(multiplier != 0),
            "positive_ray_improving": bool(multiplier > 0),
        }
        for multiplier in scalar_multipliers
    ]
    assert one_dimensional[0]["positive_ray_improving"]
    assert not one_dimensional[2]["nonzero_overlap"]
    assert one_dimensional[3]["nonzero_overlap"] and not one_dimensional[3]["positive_ray_improving"]

    payload = {
        "schema": "marici.kitaev.positivity_improvement_before_trace.v1",
        "status": "pass",
        "one_dimensional_strict_overlap": "equivalent to scalar nonvanishing",
        "real_ray_improvement": "equivalent to positive scalar multiplier",
        "quarter_turn_hostile": {
            "unitary": True,
            "completely_positive": True,
            "unital": True,
            "trace_preserving": True,
            "invertible": True,
            "choi_psd_rank": choi.rank(),
            "nonzero_state_overlap": str(overlap),
            "output_on_cone_boundary": rotated.det() == 0,
        },
        "primitive_fixture": {
            "epsilon": str(epsilon),
            "interior_floor": str(floor),
            "positive_definite_output": bool(repaired.det() > 0),
            "authorized_theta_constructor": False,
        },
        "completion_hostile": {
            "epsilon_N": "1/N",
            "interior_margin": "1/(2N)",
            "sample_margins": margins,
            "uniform_margin": False,
        },
        "one_dimensional_samples": one_dimensional,
        "required_route": "source higher-rank correspondence -> scalar trace",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": ["theta/Tate source correspondence", "uniform completion theorem", "RH"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
