"""Exact higher-jet descent through partition, logarithm, and cumulant.

The q-derivatives are propagated with a cubic epsilon jet at each integer
base grade.  This avoids interpolation in q and keeps every coefficient
rational.  The result is finite-grade evidence, not an all-orders theorem.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / "research/strominger/results/deutschean_cumulant_gevrey_descent.json"
ORDER = int(os.environ.get("STROMINGER_NORMAL_ORDER", "40"))
EPS_ORDER = 3
HANKEL_SIZE = 8
CONTIGUOUS_HANKEL_SIZE = 6


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def xp_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def xp_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([scalar * value for value in poly])


def xp_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def xt_mul(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    out = [[Fraction(0)] for _ in range(ORDER + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= ORDER:
                out[i + j] = xp_add(out[i + j], xp_mul(a, b))
    return out


def xt_exp(exponent: list[list[Fraction]]) -> list[list[Fraction]]:
    out = [[Fraction(0)] for _ in range(ORDER + 1)]
    out[0] = [Fraction(1)]
    for n in range(1, ORDER + 1):
        accumulator = [Fraction(0)]
        for k in range(1, n + 1):
            accumulator = xp_add(
                accumulator,
                xp_scale(xp_mul(exponent[k], out[n - k]), Fraction(k)),
            )
        out[n] = xp_scale(accumulator, Fraction(1, n))
    return out


def ep_zero() -> list[Fraction]:
    return [Fraction(0) for _ in range(EPS_ORDER + 1)]


def ep_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [left[i] + right[i] for i in range(EPS_ORDER + 1)]


def ep_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in poly]


def ep_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = ep_zero()
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= EPS_ORDER:
                out[i + j] += a * b
    return out


def rising_epsilon(base_grade: int | Fraction, power: int) -> list[Fraction]:
    out = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    for offset in range(1, power + 1):
        out = ep_mul(
            out,
            [Fraction(base_grade + offset), Fraction(1), Fraction(0), Fraction(0)],
        )
    return out


def gamma_expectation_epsilon(
    x_poly: list[Fraction], base_grade: int | Fraction
) -> list[Fraction]:
    out = ep_zero()
    for power, coefficient in enumerate(x_poly):
        out = ep_add(
            out, ep_scale(rising_epsilon(base_grade, power), coefficient)
        )
    return out


def partition_log_jets(
    carrier: list[list[Fraction]], base_grade: int | Fraction
) -> list[list[Fraction]]:
    partition = [
        gamma_expectation_epsilon(coefficient, base_grade)
        for coefficient in carrier
    ]
    assert partition[0] == [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    logarithm = [ep_zero() for _ in range(ORDER + 1)]
    for n in range(1, ORDER + 1):
        correction = ep_zero()
        for k in range(1, n):
            correction = ep_add(
                correction,
                ep_scale(ep_mul(logarithm[k], partition[n - k]), Fraction(k, n)),
            )
        logarithm[n] = ep_add(partition[n], ep_scale(correction, Fraction(-1)))
    return logarithm


def ts_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [left[i] + right[i] for i in range(ORDER + 1)]


def ts_scale(series: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in series]


def ts_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(ORDER + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= ORDER:
                out[i + j] += a * b
    return out


def ts_inverse(series: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(ORDER + 1)]
    out[0] = 1 / series[0]
    for n in range(1, ORDER + 1):
        out[n] = -sum(series[k] * out[n - k] for k in range(1, n + 1)) / series[0]
    return out


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    sign = 1
    value = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, len(work)):
            multiplier = work[row][column] / pivot_value
            for entry in range(column + 1, len(work)):
                work[row][entry] -= multiplier * work[column][entry]
    return sign * value


def hankel_orientation(size: int) -> int:
    return (-1) ** (size * (size - 1) // 2)


def build_carrier() -> list[list[Fraction]]:
    first = [[Fraction(0)] for _ in range(ORDER + 1)]
    first[0] = [Fraction(1)]
    first[1] = [Fraction(-3, 2), Fraction(1)]
    for n in range(2, ORDER + 1):
        first[n] = [Fraction(0)] * n + [Fraction(1, math.factorial(n))]

    second = [[Fraction(0)] for _ in range(ORDER + 1)]
    for n in range(ORDER + 1):
        second[n] = [Fraction(0)] * n + [Fraction(5, 4) ** n / math.factorial(n)]

    exponent = [[Fraction(0)] for _ in range(ORDER + 1)]
    for n in range(1, ORDER + 1):
        exponent[n] = [Fraction(0)] * (n + 1) + [
            -Fraction(1, math.factorial(n + 1))
        ]
    return xt_mul(xt_mul(first, second), xt_exp(exponent))


def margin_from_log_jets(
    upper: list[list[Fraction]],
    lower: list[list[Fraction]],
    q: int | Fraction,
) -> list[Fraction]:
    d = [Fraction(0) for _ in range(ORDER + 1)]
    variance = [Fraction(0) for _ in range(ORDER + 1)]
    skew = [Fraction(0) for _ in range(ORDER + 1)]
    d[0] = Fraction(1, q)
    variance[0] = Fraction(1, q * q)
    skew[0] = Fraction(2, q**3)
    for n in range(1, ORDER + 1):
        d[n] = upper[n][1] - lower[n][1]
        variance[n] = 2 * (lower[n][2] - upper[n][2])
        skew[n] = 6 * (upper[n][3] - lower[n][3])

    one = [Fraction(1)] + [Fraction(0) for _ in range(ORDER)]
    A = ts_add(one, ts_scale(d, Fraction(-q)))
    d_squared = ts_mul(d, d)
    raw = ts_add(
        ts_scale(ts_mul(A, variance), Fraction(3)),
        ts_mul(d_squared, ts_add(ts_scale(one, Fraction(2)), A)),
    )
    raw = ts_add(raw, ts_scale(skew, Fraction(-q)))
    return ts_mul(raw, ts_inverse(d_squared))


def margin_at_grade(
    carrier: list[list[Fraction]], q: int | Fraction
) -> list[Fraction]:
    return margin_from_log_jets(
        partition_log_jets(carrier, q),
        partition_log_jets(carrier, q - 1),
        q,
    )


def main() -> None:
    carrier = build_carrier()
    margins = {q: margin_at_grade(carrier, q) for q in range(4, 11)}
    oriented = {
        q: {
            n: Fraction((-1) ** (n - 3)) * margins[q][n] / q**3
            for n in range(3, ORDER + 1)
        }
        for q in margins
    }
    failures = {
        str(q): [n for n, value in oriented[q].items() if value <= 0]
        for q in oriented
    }
    borel_ratios = {
        q: {
            n: oriented[q][n + 1] / ((n + 1) * oriented[q][n])
            for n in range(3, ORDER)
        }
        for q in oriented
    }
    max_q, max_n, max_ratio = max(
        (
            (q, n, value)
            for q, ratios in borel_ratios.items()
            for n, value in ratios.items()
        ),
        key=lambda item: item[2],
    )
    late_q, late_n, late_ratio = max(
        (
            (q, n, value)
            for q, ratios in borel_ratios.items()
            for n, value in ratios.items()
            if n >= 6
        ),
        key=lambda item: item[2],
    )
    far_wall_t = Fraction(1, 60)
    finite_block_reserve_ratios = {
        q: sum(
            abs(margins[q][n]) * far_wall_t**n
            for n in range(6, ORDER + 1)
        )
        / (Fraction(5, 2) * q**3 * far_wall_t**3)
        for q in margins
    }
    absolute_reserve_q, absolute_reserve_ratio = max(
        finite_block_reserve_ratios.items(), key=lambda item: item[1]
    )
    signed_block_reserve_ratios = {
        q: abs(
            sum(margins[q][n] * far_wall_t**n for n in range(6, ORDER + 1))
        )
        / (Fraction(5, 2) * q**3 * far_wall_t**3)
        for q in margins
    }
    signed_reserve_q, signed_reserve_ratio = max(
        signed_block_reserve_ratios.items(), key=lambda item: item[1]
    )
    borel_moments = {
        q: [
            oriented[q][n] / math.factorial(n)
            for n in range(3, ORDER + 1)
        ]
        for q in oriented
    }
    raw_jet_moments = {
        q: [oriented[q][n] for n in range(3, ORDER + 1)]
        for q in oriented
    }
    hankel_determinants = {}
    shifted_hankel_determinants = {}
    for q, moments in borel_moments.items():
        hankel_determinants[q] = []
        shifted_hankel_determinants[q] = []
        for size in range(1, HANKEL_SIZE + 1):
            hankel_determinants[q].append(
                determinant(
                    [[moments[i + j] for j in range(size)] for i in range(size)]
                )
            )
            shifted_hankel_determinants[q].append(
                determinant(
                    [
                        [moments[i + j + 1] for j in range(size)]
                        for i in range(size)
                    ]
                )
            )
    hankel_orientation_mismatches = [
        (q, size)
        for q, determinants in hankel_determinants.items()
        for size, value in enumerate(determinants, start=1)
        if hankel_orientation(size) * value <= 0
    ]
    shifted_hankel_orientation_mismatches = [
        (q, size)
        for q, determinants in shifted_hankel_determinants.items()
        for size, value in enumerate(determinants, start=1)
        if hankel_orientation(size) * value <= 0
    ]
    shifted_contiguous_hankel_mismatches = []
    shifted_contiguous_hankel_test_count = 0
    for q, moments in borel_moments.items():
        for size in range(1, CONTIGUOUS_HANKEL_SIZE + 1):
            for start in range(1, len(moments) - 2 * size + 2):
                shifted_contiguous_hankel_test_count += 1
                value = determinant(
                    [
                        [moments[start + i + j] for j in range(size)]
                        for i in range(size)
                    ]
                )
                if hankel_orientation(size) * value <= 0:
                    shifted_contiguous_hankel_mismatches.append((q, size, start))
    raw_jet_hankel_negative_locations = []
    raw_jet_shifted_hankel_negative_locations = []
    for q, moments in raw_jet_moments.items():
        for size in range(1, HANKEL_SIZE + 1):
            if determinant(
                [[moments[i + j] for j in range(size)] for i in range(size)]
            ) <= 0:
                raw_jet_hankel_negative_locations.append((q, size))
            if determinant(
                [
                    [moments[i + j + 1] for j in range(size)]
                    for i in range(size)
                ]
            ) <= 0:
                raw_jet_shifted_hankel_negative_locations.append((q, size))

    checks = {
        "cubic_onset_matches_4q_cubed": all(
            margins[q][3] == 4 * q**3 for q in margins
        ),
        "oriented_margin_coefficients_are_positive_through_grade_40": all(
            not grades for grades in failures.values()
        ),
        "primitive_11_over_2_borel_type_is_not_preserved_by_cumulant_descent": (
            max_ratio > Fraction(11, 2)
            and max_ratio == Fraction(867, 64)
            and (max_q, max_n) == (10, 3)
        ),
        "factorially_normalized_margin_ratios_are_below_wall_scale_60": (
            max_ratio < 60
        ),
        "far_wall_borel_weighted_margin_transport_is_contractive": (
            max_ratio / 60 < 1
        ),
        "absolute_value_majorant_exceeds_reserve_and_is_rejected": (
            absolute_reserve_ratio > Fraction(3, 2)
        ),
        "oriented_grade_6_to_40_block_is_inside_reserve": (
            signed_reserve_ratio < Fraction(2, 5)
        ),
        "naive_scalar_stieltjes_moment_cone_is_rejected": any(
            value < 0
            for determinants in hankel_determinants.values()
            for value in determinants
        ),
        "scalar_laplace_complete_monotonicity_cone_is_rejected": (
            bool(raw_jet_hankel_negative_locations)
            and bool(raw_jet_shifted_hankel_negative_locations)
        ),
        "unshifted_cubic_seed_has_exactly_three_orientation_anomalies": (
            hankel_orientation_mismatches == [(4, 6), (4, 8), (5, 8)]
        ),
        "shifted_hankel_leading_minors_follow_period_four_orientation": all(
            hankel_orientation(size) * value > 0
            for determinants in shifted_hankel_determinants.values()
            for size, value in enumerate(determinants, start=1)
        ),
        "global_shifted_sign_regular_hankel_cone_is_rejected": (
            len(shifted_contiguous_hankel_mismatches) == 19
            and shifted_contiguous_hankel_mismatches[0] == (4, 5, 18)
        ),
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "maximum_normal_grade": ORDER,
            "integer_q_range": [4, 10],
            "orientation_failures_by_q": failures,
            "maximum_factorially_normalized_ratio": str(max_ratio),
            "maximum_ratio_location": {"q": max_q, "n_to_n_plus_one": max_n},
            "maximum_ratio_from_n_6": str(late_ratio),
            "maximum_ratio_from_n_6_location": {
                "q": late_q,
                "n_to_n_plus_one": late_n
            },
            "maximum_far_wall_weighted_ratio": str(max_ratio / 60),
            "maximum_grade_6_to_40_absolute_block_reserve_ratio": str(
                absolute_reserve_ratio
            ),
            "maximum_grade_6_to_40_absolute_block_reserve_q": absolute_reserve_q,
            "maximum_grade_6_to_40_oriented_block_reserve_ratio": str(
                signed_reserve_ratio
            ),
            "maximum_grade_6_to_40_oriented_block_reserve_q": signed_reserve_q,
            "hankel_leading_minor_sizes": [1, HANKEL_SIZE],
            "hankel_negative_minor_locations": [
                {"q": q, "size": size + 1}
                for q, determinants in hankel_determinants.items()
                for size, value in enumerate(determinants)
                if value <= 0
            ],
            "shifted_hankel_negative_minor_locations": [
                {"q": q, "size": size + 1}
                for q, determinants in shifted_hankel_determinants.items()
                for size, value in enumerate(determinants)
                if value <= 0
            ],
            "hankel_orientation_signature_sizes_1_to_8": [
                hankel_orientation(size) for size in range(1, HANKEL_SIZE + 1)
            ],
            "hankel_orientation_mismatch_locations": [
                {"q": q, "size": size}
                for q, size in hankel_orientation_mismatches
            ],
            "shifted_hankel_orientation_mismatch_locations": [
                {"q": q, "size": size}
                for q, size in shifted_hankel_orientation_mismatches
            ],
            "shifted_contiguous_hankel_test_count": (
                shifted_contiguous_hankel_test_count
            ),
            "shifted_contiguous_hankel_mismatch_locations": [
                {"q": q, "size": size, "start": start}
                for q, size, start in shifted_contiguous_hankel_mismatches
            ],
            "raw_jet_hankel_first_negative_location": {
                "q": raw_jet_hankel_negative_locations[0][0],
                "size": raw_jet_hankel_negative_locations[0][1]
            },
            "raw_jet_shifted_hankel_first_negative_location": {
                "q": raw_jet_shifted_hankel_negative_locations[0][0],
                "size": raw_jet_shifted_hankel_negative_locations[0][1]
            },
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "Exact integer-grade normal jets through order 40. This proves a "
            "finite-cutoff oriented Gevrey cone after partition, logarithm, and "
            "adjacent cumulant operations. It does not prove real-q positivity, "
            "all-orders Borel summability, or the physical Laplace remainder bound."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
