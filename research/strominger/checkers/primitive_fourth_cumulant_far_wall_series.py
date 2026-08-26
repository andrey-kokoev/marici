"""Exact far-wall series for the normalized adjacent-bias margin."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = (
    ROOT
    / "research"
    / "strominger"
    / "primitive-fourth-cumulant-transfer-normal-form.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "primitive_fourth_cumulant_far_wall_series.json"
)
ORDER = 12


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([scalar * value for value in poly])


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def poly_derivative(poly: list[Fraction], count: int) -> list[Fraction]:
    out = poly[:]
    for _ in range(count):
        out = [
            Fraction(index) * out[index]
            for index in range(1, len(out))
        ] or [Fraction(0)]
    return trim(out)


def poly_evaluate(poly: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def poly_shift_minus_one(poly: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(poly))]
    for power, coefficient in enumerate(poly):
        for new_power in range(power + 1):
            out[new_power] += (
                coefficient
                * math.comb(power, new_power)
                * (-1) ** (power - new_power)
            )
    return trim(out)


def poly_shift(poly: list[Fraction], offset: Fraction) -> list[Fraction]:
    """Return coefficients of poly(x + offset)."""
    out = [Fraction(0) for _ in range(len(poly))]
    for power, coefficient in enumerate(poly):
        for new_power in range(power + 1):
            out[new_power] += (
                coefficient
                * math.comb(power, new_power)
                * offset ** (power - new_power)
            )
    return trim(out)


def poly_equal(left: list[Fraction], right: list[Fraction]) -> bool:
    return trim(left[:]) == trim(right[:])


def poly_interpolate(points: list[tuple[Fraction, Fraction]]) -> list[Fraction]:
    """Return the unique polynomial through the supplied exact points."""
    result = [Fraction(0)]
    for x_i, y_i in points:
        basis = [Fraction(1)]
        denominator = Fraction(1)
        for x_j, _ in points:
            if x_j == x_i:
                continue
            basis = poly_mul(basis, [-x_j, Fraction(1)])
            denominator *= x_i - x_j
        result = poly_add(result, poly_scale(basis, y_i / denominator))
    return trim(result)


def power_to_bernstein(
    polynomial: list[Fraction], interval_length: Fraction
) -> list[Fraction]:
    """Convert p(x) on [0,L] from powers of x to Bernstein coordinates."""
    degree = len(polynomial) - 1
    return [
        sum(
            polynomial[power]
            * Fraction(math.comb(index, power), math.comb(degree, power))
            * interval_length**power
            for power in range(index + 1)
        )
        for index in range(degree + 1)
    ]


def series_mul(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    out = [[Fraction(0)] for _ in range(ORDER + 1)]
    for i, left_poly in enumerate(left):
        for j, right_poly in enumerate(right):
            if i + j <= ORDER:
                out[i + j] = poly_add(
                    out[i + j], poly_mul(left_poly, right_poly)
                )
    return out


def series_exp(exponent: list[list[Fraction]]) -> list[list[Fraction]]:
    out = [[Fraction(0)] for _ in range(ORDER + 1)]
    out[0] = [Fraction(1)]
    for n in range(1, ORDER + 1):
        accumulator = [Fraction(0)]
        for k in range(1, n + 1):
            term = poly_scale(
                poly_mul(exponent[k], out[n - k]), Fraction(k)
            )
            accumulator = poly_add(accumulator, term)
        out[n] = poly_scale(accumulator, Fraction(1, n))
    return out


def rising_q_plus_one(power: int) -> list[Fraction]:
    out = [Fraction(1)]
    for offset in range(1, power + 1):
        out = poly_mul(out, [Fraction(offset), Fraction(1)])
    return out


def gamma_expectation(poly_x: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)]
    for power, coefficient in enumerate(poly_x):
        out = poly_add(
            out, poly_scale(rising_q_plus_one(power), coefficient)
        )
    return out


def scalar_series_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(ORDER + 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            if i + j <= ORDER:
                out[i + j] += left_value * right_value
    return out


def scalar_series_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [left[index] + right[index] for index in range(ORDER + 1)]


def scalar_series_scale(series: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in series]


def scalar_series_inverse(series: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(ORDER + 1)]
    out[0] = 1 / series[0]
    for n in range(1, ORDER + 1):
        out[n] = -sum(
            series[k] * out[n - k] for k in range(1, n + 1)
        ) / series[0]
    return out


Rat = tuple[list[Fraction], list[Fraction]]


def rat_poly(poly: list[Fraction]) -> Rat:
    return trim(poly[:]), [Fraction(1)]


def rat_add(left: Rat, right: Rat) -> Rat:
    return (
        poly_add(
            poly_mul(left[0], right[1]),
            poly_mul(right[0], left[1]),
        ),
        poly_mul(left[1], right[1]),
    )


def rat_scale(value: Rat, scalar: Fraction) -> Rat:
    return poly_scale(value[0], scalar), value[1][:]


def rat_mul(left: Rat, right: Rat) -> Rat:
    return poly_mul(left[0], right[0]), poly_mul(left[1], right[1])


def rat_inverse(value: Rat) -> Rat:
    return value[1][:], value[0][:]


def rat_equal(left: Rat, right: Rat) -> bool:
    return poly_equal(
        poly_mul(left[0], right[1]),
        poly_mul(right[0], left[1]),
    )


def rat_series_add(left: list[Rat], right: list[Rat]) -> list[Rat]:
    return [rat_add(left[index], right[index]) for index in range(ORDER + 1)]


def rat_series_scale(series: list[Rat], scalar: Fraction) -> list[Rat]:
    return [rat_scale(value, scalar) for value in series]


def rat_series_mul(left: list[Rat], right: list[Rat]) -> list[Rat]:
    zero = rat_poly([Fraction(0)])
    out = [zero for _ in range(ORDER + 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            if i + j <= ORDER:
                out[i + j] = rat_add(
                    out[i + j], rat_mul(left_value, right_value)
                )
    return out


def rat_series_inverse(series: list[Rat]) -> list[Rat]:
    zero = rat_poly([Fraction(0)])
    out = [zero for _ in range(ORDER + 1)]
    out[0] = rat_inverse(series[0])
    for n in range(1, ORDER + 1):
        accumulator = zero
        for k in range(1, n + 1):
            accumulator = rat_add(
                accumulator, rat_mul(series[k], out[n - k])
            )
        out[n] = rat_scale(
            rat_mul(accumulator, rat_inverse(series[0])), Fraction(-1)
        )
    return out


# The scaled carrier relative to x^q exp(-x) is
# (exp(x t)-3t/2) exp(5xt/4)
# exp(-x^2 t/2-x^3 t^2/6-...).
first = [[Fraction(0)] for _ in range(ORDER + 1)]
first[0] = [Fraction(1)]
first[1] = [Fraction(-3, 2), Fraction(1)]
for n in range(2, ORDER + 1):
    first[n] = [Fraction(0)] * n + [Fraction(1, math.factorial(n))]

second = [[Fraction(0)] for _ in range(ORDER + 1)]
for n in range(ORDER + 1):
    second[n] = [Fraction(0)] * n + [
        Fraction(5, 4) ** n / math.factorial(n)
    ]

exponent = [[Fraction(0)] for _ in range(ORDER + 1)]
for n in range(1, ORDER + 1):
    exponent[n] = [Fraction(0)] * (n + 1) + [
        -Fraction(1, math.factorial(n + 1))
    ]
third = series_exp(exponent)
carrier_series = series_mul(series_mul(first, second), third)

# Take gamma expectations and then the formal logarithm.
partition_series = [gamma_expectation(poly) for poly in carrier_series]
log_partition = [[Fraction(0)] for _ in range(ORDER + 1)]
for n in range(1, ORDER + 1):
    correction = [Fraction(0)]
    for k in range(1, n):
        correction = poly_add(
            correction,
            poly_scale(
                poly_mul(log_partition[k], partition_series[n - k]),
                Fraction(k, n),
            ),
        )
    log_partition[n] = poly_add(
        partition_series[n], poly_scale(correction, Fraction(-1))
    )


def margin_series(q_integer: int) -> list[Fraction]:
    q = Fraction(q_integer)
    d = [Fraction(0) for _ in range(ORDER + 1)]
    variance_step = [Fraction(0) for _ in range(ORDER + 1)]
    skew_step = [Fraction(0) for _ in range(ORDER + 1)]
    d[0] = 1 / q
    variance_step[0] = 1 / q**2
    skew_step[0] = 2 / q**3
    for n in range(1, ORDER + 1):
        first_derivative = poly_derivative(log_partition[n], 1)
        second_derivative = poly_derivative(log_partition[n], 2)
        third_derivative = poly_derivative(log_partition[n], 3)
        d[n] = (
            poly_evaluate(first_derivative, q)
            - poly_evaluate(first_derivative, q - 1)
        )
        variance_step[n] = (
            poly_evaluate(second_derivative, q - 1)
            - poly_evaluate(second_derivative, q)
        )
        skew_step[n] = (
            poly_evaluate(third_derivative, q)
            - poly_evaluate(third_derivative, q - 1)
        )

    one = [Fraction(1)] + [Fraction(0) for _ in range(ORDER)]
    A = scalar_series_add(one, scalar_series_scale(d, -q))
    d_squared = scalar_series_mul(d, d)
    raw_margin = scalar_series_add(
        scalar_series_scale(
            scalar_series_mul(A, variance_step), Fraction(3)
        ),
        scalar_series_mul(
            d_squared,
            scalar_series_add(
                scalar_series_scale(one, Fraction(2)), A
            ),
        ),
    )
    raw_margin = scalar_series_add(
        raw_margin, scalar_series_scale(skew_step, -q)
    )
    return scalar_series_mul(raw_margin, scalar_series_inverse(d_squared))


series_by_q = {q: margin_series(q) for q in range(4, 11)}
leading_by_q = {}
for q, series in series_by_q.items():
    leading_order = next(
        (index for index, coefficient in enumerate(series) if coefficient),
        None,
    )
    leading_by_q[q] = {
        "order": leading_order,
        "coefficient": (
            str(series[leading_order]) if leading_order is not None else None
        ),
        "series": [str(value) for value in series],
    }

# Repeat the margin calculation over the rational function field Q(q).
q_poly = [Fraction(0), Fraction(1)]
one_rat = rat_poly([Fraction(1)])
zero_rat = rat_poly([Fraction(0)])
symbolic_d = [zero_rat for _ in range(ORDER + 1)]
symbolic_variance = [zero_rat for _ in range(ORDER + 1)]
symbolic_skew = [zero_rat for _ in range(ORDER + 1)]
symbolic_d[0] = ([Fraction(1)], q_poly)
symbolic_variance[0] = ([Fraction(1)], poly_mul(q_poly, q_poly))
symbolic_skew[0] = (
    [Fraction(2)],
    poly_mul(poly_mul(q_poly, q_poly), q_poly),
)
for n in range(1, ORDER + 1):
    first_derivative = poly_derivative(log_partition[n], 1)
    second_derivative = poly_derivative(log_partition[n], 2)
    third_derivative = poly_derivative(log_partition[n], 3)
    symbolic_d[n] = rat_poly(
        poly_add(
            first_derivative,
            poly_scale(poly_shift_minus_one(first_derivative), Fraction(-1)),
        )
    )
    symbolic_variance[n] = rat_poly(
        poly_add(
            poly_shift_minus_one(second_derivative),
            poly_scale(second_derivative, Fraction(-1)),
        )
    )
    symbolic_skew[n] = rat_poly(
        poly_add(
            third_derivative,
            poly_scale(poly_shift_minus_one(third_derivative), Fraction(-1)),
        )
    )

symbolic_one = [one_rat] + [zero_rat for _ in range(ORDER)]
symbolic_A = rat_series_add(
    symbolic_one,
    [rat_scale(rat_mul(rat_poly(q_poly), value), Fraction(-1))
     for value in symbolic_d],
)
symbolic_d_squared = rat_series_mul(symbolic_d, symbolic_d)
symbolic_raw_margin = rat_series_add(
    rat_series_scale(
        rat_series_mul(symbolic_A, symbolic_variance), Fraction(3)
    ),
    rat_series_mul(
        symbolic_d_squared,
        rat_series_add(
            rat_series_scale(symbolic_one, Fraction(2)), symbolic_A
        ),
    ),
)
symbolic_raw_margin = rat_series_add(
    symbolic_raw_margin,
    [
        rat_scale(rat_mul(rat_poly(q_poly), value), Fraction(-1))
        for value in symbolic_skew
    ],
)
symbolic_margin = rat_series_mul(
    symbolic_raw_margin, rat_series_inverse(symbolic_d_squared)
)

q_squared = poly_mul(q_poly, q_poly)
q_cubed = poly_mul(q_squared, q_poly)
continuous_targets = {
    3: rat_poly(poly_scale(q_cubed, Fraction(4))),
    4: rat_poly(
        poly_scale(
            poly_mul(q_cubed, [Fraction(-53), Fraction(92)]),
            Fraction(-1, 4),
        )
    ),
    5: rat_poly(
        poly_scale(
            poly_mul(
                q_cubed,
                [Fraction(297), Fraction(-776), Fraction(1520)],
            ),
            Fraction(1, 16),
        )
    ),
}
continuous_formula_checks = {
    order: rat_equal(symbolic_margin[order], target)
    for order, target in continuous_targets.items()
}

# Discover a degree-order candidate from exact integer evaluations, then prove
# it as an identity over Q(q) against the independently propagated rational
# function.  Interpolation proposes the coordinate; rat_equal is the gate.
continuous_coefficient_polynomials = {}
continuous_interpolation_checks = {}
continuous_q_cubed_checks = {}
oriented_shifted_quotients = {}
for order in range(3, ORDER + 1):
    coefficient_poly = poly_interpolate(
        [
            (Fraction(grade), margin_series(Fraction(grade))[order])
            for grade in range(1, order + 2)
        ]
    )
    continuous_coefficient_polynomials[order] = coefficient_poly
    continuous_interpolation_checks[order] = rat_equal(
        symbolic_margin[order], rat_poly(coefficient_poly)
    )
    continuous_q_cubed_checks[order] = (
        len(coefficient_poly) >= 4
        and coefficient_poly[:3] == [Fraction(0)] * 3
    )
    oriented_shifted_quotients[order] = poly_scale(
        poly_shift(coefficient_poly[3:], Fraction(4)),
        Fraction((-1) ** (order - 3)),
    )

ratio_37_bernstein = {}
for order in range(6, ORDER):
    difference = poly_add(
        poly_scale(oriented_shifted_quotients[order], Fraction(37)),
        poly_scale(oriented_shifted_quotients[order + 1], Fraction(-1)),
    )
    ratio_37_bernstein[order] = power_to_bernstein(
        difference, Fraction(6)
    )

# Positivity of the displayed three-term bracket for every real c>0.
# Multiplying its discriminant by 16 gives the polynomial below.
truncated_discriminant_numerator = [
    Fraction(-1943), Fraction(2664), Fraction(-15856)
]
truncated_quadratic_lead = [
    Fraction(297), Fraction(-776), Fraction(1520)
]
discriminant_decreases_from_q4 = (
    poly_evaluate(
        poly_derivative(truncated_discriminant_numerator, 1), Fraction(4)
    )
    < 0
    and poly_derivative(truncated_discriminant_numerator, 2)[0] < 0
)
lead_increases_from_q4 = (
    poly_evaluate(poly_derivative(truncated_quadratic_lead, 1), Fraction(4))
    > 0
    and poly_derivative(truncated_quadratic_lead, 2)[0] > 0
)
uniform_reserve_difference = [
    Fraction(-1027), Fraction(5096), Fraction(656)
]
uniform_reserve_increases_from_q4 = (
    poly_evaluate(
        poly_derivative(uniform_reserve_difference, 1), Fraction(4)
    )
    > 0
    and poly_derivative(uniform_reserve_difference, 2)[0] > 0
)

checks = {
    "q4_margin_vanishes_through_order_two": all(
        series_by_q[4][order] == 0 for order in range(3)
    ),
    "q4_first_nonzero_coefficient_is_256": series_by_q[4][3] == 256,
    "all_q_4_through_10_have_positive_leading_coefficient": all(
        Fraction(data["coefficient"]) > 0 for data in leading_by_q.values()
    ),
    "all_leading_coefficients_equal_4q_cubed": all(
        series_by_q[q][3] == 4 * q**3 for q in range(4, 11)
    ),
    "order_four_coefficients_match_factored_grade_law": all(
        series_by_q[q][4] == -Fraction(q**3 * (92 * q - 53), 4)
        for q in range(4, 11)
    ),
    "order_five_coefficients_match_factored_grade_law": all(
        series_by_q[q][5]
        == Fraction(q**3 * (1520 * q**2 - 776 * q + 297), 16)
        for q in range(4, 11)
    ),
    "continuous_q_order_three_formula_is_exact": continuous_formula_checks[3],
    "continuous_q_order_four_formula_is_exact": continuous_formula_checks[4],
    "continuous_q_order_five_formula_is_exact": continuous_formula_checks[5],
    "continuous_q_coefficients_are_polynomials_through_order_twelve": all(
        continuous_interpolation_checks.values()
    ),
    "continuous_q_coefficients_share_q_cubed_through_order_twelve": all(
        continuous_q_cubed_checks.values()
    ),
    "continuous_q_coefficients_alternate_through_order_twelve_for_q_at_least_four": all(
        all(coefficient > 0 for coefficient in polynomial)
        for polynomial in oriented_shifted_quotients.values()
    ),
    "oriented_coefficient_ratios_six_through_twelve_are_below_37": all(
        all(coefficient > 0 for coefficient in coordinates)
        for coordinates in ratio_37_bernstein.values()
    ),
    "three_term_bracket_has_negative_discriminant_for_q_ge_4": (
        discriminant_decreases_from_q4
        and poly_evaluate(truncated_discriminant_numerator, Fraction(4)) < 0
    ),
    "three_term_bracket_has_positive_quadratic_lead_for_q_ge_4": (
        lead_increases_from_q4
        and poly_evaluate(truncated_quadratic_lead, Fraction(4)) > 0
    ),
    "three_term_bracket_is_uniformly_at_least_five_halves": (
        uniform_reserve_increases_from_q4
        and poly_evaluate(uniform_reserve_difference, Fraction(4)) > 0
    ),
    "integer_grade_coefficients_alternate_through_order_twelve": all(
        ((-1) ** (order - 3)) * series_by_q[q][order] > 0
        for q in range(4, 11)
        for order in range(3, ORDER + 1)
    ),
    "finite_alternation_is_not_reported_as_series_convergence": True,
    "all_q_4_through_10_begin_at_order_three": all(
        data["order"] == 3 for data in leading_by_q.values()
    ),
    "series_result_is_not_reported_as_uniform_remainder_control": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "expansion_variable": "t=1/c_wall",
        "maximum_order": ORDER,
        "leading_margin_by_q": leading_by_q,
        "continuous_q_coefficient_polynomials_low_to_high": {
            str(order): [str(value) for value in polynomial]
            for order, polynomial in continuous_coefficient_polynomials.items()
        },
        "continuous_q_cubed_quotients_low_to_high": {
            str(order): [str(value) for value in polynomial[3:]]
            for order, polynomial in continuous_coefficient_polynomials.items()
        },
        "oriented_quotients_in_q_minus_four_low_to_high": {
            str(order): [str(value) for value in polynomial]
            for order, polynomial in oriented_shifted_quotients.items()
        },
        "ratio_37_difference_bernstein_coordinates_on_q_4_to_10": {
            str(order): [str(value) for value in coordinates]
            for order, coordinates in ratio_37_bernstein.items()
        },
        "uniform_remainder_status": "open",
        "compact_wall_status": "open",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "The formal series coefficients are exact. Positivity at finite wall "
        "requires a uniform remainder bound and a compact-region proof."
    ),
}

RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
