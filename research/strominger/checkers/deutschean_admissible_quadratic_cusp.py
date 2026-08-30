#!/usr/bin/env python3
"""Classify the source-admissible negative quadratic family and its cusp."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_admissible_quadratic_cusp.json"
T, alpha, y, z = s.symbols("T alpha y z", positive=True)
phi = (1 + s.sqrt(5)) / 2
psi = s.exp(-T) * (T - 1) / (4 * T)
alpha_star = s.factor(psi.subs(T, phi))
z_map = T * s.exp(-T) + 2 * alpha * T**2
z1 = s.factor(s.diff(z_map, T))
z2 = s.factor(s.diff(z_map, T, 2))
z3_cusp = s.factor(s.diff(z_map, T, 3).subs({T: phi, alpha: alpha_star}))

phase = s.log(y) + (s.exp(-z*y) - 1) / z - alpha*z*y**2
zc = s.factor(phi * s.exp(-phi) * (1 + phi) / 2)
yc = s.factor(2 * s.exp(phi) / (1 + phi))
cusp_subs = {T: phi, alpha: alpha_star, z: zc, y: yc}
fy = s.diff(phase, y)
fyy = s.diff(phase, y, 2)
fyyy = s.diff(phase, y, 3)
fyyyy = s.factor(s.diff(phase, y, 4).subs(cusp_subs))
unfolding = s.Matrix([
    [s.diff(fy, z), s.diff(fy, alpha)],
    [s.diff(fyy, z), s.diff(fyy, alpha)],
]).subs(cusp_subs).applyfunc(s.factor)
unfolding_det = s.factor(unfolding.det())

checks = {
    "fold_profile_has_unique_golden_ratio_max": s.simplify(
        s.diff(psi, T) + s.exp(-T) * (T**2 - T - 1) / (4*T**2)
    ) == 0,
    "critical_damping_is_positive": bool(alpha_star > 0),
    "saddle_map_first_derivative_vanishes_at_cusp": s.simplify(z1.subs({T: phi, alpha: alpha_star})) == 0,
    "saddle_map_second_derivative_vanishes_at_cusp": s.simplify(z2.subs({T: phi, alpha: alpha_star})) == 0,
    "saddle_map_third_derivative_is_nonzero": s.simplify(z3_cusp) != 0,
    "phase_first_three_normal_derivatives_vanish": all(
        s.simplify(expr.subs(cusp_subs)) == 0 for expr in (fy, fyy, fyyy)
    ),
    "phase_fourth_normal_derivative_is_nonzero": s.simplify(fyyyy) != 0,
    "two_parameter_unfolding_has_full_rank": s.simplify(unfolding_det) != 0,
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "admissible_parameterization": "k=-alpha, alpha>0",
        "fold_profile": str(psi),
        "cusp_T": str(phi),
        "critical_alpha": str(alpha_star),
        "cusp_z": str(zc),
        "cusp_y": str(yc),
        "saddle_map_third_derivative": str(z3_cusp),
        "phase_fourth_derivative": str(fyyyy),
        "unfolding_matrix": [[str(value) for value in row] for row in unfolding.tolist()],
        "unfolding_determinant": str(unfolding_det),
        "local_type": "two-control quartic cusp",
        "uniform_model": "Pearcey type",
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact source-admissible cusp classification for the negative quadratic "
        "family. It proves the quartic normal type and full two-control unfolding. "
        "It does not yet derive the positive-real contour's Pearcey cycle, "
        "Stokes data, or connected readout continuation."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
