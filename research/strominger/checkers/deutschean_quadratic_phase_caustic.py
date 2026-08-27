#!/usr/bin/env python3
"""Locate the first global saddle-chart obstruction in a quadratic phase family."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_quadratic_phase_caustic.json"
T, k = s.symbols("T k", positive=True)
z = T * s.exp(-T) - 2 * k * T**2
zprime = s.factor(s.diff(z, T))
kappa = s.exp(-T) * (1 - T) / (4 * T)
z_on_caustic = s.factor(z.subs(k, kappa))
log_derivative = s.simplify(s.diff(s.log(kappa), T))

checks = {
    "caustic_parameter_solves_zprime_zero": s.simplify(zprime.subs(k, kappa)) == 0,
    "caustic_source_coordinate_remains_nonzero": s.simplify(
        z_on_caustic - T * s.exp(-T) * (1 + T) / 2
    ) == 0,
    "caustic_parameter_decreases_on_unit_interval": s.simplify(
        log_derivative - (-1 - 1 / (1 - T) - 1 / T)
    ) == 0,
    "caustic_parameter_runs_from_infinity_to_zero": (
        s.limit(kappa, T, 0, dir="+") == s.oo
        and s.limit(kappa, T, 1, dir="-") == 0
    ),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "phase_family": "g(T)=T^2",
        "saddle_map": str(z),
        "saddle_derivative": str(zprime),
        "caustic_parameter": str(kappa),
        "logarithmic_derivative": str(log_derivative),
        "source_coordinate_on_caustic": str(z_on_caustic),
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact real-interval theorem for the positive quadratic phase family. "
        "Every k>0 creates one saddle-coordinate caustic in 0<T<1. This is a "
        "chart obstruction, not a pair of distinct sources with equal readout; "
        "complex caustics and other deformation signs are not classified."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
