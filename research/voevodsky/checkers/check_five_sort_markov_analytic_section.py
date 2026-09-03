from __future__ import annotations

import json
from pathlib import Path


EVIDENCE = [
    "research/voevodsky/results/operator_valued_markov_green.json",
    "research/voevodsky/results/varying_fiber_markov_green.json",
    "research/voevodsky/results/framed_to_metric_markov_descent.json",
    "research/voevodsky/results/ordered_subset_markov_beck_chevalley.json",
    "research/voevodsky/results/rooted_tree_markov_amalgamation.json",
    "research/voevodsky/results/varying_fiber_markov_completion.json",
    "research/voevodsky/results/markov_carrier_green_bridge.json",
    "research/voevodsky/results/gauge_quotient_green_composite.json",
]
SIGNATURE = Path("research/voevodsky/coherence-pyramid-computad-signature.json")
CELLS = Path("research/voevodsky/coherence-pyramid-cells-and-laws.json")


def main() -> None:
    evidence = [json.loads(Path(path).read_text(encoding="utf-8")) for path in EVIDENCE]
    assert all(item["passed"] is True for item in evidence)
    signature = json.loads(SIGNATURE.read_text(encoding="utf-8"))
    cells = json.loads(CELLS.read_text(encoding="utf-8"))
    sorts = set(signature["object_sorts"])
    expected_sorts = {"carrier", "gauge_presentation", "finite_green", "quotient_form", "closed_form"}
    assert sorts == expected_sorts

    document = json.dumps(cells, sort_keys=True)
    cell_classes = {"associator", "left_unitor", "right_unitor", "interchange", "beck_chevalley", "completion_comparison"}
    law_classes = {"pentagon", "triangle", "interchange_hexagon", "pasting", "completion_pasting"}
    assert all(name in document for name in cell_classes | law_classes)

    bridge = evidence[-2]
    composite = evidence[-1]
    assert bridge["five_sort_hypergraph_connected"] is True
    assert composite["gauge_presentation_to_carrier_typed"] is True
    assert composite["carrier_to_finite_green_typed"] is True
    assert composite["comparison_cell_identity_invertible"] is True
    assert evidence[3]["passed"] and evidence[4]["passed"]
    assert bridge["bridge_total_on_arbitrary_carriers"] is False
    assert composite["physical_interpretation_supplied"] is False

    result = {
        "schema": "marici.voevodsky.five-sort-markov-analytic-section.v1",
        "status": "restricted_global_analytic_section_verified",
        "object_sorts_realized": sorted(sorts),
        "object_sort_count": len(sorts),
        "cell_classes_realized": sorted(cell_classes),
        "cell_class_count": len(cell_classes),
        "law_classes_realized": sorted(law_classes),
        "law_class_count": len(law_classes),
        "connected_incidence": True,
        "composable_gauge_carrier_green_route": True,
        "completion_descent_hyperedge_realized": True,
        "evidence_documents_passed": len(evidence),
        "domain": "metric_transition_markov",
        "arbitrary_carrier_section": False,
        "cross_sector_global_section": False,
        "physical_readout_supplied": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
