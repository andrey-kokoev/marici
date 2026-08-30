#!/usr/bin/env python3
"""Compile tangent faithfulness into formal-arc faithfulness."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
TANGENT_RESULT = ROOT / "research/strominger/results/deutschean_h1_h2_mixed_faithfulness.json"
RESULT = ROOT / "research/strominger/results/deutschean_formal_arc_faithfulness.json"

tangent = json.loads(TANGENT_RESULT.read_text(encoding="utf-8"))
m, epsilon = s.symbols("m epsilon")
tail_multiplier = s.factor(m * (m - 1) * (m - 2) * (m + 8) / 2)
tail_roots = s.solve(tail_multiplier, m)

# Hostile necessity test: a non-injective differential permits distinct arcs
# with identical readout.
left_arc = epsilon
right_arc = -epsilon
hostile_left = s.expand(left_arc**2)
hostile_right = s.expand(right_arc**2)

checks = {
    "tangent_certificate_passes": tangent["passed"] is True,
    "initial_differential_is_injective": (
        tangent["observed"]["rank"] == 7
        and tangent["observed"]["nullity"] == 0
        and tangent["observed"]["determinant"] != "0"
    ),
    "tail_multiplier_has_no_admissible_root": all(root < 7 for root in tail_roots),
    "hostile_zero_differential_allows_arc_collision": (
        hostile_left == hostile_right
        and left_arc != right_arc
        and s.diff(epsilon**2, epsilon).subs(epsilon, 0) == 0
    ),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "tangent_result_sha256": hashlib.sha256(TANGENT_RESULT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "initial_determinant": tangent["observed"]["determinant"],
        "tail_multiplier": str(tail_multiplier),
        "tail_multiplier_roots": [str(root) for root in tail_roots],
        "hostile_map": "x -> x^2",
        "hostile_arcs": ["epsilon", "-epsilon"],
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Compiler certificate for the formal first-difference argument. It proves "
        "faithfulness on source arcs in the separated epsilon-adic completion. "
        "It does not cover smooth flat differences, convergence, distant finite "
        "sources, or global analytic monodromy."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
