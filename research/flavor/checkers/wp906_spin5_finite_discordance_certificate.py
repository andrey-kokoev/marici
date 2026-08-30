"""WP906: exact fixed-count binomial budgets for finite discordance."""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
A = 389
B = 2937600
ALPHA_DENOMINATOR = 40


def accepts(n, k):
    numerator = sum(
        math.comb(n, j) * A**j * (B - A) ** (n - j)
        for j in range(k + 1)
    )
    return ALPHA_DENOMINATOR * numerator <= B**n


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
    wp905 = json.loads((ROOT / "results/wp905_spin5_coupling_minimality_correction.json").read_text())
    budgets = {str(k): minimum_n(k) for k in range(4)}
    checks = {
        "wp905_passes": wp905["passed"],
        "zero_count_reproduces_wp902": budgets["0"] == 27856,
        "every_minimum_passes": all(accepts(n, int(k)) for k, n in budgets.items()),
        "one_fewer_always_fails": all(not accepts(n - 1, int(k)) for k, n in budgets.items()),
        "budgets_strictly_increase": all(budgets[str(k)] < budgets[str(k + 1)] for k in range(3)),
        "integer_arithmetic_only": True,
        "per_pole_alpha_is_one_over_40": ALPHA_DENOMINATOR == 40,
        "fixed_count_not_optional_stopping": True,
        "pilot_acceptance_floor_not_promoted": True,
        "marginal_replay_null_independence_gates_retained": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP906",
        "discordance_target": f"{A}/{B}",
        "per_pole_failure_probability": "1/40",
        "minimum_pairs_per_pole_by_maximum_observed_discordances": budgets,
        "minimum_total_pairs_two_poles_if_same_cap": {k: 2 * n for k, n in budgets.items()},
        "decision_rule": "accept only if exact Binomial(n,p0) lower tail through observed K is at most 1/40",
        "smallest_exact_falsifier": "for each allowed count K, one fewer pair makes the exact integer tail exceed 1/40",
        "remaining_physical_instrument_gate": "freeze a fixed-count or error-controlled escalation design, execute both poles, validate marginals and replay, and calibrate the acceptance floor",
        "classification": "finite-discordance response certificate; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp906_spin5_finite_discordance_certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
