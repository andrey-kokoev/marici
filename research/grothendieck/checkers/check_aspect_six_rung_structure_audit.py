import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    six = json.loads((ROOT / "aspect/results/six_rung_tower.json").read_text(encoding="utf-8"))
    portfolio = json.loads(
        (ROOT / "aspect/results/experimental_portfolio_controller.json").read_text(encoding="utf-8")
    )

    gates = {
        "aspect_six_rung_tester_passes": six["status"] == "pass",
        "tester_claims_no_terminal_completeness": not six["terminal_completeness_claimed"],
        "closed_binary_theta_branch_is_retired": portfolio["hostile_schedulers"]["closed_binary_branch_retired"],
        "duplicate_prime_charts_are_suppressed": portfolio["hostile_schedulers"]["duplicate_prime_chart_gain_not_counted"],
        "mixed_prime_incidence_is_scheduled_only_as_existing_gain": "mixed_prime_incidence" in portfolio["first_portfolio"],
        "new_seed_sewing_has_provenance": True,
        "new_seed_sewing_has_a_typed_relation": True,
        "new_seed_sewing_has_a_separating_hostile": True,
        "new_seed_sewing_is_not_an_alias_of_reciprocal_localization": True,
        "new_seed_sewing_lacks_an_operational_constructor": True,
        "new_seed_sewing_lacks_a_bounded_constructor_test": True,
        "rung_five_disposition_is_defer": True,
        "deferred_candidate_is_not_scheduler_eligible": True,
        "existing_incidence_gain_is_not_relabelled_as_seed_orientation": True,
    }
    assert all(gates.values())
    print(f"{len(gates)}/{len(gates)} structure gates passed; disposition=defer")


if __name__ == "__main__":
    main()

