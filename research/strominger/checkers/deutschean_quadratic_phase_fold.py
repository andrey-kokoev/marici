#!/usr/bin/env python3
"""Classify the quadratic phase caustic as a simple fold."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_quadratic_phase_fold.json"
T, k, tau = s.symbols("T k tau", positive=True)
z = T * s.exp(-T) - 2 * k * T**2
kappa = s.exp(-T) * (1 - T) / (4 * T)
z2_caustic = s.factor(s.diff(z, T, 2).subs(k, kappa))
expected_z2 = s.exp(-T) * (T**2 - T - 1) / T
positive_root = (1 + s.sqrt(5)) / 2
negative_root = (1 - s.sqrt(5)) / 2

checks = {
    "second_derivative_has_exact_fold_form": s.simplify(z2_caustic - expected_z2) == 0,
    "positive_zero_of_fold_factor_lies_beyond_unit_interval": positive_root > 1,
    "negative_zero_of_fold_factor_lies_below_unit_interval": negative_root < 0,
    "fold_factor_is_negative_at_interval_witness": (s.Rational(1, 4) - s.Rational(1, 2) - 1) < 0,
    "quadratic_normal_coefficient_is_nonzero": s.simplify(z2_caustic / 2) != 0,
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "caustic_parameter": str(kappa),
        "second_derivative_on_caustic": str(z2_caustic),
        "fold_factor_roots": [str(negative_root), str(positive_root)],
        "local_normal_form": "z-z_c = (z''_c/2)(T-T_c)^2 + O((T-T_c)^3)",
        "branching_type": "square_root_two_sheeted",
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact classification of the real quadratic caustic as a simple fold. "
        "It proves two-sheeted square-root saddle branching. It does not itself "
        "construct an authorized Airy contour, prove continuation of the full "
        "Gamma integral, or identify readout values across the fold."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
