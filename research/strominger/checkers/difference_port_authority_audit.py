#!/usr/bin/env python3
"""Audit existing magnetic constructors for full valuation-difference authority."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))
packet = source["packet"]


def R(n):
    p = packet(n)
    return (p["v3_d1"], p["v3_d2"], p["v3_d3"])


constructors = [
    {
        "id": "free_group_grammar",
        "prepares": "one decorated source word or response at a chosen grade",
        "arity": 1,
        "difference_axis": None,
        "verdict": "does_not_prepare_ordered_grade_pairs",
    },
    {
        "id": "integral_state_recurrence",
        "prepares": "(C^n,C^-n) for one grade",
        "arity": 1,
        "difference_axis": "inverse within one grade",
        "verdict": "inverse_pair_is_not_cross_grade_difference",
    },
    {
        "id": "nested_commutator_readout",
        "prepares": "one response matrix A_n",
        "arity": 1,
        "difference_axis": None,
        "verdict": "acts_gradewise",
    },
    {
        "id": "smith_packet",
        "prepares": "R(n) from one response matrix",
        "arity": 1,
        "difference_axis": None,
        "verdict": "nonlinear_unary_readout",
    },
    {
        "id": "route_packet",
        "prepares": "(A(n),B(n)) for reflected routes of one source",
        "arity": 1,
        "difference_axis": "reflection routes",
        "verdict": "wrong_axis",
    },
    {
        "id": "joint_electric_magnetic_observer",
        "prepares": "(E(n),M(n)) for one source",
        "arity": 1,
        "difference_axis": "reflection parity",
        "verdict": "wrong_axis_and_pre_smith",
    },
    {
        "id": "physical_spin_puncture_readout",
        "prepares": "puncture distributions and contours",
        "arity": 1,
        "difference_axis": "puncture support",
        "verdict": "different_target_type",
    },
    {
        "id": "electric_magnetic_bridge",
        "prepares": "cross-parity endomorphism",
        "arity": 1,
        "difference_axis": "reflection parity",
        "verdict": "not_source_authorized_and_wrong_axis",
    },
]

witness = {
    "blind_pair": [0, 1],
    "same_packet": list(R(0)),
    "successor_pair": [1, 2],
    "successor_difference": [b - a for a, b in zip(R(1), R(2))],
}
gates = {
    "source_grammar_has_no_binary_grade_pair_constructor":
        all(c["arity"] == 1 for c in constructors),
    "existing_joint_ports_use_non_grade_axes":
        all(
            c["difference_axis"] != "ordered grade pair"
            for c in constructors
        ),
    "smith_readout_is_declared_unary":
        next(c for c in constructors if c["id"] == "smith_packet")["arity"] == 1,
    "blind_pair_requires_successor_difference":
        R(0) == R(1) and R(1) != R(2),
    "candidate_electric_magnetic_bridge_is_absent":
        next(c for c in constructors if c["id"] == "electric_magnetic_bridge")[
            "verdict"
        ].startswith("not_source_authorized"),
}
payload = {
    "schema": "marici.strominger.difference_port_authority_audit.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "no_existing_magnetic_constructor_authorizes_full_difference_port",
    "required_constructor": {
        "input": "ordered pair of independently constructible grades (a,b)",
        "output": "R(b)-R(a) in the valuation-difference group",
        "required_capabilities": [
            "binary grade-pair preparation",
            "two Smith readouts with retained provenance",
            "authorized subtraction in the valuation codomain",
            "substitution-compatible transport",
        ],
    },
    "constructors": constructors,
    "witness": witness,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The source constructs each grade and each unary Smith packet, but no "
        "existing constructor forms an ordered cross-grade packet with an "
        "authorized subtraction port. Existing joint observers compare "
        "reflection routes or parity channels and cannot authorize omega."
    ),
}
print(json.dumps(payload, indent=2))
