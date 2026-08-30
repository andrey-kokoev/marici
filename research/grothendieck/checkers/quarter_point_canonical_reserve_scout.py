"""Scout basis-invariant quarter-point Hausdorff coercivity reserves."""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
import mpmath as mp


result_path = (
    Path(__file__).parents[1] / "results" / "quarter-point-order-four-interval.json"
)
data = json.loads(result_path.read_text(encoding="utf-8"))
boxes = data["moments_A0_through_A9"]
a = np.asarray([(float(lo) + float(hi)) / 2.0 for lo, hi in boxes])
m = a / 4.0 ** np.arange(len(a))


def matrices(order):
    size = order + 1
    ordinary = np.fromfunction(
        lambda i, j: m[(i + j).astype(int)], (size, size), dtype=int
    )
    lower = np.fromfunction(
        lambda i, j: m[(i + j + 1).astype(int)], (size, size), dtype=int
    )
    upper = ordinary - lower
    reference_ordinary = np.fromfunction(
        lambda i, j: 1.0 / (i + j + 1.0), (size, size)
    )
    reference_lower = np.fromfunction(
        lambda i, j: 1.0 / (i + j + 2.0), (size, size)
    )
    reference_upper = np.fromfunction(
        lambda i, j: 1.0 / ((i + j + 1.0) * (i + j + 2.0)),
        (size, size),
    )
    return (
        (ordinary, reference_ordinary),
        (lower, reference_lower),
        (upper, reference_upper),
    )


for order in range(5):
    reserves = [float(eigh(form, reference, eigvals_only=True)[0]) for form, reference in matrices(order)]
    print(
        f"order={order} ordinary={reserves[0]:.17g} "
        f"x_localizer={reserves[1]:.17g} "
        f"one_minus_x_localizer={reserves[2]:.17g} "
        f"minimum={min(reserves):.17g}"
    )

mp.mp.dps = 100
a_mp = [
    (mp.mpf(lo) + mp.mpf(hi)) / 2 for lo, hi in boxes
]
m_mp = [value / mp.mpf(4) ** index for index, value in enumerate(a_mp)]


def smallest_generalized_mp(form, reference):
    chol = mp.cholesky(reference)
    inverse = chol**-1
    reduced = inverse * form * inverse.T
    return mp.eigsy(reduced, eigvals_only=True)[0]


print("high_precision")
for order in range(5):
    size = order + 1
    ordinary = mp.matrix(size, size)
    lower = mp.matrix(size, size)
    upper = mp.matrix(size, size)
    r0 = mp.matrix(size, size)
    rx = mp.matrix(size, size)
    r1x = mp.matrix(size, size)
    for i in range(size):
        for j in range(size):
            degree = i + j
            ordinary[i, j] = m_mp[degree]
            lower[i, j] = m_mp[degree + 1]
            upper[i, j] = m_mp[degree] - m_mp[degree + 1]
            r0[i, j] = 1 / mp.mpf(degree + 1)
            rx[i, j] = 1 / mp.mpf(degree + 2)
            r1x[i, j] = 1 / (mp.mpf(degree + 1) * mp.mpf(degree + 2))
    reserves = (
        smallest_generalized_mp(ordinary, r0),
        smallest_generalized_mp(lower, rx),
        smallest_generalized_mp(upper, r1x),
    )
    print(
        f"order={order} ordinary={mp.nstr(reserves[0], 24)} "
        f"x_localizer={mp.nstr(reserves[1], 24)} "
        f"one_minus_x_localizer={mp.nstr(reserves[2], 24)} "
        f"minimum={mp.nstr(min(reserves), 24)}"
    )
