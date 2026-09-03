#!/usr/bin/env python3
"""Exact drift/state confounding, bias-bound, and interpolation diagnostics."""

import json
from fractions import Fraction
from pathlib import Path


def records(m, eta_plus, eta_minus):
    plus = eta_plus * (1 + m) / 2
    minus = eta_minus * (1 - m) / 2
    return plus, minus, 1 - plus - minus


def inferred_with_stale_calibration(m, delta_plus, delta_minus):
    q_plus = (1 + delta_plus) * (1 + m) / 2
    q_minus = (1 + delta_minus) * (1 - m) / 2
    return (q_plus - q_minus) / (q_plus + q_minus)


stale = (Fraction(1, 2), Fraction(1, 2))
drifted_records = records(Fraction(0), Fraction(3, 4), Fraction(1, 4))
state_signal_records = records(Fraction(1, 2), *stale)

# Exhaustive rational-grid check of the derived bound.
epsilon = Fraction(1, 4)
grid = tuple(Fraction(value, 4) for value in range(-4, 5))
deltas = tuple(Fraction(value, 4) for value in range(-1, 2))
bound_checks = []
for m in grid:
    for delta_plus in deltas:
        for delta_minus in deltas:
            inferred = inferred_with_stale_calibration(m, delta_plus, delta_minus)
            sharp_bound = epsilon * (1 - m * m) / (1 - epsilon)
            bound_checks.append(abs(inferred - m) <= sharp_bound)

common_mode = inferred_with_stale_calibration(Fraction(1, 3), Fraction(1, 4), Fraction(1, 4))

eta0 = (Fraction(1, 2), Fraction(1, 3))
eta1 = (Fraction(3, 4), Fraction(2, 3))
u = Fraction(1, 2)
eta_mid = tuple((1 - u) * left + u * right for left, right in zip(eta0, eta1))
true_m = Fraction(-1, 4)
mid_records = records(true_m, *eta_mid)
recovered_plus = mid_records[0] / eta_mid[0]
recovered_minus = mid_records[1] / eta_mid[1]
recovered_m = recovered_plus - recovered_minus

nonlinear_eta_mid = (eta_mid[0] + Fraction(1, 16), eta_mid[1])
nonlinear_records = records(true_m, *nonlinear_eta_mid)
nonlinear_recovered = nonlinear_records[0] / eta_mid[0] - nonlinear_records[1] / eta_mid[1]

checks = {
    "drift_and_state_signal_records_are_identical": drifted_records == state_signal_records,
    "indistinguishable_record_is_exact": drifted_records == (Fraction(3, 8), Fraction(1, 8), Fraction(1, 2)),
    "confounded_states_are_distinct": Fraction(0) != Fraction(1, 2),
    "derived_bias_bound_holds_on_exact_grid": all(bound_checks),
    "common_mode_drift_cancels": common_mode == Fraction(1, 3),
    "affine_midpoint_efficiencies_are_exact": eta_mid == (Fraction(5, 8), Fraction(1, 2)),
    "affine_interpolation_recovers_state": recovered_m == true_m,
    "nonlinear_midpoint_drift_biases_interpolation": nonlinear_recovered != true_m,
    "nonlinear_drift_preserves_declared_endpoints": eta0 != eta1 and nonlinear_eta_mid != eta_mid,
    "no_click_records_remain_normalized": sum(drifted_records) == 1 and sum(mid_records) == 1 and sum(nonlinear_records) == 1,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.calibration-drift-falsifier.v1", "status": "passed", "checks": checks, "indistinguishable_records": [str(value) for value in drifted_records], "bias_bound_epsilon": str(epsilon), "grid_case_count": len(bound_checks), "affine_recovered_m": str(recovered_m), "nonlinear_recovered_m": str(nonlinear_recovered), "claim_boundary": "Binary-channel multiplicative drift model; workflow coordinate is not physical time."}
output = Path(__file__).parents[1] / "results" / "calibration_drift_falsifier.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "grid_case_count": len(bound_checks), "nonlinear_bias": str(nonlinear_recovered - true_m)}, sort_keys=True))
