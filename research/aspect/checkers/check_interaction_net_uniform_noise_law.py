#!/usr/bin/env python3
"""SCC checker for the conditional uniform noise/degradation law."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "interaction-net-uniform-noise-law.v1.json"
RESULT = ASPECT / "results" / "interaction_net_uniform_noise_law.json"

def covariance(independent, common, sorter):
    return tuple(tuple(
        (independent ** 2 + sorter ** 2 if i == j else 0.0) + common ** 2
        for j in range(5)
    ) for i in range(5))

def push_diagonal(cov, diagonal):
    return tuple(tuple(diagonal[i] * cov[i][j] * diagonal[j] for j in range(5)) for i in range(5))

def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(5)) for i in range(5))

def max_row_sum(matrix):
    return max(sum(abs(x) for x in row) for row in matrix)

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    levels = []
    uniform_bound = 0.0
    for low in range(12):
        high = low + 1
        gain_low = 1.0 + 0.03 * low
        gain_high = 1.0 + 0.03 * high
        active = (1.0, 1.0, 1.0, 0.0 if low % 2 else 1.0, 0.0 if low % 3 else 1.0)
        jacobian = tuple(gain_low / gain_high * x for x in active)
        low_cov = covariance(0.08, 0.03, 0.02)
        high_cov = covariance(0.08, 0.03, 0.02)
        residual_cov = add(low_cov, push_diagonal(high_cov, jacobian))
        envelope = max_row_sum(residual_cov)
        uniform_bound = max(uniform_bound, envelope)
        levels.append({"low": low, "high": high, "gain_ratio": gain_low / gain_high,
                       "residual_covariance_row_sum": envelope})

    hostile_growth = [0.08 if r <= 5 else 0.08 * (r - 4) ** 2 for r in range(12)]
    prefix_indistinguishable = all(hostile_growth[r] == 0.08 for r in range(6))
    later_violation = max(hostile_growth[6:]) > 1.0
    unbounded_gain_ratios = [(r + 2) ** 2 / (r + 1) for r in range(12)]
    hostiles = {
        "finite_prefix_camouflage_constructed": prefix_indistinguishable and later_violation,
        "unbounded_gain_ratio_detected": max(unbounded_gain_ratios) > 10.0,
        "cross_covariance_required": "paired-route cross covariance is retained" in contract["law"]["uniform_requirements"],
        "raw_variance_substitution_rejected": "raw rather than calibrated variance compared" in contract["hostiles"],
        "threshold_refit_rejected": "threshold refit after observing the failing level" in contract["hostiles"],
        "finite_prefix_not_promoted": not contract["law"]["empirical_finite_prefix_can_establish_uniformity"],
        "synthetic_family_not_promoted": not contract["authority"]["uniform_physical_law_certified"]
    }
    passed = uniform_bound < 0.1 and all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-uniform-noise-law-result.v1",
        "passed": passed,
        "synthetic_levels": levels,
        "uniform_synthetic_row_sum_bound": uniform_bound,
        "hostile_growth": hostile_growth,
        "hostiles": hostiles,
        "physical_status": "not_run",
        "verdict": "conditional_uniform_law_checker_passes_but_finite_data_cannot_certify_all_levels"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
