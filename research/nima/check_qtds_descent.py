"""Exact combinatorial audits for local QTDS polarity descent.

This script deliberately stops one level before a scalar twisted-chain lift.
It verifies the finite presentation complex on which such a lift would have
to live:

* at six points, the three quadrangulations form a flip triangle and the
  diagramwise polarity difference has a canonical cyclic local flow;
* at eight points, the twelve quadrangulations form the line graph of the
  octagon's admissible-diagonal graph, with the projective-plane cellulation
  that carries the first square and octagonal coherence tests.

Only standard-library exact arithmetic is used.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations

from check_j_reconstruction import (
    Channel,
    Kinematics,
    Order,
    canonical_channel,
    channel_invariant,
    exact_kinematics,
    triangulations,
)
from check_qtds_lift import (
    constrained_channel_kinematics,
    odd_three_splits,
    qtds_raw_terms,
)


Diagonal = tuple[int, int]
Quadrangulation = tuple[Diagonal, Diagonal]
Flip = tuple[Quadrangulation, Quadrangulation]


class LaurentPolynomial:
    """Tiny exact Laurent-polynomial ring used for symbolic six-point checks."""

    variable_count = 9

    def __init__(self, terms=None):
        self.terms = {
            powers: Fraction(coefficient)
            for powers, coefficient in (terms or {}).items()
            if coefficient
        }

    @classmethod
    def constant(cls, value):
        powers = (0,) * cls.variable_count
        return cls({powers: Fraction(value)}) if value else cls()

    @classmethod
    def variable(cls, index):
        powers = [0] * cls.variable_count
        powers[index] = 1
        return cls({tuple(powers): Fraction(1)})

    @staticmethod
    def coerce(value):
        if isinstance(value, LaurentPolynomial):
            return value
        return LaurentPolynomial.constant(value)

    def __add__(self, other):
        other = self.coerce(other)
        result = dict(self.terms)
        for powers, coefficient in other.terms.items():
            result[powers] = result.get(powers, Fraction(0)) + coefficient
            if not result[powers]:
                del result[powers]
        return LaurentPolynomial(result)

    __radd__ = __add__

    def __neg__(self):
        return LaurentPolynomial(
            {
                powers: -coefficient
                for powers, coefficient in self.terms.items()
            }
        )

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        result = defaultdict(Fraction)
        for first_powers, first_coefficient in self.terms.items():
            for second_powers, second_coefficient in other.terms.items():
                powers = tuple(
                    first + second
                    for first, second in zip(
                        first_powers, second_powers, strict=True
                    )
                )
                result[powers] += first_coefficient * second_coefficient
        return LaurentPolynomial(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        assert len(other.terms) == 1, "division is only needed by a monomial"
        (other_powers, other_coefficient), = other.terms.items()
        return LaurentPolynomial(
            {
                tuple(
                    first - second
                    for first, second in zip(
                        powers, other_powers, strict=True
                    )
                ): coefficient / other_coefficient
                for powers, coefficient in self.terms.items()
            }
        )

    def __pow__(self, exponent):
        assert exponent >= 0
        result = LaurentPolynomial.constant(1)
        for _ in range(exponent):
            result *= self
        return result

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def __bool__(self):
        return bool(self.terms)


def canonical_edge(first, second):
    """Canonical orientation-free encoding of an edge."""

    return tuple(sorted((first, second)))


def diagram_terms(
    order: Order, s: Kinematics, *, first_is_plus: bool
) -> dict[Channel, tuple[Fraction, Fraction, Fraction | None]]:
    """Six-point terms keyed by their unrooted physical channel.

    The tuple is (numerator, propagator, evaluated term).
    """

    result = {}
    for numerator, propagators in qtds_raw_terms(
        order, s, first_is_plus=first_is_plus
    ):
        assert len(propagators) == 1
        channel = canonical_channel(propagators[0], len(order))
        propagator = channel_invariant(propagators[0], s)
        assert channel not in result
        result[channel] = (
            numerator,
            propagator,
            numerator / propagator if propagator else None,
        )
    return result


def channel_without_root(channel: Channel, multiplicity: int) -> Order:
    """Choose the representative of a channel that omits the rooted last leg."""

    if multiplicity - 1 not in channel:
        return tuple(sorted(channel))
    return tuple(sorted(set(range(multiplicity)) - set(channel)))


def six_point_flip_flow_audit() -> None:
    """Construct the canonical triangle flow for the polarity difference."""

    multiplicity = 6
    order = tuple(range(multiplicity))
    for seed in (11, 17, 29):
        s = exact_kinematics(multiplicity, seed)
        plus = diagram_terms(order, s, first_is_plus=True)
        minus = diagram_terms(order, s, first_is_plus=False)
        assert plus.keys() == minus.keys()
        assert len(plus) == 3

        difference = {
            channel: plus[channel][2] - minus[channel][2]
            for channel in plus
        }
        assert sum(difference.values(), Fraction(0)) == 0

        # On its pole, each endpoint diagram has the same four-point residue.
        # Hence the numerator difference is a contact term divisible by X_D.
        for index, channel in enumerate(
            sorted(plus, key=lambda item: tuple(sorted(item)))
        ):
            representative = channel_without_root(channel, multiplicity)
            channel_s = constrained_channel_kinematics(
                multiplicity, representative, seed * 10 + index
            )
            channel_plus = diagram_terms(
                order, channel_s, first_is_plus=True
            )
            channel_minus = diagram_terms(
                order, channel_s, first_is_plus=False
            )
            assert channel_plus[channel][0] == channel_minus[channel][0]

        # The basepoint-free solution is the inverse graph Laplacian on the
        # sum-zero subspace of the triangle:
        # H_ij=(c_i-c_j)/3 and div(H)=c.
        vertices = sorted(difference, key=lambda item: tuple(sorted(item)))
        flow = {
            (first, second): (
                difference[first] - difference[second]
            ) / 3
            for first, second in combinations(vertices, 2)
        }
        boundary = defaultdict(Fraction)
        for (first, second), coefficient in flow.items():
            boundary[first] += coefficient
            boundary[second] -= coefficient
        assert dict(boundary) == difference

        # A one-step cyclic rotation exchanges the two alternating lifts.
        rotated = order[1:] + order[:1]
        rotated_plus = diagram_terms(rotated, s, first_is_plus=True)
        rotated_minus = diagram_terms(rotated, s, first_is_plus=False)
        assert {
            channel: data[2] for channel, data in rotated_plus.items()
        } == {
            channel: data[2] for channel, data in minus.items()
        }
        assert {
            channel: data[2] for channel, data in rotated_minus.items()
        } == {
            channel: data[2] for channel, data in plus.items()
        }
        rotated_difference = {
            channel: rotated_plus[channel][2] - rotated_minus[channel][2]
            for channel in rotated_plus
        }
        assert rotated_difference == {
            channel: -value for channel, value in difference.items()
        }

    print(
        "n=6: the polarity difference is a three-contact sum with a "
        "canonical cyclic local flow; one-step rotation reverses it"
    )


def symbolic_six_point_kinematics():
    """Formal six-point Mandelstams in nine independent planar variables."""

    x = tuple(LaurentPolynomial.variable(index) for index in range(6))
    y = tuple(
        LaurentPolynomial.variable(6 + index) for index in range(3)
    )
    zero = LaurentPolynomial.constant(0)
    s = [[zero for _ in range(6)] for _ in range(6)]

    def assign(first, second, value):
        first %= 6
        second %= 6
        if s[first][second]:
            assert s[first][second] == value
        s[first][second] = value
        s[second][first] = value

    for index in range(6):
        assign(index, index + 1, x[index])
        assign(
            index,
            index + 2,
            y[index % 3] - x[index] - x[(index + 1) % 6],
        )
        assign(
            index,
            index + 3,
            x[(index + 1) % 6]
            + x[(index + 4) % 6]
            - y[index % 3]
            - y[(index + 1) % 3],
        )
    assert all(sum(row, zero) == zero for row in s)
    return x, y, s


def symbolic_scalar_grade_groups():
    """Grade the fourteen scalar triangulations before summing channels."""

    order = tuple(range(6))
    x, y, _ = symbolic_six_point_kinematics()
    zero = LaurentPolynomial.constant(0)
    one = LaurentPolynomial.constant(1)
    groups = defaultdict(lambda: zero)

    def variable_for_channel(channel):
        labels = set(channel)
        if len(labels) == 2:
            start = next(
                index
                for index in range(6)
                if labels == {index, (index + 1) % 6}
            )
            return x[start], None
        assert len(labels) == 3
        start = next(
            index
            for index in range(6)
            if labels
            == {
                index,
                (index + 1) % 6,
                (index + 2) % 6,
            }
        )
        return y[start % 3], start % 3

    for triangulation in triangulations(tuple(range(6))):
        series = {0: one}
        physical_channel = None
        for start, end in triangulation:
            channel = canonical_channel(order[start:end], 6)
            variable, physical_index = variable_for_channel(channel)
            if physical_index is not None:
                assert physical_channel is None
                physical_channel = physical_index
                factor = {0: one / variable}
            else:
                shift_sign = 1 if start % 2 else -1
                factor = {
                    degree: (
                        Fraction((-1) ** (degree - 1), shift_sign**degree)
                        * variable ** (degree - 1)
                    )
                    for degree in range(1, 5)
                }
            product = defaultdict(lambda: zero)
            for first_degree, first_value in series.items():
                for second_degree, second_value in factor.items():
                    if first_degree + second_degree <= 4:
                        product[first_degree + second_degree] += (
                            first_value * second_value
                        )
            series = dict(product)
        groups[physical_channel] += series.get(4, zero)
    return x, dict(groups)


def six_point_scalar_cell_audit() -> None:
    """Derive QTDS contact allocation from scalar cubic-tree grade cells."""

    order = tuple(range(6))
    x, scalar_groups = symbolic_scalar_grade_groups()
    _, _, s = symbolic_six_point_kinematics()
    zero = LaurentPolynomial.constant(0)

    assert scalar_groups[None] == -sum(x, zero)
    predicted_contacts = {
        True: {
            0: -(x[3] + x[4]),
            1: -(x[1] + x[2]),
            2: -(x[5] + x[0]),
        },
        False: {
            0: -(x[0] + x[1]),
            1: -(x[4] + x[5]),
            2: -(x[2] + x[3]),
        },
    }
    for first_is_plus in (True, False):
        qtds_by_channel = {}
        for numerator, propagators in qtds_raw_terms(
            order, s, first_is_plus=first_is_plus
        ):
            assert len(propagators) == 1
            block = propagators[0]
            channel_index = block[0] % 3
            term = numerator / channel_invariant(block, s)
            qtds_by_channel[channel_index] = term
        assert set(qtds_by_channel) == {0, 1, 2}
        for channel_index in range(3):
            assert (
                qtds_by_channel[channel_index]
                == scalar_groups[channel_index]
                + predicted_contacts[first_is_plus][channel_index]
            )
        assert (
            sum(
                predicted_contacts[first_is_plus].values(),
                zero,
            )
            == scalar_groups[None]
        )

    print(
        "n=6 symbolic: the scalar cubic grade is 3 four-tree channel "
        "fibers plus 2 central trees; QTDS is the exact local redistribution "
        "of their contact sum for either polarity"
    )


def admissible_octagon_diagonals() -> tuple[Diagonal, ...]:
    """Diagonals that split an octagon into two even polygons."""

    multiplicity = 8
    return tuple(
        sorted(
            {
                tuple(sorted((vertex, (vertex + 3) % multiplicity)))
                for vertex in range(multiplicity)
            }
        )
    )


def strictly_between(vertex: int, first: int, second: int) -> bool:
    """Whether vertex lies on the open clockwise arc first -> second."""

    multiplicity = 8
    return 0 < (vertex - first) % multiplicity < (
        second - first
    ) % multiplicity


def diagonals_cross(first: Diagonal, second: Diagonal) -> bool:
    """Test crossing in the interior of the labelled octagon."""

    first_start, first_end = first
    second_start, second_end = second
    return (
        strictly_between(second_start, first_start, first_end)
        != strictly_between(second_end, first_start, first_end)
        and strictly_between(first_start, second_start, second_end)
        != strictly_between(first_end, second_start, second_end)
    )


def octagon_compatibility_graph():
    """Return the 2-divisible A2 compatibility graph."""

    diagonals = admissible_octagon_diagonals()
    edges = tuple(
        canonical_edge(first, second)
        for first, second in combinations(diagonals, 2)
        if not diagonals_cross(first, second)
    )
    return diagonals, edges


def mobius_cycle(diagonals, edges):
    """Find the 8-cycle whose complementary edges are antipodal matchings."""

    start = diagonals[0]
    for tail in permutations(diagonals[1:]):
        cycle = (start,) + tail
        cycle_edges = {
            canonical_edge(cycle[index], cycle[(index + 1) % 8])
            for index in range(8)
        }
        if not cycle_edges <= set(edges):
            continue
        matching = set(edges) - cycle_edges
        positions = {
            diagonal: index for index, diagonal in enumerate(cycle)
        }
        if len(matching) == 4 and all(
            (positions[first] - positions[second]) % 8 == 4
            for first, second in matching
        ):
            return cycle, tuple(sorted(matching))
    raise AssertionError("the compatibility graph is not the expected Mobius ladder")


def quadrangulation_cellulation():
    """Build the line-graph cellulation of the full octagon complex."""

    diagonals, compatibility_edges = octagon_compatibility_graph()
    quadrangulations = tuple(sorted(compatibility_edges))
    flips = tuple(
        canonical_edge(first, second)
        for first, second in combinations(quadrangulations, 2)
        if len(set(first) & set(second)) == 1
    )
    cycle, matching = mobius_cycle(diagonals, compatibility_edges)

    triangles = []
    for diagonal in diagonals:
        incident = tuple(
            sorted(
                quadrangulation
                for quadrangulation in quadrangulations
                if diagonal in quadrangulation
            )
        )
        assert len(incident) == 3
        triangles.append(incident)

    original_squares = tuple(
        (
            cycle[index],
            cycle[(index + 1) % 8],
            cycle[(index + 5) % 8],
            cycle[(index + 4) % 8],
        )
        for index in range(4)
    )

    def medial_face(original_face):
        return tuple(
            canonical_edge(
                original_face[index],
                original_face[(index + 1) % len(original_face)],
            )
            for index in range(len(original_face))
        )

    squares = tuple(medial_face(face) for face in original_squares)
    octagon = medial_face(cycle)
    faces = tuple(triangles) + squares + (octagon,)
    return (
        diagonals,
        compatibility_edges,
        cycle,
        matching,
        quadrangulations,
        flips,
        faces,
    )


def matrix_rank(matrix, modulus: int | None = None) -> int:
    """Row rank over Q or a prime field."""

    if not matrix:
        return 0
    data = [
        [
            value % modulus if modulus else Fraction(value)
            for value in row
        ]
        for row in matrix
    ]
    row_count = len(data)
    column_count = len(data[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if data[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        pivot_value = data[pivot_row][column]
        inverse = (
            pow(int(pivot_value), -1, modulus)
            if modulus
            else Fraction(1, 1) / pivot_value
        )
        data[pivot_row] = [
            value * inverse % modulus if modulus else value * inverse
            for value in data[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row or data[row][column] == 0:
                continue
            coefficient = data[row][column]
            data[row] = [
                (
                    (data[row][index] - coefficient * data[pivot_row][index])
                    % modulus
                    if modulus
                    else data[row][index]
                    - coefficient * data[pivot_row][index]
                )
                for index in range(column_count)
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def multiply_matrices(first, second):
    """Small exact matrix product."""

    return [
        [
            sum(
                (
                    first[row][middle] * second[middle][column]
                    for middle in range(len(second))
                ),
                0,
            )
            for column in range(len(second[0]))
        ]
        for row in range(len(first))
    ]


def octagon_cellulation_audit() -> None:
    """Verify the RP2 medial cellulation and its coefficient sensitivity."""

    (
        diagonals,
        compatibility_edges,
        cycle,
        matching,
        quadrangulations,
        flips,
        faces,
    ) = quadrangulation_cellulation()
    assert len(diagonals) == 8
    assert len(compatibility_edges) == 12
    assert len(cycle) == 8
    assert len(matching) == 4
    compatibility_degree = Counter(
        diagonal for edge in compatibility_edges for diagonal in edge
    )
    assert set(compatibility_degree.values()) == {3}

    assert len(quadrangulations) == 12
    assert len(flips) == 24
    flip_degree = Counter(
        quadrangulation for edge in flips for quadrangulation in edge
    )
    assert set(flip_degree.values()) == {4}
    assert [len(face) for face in faces] == [3] * 8 + [4] * 4 + [8]

    face_edge_counts = Counter()
    for face in faces:
        for index, vertex in enumerate(face):
            edge = canonical_edge(vertex, face[(index + 1) % len(face)])
            assert edge in flips
            face_edge_counts[edge] += 1
    assert set(face_edge_counts) == set(flips)
    assert set(face_edge_counts.values()) == {2}
    assert len(quadrangulations) - len(flips) + len(faces) == 1

    # Each vertex link is one four-cycle, so this is a closed connected
    # combinatorial surface rather than merely a two-dimensional pseudocomplex.
    for vertex in quadrangulations:
        link_edges = []
        for face in faces:
            if vertex not in face:
                continue
            position = face.index(vertex)
            link_edges.append(
                canonical_edge(
                    face[position - 1],
                    face[(position + 1) % len(face)],
                )
            )
        assert len(link_edges) == 4
        link_degree = Counter(
            neighbor for edge in link_edges for neighbor in edge
        )
        assert len(link_degree) == 4
        assert set(link_degree.values()) == {2}

    vertex_index = {
        vertex: index for index, vertex in enumerate(quadrangulations)
    }
    edge_index = {edge: index for index, edge in enumerate(flips)}
    boundary_one = [
        [0 for _ in flips] for _ in quadrangulations
    ]
    for column, (first, second) in enumerate(flips):
        boundary_one[vertex_index[first]][column] = -1
        boundary_one[vertex_index[second]][column] = 1

    boundary_two = [[0 for _ in faces] for _ in flips]
    for column, face in enumerate(faces):
        for index, first in enumerate(face):
            second = face[(index + 1) % len(face)]
            edge = canonical_edge(first, second)
            sign = 1 if edge == (first, second) else -1
            boundary_two[edge_index[edge]][column] += sign
    assert all(
        value == 0
        for row in multiply_matrices(boundary_one, boundary_two)
        for value in row
    )

    rational_ranks = (
        matrix_rank(boundary_one),
        matrix_rank(boundary_two),
    )
    mod_two_ranks = (
        matrix_rank(boundary_one, 2),
        matrix_rank(boundary_two, 2),
    )
    assert rational_ranks == (11, 13)
    assert mod_two_ranks == (11, 12)
    rational_betti = (
        len(quadrangulations) - rational_ranks[0],
        len(flips) - rational_ranks[0] - rational_ranks[1],
        len(faces) - rational_ranks[1],
    )
    mod_two_betti = (
        len(quadrangulations) - mod_two_ranks[0],
        len(flips) - mod_two_ranks[0] - mod_two_ranks[1],
        len(faces) - mod_two_ranks[1],
    )
    assert rational_betti == (1, 0, 0)
    assert mod_two_betti == (1, 1, 1)

    print(
        "n=8: 12 quadrangulations and 24 flips form a closed cellulation "
        "with 8 triangles, 4 squares, 1 octagon, and Euler characteristic 1"
    )
    print(
        "n=8: Betti numbers are (1,0,0) over Q and (1,1,1) over F2; "
        "the projective-plane Z2 sector cannot be discarded"
    )


def scalar_parity_core_audit() -> None:
    """Relate scalar triangulations to partial quadrangulation cores."""

    counts_by_multiplicity = {}
    for multiplicity in (6, 8, 10):
        counts = Counter()
        for triangulation in triangulations(tuple(range(multiplicity))):
            allowed = tuple(
                diagonal
                for diagonal in triangulation
                if (diagonal[0] - diagonal[1]) % 2
            )
            counts[len(allowed)] += 1
        counts_by_multiplicity[multiplicity] = dict(counts)
    assert counts_by_multiplicity == {
        6: {1: 12, 0: 2},
        8: {2: 96, 1: 32, 0: 4},
        10: {3: 880, 2: 440, 1: 100, 0: 10},
    }

    (
        admissible,
        _,
        _,
        _,
        quadrangulations,
        _,
        faces,
    ) = quadrangulation_cellulation()
    full_core_counts = Counter()
    one_core_counts = Counter()
    central_triangulations = []
    for triangulation in triangulations(tuple(range(8))):
        allowed = tuple(
            sorted(
                diagonal
                for diagonal in triangulation
                if (diagonal[0] - diagonal[1]) % 2
            )
        )
        if len(allowed) == 2:
            assert allowed in quadrangulations
            full_core_counts[allowed] += 1
        elif len(allowed) == 1:
            assert allowed[0] in admissible
            one_core_counts[allowed[0]] += 1
        else:
            assert not allowed
            central_triangulations.append(triangulation)

    assert set(full_core_counts.values()) == {8}
    assert set(full_core_counts) == set(quadrangulations)
    assert set(one_core_counts.values()) == {4}
    assert set(one_core_counts) == set(admissible)
    assert len(central_triangulations) == 4

    square_vertex_sets = {
        frozenset(face) for face in faces[8:12]
    }
    central_diameters = set()
    for triangulation in central_triangulations:
        diameters = tuple(
            diagonal
            for diagonal in triangulation
            if diagonal[1] - diagonal[0] == 4
        )
        assert len(diameters) == 1
        diameter = diameters[0]
        central_diameters.add(diameter)
        compatible_quadrangulations = frozenset(
            quadrangulation
            for quadrangulation in quadrangulations
            if all(
                not diagonals_cross(diameter, diagonal)
                for diagonal in quadrangulation
            )
        )
        assert compatible_quadrangulations in square_vertex_sets
    assert central_diameters == {
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    }

    print(
        "scalar parity cores: n=6 {1:12,0:2}, "
        "n=8 {2:96,1:32,0:4}, n=10 {3:880,2:440,1:100,0:10}"
    )
    print(
        "n=8 scalar cells: each quadrangulation has 8 cubic refinements, "
        "each one-channel core has 4, and the 4 central triangulations "
        "canonically label the 4 square coherence faces"
    )


def ternary_presentations() -> dict[Quadrangulation, tuple]:
    """Root the twelve octagon quadrangulations as signed ternary words."""

    multiplicity = 8
    order = tuple(range(multiplicity))

    @lru_cache(None)
    def current_trees(block: Order, starts_plus: bool):
        if len(block) == 1:
            return ((block[0], ()),)
        return tuple(
            (expression, (block,) + propagators)
            for expression, propagators in vertex_trees(block, starts_plus)
        )

    @lru_cache(None)
    def vertex_trees(block: Order, starts_plus: bool):
        result = []
        operation = "T+" if starts_plus else "T-"
        for first_size, second_size, _ in odd_three_splits(len(block)):
            first_end = first_size
            second_end = first_size + second_size
            first_block = block[:first_end]
            second_block = block[first_end:second_end]
            third_block = block[second_end:]
            for first_expression, first_propagators in current_trees(
                first_block, starts_plus
            ):
                for second_expression, second_propagators in current_trees(
                    second_block, not starts_plus
                ):
                    for third_expression, third_propagators in current_trees(
                        third_block, starts_plus
                    ):
                        result.append(
                            (
                                (
                                    operation,
                                    first_expression,
                                    second_expression,
                                    third_expression,
                                ),
                                first_propagators
                                + second_propagators
                                + third_propagators,
                            )
                        )
        return tuple(result)

    diagonal_to_channel = {
        diagonal: canonical_channel(
            tuple(range(diagonal[0], diagonal[1])),
            multiplicity,
        )
        for diagonal in admissible_octagon_diagonals()
    }
    channel_pair_to_quadrangulation = {
        frozenset(diagonal_to_channel[diagonal] for diagonal in quadrangulation):
        quadrangulation
        for quadrangulation in quadrangulation_cellulation()[4]
    }
    result = {}
    for expression, propagators in vertex_trees(order[:-1], True):
        channel_pair = frozenset(
            canonical_channel(block, multiplicity) for block in propagators
        )
        quadrangulation = channel_pair_to_quadrangulation[channel_pair]
        assert quadrangulation not in result
        result[quadrangulation] = expression
    assert len(result) == 12
    return result


def substitute_expression(expression, replacements):
    """Substitute leaf symbols in a ternary-word syntax tree."""

    if isinstance(expression, int):
        return replacements[expression]
    return (
        expression[0],
        substitute_expression(expression[1], replacements),
        substitute_expression(expression[2], replacements),
        substitute_expression(expression[3], replacements),
    )


def jordan_defect_location_audit() -> None:
    """Locate the quadratic Jordan fundamental formula in the flip complex."""

    (
        _,
        _,
        cycle,
        _,
        quadrangulations,
        flips,
        _,
    ) = quadrangulation_cellulation()
    outer = tuple(
        canonical_edge(cycle[index], cycle[(index + 1) % 8])
        for index in range(8)
    )
    matching = tuple(
        canonical_edge(cycle[index], cycle[index + 4])
        for index in range(4)
    )
    presentations = ternary_presentations()
    replacements = {
        0: "x",
        1: "y",
        2: "x",
        3: "z",
        4: "x",
        5: "y",
        6: "x",
    }
    left = substitute_expression(presentations[matching[0]], replacements)
    right = substitute_expression(presentations[matching[2]], replacements)
    qxy = ("T+", "x", "y", "x")
    qxz = ("T+", "x", "z", "x")
    expected_left = ("T+", qxy, "z", qxy)
    expected_right = (
        "T+",
        "x",
        ("T-", "y", qxz, "y"),
        "x",
    )
    assert left == expected_left
    assert right == expected_right

    adjacency = {vertex: set() for vertex in quadrangulations}
    for first, second in flips:
        adjacency[first].add(second)
        adjacency[second].add(first)
    paths = []

    def visit(vertex, path):
        if len(path) > 4:
            return
        if vertex == matching[2]:
            paths.append(tuple(path))
            return
        for neighbor in adjacency[vertex]:
            if neighbor not in path:
                visit(neighbor, path + [neighbor])

    visit(matching[0], [matching[0]])
    shortest_size = min(len(path) for path in paths)
    shortest_paths = {
        path for path in paths if len(path) == shortest_size
    }
    assert shortest_size == 4
    assert len(shortest_paths) == 4
    assert {
        tuple(path[1:3]) for path in shortest_paths
    } == {
        (outer[0], outer[1]),
        (outer[3], outer[2]),
        (outer[4], outer[5]),
        (outer[7], outer[6]),
    }

    print(
        "n=8: B0 and B2 specialize to Q_{Q_x y}z and "
        "Q_x Q_y Q_x z and are connected by four shortest three-flip paths"
    )


def main() -> None:
    six_point_flip_flow_audit()
    six_point_scalar_cell_audit()
    octagon_cellulation_audit()
    scalar_parity_core_audit()
    jordan_defect_location_audit()
    print("all exact QTDS descent-complex checks passed")


if __name__ == "__main__":
    main()
