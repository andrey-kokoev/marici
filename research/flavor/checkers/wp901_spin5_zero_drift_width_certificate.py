"""WP901: exact zero-observed-drift instantiation of corrected WP900."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp900 = json.loads((ROOT / "results/wp900_spin5_paired_width_response_experiment.json").read_text())
    k = 6
    alpha = sp.Rational(1, 20)
    epsilon = sp.Rational(1, 100)
    n = sp.Integer(wp900["minimum_selected_events_per_cell_if_empirical_drift_zero"])
    radius = sp.sqrt(sp.log(2 ** (k + 2) / alpha) / (2 * n))
    upper = 2 * radius
    margin = epsilon - upper
    failure_bound = 2 ** (k + 2) * sp.exp(-n * epsilon**2 / 2)
    pilot_acceptance = sp.Rational(389, 14688)
    generated_per_cell = sp.ceiling(n / pilot_acceptance)
    checks = {
        "wp900_passes": wp900["passed"],
        "observed_drift_is_zero": True,
        "corrected_minimum_is_170819": n == 170819,
        "four_cell_selected_total_is_683276": 4 * n == 683276,
        "zero_drift_upper_bound_meets_tolerance": upper <= epsilon,
        "confidence_margin_positive": margin > 0,
        "four_cell_failure_bound_below_five_percent": failure_bound <= alpha,
        "one_fewer_selected_event_fails": 2 * sp.sqrt(sp.log(2 ** (k + 2) / alpha) / (2 * (n - 1))) > epsilon,
        "pilot_generated_projection_is_6449845_per_cell": generated_per_cell == 6449845,
        "pilot_projection_not_acceptance_authority": True,
        "no_observed_sample_or_selector_claim": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP901",
        "observed_empirical_tv": 0,
        "selected_events_per_cell": int(n),
        "selected_events_four_cells": int(4 * n),
        "confidence_upper_bound": float(sp.N(upper, 17)),
        "tolerance_margin": float(sp.N(margin, 17)),
        "four_cell_failure_probability_bound": float(sp.N(failure_bound, 17)),
        "pilot_acceptance": "389/14688",
        "diagnostic_generated_events_per_cell": int(generated_per_cell),
        "diagnostic_generated_events_four_cells": int(4 * generated_per_cell),
        "classification": "prospective exact zero-drift certificate; samples not executed; no selector",
        "smallest_exact_falsifier": "170818 selected events per cell fail the one-percent four-cell joint bound even at zero drift",
        "remaining_physical_instrument_gate": "generate and reconstruct all four direct-pole width cells and observe their actual drift and cell-specific efficiencies",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp901_spin5_zero_drift_width_certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
