"""Scout center jets of the principal odd eigenfunction of the T44 B-kernel."""

import math
import numpy as np
from scipy.linalg import eigh


LENGTH = math.log(2.0)
HALF = LENGTH / 2.0


def kernel(t):
    result = np.exp(t / 2.0)
    for n in range(1, 44):
        result -= np.exp(-(2 * n + 0.5) * t)
    return result


for count in (400, 800, 1200):
    step = HALF / count
    x = (np.arange(count) + 0.5) * step
    folded = kernel(x[:, None] + x[None, :]) - kernel(
        np.abs(x[:, None] - x[None, :])
    )
    # Midpoint Nyström matrix is symmetric because the weights are uniform.
    values, vectors = eigh(
        step * folded,
        subset_by_index=(count - 1, count - 1),
        driver="evr",
    )
    vector = vectors[:, 0]
    if vector[0] < 0.0:
        vector = -vector
    vector /= vector[0] / x[0]
    log_shape = np.log(vector / x)
    print(f"count={count} lambda_odd={values[0]:.17g}")
    for radius in (0.03, 0.05, 0.08, 0.12, 0.18):
        mask = x <= radius
        z = x[mask] ** 2
        # Include through x^8 so the first two coefficients are not forced to
        # absorb all higher center jets.
        design = np.column_stack((np.ones_like(z), z, z**2, z**3, z**4))
        coefficients = np.linalg.lstsq(design, log_shape[mask], rcond=None)[0]
        print(
            f"  radius={radius:.2f} log_c2={coefficients[1]:.12g} "
            f"log_c4={coefficients[2]:.12g} log_c6={coefficients[3]:.12g}"
        )
