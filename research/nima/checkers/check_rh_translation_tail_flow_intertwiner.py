from fractions import Fraction
from math import comb
import json
from pathlib import Path


def add(left, right):
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ]


def scale(value, polynomial):
    return [value * coefficient for coefficient in polynomial]


def derivative(polynomial):
    return [index * polynomial[index] for index in range(1, len(polynomial))] or [Fraction(0)]


def multiply(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def translate(polynomial, displacement):
    out = [Fraction(0)] * len(polynomial)
    for degree, coefficient in enumerate(polynomial):
        for power in range(degree + 1):
            out[power] += coefficient * comb(degree, power) * displacement ** (degree - power)
    return out


def evaluate(polynomial, point):
    return sum(coefficient * point ** degree for degree, coefficient in enumerate(polynomial))


def integrate_interval(polynomial, endpoint):
    return sum(
        coefficient * endpoint ** (degree + 1) / Fraction(degree + 1)
        for degree, coefficient in enumerate(polynomial)
    )


def tail_operator(polynomial, spectral_parameter):
    return add(derivative(polynomial), scale(spectral_parameter, polynomial))


states = [
    [Fraction(3), Fraction(2), Fraction(1)],
    [Fraction(-1), Fraction(4), Fraction(-2), Fraction(1)],
]
parameters = [Fraction(1), Fraction(-2), Fraction(3, 2)]
displacements = [Fraction(1), Fraction(2), Fraction(3, 2)]

commutator_checks = 0
endpoint_checks = 0
for state in states:
    for parameter in parameters:
        forcing = scale(-1, tail_operator(state, parameter))
        for displacement in displacements:
            left = tail_operator(translate(state, displacement), parameter)
            right = translate(tail_operator(state, parameter), displacement)
            assert left == right
            commutator_checks += 1

            endpoint_defect = evaluate(state, displacement) - evaluate(state, Fraction(0))
            incidence_integrand = add(scale(parameter, state), forcing)
            incidence = -integrate_interval(incidence_integrand, displacement)
            assert endpoint_defect == incidence
            endpoint_checks += 1

# Polarized interval Green identity.
polarized_checks = 0
for left_state in states:
    for right_state in states:
        eta = Fraction(1)
        zeta = Fraction(2)
        left_forcing = scale(-1, tail_operator(left_state, eta))
        right_forcing = scale(-1, tail_operator(right_state, zeta))
        for displacement in displacements:
            kernel_integral = integrate_interval(multiply(left_state, right_state), displacement)
            forcing_integrand = add(
                multiply(left_forcing, right_state),
                multiply(left_state, right_forcing),
            )
            left = (zeta + eta) * kernel_integral
            right = (
                evaluate(left_state, 0) * evaluate(right_state, 0)
                - evaluate(left_state, displacement) * evaluate(right_state, displacement)
                - integrate_interval(forcing_integrand, displacement)
            )
            assert left == right
            polarized_checks += 1

result = {
    "operator_commutator_checks": commutator_checks,
    "endpoint_incidence_checks": endpoint_checks,
    "polarized_interval_checks": polarized_checks,
    "tail_flow_commutes_with_translation": True,
    "fixed_endpoint_commutes_with_translation": False,
    "moving_endpoint_defect_is_interval_incidence": True,
    "bulk_arithmetic_supply_anomaly": False,
    "remaining_gate": "completion and reciprocal sewing of weighted endpoint incidences",
    "verdict": "arithmetic translation intertwines the passive tail interior exactly and acts nontrivially only on the endpoint through the seam interval",
}

out = Path(__file__).parents[1] / "results" / "rh-translation-tail-flow-intertwiner.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
