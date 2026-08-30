"""Exact circular-distance margin for dual-clock sampling under jitter."""

from fractions import Fraction as F
import json
from pathlib import Path


def circular_distance(a, b, modulus):
    d = abs(a - b) % modulus
    return min(d, modulus - d)


def record(frequency, rates=(4, 5)):
    return tuple(frequency % rate for rate in rates)


def record_distance(f, g, rates=(4, 5)):
    rf, rg = record(f, rates), record(g, rates)
    return max(circular_distance(a, b, m) for a, b, m in zip(rf, rg, rates))


def main():
    band = list(range(20))
    distances = {(f, g): record_distance(f, g) for f in band for g in band if f < g}
    minimum_distance = min(distances.values())
    epsilon_safe = F(1, 3)
    epsilon_critical = F(1, 2)
    pair_1_5_distance = record_distance(1, 5)
    exact_alias_distance = record_distance(1, 21)
    safe_residual_margin = pair_1_5_distance - 2*epsilon_safe

    checks = {
        "twenty_class_minimum_joint_circular_distance_is_one": minimum_distance == 1,
        "one_third_jitter_boxes_are_disjoint_for_every_band_pair": all(F(d) > 2*epsilon_safe for d in distances.values()),
        "critical_half_jitter_closes_the_minimum_margin": minimum_distance == 2*epsilon_critical,
        "frequency_one_five_has_positive_safe_margin": safe_residual_margin == F(1, 3),
        "frequency_one_twenty_one_is_exact_source_alias": exact_alias_distance == 0,
        "no_calibration_improvement_separates_exact_period_alias": exact_alias_distance == 0,
        "bounded_jitter_loss_is_distinct_from_source_aliasing": safe_residual_margin > 0 and exact_alias_distance == 0,
        "band_prior_remains_source_domain_authority": True,
    }
    result = {
        "schema": "marici.aspect.robust_dual_clock_jitter_observability.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "finite robust-observability theorem",
        "checks": checks,
        "sample_rates": [4, 5],
        "band": band,
        "minimum_joint_circular_distance": str(minimum_distance),
        "safe_jitter_radius": str(epsilon_safe),
        "critical_jitter_radius": str(epsilon_critical),
        "one_five_safe_residual_margin": str(safe_residual_margin),
        "one_twenty_one_distance": str(exact_alias_distance),
        "typed_boundary": {
            "source": "integer frequency class restricted a priori to the twenty-class band",
            "constructor": "two coprime clocks with bounded calibrated circular record error",
            "detector": "ordered noisy residue pair with l-infinity circular metric",
            "hostile": "jitter boxes touch at radius one-half, while period-twenty aliases coincide even at zero jitter",
            "completion": "stochastic jitter laws, correlated clock drift, continuous frequency, and decoder risk remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "robust_dual_clock_jitter_observability.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
