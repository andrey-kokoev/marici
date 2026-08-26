"""Exact WP573 frozen symmetric support-cover local measure jet."""

import json
from pathlib import Path

import sympy as sp


theta = sp.symbols("theta", real=True)
h = sp.Rational(1, 2)

amplitudes = sp.Matrix([1 + theta, 1, theta])
weights = amplitudes.applyfunc(lambda value: sp.expand(value**2))
central = weights.subs(theta, 0)
first = weights.diff(theta).subs(theta, 0)
second = weights.diff(theta, 2).subs(theta, 0)

minus = weights.subs(theta, -h)
plus = weights.subs(theta, h)
proposal = sp.simplify(minus + central + plus)

r_minus = sp.Matrix([sp.simplify(minus[index] / proposal[index]) for index in range(3)])
r_zero = sp.Matrix([sp.simplify(central[index] / proposal[index]) for index in range(3)])
r_plus = sp.Matrix([sp.simplify(plus[index] / proposal[index]) for index in range(3)])

first_density = sp.simplify((r_plus - r_minus) / (2 * h))
second_density = sp.simplify((r_plus - 2 * r_zero + r_minus) / h**2)
recovered_first = sp.simplify(sp.diag(*proposal) * first_density)
recovered_second = sp.simplify(sp.diag(*proposal) * second_density)

selected_central = central[:2, :]
selected_first = first[:2, :]
selected_rate = sp.simplify(sum(selected_central))
selected_rate_first = sp.simplify(sum(selected_first))
selected_shape = sp.simplify(selected_central / selected_rate)
selected_shape_first = sp.simplify(
    selected_first / selected_rate
    - selected_central * selected_rate_first / selected_rate**2
)

frozen_proposal_step = 1
neighbor_evaluation_step = 2
failure_observation_step = 2
adaptive_proposal_step = 3
frozen_authorized = frozen_proposal_step < neighbor_evaluation_step
adaptive_authorized = adaptive_proposal_step < failure_observation_step

checks = {
    "central_measure_matches_fixture": central == sp.Matrix([1, 1, 0]),
    "first_signed_measure_matches_fixture": first == sp.Matrix([2, 0, 0]),
    "second_measure_jet_matches_fixture": second == sp.Matrix([2, 0, 2]),
    "frozen_symmetric_proposal_dominates_all_cells": all(value > 0 for value in proposal),
    "first_density_recovers_signed_derivative": recovered_first == first,
    "second_density_recovers_second_jet": recovered_second == second,
    "quadratic_support_birth_is_first_order_invisible": central[2] == first[2] == 0,
    "quadratic_support_birth_has_nonzero_second_derivative": second[2] == 2,
    "selected_rate_and_derivative_are_two": selected_rate == selected_rate_first == 2,
    "selected_shape_is_uniform": selected_shape == sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)]),
    "selected_shape_derivative_is_relative_direction": selected_shape_first == sp.Matrix([sp.Rational(1, 2), sp.Rational(-1, 2)]),
    "frozen_proposal_precedes_evaluation": frozen_authorized,
    "adaptive_proposal_follows_failure_observation": not adaptive_authorized,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP573",
    "classification": "source-authorized frozen support-cover local measure jet, prospective separator input rather than selector or physical HHH claim",
    "amplitudes": encode_matrix(amplitudes),
    "weights": encode_matrix(weights),
    "central_measure": encode_matrix(central),
    "first_signed_measure": encode_matrix(first),
    "second_measure_jet": encode_matrix(second),
    "symmetric_step": str(h),
    "proposal_measure": encode_matrix(proposal),
    "proposal_densities": {
        "minus": encode_matrix(r_minus),
        "central": encode_matrix(r_zero),
        "plus": encode_matrix(r_plus),
    },
    "first_derivative_density": encode_matrix(first_density),
    "second_derivative_density": encode_matrix(second_density),
    "selected_factorization": {
        "rate": str(selected_rate),
        "rate_derivative": str(selected_rate_first),
        "shape": encode_matrix(selected_shape),
        "shape_derivative": encode_matrix(selected_shape_first),
        "null_central": str(central[2]),
        "null_first_derivative": str(first[2]),
        "null_second_derivative": str(second[2]),
        "exposure_port": "required to turn selected rate into a relational count response",
    },
    "hostiles": {
        "quadratic_support_birth": "null cell has zero central mass and first derivative but second derivative 2",
        "adaptive_proposal": {
            "failure_observed_step": failure_observation_step,
            "proposal_chosen_step": adaptive_proposal_step,
            "authorized": adaptive_authorized,
        },
    },
    "contextual_partition": "first-order shape and rate response omit quadratic support birth; the second local jet and completed null record retain it",
    "weak_basis_descent": "passes after a declared invariant portal-to-generator coupling path",
    "remaining_gate": "portal-complete frozen proposal, shower-detector transport, null or exposure completion, covariance, and robust resolution",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp573_symmetric_support_cover_measure_jet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
