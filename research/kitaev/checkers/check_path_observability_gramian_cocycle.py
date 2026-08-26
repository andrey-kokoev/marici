#!/usr/bin/env python3
"""Exact audit of the twisted observability-Gramian cocycle."""

import hashlib
import json
from itertools import product
from pathlib import Path

from sympy import I, Matrix, Rational, conjugate, simplify, symbols


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/path-observability-gramian-cocycle.json"


def adjoint(M):
    return conjugate(M.T)


def shear(F):
    return Matrix([[1, F], [0, 1]])


def kernel_vectors(M, bound=2):
    out = set()
    for x, y in product(range(-bound, bound + 1), repeat=2):
        v = Matrix([x, y])
        if M * v == Matrix.zeros(M.rows, 1):
            out.add((x, y))
    return out


def main():
    # Symbolic cocycle from the stacked observation map.
    f = symbols("f", real=True)
    S = shear(f)
    J1 = Matrix([[1, 0]])
    J2 = Matrix([[0, 1], [1, 1]])
    stacked = J1.col_join(J2 * S)
    direct = adjoint(stacked) * stacked
    cocycle = adjoint(J1) * J1 + adjoint(S) * adjoint(J2) * J2 * S
    assert (direct - cocycle).applyfunc(simplify) == Matrix.zeros(2)

    # Exhaustive exact kernel-intersection checks on small integer fixtures.
    kernel_checks = 0
    for f_value in (-2, -1, 0, 1, 2):
        Sf = shear(Rational(f_value))
        for j1 in product((-1, 0, 1), repeat=2):
            for j2 in product((-1, 0, 1), repeat=2):
                A = Matrix([j1])
                B = Matrix([j2])
                W1 = adjoint(A) * A
                W2 = adjoint(B) * B
                W = W1 + adjoint(Sf) * W2 * Sf
                lhs = kernel_vectors(W)
                rhs = {
                    v for v in kernel_vectors(W1)
                    if W2 * Sf * Matrix(v) == Matrix.zeros(2, 1)
                }
                assert lhs == rhs
                kernel_checks += 1

    # Identity total shear with a positive path Gramian.
    F = Rational(2, 3) + Rational(1, 2) * I
    S1 = shear(F)
    S2 = shear(-F)
    assert S2 * S1 == Matrix.eye(2)
    C = Matrix([[1, 0]])
    segment = adjoint(C) * C
    W_identity_path = segment + adjoint(S1) * segment * S1
    expected = Matrix([[2, F], [conjugate(F), conjugate(F) * F]])
    assert (W_identity_path - expected).applyfunc(simplify) == Matrix.zeros(2)
    determinant = simplify(W_identity_path.det())
    assert determinant == Rational(25, 36)
    assert W_identity_path[0, 0] > 0 and determinant > 0
    assert W_identity_path != Matrix.zeros(2)

    # Same endpoint, different path energy.
    zero_path_gramian = Matrix.zeros(2)
    assert S2 * S1 == Matrix.eye(2)
    assert W_identity_path != zero_path_gramian

    # Positive finite family with a collapsing normalized direction.
    collapse = []
    e2 = Matrix([0, 1])
    for N in (2, 3, 5, 10, 20):
        eps = Rational(1, N)
        SN = shear(eps)
        WN = segment + adjoint(SN) * segment * SN
        detN = simplify(WN.det())
        energy = simplify((adjoint(e2) * WN * e2)[0])
        assert WN[0, 0] == 2
        assert detN == eps**2 and detN > 0
        assert energy == eps**2
        collapse.append({"N": N, "determinant": str(detN), "e2_energy": str(energy)})

    payload = {
        "schema": "marici.kitaev.path_observability_gramian_cocycle.v1",
        "status": "pass",
        "strength": "finite-dimensional compiler theorem",
        "symbolic_cocycle": "pass",
        "kernel_intersection_checks": kernel_checks,
        "identity_endpoint_hostile": {
            "F": str(F),
            "total_shear": "I_2",
            "path_gramian": [[str(z) for z in W_identity_path.row(i)] for i in range(2)],
            "determinant": str(determinant),
            "zero_observation_path_same_endpoint": True,
        },
        "collapsing_positive_family": collapse,
        "limiting_normalized_direction_energy": "0",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta observation rows", "uniform theta observability",
            "positive reciprocal energy", "passivity", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
