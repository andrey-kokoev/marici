import json
import math


def phi(u):
    total = 0.0
    for n in range(1, 30):
        x = math.pi * n * n * math.exp(2.0 * u)
        total += math.exp(u / 2.0) * (4.0 * x * x - 6.0 * x) * math.exp(-x)
    return total


def rho(d, y, panels=60000):
    endpoint = 5.0
    h = endpoint / panels
    total = 0.0
    for j in range(panels + 1):
        v = j * h
        value = 2.0 * phi(v + d) * phi(v) * math.sinh(y * (2.0 * v + d))
        weight = 1 if j in (0, panels) else 4 if j % 2 else 2
        total += weight * value
    return total * h / 3.0


y = 0.2
h = 0.001
values = [rho(j * h, y) for j in range(4)]
origin_curvature = (2.0 * values[0] - 5.0 * values[1] + 4.0 * values[2] - values[3]) / (h * h)

result = {
    "schema": "marici.grothendieck.theta_separation_density_origin_curvature.v1",
    "y": y,
    "step": h,
    "rho_samples": values,
    "one_sided_origin_curvature": origin_curvature,
    "checks": {
        "origin_curvature_is_negative": origin_curvature < -0.33,
        "density_initially_decreases": values[1] < values[0],
        "convex_polya_certificate_fails": 2.0 * values[1] > values[0] + values[2],
    },
    "scope": "Numerical replay of an analytically proved strict-sign identity.",
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
