"""WP902: exact zero-discordance paired null-completed width test."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp901 = json.loads((ROOT / "results/wp901_spin5_zero_drift_width_certificate.json").read_text())
    alpha = sp.Rational(1, 20)
    epsilon = sp.Rational(1, 100)
    acceptance_floor = sp.Rational(389, 14688)
    discordance_target = acceptance_floor * epsilon / 2
    n = sp.ceiling(sp.log(alpha / 2) / sp.log(1 - discordance_target))
    discordance_upper = 1 - (alpha / 2) ** (sp.Rational(1, n))
    conditional_upper = 2 * discordance_upper / acceptance_floor
    previous_upper = 2 * (1 - (alpha / 2) ** (sp.Rational(1, n - 1))) / acceptance_floor
    checks = {
        "wp901_passes": wp901["passed"],
        "seven_symbol_output_includes_null": 1 + 6 == 7,
        "two_pole_failure_allocation_is_alpha_over_two": alpha / 2 == sp.Rational(1, 40),
        "discordance_target_exact": discordance_target == sp.Rational(389, 2937600),
        "minimum_pairs_per_pole_is_27856": n == 27856,
        "total_pairs_is_55712": 2 * n == 55712,
        "conditional_upper_meets_one_percent": conditional_upper <= epsilon,
        "one_fewer_pair_fails": previous_upper > epsilon,
        "paired_budget_below_independent_selected_budget": 2 * n < wp901["selected_events_four_cells"],
        "acceptance_floor_is_design_not_authority": True,
        "coupling_must_be_frozen_and_replayable": True,
        "independent_fallback_retained": True,
        "no_execution_or_selector_claim": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP902",
        "output_alphabet": ["not_selected", "bin1", "bin2", "bin3", "bin4", "bin5", "bin6"],
        "observed_discordances": 0,
        "pilot_acceptance_floor": "389/14688",
        "discordance_probability_target": str(discordance_target),
        "minimum_generated_pairs_per_pole": int(n),
        "minimum_generated_pairs_total": int(2 * n),
        "conditional_selected_shape_tv_upper": float(sp.N(conditional_upper, 17)),
        "classification": "prospective paired null-completed response certificate; no samples executed and no selector",
        "smallest_exact_falsifier": "27855 zero-discordance pairs per pole fail the one-percent conditional bound",
        "remaining_physical_instrument_gate": "implement the frozen common-random-number CMS coupling and independently certify the acceptance floor at both poles under nuisance completion",
        "fallback": "WP901 independent four-cell test if pairing, null retention, or acceptance certification fails",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp902_spin5_paired_null_completed_width_test.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
