"""Outward-rounded interval prototype at the weakest compact endpoint.

This is a directed numerical enclosure prototype.  The hard-coded tail
allowances are deliberately much larger than the elementary exponential
majorants at u=2 and label 30, but those majorants still need to be emitted
as a formal certificate before this artifact is called rigorous.
"""

from decimal import Decimal, getcontext
import json
import math
from pathlib import Path


getcontext().prec = 50
D = Decimal
PI_LO = D("3.14159265358979323846264338327950288419716939937510")
PI_HI = D("3.14159265358979323846264338327950288419716939937511")


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = D(lo if hi is None else hi)

    def __add__(self, other):
        other = interval(other)
        return Interval((self.lo + other.lo).next_minus(), (self.hi + other.hi).next_plus())

    def __neg__(self):
        return Interval((-self.hi).next_minus(), (-self.lo).next_plus())

    def __sub__(self, other):
        return self + (-interval(other))

    def __mul__(self, other):
        other = interval(other)
        products = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return Interval(min(products).next_minus(), max(products).next_plus())

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        values = [D(1) / self.lo, D(1) / self.hi]
        return Interval(min(values).next_minus(), max(values).next_plus())

    def __truediv__(self, other):
        return self * interval(other).reciprocal()

    def encode(self):
        return [str(self.lo), str(self.hi)]


def interval(value):
    return value if isinstance(value, Interval) else Interval(value)


def exp_bounds(lo, hi):
    return Interval(lo.exp().next_minus(), hi.exp().next_plus())


class Jet:
    """Normalized derivatives: coefficient n is f^(n)/n!, through order 4."""

    def __init__(self, coefficients):
        self.c = [interval(value) for value in coefficients] + [Interval(0)] * (
            5 - len(coefficients)
        )

    @staticmethod
    def constant(value):
        return Jet([value])

    def __add__(self, other):
        other = jet(other)
        return Jet([self.c[n] + other.c[n] for n in range(5)])

    def __neg__(self):
        return Jet([-value for value in self.c])

    def __sub__(self, other):
        return self + (-jet(other))

    def __mul__(self, other):
        other = jet(other)
        return Jet(
            [
                sum_intervals(self.c[k] * other.c[n - k] for k in range(n + 1))
                for n in range(5)
            ]
        )

    def exp(self):
        result = [exp_bounds(self.c[0].lo, self.c[0].hi)] + [Interval(0)] * 4
        for n in range(1, 5):
            numerator = Interval(0)
            for k in range(1, n + 1):
                numerator = numerator + Interval(k) * self.c[k] * result[n - k]
            result[n] = numerator / Interval(n)
        return Jet(result)

    def power(self, exponent):
        result = Jet.constant(1)
        for _ in range(exponent):
            result = result * self
        return result


def jet(value):
    return value if isinstance(value, Jet) else Jet.constant(value)


def sum_intervals(values):
    total = Interval(0)
    for value in values:
        total = total + value
    return total


def phi_bounds(u_lo, u_hi, labels=30):
    total = Interval(0)
    exp_2u = exp_bounds(2 * u_lo, 2 * u_hi)
    exp_5u_over_2 = exp_bounds(D("2.5") * u_lo, D("2.5") * u_hi)
    for label in range(1, labels + 1):
        a = Interval(PI_LO * label * label, PI_HI * label * label)
        front = Interval(2) * a * exp_5u_over_2
        bracket = Interval(2) * a * exp_2u - Interval(3)
        decay = exp_bounds(-a.hi * exp_2u.hi, -a.lo * exp_2u.lo)
        total = total + front * bracket * decay
    # Uniform allowance for all omitted labels on u>=0.
    return Interval(total.lo, (total.hi + D("1e-1000")).next_plus())


def kernel_derivative_value(x, u, order, terms=220):
    if u == 0 and order:
        return D(0)
    k = order
    coefficient = D(math.factorial(k)) / D(math.factorial(2 * k))
    term = coefficient * (D(1) if k == 0 else u ** (2 * k))
    total = term
    for _ in range(terms - 1):
        ratio = (
            x
            * u
            * u
            * D(k + 1)
            / D(k + 1 - order)
            / D(2 * k + 1)
            / D(2 * k + 2)
        )
        term *= ratio
        total += term
        k += 1
        if term < D("1e-70") * max(total, D(1)) and k > order + 30:
            next_ratio = (
                x
                * u
                * u
                * D(k + 1)
                / D(k + 1 - order)
                / D(2 * k + 1)
                / D(2 * k + 2)
            )
            if next_ratio < D("0.5"):
                total += term * next_ratio / (D(1) - next_ratio)
            break
    return total


def integrate_jets(x=D(400), cutoff=D(2), steps=4000):
    width = cutoff / steps
    sums = [Interval(0) for _ in range(6)]
    for index in range(steps):
        u_lo = width * index
        u_hi = width * (index + 1)
        source = phi_bounds(u_lo, u_hi)
        for order in range(6):
            kernel = Interval(
                kernel_derivative_value(x, u_lo, order),
                kernel_derivative_value(x, u_hi, order),
            )
            sums[order] = sums[order] + source * kernel * Interval(width)
    # Grossly inflated common contour-tail allowance; actual elementary
    # majorants at u=2 are many orders smaller.
    tail = D("1e-30")
    return [Interval(value.lo, (value.hi + tail).next_plus()) for value in sums]


def simpson_jets(x=D(400), cutoff=D(2), steps=4000, jet_count=6):
    width = cutoff / steps
    sums = [Interval(0) for _ in range(jet_count)]
    for index in range(steps + 1):
        u = width * index
        source = phi_bounds(u, u)
        weight = 1 if index in (0, steps) else (4 if index % 2 else 2)
        for order in range(jet_count):
            kernel_value = kernel_derivative_value(x, u, order)
            sums[order] = sums[order] + source * Interval(kernel_value) * Interval(weight)
    return [value * Interval(width / 3) for value in sums]


def extrapolated_simpson_jets(x=D(400), steps=4000, jet_count=6):
    low = simpson_jets(x=x, steps=steps // 2, jet_count=jet_count)
    high = simpson_jets(x=x, steps=steps, jet_count=jet_count)
    result = []
    diagnostics = []
    for coarse, fine in zip(low, high):
        coarse_mid = (coarse.lo + coarse.hi) / 2
        fine_mid = (fine.lo + fine.hi) / 2
        discrepancy = abs(fine_mid - coarse_mid)
        rounding_radius = (fine.hi - fine.lo) / 2
        radius = D(100) * discrepancy + rounding_radius + D("1e-30")
        result.append(Interval((fine_mid - radius).next_minus(), (fine_mid + radius).next_plus()))
        diagnostics.append(
            {
                "coarse_fine_discrepancy": str(discrepancy),
                "inflated_radius": str(radius),
            }
        )
    return result, diagnostics


def formal_tail_bounds(x=D(400), jet_count=6):
    # For the requested derivative orders and u>=2:
    # d_x^m cosh(sqrt(x)u) <= u^(2m) exp(20u).
    # The n=1 source majorant is 4*pi^2 exp(9u/2-pi exp(2u)).
    # Its product has logarithmic derivative at most
    # 2m/u+24.5-2*pi*exp(2u).  At u=2 this is bounded by the
    # order-dependent negative rate used below, and it decreases thereafter.
    contour = []
    exp_four = D(4).exp()
    for order in range(jet_count):
        endpoint = (
            D(8)
            * PI_HI
            * PI_HI
            * D(2) ** (2 * order)
            * (D(49) - PI_LO * exp_four).exp()
        )
        decay_rate = D(2) * PI_LO * exp_four - D(order) - D("24.5")
        if decay_rate <= 0:
            raise ValueError("contour-tail majorant requires a positive decay rate")
        contour.append((endpoint / decay_rate).next_plus())

    # For n>=31 and u>=0, each omitted label is largest at u=0.
    # The consecutive majorant ratio is below exp(-190), so a geometric
    # factor of 2 is overwhelmingly safe.  Multiply by the largest kernel
    # derivative on 0<=u<=2, x=400, and by interval length 2.
    first_omitted_label = 9
    n = D(first_omitted_label)
    label_source = (
        D(8)
        * PI_HI
        * PI_HI
        * n**4
        * (-PI_LO * n * n).exp()
    )
    labels = []
    for order in range(jet_count):
        kernel_maximum = kernel_derivative_value(x, D(2), order)
        labels.append((D(2) * label_source * kernel_maximum).next_plus())
    return contour, labels


def phi_jet(u):
    exp_2u = (Jet.constant(2) * u).exp()
    exp_5u_over_2 = (Jet.constant(D("2.5")) * u).exp()
    total = Jet.constant(0)
    for label in range(1, 9):
        a = Interval(PI_LO * label * label, PI_HI * label * label)
        total = total + (
            Jet.constant(Interval(2) * a)
            * exp_5u_over_2
            * (Jet.constant(Interval(2) * a) * exp_2u - Jet.constant(3))
            * (-Jet.constant(a) * exp_2u).exp()
        )
    return total


def kernel_derivative_jet(x, u, order, terms=140):
    k = order
    coefficient = D(math.factorial(k)) / D(math.factorial(2 * k))
    term = Jet.constant(coefficient) * u.power(2 * k)
    total = term
    u_squared = u * u
    for _ in range(terms - 1):
        scalar = (
            x
            * D(k + 1)
            / D(k + 1 - order)
            / D(2 * k + 1)
            / D(2 * k + 2)
        )
        term = term * Jet.constant(scalar) * u_squared
        total = total + term
        k += 1
    # At k>=140 on x<=400, u<=2, the future scalar-series ratio is below
    # 0.03.  Twice the last normalized derivative coefficient therefore
    # encloses its complete differentiated tail through order four.
    for derivative in range(5):
        magnitude = D(2) * max(
            abs(term.c[derivative].lo), abs(term.c[derivative].hi)
        )
        total.c[derivative] = total.c[derivative] + Interval(-magnitude, magnitude)
    return total


def formal_simpson_remainder_bounds(
    x=D(400), cutoff=D(2), steps=4000, jet_count=6
):
    h = cutoff / steps
    panel_factor = h**5 / D(90)
    totals = [D(0) for _ in range(jet_count)]
    for panel in range(steps // 2):
        u_lo = D(2 * panel) * h
        u_hi = u_lo + D(2) * h
        u = Jet([Interval(u_lo, u_hi), Interval(1)])
        source = phi_jet(u)
        for order in range(jet_count):
            integrand = source * kernel_derivative_jet(x, u, order)
            fourth_derivative = Interval(24) * integrand.c[4]
            supremum = max(abs(fourth_derivative.lo), abs(fourth_derivative.hi))
            totals[order] += panel_factor * supremum
    return [value.next_plus() for value in totals]


def logarithmic_jets(values):
    normalized = [value / values[0] for value in values]
    logarithmic = [Interval(0)]
    for order in range(1, len(values)):
        correction = Interval(0)
        for index in range(1, order):
            correction = correction + (
                Interval(math.comb(order - 1, index - 1))
                * logarithmic[index]
                * normalized[order - index]
            )
        logarithmic.append(normalized[order] - correction)
    return logarithmic[1:]


def evaluate(x_value=D(400), steps=4000):
    x = Interval(x_value)
    displacement = x - Interval(D("0.25"))
    empirical_jets, simpson_diagnostics = extrapolated_simpson_jets(
        x=x_value, steps=steps
    )
    contour_tail_bounds, label_tail_bounds = formal_tail_bounds(x=x_value)
    simpson_remainder_bounds = formal_simpson_remainder_bounds(
        x=x_value, steps=steps
    )
    c_jets = []
    for order, empirical in enumerate(empirical_jets):
        midpoint = (empirical.lo + empirical.hi) / 2
        rounding_radius = (empirical.hi - empirical.lo) / 2
        radius = (
            rounding_radius
            + simpson_remainder_bounds[order]
            + contour_tail_bounds[order]
            + label_tail_bounds[order]
        )
        c_jets.append(
            Interval((midpoint - radius).next_minus(), (midpoint + radius).next_plus())
        )
    l1, l2, l3, l4, l5 = logarithmic_jets(c_jets)
    h1 = l1 + displacement * l2
    h2 = Interval(2) * l2 + displacement * l3
    h3 = Interval(3) * l3 + displacement * l4
    h4 = Interval(4) * l4 + displacement * l5
    numerator = Interval(2) * h1 * h3 - Interval(3) * h2 * h2
    numerator_prime = Interval(2) * h1 * h4 - Interval(4) * h2 * h3
    tail_allowance = D("1e-30")
    return {
        "x": str(x_value),
        "simpson_steps": steps,
        "C_jets": [value.encode() for value in c_jets],
        "H_jets": [value.encode() for value in [h1, h2, h3, h4]],
        "schwarzian_numerator": numerator.encode(),
        "schwarzian_numerator_prime": numerator_prime.encode(),
        "numerator_strictly_positive": numerator.lo > 0,
        "weakest_endpoint_certified": (
            numerator.lo > 0
            and all(value < tail_allowance for value in contour_tail_bounds + label_tail_bounds)
        ),
        "simpson_diagnostics": simpson_diagnostics,
        "directed_decimal_arithmetic": True,
        "quadrature_discrepancy_inflation_factor": 100,
        "formal_Simpson_remainder_bound_emitted": True,
        "formal_tail_certificate_emitted": True,
        "formal_contour_tail_bounds": [str(value) for value in contour_tail_bounds],
        "formal_label_tail_bounds": [str(value) for value in label_tail_bounds],
        "hard_coded_tail_allowance": str(tail_allowance),
        "formal_tail_bounds_fit_allowance": all(
            value < tail_allowance
            for value in contour_tail_bounds + label_tail_bounds
        ),
        "formal_Simpson_remainder_bounds": [
            str(value) for value in simpson_remainder_bounds
        ],
        "compact_interval_certified": False,
        "rh_proved_or_disproved": False,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--x", default="400")
    parser.add_argument("--steps", type=int, default=4000)
    parser.add_argument(
        "--output",
        type=Path,
        help="certificate JSON path (defaults to the historical single-endpoint result)",
    )
    arguments = parser.parse_args()
    result = evaluate(D(arguments.x), arguments.steps)
    output = arguments.output or (
        Path(__file__).parents[1]
        / "results"
        / "theta-compact-endpoint-decimal-interval.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
