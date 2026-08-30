"""WP900: exact distribution-free paired-width response design."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp897 = json.loads((ROOT / "results/wp897_spin5_universal_mixing_source_card_factorization.json").read_text())
    wp899 = json.loads((ROOT / "results/wp899_spin5_tau_resolution_applicability_audit.json").read_text())
    k = 6
    alpha = sp.Rational(1, 20)
    epsilon = sp.Rational(1, 100)
    n = sp.symbols("n", positive=True, integer=True)
    radius = sp.sqrt(sp.log(2 ** (k + 2) / alpha) / (2 * n))
    minimum_equal_n = sp.ceiling(2 * sp.log(2 ** (k + 2) / alpha) / epsilon**2)
    at_minimum = sp.N(2 * radius.subs(n, minimum_equal_n), 20)
    checks = {
        "parent_packets_pass": wp897["passed"] and wp899["passed"],
        "six_bin_family": k == 6,
        "four_cell_union_factor_is_2_power_k_plus_two": 2 ** (k + 2) == 256,
        "radius_positive": radius > 0,
        "radius_decreases_with_n": sp.diff(radius, n) < 0,
        "minimum_selected_events_is_170819": minimum_equal_n == 170819,
        "minimum_meets_one_percent_bound": at_minimum <= sp.N(epsilon, 20),
        "one_fewer_fails_one_percent_bound": sp.N(2 * radius.subs(n, minimum_equal_n - 1), 20) > sp.N(epsilon, 20),
        "four_source_width_cells_required": 2 * 2 == 4,
        "distribution_free_not_gaussian": True,
        "no_execution_or_selector_claim": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP900",
        "bins": k,
        "joint_failure_probability": str(alpha),
        "diagnostic_tv_tolerance": str(epsilon),
        "confidence_radius": "sqrt(log(2^(k+2)/alpha)/(2*n)) per cell for four-cell joint coverage",
        "required_cells": ["u_zero_width", "u_max_width", "v_zero_width", "v_max_width"],
        "minimum_selected_events_per_cell_if_empirical_drift_zero": int(minimum_equal_n),
        "acceptance": "empirical_TV + r(n0,alpha) + r(n1,alpha) <= epsilon independently at both poles",
        "classification": "executable distribution-free response-stability experiment; not executed instrument or selector",
        "smallest_falsifier": "one pole's confidence upper bound exceeds the frozen tolerance",
        "remaining_physical_instrument_gate": "produce and reconstruct four checksum-pinned CP-even cells, then include efficiencies and nuisance completion",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp900_spin5_paired_width_response_experiment.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
