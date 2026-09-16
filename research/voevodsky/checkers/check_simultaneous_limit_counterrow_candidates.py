#!/usr/bin/env python3
"""Audit existing rank-two/index constructions against the pro-horn repair gate."""
import json
from pathlib import Path

requirements = [
    "source_derived_for_actual_tate_multiplier",
    "cancels_2L_over_pi_with_required_orientation",
    "uniform_on_bounded_source_packets",
    "physical_trace_ideal_realization",
    "mixed_crossing_cutoff_coherence",
    "dagger_and_successor_compatibility",
]

candidates = {
    "recentered_finite_blaschke_rotor": {
        "source_derived_for_actual_tate_multiplier": False,
        "cancels_2L_over_pi_with_required_orientation": False,
        "uniform_on_bounded_source_packets": True,
        "physical_trace_ideal_realization": True,
        "mixed_crossing_cutoff_coherence": True,
        "dagger_and_successor_compatibility": True,
        "note": "stationary rank-two projection of trace 2, conditional on inserting a hostile Blaschke factor; it is not the required linear counter-row",
    },
    "paley_wiener_crossing_clutching": {
        "source_derived_for_actual_tate_multiplier": False,
        "cancels_2L_over_pi_with_required_orientation": False,
        "uniform_on_bounded_source_packets": False,
        "physical_trace_ideal_realization": False,
        "mixed_crossing_cutoff_coherence": False,
        "dagger_and_successor_compatibility": True,
        "note": "exact at finite window, but its trace norm grows linearly with L",
    },
    "infinite_atomic_boundary_current": {
        "source_derived_for_actual_tate_multiplier": False,
        "cancels_2L_over_pi_with_required_orientation": False,
        "uniform_on_bounded_source_packets": True,
        "physical_trace_ideal_realization": False,
        "mixed_crossing_cutoff_coherence": False,
        "dagger_and_successor_compatibility": True,
        "note": "strong Schwartz-dual limit when crossings produce locally finite atoms; no physical trace-class realization",
    },
    "existing_endpoint_index_row": {
        "source_derived_for_actual_tate_multiplier": True,
        "cancels_2L_over_pi_with_required_orientation": False,
        "uniform_on_bounded_source_packets": True,
        "physical_trace_ideal_realization": True,
        "mixed_crossing_cutoff_coherence": False,
        "dagger_and_successor_compatibility": True,
        "note": "retains Tate endpoint normalization but has the wrong observer functional for the rotor growth",
    },
}

for item in candidates.values():
    item["passes"] = all(item[r] for r in requirements)
assert not any(item["passes"] for item in candidates.values())

out = {
    "schema": "marici.voevodsky.simultaneous-limit-counterrow-candidate-audit.v1",
    "requirements": requirements,
    "candidates": candidates,
    "passing_candidates": [],
    "passed": True,
    "conclusion": "No existing endpoint, rotor, clutching, or atomic-current construction supplies the source-derived counter-row required for simultaneous convergence.",
    "next_gate": "derive a crossing-specific rank-two row from the actual Tate scattering/endpoint data and prove its trace equals -2L/pi plus a uniformly convergent remainder",
}
path = Path(__file__).parents[1]/"results"/"simultaneous_limit_counterrow_candidates.json"
path.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
