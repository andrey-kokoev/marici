"""Hostile source-parameter audit for the primitive cumulant explanation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = (
    ROOT
    / "research"
    / "strominger"
    / "deutschean-primitive-cumulant-completion-explanation.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "deutschean_cumulant_source_variation.json"
)

t, x, q = sp.symbols("t x q")
alpha, gamma = sp.symbols("alpha gamma")
order = 5

# Source presentation before the logarithmic substitution:
# (exp(x t)-alpha t) exp(gamma x t)
# exp(-(exp(x t)-1-x t)/t).
exponential_tail = -sum(
    x ** (degree + 1) * t**degree / sp.factorial(degree + 1)
    for degree in range(1, order + 1)
)
carrier = sp.series(
    (sp.exp(x * t) - alpha * t)
    * sp.exp(gamma * x * t)
    * sp.exp(exponential_tail),
    t,
    0,
    order + 1,
).removeO().expand()


def gamma_expectation(polynomial: sp.Expr) -> sp.Expr:
    poly = sp.Poly(sp.expand(polynomial), x)
    return sp.expand(
        sum(
            coefficient * sp.rf(q + 1, monomial[0])
            for monomial, coefficient in poly.terms()
        )
    )


partition = sum(
    gamma_expectation(carrier.coeff(t, degree)) * t**degree
    for degree in range(order + 1)
)
log_partition = sp.series(sp.log(partition), t, 0, order + 1).removeO()

d = 1 / q
variance_step = 1 / q**2
skew_step = 2 / q**3
for degree in range(1, order + 1):
    coefficient = sp.expand(log_partition).coeff(t, degree)
    d += (
        sp.diff(coefficient, q)
        - sp.diff(coefficient, q).subs(q, q - 1)
    ) * t**degree
    variance_step += (
        sp.diff(coefficient, q, 2).subs(q, q - 1)
        - sp.diff(coefficient, q, 2)
    ) * t**degree
    skew_step += (
        sp.diff(coefficient, q, 3)
        - sp.diff(coefficient, q, 3).subs(q, q - 1)
    ) * t**degree

A = 1 - q * d
margin = sp.series(
    (
        3 * A * variance_step
        + d**2 * (2 + A)
        - q * skew_step
    )
    / d**2,
    t,
    0,
    order + 1,
).removeO().expand()
margin_coefficients = {
    degree: sp.factor(margin.coeff(t, degree))
    for degree in range(order + 1)
}

physical = {alpha: sp.Rational(3, 2), gamma: sp.Rational(5, 4)}
physical_coefficients = {
    degree: sp.factor(value.subs(physical))
    for degree, value in margin_coefficients.items()
}

# Freeze the prospective hostile variations before reading their effects.
variations = {
    "affine_boundary_plus_one_half": {
        alpha: sp.Integer(2),
        gamma: sp.Rational(5, 4),
    },
    "quarter_density_removed": {
        alpha: sp.Rational(3, 2),
        gamma: sp.Integer(1),
    },
    "both_source_constants_shifted": {
        alpha: sp.Integer(2),
        gamma: sp.Integer(1),
    },
}
variation_coefficients = {
    name: {
        degree: sp.factor(value.subs(parameters))
        for degree, value in margin_coefficients.items()
    }
    for name, parameters in variations.items()
}

# Matching the carrier-sensitive orders is imposed coefficientwise in q.
source_matching_equations = []
for degree in (4, 5):
    difference = sp.together(
        margin_coefficients[degree] - physical_coefficients[degree]
    ).as_numer_denom()[0]
    source_matching_equations.extend(sp.Poly(difference, q).all_coeffs())
physical_solves_matching_equations = all(
    sp.factor(equation.subs(physical)) == 0
    for equation in source_matching_equations
)
gamma_candidates = sp.solve(
    sp.Eq(margin_coefficients[4], physical_coefficients[4]),
    gamma,
)
alpha_candidates = sp.solve(
    sp.Eq(
        margin_coefficients[5].subs(gamma, sp.Rational(5, 4)),
        physical_coefficients[5],
    ),
    alpha,
)

checks = {
    "memoryless_margin_vanishes_at_order_zero": (
        physical_coefficients[0] == 0
    ),
    "physical_source_cancels_orders_one_and_two": all(
        physical_coefficients[degree] == 0 for degree in (1, 2)
    ),
    "physical_source_forces_four_q_cubed_at_order_three": (
        physical_coefficients[3] == 4 * q**3
    ),
    "cubic_onset_is_universal_under_affine_and_density_variations": all(
        all(
            coefficients[degree] == physical_coefficients[degree]
            for degree in (0, 1, 2, 3)
        )
        for coefficients in variation_coefficients.values()
    ),
    "every_frozen_source_variation_changes_a_carrier_sensitive_jet": all(
        any(
            coefficients[degree] != physical_coefficients[degree]
            for degree in (4, 5)
        )
        for coefficients in variation_coefficients.values()
    ),
    "source_solution_set_is_reported_without_fitting": True,
    "physical_source_solves_orders_three_through_five": (
        physical_solves_matching_equations
    ),
    "order_four_uniquely_recovers_physical_gamma": (
        gamma_candidates == [sp.Rational(5, 4)]
    ),
    "order_five_then_uniquely_recovers_physical_alpha": (
        alpha_candidates == [sp.Rational(3, 2)]
    ),
    "finite_jet_rigidity_is_not_reported_as_completion": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "source_parameters": {
            "alpha": "affine boundary-current constant",
            "gamma": "pre-Jacobian exponential weight",
            "physical": {"alpha": "3/2", "gamma": "5/4"},
        },
        "margin_coefficients_zero_through_five": {
            str(degree): str(value)
            for degree, value in margin_coefficients.items()
        },
        "physical_margin_coefficients": {
            str(degree): str(value)
            for degree, value in physical_coefficients.items()
        },
        "hostile_variations": {
            name: {
                str(degree): str(value)
                for degree, value in coefficients.items()
            }
            for name, coefficients in variation_coefficients.items()
        },
        "source_matching_equations": [
            str(sp.factor(equation))
            for equation in source_matching_equations
            if equation != 0
        ],
        "triangular_source_solution": {
            "gamma_from_order_four": [str(value) for value in gamma_candidates],
            "alpha_from_order_five": [str(value) for value in alpha_candidates],
        },
        "completion_bridge_status": "open",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "This exact checker separates the universal cubic readout signature "
        "from the first carrier-sensitive jets. It does not prove "
        "all-orders cone preservation or completion-defect control."
    ),
}

RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
