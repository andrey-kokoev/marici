"""High-precision real-space audit of the prime-two cosine trial mode."""

import json

import mpmath as mp


mp.mp.dps = 80
length = mp.log(2)
h_zero = -mp.log(mp.pi) + mp.digamma(mp.mpf(1) / 4)


def levy_weight(distance):
    return mp.exp(distance / 2) / mp.sinh(distance)


def normalized_cosine_correlation(distance):
    angle = mp.pi * distance / length
    return (1 - distance / length) * mp.cos(angle) + mp.sin(angle) / mp.pi


tail = mp.quad(levy_weight, [length, mp.inf])
kinetic = mp.quad(
    lambda distance: levy_weight(distance)
    * (1 - normalized_cosine_correlation(distance)),
    [0, length],
)
universal_log_kinetic = mp.quad(
    lambda distance: (1 - normalized_cosine_correlation(distance)) / distance,
    [0, length],
)
archimedean = h_zero + tail + kinetic

cosine_norm_squared = length / 2
endpoint_overlap = mp.quad(
    lambda x: mp.cosh(x / 2) * mp.cos(mp.pi * x / length),
    [-length / 2, length / 2],
) / mp.sqrt(cosine_norm_squared)
boundary = 2 * endpoint_overlap**2

gamma_levels = []
gamma_cumulative = mp.mpf(0)
for index in range(32):
    rate = 2 * index + mp.mpf(1) / 2
    level_energy = 2 * mp.quad(
        lambda distance: mp.exp(-rate * distance)
        * (1 - normalized_cosine_correlation(distance)),
        [0, length],
    ) + 2 * mp.exp(-rate * length) / rate
    gamma_cumulative += level_energy
    gamma_levels.append(
        {
            "index": index,
            "rate": mp.nstr(rate, 20),
            "level_energy": mp.nstr(level_energy, 40),
            "partial_total_with_h0_and_boundary": mp.nstr(
                h_zero + boundary + gamma_cumulative, 40
            ),
        }
    )

result = {
    "schema": "marici.burnol-cosine-exact-quadratic.v1",
    "status": "pass",
    "scope": "high-precision evaluation of exact integral identities",
    "support_length": mp.nstr(length, 70),
    "h_infinity_at_zero": mp.nstr(h_zero, 70),
    "outside_support_tail": mp.nstr(tail, 70),
    "inside_support_difference_energy": mp.nstr(kinetic, 70),
    "universal_one_over_r_difference_energy": mp.nstr(
        universal_log_kinetic, 70
    ),
    "archimedean_cosine_energy": mp.nstr(archimedean, 70),
    "rank_one_boundary_energy": mp.nstr(boundary, 70),
    "total_cosine_rayleigh": mp.nstr(archimedean + boundary, 70),
    "one_over_r_comparison_total_lower_bound": mp.nstr(
        h_zero + tail + universal_log_kinetic + boundary, 70
    ),
    "first_32_gamma_level_partial_sums": gamma_levels,
}

print(json.dumps(result, indent=2))
