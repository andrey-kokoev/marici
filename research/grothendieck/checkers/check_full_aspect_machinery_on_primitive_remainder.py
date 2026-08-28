import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def decide(profile):
    provenance, typed, target, operational, nonredundant, bounded = profile
    if not (provenance and typed and target and nonredundant):
        return "reject"
    if not (operational and bounded):
        return "defer"
    return "admit"


def main() -> None:
    expected_results = [
        "ontology_falsifier.json",
        "four_rung_tower.json",
        "admissibility_governance_falsifier.json",
        "five_rung_tower.json",
        "experimental_portfolio_controller.json",
        "environment_port_tomography_run_analyzer.json",
        "sealed_controller_replay_run_analyzer.json",
        "comb_referenced_flavor_comparison.json",
        "four_atom_cross_scale_hostile.json",
        "laboratory_portfolio_schedule.json",
        "six_rung_tower.json",
    ]
    stack = {
        name: json.loads((ROOT / "aspect/results" / name).read_text(encoding="utf-8"))
        for name in expected_results
    }
    assert all(result["status"] == "pass" for result in stack.values())

    profiles = {
        "nonlinear_degree_lift": (True, True, True, True, False, True),
        "cross_coordinate_composition": (True, True, True, False, True, False),
        "probe_dependent_adversary": (False, True, True, True, True, True),
        "port_creation": (True, True, True, True, True, True),
        "support_refinement": (True, True, True, True, True, True),
        "arity_lift": (True, True, True, False, True, False),
        "singular_support": (True, True, True, True, True, True),
        "fresh_predicate": (False, True, False, False, True, False),
    }
    dispositions = {name: decide(profile) for name, profile in profiles.items()}
    expected = {
        "nonlinear_degree_lift": "reject",
        "cross_coordinate_composition": "defer",
        "probe_dependent_adversary": "reject",
        "port_creation": "admit",
        "support_refinement": "admit",
        "arity_lift": "defer",
        "singular_support": "admit",
        "fresh_predicate": "reject",
    }
    assert dispositions == expected

    gates = {
        "all_eleven_aspect_executables_pass": len(stack) == 11,
        "all_eight_ontology_mutations_classified": len(dispositions) == 8,
        "three_mutations_admitted": list(dispositions.values()).count("admit") == 3,
        "two_mutations_deferred": list(dispositions.values()).count("defer") == 2,
        "three_mutations_rejected": list(dispositions.values()).count("reject") == 3,
        "primitive_remainder_port_admitted": dispositions["port_creation"] == "admit",
        "joint_seed_sewing_deferred": dispositions["cross_coordinate_composition"] == "defer",
        "arity_three_sewing_deferred": dispositions["arity_lift"] == "defer",
        "degree_lift_alias_rejected": dispositions["nonlinear_degree_lift"] == "reject",
        "adaptive_source_without_provenance_rejected": dispositions["probe_dependent_adversary"] == "reject",
        "laboratory_schedule_excludes_deferred_cross_scale_invariant": stack["laboratory_portfolio_schedule.json"]["hostile_cost_models"]["deferred_cross_scale_invariant_not_scheduled"],
        "apparatus_availability_not_inferred": not stack["laboratory_portfolio_schedule.json"]["apparatus_availability_bound"],
    }
    assert all(gates.values())
    print(f"{len(gates)}/{len(gates)} full-machinery gates passed")


if __name__ == "__main__":
    main()

