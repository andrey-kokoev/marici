from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/bounded-categorical-completeness-contract-v1.json")
RESULTS = {
    "markov": Path("research/voevodsky/results/five_sort_markov_analytic_section.json"),
    "pentagon": Path("research/voevodsky/results/markov_amalgamation_pentagon_horn.json"),
    "tower": Path("research/voevodsky/results/typed_horn_obstruction_tower_status.json"),
    "filler": Path("research/voevodsky/results/filler_fiber_selection_layer.json"),
    "edge": Path("research/voevodsky/results/sector_overlap_edge_contract.json"),
    "rh": Path("research/voevodsky/results/rh_modular_filling_constructor_contract.json"),
}


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    results = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in RESULTS.items()}
    assert all(result["passed"] is True for result in results.values())
    assert len(contract["completeness_is_parameterized_by"]) == 8
    assert set(contract["required_gates"]) == {"presentation", "realization", "horn_coverage", "filler_semantics", "completion", "cross_sector", "physical"}

    markov = results["markov"]
    assert (markov["object_sort_count"], markov["cell_class_count"], markov["law_class_count"]) == (5, 6, 5)
    assert results["pentagon"]["simplicial_degree"] == 4
    assert results["tower"]["markov_internal_highest_filled_dimension"] == 4
    assert results["tower"]["markov_scope_limited_to_declared_laws"] is True
    assert results["filler"]["relative_class_and_selection_separated"] is True

    assert results["edge"]["admitted_edges"] == 0
    assert results["tower"]["cross_sector_first_obstruction_dimension"] == 1
    assert results["tower"]["cross_sector_higher_obstructions_defined"] is False
    assert results["rh"]["cutoff_nonclosability_fixture_executable"] is False

    certificates = contract["current_certificates"]
    assert certificates["markov_declared_truncation"]["status"] == "complete_for_declared_presentation_laws"
    assert certificates["cross_sector"]["status"] == "incomplete_at_dimension_1"
    assert certificates["global_unbounded"]["status"] == "not_claimed"

    output = {
        "schema": "marici.voevodsky.bounded-categorical-completeness-check.v1",
        "status": "parameterized_completeness_boundary_verified",
        "completeness_parameters": 8,
        "gate_families": 7,
        "markov_degree_4_declared_law_completeness": True,
        "markov_physical_completeness": False,
        "cross_sector_dimension_1_completeness": False,
        "RH_completed_filler_completeness": False,
        "global_unbounded_completeness_claimed": False,
        "unsupported_promotions_detected": 0,
        "passed": True,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
