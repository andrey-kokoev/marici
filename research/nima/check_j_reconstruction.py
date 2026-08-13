"""Exact low-point checks for the scalar-derived NLSM half-object.

The script has no third-party dependencies.  It implements

* planar cubic trees as polygon triangulations;
* the alternating large-delta associated grade of the planar scalar amplitude;
* the biadjoint double-partial pairing, including its relative-winding sign;
* exact inverse-pairing reconstruction in two independent six-point BCJ bases.
* photon-decoupling, Kleiss--Kuijf, and fundamental-BCJ identities through
  eight points.
* the exceptional six-point tensor identity in the quadratic soft-contact
  lemma.

All arithmetic is rational.  The checks are evidence, not an all-multiplicity
proof; see the accompanying ledger entries for the precise theorem and gap.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
import random


Order = tuple[int, ...]
Channel = frozenset[int]
Kinematics = list[list[Fraction]]
Edge = tuple[int, int]


@lru_cache(None)
def triangulations(vertices: tuple[int, ...]) -> tuple[frozenset[tuple[int, int]], ...]:
    """Return all triangulations as sets of polygon diagonals."""

    size = len(vertices)
    if size <= 3:
        return (frozenset(),)

    result: list[frozenset[tuple[int, int]]] = []
    for split in range(1, size - 1):
        left = vertices[: split + 1]
        right = vertices[split:]
        for left_diagonals in triangulations(left):
            for right_diagonals in triangulations(right):
                diagonals = set(left_diagonals) | set(right_diagonals)
                if split > 1:
                    diagonals.add(tuple(sorted((vertices[0], vertices[split]))))
                if split < size - 2:
                    diagonals.add(tuple(sorted((vertices[split], vertices[-1]))))
                result.append(frozenset(diagonals))

    # The recursion is unique, but de-duplicating also guards future changes.
    return tuple(dict.fromkeys(result))


def canonical_channel(labels: tuple[int, ...], multiplicity: int) -> Channel:
    """Identify a channel with its momentum-conserving complement."""

    channel = frozenset(labels)
    complement = frozenset(set(range(multiplicity)) - set(channel))
    if len(channel) < len(complement):
        return channel
    if len(complement) < len(channel):
        return complement
    return min(channel, complement, key=lambda item: tuple(sorted(item)))


@lru_cache(None)
def planar_trees(order: Order) -> tuple[frozenset[Channel], ...]:
    """Return the channel sets of all cubic trees planar in ``order``."""

    multiplicity = len(order)
    result = []
    for triangulation in triangulations(tuple(range(multiplicity))):
        channels = {
            canonical_channel(order[start:end], multiplicity)
            for start, end in triangulation
        }
        result.append(frozenset(channels))
    return tuple(result)


def is_planar(channel: Channel, order: Order) -> bool:
    """A channel is planar iff its labels form one cyclic interval."""

    membership = [label in channel for label in order]
    transitions = sum(
        membership[index] != membership[(index + 1) % len(order)]
        for index in range(len(order))
    )
    return transitions == 2


def channel_invariant(channel: tuple[int, ...] | Channel, s: Kinematics) -> Fraction:
    """Return (sum p_i)^2 using s_ij = 2 p_i dot p_j."""

    labels = tuple(channel)
    return sum(
        (s[labels[left]][labels[right]]
         for left in range(len(labels))
         for right in range(left + 1, len(labels))),
        Fraction(0),
    )


def relative_winding(first: Order, second: Order) -> int:
    """Relative winding entering the sign of m(first | second)."""

    multiplicity = len(first)
    positions = {label: index for index, label in enumerate(first)}
    distance = 0
    for index, label in enumerate(second):
        next_label = second[(index + 1) % multiplicity]
        distance += (positions[next_label] - positions[label]) % multiplicity
    assert distance % multiplicity == 0
    return distance // multiplicity


def double_partial(first: Order, second: Order, s: Kinematics) -> Fraction:
    """The BAS pairing m(first | second) from common planar cubic trees."""

    sign = (-1) ** (relative_winding(first, second) + 1)
    result = Fraction(0)
    for tree in planar_trees(first):
        if all(is_planar(channel, second) for channel in tree):
            denominator = Fraction(1)
            for channel in tree:
                denominator *= channel_invariant(channel, s)
            result += Fraction(1, denominator)
    return sign * result


def multiply_series(
    first: dict[int, Fraction],
    second: dict[int, Fraction],
    maximum_degree: int,
) -> dict[int, Fraction]:
    """Multiply truncated power series in t = delta^{-1}."""

    result: dict[int, Fraction] = defaultdict(Fraction)
    for first_degree, first_coefficient in first.items():
        for second_degree, second_coefficient in second.items():
            degree = first_degree + second_degree
            if degree <= maximum_degree:
                result[degree] += first_coefficient * second_coefficient
    return dict(result)


def scalar_grade(order: Order, s: Kinematics) -> Fraction:
    """Coefficient of delta^{-(n-2)} in the alternating shifted scalar tree."""

    multiplicity = len(order)
    target_degree = multiplicity - 2
    result = Fraction(0)

    for triangulation in triangulations(tuple(range(multiplicity))):
        series = {0: Fraction(1)}
        for start, end in triangulation:
            invariant = channel_invariant(order[start:end], s)
            # The positions in the scalar shift are one-indexed.  Opposite
            # colours are unshifted; equal colours receive opposite signs.
            first_position = start + 1
            second_position = end + 1
            if (first_position - second_position) % 2:
                factor = {0: Fraction(1, invariant)}
            else:
                shift_sign = 1 if first_position % 2 == 0 else -1
                factor = {
                    degree: (
                        Fraction((-1) ** (degree - 1))
                        * invariant ** (degree - 1)
                        / shift_sign**degree
                    )
                    for degree in range(1, target_degree + 1)
                }
            series = multiply_series(series, factor, target_degree)
        result += series.get(target_degree, Fraction(0))

    return result


def exact_kinematics(multiplicity: int, seed: int) -> Kinematics:
    """Create generic rational massless Mandelstams with zero row sums."""

    generator = random.Random(seed)
    s = [
        [Fraction(0) for _ in range(multiplicity)]
        for _ in range(multiplicity)
    ]
    independent_pairs = [
        (left, right)
        for left in range(multiplicity - 1)
        for right in range(left + 1, multiplicity - 1)
    ]
    values = [
        Fraction(generator.randint(-20, 20) or 1)
        for _ in independent_pairs[:-1]
    ]
    # This condition makes the final row sum vanish after solving the others.
    values.append(-sum(values, Fraction(0)))
    for (left, right), value in zip(independent_pairs, values, strict=True):
        s[left][right] = s[right][left] = value
    for left in range(multiplicity - 1):
        value = -sum(s[left][: multiplicity - 1], Fraction(0))
        s[left][multiplicity - 1] = s[multiplicity - 1][left] = value
    assert all(sum(row, Fraction(0)) == 0 for row in s)
    return s


def fundamental_bcj(multiplicity: int, s: Kinematics) -> Fraction:
    """Evaluate the fundamental BCJ combination of scalar grades."""

    result = Fraction(0)
    coefficient = Fraction(0)
    for insertion_end in range(1, multiplicity - 1):
        coefficient += s[0][insertion_end]
        order = (
            tuple(range(1, insertion_end + 1))
            + (0,)
            + tuple(range(insertion_end + 1, multiplicity))
        )
        result += coefficient * scalar_grade(order, s)
    return result


def photon_decoupling(multiplicity: int, s: Kinematics) -> Fraction:
    """Insert leg 0 in every slot of a fixed cyclic word."""

    fixed_order = tuple(range(1, multiplicity))
    return sum(
        (
            scalar_grade(
                fixed_order[:insertion] + (0,) + fixed_order[insertion:], s
            )
            for insertion in range(multiplicity - 1)
        ),
        Fraction(0),
    )


def ordered_shuffles(first: Order, second: Order) -> tuple[Order, ...]:
    """Return shuffles preserving the internal orders of both words."""

    if not first:
        return (second,)
    if not second:
        return (first,)
    return tuple(
        dict.fromkeys(
            tuple(
                (first[0],) + suffix
                for suffix in ordered_shuffles(first[1:], second)
            )
            + tuple(
                (second[0],) + suffix
                for suffix in ordered_shuffles(first, second[1:])
            )
        )
    )


def kleiss_kuijf(alpha: Order, beta: Order, s: Kinematics) -> Fraction:
    """Evaluate A(0,alpha,n-1,beta)-(-1)^|beta| sum_shuffle A."""

    last = len(s) - 1
    left = scalar_grade((0,) + alpha + (last,) + beta, s)
    right = sum(
        (
            scalar_grade((0,) + shuffle + (last,), s)
            for shuffle in ordered_shuffles(alpha, tuple(reversed(beta)))
        ),
        Fraction(0),
    )
    return left - (-1) ** len(beta) * right


def solve(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    """Solve a square rational linear system by Gauss-Jordan elimination."""

    size = len(matrix)
    augmented = [list(matrix[row]) + [vector[row]] for row in range(size)]
    for column in range(size):
        pivot = next(
            row for row in range(column, size) if augmented[row][column] != 0
        )
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column or augmented[row][column] == 0:
                continue
            multiplier = augmented[row][column]
            augmented[row] = [
                augmented[row][index] - multiplier * augmented[column][index]
                for index in range(size + 1)
            ]
    return [augmented[row][-1] for row in range(size)]


def reconstruct(
    test_basis: list[Order],
    expansion_basis: list[Order],
    s: Kinematics,
) -> list[Fraction]:
    """Raise the scalar-grade covector with the inverse BAS pairing."""

    pairing = [
        [double_partial(test, expansion, s) for expansion in expansion_basis]
        for test in test_basis
    ]
    periods = [scalar_grade(order, s) for order in test_basis]
    return solve(pairing, periods)


def six_point_formula(s: Kinematics) -> Fraction:
    """Closed scalar-grade expression in canonical planar variables."""

    order = tuple(range(6))

    def x(start: int, end: int) -> Fraction:
        return channel_invariant(order[start:end], s)

    x13, x14, x15 = x(0, 2), x(0, 3), x(0, 4)
    x24, x25, x26 = x(1, 3), x(1, 4), x(1, 5)
    x35, x36, x46 = x(2, 4), x(2, 5), x(3, 5)
    return (
        -(x13 + x15 + x24 + x26 + x35 + x46)
        + (x13 + x24) * (x15 + x46) / x14
        + (x15 + x26) * (x24 + x35) / x25
        + (x13 + x26) * (x35 + x46) / x36
    )


def relation_audit() -> None:
    """Check photon, KK, and fundamental BCJ relations at 4, 6, and 8 points."""

    safe_seeds = {4: (1, 2, 3), 6: (1, 2, 3), 8: (4, 5, 6)}
    for multiplicity, seeds in safe_seeds.items():
        checked = 0
        for seed in seeds:
            try:
                s = exact_kinematics(multiplicity, seed)
                photon_value = photon_decoupling(multiplicity, s)
                bcj_value = fundamental_bcj(multiplicity, s)
            except ZeroDivisionError:
                continue
            assert photon_value == 0, (multiplicity, seed, photon_value)
            assert bcj_value == 0, (multiplicity, seed, bcj_value)
            checked += 1
        assert checked > 0
        print(
            f"n={multiplicity}: photon decoupling and fundamental BCJ vanish "
            f"in {checked} exact sample(s)"
        )

    for multiplicity in (6, 8):
        s = exact_kinematics(multiplicity, 20 + multiplicity)
        middle = tuple(range(1, multiplicity - 1))
        checked = 0
        for split in range(len(middle) + 1):
            alpha, beta = middle[:split], middle[split:]
            assert kleiss_kuijf(alpha, beta, s) == 0, (
                multiplicity,
                alpha,
                beta,
            )
            checked += 1
        print(
            f"n={multiplicity}: KK shuffle identity vanishes for {checked} "
            "exact ordered splits"
        )


def four_cycle(first: int, second: int, third: int, fourth: int) -> dict[Edge, int]:
    """Edge coordinates of the alternating cycle C(first,second,third,fourth)."""

    result: dict[Edge, int] = defaultdict(int)
    for left, right, coefficient in (
        (first, second, 1),
        (second, third, -1),
        (third, fourth, 1),
        (fourth, first, -1),
    ):
        result[tuple(sorted((left, right)))] += coefficient
    return dict(result)


def symmetric_tensor(
    first: dict[Edge, int], second: dict[Edge, int]
) -> dict[tuple[Edge, Edge], Fraction]:
    """Coordinates of first odot second in the ordered edge-pair basis."""

    edges = tuple(combinations(range(1, 7), 2))
    return {
        (left, right): Fraction(
            first.get(left, 0) * second.get(right, 0)
            + second.get(left, 0) * first.get(right, 0),
            2,
        )
        for left in edges
        for right in edges
    }


def quadratic_contact_audit() -> None:
    """Verify the exceptional S6 orbit identity in the quadratic contact lemma."""

    def tensor(first: tuple[int, ...], second: tuple[int, ...]):
        return symmetric_tensor(four_cycle(*first), four_cycle(*second))

    left = tensor((1, 3, 4, 2), (1, 5, 6, 2))
    terms = (
        (1, (1, 2, 4, 3), (1, 2, 3, 5)),
        (1, (1, 2, 4, 3), (1, 2, 6, 3)),
        (-1, (1, 2, 4, 3), (1, 2, 3, 6)),
        (-1, (1, 2, 5, 3), (1, 2, 4, 5)),
        (1, (1, 2, 4, 5), (1, 2, 5, 6)),
        (-1, (1, 3, 4, 5), (1, 3, 5, 6)),
    )
    right = {
        coordinate: sum(
            (
                sign * tensor(first, second)[coordinate]
                for sign, first, second in terms
            ),
            Fraction(0),
        )
        for coordinate in left
    }
    assert left == right
    print("n=6: exceptional quadratic soft-contact tensor identity passes")


def four_point_audit() -> None:
    """Fix the four-point normalization and same-basis coordinate."""

    s = exact_kinematics(4, 7)
    order = (0, 1, 2, 3)
    grade = scalar_grade(order, s)
    assert grade == s[0][2]
    pairing = double_partial(order, order, s)
    coordinate = -s[0][1] * s[1][2]
    assert pairing * coordinate == grade
    print("n=4: a_R=s_13 and J=-s_12 s_23 PT(1234) in the same PT basis")


def six_point_audit() -> None:
    """Compare two independent inverse-BAS reconstructions on many orderings."""

    s = exact_kinematics(6, 11)
    assert scalar_grade(tuple(range(6)), s) == six_point_formula(s)

    middle = (1, 2, 3)
    left_basis = [(0,) + item + (4, 5) for item in permutations(middle)]
    right_basis = [(0,) + item + (5, 4) for item in permutations(middle)]
    alternate_left = [
        (1,) + item + (4, 5) for item in permutations((0, 2, 3))
    ]
    alternate_right = [
        (1,) + item + (5, 4) for item in permutations((0, 2, 3))
    ]

    first_coordinates = reconstruct(left_basis, right_basis, s)
    second_coordinates = reconstruct(alternate_left, alternate_right, s)
    audit_orders = list(
        dict.fromkeys(
            left_basis
            + right_basis
            + alternate_left
            + alternate_right
            + [
                (0, 1, 4, 2, 5, 3),
                (3, 0, 2, 5, 1, 4),
                (5, 4, 3, 2, 1, 0),
            ]
        )
    )

    for order in audit_orders:
        first_prediction = sum(
            (
                double_partial(order, basis_order, s) * coordinate
                for basis_order, coordinate in zip(
                    right_basis, first_coordinates, strict=True
                )
            ),
            Fraction(0),
        )
        second_prediction = sum(
            (
                double_partial(order, basis_order, s) * coordinate
                for basis_order, coordinate in zip(
                    alternate_right, second_coordinates, strict=True
                )
            ),
            Fraction(0),
        )
        actual = scalar_grade(order, s)
        assert first_prediction == second_prediction == actual, (
            order,
            first_prediction,
            second_prediction,
            actual,
        )

    print(
        "n=6: two 6x6 inverse-BAS reconstructions agree with the scalar grade "
        f"on {len(audit_orders)} orderings"
    )


def main() -> None:
    print("triangulation counts:", {n: len(triangulations(tuple(range(n)))) for n in (4, 6, 8)})
    four_point_audit()
    six_point_audit()
    quadratic_contact_audit()
    relation_audit()
    print("all exact low-point checks passed")


if __name__ == "__main__":
    main()
