"""Exact audits for the Jordan/QTDS lift of the scalar-derived half-object.

The checks distinguish two statements:

* QTDS gives a canonical quartic presentation of each cyclic period of J once
  the alternating polarity cover of that cyclic ordering is supplied;
* this does not by itself define an endomorphism of the bare twisted class J,
  because the ordering/polarity and Jordan-pair data live in an enrichment.

Only standard-library exact arithmetic is used.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb
import random

from check_j_reconstruction import (
    Kinematics,
    Order,
    channel_invariant,
    double_partial,
    exact_kinematics,
    scalar_grade,
    solve,
)


Matrix = tuple[tuple[Fraction, ...], ...]
Momentum = tuple[Fraction, ...]
TreeShape = tuple[object, ...]


def momentum_dot(
    first: tuple[int, ...], second: tuple[int, ...], s: Kinematics
) -> Fraction:
    """Return K_first dot K_second using s_ij = 2 k_i dot k_j."""

    return sum((s[left][right] for left in first for right in second), Fraction(0)) / 2


@lru_cache(None)
def odd_three_splits(size: int) -> tuple[tuple[int, int, int], ...]:
    """Ordered decompositions of an odd size into three positive odd sizes."""

    return tuple(
        (first, second, size - first - second)
        for first in range(1, size - 1, 2)
        for second in range(1, size - first, 2)
        if size - first - second > 0 and (size - first - second) % 2 == 1
    )


def qtds_amplitude(
    order: Order, s: Kinematics, *, first_is_plus: bool = True
) -> Fraction:
    """Planar tree amplitude from the paper's alternating QTDS vertex convention.

    Rooting on the final external leg turns a quartic tree into a ternary tree.
    Every current contains an odd consecutive block.  If its first leaf is +,
    the two plus entries at its root vertex are the first and third branches;
    if its first leaf is -, they are the root and middle branch.
    """

    if len(order) % 2:
        return Fraction(0)

    def vertex(
        block: Order,
        first_block: Order,
        second_block: Order,
        third_block: Order,
        starts_plus: bool,
    ) -> Fraction:
        if starts_plus:
            return -2 * momentum_dot(first_block, third_block, s)
        # The outgoing root momentum is -K_block.  The plus entries are the
        # root and middle branch, hence -2(-K_block).K_second.
        return 2 * momentum_dot(block, second_block, s)

    @lru_cache(None)
    def current(block: Order, starts_plus: bool) -> Fraction:
        if len(block) == 1:
            return Fraction(1)
        numerator = vertex_sum(block, starts_plus)
        return numerator / channel_invariant(block, s)

    @lru_cache(None)
    def vertex_sum(block: Order, starts_plus: bool) -> Fraction:
        result = Fraction(0)
        for first_size, second_size, _ in odd_three_splits(len(block)):
            first_end = first_size
            second_end = first_size + second_size
            first_block = block[:first_end]
            second_block = block[first_end:second_end]
            third_block = block[second_end:]
            result += (
                vertex(
                    block,
                    first_block,
                    second_block,
                    third_block,
                    starts_plus,
                )
                * current(first_block, starts_plus)
                * current(second_block, not starts_plus)
                * current(third_block, starts_plus)
            )
        return result

    return vertex_sum(order[:-1], first_is_plus)


def qtds_terms(
    order: Order, s: Kinematics, *, first_is_plus: bool
) -> dict[TreeShape, Fraction]:
    """Return individual rooted quartic-tree contributions by tree shape."""

    def vertex(
        block: Order,
        first_block: Order,
        second_block: Order,
        third_block: Order,
        starts_plus: bool,
    ) -> Fraction:
        if starts_plus:
            return -2 * momentum_dot(first_block, third_block, s)
        return 2 * momentum_dot(block, second_block, s)

    @lru_cache(None)
    def current_terms(block: Order, starts_plus: bool):
        if len(block) == 1:
            return (((), Fraction(1)),)
        denominator = channel_invariant(block, s)
        return tuple(
            (shape, value / denominator)
            for shape, value in vertex_terms(block, starts_plus)
        )

    @lru_cache(None)
    def vertex_terms(block: Order, starts_plus: bool):
        result: list[tuple[TreeShape, Fraction]] = []
        for first_size, second_size, third_size in odd_three_splits(len(block)):
            first_end = first_size
            second_end = first_size + second_size
            first_block = block[:first_end]
            second_block = block[first_end:second_end]
            third_block = block[second_end:]
            factor = vertex(
                block,
                first_block,
                second_block,
                third_block,
                starts_plus,
            )
            for first_shape, first_value in current_terms(first_block, starts_plus):
                for second_shape, second_value in current_terms(
                    second_block, not starts_plus
                ):
                    for third_shape, third_value in current_terms(
                        third_block, starts_plus
                    ):
                        shape = (
                            (first_size, second_size, third_size),
                            first_shape,
                            second_shape,
                            third_shape,
                        )
                        result.append(
                            (
                                shape,
                                factor * first_value * second_value * third_value,
                            )
                        )
        return tuple(result)

    return dict(vertex_terms(order[:-1], first_is_plus))


def qtds_raw_terms(
    order: Order, s: Kinematics, *, first_is_plus: bool
) -> tuple[tuple[Fraction, tuple[Order, ...]], ...]:
    """Return tree numerators together with their un-evaluated propagator blocks.

    Keeping the propagators separate lets the audit take an exact channel
    residue without ever dividing by the vanishing channel invariant.
    """

    def vertex(
        block: Order,
        first_block: Order,
        second_block: Order,
        third_block: Order,
        starts_plus: bool,
    ) -> Fraction:
        if starts_plus:
            return -2 * momentum_dot(first_block, third_block, s)
        return 2 * momentum_dot(block, second_block, s)

    @lru_cache(None)
    def current_terms(
        block: Order, starts_plus: bool
    ) -> tuple[tuple[Fraction, tuple[Order, ...]], ...]:
        if len(block) == 1:
            return ((Fraction(1), ()),)
        return tuple(
            (numerator, (block,) + propagators)
            for numerator, propagators in vertex_terms(block, starts_plus)
        )

    @lru_cache(None)
    def vertex_terms(
        block: Order, starts_plus: bool
    ) -> tuple[tuple[Fraction, tuple[Order, ...]], ...]:
        result: list[tuple[Fraction, tuple[Order, ...]]] = []
        for first_size, second_size, _ in odd_three_splits(len(block)):
            first_end = first_size
            second_end = first_size + second_size
            first_block = block[:first_end]
            second_block = block[first_end:second_end]
            third_block = block[second_end:]
            factor = vertex(
                block,
                first_block,
                second_block,
                third_block,
                starts_plus,
            )
            for first_value, first_propagators in current_terms(
                first_block, starts_plus
            ):
                for second_value, second_propagators in current_terms(
                    second_block, not starts_plus
                ):
                    for third_value, third_propagators in current_terms(
                        third_block, starts_plus
                    ):
                        result.append(
                            (
                                factor
                                * first_value
                                * second_value
                                * third_value,
                                first_propagators
                                + second_propagators
                                + third_propagators,
                            )
                        )
        return tuple(result)

    return vertex_terms(order[:-1], first_is_plus)


def constrained_channel_kinematics(
    multiplicity: int, channel: Order, seed: int
) -> Kinematics:
    """Create exact generic Mandelstams on the divisor s_channel=0."""

    assert multiplicity >= 6
    assert 1 < len(channel) < multiplicity - 1
    assert multiplicity - 1 not in channel
    generator = random.Random(seed)
    last = multiplicity - 1
    pairs = [
        (left, right)
        for left in range(last)
        for right in range(left + 1, last)
    ]
    channel_pairs = [
        pair for pair in pairs if pair[0] in channel and pair[1] in channel
    ]
    outside_pairs = [pair for pair in pairs if pair not in channel_pairs]
    channel_pivot = channel_pairs[-1]
    total_pivot = outside_pairs[-1]

    values: dict[tuple[int, int], Fraction] = {}
    for pair in pairs:
        if pair in (channel_pivot, total_pivot):
            continue
        values[pair] = Fraction(generator.randint(-30, 30) or 1)
    values[channel_pivot] = -sum(
        (values[pair] for pair in channel_pairs if pair != channel_pivot),
        Fraction(0),
    )
    values[total_pivot] = -sum(values.values(), Fraction(0))

    s = [
        [Fraction(0) for _ in range(multiplicity)]
        for _ in range(multiplicity)
    ]
    for (left, right), value in values.items():
        s[left][right] = s[right][left] = value
    for left in range(last):
        value = -sum(s[left][:last], Fraction(0))
        s[left][last] = s[last][left] = value
    assert all(sum(row, Fraction(0)) == 0 for row in s)
    assert channel_invariant(channel, s) == 0
    return s


def constrained_nested_kinematics(
    multiplicity: int, inner: Order, outer: Order, seed: int
) -> Kinematics:
    """Create exact Mandelstams on two nested channel divisors."""

    assert set(inner) < set(outer)
    assert multiplicity - 1 not in outer
    generator = random.Random(seed)
    last = multiplicity - 1
    pairs = [
        (left, right)
        for left in range(last)
        for right in range(left + 1, last)
    ]
    inner_pairs = [
        pair for pair in pairs if pair[0] in inner and pair[1] in inner
    ]
    outer_pairs = [
        pair for pair in pairs if pair[0] in outer and pair[1] in outer
    ]
    outer_only_pairs = [pair for pair in outer_pairs if pair not in inner_pairs]
    outside_pairs = [pair for pair in pairs if pair not in outer_pairs]
    inner_pivot = inner_pairs[-1]
    outer_pivot = outer_only_pairs[-1]
    total_pivot = outside_pairs[-1]

    values: dict[tuple[int, int], Fraction] = {}
    for pair in pairs:
        if pair in (inner_pivot, outer_pivot, total_pivot):
            continue
        values[pair] = Fraction(generator.randint(-30, 30) or 1)
    values[inner_pivot] = -sum(
        (values[pair] for pair in inner_pairs if pair != inner_pivot),
        Fraction(0),
    )
    values[outer_pivot] = -sum(
        (values[pair] for pair in outer_pairs if pair != outer_pivot),
        Fraction(0),
    )
    values[total_pivot] = -sum(values.values(), Fraction(0))

    s = [
        [Fraction(0) for _ in range(multiplicity)]
        for _ in range(multiplicity)
    ]
    for (left, right), value in values.items():
        s[left][right] = s[right][left] = value
    for left in range(last):
        value = -sum(s[left][:last], Fraction(0))
        s[left][last] = s[last][left] = value
    assert all(sum(row, Fraction(0)) == 0 for row in s)
    assert channel_invariant(inner, s) == 0
    assert channel_invariant(outer, s) == 0
    return s


def momentum_vector(label: int, multiplicity: int) -> Momentum:
    """Unit coefficient vector for one external momentum."""

    return tuple(
        Fraction(1 if index == label else 0) for index in range(multiplicity)
    )


def add_momenta(*momenta: Momentum) -> Momentum:
    """Add coefficient vectors in the external-momentum basis."""

    return tuple(
        sum((momentum[index] for momentum in momenta), Fraction(0))
        for index in range(len(momenta[0]))
    )


def scale_momentum(coefficient: int, momentum: Momentum) -> Momentum:
    """Scale a momentum coefficient vector."""

    return tuple(coefficient * value for value in momentum)


def vector_dot(first: Momentum, second: Momentum, s: Kinematics) -> Fraction:
    """Bilinear dot product of momentum coefficient vectors."""

    return sum(
        (
            first[left] * second[right] * s[left][right]
            for left in range(len(first))
            for right in range(len(second))
        ),
        Fraction(0),
    ) / 2


def qtds_momentum_amplitude(
    order: tuple[Momentum, ...], s: Kinematics, *, first_is_plus: bool
) -> Fraction:
    """QTDS recursion for possibly composite on-shell external momenta."""

    def block_momentum(block: tuple[Momentum, ...]) -> Momentum:
        return add_momenta(*block)

    @lru_cache(None)
    def current(block: tuple[Momentum, ...], starts_plus: bool) -> Fraction:
        if len(block) == 1:
            return Fraction(1)
        total = vertex_sum(block, starts_plus)
        momentum = block_momentum(block)
        return total / vector_dot(momentum, momentum, s)

    @lru_cache(None)
    def vertex_sum(block: tuple[Momentum, ...], starts_plus: bool) -> Fraction:
        result = Fraction(0)
        for first_size, second_size, _ in odd_three_splits(len(block)):
            first_end = first_size
            second_end = first_size + second_size
            first_block = block[:first_end]
            second_block = block[first_end:second_end]
            third_block = block[second_end:]
            if starts_plus:
                vertex = -2 * vector_dot(
                    block_momentum(first_block),
                    block_momentum(third_block),
                    s,
                )
            else:
                vertex = 2 * vector_dot(
                    block_momentum(block),
                    block_momentum(second_block),
                    s,
                )
            result += (
                vertex
                * current(first_block, starts_plus)
                * current(second_block, not starts_plus)
                * current(third_block, starts_plus)
            )
        return result

    return vertex_sum(order[:-1], first_is_plus)


def qtds_channel_residue(
    order: Order,
    channel: Order,
    s: Kinematics,
    *,
    first_is_plus: bool,
) -> Fraction:
    """Residue obtained by cutting the selected propagator in every tree."""

    target = frozenset(channel)
    result = Fraction(0)
    for numerator, propagators in qtds_raw_terms(
        order, s, first_is_plus=first_is_plus
    ):
        matching = [
            index
            for index, block in enumerate(propagators)
            if frozenset(block) == target
        ]
        if not matching:
            continue
        assert len(matching) == 1
        denominator = Fraction(1)
        for index, block in enumerate(propagators):
            if index != matching[0]:
                denominator *= channel_invariant(block, s)
        result += numerator / denominator
    return result


def qtds_iterated_residue(
    order: Order,
    channels: tuple[Order, ...],
    s: Kinematics,
    *,
    first_is_plus: bool,
) -> Fraction:
    """Simultaneous residue on a compatible collection of propagators."""

    targets = tuple(frozenset(channel) for channel in channels)
    result = Fraction(0)
    for numerator, propagators in qtds_raw_terms(
        order, s, first_is_plus=first_is_plus
    ):
        propagator_sets = tuple(frozenset(block) for block in propagators)
        if not all(target in propagator_sets for target in targets):
            continue
        denominator = Fraction(1)
        for block, block_set in zip(propagators, propagator_sets, strict=True):
            if block_set not in targets:
                denominator *= channel_invariant(block, s)
        result += numerator / denominator
    return result


@lru_cache(None)
def quartic_tree_count(multiplicity: int) -> int:
    """Number of planar quartic trees with a fixed cyclic ordering."""

    @lru_cache(None)
    def current_count(size: int) -> int:
        if size == 1:
            return 1
        return sum(
            current_count(first) * current_count(second) * current_count(third)
            for first, second, third in odd_three_splits(size)
        )

    return current_count(multiplicity - 1)


def paper_six_point_formula(order: Order, s: Kinematics) -> Fraction:
    """Equation (6) of arXiv:2607.27345 in label-covariant form."""

    k1, k2, k3, k4, k5, k6 = order
    return (
        4
        * momentum_dot((k1,), (k3,), s)
        * momentum_dot((k5,), (k1, k2, k3), s)
        / channel_invariant((k1, k2, k3), s)
        + 4
        * momentum_dot((k1,), (k5,), s)
        * momentum_dot((k3,), (k5, k6, k1), s)
        / channel_invariant((k2, k3, k4), s)
        + 4
        * momentum_dot((k3,), (k5,), s)
        * momentum_dot((k1,), (k3, k4, k5), s)
        / channel_invariant((k3, k4, k5), s)
    )


def matrix_product(first: Matrix, second: Matrix) -> Matrix:
    """Exact rectangular matrix product."""

    assert len(first[0]) == len(second)
    return tuple(
        tuple(
            sum(
                (first[row][middle] * second[middle][column] for middle in range(len(second))),
                Fraction(0),
            )
            for column in range(len(second[0]))
        )
        for row in range(len(first))
    )


def q_map(outer: Matrix, inner: Matrix) -> Matrix:
    """The special rectangular Jordan-pair map Q_outer(inner)=outer inner outer."""

    return matrix_product(matrix_product(outer, inner), outer)


def jordan_fundamental_formula_audit() -> None:
    """Check Q_{Q_x y}=Q_x Q_y Q_x for a rectangular Jordan pair."""

    x: Matrix = (
        (Fraction(1), Fraction(2), Fraction(-1)),
        (Fraction(0), Fraction(3), Fraction(2)),
    )
    y: Matrix = (
        (Fraction(2), Fraction(-1)),
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(3)),
    )
    z: Matrix = (
        (Fraction(1), Fraction(4)),
        (Fraction(-1), Fraction(2)),
        (Fraction(3), Fraction(0)),
    )
    qxy = q_map(x, y)
    left = q_map(qxy, z)
    right = q_map(x, q_map(y, q_map(x, z)))
    assert left == right
    print("rectangular Jordan pair: Q_{Q_x y}=Q_x Q_y Q_x exactly")


def complete_period_reconstruction_audit() -> None:
    """Reconstruct J from a complete six-point basis of QTDS periods."""

    multiplicity = 6
    s = exact_kinematics(multiplicity, 11)
    middle = (1, 2, 3)
    test_basis = [(0,) + item + (4, 5) for item in permutations(middle)]
    expansion_basis = [(0,) + item + (5, 4) for item in permutations(middle)]
    pairing = [
        [double_partial(test, expansion, s) for expansion in expansion_basis]
        for test in test_basis
    ]
    scalar_periods = [scalar_grade(order, s) for order in test_basis]
    convention_sign = (-1) ** (multiplicity // 2 - 1)
    plus_periods = [
        convention_sign * qtds_amplitude(order, s, first_is_plus=True)
        for order in test_basis
    ]
    minus_periods = [
        convention_sign * qtds_amplitude(order, s, first_is_plus=False)
        for order in test_basis
    ]
    assert plus_periods == minus_periods == scalar_periods

    scalar_coordinates = solve(pairing, scalar_periods)
    plus_coordinates = solve(pairing, plus_periods)
    minus_coordinates = solve(pairing, minus_periods)
    assert plus_coordinates == minus_coordinates == scalar_coordinates

    audit_orders = list(
        dict.fromkeys(
            test_basis
            + expansion_basis
            + [
                (0, 1, 4, 2, 5, 3),
                (3, 0, 2, 5, 1, 4),
                (5, 4, 3, 2, 1, 0),
            ]
        )
    )
    for order in audit_orders:
        reconstructed = sum(
            (
                double_partial(order, basis_order, s) * coordinate
                for basis_order, coordinate in zip(
                    expansion_basis, scalar_coordinates, strict=True
                )
            ),
            Fraction(0),
        )
        plus = convention_sign * qtds_amplitude(
            order, s, first_is_plus=True
        )
        minus = convention_sign * qtds_amplitude(
            order, s, first_is_plus=False
        )
        assert reconstructed == plus == minus == scalar_grade(order, s)

    print(
        "n=6: both QTDS polarity families reconstruct the same J coordinate "
        f"from all {len(test_basis)} independent PT periods"
    )


def factorization_audit() -> None:
    """Check cut-bijection counts and exact QTDS residues at six and eight points."""

    samples = (
        (6, 0, 3, 101),
        (6, 1, 3, 102),
        (6, 2, 3, 103),
        (8, 0, 3, 104),
        (8, 1, 3, 105),
        (8, 0, 5, 106),
    )
    for multiplicity, start, size, seed in samples:
        order = tuple(range(multiplicity))
        channel = order[start : start + size]
        s = constrained_channel_kinematics(multiplicity, channel, seed)
        external = tuple(
            momentum_vector(label, multiplicity) for label in order
        )
        channel_momentum = add_momenta(
            *(external[index] for index in range(start, start + size))
        )
        left_order = (
            external[start : start + size]
            + (scale_momentum(-1, channel_momentum),)
        )
        right_order = (
            external[:start]
            + (channel_momentum,)
            + external[start + size :]
        )

        raw_terms = qtds_raw_terms(order, s, first_is_plus=True)
        trees_on_cut = sum(
            any(frozenset(block) == frozenset(channel) for block in propagators)
            for _, propagators in raw_terms
        )
        expected_trees = (
            quartic_tree_count(size + 1)
            * quartic_tree_count(multiplicity - size + 1)
        )
        assert trees_on_cut == expected_trees

        for first_is_plus in (True, False):
            residue = qtds_channel_residue(
                order,
                channel,
                s,
                first_is_plus=first_is_plus,
            )
            left_first_is_plus = (
                first_is_plus if start % 2 == 0 else not first_is_plus
            )
            product = qtds_momentum_amplitude(
                left_order,
                s,
                first_is_plus=left_first_is_plus,
            ) * qtds_momentum_amplitude(
                right_order,
                s,
                first_is_plus=first_is_plus,
            )
            assert residue == product

    print(
        "n=6,8: every audited cut has the quartic-tree product count and "
        "residue = left QTDS period x right QTDS period for both polarities"
    )

    multiplicity = 8
    order = tuple(range(multiplicity))
    inner = order[0:3]
    outer = order[0:5]
    s = constrained_nested_kinematics(multiplicity, inner, outer, 151)
    external = tuple(
        momentum_vector(label, multiplicity) for label in order
    )
    inner_momentum = add_momenta(*external[0:3])
    outer_momentum = add_momenta(*external[0:5])
    first_component = external[0:3] + (
        scale_momentum(-1, inner_momentum),
    )
    middle_component = (
        (inner_momentum,)
        + external[3:5]
        + (scale_momentum(-1, outer_momentum),)
    )
    final_component = (outer_momentum,) + external[5:8]

    raw_terms = qtds_raw_terms(order, s, first_is_plus=True)
    corner_trees = sum(
        all(
            frozenset(channel)
            in tuple(frozenset(block) for block in propagators)
            for channel in (inner, outer)
        )
        for _, propagators in raw_terms
    )
    assert corner_trees == 1
    for first_is_plus in (True, False):
        iterated_residue = qtds_iterated_residue(
            order,
            (inner, outer),
            s,
            first_is_plus=first_is_plus,
        )
        corner_product = (
            qtds_momentum_amplitude(
                first_component,
                s,
                first_is_plus=first_is_plus,
            )
            * qtds_momentum_amplitude(
                middle_component,
                s,
                first_is_plus=first_is_plus,
            )
            * qtds_momentum_amplitude(
                final_component,
                s,
                first_is_plus=first_is_plus,
            )
        )
        assert iterated_residue == corner_product

    print(
        "n=8: the nested 3|3 and 5|3 corner residue is order-independent "
        "and equals the product of three four-point QTDS periods"
    )


def qtds_audit() -> None:
    """Compare QTDS periods with scalar grades and audit polarity dependence."""

    expected_counts = {4: 1, 6: 3, 8: 12, 10: 55, 12: 273}
    actual_counts = {
        multiplicity: quartic_tree_count(multiplicity)
        for multiplicity in expected_counts
    }
    assert actual_counts == expected_counts
    print("quartic tree counts:", actual_counts)

    audit_orders = {
        4: ((0, 1, 2, 3),),
        6: ((0, 1, 2, 3, 4, 5), (1, 4, 0, 3, 5, 2)),
        8: (
            (0, 1, 2, 3, 4, 5, 6, 7),
            (3, 0, 6, 2, 7, 1, 5, 4),
        ),
    }
    for multiplicity, orders in audit_orders.items():
        s = exact_kinematics(multiplicity, 40 + multiplicity)
        for order in orders:
            plus = qtds_amplitude(order, s, first_is_plus=True)
            minus = qtds_amplitude(order, s, first_is_plus=False)
            scalar = scalar_grade(order, s)
            convention_sign = (-1) ** (multiplicity // 2 - 1)
            assert plus == minus == convention_sign * scalar
        print(
            f"n={multiplicity}: both QTDS polarities equal the scalar grade "
            f"on {len(orders)} exact ordering sample(s), up to vertex convention"
        )

    s6 = exact_kinematics(6, 11)
    canonical = tuple(range(6))
    assert qtds_amplitude(canonical, s6) == paper_six_point_formula(canonical, s6)
    plus_terms = qtds_terms(canonical, s6, first_is_plus=True)
    minus_terms = qtds_terms(canonical, s6, first_is_plus=False)
    assert sum(plus_terms.values(), Fraction(0)) == sum(
        minus_terms.values(), Fraction(0)
    )
    assert any(plus_terms[shape] != minus_terms[shape] for shape in plus_terms)
    print("n=6: paper formula reproduced; polarity flips change diagrams but not their sum")

    for multiplicity in (4, 6, 8):
        bipartitions = comb(multiplicity, multiplicity // 2) // 2
        assert bipartitions > 1
        print(
            f"n={multiplicity}: {bipartitions} unordered balanced polarizations; "
            "the bare label set has no invariant choice"
        )


def main() -> None:
    qtds_audit()
    complete_period_reconstruction_audit()
    factorization_audit()
    jordan_fundamental_formula_audit()
    print("all exact QTDS/Jordan lift checks passed")


if __name__ == "__main__":
    main()
