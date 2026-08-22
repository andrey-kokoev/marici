"""Analytic high-precision evaluation of F'(t), without finite differences."""
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


D = Decimal
PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
BERNOULLI = [Fraction(1,6),Fraction(-1,30),Fraction(1,42),Fraction(-1,30),
             Fraction(5,66),Fraction(-691,2730),Fraction(7,6),Fraction(-3617,510)]


def digamma_trigamma(z):
    psi_correction = D(0)
    trigamma_correction = D(0)
    while z < 100:
        psi_correction -= 1 / z
        trigamma_correction += 1 / (z * z)
        z += 1
    psi = z.ln() - 1 / (2 * z)
    trigamma = 1 / z + 1 / (2 * z * z)
    for k, bernoulli in enumerate(BERNOULLI, 1):
        bernoulli = D(bernoulli.numerator) / D(bernoulli.denominator)
        psi -= bernoulli / (2 * k * z ** (2 * k))
        trigamma += bernoulli / z ** (2 * k + 1)
    return psi + psi_correction, trigamma + trigamma_correction


def eta_triple(s, depth):
    row = []
    for n in range(1, depth + 2):
        logn = D(n).ln()
        term = (-s * logn).exp()
        row.append([term, -logn * term, logn * logn * term])
    sums = [D(0), D(0), D(0)]
    two = D(2)
    for _ in range(depth):
        for j in range(3):
            sums[j] += row[0][j] / two
        row = [[row[i][j] - row[i + 1][j] for j in range(3)] for i in range(len(row) - 1)]
        two *= 2
    return sums


def analytic_slope(t, depth):
    q = t.sqrt()
    s = D("0.5") + q
    eta, eta1, eta2 = eta_triple(s, depth)
    log2 = D(2).ln()
    r = ((1 - s) * log2).exp()
    zlog = eta1 / eta - log2 * r / (1 - r)
    zlog1 = eta2 / eta - (eta1 / eta) ** 2 + log2 * log2 * r / (1 - r) ** 2
    psi, trigamma = digamma_trigamma(s / 2)
    coupled = -D("0.5") * PI.ln() + D("0.5") * psi + zlog
    coupled1 = D("0.25") * trigamma + zlog1
    prefactor = 2 * q - D("0.5") / q
    prefactor1 = 2 + D("0.5") / (q * q)
    return (prefactor1 * coupled + prefactor * coupled1) / (2 * q)


def run(precision, depth):
    with localcontext() as context:
        context.prec = precision
        endpoints = [D(f"1e-{power}") for power in range(8, 1, -1)]
        cache = {}

        def height(t):
            key = str(t)
            if key not in cache:
                slope = analytic_slope(t, depth)
                assert slope > 0
                cache[key] = 1 / slope.sqrt()
            return cache[key]

        rows = []
        for i, x in enumerate(endpoints):
            for y in endpoints[i + 1:]:
                midpoint = (x + y) / 2
                rows.append((height(midpoint) - (height(x) + height(y)) / 2, x, midpoint, y))
        return rows


baseline = run(80, 120)
control = run(90, 132)
minimum = min(baseline)
control_minimum = min(control)
maximum_discrepancy = max(abs(a[0] - b[0]) for a, b in zip(baseline, control))
robust_margin = min(minimum[0], control_minimum[0]) - maximum_discrepancy

result = {
    "method": "analytic differentiation carrying eta, eta-prime, eta-double-prime, digamma, and trigamma",
    "endpoint_range": ["1e-8", "1e-2"],
    "chord_count": len(baseline),
    "minimum_baseline_gap": str(minimum[0]),
    "minimum_baseline_chord": [str(x) for x in minimum[1:]],
    "minimum_control_gap": str(control_minimum[0]),
    "minimum_control_chord": [str(x) for x in control_minimum[1:]],
    "maximum_precision_depth_discrepancy": str(maximum_discrepancy),
    "conservative_robust_margin": str(robust_margin),
    "finite_difference_used": False,
    "all_chords_positive": minimum[0] > 0 and control_minimum[0] > 0,
    "interval_certified": False,
    "zero_locations_used": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "reduced-source-central-analytic-slope.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
