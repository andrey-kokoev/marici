"""Exact WP139 boundary/instrument candidate-class closeout."""

import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
precursors = [
    "wp134_dimensional_transmutation_authority.json",
    "wp135_uv_fixed_point_scale_authority.json",
    "wp136_stochastic_cosmological_boundary.json",
    "wp137_reheating_detector_reliability.json",
    "wp138_compact_source_uniform_faithfulness.json",
]
precursor_pass = {}
for name in precursors:
    data = json.loads((root / "results" / name).read_text(encoding="utf-8"))
    precursor_pass[name] = data["all_pass"]

gates = [
    "independent_boundary_source",
    "scale_or_distribution_derived",
    "full_descent",
    "mediator_pushforward",
    "uniform_accessibility",
    "open_rival_contextual_faithfulness",
    "executable_physical_instrument",
]

candidates = {
    "dimensional_transmutation": [False, False, True, True, False, False, False],
    "uv_fixed_point_with_physical_clock": [False, False, True, True, False, False, False],
    "gaussian_cosmological_preparation": [True, True, True, True, False, False, False],
    "compact_cosmological_preparation": [True, False, True, True, False, False, False],
}

pass_counts = {name: sum(row) for name, row in candidates.items()}
admitted = [name for name, row in candidates.items() if all(row)]

checks = {
    "all_precursor_checkers_pass": all(precursor_pass.values()),
    "seven_frozen_gates": len(gates) == 7,
    "four_frozen_candidates": len(candidates) == 4,
    "no_candidate_passes_all_gates": admitted == [],
    "rg_route_has_descent_not_boundary_authority": candidates["dimensional_transmutation"][2] and not candidates["dimensional_transmutation"][0],
    "fixed_point_leaves_amplitude_gate": not candidates["uv_fixed_point_with_physical_clock"][1],
    "gaussian_route_derives_distribution": candidates["gaussian_cosmological_preparation"][1],
    "gaussian_route_not_uniformly_accessible": not candidates["gaussian_cosmological_preparation"][4],
    "compact_route_has_normalized_source_shape": candidates["compact_cosmological_preparation"][0],
    "compact_support_scale_not_derived": not candidates["compact_cosmological_preparation"][1],
    "no_open_rival_faithfulness": not any(row[5] for row in candidates.values()),
    "no_executable_instrument": not any(row[6] for row in candidates.values()),
}

result = {
    "work_package": "WP139",
    "classification": "no admitted boundary-to-instrument chain in the frozen candidate class",
    "scope": "four predeclared boundary candidates; not a universal no-go over all future source theories",
    "gates": gates,
    "candidate_matrix": {name: dict(zip(gates, row)) for name, row in candidates.items()},
    "pass_counts": pass_counts,
    "admitted_candidates": admitted,
    "smallest_surviving_obstructions": {
        "dimensional_transmutation": "RG boundary packet unsourced",
        "uv_fixed_point_with_physical_clock": "relevant amplitude unsourced",
        "gaussian_cosmological_preparation": "unbounded support defeats uniform finite reach",
        "compact_cosmological_preparation": "compact support scale unsourced",
        "all_candidates": "no executable open-rival multi-point instrument",
    },
    "reopening_condition": "predeclared source fixes trajectory/support scale relative to a clock and an executable detector is faithful on an enlarged non-gauge rival class",
    "physical_instrument_established": False,
    "precursor_pass": precursor_pass,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = root / "results" / "wp139_boundary_instrument_candidate_closeout.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
