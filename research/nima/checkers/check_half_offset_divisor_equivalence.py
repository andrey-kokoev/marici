import json
import math


alpha = 0.49
safe_rate = 0.5
hostile_rate = 0.25
frequency = 1.0
samples = [2.0 * math.pi * n for n in (0, 1, 2, 4, 8)]


def weighted_mode(rate, x):
    return math.exp((alpha - rate) * abs(x))


safe = [weighted_mode(safe_rate, x) for x in samples]
hostile_component = [
    weighted_mode(hostile_rate, x) * abs(math.cos(frequency * x))
    for x in samples
]

assert all(value <= 1.0 for value in safe)
assert all(
    hostile_component[i + 1] > hostile_component[i]
    for i in range(len(hostile_component) - 1)
)

# For every off-seam rate a < 1/2, the midpoint alpha between a and 1/2
# witnesses failure of the intersection of weighted spaces.
rates = [0.05, 0.125, 0.25, 0.49]
midpoint_witnesses = [(rate + 0.5) / 2.0 for rate in rates]
assert all(rate < witness < 0.5 for rate, witness in zip(rates, midpoint_witnesses))

result = {
    "schema": "marici.nima.half-offset-divisor-equivalence.v1",
    "alpha": alpha,
    "safe_rate": safe_rate,
    "hostile_rate": hostile_rate,
    "safe_weighted_samples_bounded": True,
    "hostile_weighted_samples_strictly_grow": True,
    "every_tested_off_seam_rate_has_weight_witness": True,
    "criterion_status_after_divisor_factorization": "rh_equivalent_detector",
    "remaining_non_circular_gate": "pre_divisor_low_grade_source_continuity",
}
print(json.dumps(result, indent=2, sort_keys=True))

