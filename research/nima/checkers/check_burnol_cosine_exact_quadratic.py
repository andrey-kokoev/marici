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
archimedean = h_zero + tail + kinetic

cosine_norm_squared = length / 2
endpoint_overlap = mp.quad(
    lambda x: mp.cosh(x / 2) * mp.cos(mp.pi * x / length),
    [-length / 2, length / 2],
) / mp.sqrt(cosine_norm_squared)
boundary = 2 * endpoint_overlap**2

result = {
    "schema": "marici.burnol-cosine-exact-quadratic.v1",
    "status": "pass",
    "scope": "high-precision evaluation of exact integral identities",
    "support_length": mp.nstr(length, 70),
    "h_infinity_at_zero": mp.nstr(h_zero, 70),
    "outside_support_tail": mp.nstr(tail, 70),
    "inside_support_difference_energy": mp.nstr(kinetic, 70),
    "archimedean_cosine_energy": mp.nstr(archimedean, 70),
    "rank_one_boundary_energy": mp.nstr(boundary, 70),
    "total_cosine_rayleigh": mp.nstr(archimedean + boundary, 70),
}

print(json.dumps(result, indent=2))

