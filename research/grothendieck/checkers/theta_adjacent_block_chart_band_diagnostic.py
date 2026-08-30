"""Three-chart, four-band diagnostic of the hostile asymmetric theta block."""
import json
import math
from pathlib import Path


PI = math.pi
a, b = 1.0, 8.0
L = PI / b
radius_squared = a * a + b * b
alpha = 2 * a - a / (2 * radius_squared)
beta = 2 * b + b / (2 * radius_squared)
label_pairs = ((1, 2), (2, 1))


def log_phi(label, radius):
    y = PI * label * label * math.exp(2 * radius)
    return math.log(2 * PI * label * label) + 2.5 * radius + math.log(2 * y - 3) - y


def integrand(n, m, S, d, radius_n, radius_m):
    exponent = a * S + log_phi(n, radius_n) + log_phi(m, radius_m)
    density = 0.0 if exponent < -745 else math.exp(exponent)
    return density * (beta * S * math.cos(b * d) + alpha * d * math.sin(b * d))


def chart_inner(chart, d, n, m, steps=1200, cutoff=6.0):
    upper = d if chart == "C" else cutoff
    if upper == 0:
        return 0.0
    width = upper / steps
    total = 0.0
    for index in range(steps + 1):
        x = index * width
        if chart == "A":
            S, radius_n, radius_m = 2 * x + d, x + d, x
        elif chart == "B":
            S, radius_n, radius_m = -2 * x - d, x, x + d
        else:
            S, radius_n, radius_m = d - 2 * x, d - x, x
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        total += coefficient * integrand(n, m, S, d, radius_n, radius_m)
    return total * width / 3


def chart_band(chart, band, D_steps=120):
    lower = band * PI / 16
    upper = (band + 1) * PI / 16
    width = (upper - lower) / D_steps
    total = 0.0
    for index in range(D_steps + 1):
        d = lower + index * width
        value = sum(chart_inner(chart, d, n, m) for n, m in label_pairs)
        coefficient = 1 if index in (0, D_steps) else (4 if index % 2 else 2)
        total += coefficient * value
    return total * width / 3


chart_rows = {chart: [chart_band(chart, band) for band in range(4)] for chart in "ABC"}
band_totals = [sum(chart_rows[chart][band] for chart in "ABC") for band in range(4)]
chart_totals = {chart: sum(values) for chart, values in chart_rows.items()}
block_total = sum(band_totals)

assert band_totals[0] > 0 and band_totals[1] < 0 and band_totals[2] < 0 and band_totals[3] > 0
assert all(value < 0 for value in chart_totals.values())
assert block_total < 0

result = {
    "parameters_a_b": [a, b],
    "exchange_label_orbit": [[1, 2], [2, 1]],
    "charts": ["A: U,V>=0", "B: U,V<=0", "C: U>=0>=V"],
    "canonical_d_bands": ["[0,pi/16]", "[pi/16,pi/8]", "[pi/8,3pi/16]", "[3pi/16,pi/4]"],
    "chart_by_band_values": chart_rows,
    "chart_totals": chart_totals,
    "band_totals_after_chart_and_label_sum": band_totals,
    "whole_block_total": block_total,
    "middle_two_bands_negative": True,
    "endpoint_two_bands_positive": True,
    "negative_middle_bands_dominate": True,
    "recommended_interval_grouping": "sum exchange labels and all three charts inside each fixed d-band",
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-adjacent-block-chart-band-diagnostic.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
