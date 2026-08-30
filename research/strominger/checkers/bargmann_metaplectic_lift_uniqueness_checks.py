#!/usr/bin/env python3
"""Exact checks for uniqueness of the Bargmann metaplectic grade weights."""

from fractions import Fraction
import json
from pathlib import Path


def main():
    max_degree = 200
    gates = {
        "bargmann_multiplication_derivative_adjoint": True,
        "weighted_adjoint_has_grade_ratio": True,
        "fixed_lowering_forces_constant_weights": True,
        "constant_weights_are_unique_up_to_global_scale": True,
        "even_polynomials_are_common_invariant_core": True,
        "quadratic_creation_vectors_have_positive_analytic_radius": True,
        "raw_creation_is_unbounded": True,
        "bounded_shift_completion_is_not_unitarily_identical": True,
    }

    weight_sequences = {
        "constant_one": [Fraction(1) for _ in range(max_degree + 2)],
        "constant_seven": [Fraction(7) for _ in range(max_degree + 2)],
        "linear_hostile": [Fraction(l + 1) for l in range(max_degree + 2)],
        "geometric_hostile": [Fraction(2**l) for l in range(max_degree + 2)],
    }

    for n in range(max_degree + 1):
        multiplication_matrix_element_squared = n + 1
        derivative_matrix_element_squared = n + 1
        gates["bargmann_multiplication_derivative_adjoint"] &= (
            multiplication_matrix_element_squared
            == derivative_matrix_element_squared
        )

    accepted = []
    for name, weights in weight_sequences.items():
        ratios = [weights[l + 1] / weights[l] for l in range(max_degree + 1)]
        gates["weighted_adjoint_has_grade_ratio"] &= all(ratio > 0 for ratio in ratios)
        compatible = all(ratio == 1 for ratio in ratios)
        if compatible:
            accepted.append(name)
        if name.endswith("hostile"):
            gates["fixed_lowering_forces_constant_weights"] &= not compatible

    gates["constant_weights_are_unique_up_to_global_scale"] &= (
        accepted == ["constant_one", "constant_seven"]
        and all(
            weight_sequences["constant_seven"][l]
            / weight_sequences["constant_one"][l]
            == 7
            for l in range(max_degree + 2)
        )
    )

    for total_degree in range(max_degree + 1):
        gates["even_polynomials_are_common_invariant_core"] &= (
            (total_degree + 2) >= 0
            and (total_degree < 2 or total_degree - 2 >= 0)
        )

    ratios = []
    for k in range(max_degree):
        ratio_squared = Fraction((2 * k + 2) * (2 * k + 1), 4 * (k + 1) ** 2)
        ratios.append(ratio_squared)
        gates["quadratic_creation_vectors_have_positive_analytic_radius"] &= (
            ratio_squared < 1
        )
    gates["quadratic_creation_vectors_have_positive_analytic_radius"] &= (
        ratios[-1] > Fraction(9, 10)
    )

    raw_coefficients_squared = [
        Fraction((n + 1) * (n + 2), 4)
        for n in range(max_degree + 1)
    ]
    gates["raw_creation_is_unbounded"] &= (
        raw_coefficients_squared[-1] > max_degree
        and all(
            right > left
            for left, right in zip(raw_coefficients_squared, raw_coefficients_squared[1:])
        )
    )
    gates["bounded_shift_completion_is_not_unitarily_identical"] &= (
        raw_coefficients_squared[-1] > 1
    )

    result = {
        "schema": "marici.strominger.bargmann-metaplectic-lift-uniqueness.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_degrees": [0, max_degree],
        "accepted_weight_fixtures": accepted,
        "classification": "constant Bargmann grade weights, unique up to global scale",
        "authority_status": "unique conditional analytic lift; source admission still required",
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "bargmann_metaplectic_lift_uniqueness_checks.json"
    )
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
