from __future__ import annotations

import json

import sympy as sp


def ray(angle: sp.Expr) -> sp.Matrix:
    return sp.Matrix([sp.cos(angle), sp.sin(angle)])


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.T)


def ordered_trace(operators: list[sp.Matrix]) -> sp.Expr:
    value = sp.eye(operators[0].rows)
    for operator in operators:
        value *= operator
    return sp.simplify(sp.trace(value))


def main() -> None:
    angles = [0, sp.pi / 3, 2 * sp.pi / 3, sp.pi]
    projectors = [projector(ray(angle)) for angle in angles]
    assert all(item.is_positive_semidefinite for item in projectors)
    negative_loop = ordered_trace(projectors)
    assert negative_loop == -sp.Rational(1, 8)
    commutators = [sp.simplify(projectors[i] * projectors[(i + 1) % 4] - projectors[(i + 1) % 4] * projectors[i]) for i in range(4)]
    assert any(commutator != sp.zeros(2) for commutator in commutators)

    # Commuting positive diagonal event fixtures have nonnegative products.
    commuting_fixtures = [
        [sp.diag(1, 2), sp.diag(3, 0), sp.diag(2, 1), sp.diag(4, 5)],
        [sp.diag(sp.Rational(1, 2), 0), sp.diag(1, 3), sp.diag(2, 2), sp.diag(0, 1)],
    ]
    commuting_values = []
    for fixture in commuting_fixtures:
        assert all(left * right == right * left for left in fixture for right in fixture)
        assert all(item.is_positive_semidefinite for item in fixture)
        value = ordered_trace(fixture)
        assert value >= 0
        commuting_values.append(value)

    # The scalar is not reconstructive: retain prior modality separation.
    coordinate_faithful = False
    positive_commutative_factorization_possible = bool(negative_loop >= 0)
    assert coordinate_faithful is False
    assert positive_commutative_factorization_possible is False

    result = {
        "schema": "marici.voevodsky.negative-loop-factorization-witness.v1",
        "status": "nonfaithful_separating_witness_verified",
        "exact_negative_loop": "-1/8",
        "factors_positive_rank_one": True,
        "ordered_factors_noncommuting": True,
        "commuting_positive_fixture_values": [str(value) for value in commuting_values],
        "coordinate_faithful": False,
        "positive_commutative_multiplicative_factorization_excluded": True,
        "signed_or_complex_quasiprobability_excluded": False,
        "physical_constructor_authorized": False,
        "coordinate_and_rival_exclusion_modalities_separate": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
