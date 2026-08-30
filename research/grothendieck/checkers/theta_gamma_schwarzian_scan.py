"""Hostile scan of the exact completed-gamma Schwarzian baseline.

This is reconnaissance, not interval certification.  Digamma derivatives are
evaluated by recurrence to a large argument followed by a differentiated
Bernoulli expansion.
"""

import json
import math
from pathlib import Path


BERNOULLI_EVEN = [
    1.0 / 6.0,
    -1.0 / 30.0,
    1.0 / 42.0,
    -1.0 / 30.0,
    5.0 / 66.0,
    -691.0 / 2730.0,
    7.0 / 6.0,
    -3617.0 / 510.0,
]


def falling(power, order):
    value = 1.0
    for index in range(order):
        value *= power - index
    return value


def derivative_power(z, power, order):
    return falling(power, order) * z ** (power - order)


def digamma_derivative(z, order, shift_target=24.0):
    """Return psi^(order)(z), for order 0..3 and positive z."""
    shift = max(0, math.ceil(shift_target - z))
    y = z + shift

    # psi(y) = log y - 1/(2y) - sum B_2k/(2k y^(2k)).
    if order == 0:
        asymptotic = math.log(y)
    else:
        asymptotic = ((-1) ** (order - 1)) * math.factorial(order - 1) / y**order
    asymptotic -= 0.5 * derivative_power(y, -1, order)
    for k, bernoulli in enumerate(BERNOULLI_EVEN, start=1):
        asymptotic -= (
            bernoulli
            / (2 * k)
            * derivative_power(y, -2 * k, order)
        )

    # psi(z) = psi(z+n) - sum_{j=0}^{n-1} 1/(z+j), differentiated.
    recurrence = math.fsum(
        derivative_power(z + index, -1, order) for index in range(shift)
    )
    return asymptotic - recurrence


def evaluate(x):
    r = math.sqrt(x)
    s = 0.5 + r
    z = s / 2.0

    g = 0.5 * (digamma_derivative(z, 0) - math.log(math.pi))
    g1s = 0.25 * digamma_derivative(z, 1)
    g2s = 0.125 * digamma_derivative(z, 2)
    g3s = 0.0625 * digamma_derivative(z, 3)

    gx = g1s / (2 * r)
    gxx = g2s / (4 * r**2) - g1s / (4 * r**3)
    gxxx = (
        g3s / (8 * r**3)
        - 3 * g2s / (8 * r**4)
        + 3 * g1s / (8 * r**5)
    )

    a = r / 2 - 1 / (8 * r)
    a1 = 1 / (4 * r) + 1 / (16 * r**3)
    a2 = -1 / (8 * r**3) - 3 / (32 * r**5)
    a3 = 3 / (16 * r**5) + 15 / (64 * r**7)

    h1 = a1 * g + a * gx
    h2 = a2 * g + 2 * a1 * gx + a * gxx
    h3 = a3 * g + 3 * a2 * gx + 3 * a1 * gxx + a * gxxx
    numerator = 2 * h1 * h3 - 3 * h2 * h2
    return {
        "x": x,
        "s": s,
        "H_gamma_prime": h1,
        "H_gamma_second": h2,
        "H_gamma_third": h3,
        "schwarzian_numerator": numerator,
        "passes": h1 > 0 and numerator >= 0,
    }


def scan_points():
    points = [0.250001 + index * (0.25 - 0.000001) / 249 for index in range(250)]
    log_start = math.log(0.5)
    log_end = math.log(1.0e8)
    points.extend(
        math.exp(log_start + index * (log_end - log_start) / 1999)
        for index in range(2000)
    )
    return sorted(set(points))


rows = [evaluate(x) for x in scan_points()]
failures = [row for row in rows if not row["passes"]]


def last_nonpositive_window(field):
    bad_indices = [index for index, row in enumerate(rows) if row[field] <= 0]
    if not bad_indices:
        return None
    index = bad_indices[-1]
    return {
        "last_nonpositive": rows[index],
        "next_sample": rows[index + 1] if index + 1 < len(rows) else None,
    }


result = {
    "target": "exact completed-gamma baseline has H_gamma' > 0 and nonnegative Schwarzian numerator",
    "method": "digamma recurrence to >=24 plus eight-term differentiated Bernoulli expansion",
    "sample_count": len(rows),
    "domain": [rows[0]["x"], rows[-1]["x"]],
    "all_samples_pass": not failures,
    "first_failure": failures[0] if failures else None,
    "smallest_numerator_row": min(rows, key=lambda row: row["schwarzian_numerator"]),
    "smallest_H_gamma_prime_row": min(rows, key=lambda row: row["H_gamma_prime"]),
    "last_nonpositive_H_gamma_prime_window": last_nonpositive_window("H_gamma_prime"),
    "last_nonpositive_schwarzian_window": last_nonpositive_window("schwarzian_numerator"),
    "selected_rows": [
        evaluate(x) for x in [0.250001, 0.26, 0.5, 1.0, 10.0, 100.0, 1.0e4, 1.0e8]
    ],
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-gamma-schwarzian-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
