import json
from fractions import Fraction as F
from pathlib import Path


def observe(correlation, imbalance):
    return (correlation + imbalance) / (1 + imbalance * correlation)


def invert(observed, imbalance):
    return (observed - imbalance) / (1 - imbalance * observed)


def coherence_vector(records):
    return (
        (records["XX"] - records["YY"]) / 4,
        -(records["XY"] + records["YX"]) / 4,
    )


def residual(records, population_product):
    real, imaginary = coherence_vector(records)
    return real * real + imaginary * imaginary - population_product


true_records = {
    "XX": F(2, 25),
    "YY": F(-1, 25),
    "XY": F(-9, 100),
    "YX": F(-7, 100),
}
population_product = F(1, 400)
imbalances = {
    "XX": F(1, 100),
    "YY": F(-1, 100),
    "XY": F(-1, 100),
    "YX": F(-1, 100),
}

observed_records = {
    setting: observe(true_records[setting], imbalances[setting])
    for setting in true_records
}

# A second plant/sensor explanation: treat the biased packet as the true
# physical correlations and use balanced detectors.
alias_records = {
    setting: observe(observed_records[setting], F(0))
    for setting in observed_records
}

# A known zero-correlation calibration identifies each imbalance exactly.
calibration_records = {
    setting: observe(F(0), imbalances[setting]) for setting in imbalances
}
corrected_records = {
    setting: invert(observed_records[setting], calibration_records[setting])
    for setting in observed_records
}

stale_balanced_correction = {
    setting: invert(observed_records[setting], F(0))
    for setting in observed_records
}

# One setting with affine drift k(t), calibrated at t=0 and t=2 and measured
# at t=1.
k0 = F(-1, 100)
k2 = F(3, 100)
k1 = (k0 + k2) / 2
science_at_t1 = observe(true_records["XX"], k1)
interpolated_k1 = (observe(F(0), k0) + observe(F(0), k2)) / 2

checks = {
    "true_packet_is_on_boundary": residual(true_records, population_product)
    == 0,
    "gain_hostile_has_positive_naive_residual": residual(
        observed_records, population_product
    )
    > 0,
    "balanced_alias_has_identical_observed_packet": alias_records
    == observed_records,
    "balanced_alias_is_physically_npt": residual(alias_records, population_product)
    > 0,
    "zero_correlation_calibration_identifies_gain": calibration_records
    == imbalances,
    "calibration_inversion_recovers_every_true_record": corrected_records
    == true_records,
    "calibration_restores_boundary_residual": residual(
        corrected_records, population_product
    )
    == 0,
    "stale_balanced_calibration_preserves_false_positive": residual(
        stale_balanced_correction, population_product
    )
    > 0,
    "affine_bracketing_recovers_midpoint_gain": interpolated_k1 == k1,
    "affine_bracketing_recovers_midpoint_science_record": invert(
        science_at_t1, interpolated_k1
    )
    == true_records["XX"],
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "naive_residual": str(residual(observed_records, population_product)),
    "corrected_residual": str(residual(corrected_records, population_product)),
    "classification": {
        "defect": "plant correlation and setting-dependent detector imbalance are observationally aliased",
        "repair": "independent zero-correlation excitation makes the nuisance state observable",
        "temporal_gate": "calibration must be simultaneous or transported by a declared gain-dynamics model",
    },
}

output = Path(__file__).parents[1] / "results" / "detector_gain_nuisance_observability.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

