from __future__ import annotations

import json

import sympy as sp


def projector(vector: sp.Matrix) -> sp.Matrix:
    return vector * vector.T


def bargmann(projectors: list[sp.Matrix]) -> sp.Expr:
    value = sp.eye(projectors[0].rows)
    for item in projectors:
        value *= item
    return sp.simplify(sp.trace(value))


def transition_squared(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(left * right))


def main() -> None:
    e1 = sp.Matrix([1, 0])
    e2 = sp.Matrix([0, 1])
    diagonal = sp.Matrix([sp.sqrt(2) / 2, sp.sqrt(2) / 2])

    quadruple_a = [projector(vector) for vector in (e1, e2, e1, e2)]
    quadruple_b = [projector(vector) for vector in (e1, e2, e1, diagonal)]
    assert bargmann(quadruple_a) == 0
    assert bargmann(quadruple_b) == 0

    pairwise_a = sp.Matrix(4, 4, lambda i, j: transition_squared(quadruple_a[i], quadruple_a[j]))
    pairwise_b = sp.Matrix(4, 4, lambda i, j: transition_squared(quadruple_b[i], quadruple_b[j]))
    assert pairwise_a != pairwise_b
    assert pairwise_a[0, 3] == 0
    assert pairwise_b[0, 3] == sp.Rational(1, 2)

    # Any simultaneous unitary preserving labelled P1=e1 and P2=e2 preserves
    # their transition values with P4, so the collision is quotient-distinct.
    assert quadruple_a[:3] == quadruple_b[:3]
    assert transition_squared(quadruple_a[0], quadruple_a[3]) != transition_squared(quadruple_b[0], quadruple_b[3])

    reversed_a = bargmann(list(reversed(quadruple_a)))
    reversed_b = bargmann(list(reversed(quadruple_b)))
    assert reversed_a == reversed_b == 0

    result = {
        "schema": "marici.voevodsky.bargmann-loop-identifiability.v1",
        "status": "global_Bargmann_nonfaithfulness_verified",
        "exact_collision_value": "0",
        "collision_pairwise_coordinate_residual": "P1-P4 squared overlap: 0 versus 1/2",
        "labelled_projector_quadruples_inequivalent": True,
        "reversal_resolves_collision": False,
        "global_Bargmann_coordinate_monic": False,
        "frozen_D_S3_minus_one_eighth_fiber_computed": False,
        "first_missing_typed_object": "explicit admissible-family quotient parameterization",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
