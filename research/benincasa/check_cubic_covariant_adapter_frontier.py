#!/usr/bin/env python3
"""Locate the unresolved cell in the cubic source-to-period adapter."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).parent

def load(name: str) -> dict:
    return json.loads((HERE / name).read_text(encoding="utf-8"))

coefficient = load("rank7-contact-normal-score-recovery.json")
lift = load("physical-normal-gauss-manin-lift.json")
cech = load("physical-normal-lift-cech-coherence.json")
endpoint = load("physical-cycle-endpoint-normal-lifts.json")
moving = load("moving-cycle-score-tower-rank.json")
descent = load("integrated-period-source-relation-descent.json")

checks = {
    "coefficient_adapter_exact": coefficient["moment_cumulant_recovery_exact"],
    "coefficient_adapter_invertible": coefficient["source_measure_response_jacobian_determinant"] == "1/128",
    "three_first_order_lifts_exist": len(lift["normal_lifts"]) == 3,
    "first_order_K_poles_cancel": all(x["explicit_K_denominator_cancels"] for x in lift["normal_lifts"]),
    "first_order_lifts_glue_mod_exact": cech["pairwise_tangency_checks"] == 9 and cech["triple_cocycle_checks"] == 3,
    "endpoint_incidence_is_preserved": endpoint["incidence_tangency_checks"] == 9,
    "global_period_covector_was_uncomputed": moving["global_period_covector_rank"] == "uncomputed",
    "naive_integrated_descent_failed": descent["status"] == "naive_descent_rejected",
}

packet = {
    "schema": "marici.benincasa.cubic-covariant-adapter-frontier.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "completed_cells": [
        "exact coefficient moment-cumulant/Faa-di-Bruno adapter through degree three",
        "three first-order K-tangent Gauss-Manin lifts",
        "marked-wall contact corrections",
        "pairwise Cech gluing modulo exact meromorphic forms",
        "loop-distance endpoint incidence compatibility"
    ],
    "unique_missing_cell": (
        "ordered degree-two and degree-three covariant compositions, including derivatives "
        "and commutators of the lifts, reduced in the global de-Rham-Cech complex before period pushforward"
    ),
    "prohibited_shortcut": (
        "No coefficient renormalization or direct selection of seven Taylor columns may replace "
        "the missing higher transport cell."
    ),
    "new_carrier_support": False,
}

out = HERE / "cubic-covariant-adapter-frontier.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
