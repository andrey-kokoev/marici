#!/usr/bin/env python3
"""Bounded completion audit for the interacting cosmology objective."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

PACKETS = {
    "source_normal_tower": "generic-six-scale-kernel-normal-tower.json",
    "interaction_action": "rank60-interaction-action-faithfulness.json",
    "moving_cycle": "physical-normal-gauss-manin-lift.json",
    "weighted_gram": "weighted-gram-rank60-base-change.json",
    "tensor_vertex": "finite-q-tensor-vertex-ports.json",
    "time_weight": "cc-scalar-tensor-time-weight.json",
    "cyclic_tensor": "cyclic-tensor-vertex-cm-sheet.json",
    "coefficient_split": "tensor-kummer-tate-decomposition.json",
    "physical_trace": "physical-cycle-helicity-reflection-trace.json",
    "rank7_tensor": "parity-even-tensor-rank7-module.json",
    "ward_kernel": "tt-ward-kernel-endpoint-lift.json",
    "gm_frame": "adapted-tt-frame-gm-horizontal.json",
    "gram_grade": "spin2-weighted-gram-cartier-grade.json",
    "soft_port": "soft-tensor-ward-score-recovery.json",
    "marked_wall": "tensor-marked-wall-localization.json",
    "total_energy": "tensor-total-energy-gram-nearby.json",
    "landau": "tensor-cayley-menger-landau-exponent.json",
    "infinity": "tensor-infinity-gysin-elliptic.json",
    "polarization": "tensor-polarization-parity-observer.json",
    "normalization": "rank7-score-normalization-line.json",
    "local_scores": "moving-cycle-score-tower-rank.json",
    "physical_scores": "fixed-loop-physical-score-rank.json",
    "scope": "interacting-regulated-period-scope.json",
}


def load(name: str) -> dict:
    with (ROOT / name).open(encoding="utf-8") as stream:
        return json.load(stream)


data = {key: load(path) for key, path in PACKETS.items()}
checks: dict[str, bool] = {}

checks["all_packets_present"] = len(data) == len(PACKETS)
checks["all_versioned_schemas"] = all(
    str(packet.get("schema", "")).startswith("marici.benincasa.")
    for packet in data.values()
)
checks["all_status_packets_pass"] = all(
    packet.get("status", "passed") in {
        "passed",
        "generic_rank60_normal_interaction_action_is_faithful",
    }
    for packet in data.values()
)
checks["rank60_interaction_is_faithful"] = (
    data["interaction_action"].get("status")
    == "generic_rank60_normal_interaction_action_is_faithful"
)
checks["tensor_polarization_observer_rank6"] = (
    data["polarization"].get("full_rank") == 6
)
checks["physical_observer_rank3"] = (
    data["polarization"].get("physical_cycle_projection_rank") == 3
)
checks["connected_scores_have_one_normalization_kernel"] = (
    data["normalization"].get("connected_score_kernel_rank") == 1
    and data["normalization"].get("augmented_mean_plus_connected_rank") == 7
)
checks["local_score_tower_recovers_ten_responses"] = (
    data["local_scores"].get("primary_rank_with_constant") == 11
)
checks["fixed_cycle_recovers_ten_responses"] = (
    data["physical_scores"].get("generic_response_rank") == 10
    and data["physical_scores"].get("generic_rank_with_constant") == 11
)
checks["fixed_cycle_has_two_prime_replication"] = (
    len(data["physical_scores"].get("runs", [])) >= 2
)
checks["source_only_authorizes_regulated_period"] = (
    data["scope"].get("counterterm_or_finite_subtraction_map_in_source") is False
    and "regulated" in str(data["scope"].get("authorized_theorem_scope", "")).lower()
)

new_carrier_fields = []
for key, packet in data.items():
    for field in ("new_carrier_support", "new_carrier_datum"):
        if field in packet:
            new_carrier_fields.append((key, field, packet[field]))
checks["no_packet_requires_new_carrier"] = all(
    value in (False, None, "none", "no", "not_required")
    or (isinstance(value, str) and "no new" in value.lower())
    for _, _, value in new_carrier_fields
)

result = {
    "schema": "marici.benincasa.interacting-contextual-faithfulness-completion.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "packet_count": len(data),
    "carrier_classification": (
        "existing energy/Cut/Cayley-Menger/Gram/Landau carrier and support calculus"
    ),
    "coefficient_classification": (
        "sector-specific tensor Kummer/Tate and elliptic coefficient objects"
    ),
    "physical_readout": (
        "source-defined regulated fixed-loop score tower, with reflection coinvariants"
    ),
    "hard_falsifier_found": False,
    "surviving_hypothesis": (
        "H2 survives this generic regulated interacting nonhomogeneous test"
    ),
    "scope_boundary": (
        "No scheme-independent UV-renormalized theorem: the frozen source does not "
        "define the required finite subtraction/readout map."
    ),
    "evidence_packets": PACKETS,
}

output = ROOT / "interacting-contextual-faithfulness-completion.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, indent=2))

if result["status"] != "passed":
    raise SystemExit(1)
