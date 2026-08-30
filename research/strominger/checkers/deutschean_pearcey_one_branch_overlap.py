#!/usr/bin/env python3
"""Compute exact one-branch Pearcey-to-Gaussian overlap coefficients."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_pearcey_one_branch_overlap.json"
epsilon = s.symbols("epsilon")


def gaussian_even_moment(power):
    if power == 0:
        return s.Integer(1)
    return s.factorial2(power - 1)


order = 5
partition_series = sum(
    (-1)**j * gaussian_even_moment(4*j) * epsilon**j
    / (4**j * s.factorial(j))
    for j in range(order)
)
second_numerator = sum(
    (-1)**j * gaussian_even_moment(4*j + 2) * epsilon**j
    / (4**j * s.factorial(j))
    for j in range(order)
)
variance_factor = s.series(second_numerator / partition_series, epsilon, 0, order).removeO().expand()
log_partition_factor = s.series(s.log(partition_series), epsilon, 0, order).removeO().expand()

checks = {
    "partition_first_correction_is_minus_three_quarters": partition_series.coeff(epsilon, 1) == -s.Rational(3, 4),
    "partition_second_correction_is_105_over_32": partition_series.coeff(epsilon, 2) == s.Rational(105, 32),
    "variance_first_correction_is_minus_three": variance_factor.coeff(epsilon, 1) == -3,
    "log_partition_first_correction_is_minus_three_quarters": log_partition_factor.coeff(epsilon, 1) == -s.Rational(3, 4),
    "all_coefficients_are_exact_rationals": all(
        value.is_Rational for polynomial in (partition_series, variance_factor, log_partition_factor)
        for value in s.Poly(polynomial, epsilon).all_coeffs()
    ),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "overlap_parameter": "epsilon=A^(-2)",
        "partition_factor": str(partition_series),
        "log_partition_factor": str(log_partition_factor),
        "variance_factor": str(variance_factor),
        "P_asymptotic": "sqrt(2*pi/A)*partition_factor",
        "connected_variance_asymptotic": "A^(-1)*variance_factor",
        "first_terms": {
            "P": "sqrt(2*pi/A)*(1-3/(4*A^2)+105/(32*A^4)+...)",
            "variance": "1/A-3/A^3+24/A^5+...",
        },
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact formal overlap coefficients for the canonical one-branch "
        "Pearcey integral. They recover the Gaussian propagator and its quartic "
        "corrections. They do not yet include the source-specific Gamma amplitude "
        "or adjacent-grade H1/H2 normalization."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
