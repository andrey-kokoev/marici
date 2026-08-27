import itertools
import json
from fractions import Fraction as F
from pathlib import Path


def observe(correlation, imbalance):
    return (correlation + imbalance) / (1 + imbalance * correlation)


def invert(observed, imbalance):
    return (observed - imbalance) / (1 - imbalance * observed)


def norm_squared(records):
    real = (records["XX"] - records["YY"]) / 4
    imaginary = -(records["XY"] + records["YX"]) / 4
    return real * real + imaginary * imaginary


true_records = {
    "XX": F(1, 25),
    "YY": F(-1, 25),
    "XY": F(-3, 50),
    "YX": F(-3, 50),
}
population_product = F(1, 1000)
theta = F(3, 100)
signs = {"XX": 1, "YY": -1, "XY": 1, "YX": -1}


def gain_vector(mode):
    return {setting: signs[setting] * mode for setting in signs}


actual_gains = gain_vector(theta)
observed = {
    setting: observe(true_records[setting], actual_gains[setting])
    for setting in true_records
}

coupled_gain_vectors = [gain_vector(-theta), gain_vector(theta)]
coupled_corrected = [
    {
        setting: invert(observed[setting], gains[setting])
        for setting in observed
    }
    for gains in coupled_gain_vectors
]
coupled_norms = [norm_squared(records) for records in coupled_corrected]

settings = tuple(true_records)
box_gain_vectors = []
for choices in itertools.product((-theta, theta), repeat=4):
    box_gain_vectors.append(dict(zip(settings, choices)))
box_corrected = [
    {
        setting: invert(observed[setting], gains[setting])
        for setting in observed
    }
    for gains in box_gain_vectors
]
box_norms = [norm_squared(records) for records in box_corrected]

coupled_margin = min(coupled_norms) - population_product
box_margin = min(box_norms) - population_product
reachable_box_vectors = {
    tuple(gains[setting] for setting in settings) for gains in coupled_gain_vectors
}
all_box_vectors = {
    tuple(gains[setting] for setting in settings) for gains in box_gain_vectors
}

checks = {
    "true_coherence_norm_is_thirteen_over_ten_thousand": norm_squared(
        true_records
    )
    == F(13, 10000),
    "true_margin_is_positive": norm_squared(true_records) - population_product
    == F(3, 10000),
    "coupled_reachable_set_has_two_gain_vectors": len(reachable_box_vectors) == 2,
    "cartesian_projection_box_has_sixteen_vectors": len(all_box_vectors) == 16,
    "box_adds_fourteen_unreachable_vectors": len(
        all_box_vectors - reachable_box_vectors
    )
    == 14,
    "actual_gain_vector_is_coupled_reachable": tuple(
        actual_gains[setting] for setting in settings
    )
    in reachable_box_vectors,
    "coupled_worst_case_norm_retains_true_norm": min(coupled_norms)
    == F(13, 10000),
    "coupled_margin_certifies_npt": coupled_margin == F(3, 10000),
    "box_contains_subboundary_spurious_reconstruction": min(box_norms)
    < population_product,
    "box_margin_withholds_certification": box_margin < 0,
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "coupled_norms": [str(value) for value in coupled_norms],
    "coupled_margin": str(coupled_margin),
    "box_minimum_norm": str(min(box_norms)),
    "box_margin": str(box_margin),
    "classification": {
        "coupled_set": "source-derived two-state shared gain mode",
        "box": "Cartesian product of identical per-setting marginals",
        "result": "forgetting covariance changes a positive robust certificate into an inconclusive one",
    },
}

output = Path(__file__).parents[1] / "results" / "coupled_gain_reachability.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

