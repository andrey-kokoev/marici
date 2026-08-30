import json
import math


decay_rate = 0.25
weight = 0.49
centers = [4.0, 8.0, 16.0, 32.0]
observation_radius = 2.0
profile_radius = 1.0


def profile(x):
    return max(0.0, 1.0 - abs(x))


def defect(x, center):
    return math.exp(-decay_rate * center) * profile(x - center)


local_grid = [i / 4.0 for i in range(-8, 9)]
local_maxima = [max(abs(defect(x, center)) for x in local_grid) for center in centers]
weighted_peaks = [
    math.exp(weight * center) * abs(defect(center, center)) for center in centers
]

assert all(center - profile_radius > observation_radius for center in centers)
assert local_maxima == [0.0] * len(centers)
assert all(
    weighted_peaks[i + 1] > weighted_peaks[i]
    for i in range(len(weighted_peaks) - 1)
)
assert weighted_peaks[-1] > 2000.0

result = {
    "schema": "marici.nima.low-grade-translated-defect.v1",
    "decay_rate": decay_rate,
    "weight": weight,
    "centers": centers,
    "fixed_window_observations": local_maxima,
    "weighted_peaks": weighted_peaks,
    "all_local_observations_zero": True,
    "weighted_norms_strictly_grow": True,
    "local_bonding_controls_half_offset_topology": False,
    "required_successor": "source_authorized_global_tightness_or_weighted_energy",
}
print(json.dumps(result, indent=2, sort_keys=True))

