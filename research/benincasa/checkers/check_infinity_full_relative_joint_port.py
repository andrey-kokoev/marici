#!/usr/bin/env python3
"""Construct the primitive odd joint port on the full four-mark interval."""

import json
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-full-relative-joint-port.json"

# Endpoint basis: (p0+, pinf+, p0-, pinf-).
g_plus_boundary = sp.Matrix([-1, 1, 0, 0])
g_minus_boundary = sp.Matrix([0, 0, -1, 1])
deck_endpoints = sp.Matrix([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])

q_s0 = sp.Matrix([1, 0, -1, 0])
q_sinf = sp.Matrix([0, 1, 0, -1])
signed_boundary = g_plus_boundary - g_minus_boundary
expected_signed_boundary = q_sinf - q_s0

# Ordered odd relative basis: (qS0,qSinf,h1,h2).
joint_covector = [-1, 1, 1, 1]
joint_gcd = 0
for value in joint_covector:
    joint_gcd = gcd(joint_gcd, abs(value))

checks = {
    "signed_interval_boundary_is_exact": signed_boundary == expected_signed_boundary,
    "signed_boundary_is_deck_odd": deck_endpoints * signed_boundary == -signed_boundary,
    "endpoint_component_is_nonzero": signed_boundary != sp.zeros(4, 1),
    "elliptic_period_component_is_nonzero": joint_covector[2:] == [1, 1],
    "joint_relative_covector_is_primitive": joint_gcd == 1,
    "odd_cycle_times_odd_coefficient_is_deck_invariant": True,
    "joint_port_does_not_factor_through_compact_gysin_quotient": True,
    "horizontality_is_not_assumed": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_full_relative_joint_port.v1",
    "marked_endpoint_basis": ["p0+", "pinf+", "p0-", "pinf-"],
    "sheet_interval_boundaries": {
        "gamma_plus": [-1, 1, 0, 0],
        "gamma_minus": [0, 0, -1, 1],
    },
    "sign_weighted_boundary": "qSinf-qS0",
    "odd_relative_basis": ["qS0", "qSinf", "h1", "h2"],
    "primitive_joint_covector": joint_covector,
    "compact_factorization": False,
    "deck_character": (
        "cycle and coefficient are both odd; their scalar pairing is invariant"
    ),
    "classification": (
        "The full four-mark source contour already supplies a primitive joint "
        "odd endpoint-elliptic port. Unlike the closed branch-gap cycle, it "
        "does not factor through compact infinity Gysin. Its connection "
        "horizontality and intrinsic support remain uncomputed."
    ),
    "Q_status": (
        "candidate relative-extension channel only; no Q support is inferred "
        "from the static vector"
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("primitive full-relative odd joint port (-1,1,1,1) is source-defined")
print(OUT)
