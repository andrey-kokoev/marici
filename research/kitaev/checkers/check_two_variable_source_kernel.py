#!/usr/bin/env python3
"""Exact audit of the two-variable source-kernel compiler."""

import hashlib
import json
from pathlib import Path

from sympy import I, Matrix, Rational, Symbol, conjugate, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/two-variable-source-kernel.json"


def adjoint(M):
    return conjugate(M.T)


def main():
    w = Symbol("w")
    J0 = Matrix.eye(2)
    J1 = Matrix([[0, 1], [1, 0]])
    J2 = Matrix([[1, I], [0, 1]])
    coefficients = [J0, J1, J2]

    def feature(value):
        return sum((coefficient * value**n for n, coefficient in enumerate(coefficients)), Matrix.zeros(2))

    def kernel(z, value):
        return (adjoint(feature(z)) * feature(value)).applyfunc(simplify)

    # Mixed coefficient block matrix is T^*T and hence PSD.
    T = J0.row_join(J1).row_join(J2)
    block_gram = adjoint(T) * T
    for m in range(3):
        for n in range(3):
            block = block_gram[2*m:2*m+2, 2*n:2*n+2]
            assert block == adjoint(coefficients[m]) * coefficients[n]
    assert block_gram.rank() == T.rank()

    # Direct finite kernel positivity identity.
    points = [Rational(0), Rational(1, 2), 1 + I]
    states = [Matrix([1, 0]), Matrix([1, -1]), Matrix([I, 2])]
    quadratic = 0
    feature_sum = Matrix.zeros(2, 1)
    for i in range(3):
        feature_sum += feature(points[i]) * states[i]
        for j in range(3):
            quadratic += (adjoint(states[i]) * kernel(points[i], points[j]) * states[j])[0]
    norm_squared = (adjoint(feature_sum) * feature_sum)[0]
    assert simplify(quadratic - norm_squared) == 0

    # Distinct minimal reciprocal carrier related by a unitary.
    U = Matrix([[0, 1], [1, 0]])
    assert adjoint(U) * U == Matrix.eye(2)
    for z in points:
        for value in points:
            direct = kernel(z, value)
            reciprocal = adjoint(U * feature(z)) * (U * feature(value))
            assert (direct - reciprocal).applyfunc(simplify) == Matrix.zeros(2)
    assert J0.rank() == 2  # generated feature span is already the whole carrier

    # Same kernel on a larger nonminimal carrier with one dark summand.
    def dark_feature(value):
        return (U * feature(value)).col_join(Matrix.zeros(1, 2))
    for z in points:
        for value in points:
            assert (adjoint(dark_feature(z)) * dark_feature(value) - kernel(z, value)).applyfunc(simplify) == Matrix.zeros(2)
    assert dark_feature(0).rank() == 2
    assert dark_feature(0).rows == 3

    # A scalar state compression misses an orthogonal operator direction.
    e1 = Matrix([1, 0])
    K_a = Matrix.eye(2)
    K_b = Matrix([[1, 0], [0, 4]])
    scalar_a = (adjoint(e1) * K_a * e1)[0]
    scalar_b = (adjoint(e1) * K_b * e1)[0]
    assert scalar_a == scalar_b == 1
    assert K_a != K_b

    # Circular Xi polarization is PSD even with an explicit off-target zero.
    def xi(value):
        return (value - 1) * (value - (1 + I))
    xi_points = [0, 2, I]
    xi_values = Matrix([xi(value) for value in xi_points])
    xi_gram = conjugate(xi_values) * xi_values.T
    assert xi_gram == adjoint(xi_values.T) * xi_values.T
    assert xi_gram.rank() == 1
    assert xi(1 + I) == 0
    xi_test = Matrix([1, -2, I])
    xi_quadratic = simplify((adjoint(xi_test) * xi_gram * xi_test)[0])
    xi_norm = simplify((xi_values.T * xi_test)[0].conjugate() * (xi_values.T * xi_test)[0])
    assert xi_quadratic == xi_norm

    payload = {
        "schema": "marici.kitaev.two_variable_source_kernel.v1",
        "status": "pass",
        "strength": "finite operator-analytic compiler theorem",
        "mixed_jet_block_count": 9,
        "mixed_block_gram_rank": block_gram.rank(),
        "finite_kernel_positivity_identity": "pass",
        "direct_reciprocal_unitary_factorization": "pass",
        "minimal_feature_dimension": 2,
        "dark_summand_hostile": {
            "ambient_dimension": 3,
            "generated_dimension": 2,
            "same_kernel": True,
        },
        "scalar_compression_hostile": {
            "common_scalar": str(scalar_a),
            "operator_kernels_distinct": True,
        },
        "circular_xi_polarization": {
            "positive_rank": xi_gram.rank(),
            "off_target_zero": "1 + I",
            "positive_despite_off_target_zero": True,
            "rejected_as_source_explanation": True,
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta source kernel", "completion bounds", "Fourier-Tate sewing",
            "signed arithmetic current", "zero orientation", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
