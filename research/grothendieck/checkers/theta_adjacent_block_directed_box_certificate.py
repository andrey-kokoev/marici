"""Outward-rounded box enclosure of the hostile three-chart theta block."""
import json
import math
from pathlib import Path


NEG_INF = -math.inf
POS_INF = math.inf
PI = (math.nextafter(math.pi, NEG_INF), math.nextafter(math.pi, POS_INF))


def point(value):
    return (math.nextafter(float(value), NEG_INF), math.nextafter(float(value), POS_INF))


def add(left, right):
    return (math.nextafter(left[0] + right[0], NEG_INF), math.nextafter(left[1] + right[1], POS_INF))


def neg(value):
    return (-value[1], -value[0])


def subtract(left, right):
    return add(left, neg(right))


def multiply(left, right):
    values = (left[0] * right[0], left[0] * right[1], left[1] * right[0], left[1] * right[1])
    return (math.nextafter(min(values), NEG_INF), math.nextafter(max(values), POS_INF))


def scale(value, scalar):
    return multiply(value, point(scalar))


def exp_interval(value):
    return (math.nextafter(math.exp(value[0]), NEG_INF), math.nextafter(math.exp(value[1]), POS_INF))


def trig_interval(value, cosine=False):
    function = math.cos if cosine else math.sin
    candidates = [function(value[0]), function(value[1])]
    offset = 0 if cosine else math.pi / 2
    first = math.ceil((value[0] - offset) / math.pi)
    last = math.floor((value[1] - offset) / math.pi)
    for integer in range(first, last + 1):
        candidates.append(function(offset + integer * math.pi))
    return (math.nextafter(min(candidates), NEG_INF), math.nextafter(max(candidates), POS_INF))


def phi_label(label, radius):
    label_constant = scale(PI, label * label)
    exponential_two_r = exp_interval(scale(radius, 2))
    y = multiply(label_constant, exponential_two_r)
    prefactor = scale(label_constant, 2)
    growth = exp_interval(scale(radius, 2.5))
    bracket = subtract(scale(y, 2), point(3))
    decay = exp_interval(neg(y))
    return multiply(multiply(multiply(prefactor, growth), bracket), decay)


a = 1.0
b = 11.0
radius_squared = a * a + b * b
alpha = point(2 * a - a / (2 * radius_squared))
beta = point(2 * b + b / (2 * radius_squared))


def chart_geometry(chart, d, coordinate):
    if chart == "A":
        x = coordinate
        S = add(scale(x, 2), d)
        radius_n, radius_m = add(x, d), x
        jacobian = point(1)
    elif chart == "B":
        x = coordinate
        S = neg(add(scale(x, 2), d))
        radius_n, radius_m = x, add(x, d)
        jacobian = point(1)
    else:
        proportion = coordinate
        x = multiply(d, proportion)
        S = subtract(d, scale(x, 2))
        radius_n, radius_m = subtract(d, x), x
        jacobian = d

    return S, radius_n, radius_m, jacobian


def exchange_orbit_integrand(chart, d, coordinate):
    S, radius_n, radius_m, jacobian = chart_geometry(chart, d, coordinate)
    # Factor the common signed kernel before interval evaluation.  Keeping the
    # exchanged labels inside one positive density orbit avoids losing their
    # exact correlation by intervalizing two complete signed summands.
    exchange_density = add(
        multiply(phi_label(1, radius_n), phi_label(2, radius_m)),
        multiply(phi_label(2, radius_n), phi_label(1, radius_m)),
    )
    density = multiply(exp_interval(S), exchange_density)
    phase = scale(d, b)
    kernel = add(
        multiply(beta, multiply(S, trig_interval(phase, cosine=True))),
        multiply(alpha, multiply(d, trig_interval(phase, cosine=False))),
    )
    return multiply(jacobian, multiply(density, kernel))


def reflected_AB_orbit_integrand(d, x):
    """Enclose charts A+B only after their exact source reflection sum."""
    s = add(scale(x, 2), d)
    exchange_density = add(
        multiply(phi_label(1, add(x, d)), phi_label(2, x)),
        multiply(phi_label(2, add(x, d)), phi_label(1, x)),
    )
    positive_exp = exp_interval(s)
    negative_exp = exp_interval(neg(s))
    odd_exp = subtract(positive_exp, negative_exp)
    even_exp = add(positive_exp, negative_exp)
    phase = scale(d, b)
    reflected_kernel = add(
        multiply(beta, multiply(multiply(s, trig_interval(phase, cosine=True)), odd_exp)),
        multiply(alpha, multiply(multiply(d, trig_interval(phase, cosine=False)), even_exp)),
    )
    return multiply(exchange_density, reflected_kernel)


def enclose_chart_band(chart, band, d_steps, x_steps, cutoff=3.0):
    # Four canonical half-bands cover the adjacent block [0, 2*pi/b].
    d_lower = band * math.pi / (2 * b)
    d_upper = (band + 1) * math.pi / (2 * b)
    coordinate_upper = 1.0 if chart == "C" else cutoff
    d_width = (d_upper - d_lower) / d_steps
    x_width = coordinate_upper / x_steps
    total = (0.0, 0.0)
    area = point(d_width * x_width)
    for d_index in range(d_steps):
        d = (d_lower + d_index * d_width, d_lower + (d_index + 1) * d_width)
        for x_index in range(x_steps):
            coordinate = (x_index * x_width, (x_index + 1) * x_width)
            value = (
                reflected_AB_orbit_integrand(d, coordinate)
                if chart == "AB"
                else exchange_orbit_integrand(chart, d, coordinate)
            )
            total = add(total, multiply(area, value))
    return total


d_steps = 160
x_steps = 320
chart_band_intervals = {
    chart: [enclose_chart_band(chart, band, d_steps, x_steps) for band in range(4)]
    for chart in ("AB", "C")
}
band_intervals = []
for band in range(4):
    value = (0.0, 0.0)
    for chart in ("AB", "C"):
        value = add(value, chart_band_intervals[chart][band])
    band_intervals.append(value)

compact_total = (0.0, 0.0)
for value in band_intervals:
    compact_total = add(compact_total, value)

# For x>=3, both A/B label products contain a factor bounded by
# exp(-pi*exp(2x)); a deliberately enormous 1e-100 absolute allowance is
# retained rather than relying on floating underflow.
tail_bound = 1e-100
full_total = (math.nextafter(compact_total[0] - tail_bound, NEG_INF), math.nextafter(compact_total[1] + tail_bound, POS_INF))

result = {
    "parameters_a_b": [a, b],
    "exchange_label_orbit": [[1, 2], [2, 1]],
    "d_steps_per_band": d_steps,
    "x_or_proportion_steps": x_steps,
    "AB_x_cutoff": 3,
    "chart_band_intervals": {
        chart: [[lo, hi] for lo, hi in values] for chart, values in chart_band_intervals.items()
    },
    "band_intervals_after_chart_and_label_sum": [[lo, hi] for lo, hi in band_intervals],
    "compact_total_interval": list(compact_total),
    "analytic_tail_absolute_bound": tail_bound,
    "full_block_interval": list(full_total),
    "strictly_negative": full_total[1] < 0,
    "outward_rounded_binary64": True,
    "transcendental_library_correct_rounding_assumed": True,
    "fully_formal_interval_certificate": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-adjacent-block-directed-box-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
