"""High-precision central-coordinate scan of reciprocal-slope concavity."""
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


D = Decimal
BERNOULLI = [Fraction(1,6),Fraction(-1,30),Fraction(1,42),Fraction(-1,30),
             Fraction(5,66),Fraction(-691,2730),Fraction(7,6),Fraction(-3617,510)]


def digamma(z):
    correction = D(0)
    # A high recurrence target makes even independently propagated asymptotic
    # remainder bounds harmless near the singular central prefactor.
    while z < 100:
        correction -= 1 / z
        z += 1
    value = z.ln() - 1 / (2 * z)
    z2 = z * z
    power = z2
    for k, bernoulli in enumerate(BERNOULLI, 1):
        bernoulli = D(bernoulli.numerator) / D(bernoulli.denominator)
        value -= bernoulli / (2 * k * power)
        power *= z2
    return value + correction


def eta_pair(s, depth):
    row = []
    for n in range(1, depth + 2):
        logn = D(n).ln()
        term = (-s * logn).exp()
        row.append([term, -logn * term])
    eta = D(0)
    derivative = D(0)
    two = D(2)
    for _ in range(depth):
        eta += row[0][0] / two
        derivative += row[0][1] / two
        row = [[row[i][j] - row[i + 1][j] for j in range(2)] for i in range(len(row) - 1)]
        two *= 2
    return eta, derivative


def source_F(t, depth):
    s = D("0.5") + t.sqrt()
    eta, etap = eta_pair(s, depth)
    log2 = D(2).ln()
    r = ((1 - s) * log2).exp()
    zeta_log_derivative = etap / eta - log2 * r / (1 - r)
    coupled = -D("0.5") * D(str("3.141592653589793238462643383279502884197169399375105820974944592307816406286")).ln()
    coupled += D("0.5") * digamma(s / 2) + zeta_log_derivative
    return 4 + 4 * s * (s - 1) / (2 * s - 1) * coupled


def run(precision, depth, relative_step):
    with localcontext() as context:
        context.prec = precision

        @lru_cache(maxsize=None)
        def F(text):
            return source_F(D(text), depth)

        def slope(x):
            h = x * D(relative_step)
            values = [F(str(x + multiple * h)) for multiple in (-2, -1, 1, 2)]
            return (values[0] - 8 * values[1] + 8 * values[2] - values[3]) / (12 * h)

        def height(x):
            derivative = slope(x)
            assert derivative > 0
            return 1 / derivative.sqrt()

        endpoints = [D(f"1e-{power}") for power in range(8, 1, -1)]
        rows = []
        for i, x in enumerate(endpoints):
            for y in endpoints[i + 1:]:
                midpoint = (x + y) / 2
                gap = height(midpoint) - (height(x) + height(y)) / 2
                rows.append((gap, x, midpoint, y))
        return rows


baseline = run(70, 120, "0.001")
control = run(80, 132, "0.0005")
minimum = min(baseline)
control_minimum = min(control)
maximum_discrepancy = max(abs(a[0] - b[0]) for a, b in zip(baseline, control))
robust_margin = min(minimum[0], control_minimum[0]) - maximum_discrepancy

result = {
    "endpoint_range": ["1e-8", "1e-2"],
    "chord_count": len(baseline),
    "minimum_baseline_gap": str(minimum[0]),
    "minimum_baseline_chord": [str(x) for x in minimum[1:]],
    "minimum_control_gap": str(control_minimum[0]),
    "minimum_control_chord": [str(x) for x in control_minimum[1:]],
    "maximum_baseline_control_discrepancy": str(maximum_discrepancy),
    "conservative_robust_margin": str(robust_margin),
    "all_chords_positive": minimum[0] > 0 and control_minimum[0] > 0,
    "robust_after_control_discrepancy": robust_margin > 0,
    "arbitrary_precision_decimal": True,
    "interval_certified": False,
    "zero_locations_used": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "reduced-source-central-decimal-concavity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
