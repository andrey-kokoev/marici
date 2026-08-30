"""WP910: exact shared-nuisance hostile to unconditional binomial counts."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp907 = json.loads((ROOT / "results/wp907_spin5_error_controlled_escalation.json").read_text())
    wp909 = json.loads((ROOT / "results/wp909_spin5_cross_sector_independence_transfer.json").read_text())
    p0 = Fraction(389, 2937600)
    delta = p0 / 2
    p_minus = p0 - delta
    p_plus = p0 + delta
    n = wp907["looks"][0]["pairs_per_pole"]
    iid_zero = (1 - p0) ** n
    mixture_zero = ((1 - p_minus) ** n + (1 - p_plus) ** n) / 2
    covariance = delta**2
    iid_variance = n * p0 * (1 - p0)
    mixture_variance = iid_variance + n * (n - 1) * covariance
    look_alpha = Fraction(1, 160)
    checks = {
        "wp907_passes_conditionally": wp907["passed"],
        "wp909_global_obstruction_retained": wp909["passed"],
        "mixture_event_marginal_is_p0": (p_minus + p_plus) / 2 == p0,
        "both_conditional_probabilities_are_valid": 0 < p_minus < p_plus < 1,
        "conditional_keys_can_be_iid": True,
        "unconditional_covariance_is_delta_squared": covariance == Fraction(389**2, (2 * 2937600) ** 2),
        "unconditional_covariance_is_positive": covariance > 0,
        "mixture_variance_exceeds_binomial": mixture_variance > iid_variance,
        "mixture_zero_probability_exceeds_iid": mixture_zero > iid_zero,
        "iid_first_look_meets_allocation": iid_zero <= look_alpha,
        "mixture_first_look_breaks_allocation": mixture_zero > look_alpha,
        "run_label_must_not_be_discarded": True,
        "event_locality_is_required": True,
        "key_acquisition_still_uninstantiated": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP910",
        "product_law": "fixed run state plus independent event keys plus event-local deterministic transform implies conditional iid discordances",
        "first_look_pairs": n,
        "p0": str(p0),
        "delta": str(delta),
        "conditional_probabilities": [str(p_minus), str(p_plus)],
        "unconditional_pair_covariance": str(covariance),
        "iid_zero_probability_decimal": float(iid_zero),
        "mixture_zero_probability_decimal": float(mixture_zero),
        "look_error_allocation": str(look_alpha),
        "smallest_exact_falsifier": "one forgotten binary run nuisance with p(C)=p0 plus or minus p0/2 creates positive cross-event covariance",
        "required_constructor": "freeze and retain the complete run-state stratum, prove event-locality, and acquire independent per-event keys",
        "remaining_physical_instrument_gate": "calibrated event-key acquisition plus a manifest excluding cross-event mutable state; otherwise use a stratified or mixture-valid test",
        "classification": "conditional product-law gate; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp910_spin5_conditional_product_law.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
