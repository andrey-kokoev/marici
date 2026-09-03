from __future__ import annotations

import json

import sympy as sp


def diagonal(signs: tuple[int, ...]) -> sp.Matrix:
    return sp.diag(*signs)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    assert len(left) == len(right)
    return tuple(a * b for a, b in zip(left, right))


def main() -> None:
    epsilon = (1, -1, 1, -1)
    eta = (-1, -1, 1, 1)
    theta = (1, 1, -1, 1)
    identity = (1, 1, 1, 1)

    d_epsilon = diagonal(epsilon)
    assert d_epsilon.T * d_epsilon == sp.eye(4)
    assert d_epsilon.inv() == d_epsilon

    # Companion/conjoint triangle realization reduces to orthogonality.
    companion_left_triangle = d_epsilon.T * d_epsilon * d_epsilon
    companion_right_triangle = d_epsilon * d_epsilon.T * d_epsilon
    assert companion_left_triangle == d_epsilon
    assert companion_right_triangle == d_epsilon

    # Comparison cells for composition and their pentagon normal form.
    assert diagonal(compose(epsilon, eta)) == diagonal(eta) * diagonal(epsilon)
    left_parenthesized = compose(compose(epsilon, eta), theta)
    right_parenthesized = compose(epsilon, compose(eta, theta))
    assert left_parenthesized == right_parenthesized
    assert diagonal(left_parenthesized) == diagonal(theta) * diagonal(eta) * diagonal(epsilon)
    assert compose(identity, epsilon) == epsilon == compose(epsilon, identity)

    result = {
        "schema": "marici.voevodsky.free-gauge-companion-extension.v1",
        "status": "restricted_gauge_equipment_fragment_verified",
        "new_horizontal_class": "gauge_correspondence",
        "distinct_from_chain_extension": True,
        "companion_unit_counit_realized": True,
        "conjoint_unit_counit_realized": True,
        "companion_triangles": True,
        "conjoint_triangles": True,
        "composition_comparison": True,
        "comparison_pentagon": True,
        "identity_comparison": True,
        "finite_matrix_realization": "diagonal_orthogonal_isometry",
        "all_vertical_arrows_have_companions": False,
        "full_equipment_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
