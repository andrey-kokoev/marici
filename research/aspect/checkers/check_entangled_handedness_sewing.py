from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


Matrix = tuple[tuple[F, ...], ...]
Vector = tuple[F, ...]


def quadratic_form(vector: Vector, matrix: Matrix) -> F:
    return sum(
        (vector[row] * matrix[row][column] * vector[column]
         for row in range(len(vector))
         for column in range(len(vector))),
        F(0),
    )


def partial_transpose_second(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(
            matrix[2 * (row // 2) + (column % 2)][2 * (column // 2) + (row % 2)]
            for column in range(4)
        )
        for row in range(4)
    )


def mix(left: Matrix, left_weight: F, right: Matrix, right_weight: F) -> Matrix:
    return tuple(
        tuple(left_weight * left[row][column] + right_weight * right[row][column]
              for column in range(4))
        for row in range(4)
    )


def main() -> None:
    zero = F(0)
    half = F(1, 2)
    quarter = F(1, 4)
    bell_phi_plus: Matrix = (
        (half, zero, zero, half),
        (zero, zero, zero, zero),
        (zero, zero, zero, zero),
        (half, zero, zero, half),
    )
    identity_over_four: Matrix = tuple(
        tuple(quarter if row == column else zero for column in range(4))
        for row in range(4)
    )
    antisymmetric: Vector = (zero, 1, -1, zero)

    bell_partial_transpose = partial_transpose_second(bell_phi_plus)
    bell_witness = quadratic_form(antisymmetric, bell_partial_transpose)
    witness_norm = quadratic_form(
        antisymmetric,
        tuple(tuple(F(1) if row == column else zero for column in range(4)) for row in range(4)),
    )
    bell_negative_eigenvalue = bell_witness / witness_norm
    assert bell_witness == -1
    assert bell_negative_eigenvalue == -half

    # Werner family: rho(p) = p |Phi+><Phi+| + (1-p) I/4.
    # The same antisymmetric vector has partial-transpose eigenvalue (1-3p)/4.
    threshold = F(1, 3)
    below, above = F(1, 4), F(1, 2)

    def witness_eigenvalue(p: F) -> F:
        state = mix(bell_phi_plus, p, identity_over_four, F(1) - p)
        transformed = partial_transpose_second(state)
        return quadratic_form(antisymmetric, transformed) / witness_norm

    assert witness_eigenvalue(threshold) == 0
    assert witness_eigenvalue(below) == F(1, 16)
    assert witness_eigenvalue(above) == F(-1, 8)

    # A real separable packet is unchanged by one-sided transpose and remains
    # a convex mixture of positive rank-one projectors.
    product_00: Matrix = (
        (F(1), zero, zero, zero),
        (zero, zero, zero, zero),
        (zero, zero, zero, zero),
        (zero, zero, zero, zero),
    )
    product_pp: Matrix = tuple(tuple(quarter for _ in range(4)) for _ in range(4))
    separable = mix(product_00, half, product_pp, half)
    assert partial_transpose_second(separable) == separable

    result = {
        "schema": "marici.aspect.entangled-handedness-sewing.v1",
        "status": "pass",
        "local_frame_involution": "transpose on the second polarization subsystem; X and Z fixed, Y sign reversed",
        "bell_partial_transpose_antisymmetric_eigenvalue": str(bell_negative_eigenvalue),
        "werner_npt_threshold": str(threshold),
        "werner_test_below_threshold": {"p": str(below), "eigenvalue": str(witness_eigenvalue(below))},
        "werner_test_above_threshold": {"p": str(above), "eigenvalue": str(witness_eigenvalue(above))},
        "separable_real_packet_unchanged": True,
        "verdict": "Composite positivity rejects the relative handedness reversal on the NPT locus but not on all separable records.",
        "optical_instrument": "source-authorized polarization-entangled pair plus joint Stokes tomography and positivity audit",
        "claim_boundary": "exact two-qubit Bell/Werner family; no finite-count tomography or detector-systematics model",
    }
    output = Path(__file__).parents[1] / "results" / "entangled_handedness_sewing.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
