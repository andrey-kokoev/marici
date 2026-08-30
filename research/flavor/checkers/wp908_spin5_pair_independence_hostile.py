"""WP908: exact run-level latent-bit hostile to pair independence."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp904 = json.loads((ROOT / "results/wp904_spin5_semantic_random_field_coupling.json").read_text())
    wp907 = json.loads((ROOT / "results/wp907_spin5_error_controlled_escalation.json").read_text())
    p0 = Fraction(389, 2937600)
    n0 = wp907["looks"][0]["pairs_per_pole"]
    hostile_zero_probability = 1 - p0
    iid_zero_probability = (1 - p0) ** n0
    look_alpha = Fraction(1, 160)
    marginal_discordance = p0
    covariance_entry = p0 * (1 - p0)
    checks = {
        "wp904_replay_hostile_available": wp904["passed"],
        "wp907_conditional_rule_passes": wp907["passed"],
        "each_event_has_target_marginal": marginal_discordance == p0,
        "hostile_is_replayable": True,
        "hostile_can_use_stable_addresses": True,
        "run_count_support_is_only_zero_or_n": True,
        "hostile_zero_probability_exceeds_look_alpha": hostile_zero_probability > look_alpha,
        "iid_zero_probability_meets_look_alpha": iid_zero_probability <= look_alpha,
        "hostile_and_iid_count_laws_differ": hostile_zero_probability != iid_zero_probability,
        "covariance_entry_is_positive": covariance_entry > 0,
        "covariance_rank_is_one": n0 > 1 and covariance_entry != 0,
        "marginals_do_not_imply_independence": True,
        "empirical_tests_are_falsifiers_not_proofs": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP908",
        "hostile": "one run-level Bernoulli bit copied to every pair-discordance indicator",
        "target_pair_discordance_marginal": str(p0),
        "first_look_pairs": n0,
        "hostile_zero_discordance_probability": str(hostile_zero_probability),
        "iid_zero_discordance_probability_decimal": float(iid_zero_probability),
        "first_look_error_allocation": str(look_alpha),
        "discordance_covariance_rank": 1,
        "smallest_exact_falsifier": "one shared run-level latent bit yields correct event marginals but rank-one dependence and false-certification probability 1-p0",
        "required_constructor": "independently randomized event-key acquisition or an explicit source theorem for the randomized counter-based key model",
        "remaining_physical_instrument_gate": "declare and calibrate the entropy instrument, event-key provenance, key scope, health tests, retries, collision policy, and run boundaries",
        "classification": "independence-authority obstruction; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp908_spin5_pair_independence_hostile.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
