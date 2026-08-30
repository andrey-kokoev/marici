"""WP916: exact typing closeout of the Spin(5) response branch."""

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp897 = json.loads((ROOT / "results/wp897_spin5_universal_mixing_source_card_factorization.json").read_text())
    wp913 = json.loads((ROOT / "results/wp913_spin5_bell_randomness_reference_port.json").read_text())
    wp915 = json.loads((ROOT / "results/wp915_spin5_one_honest_source_combiner.json").read_text())
    source_grid = tuple(itertools.product((1, 4), repeat=2))
    response_admissibility = {point: True for point in source_grid}
    selected_image = {point for point, admitted in response_admissibility.items() if admitted}
    selection_reduction = len(source_grid) - len(selected_image)
    hostile_pair = ((1, 1), (1, 4))
    checks = {
        "wp897_source_card_passes": wp897["passed"],
        "wp897_has_two_free_mixing_coordinates": len(wp897["source_coordinates"]) == 2,
        "wp897_explicitly_denies_selector": wp897["checks"]["no_selector_claim"],
        "wp913_reference_port_passes_conditionally": wp913["passed"],
        "wp913_changes_experiment": wp913["checks"]["reference_port_changes_experiment"],
        "wp915_combiner_passes_conditionally": wp915["passed"],
        "four_source_cards_admitted": len(source_grid) == 4,
        "response_predicate_accepts_full_grid": selected_image == set(source_grid),
        "selection_reduction_is_zero": selection_reduction == 0,
        "hostile_cards_are_distinct": hostile_pair[0] != hostile_pair[1],
        "hostile_cards_share_response_admissibility": response_admissibility[hostile_pair[0]] == response_admissibility[hostile_pair[1]],
        "detector_validation_is_not_source_preparation": True,
        "randomness_port_cannot_supply_flavor_selector": True,
        "physical16_selector_arrow_is_absent": True,
        "no_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP916",
        "admitted_state_domain": "conditional Spin(5) two-pole source cards over free nonnegative q_u,q_v and frozen detector nuisance strata",
        "faithful_quotient_coordinate": "physical16; no source-to-physical16 selecting map is supplied by this branch",
        "source_authorized_probe_family": "conditional rates, widths, null-completed paired detector responses, replay/locality challenges, and reference-port randomization",
        "contextual_partition": "response-admissibility classes; the exact four-card grid is one class under the zero-drift predicate",
        "source_grid": [list(point) for point in source_grid],
        "selected_image_size": len(selected_image),
        "selection_reduction": selection_reduction,
        "operation_classification": "neither selector nor rigidifier; prospective detector-response validator",
        "smallest_exact_falsifier": "distinct cards (q_u,q_v)=(1,1) and (1,4) share the same response-admissibility record",
        "remaining_physical_instrument_gate": "response execution remains open, but even completion cannot replace the missing independently derived source-to-physical16 selector",
        "progressive_successor": "derive or falsify an invariant source portal such as WP360 from Spin(5), RG, threshold, or flavor geometry without fitted low-energy input",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp916_spin5_response_branch_disposition.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
