"""Independent twelve-point QTDS verification of scalar sink contacts.

The scalar target is constructed from alternating polygon geometry alone:
enumerate the 273 dodecagon quadrangulations, direct each dual tree by the
alternating coorientation, and take the two diagonals of its unique sink.

Only after that construction does the audit expand the 273 QTDS numerator
terms in the 54-variable formal planar kinematic ring.  The two occurrence
tables are compared diagram, marked diagonal, and coefficient at a time.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from check_eight_point_transfer import (
    negative_support,
    planar_symbolic_kinematics,
    select_terms,
)
from check_j_reconstruction import canonical_channel, triangulations
from check_qtds_lift import qtds_raw_terms


MULTIPLICITY = 12

Diagonal = tuple[int, int]
Quadrangulation = tuple[Diagonal, ...]
Cell = tuple[int, int, int, int]


def boundary_edges() -> frozenset[Diagonal]:
    """Boundary edges of the labelled dodecagon."""

    return frozenset(
        tuple(sorted((vertex, (vertex + 1) % MULTIPLICITY)))
        for vertex in range(MULTIPLICITY)
    )


def physical_diagonals() -> tuple[Diagonal, ...]:
    """Diagonals splitting the dodecagon into two even polygons."""

    boundary = boundary_edges()
    result = tuple(
        diagonal
        for diagonal in combinations(range(MULTIPLICITY), 2)
        if diagonal not in boundary and (diagonal[0] - diagonal[1]) % 2
    )
    assert len(result) == 24
    return result


def diagonals_cross(first: Diagonal, second: Diagonal) -> bool:
    """Whether two canonical dodecagon diagonals cross."""

    first_start, first_end = first
    second_start, second_end = second
    return (
        first_start < second_start < first_end < second_end
        or second_start < first_start < second_end < first_end
    )


def quadrangulations() -> tuple[Quadrangulation, ...]:
    """All noncrossing four-diagonal dodecagon quadrangulations."""

    result = tuple(
        candidate
        for candidate in combinations(physical_diagonals(), 4)
        if all(
            not diagonals_cross(first, second)
            for first, second in combinations(candidate, 2)
        )
    )
    assert len(result) == 273
    return result


def quadrangulation_cells(quadrangulation: Quadrangulation) -> tuple[Cell, ...]:
    """The five quadrilateral regions cut out by a quadrangulation."""

    edges = set(quadrangulation) | set(boundary_edges())
    cells = tuple(
        vertices
        for vertices in combinations(range(MULTIPLICITY), 4)
        if all(
            tuple(
                sorted(
                    (
                        vertices[index],
                        vertices[(index + 1) % 4],
                    )
                )
            )
            in edges
            for index in range(4)
        )
    )
    assert len(cells) == 5
    return cells


def cell_side(diagonal: Diagonal, cell: Cell) -> int:
    """Return 0 on the increasing-arc side and 1 on its complement."""

    first, second = diagonal
    increasing_arc = set(range(first + 1, second))
    other_vertices = set(cell) - set(diagonal)
    if other_vertices <= increasing_arc:
        return 0
    assert other_vertices.isdisjoint(increasing_arc)
    return 1


def alternating_coorientation(
    diagonal: Diagonal, *, first_is_plus: bool
) -> int:
    """The same endpoint-coloring coorientation as at eight and ten points."""

    first, second = diagonal
    plus_side = 1 if first % 2 == 0 else 0
    return plus_side if first_is_plus else 1 - plus_side


def sink_contact_slots(
    quadrangulation: Quadrangulation, *, first_is_plus: bool
) -> frozenset[Diagonal]:
    """Two scalar diagonals of the unique cooriented dual-tree sink."""

    cells = quadrangulation_cells(quadrangulation)
    outdegree = Counter()
    for diagonal in quadrangulation:
        adjacent = tuple(
            cell for cell in cells if set(diagonal) <= set(cell)
        )
        assert len(adjacent) == 2
        side = alternating_coorientation(
            diagonal, first_is_plus=first_is_plus
        )
        target = next(
            cell
            for cell in adjacent
            if cell_side(diagonal, cell) == side
        )
        source = next(cell for cell in adjacent if cell != target)
        outdegree[source] += 1
    sinks = tuple(cell for cell in cells if not outdegree[cell])
    if len(sinks) != 1:
        return frozenset()
    first, second, third, fourth = sinks[0]
    return frozenset(
        (
            tuple(sorted((first, third))),
            tuple(sorted((second, fourth))),
        )
    )


def scalar_zero_core_coefficients():
    """Marked t^10 coefficients of the all-shifted scalar cells."""

    result = {}
    zero_core_cells = tuple(
        triangulation
        for triangulation in triangulations(tuple(range(MULTIPLICITY)))
        if not any(
            (diagonal[0] - diagonal[1]) % 2
            for diagonal in triangulation
        )
    )
    assert len(zero_core_cells) == 28
    for triangulation in zero_core_cells:
        signs = {
            diagonal: (1 if diagonal[0] % 2 else -1)
            for diagonal in triangulation
        }
        base_sign = 1
        for sign in signs.values():
            base_sign *= sign
        for mark, sign in signs.items():
            result[(triangulation, mark)] = -base_sign * sign
    assert len(result) == 252
    assert set(result.values()) == {-1}
    return result


def scalar_sink_coefficients(*, first_is_plus: bool):
    """Target-independent scalar-derived contact occurrence table."""

    result = {}
    for quadrangulation in quadrangulations():
        for mark in sink_contact_slots(
            quadrangulation, first_is_plus=first_is_plus
        ):
            result[(quadrangulation, mark)] = -1
    assert len(result) == 252
    return result


def qtds_contact_coefficients(*, first_is_plus: bool):
    """Polynomial contacts of the independently expanded QTDS recursion."""

    diagonals, variables, kinematics = planar_symbolic_kinematics(
        MULTIPLICITY
    )
    polynomial_type = type(next(iter(variables.values())))
    channel_to_diagonal = {}
    for diagonal in physical_diagonals():
        start, end = diagonal
        channel = canonical_channel(
            tuple(range(start, end)), MULTIPLICITY
        )
        assert channel not in channel_to_diagonal
        channel_to_diagonal[channel] = diagonal

    result = {}
    diagram_count = 0
    convention_sign = (-1) ** (MULTIPLICITY // 2 - 1)
    for numerator, propagators in qtds_raw_terms(
        tuple(range(MULTIPLICITY)),
        kinematics,
        first_is_plus=first_is_plus,
    ):
        assert len(propagators) == 4
        denominator = polynomial_type.constant(1)
        diagram_diagonals = []
        for block in propagators:
            diagonal = channel_to_diagonal[
                canonical_channel(block, MULTIPLICITY)
            ]
            diagram_diagonals.append(diagonal)
            denominator *= variables[diagonal]
        quadrangulation = tuple(sorted(diagram_diagonals))
        assert quadrangulation in quadrangulations()
        diagram_count += 1
        diagram = convention_sign * numerator / denominator
        contact = select_terms(
            diagram, lambda powers: not negative_support(powers)
        )
        for powers, coefficient in contact.terms.items():
            support = tuple(
                index
                for index, exponent in enumerate(powers)
                if exponent
            )
            assert len(support) == 1
            assert powers[support[0]] == 1
            key = (quadrangulation, diagonals[support[0]])
            assert key not in result
            result[key] = coefficient
    assert diagram_count == 273
    assert len(result) == 252
    assert set(result.values()) == {-1}
    return result


def main() -> None:
    source = scalar_zero_core_coefficients()
    source_multiplicity = Counter(
        mark for _, mark in source
    )
    for polarity in (True, False):
        scalar = scalar_sink_coefficients(first_is_plus=polarity)
        qtds = qtds_contact_coefficients(first_is_plus=polarity)
        assert scalar == qtds
        assert Counter(mark for _, mark in scalar) == source_multiplicity

    print(
        "n=12 scalar grade: 28 zero-core cells give 252 marked "
        "coefficient -1 sources"
    )
    print(
        "n=12 QTDS: all 273 symbolic diagrams expanded for both "
        "polarities; their 252 contacts agree occurrence-by-occurrence "
        "with the scalar unique-sink rule"
    )
    print("all exact twelve-point QTDS contact checks passed")


if __name__ == "__main__":
    main()
