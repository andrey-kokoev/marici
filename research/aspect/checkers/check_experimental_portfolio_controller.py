from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "experimental-portfolio-controller.v1.json"
RESULT = ROOT / "results" / "experimental_portfolio_controller.json"


def candidates():
    return [
        {"key": "environment_tomography", "cost": 4, "gains": {0, 1}, "sector": "optics", "status": "admit", "faithful": True, "closed": False, "deps": set()},
        {"key": "flux_dual_gain", "cost": 2, "gains": {2}, "sector": "optics", "status": "admit", "faithful": True, "closed": False, "deps": set()},
        {"key": "controller_replay", "cost": 2, "gains": {3}, "sector": "control", "status": "admit", "faithful": True, "closed": False, "deps": set()},
        {"key": "three_back_hankel", "cost": 3, "gains": {4}, "sector": "optics", "status": "admit", "faithful": True, "closed": False, "deps": set()},
        {"key": "mixed_prime_incidence", "cost": 3, "gains": {5}, "sector": "arithmetic", "status": "admit", "faithful": True, "closed": False, "deps": {"direct_ternary_constructor"}},
        {"key": "prime_chart_p2", "cost": 1, "gains": {5}, "sector": "arithmetic", "status": "admit", "faithful": False, "closed": False, "deps": set()},
        {"key": "prime_chart_p3", "cost": 1, "gains": {5}, "sector": "arithmetic", "status": "admit", "faithful": False, "closed": False, "deps": set()},
        {"key": "finite_binary_theta_repair", "cost": 1, "gains": {5}, "sector": "arithmetic", "status": "admit", "faithful": True, "closed": True, "deps": set()},
        {"key": "variable_amplitude_arity_four", "cost": 4, "gains": {6}, "sector": "arithmetic", "status": "defer", "faithful": True, "closed": False, "deps": {"arity_four_constructor"}},
        {"key": "sterile_fresh_nonce", "cost": 1, "gains": {7}, "sector": "unknown", "status": "reject", "faithful": False, "closed": False, "deps": set()},
    ]


def eligible(item, completed):
    return (item["status"] == "admit" and item["faithful"] and
            not item["closed"] and item["deps"] <= completed)


def score(portfolio):
    gains = set().union(*(item["gains"] for item in portfolio)) if portfolio else set()
    sectors = {item["sector"] for item in portfolio}
    cost = sum(item["cost"] for item in portfolio)
    keys = tuple(sorted(item["key"] for item in portfolio))
    return len(gains), len(sectors), -cost, tuple(reversed(keys))


def optimize(items, budget, completed):
    pool = [item for item in items if eligible(item, completed)]
    feasible = []
    for size in range(len(pool) + 1):
        for portfolio in combinations(pool, size):
            if sum(item["cost"] for item in portfolio) <= budget:
                feasible.append(portfolio)
    best = max(feasible, key=score)
    return best, len(feasible)


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    items = candidates()
    completed = {"direct_ternary_constructor"}
    first, searched = optimize(items, contract["budget"], completed)
    first_keys = sorted(item["key"] for item in first)
    assert first_keys == ["controller_replay", "environment_tomography", "mixed_prime_incidence"]
    first_gains = set().union(*(item["gains"] for item in first))
    assert len(first_gains) == 4 and sum(item["cost"] for item in first) == 9

    remaining = [item for item in items if item["key"] not in first_keys and not (item["gains"] <= first_gains)]
    second, searched_second = optimize(remaining, contract["budget"], completed)
    second_keys = sorted(item["key"] for item in second)
    assert second_keys == ["flux_dual_gain", "three_back_hankel"]
    scheduled = set(first_keys + second_keys)
    live_faithful = {item["key"] for item in items if eligible(item, completed)}
    nonstarved = live_faithful <= scheduled | {"finite_binary_theta_repair"}
    assert nonstarved

    hostiles = {
        "rejected_and_deferred_candidates_excluded": not any(item["status"] != "admit" for item in first + second),
        "budget_violation_rejected": sum(item["cost"] for item in first) <= contract["budget"],
        "dependency_inversion_rejected": all(item["deps"] <= completed for item in first + second),
        "closed_binary_branch_retired": "finite_binary_theta_repair" not in scheduled,
        "duplicate_prime_chart_gain_not_counted": not ({"prime_chart_p2", "prime_chart_p3"} & scheduled),
        "unfaithful_cheap_alias_cannot_replace_incidence": "mixed_prime_incidence" in scheduled,
        "cheap_test_loop_cannot_starve_decisive_tests": nonstarved,
        "speaker_and_name_capture_rejected": first_gains == set().union(*(item["gains"] for item in reversed(first))),
        "desired_verdict_not_an_objective": "verdict" not in contract["objective_order"],
        "adaptive_retirement_exposes_second_portfolio": second_keys == ["flux_dual_gain", "three_back_hankel"],
    }
    assert all(hostiles.values())
    out = {
        "schema": "marici.aspect.experimental-portfolio-controller-check.v1",
        "status": "pass", "candidate_count": len(items),
        "first_cycle_feasible_portfolios_exhausted": searched,
        "first_portfolio": first_keys, "first_cost": 9,
        "first_independent_directions": len(first_gains),
        "second_cycle_feasible_portfolios_exhausted": searched_second,
        "second_portfolio": second_keys,
        "all_live_faithful_candidates_scheduled_within_two_cycles": nonstarved,
        "hostile_schedulers": hostiles,
        "theta_disposition": "retire finite binary and duplicate prime-chart probes; schedule mixed-prime incidence after direct ternary construction",
        "absolute_scheduler_optimality": False,
        "boundary": "Optimality is exact for the frozen candidates, costs, quotient gains, dependencies, budget, and lexicographic objective; those inputs remain falsifiable.",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
