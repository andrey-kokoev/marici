"""High-precision reconnaissance for the theta mean--variance boundary gate.

This is not interval-certified.  It evaluates the completed Xi function directly
and scans

    G(x) = (1+4x^2)m(x) - x(1-4x^2)m'(x),
    m(x) = Xi'(x)/Xi(x),

on 0 < x < 1/2.  Positive output is diagnostic only; a negative value at
sufficient precision would be a candidate falsifier requiring certification.
"""

import json
from pathlib import Path
import sys

try:
    import mpmath as mp
except ModuleNotFoundError:
    vendored = Path(__file__).parents[2] / "flavor" / ".venv" / "Lib" / "site-packages"
    sys.path.insert(0, str(vendored))
    import mpmath as mp

mp.mp.dps = 80


def xi_centered(x):
    s = mp.mpf("0.5") + x
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def gate(x):
    X = xi_centered(x)
    X1 = mp.diff(xi_centered, x, 1)
    X2 = mp.diff(xi_centered, x, 2)
    m = X1 / X
    mp1 = X2 / X - m * m
    return (1 + 4 * x * x) * m - x * (1 - 4 * x * x) * mp1, m, mp1


# Logarithmic near-center mesh plus a uniform mesh through the compact interval.
points = set()
for j in range(1, 121):
    exponent = mp.mpf(-12) + mp.mpf(12) * j / 120
    points.add(mp.power(10, exponent) * mp.mpf("0.49"))
for j in range(1, 401):
    points.add(mp.mpf("0.5") * j / 401)
points = sorted(x for x in points if 0 < x < mp.mpf("0.5"))

records = []
minimum = None
for x in points:
    G, m, mp1 = gate(x)
    item = (G, x, m, mp1)
    if minimum is None or G < minimum[0]:
        minimum = item
    records.append(item)

Gmin, xmin, mmin, mp1min = minimum

# Also sample the branch-point coefficient G(x)/x^3.
small_points = [mp.mpf(10) ** (-k) for k in range(2, 9)]
small_ratios = []
for x in small_points:
    G, _, _ = gate(x)
    small_ratios.append((x, G / x**3))

result = {
    "precision_decimal_digits": mp.mp.dps,
    "point_count": len(points),
    "minimum_G": mp.nstr(Gmin, 50),
    "minimum_x": mp.nstr(xmin, 50),
    "m_at_minimum": mp.nstr(mmin, 50),
    "m_prime_at_minimum": mp.nstr(mp1min, 50),
    "all_sampled_positive": bool(Gmin > 0),
    "small_x_G_over_x_cubed": [
        {"x": mp.nstr(x, 20), "ratio": mp.nstr(ratio, 50)}
        for x, ratio in small_ratios
    ],
    "interval_certified": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "xi-boundary-mean-variance-scout.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
