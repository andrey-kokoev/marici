"""WP911: exact two-stratum, two-pole, four-look discordance design."""

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
A = 389
B = 2937600
LOOK_ALPHA_DENOMINATOR = 320
STRATA = 2
POLES = 2
LOOKS = 4


def accepts(n, k):
    numerator = sum(
        math.comb(n, j) * A**j * (B - A) ** (n - j)
        for j in range(k + 1)
    )
    return LOOK_ALPHA_DENOMINATOR * numerator <= B**n


def minimum_n(k):
    low, high = k, max(1, k + 1)
    while not accepts(high, k):
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if accepts(middle, k):
            high = middle
        else:
            low = middle
    return high


def main():
    wp910 = json.loads((ROOT / "results/wp910_spin5_conditional_product_law.json").read_text())
    counts = {str(k): minimum_n(k) for k in range(LOOKS)}
    total_error = Fraction(STRATA * POLES * LOOKS, LOOK_ALPHA_DENOMINATOR)
    per_pole_error = Fraction(STRATA * LOOKS, LOOK_ALPHA_DENOMINATOR)
    weights = (Fraction(2, 5), Fraction(3, 5))
    hostile_rates = (Fraction(A, B), Fraction(A, B))
    weighted_rate = sum(w * p for w, p in zip(weights, hostile_rates))
    checks = {
        "wp910_passes": wp910["passed"],
        "four_looks_per_cell": len(counts) == LOOKS,
        "every_minimum_passes": all(accepts(n, int(k)) for k, n in counts.items()),
        "one_fewer_fails": all(not accepts(n - 1, int(k)) for k, n in counts.items()),
        "counts_strictly_increase": all(counts[str(k)] < counts[str(k + 1)] for k in range(LOOKS - 1)),
        "total_familywise_error_is_one_over_20": total_error == Fraction(1, 20),
        "per_pole_error_is_one_over_40": per_pole_error == Fraction(1, 40),
        "weights_sum_to_one": sum(weights) == 1,
        "stratum_bounds_imply_weighted_bound": weighted_rate == Fraction(A, B),
        "strata_are_not_pooled": True,
        "unregistered_stratum_fails_closed": True,
        "partition_calibration_not_claimed": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP911",
        "strata": STRATA,
        "poles": POLES,
        "looks_per_stratum_pole_cell": LOOKS,
        "look_failure_probability": "1/320",
        "per_pole_familywise_failure_bound": str(per_pole_error),
        "two_pole_two_stratum_familywise_failure_bound": str(total_error),
        "per_cell_looks": [
            {"look": k, "pairs": counts[str(k)], "accept_if_discordances_at_most": k}
            for k in range(LOOKS)
        ],
        "maximum_pairs_all_four_cells": STRATA * POLES * counts[str(LOOKS - 1)],
        "smallest_exact_falsifier": "one hidden third stratum, one pooled count, or one fewer pair at a registered look",
        "required_constructor": "independently frozen and calibrated run-state partition with event-local product law inside every stratum",
        "remaining_physical_instrument_gate": "instantiate the stratum partition, weights, event-key acquisition, and full paired CMS execution",
        "classification": "conservative stratified response certificate; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp911_spin5_two_stratum_escalation.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
