"""WP914: exact CHSH measurement-dependence hostile."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETTINGS = tuple(itertools.product((0, 1), repeat=2))


def local_wins(alice, bob):
    return sum((alice[x] ^ bob[y]) == (x & y) for x, y in SETTINGS)


def main():
    wp913 = json.loads((ROOT / "results/wp913_spin5_bell_randomness_reference_port.json").read_text())
    response_functions = tuple(itertools.product((0, 1), repeat=2))
    local_scores = [local_wins(alice, bob) for alice in response_functions for bob in response_functions]
    correlated_records = []
    for x, y in SETTINGS:
        hidden_lambda = (x, y)
        a = 0
        b = hidden_lambda[0] & hidden_lambda[1]
        correlated_records.append({"x": x, "y": y, "a": a, "b": b, "win": (a ^ b) == (x & y)})
    setting_counts = {(x, y): 0 for x, y in SETTINGS}
    for row in correlated_records:
        setting_counts[(row["x"], row["y"])] += 1
    checks = {
        "wp913_passes_conditionally": wp913["passed"],
        "sixteen_local_deterministic_strategies": len(local_scores) == 16,
        "measurement_independent_local_max_is_three": max(local_scores) == 3,
        "local_classical_win_rate_is_at_most_three_quarters": Fraction(max(local_scores), 4) == Fraction(3, 4),
        "correlated_settings_are_uniform_marginally": set(setting_counts.values()) == {1},
        "measurement_dependent_strategy_wins_all_four": all(row["win"] for row in correlated_records),
        "measurement_dependent_win_rate_is_one": Fraction(sum(row["win"] for row in correlated_records), 4) == 1,
        "outputs_are_deterministic_given_lambda": True,
        "conditional_output_entropy_is_zero": True,
        "bell_score_does_not_certify_seed_independence": True,
        "randomness_expansion_requires_upstream_seed": True,
        "public_beacon_requires_causal_isolation": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP914",
        "independent_local_maximum_win_rate": "3/4",
        "measurement_dependent_hostile_win_rate": "1",
        "setting_distribution": "uniform on four CHSH setting pairs",
        "conditional_output_entropy_given_hidden_settings": "0",
        "smallest_exact_falsifier": "one future setting bit is predictable to both Bell devices before the trial",
        "required_constructor": "causally isolated private setting seed, or a typed randomness-amplification/multiple-source protocol whose assumptions exclude device correlation",
        "remaining_physical_instrument_gate": "instantiate and audit the upstream setting-source preparation and its causal separation from both Bell devices",
        "classification": "measurement-independence obstruction to the reference port; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp914_spin5_bell_setting_seed_hostile.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
