"""Scout weighted Schur bounds for the odd level-44 folded kernel."""

import math
import numpy as np


length = math.log(2.0)
half = length / 2.0
d44 = 2.633783493671972324594303424623756044375
count = 2400
x = (np.arange(count) + 0.5) * half / count
distance = np.abs(x[:, None] - x[None, :])
sum_coordinate = x[:, None] + x[None, :]


def kernel(t):
    result = np.exp(t / 2.0)
    for n in range(1, 44):
        result -= np.exp(-(2 * n + 0.5) * t)
    return result


folded = kernel(sum_coordinate) - kernel(distance)
# B(|x-y|)-B(x+y) = K(x+y)-K(|x-y|).
step = half / count

for name, weight in (
    ("nima_integer_weight", x * np.exp(-7.0 * x**2 - 32.0 * x**4)),
    ("sin_pi_x_over_L", np.sin(np.pi * x / length)),
    ("linear", x),
    ("sinh_half", np.sinh(x / 2.0)),
):
    ratios = step * (folded @ weight) / weight
    print(name)
    print(f"  minimum_ratio={ratios.min():.17g}")
    print(f"  maximum_ratio={ratios.max():.17g}")
    print(f"  reserve={d44-ratios.max():.17g}")
    print(f"  maximizing_x={x[ratios.argmax()]:.17g}")

best = (math.inf, None, None)
for kh_over_pi in np.linspace(0.15, 0.999, 500):
    frequency = kh_over_pi * np.pi / half
    weight = np.sin(frequency * x)
    ratios = step * (folded @ weight) / weight
    maximum = float(ratios.max())
    if maximum < best[0]:
        best = (maximum, kh_over_pi, float(x[ratios.argmax()]))
print("optimized_sine")
print(f"  maximum_ratio={best[0]:.17g}")
print(f"  kh_over_pi={best[1]:.17g}")
print(f"  reserve={d44-best[0]:.17g}")
print(f"  maximizing_x={best[2]:.17g}")
