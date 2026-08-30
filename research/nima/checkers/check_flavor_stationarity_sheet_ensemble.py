"""Test the t-purity stationarity curve on all viable flavor sheets."""

import contextlib
import glob
import importlib.util
import io
import json
import math
import sys
from pathlib import Path

import numpy as np

flavor_root = Path(__file__).parents[2] / "flavor"
sys.path.insert(0, str(flavor_root / "checkers"))
import wp7_ensemble as wp7

base_path = Path(__file__).with_name("check_flavor_t_stationarity_robustness.py")
spec = importlib.util.spec_from_file_location("stationarity", base_path)
stationarity = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    try:
        spec.loader.exec_module(stationarity)
    except SystemExit as exc:
        if exc.code:
            raise


def predict(values):
    p = {
        "yu": values[0], "yc": values[1], "yt": values[2],
        "yd": values[3], "ys": values[4], "yb": values[5],
        "s12": values[6], "delta": math.radians(values[14]),
    }
    return stationarity.maximize(p)


records = []
for path in sorted(glob.glob(str(flavor_root / "results" / "wp15b_dense_orbit*.json"))):
    data = json.load(open(path, encoding="utf-8"))
    for half in data["s3_orbits"]:
        for member_result in half["member_results"]:
            member = tuple(member_result["member"])
            for minimum in member_result["viable_minima"]:
                if minimum["chi2"] >= 4:
                    continue
                phase_edge = minimum["phase_edge"]
                theta = np.array(minimum["log_mags"] + [minimum["phi"]])
                yu, yd = wp7.build_texture(
                    member[0], member[1], phase_edge[0],
                    (phase_edge[1], phase_edge[2]), theta,
                )
                values = wp7.observables17(yu, yd)
                if not np.all(np.isfinite(values)):
                    continue
                observed = float(values[7] / values[8])
                predicted = predict(values)
                records.append((observed, predicted, float(values[14])))

observed = np.array([row[0] for row in records])
predicted = np.array([row[1] for row in records])
central_prediction = stationarity.maximize(stationarity.CENTERS)
rmse_curve = float(np.sqrt(np.mean((observed - predicted) ** 2)))
rmse_constant = float(np.sqrt(np.mean((observed - central_prediction) ** 2)))
corr = float(np.corrcoef(observed, predicted)[0, 1])
residual_sigma = (observed - predicted) / stationarity.sigma_r if hasattr(stationarity, "sigma_r") else (observed - predicted) / 0.0027258502522580085

checks = {
    "all_1210_viable_sheets_recovered": len(records) == 1210,
    "curve_is_worse_than_constant_by_factor_five": rmse_curve > 5 * rmse_constant,
    "no_sheet_within_one_sigma": float(np.mean(np.abs(residual_sigma) < 1)) == 0,
    "predicted_and_observed_ranges_are_disjoint": float(predicted.max()) < float(observed.min()),
}
report = {
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "sheet_count": len(records),
    "rmse_stationarity_curve": rmse_curve,
    "rmse_constant_central_stationary_point": rmse_constant,
    "rmse_ratio": rmse_curve / rmse_constant,
    "correlation_observed_predicted": corr,
    "fraction_within_one_sigma": float(np.mean(np.abs(residual_sigma) < 1)),
    "observed_ratio_range": [float(observed.min()), float(observed.max())],
    "predicted_ratio_range": [float(predicted.min()), float(predicted.max())],
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
