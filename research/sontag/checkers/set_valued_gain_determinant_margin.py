import json
from fractions import Fraction as F
from pathlib import Path


def observe(correlation, imbalance):
    return (correlation + imbalance) / (1 + imbalance * correlation)


def invert(observed, imbalance):
    return (observed - imbalance) / (1 - imbalance * observed)


def corrected_interval(observed_interval, gain_interval):
    y_low, y_high = observed_interval
    k_low, k_high = gain_interval
    return invert(y_low, k_high), invert(y_high, k_low)


def linear_difference(left, right, scale):
    return (
        (left[0] - right[1]) / scale,
        (left[1] - right[0]) / scale,
    )


def negative_sum(left, right, scale):
    return (
        -(left[1] + right[1]) / scale,
        -(left[0] + right[0]) / scale,
    )


def distance_zero(interval):
    low, high = interval
    if low <= 0 <= high:
        return F(0)
    return min(abs(low), abs(high))


def robust_margin(observed, gain_sets, population_product):
    correlations = {
        setting: corrected_interval((value, value), gain_sets[setting])
        for setting, value in observed.items()
    }
    real_interval = linear_difference(correlations["XX"], correlations["YY"], F(4))
    imaginary_interval = negative_sum(
        correlations["XY"], correlations["YX"], F(4)
    )
    margin = (
        distance_zero(real_interval) ** 2
        + distance_zero(imaginary_interval) ** 2
        - population_product
    )
    return margin, correlations, real_interval, imaginary_interval


boundary_records = {
    "XX": F(2, 25),
    "YY": F(-1, 25),
    "XY": F(-9, 100),
    "YX": F(-7, 100),
}
boundary_gains = {
    "XX": F(1, 100),
    "YY": F(-1, 100),
    "XY": F(-1, 100),
    "YX": F(-1, 100),
}
boundary_observed = {
    setting: observe(boundary_records[setting], boundary_gains[setting])
    for setting in boundary_records
}
gain_radius = F(1, 500)
boundary_gain_sets = {
    setting: (gain - gain_radius, gain + gain_radius)
    for setting, gain in boundary_gains.items()
}
boundary_margin, _, boundary_real, boundary_imaginary = robust_margin(
    boundary_observed, boundary_gain_sets, F(1, 400)
)

strong_records = {
    "XX": F(1, 5),
    "YY": F(-1, 5),
    "XY": F(-1, 5),
    "YX": F(-1, 5),
}
strong_gains = {
    "XX": F(1, 100),
    "YY": F(-1, 100),
    "XY": F(1, 100),
    "YX": F(-1, 100),
}
strong_observed = {
    setting: observe(strong_records[setting], strong_gains[setting])
    for setting in strong_records
}
strong_gain_sets = {
    setting: (gain - gain_radius, gain + gain_radius)
    for setting, gain in strong_gains.items()
}
strong_margin, _, strong_real, strong_imaginary = robust_margin(
    strong_observed, strong_gain_sets, F(1, 200)
)

y = F(1, 5)
k = F(1, 100)
dy_numerator = 1 - k * k
dk_numerator = y * y - 1

checks = {
    "inverse_increases_with_observed_record": dy_numerator > 0,
    "inverse_decreases_with_gain": dk_numerator < 0,
    "boundary_true_gain_is_inside_every_set": all(
        low <= boundary_gains[setting] <= high
        for setting, (low, high) in boundary_gain_sets.items()
    ),
    "boundary_robust_margin_withholds_claim": boundary_margin <= 0,
    "boundary_real_interval_contains_true_value": boundary_real[0]
    <= F(3, 100)
    <= boundary_real[1],
    "boundary_imaginary_interval_contains_true_value": boundary_imaginary[0]
    <= F(1, 25)
    <= boundary_imaginary[1],
    "strong_true_gain_is_inside_every_set": all(
        low <= strong_gains[setting] <= high
        for setting, (low, high) in strong_gain_sets.items()
    ),
    "strong_real_interval_contains_true_value": strong_real[0]
    <= F(1, 10)
    <= strong_real[1],
    "strong_imaginary_interval_contains_true_value": strong_imaginary[0]
    <= F(1, 10)
    <= strong_imaginary[1],
    "strong_robust_margin_certifies_npt": strong_margin > 0,
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "gain_radius": str(gain_radius),
    "boundary_margin": str(boundary_margin),
    "strong_npt_margin": str(strong_margin),
    "classification": {
        "observer": "set-valued nuisance-state estimate transported through the exact nonlinear inverse",
        "decision": "strictly positive worst-case determinant margin",
        "residual": "rectangular gain sets ignore cross-setting covariance and may be conservative",
    },
}

output = Path(__file__).parents[1] / "results" / "set_valued_gain_determinant_margin.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

