#!/usr/bin/env python3
"""Completion audit for the compatible action-level one-loop cubic sector."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(name: str) -> dict:
    with (ROOT / name).open(encoding="utf-8") as stream:
        return json.load(stream)


inventory = load("time-dependent-phi3-counterterm-inventory.json")
counterterms = load("action-level-counterterm-block-typing.json")
dressing = load("external-leg-dressing-jet-invertibility.json")
graph_local = load("source-authorized-renormalization-completion.json")
physical = load("fixed-loop-physical-score-rank.json")

checks = {
    "compatible_parent_inventory_passes": inventory.get("status") == "passed",
    "triangle_has_no_vertex_counterterm": (
        inventory.get("checks", {}).get("no_one_loop_vertex_counterterm_from_triangle")
        is True
    ),
    "no_field_strength_counterterm": (
        inventory.get("checks", {}).get(
            "no_one_loop_wavefunction_counterterm_from_two_point_power_counting"
        )
        is True
    ),
    "normalized_lower_point_reduction_has_rank7": (
        counterterms.get("status") == "passed"
        and counterterms.get("renormalized_graph_rank") == 7
    ),
    "lower_point_reduction_is_cyclic": (
        counterterms.get("checks", {}).get("cyclic_equivariance") is True
    ),
    "external_leg_dressing_projection_is_invertible": (
        dressing.get("status") == "passed"
        and dressing.get("complete_tower_determinant_at_F0_1") == "1"
        and dressing.get("response_tower_determinant_at_F0_1") == "1"
    ),
    "graph_local_finite_map_has_rank7": (
        graph_local.get("status") == "passed"
        and graph_local.get("renormalized_readout_rank") == 7
    ),
    "physical_observer_kernel_remains_zero": (
        physical.get("regulated_physical_score_kernel_on_source_quotient") == 0
    ),
    "no_new_carrier_support": all(
        packet.get("new_carrier_support") is False
        for packet in (inventory, counterterms, dressing, graph_local)
    ),
}

packet = {
    "schema": "marici.benincasa.action-level-rank7-completion.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "parent_action": "time-dependent cubic scalar sector of arXiv:1709.02813 Eq. (1)",
    "renormalization_conditions": [
        "zero renormalized one-point function",
        "preserve the declared massless/conformally-coupled free state",
    ],
    "counterterm_reduction": "[I7|0_B1|0_M3]",
    "external_leg_dressing": (
        "analytic coefficient multiplication with invertible projection for F(0)!=0"
    ),
    "finite_readout_rank": 7,
    "contextual_faithfulness": "preserved",
    "coefficient_enlargement": (
        "external-leg dynamics may generate additional pure cubic and higher normal "
        "jets, but the original R7 is recovered by the predeclared projection"
    ),
    "carrier_classification": "unchanged",
    "hard_failure_support": "F(0)=0, excluded in perturbation theory around F(0)=1",
    "scope": (
        "one-loop three-point sector of the compatible time-dependent cubic scalar "
        "parent action, with the declared background and free-state normalization"
    ),
    "new_carrier_support": False,
    "evidence": [
        "time-dependent-phi3-counterterm-inventory.json",
        "action-level-counterterm-block-typing.json",
        "external-leg-dressing-jet-invertibility.json",
        "source-authorized-renormalization-completion.json",
        "fixed-loop-physical-score-rank.json",
    ],
}

output = ROOT / "action-level-rank7-completion.json"
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
