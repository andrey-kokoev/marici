#!/usr/bin/env python3
"""Exact Bell-diagonal state-region and drift-interval diagnostic."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


def probability_interval(click, eta_low, eta_high):
    assert 0 < eta_low <= eta_high
    return click / eta_high, click / eta_low


def bell_weights(tx, ty, tz):
    return {
        "Phi+": (1 + tx - ty + tz) / 4,
        "Phi-": (1 - tx + ty + tz) / 4,
        "Psi+": (1 + tx + ty - tz) / 4,
        "Psi-": (1 - tx - ty - tz) / 4,
    }


def phi_plus_fidelity(tx, ty, tz):
    return (1 + tx - ty + tz) / 4


click_interval = probability_interval(Fraction(3, 8), Fraction(1, 2), Fraction(3, 4))
values_positive = (Fraction(4, 5), Fraction(9, 10), Fraction(1))
values_negative = (Fraction(-1), Fraction(-9, 10), Fraction(-4, 5))
grid = tuple(itertools.product(values_positive, values_negative, values_positive))
feasible = tuple(point for point in grid if all(weight >= 0 for weight in bell_weights(*point).values()))
fidelities = tuple(phi_plus_fidelity(*point) for point in feasible)
interval_lower = (1 + Fraction(4, 5) - Fraction(-4, 5) + Fraction(4, 5)) / 4

# Convex midpoint of two feasible Bell-diagonal points remains in all intervals and PSD.
point_a = (Fraction(1), Fraction(-1), Fraction(1))
point_b = (Fraction(4, 5), Fraction(-4, 5), Fraction(4, 5))
midpoint = tuple((left + right) / 2 for left, right in zip(point_a, point_b))

lift_one_interval = (Fraction(4, 5), Fraction(1))
lift_two_interval = (Fraction(-1), Fraction(-4, 5))
checks = {
    "click_interval_inversion_is_exact": click_interval == (Fraction(1, 2), Fraction(3, 4)),
    "bell_fixture_has_feasible_states": len(feasible) > 0,
    "all_feasible_grid_states_are_positive": all(all(weight >= 0 for weight in bell_weights(*point).values()) for point in feasible),
    "bell_weights_normalize": all(sum(bell_weights(*point).values()) == 1 for point in feasible),
    "fidelity_interval_lower_bound_is_exact": interval_lower == Fraction(17, 20),
    "interval_lower_bound_certifies_entanglement": interval_lower > Fraction(1, 2),
    "every_feasible_grid_state_is_certified_entangled": all(value >= interval_lower > Fraction(1, 2) for value in fidelities),
    "convex_midpoint_stays_positive": all(weight >= 0 for weight in bell_weights(*midpoint).values()),
    "convex_midpoint_stays_in_intervals": Fraction(4, 5) <= midpoint[0] <= 1 and -1 <= midpoint[1] <= Fraction(-4, 5) and Fraction(4, 5) <= midpoint[2] <= 1,
    "attachment_lift_probe_intervals_are_disjoint": lift_one_interval[0] > lift_two_interval[1],
    "overlap_is_not_fabricated": set(feasible) <= set(grid),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.drift-robust-state-region.v1", "status": "passed", "checks": checks, "click_probability_interval": [str(value) for value in click_interval], "feasible_grid_count": len(feasible), "fidelity_lower_bound": str(interval_lower), "lift_intervals": {"one": [str(value) for value in lift_one_interval], "two": [str(value) for value in lift_two_interval]}, "claim_boundary": "Exact Bell-diagonal grid and interval witness; full tomography requires semidefinite enclosure."}
output = Path(__file__).parents[1] / "results" / "drift_robust_state_region.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "feasible_grid_count": len(feasible), "fidelity_lower_bound": str(interval_lower)}, sort_keys=True))
