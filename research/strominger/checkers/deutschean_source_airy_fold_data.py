#!/usr/bin/env python3
"""Derive the local Airy fold data from the deformed Gamma phase."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_source_airy_fold_data.json"
y, z, k, T, q = s.symbols("y z k T q", positive=True)
phase = s.log(y) + (s.exp(-z * y) - 1) / z + k * z * y**2
kappa = s.exp(-T) * (1 - T) / (4 * T)
zc = T * s.exp(-T) * (1 + T) / 2
yc = s.factor(T / zc)
subs_caustic = {y: yc, z: zc, k: kappa}
fy = s.diff(phase, y)
fyy = s.diff(phase, y, 2)
fyyy = s.factor(s.diff(phase, y, 3).subs(subs_caustic))
unfolding = s.factor(s.diff(fy, z).subs(subs_caustic))
expected_cubic = s.exp(-3*T) * (1 + T)**2 * (1 + T - T**2) / 4
airy_argument_factor = s.factor(unfolding * (2 / fyyy)**s.Rational(1, 3))

checks = {
    "source_saddle_derivative_vanishes_on_caustic": s.simplify(fy.subs(subs_caustic)) == 0,
    "source_hessian_vanishes_on_caustic": s.simplify(fyy.subs(subs_caustic)) == 0,
    "source_cubic_coefficient_has_exact_positive_form": s.simplify(fyyy - expected_cubic) == 0,
    "transverse_unfolding_coefficient_is_inverse_T": s.simplify(unfolding - 1 / T) == 0,
    "cubic_positive_on_unit_interval_witnesses": all(
        expected_cubic.subs(T, value) > 0
        for value in (s.Rational(1, 10), s.Rational(1, 2), s.Rational(9, 10))
    ),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "deformed_phase": str(phase),
        "critical_y": str(yc),
        "critical_z": str(zc),
        "critical_k": str(kappa),
        "cubic_phase_coefficient": str(fyyy),
        "transverse_unfolding_coefficient": str(unfolding),
        "airy_normal_scale": "u=(q*f'''_c/2)^(1/3)*(y-y_c)",
        "airy_argument": "xi=-q^(2/3)*(z-z_c)*B_c*(2/f'''_c)^(1/3)",
        "airy_argument_source_factor": str(airy_argument_factor),
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact local fold data from the original deformed Gamma phase. It "
        "derives Airy scaling and the q^(-2/3) transition width. It does not "
        "select the global Airy contour combination, Stokes multipliers, or "
        "continued connected readout normalization."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
