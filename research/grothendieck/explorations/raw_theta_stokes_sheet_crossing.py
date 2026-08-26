import cmath
import json
import math
from pathlib import Path


def phi(u):
    total = 0.0
    for n in range(1, 14):
        X = math.pi * n * n * math.exp(2.0 * u)
        if X < 745.0:
            total += math.exp(u / 2.0) * (4.0 * X * X - 6.0 * X) * math.exp(-X)
    return total


def stokes_3(x, y, panels, endpoint):
    h = endpoint / panels
    plus = 0.0j
    minus = 0.0j
    for j in range(panels + 1):
        u = j * h
        weight = 1 if j in (0, panels) else 4 if j % 2 else 2
        source = phi(u)
        phase = cmath.exp(1.0j * x * u)
        plus += weight * source * math.exp(y * u) * phase
        minus += weight * source * math.exp(-y * u) * phase
    plus *= h / 3.0
    minus *= h / 3.0
    return abs(plus) ** 2 - abs(minus) ** 2


refinements = [(2000, 3.0), (4000, 3.0), (8000, 3.0), (8000, 4.0), (16000, 4.0)]
samples = []
for panels, endpoint in refinements:
    left = stokes_3(15.7, 0.2, panels, endpoint)
    right = stokes_3(15.8, 0.2, panels, endpoint)
    samples.append(
        {
            "panels": panels,
            "endpoint": endpoint,
            "S3_at_15_7": left,
            "S3_at_15_8": right,
            "opposite_signs": left > 0.0 > right,
        }
    )

checks = {
    "all_refinements_reproduce_crossing": all(item["opposite_signs"] for item in samples),
    "positive_margin_at_left": min(item["S3_at_15_7"] for item in samples) > 4.2e-7,
    "negative_margin_at_right": max(item["S3_at_15_8"] for item in samples) < -5.3e-7,
}

result = {
    "schema": "marici.grothendieck.raw_theta_stokes_sheet_crossing.v1",
    "status": "numerical_reconnaissance_not_interval_certification",
    "parameters": {"y": 0.2, "crossing_bracket": [15.7, 15.8]},
    "checks": checks,
    "refinements": samples,
}

assert all(checks.values())
output = Path("research/grothendieck/results/raw_theta_stokes_sheet_crossing.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
