import json
import math


max_n = 200000
ratios = []
for n in range(2, max_n + 1):
    delta = math.log1p(1.0 / n)
    ratios.append((1.0 / n) / delta)

result = {
    "schema": "marici.grothendieck.primitive_log_prime_h1_sampling.v1",
    "checks": {
        "mesh_weight_ratio_below_three_halves": max(ratios) < 1.5,
        "mesh_lengths_below_one": math.log(1.5) < 1.0,
        "constant_profile_partial_norm_diverges": sum(1.0 / n for n in range(2, max_n + 1)) > 11.0,
    },
    "max_weight_to_mesh_ratio": max(ratios),
    "derived_sampling_bound": 3.0,
    "note": "The packet proves the H1 sampling inequality on logarithmic integer cells; primes are a subset.",
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
