#!/usr/bin/env python3
"""Derive the real Pearcey cycle selected by the admissible Gamma contour."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_real_pearcey_cycle.json"
y, z, alpha, q = s.symbols("y z alpha q", positive=True)
u, X, Y = s.symbols("u X Y", real=True)
T = s.symbols("T", positive=True)
phi = (1 + s.sqrt(5)) / 2
alpha_star = s.exp(-phi) / (4 * phi**2)
zc = s.factor(phi * s.exp(-phi) * (1 + phi) / 2)
yc = s.factor(2 * s.exp(phi) / (1 + phi))
phase = s.log(y) + (s.exp(-z*y) - 1) / z - alpha*z*y**2
subs_cusp = {y: yc, z: zc, alpha: alpha_star}
f4 = s.factor(s.diff(phase, y, 4).subs(subs_cusp))
C = s.factor(-f4)
fy = s.diff(phase, y)
fyy = s.diff(phase, y, 2)
linear_control = s.Matrix([
    s.factor(s.diff(fy, z).subs(subs_cusp)),
    s.factor(s.diff(fy, alpha).subs(subs_cusp)),
])
quadratic_control = s.Matrix([
    s.factor(s.diff(fyy, z).subs(subs_cusp)),
    s.factor(s.diff(fyy, alpha).subs(subs_cusp)),
])
pearcey_exponent = -u**4 / 4 + X*u**2 / 2 + Y*u
amplitude = s.exp(-s.Rational(9, 4)*z*y) * (1 + 3*z*s.exp(z*y)/(2*q))
amplitude_cusp = s.factor(amplitude.subs(subs_cusp))

checks = {
    "original_phase_decays_at_zero_endpoint": s.limit(phase, y, 0, dir="+") == -s.oo,
    "original_phase_decays_at_infinite_endpoint": s.limit(phase, y, s.oo) == -s.oo,
    "quartic_normal_coefficient_is_negative": bool(C > 0),
    "real_pearcey_cycle_decays_at_both_ends": (
        s.limit(pearcey_exponent, u, s.oo) == -s.oo
        and s.limit(pearcey_exponent, u, -s.oo) == -s.oo
    ),
    "source_amplitude_is_positive_at_cusp": bool(amplitude_cusp > 0),
    "control_covectors_are_independent": s.simplify(s.det(s.Matrix.hstack(
        linear_control, quadratic_control
    ))) != 0,
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "cusp_T": str(phi),
        "positive_quartic_scale_C": str(C),
        "linear_control_covector": [str(value) for value in linear_control],
        "quadratic_control_covector": [str(value) for value in quadratic_control],
        "normal_coordinate": "u=(q*C/6)^(1/4)*(y-y_c)",
        "pearcey_cycle": "u in (-infinity,infinity)",
        "pearcey_exponent": str(pearcey_exponent),
        "scaled_quadratic_control": "X=q^(1/2)*(6/C)^(1/2)*delta(f_yy)",
        "scaled_linear_control": "Y=q^(3/4)*(6/C)^(1/4)*delta(f_y)",
        "leading_jacobian": "(6/(q*C))^(1/4)",
        "cusp_amplitude": str(amplitude_cusp),
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact source selection of the local real Pearcey cycle at the "
        "admissible cusp. It fixes the leading contour, scales, and amplitude. "
        "It does not yet compute higher uniform corrections or transport the "
        "connected H1/H2 definitions through the cusp."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
