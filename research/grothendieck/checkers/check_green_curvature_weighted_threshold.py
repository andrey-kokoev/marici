import math


ROOTS = (0.2659956819935979, 1.6705589357127293, 5.063445382293672)


def polynomial(x: float) -> float:
    return 16 * x**4 - 112 * x**3 + 164 * x**2 - 36 * x


def weighted_readout(u: float):
    total_weight = 0.0
    first_moment = 0.0
    direct = 0.0
    for n in range(1, 30):
        x = math.pi * n * n * math.exp(2 * u)
        carrier = math.exp(u / 2 - x)
        weight = 16 * carrier * x * (x - ROOTS[0]) * (x - ROOTS[1])
        total_weight += weight
        first_moment += weight * x
        direct += carrier * polynomial(x)
    mean = first_moment / total_weight
    factored = total_weight * (mean - ROOTS[2])
    assert total_weight > 0
    assert abs(direct - factored) < 1e-10 * max(1.0, abs(direct))
    return mean, direct


previous = None
for k in range(0, 401):
    u = k / 400
    mean, _ = weighted_readout(u)
    if previous is not None:
        assert mean > previous
    previous = mean

print("aggregate_sign=positive_weighted_mean_minus_fixed_threshold")
print("threshold=largest_cubic_root")
print("monotonicity_scout=401_points_passed")
print("scope=monotonicity_not_certified_by_scout")
