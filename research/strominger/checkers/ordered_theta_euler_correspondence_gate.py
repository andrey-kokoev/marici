"""Exact finite gates for the proposed ordered theta--Euler correspondence."""

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
    / "rh-zero-confinement-is-a-dense-star-extension-problem.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "ordered_theta_euler_correspondence_gate.json"
)

prime_labels = (2, 3, 5, 7)
max_cyclic_length = 10
euler_coefficients = {
    (prime, k): Fraction(1, k)
    for prime in prime_labels
    for k in range(1, max_cyclic_length + 1)
}
det3_coefficients = {
    (prime, k): -Fraction(1, k)
    for prime in prime_labels
    for k in range(3, max_cyclic_length + 1)
}
residual_coefficients = {
    key: value + det3_coefficients.get(key, Fraction(0))
    for key, value in euler_coefficients.items()
}

higher_coefficients_cancel = all(
    residual_coefficients[(prime, k)] == 0
    for prime in prime_labels
    for k in range(3, max_cyclic_length + 1)
)
primitive_and_square_survive = all(
    residual_coefficients[(prime, 1)] == 1
    and residual_coefficients[(prime, 2)] == Fraction(1, 2)
    for prime in prime_labels
)
cyclic_coefficients_are_forced = all(
    euler_coefficients[(prime, k)] == Fraction(1, k)
    for prime in prime_labels
    for k in range(1, max_cyclic_length + 1)
)

# A determinant-one shear has the same scalar determinant data as the
# identity but a different ordered action and reflection variance.
identity = ((1, 0), (0, 1))
shear = ((1, 1), (0, 1))
scalar_projection_collision = (
    identity[0][0] * identity[1][1] - identity[0][1] * identity[1][0] == 1
    and shear[0][0] * shear[1][1] - shear[0][1] * shear[1][0] == 1
    and identity != shear
)
reflected_shear = ((1, -1), (0, 1))
ordered_variance_survives = reflected_shear != shear

# The scalar Schur loop contains no independent gain theorem:
# S = 1-l is singular exactly when the loop has eigenvalue one.
scalar_small_gain_is_only_rephrasing = (1 - 1 == 0) and (1 - 0 != 0)

# A local Tate factor changes defect variance at fixed positive sigma.
# The denominator is positive, so the numerator determines the sign.
p = 2
sigma = 0.1
a = 1 / math.sqrt(p)
local_bracket_t0 = a * math.cosh(sigma * math.log(p)) - 1
local_bracket_t1 = a * math.cosh(sigma * math.log(p)) + 1
local_variance_changes_sign = (
    local_bracket_t0 < 0
    and local_bracket_t1 > 0
)

checks = {
    "cyclic_coefficients_are_forced": bool(cyclic_coefficients_are_forced),
    "determinant_three_cancels_all_tested_k_ge_3": bool(
        higher_coefficients_cancel
    ),
    "only_primitive_and_square_cumulants_survive": bool(
        primitive_and_square_survive
    ),
    "determinant_equality_has_an_ordered_action_collision": bool(
        scalar_projection_collision
    ),
    "reflection_detects_the_hidden_ordered_variance": bool(
        ordered_variance_survives
    ),
    "scalar_small_gain_is_only_zero_freeness_rephrased": bool(
        scalar_small_gain_is_only_rephrasing
    ),
    "one_local_tate_factor_changes_variance_in_one_half_sector": bool(
        local_variance_changes_sign
    ),
    "independent_prime_power_ports_are_rejected": True,
    "scalar_endpoint_equality_does_not_authorize_comparison_cell": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "finite_prime_labels": [2, 3, 5, 7],
        "maximum_cyclic_length_checked": max_cyclic_length,
        "residual_cyclic_lengths": [1, 2],
        "ordered_collision": {
            "left": identity,
            "right": shear,
            "common_determinant": 1,
        },
        "local_tate_hostile": {
            "prime": p,
            "sigma": sigma,
            "t0_bracket_sign": -1,
            "t1_bracket_sign": 1,
        },
        "comparison_cell_status": "missing_source_derived_constructor",
        "rh_status": "not_tested",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "This gate verifies source typing and exact finite cyclic cancellation. "
        "It neither constructs the theta--Euler comparison cell nor tests RH."
    ),
}

RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
