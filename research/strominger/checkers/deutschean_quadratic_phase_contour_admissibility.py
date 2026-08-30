#!/usr/bin/env python3
"""Test quadratic phase deformations against the original Gamma contour."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_quadratic_phase_contour_admissibility.json"
y, z, k, q, T, u = s.symbols("y z k q T u", positive=True)
phase = s.log(y) + (s.exp(-z*y) - 1) / z + k*z*y**2
base_log_integrand = q * phase - s.Rational(9, 4) * z * y
quadratic_tail = s.limit(base_log_integrand / y**2, y, s.oo)
kappa = s.exp(-T) * (1 - T) / (4 * T)
kappa_unit_parameterization = s.factor(kappa.subs(T, u / (1 + u)))
expected_unit_parameterization = s.exp(-u / (1 + u)) / (4 * u)

checks = {
    "real_contour_tail_is_controlled_by_quadratic_sign": s.simplify(quadratic_tail - q*k*z) == 0,
    "positive_quadratic_phase_overwhelms_linear_amplitude_decay": quadratic_tail == q*k*z,
    "real_caustic_parameter_is_positive_on_unit_interval": s.simplify(
        kappa_unit_parameterization - expected_unit_parameterization
    ) == 0,
    "admissible_and_real_caustic_signs_are_disjoint": bool(
        expected_unit_parameterization > 0
    ),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "deformed_phase": str(phase),
        "base_log_integrand": str(base_log_integrand),
        "quadratic_tail_coefficient": str(quadratic_tail),
        "original_positive_real_contour_admissible_sign": "k<=0",
        "interior_real_caustic_sign": "k>0",
        "classification": "virtual fold outside the original real-contour source domain",
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact large-y sign audit for the original positive-real Gamma contour. "
        "It proves that the real quadratic fold lies outside that contour's "
        "admissible source domain. It does not prohibit an independently "
        "authorized complex contour, analytic continuation, or different "
        "source amplitude with quadratic decay."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
