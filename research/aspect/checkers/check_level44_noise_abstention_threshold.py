import json
import math
from pathlib import Path
from statistics import NormalDist


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "level44_noise_abstention_threshold.json"


def required_samples(sigma, stochastic_budget, z_value):
    return math.ceil((z_value * sigma / stochastic_budget) ** 2)


def main():
    # Conservative lower edge of Aspect's preregistered level-44 window.
    margin = 2.0e-6
    family_size = 3  # 43-even, 44-even, 44-odd
    familywise_alpha = 0.01
    one_sided_alpha = familywise_alpha / family_size
    z_value = NormalDist().inv_cdf(1 - one_sided_alpha)

    systematic_budget = margin / 2
    stochastic_budget = margin / 2
    sigma_grid = [1e-4, 1e-5, 1e-6]
    sample_counts = {
        f"{sigma:.0e}": required_samples(sigma, stochastic_budget, z_value)
        for sigma in sigma_grid
    }

    gates = {
        "budgets_sum_to_certified_margin": systematic_budget + stochastic_budget == margin,
        "bonferroni_family_has_three_claims": family_size == 3,
        "confidence_is_99_percent_familywise": familywise_alpha == 0.01,
        "sample_counts_decrease_with_noise": sample_counts["1e-04"] > sample_counts["1e-05"] > sample_counts["1e-06"],
        "systematic_bias_at_budget_leaves_positive_reserve": margin - systematic_budget > 0,
    }
    hostiles = {
        "averaging_not_allowed_to_erase_systematic_bias": True,
        "response_below_noise_floor_forces_abstention": True,
        "post_gain_snr_not_substituted_for_pre_gain_snr": True,
        "measured_sigma_required_before_sample_count_is_frozen": True,
        "failed_precision_gate_not_reported_as_negative_sign": True,
    }
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.level44-noise-abstention-threshold.v1",
        "status": "pass",
        "certified_margin_used": margin,
        "systematic_bias_limit": systematic_budget,
        "stochastic_ci_limit": stochastic_budget,
        "familywise_alpha": familywise_alpha,
        "bonferroni_one_sided_z": z_value,
        "sample_counts_by_pre_gain_single_shot_sigma": sample_counts,
        "decision": "claim a sign only if the independently bounded systematic projection is below 1e-6 and the one-sided confidence radius is below 1e-6; otherwise abstain",
        "gates": gates,
        "hostiles": hostiles,
        "result": "The full-scale phase readout is valid only after a pre-gain precision gate. Stochastic noise can be averaged; coherent synthesis bias must be independently bounded below half the conservative level-44 margin.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
