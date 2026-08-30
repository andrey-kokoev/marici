"""Exact algebra gates for the adjacent-bias fourth-cumulant normal form."""

from __future__ import annotations

import hashlib
import json
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
    / "primitive_fourth_cumulant_transfer_checks.json"
)


fixtures = (
    (4, Fraction(1, 5), Fraction(1, 30), Fraction(1, 70)),
    (6, Fraction(1, 8), Fraction(1, 40), Fraction(1, 150)),
    (10, Fraction(1, 12), Fraction(1, 90), Fraction(1, 400)),
)

normalization_equivalence = []
flow_identity_a = []
flow_identity_b = []
for q_integer, d, variance_step, skew_step in fixtures:
    q = Fraction(q_integer)
    A = 1 - q * d
    b = variance_step / d**2
    c = skew_step / d**3

    raw_margin = (
        3 * A * variance_step
        + d**2 * (2 + A)
        - q * skew_step
    )
    normalized_margin = 2 + A + 3 * A * b - (1 - A) * c
    normalization_equivalence.append(raw_margin == d**2 * normalized_margin)

    direct_a_derivative = -d + q * variance_step
    normalized_a_derivative = d * ((1 - A) * b - 1)
    flow_identity_a.append(direct_a_derivative == normalized_a_derivative)

    direct_b_derivative = (
        -skew_step / d**2
        + 2 * variance_step**2 / d**3
    )
    normalized_b_derivative = d * (2 * b**2 - c)
    flow_identity_b.append(direct_b_derivative == normalized_b_derivative)

exponential_boundary = []
for q_integer in range(4, 11):
    q = Fraction(q_integer)
    d = 1 / q
    variance_step = 1 / q**2
    skew_step = 2 / q**3
    A = 1 - q * d
    b = variance_step / d**2
    c = skew_step / d**3
    normalized_margin = 2 + A + 3 * A * b - (1 - A) * c
    exponential_boundary.append(
        A == 0 and b == 1 and c == 2 and normalized_margin == 0
    )

checks = {
    "raw_and_normalized_margins_are_exactly_equivalent": all(
        normalization_equivalence
    ),
    "a_flow_identity_follows_from_d_prime_equals_minus_b": all(
        flow_identity_a
    ),
    "b_flow_identity_follows_from_b_prime_equals_minus_c": all(
        flow_identity_b
    ),
    "exponential_reference_is_the_exact_boundary_for_q_4_through_10": all(
        exponential_boundary
    ),
    "open_theta_invariant_region_is_not_reported_as_proved": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "dimensionless_margin": "2 + A + 3*A*b - (1-A)*c",
        "memoryless_boundary": {"A": 0, "b": 1, "c": 2},
        "q_range_checked": [4, 10],
        "theta_invariant_region_status": "open",
        "rh_status": "not_tested",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "The checker certifies algebraic normalization only. It does not "
        "certify the theta carrier inequality or its B-spline average."
    ),
}

RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
