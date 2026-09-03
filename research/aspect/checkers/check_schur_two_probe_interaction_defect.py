#!/usr/bin/env python3
"""Exact rational witness for the Schur two-probe cross-effect."""

import json
from fractions import Fraction as Q
from pathlib import Path

A, B, C, E = Q(2), Q(3), Q(4), Q(5)
Ap, Bp, Cp, Ep = Q(1, 2), Q(0), Q(2), Q(0)

empty = E
unary_b = E
unary_c = E
joint = E - C / A * B
cross_effect = joint - unary_b - unary_c + empty
expected_residue = -C / A * B

joint_prime = Ep - Cp / A * B + C / A * Ap / A * B - C / A * Bp
local_shadow_prime = Ep

zero_b_cross_effect = -(C / A) * Q(0)
zero_c_cross_effect = -(Q(0) / A) * B

checks = {
    "unary_entry_probe_is_locally_silent": unary_b == E,
    "unary_exit_probe_is_locally_silent": unary_c == E,
    "joint_response_is_schur_complement": joint == Q(-1),
    "binary_cross_effect_equals_closed_continuation_residue": cross_effect == expected_residue == Q(-6),
    "erasing_entry_wire_kills_interaction": zero_b_cross_effect == 0,
    "erasing_exit_wire_kills_interaction": zero_c_cross_effect == 0,
    "local_first_jet_shadow_is_zero": local_shadow_prime == 0,
    "joint_first_jet_remains_nonzero": joint_prime == Q(-3, 2),
    "noninvertible_retained_response_is_undefined_not_zero": True,
}
assert all(checks.values()), checks

try:
    _ = C / Q(0) * B
    noninvertible_fixture = "incorrectly_defined"
except ZeroDivisionError:
    noninvertible_fixture = "rejected_as_undefined"
assert noninvertible_fixture == "rejected_as_undefined"

result = {
    "schema": "marici.aspect.schur-two-probe-interaction-defect.v1",
    "status": "passed",
    "arithmetic": "exact_rational",
    "checks": checks,
    "responses": {
        "empty": str(empty),
        "entry_only": str(unary_b),
        "exit_only": str(unary_c),
        "joint": str(joint),
        "cross_effect": str(cross_effect),
    },
    "first_jet": {
        "local_shadow": str(local_shadow_prime),
        "joint": str(joint_prime),
    },
    "deliberate_failure": {
        "fixture": "A=0",
        "disposition": noninvertible_fixture,
        "forbidden_repair": "assign_zero_interaction",
    },
    "claim_boundary": "Exact scalar Schur witness; no SCC-wide or physical realization theorem.",
}

output = Path(__file__).parents[1] / "results" / "schur_two_probe_interaction_defect.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
