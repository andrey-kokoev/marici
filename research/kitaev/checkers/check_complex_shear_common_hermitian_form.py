#!/usr/bin/env python3
"""Exact audit of common Hermitian forms for rank-two complex shears."""

import hashlib
import json
from pathlib import Path

from sympy import I, Matrix, Rational, conjugate, det, simplify, symbols


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/complex-shear-common-hermitian-form.json"


def shear(F):
    return Matrix([[1, F], [0, 1]])


def adjoint(M):
    return conjugate(M.T)


def main():
    a, d, u, v, x, y = symbols("a d u v x y", real=True)
    b = u + I * v
    F = x + I * y
    H = Matrix([[a, b], [conjugate(b), d]])
    S = shear(F)
    residual = (adjoint(S) * H * S - H).applyfunc(simplify)
    expected = Matrix([
        [0, a * F],
        [a * conjugate(F), a * conjugate(F) * F + conjugate(F) * b + conjugate(b) * F],
    ]).applyfunc(simplify)
    assert residual == expected

    # Every complex shear is symplectic for the bilinear alternating form.
    J = Matrix([[0, 1], [-1, 0]])
    assert (S.T * J * S - J).applyfunc(simplify) == Matrix.zeros(2)

    # Exact collinear family and its common indefinite Hermitian form.
    q = Rational(1) + 2 * I
    bq = I * q
    Hq = Matrix([[0, bq], [conjugate(bq), Rational(3)]])
    collinear = [0, q, -2 * q, Rational(5, 3) * q]
    for coefficient in collinear:
        Sq = shear(coefficient)
        assert (adjoint(Sq) * Hq * Sq - Hq).applyfunc(simplify) == Matrix.zeros(2)
    assert simplify(det(Hq)) == -5

    # Hostile F={1,i}: solve the invariance equations directly.
    residual_one = residual.subs({x: 1, y: 0})
    residual_i = residual.subs({x: 0, y: 1})
    equations = [simplify(z) for z in list(residual_one) + list(residual_i)]
    # The explicit equations contain a=0, u=0, and v=0; d remains free.
    assert residual_one[0, 1] == a
    assert simplify(residual_one[1, 1].subs(a, 0)) == 2 * u
    assert residual_i[0, 1] == I * a
    assert simplify(residual_i[1, 1].subs(a, 0)) == 2 * v
    hostile_forced_det = simplify(det(H).subs({a: 0, u: 0, v: 0}))
    assert hostile_forced_det == 0

    # One nonzero coefficient forces every invariant nondegenerate form to be indefinite.
    invariant_det = simplify(det(H).subs(a, 0))
    assert invariant_det == -(u**2 + v**2)

    payload = {
        "schema": "marici.kitaev.complex_shear_common_hermitian_form.v1",
        "status": "pass",
        "strength": "exact rank-two algebraic theorem",
        "symbolic_residual": [[str(z) for z in residual.row(i)] for i in range(2)],
        "complex_symplectic_identity": "pass",
        "collinear_fixture": {
            "line_generator": str(q),
            "coefficients": [str(z) for z in collinear],
            "common_form": [[str(z) for z in Hq.row(i)] for i in range(2)],
            "determinant": str(det(Hq)),
            "signature": [1, 1],
        },
        "noncollinear_hostile": {
            "coefficients": ["1", "I"],
            "forced_parameters": {"a": 0, "u": 0, "v": 0},
            "forced_determinant": str(hostile_forced_det),
        },
        "positive_definite_common_form_for_nonzero_shear": False,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta coefficient derivation", "boundary-current metric",
            "parameter-dependent form", "larger realization", "passivity", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
