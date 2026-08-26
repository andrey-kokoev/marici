"""Exact reconstruction of the continuous-q oriented cone through grade 40.

The source filtration predicts degree n-3 after removing the universal q^3
factor at normal grade n.  Consecutive exact values reconstruct that
polynomial, and four withheld values test the predicted degree before any
positivity claim is evaluated.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path

import deutschean_cumulant_gevrey_descent as descent


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / os.environ.get(
    "STROMINGER_CONTINUOUS_RESULT",
    "research/strominger/results/deutschean_continuous_q_cone.json",
)
ORDER = descent.ORDER
RECONSTRUCTION_SAMPLES = ORDER + 1
WITHHELD_SAMPLES = 4
VERTEX_ORDER = int(os.environ.get("STROMINGER_VERTEX_ORDER", "12"))


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in poly]


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def poly_eval(poly: list[Fraction], value: Fraction) -> Fraction:
    out = Fraction(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) == 1:
        return [Fraction(0)]
    return [Fraction(i) * poly[i] for i in range(1, len(poly))]


def series_mul(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    out = [[Fraction(0)] for _ in range(ORDER + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= ORDER:
                out[i + j] = poly_add(out[i + j], poly_mul(a, b))
    return out


def series_add(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [poly_add(left[n], right[n]) for n in range(ORDER + 1)]


def series_inverse(series: list[list[Fraction]]) -> list[list[Fraction]]:
    assert series[0] == [Fraction(1)]
    out = [[Fraction(0)] for _ in range(ORDER + 1)]
    out[0] = [Fraction(1)]
    for n in range(1, ORDER + 1):
        accumulator = [Fraction(0)]
        for k in range(1, n + 1):
            accumulator = poly_add(
                accumulator, poly_mul(series[k], out[n - k])
            )
        out[n] = poly_scale(accumulator, Fraction(-1))
    return out


def series_mul_limit(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
    limit: int,
) -> list[list[Fraction]]:
    out = [[Fraction(0)] for _ in range(limit + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= limit:
                out[i + j] = poly_add(out[i + j], poly_mul(a, b))
    return out


def reconstruct_in_q_minus_four(values_at_q_1: list[Fraction]) -> list[Fraction]:
    """Newton reconstruction, returned in powers of s=q-4."""
    level = values_at_q_1[:]
    forward = []
    while level:
        forward.append(level[0])
        level = [level[i + 1] - level[i] for i in range(len(level) - 1)]

    result = [Fraction(0)]
    basis = [Fraction(1)]
    for k, coefficient in enumerate(forward):
        result = poly_add(result, poly_scale(basis, coefficient))
        # binom(q-1,k+1) from binom(q-1,k), with q-1=s+3.
        basis = poly_scale(
            poly_mul(basis, [Fraction(3 - k), Fraction(1)]),
            Fraction(1, k + 1),
        )
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def power_to_bernstein(poly: list[Fraction], length: Fraction) -> list[Fraction]:
    degree = len(poly) - 1
    return [
        sum(
            poly[k]
            * Fraction(math.comb(i, k), math.comb(degree, k))
            * length**k
            for k in range(i + 1)
        )
        for i in range(degree + 1)
    ]


def divide_by_q(poly_in_q_minus_four: list[Fraction]) -> tuple[list[Fraction], Fraction]:
    """Divide by q=s+4, returning quotient and exact remainder."""
    work = poly_in_q_minus_four[:]
    quotient = [Fraction(0) for _ in range(len(work) - 1)]
    for degree in range(len(work) - 1, 0, -1):
        coefficient = work[degree]
        quotient[degree - 1] = coefficient
        work[degree] -= coefficient
        work[degree - 1] -= 4 * coefficient
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient, work[0]


def bounded_fraction_certificate(value: Fraction) -> str:
    if max(value.numerator.bit_length(), value.denominator.bit_length()) < 12000:
        return str(value)
    return (
        "exact_fraction_omitted_from_output:"
        f"numerator_bits={value.numerator.bit_length()}:"
        f"denominator_bits={value.denominator.bit_length()}"
    )


def main() -> None:
    maximum_q = RECONSTRUCTION_SAMPLES + WITHHELD_SAMPLES
    carrier = descent.build_carrier()
    carrier_log = [[Fraction(0)] for _ in range(ORDER + 1)]
    carrier_log_degrees = {}
    for n in range(1, ORDER + 1):
        correction = [Fraction(0)]
        for k in range(1, n):
            correction = descent.xp_add(
                correction,
                descent.xp_scale(
                    descent.xp_mul(carrier_log[k], carrier[n - k]),
                    Fraction(k, n),
                ),
            )
        carrier_log[n] = descent.xp_add(
            carrier[n], descent.xp_scale(correction, Fraction(-1))
        )
        carrier_log_degrees[n] = len(carrier_log[n]) - 1
    log_jets = {
        q: descent.partition_log_jets(carrier, q)
        for q in range(maximum_q + 1)
    }
    margins = {
        q: descent.margin_from_log_jets(log_jets[q], log_jets[q - 1], q)
        for q in range(1, maximum_q + 1)
    }
    relative_inverse_values = {}
    for q in range(1, maximum_q + 1):
        normalized_adjacent_response = [Fraction(1)] + [
            Fraction(q) * (log_jets[q][n][1] - log_jets[q - 1][n][1])
            for n in range(1, ORDER + 1)
        ]
        relative_inverse_values[q] = descent.ts_inverse(
            normalized_adjacent_response
        )

    oriented_polynomials = {}
    raw_degrees = {}
    quotient_degrees = {}
    q_cubed_factor_failures = []
    withheld_failures = []
    oriented_deformation = [[Fraction(0)] for _ in range(ORDER + 1)]
    deformation_q_factor_failures = []
    deformation_withheld_failures = []
    rooted_tree_leading_failures = []
    for normal_grade in range(3, ORDER + 1):
        reconstruction_values = [
            Fraction((-1) ** (normal_grade - 3))
            * margins[q][normal_grade]
            for q in range(1, RECONSTRUCTION_SAMPLES + 1)
        ]
        raw_polynomial = reconstruct_in_q_minus_four(reconstruction_values)
        raw_degrees[normal_grade] = len(raw_polynomial) - 1
        polynomial = raw_polynomial
        for multiplicity in range(1, 4):
            polynomial, remainder = divide_by_q(polynomial)
            if remainder:
                q_cubed_factor_failures.append((normal_grade, multiplicity))
        oriented_polynomials[normal_grade] = polynomial
        quotient_degrees[normal_grade] = len(polynomial) - 1
        for q in range(RECONSTRUCTION_SAMPLES + 1, maximum_q + 1):
            expected = (
                Fraction((-1) ** (normal_grade - 3))
                * margins[q][normal_grade]
            )
            if poly_eval(raw_polynomial, Fraction(q - 4)) != expected:
                withheld_failures.append((normal_grade, q))

    for normal_grade in range(1, ORDER + 1):
        raw_relative_inverse = reconstruct_in_q_minus_four(
            [
                relative_inverse_values[q][normal_grade]
                for q in range(1, RECONSTRUCTION_SAMPLES + 1)
            ]
        )
        deformation, remainder = divide_by_q(raw_relative_inverse)
        if remainder:
            deformation_q_factor_failures.append(normal_grade)
        oriented_deformation[normal_grade] = poly_scale(
            deformation, Fraction((-1) ** (normal_grade - 1))
        )
        expected_leading = Fraction(
            normal_grade ** (normal_grade - 2),
            math.factorial(normal_grade - 1),
        ) if normal_grade > 1 else Fraction(1)
        if oriented_deformation[normal_grade][-1] != expected_leading:
            rooted_tree_leading_failures.append(normal_grade)
        for q in range(RECONSTRUCTION_SAMPLES + 1, maximum_q + 1):
            if poly_eval(raw_relative_inverse, Fraction(q - 4)) != (
                relative_inverse_values[q][normal_grade]
            ):
                deformation_withheld_failures.append((normal_grade, q))

    q_polynomial = [Fraction(4), Fraction(1)]
    first_q_derivative = [
        poly_derivative(poly) for poly in oriented_deformation
    ]
    second_q_derivative = [
        poly_derivative(poly) for poly in first_q_derivative
    ]
    q_times_deformation = [
        poly_mul(q_polynomial, poly) for poly in oriented_deformation
    ]
    denominator = [[Fraction(1)]] + [
        poly_scale(q_times_deformation[n], Fraction(-1))
        for n in range(1, ORDER + 1)
    ]
    numerator = series_add(
        series_mul(oriented_deformation, first_q_derivative),
        [
            poly_scale(poly_mul(q_polynomial, poly), Fraction(2))
            for poly in series_mul(first_q_derivative, first_q_derivative)
        ],
    )
    reduced_curvature = series_add(
        second_q_derivative,
        series_mul(numerator, series_inverse(denominator)),
    )
    reduced_curvature_failures = [
        n
        for n in range(3, ORDER + 1)
        if reduced_curvature[n] != oriented_polynomials[n]
    ]

    vertex_order = min(VERTEX_ORDER, ORDER - 1)
    deformation_truncation = oriented_deformation[: vertex_order + 2]
    unit_series = [[Fraction(1)]] + [
        [Fraction(0)] for _ in range(vertex_order)
    ]
    deformation_powers = [unit_series]
    for _ in range(1, vertex_order + 1):
        deformation_powers.append(
            series_mul_limit(
                deformation_powers[-1],
                deformation_truncation,
                vertex_order,
            )
        )
    vertex_constructor = [[Fraction(1)]]
    for m in range(1, vertex_order + 1):
        known = [Fraction(0)]
        for k in range(m):
            known = poly_add(
                known,
                poly_mul(vertex_constructor[k], deformation_powers[k][m]),
            )
        vertex_constructor.append(
            poly_add(oriented_deformation[m + 1], poly_scale(known, Fraction(-1)))
        )
    connected_vertex_source = [[Fraction(0)] for _ in range(vertex_order + 1)]
    for n in range(1, vertex_order + 1):
        correction = [Fraction(0)]
        for k in range(1, n):
            correction = poly_add(
                correction,
                poly_scale(
                    poly_mul(
                        connected_vertex_source[k], vertex_constructor[n - k]
                    ),
                    Fraction(k, n),
                ),
            )
        connected_vertex_source[n] = poly_add(
            vertex_constructor[n], poly_scale(correction, Fraction(-1))
        )
    vertex_constructor_failures = [
        n
        for n in range(1, vertex_order + 1)
        if not all(coefficient > 0 for coefficient in vertex_constructor[n])
    ]
    connected_vertex_source_failures = [
        n
        for n in range(1, vertex_order + 1)
        if not all(coefficient > 0 for coefficient in connected_vertex_source[n])
    ]
    vertex_leading_failures = [
        n
        for n in range(1, vertex_order + 1)
        if vertex_constructor[n][-1] != Fraction(1, math.factorial(n))
    ]
    far_wall_parameter = Fraction(1, 60)
    far_wall_deformation = sum(
        poly_eval(oriented_deformation[n], Fraction(6)) * far_wall_parameter**n
        for n in range(1, ORDER + 1)
    )
    connected_vertex_derivative = sum(
        Fraction(n)
        * poly_eval(connected_vertex_source[n], Fraction(6))
        * far_wall_deformation ** (n - 1)
        for n in range(1, vertex_order + 1)
    )
    finite_vertex_contraction = (
        far_wall_deformation * connected_vertex_derivative
    )

    stable_bernstein_failures = []
    initialization_bernstein_failures = []
    for n in range(3, ORDER):
        initialization_difference = poly_add(
            poly_scale(oriented_polynomials[n], Fraction(14 * (n + 1))),
            poly_scale(oriented_polynomials[n + 1], Fraction(-1)),
        )
        if any(
            coordinate <= 0
            for coordinate in power_to_bernstein(initialization_difference, Fraction(6))
        ):
            initialization_bernstein_failures.append(n)
        if n >= 6:
            stable_difference = poly_add(
                poly_scale(
                    oriented_polynomials[n], Fraction(11 * (n + 1), 2)
                ),
                poly_scale(oriented_polynomials[n + 1], Fraction(-1)),
            )
            if any(
                coordinate <= 0
                for coordinate in power_to_bernstein(stable_difference, Fraction(6))
            ):
                stable_bernstein_failures.append(n)

    t = Fraction(1, 60)
    signed_block = [Fraction(0)]
    for n in range(6, ORDER + 1):
        signed_block = poly_add(
            signed_block,
            poly_scale(oriented_polynomials[n], Fraction((-1) ** (n - 3)) * t**n),
        )
    negative_block_coordinates = power_to_bernstein(
        poly_scale(signed_block, Fraction(-1)), Fraction(6)
    )
    reserve_slack = poly_add([t**3], signed_block)
    reserve_slack_coordinates = power_to_bernstein(reserve_slack, Fraction(6))

    checks = {
        "source_log_vertex_degree_is_at_most_n_plus_one": all(
            carrier_log_degrees[n] <= n + 1 for n in range(1, ORDER + 1)
        ),
        "source_raw_degree_n_reconstructed_through_grade_40": all(
            raw_degrees[n] == n for n in range(3, ORDER + 1)
        ),
        "relative_inverse_deformation_has_exact_q_factor": (
            not deformation_q_factor_failures
        ),
        "relative_inverse_oriented_coefficients_are_positive_in_q_minus_four": all(
            all(coefficient > 0 for coefficient in oriented_deformation[n])
            for n in range(1, ORDER + 1)
        ),
        "relative_inverse_has_rooted_tree_leading_coefficients": (
            not rooted_tree_leading_failures
        ),
        "relative_inverse_reconstruction_matches_four_withheld_q_values": (
            not deformation_withheld_failures
        ),
        "positive_reduced_curvature_formula_reconstructs_margin": (
            not reduced_curvature_failures
        ),
        "implicit_vertex_constructor_is_positive_in_q_minus_four": (
            not vertex_constructor_failures
        ),
        "connected_log_vertex_source_is_positive_in_q_minus_four": (
            not connected_vertex_source_failures
        ),
        "implicit_vertex_constructor_has_exponential_leading_face": (
            not vertex_leading_failures
        ),
        "finite_atomic_vertex_constructor_is_contractive_at_far_wall": (
            finite_vertex_contraction < 1
        ),
        "universal_q_cubed_factor_is_exact_through_grade_40": (
            not q_cubed_factor_failures
        ),
        "q_cubed_quotient_has_degree_n_minus_three": all(
            quotient_degrees[n] == n - 3 for n in range(3, ORDER + 1)
        ),
        "four_withheld_exact_q_values_match_every_reconstruction": (
            not withheld_failures
        ),
        "all_q_minus_four_power_coefficients_are_positive": all(
            all(coefficient > 0 for coefficient in polynomial)
            for polynomial in oriented_polynomials.values()
        ),
        "continuous_q_initialization_borel_ratio_is_below_14": (
            not initialization_bernstein_failures
        ),
        "continuous_q_post_grade_6_borel_ratio_is_below_11_over_2": (
            not stable_bernstein_failures
        ),
        "continuous_q_grade_6_to_40_block_has_expected_negative_orientation": all(
            coordinate > 0 for coordinate in negative_block_coordinates
        ),
        "continuous_q_grade_6_to_40_block_uses_less_than_two_fifths_reserve": all(
            coordinate > 0 for coordinate in reserve_slack_coordinates
        ),
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "dependency_sha256": sha256(Path(descent.__file__).read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "normal_grade_range": [3, ORDER],
            "source_log_vertex_degrees": {
                str(n): degree for n, degree in carrier_log_degrees.items()
            },
            "continuous_q_interval": [4, 10],
            "reconstruction_q_samples": [1, RECONSTRUCTION_SAMPLES],
            "withheld_q_samples": [
                RECONSTRUCTION_SAMPLES + 1,
                RECONSTRUCTION_SAMPLES + WITHHELD_SAMPLES,
            ],
            "withheld_failures": withheld_failures,
            "raw_degrees_by_normal_grade": {
                str(n): degree for n, degree in raw_degrees.items()
            },
            "q_cubed_quotient_degrees_by_normal_grade": {
                str(n): degree for n, degree in quotient_degrees.items()
            },
            "q_cubed_factor_failures": q_cubed_factor_failures,
            "deformation_q_factor_failures": deformation_q_factor_failures,
            "deformation_withheld_failures": deformation_withheld_failures,
            "rooted_tree_leading_failures": rooted_tree_leading_failures,
            "reduced_curvature_failures": reduced_curvature_failures,
            "implicit_vertex_order": vertex_order,
            "vertex_constructor_failures": vertex_constructor_failures,
            "connected_vertex_source_failures": connected_vertex_source_failures,
            "vertex_leading_failures": vertex_leading_failures,
            "finite_atomic_vertex_contraction_at_q_10_t_1_over_60": str(
                bounded_fraction_certificate(finite_vertex_contraction)
            ),
            "finite_atomic_vertex_contraction_decimal": float(
                finite_vertex_contraction
            ),
            "first_connected_vertex_source_polynomials": {
                str(n): [str(value) for value in connected_vertex_source[n]]
                for n in range(1, min(4, vertex_order) + 1)
            },
            "connected_vertex_source_diagonals": {
                str(n): {
                    "degree": len(connected_vertex_source[n]) - 1,
                    "constant": bounded_fraction_certificate(
                        connected_vertex_source[n][0]
                    ),
                    "next_to_leading": bounded_fraction_certificate(
                        connected_vertex_source[n][-2]
                        if len(connected_vertex_source[n]) > 1
                        else Fraction(0)
                    ),
                    "leading": bounded_fraction_certificate(
                        connected_vertex_source[n][-1]
                    ),
                    "top_six": [
                        bounded_fraction_certificate(value)
                        for value in reversed(connected_vertex_source[n][-6:])
                    ],
                }
                for n in range(1, vertex_order + 1)
            },
            "initialization_bernstein_failure_orders": initialization_bernstein_failures,
            "stable_bernstein_failure_orders": stable_bernstein_failures,
            "minimum_negative_block_bernstein_coordinate": str(
                min(negative_block_coordinates)
            ),
            "minimum_reserve_slack_bernstein_coordinate": str(
                min(reserve_slack_coordinates)
            ),
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "Exact continuous-q finite-cutoff theorem through normal grade 40, "
            "with a bounded replay of the source vertex degree filtration. The connected-cumulant "
            "argument supplies its all-orders degree proof and the Ward identity supplies exact "
            "q^3 divisibility. The reconstruction verifies the stronger positive relative-inverse "
            "cone, its rooted-tree leading face, the reduced-curvature closure, and four withheld "
            "values. It does not machine-verify the all-orders connected-hypergraph argument, Borel "
            "continuation, or the remainder beyond grade 40."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
