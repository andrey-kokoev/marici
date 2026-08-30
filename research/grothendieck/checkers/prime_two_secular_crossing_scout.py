"""Scout the source-fixed secular scalar around the first positive level."""

import math
import numpy as np
from numpy.polynomial.legendre import leggauss


LENGTH = math.log(2.0)
H_INFINITY_ZERO = (
    -math.log(math.pi)
    - 0.577215664901532860606512090082402431
    - math.pi / 2.0
    - 3.0 * math.log(2.0)
)


def rate(n):
    return 2.0 * n + 0.5


def d_level(level):
    return H_INFINITY_ZERO + sum(2.0 / rate(n) for n in range(level))


def kernel(level, t):
    result = np.exp(t / 2.0)
    for n in range(1, level):
        result -= np.exp(-rate(n) * t)
    return result


def secular(level, order):
    nodes, weights = leggauss(order)
    x = LENGTH * (nodes + 1.0) / 2.0
    weights = LENGTH * weights / 2.0
    root_weights = np.sqrt(weights)
    c = (5.0 + 4.0 ** (-(level - 1))) / (3.0 * math.sqrt(2.0))
    b = c - kernel(level, np.abs(x[:, None] - x[None, :]))
    symmetric_b = root_weights[:, None] * b * root_weights[None, :]
    a = d_level(level) * np.eye(order) - symmetric_b
    one = root_weights
    solved = np.linalg.solve(a, one)
    return 1.0 + c * float(one @ solved)


orders = (512, 768, 1024, 1280)
for level in (43, 44, 45):
    values = [secular(level, order) for order in orders]
    # Leading diagonal-cusp error is empirically O(order^-2).
    coordinate = np.asarray([1.0 / order**2 for order in orders])
    fit = np.polyfit(coordinate, np.asarray(values), 2)
    print(f"level={level} d={d_level(level):.17g}")
    for order, value in zip(orders, values):
        print(f"  order={order} secular={value:.17g}")
    print(f"  extrapolated={fit[-1]:.17g}")
