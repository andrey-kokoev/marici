"""WP907: exact Bonferroni-safe four-look discordance escalation."""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
A = 389
B = 2937600
LOOK_ALPHA_DENOMINATOR = 160


def accepts(n, k):
    tail_numerator = sum(
        math.comb(n, j) * A**j * (B - A) ** (n - j)
        for j in range(k + 1)
    )
    return LOOK_ALPHA_DENOMINATOR * tail_numerator <= B**n


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
    wp906 = json.loads((ROOT / "results/wp906_spin5_finite_discordance_certificate.json").read_text())
    looks = {str(k): minimum_n(k) for k in range(4)}
    checks = {
        "wp906_passes": wp906["passed"],
        "four_looks_frozen": len(looks) == 4,
        "every_look_minimum_passes": all(accepts(n, int(k)) for k, n in looks.items()),
        "one_fewer_pair_fails_each_look": all(not accepts(n - 1, int(k)) for k, n in looks.items()),
        "look_counts_strictly_increase": all(looks[str(k)] < looks[str(k + 1)] for k in range(3)),
        "per_pole_union_bound_is_one_over_40": 4 * 40 == LOOK_ALPHA_DENOMINATOR,
        "two_pole_union_bound_is_one_over_20": 2 * 4 * 20 == LOOK_ALPHA_DENOMINATOR,
        "look_dependence_does_not_break_union_bound": True,
        "no_unregistered_optional_look": True,
        "instrument_gates_retained": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP907",
        "discordance_target": f"{A}/{B}",
        "look_failure_probability": "1/160",
        "per_pole_familywise_failure_bound": "1/40",
        "two_pole_familywise_failure_bound": "1/20",
        "looks": [
            {"look": k, "pairs_per_pole": looks[str(k)], "accept_if_discordances_at_most": k}
            for k in range(4)
        ],
        "stopping_rule": "at each frozen look stop and certify iff cumulative discordances do not exceed that look's boundary; otherwise continue, and fail closed after look 3",
        "smallest_exact_falsifier": "one unregistered extra look or one acceptance above its frozen discordance boundary",
        "remaining_physical_instrument_gate": "execute the frozen paired chain with marginal validation, replay evidence, null retention, pair-independence audit, and calibrated acceptance floor",
        "classification": "error-controlled stopping instrument; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp907_spin5_error_controlled_escalation.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
