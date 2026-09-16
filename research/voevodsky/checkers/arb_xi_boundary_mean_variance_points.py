"""Arb-certified point evaluations of the Xi boundary mean--variance gate.

This certifies only the listed points, not intervals between them.
Run with:
  PYTHONPATH="$PWD/research/benincasa/.tmp_flint" python <this-file>
"""

import json
from pathlib import Path

from flint import acb, acb_series, arb, ctx

ctx.dps = 70


def gate_at(x_text):
    x = arb(x_text)
    s = acb_series([acb(x + arb("0.5")), 1], 3)
    pi = acb(arb.pi())
    xi = (
        acb("0.5")
        * s
        * (s - 1)
        * ((-s / 2) * pi.log()).exp()
        * (s / 2).gamma()
        * s.zeta()
    )
    X = xi[0].real
    X1 = xi[1].real
    X2 = 2 * xi[2].real
    m = X1 / X
    m1 = X2 / X - m * m
    G = (1 + 4 * x * x) * m - x * (1 - 4 * x * x) * m1
    return G


points = [f"{j}/2000" for j in range(1, 1000)]
# arb does not parse rational strings through this constructor uniformly.
points = [str(j / 2000) for j in range(1, 1000)]
points += [f"1e-{k}" for k in range(1, 13)]

minimum_lower = None
minimum_record = None
failures = []
records = []
for text in points:
    G = gate_at(text)
    lower = G.lower()
    upper = G.upper()
    record = {"x": text, "G_lower": str(lower), "G_upper": str(upper)}
    records.append(record)
    if lower <= 0:
        failures.append(record)
    if minimum_lower is None or lower < minimum_lower:
        minimum_lower = lower
        minimum_record = record

result = {
    "precision_decimal_digits": ctx.dps,
    "certified_point_count": len(points),
    "all_point_balls_strictly_positive": not failures,
    "failure_count": len(failures),
    "minimum_lower_record": minimum_record,
    "failures": failures[:20],
    "interval_between_points_certified": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "arb-xi-boundary-mean-variance-points.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        if key != "failures":
            print(f"{key}={value}")
