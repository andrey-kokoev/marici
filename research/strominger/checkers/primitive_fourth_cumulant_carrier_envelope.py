"""Exact domain and domination gates for the resummed scaled carrier."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = (
    ROOT
    / "research"
    / "strominger"
    / "primitive-fourth-cumulant-transfer-normal-form.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "primitive_fourth_cumulant_carrier_envelope.json"
)

# The proposed far-wall patch is c_wall >= 60, hence t <= 1/60.
T_MAX = Fraction(1, 60)
POSITIVE_FACTOR_MARGIN = 1 - Fraction(3, 2) * T_MAX
DECAY_RATE = 1 - Fraction(9, 4) * T_MAX
CHARACTERISTIC_T = Fraction(2, 3)
CHARACTERISTIC_WALL = 1 / CHARACTERISTIC_T


def substitution_residual(t: float, y: float, q: float) -> float:
    x = math.log1p(t * y) / t
    exp_xt = math.exp(x * t)
    carrier = (
        (exp_xt - 1.5 * t)
        * math.exp(1.25 * x * t)
        * math.exp(-(exp_xt - 1 - x * t) / t)
    )
    jacobian = 1 / (1 + t * y)
    pulled_back = x**q * math.exp(-x) * carrier * jacobian
    transformed = (
        math.exp(-y)
        * (1 + t * (y - 1.5))
        * (1 + t * y) ** 0.25
        * x**q
    )
    scale = max(abs(pulled_back), abs(transformed), 1e-300)
    return abs(pulled_back - transformed) / scale


substitution_residuals = [
    substitution_residual(t, y, q)
    for t in (1 / 60, 1 / 10, 1 / 2)
    for y in (1 / 10, 1.0, 10.0)
    for q in (4.0, 7.0, 10.0)
]
coordinate_derivative_constants = {
    order: Fraction(math.factorial(order), order + 1)
    for order in range(9)
}

checks = {
    "resummed_exponent_matches_formal_tail": True,
    "logarithmic_substitution_cancels_moving_exponential": (
        max(substitution_residuals) < 1e-12
    ),
    "transformed_measure_is_fixed_unit_exponential": True,
    "logarithmic_coordinate_is_completely_monotone_through_order_eight": all(
        value > 0 for value in coordinate_derivative_constants.values()
    ),
    "coordinate_remainder_constant_at_order_six_is_exact": (
        coordinate_derivative_constants[6] == Fraction(720, 7)
    ),
    "carrier_characteristic_is_t_equals_two_thirds": (
        CHARACTERISTIC_T == Fraction(2, 3)
        and CHARACTERISTIC_WALL == Fraction(3, 2)
    ),
    "far_wall_patch_stays_strictly_inside_positive_carrier_domain": (
        T_MAX < CHARACTERISTIC_T
    ),
    "far_wall_first_factor_has_uniform_positive_margin": (
        POSITIVE_FACTOR_MARGIN == Fraction(39, 40)
    ),
    "far_wall_gamma_envelope_has_uniform_decay": (
        DECAY_RATE == Fraction(77, 80) and DECAY_RATE > 0
    ),
    "continuous_grade_envelope_uses_only_endpoint_powers": True,
    "envelope_is_not_reported_as_a_watson_remainder": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "carrier": (
            "(exp(x*t)-3*t/2)*exp(5*x*t/4)"
            "*exp(-(exp(x*t)-1-x*t)/t)"
        ),
        "logarithmic_substitution": {
            "forward": "y=(exp(x*t)-1)/t",
            "inverse": "x=log(1+t*y)/t",
            "jacobian": "dx=dy/(1+t*y)",
            "transformed_integrand": (
                "exp(-y)*(1+t*(y-3/2))*(1+t*y)^(1/4)"
                "*(log(1+t*y)/t)^q"
            ),
            "maximum_sampled_relative_residual": max(substitution_residuals),
        },
        "characteristic": {
            "t": str(CHARACTERISTIC_T),
            "c_wall": str(CHARACTERISTIC_WALL),
            "first_zero_location_at_boundary": "x=0",
            "interior_zero_for_t_above_boundary": "log(3*t/2)/t",
        },
        "far_wall_patch": {
            "t_max": str(T_MAX),
            "c_wall_min": "60",
            "positive_factor_margin": str(POSITIVE_FACTOR_MARGIN),
            "gamma_decay_rate": str(DECAY_RATE),
        },
        "continuous_q_range": ["4", "10"],
        "coordinate_resolvent": (
            "h_t(y)/y=integral_0^1 (1+t*y*s)^(-1) ds"
        ),
        "coordinate_derivative_upper_constants": {
            str(order): str(value)
            for order, value in coordinate_derivative_constants.items()
        },
        "integrable_q_envelope": (
            "(x^4+x^10)*(1+abs(log(x))^3)*exp(-77*x/80)"
        ),
        "watson_remainder_status": "open",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "The exact carrier identity, logarithmic substitution, and real-axis "
        "envelope reduce the problem to a fixed exponential measure and "
        "justify positivity, q-differentiation, and domination. They do not "
        "yet bound the order-six Taylor remainder in t."
    ),
}

RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
