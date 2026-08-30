import itertools
import json
from fractions import Fraction as F
from pathlib import Path


settings = ("XX", "YY", "XY", "YX")
signs = {"XX": 1, "YY": -1, "XY": 1, "YX": -1}
theta = F(3, 100)
delta = F(1, 100)


def shared_vector(mode):
    return {setting: signs[setting] * mode for setting in settings}


def adjusted(gains):
    return {setting: signs[setting] * gains[setting] for setting in settings}


def contrasts(gains):
    values = adjusted(gains)
    anchor = values["XX"]
    return tuple(values[setting] - anchor for setting in settings[1:])


nominal = shared_vector(theta)
omitted_hostiles = {}
for omitted in settings:
    hostile = dict(nominal)
    hostile[omitted] += delta
    measured = tuple(setting for setting in settings if setting != omitted)
    omitted_hostiles[omitted] = {
        "hostile": hostile,
        "measured": measured,
        "matches_nominal_on_measured": all(
            hostile[setting] == nominal[setting] for setting in measured
        ),
        "violates_full_model": contrasts(hostile) != (F(0), F(0), F(0)),
    }


def signed_interval(interval, sign):
    low, high = interval
    if sign == 1:
        return low, high
    return -high, -low


def common_mode_intersection(intervals):
    adjusted_intervals = [
        signed_interval(intervals[setting], signs[setting])
        for setting in settings
    ]
    low = max(interval[0] for interval in adjusted_intervals)
    high = min(interval[1] for interval in adjusted_intervals)
    return low, high


radius = F(1, 500)
compatible_intervals = {
    setting: (nominal[setting] - radius, nominal[setting] + radius)
    for setting in settings
}
incompatible_intervals = dict(compatible_intervals)
incompatible_intervals["YX"] = (
    nominal["YX"] + F(1, 100),
    nominal["YX"] + F(3, 250),
)
compatible_intersection = common_mode_intersection(compatible_intervals)
incompatible_intersection = common_mode_intersection(incompatible_intervals)

checks = {
    "nominal_shared_mode_has_zero_contrasts": contrasts(nominal)
    == (F(0), F(0), F(0)),
    "three_independent_contrasts_are_declared": len(contrasts(nominal)) == 3,
    "every_omitted_setting_has_an_indistinguishable_hostile": all(
        item["matches_nominal_on_measured"] for item in omitted_hostiles.values()
    ),
    "every_omitted_setting_hostile_violates_full_model": all(
        item["violates_full_model"] for item in omitted_hostiles.values()
    ),
    "all_four_records_detect_each_single_setting_deviation": all(
        contrasts(item["hostile"]) != (F(0), F(0), F(0))
        for item in omitted_hostiles.values()
    ),
    "compatible_intervals_have_nonempty_common_mode": compatible_intersection[0]
    <= compatible_intersection[1],
    "compatible_intersection_contains_true_mode": compatible_intersection[0]
    <= theta
    <= compatible_intersection[1],
    "incompatible_intervals_reject_shared_mode": incompatible_intersection[0]
    > incompatible_intersection[1],
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "contrast_rank": 3,
    "minimum_direct_setting_records": 4,
    "compatible_theta_interval": [str(value) for value in compatible_intersection],
    "incompatible_theta_intersection": [
        str(value) for value in incompatible_intersection
    ],
    "classification": {
        "necessity": "any omitted setting supports an undetectable localized model violation",
        "sufficiency": "four exact zero-correlation records expose all three transverse contrasts",
        "bounded_test": "shared-mode compatibility is nonempty intersection of sign-adjusted calibration intervals",
    },
}

output = Path(__file__).parents[1] / "results" / "shared_gain_mode_falsification.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

