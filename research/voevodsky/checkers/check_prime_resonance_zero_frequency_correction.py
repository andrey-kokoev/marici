from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    xi = sp.Symbol("xi", nonnegative=True)
    coefficients = [sp.Integer(2), sp.Integer(3), sp.Integer(5)]
    frequencies = [sp.Integer(1), sp.Integer(2), sp.Integer(4)]
    mass = sum(coefficients)
    symbol = sum(coefficient * sp.cos(xi * frequency) for coefficient, frequency in zip(coefficients, frequencies))
    residual = symbol - sp.log(1 + xi)
    assert sp.simplify(residual.subs(xi, 0) - mass) == 0

    # Structural bound: cos <= 1 and log(1+xi) >= 0 for xi >= 0.
    structural_upper_bound = mass
    high_frequency_threshold = sp.Integer(3)
    restricted_crude_bound = mass - sp.log(1 + high_frequency_threshold)
    assert restricted_crude_bound < mass

    samples = [sp.Integer(0), sp.Rational(1, 2), sp.Integer(1), sp.Integer(2), sp.Integer(3), sp.Integer(5)]
    sample_values = [sp.simplify(residual.subs(xi, value)) for value in samples]
    assert all(value <= mass for value in sample_values)

    result = {
        "schema": "marici.voevodsky.prime-resonance-zero-frequency-correction.v1",
        "status": "unrestricted_scalar_maximum_exactly_coefficient_mass",
        "fixture_coefficients": [str(value) for value in coefficients],
        "fixture_frequencies": [str(value) for value in frequencies],
        "coefficient_mass": str(mass),
        "residual_at_zero": str(residual.subs(xi, 0)),
        "sharp_unrestricted_constant": str(structural_upper_bound),
        "global_branch_and_bound_required": False,
        "high_frequency_threshold_fixture": str(high_frequency_threshold),
        "restricted_crude_bound": str(restricted_crude_bound),
        "restricted_problem_nontrivial": True,
        "actual_interval_operator_analyzed": False,
        "next_gate": "declare xi_0 or analyze interval overlap operator",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
