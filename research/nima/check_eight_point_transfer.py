"""Exact eight-point scalar-cell/QTDS transfer audit.

This script works in the 20-variable formal planar kinematic space.  It
retains every scalar triangulation while taking the sixth alternating grade,
groups the result by parity core, and compares those groups diagram by
diagram with the two QTDS polarities.

The immediate questions are:

* do full-core scalar fibers supply the double-pole part of each QTDS term?
* do one-core scalar fibers redistribute only within their factorization
  triangles?
* do zero-core scalar cells supply exactly the remaining contacts?

Only standard-library sparse Laurent-polynomial arithmetic is used.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations

from check_j_reconstruction import canonical_channel, triangulations
from check_qtds_descent import (
    LaurentPolynomial,
    admissible_octagon_diagonals,
    canonical_edge,
    diagonals_cross,
    quadrangulation_cellulation,
)
from check_qtds_lift import qtds_raw_terms


Diagonal = tuple[int, int]
Quadrangulation = tuple[Diagonal, Diagonal]


def planar_symbolic_kinematics(multiplicity: int = 8):
    """Return formal planar variables and the induced Mandelstam matrix."""

    diagonals = tuple(
        (first, second)
        for first, second in combinations(range(multiplicity), 2)
        if (second - first) not in (1, multiplicity - 1)
    )
    assert len(diagonals) == multiplicity * (multiplicity - 3) // 2
    LaurentPolynomial.variable_count = len(diagonals)
    variables = {
        diagonal: LaurentPolynomial.variable(index)
        for index, diagonal in enumerate(diagonals)
    }
    zero = LaurentPolynomial.constant(0)

    def planar(first: int, second: int):
        first %= multiplicity
        second %= multiplicity
        if first == second or (first - second) % multiplicity in (1, multiplicity - 1):
            return zero
        return variables[tuple(sorted((first, second)))]

    s = [[zero for _ in range(multiplicity)] for _ in range(multiplicity)]
    for first, second in combinations(range(multiplicity), 2):
        value = (
            planar(first, second + 1)
            + planar(first + 1, second)
            - planar(first, second)
            - planar(first + 1, second + 1)
        )
        s[first][second] = value
        s[second][first] = value
    assert all(sum(row, zero) == zero for row in s)
    return diagonals, variables, s


def multiply_series(first, second, maximum_degree):
    """Multiply exact Laurent-polynomial series in the scalar parameter."""

    zero = LaurentPolynomial.constant(0)
    result = defaultdict(lambda: zero)
    for first_degree, first_value in first.items():
        for second_degree, second_value in second.items():
            degree = first_degree + second_degree
            if degree <= maximum_degree:
                result[degree] += first_value * second_value
    return dict(result)


def scalar_grade_by_core(variables):
    """Take the t^6 scalar grade before forgetting triangulation cells."""

    target_degree = 6
    zero = LaurentPolynomial.constant(0)
    one = LaurentPolynomial.constant(1)
    groups = defaultdict(lambda: zero)
    individual = {}
    for triangulation in triangulations(tuple(range(8))):
        core = tuple(
            sorted(
                diagonal
                for diagonal in triangulation
                if (diagonal[0] - diagonal[1]) % 2
            )
        )
        series = {0: one}
        for start, end in triangulation:
            variable = variables[(start, end)]
            if (start - end) % 2:
                factor = {0: one / variable}
            else:
                shift_sign = 1 if start % 2 else -1
                factor = {
                    degree: (
                        Fraction((-1) ** (degree - 1), shift_sign**degree)
                        * variable ** (degree - 1)
                    )
                    for degree in range(1, target_degree + 1)
                }
            series = multiply_series(series, factor, target_degree)
        value = series.get(target_degree, zero)
        groups[core] += value
        individual[triangulation] = value
    return dict(groups), individual


def channel_diagonal_map():
    """Map rooted QTDS propagator channels to physical octagon diagonals."""

    result = {}
    for diagonal in admissible_octagon_diagonals():
        start, end = diagonal
        channel = canonical_channel(tuple(range(start, end)), 8)
        assert channel not in result
        result[channel] = diagonal
    return result


def qtds_diagrams(s, variables, *, first_is_plus: bool):
    """Return the twelve QTDS terms keyed by their quadrangulations."""

    channel_to_diagonal = channel_diagonal_map()
    result = {}
    for numerator, propagators in qtds_raw_terms(
        tuple(range(8)), s, first_is_plus=first_is_plus
    ):
        assert len(propagators) == 2
        diagonals = []
        denominator = LaurentPolynomial.constant(1)
        for block in propagators:
            channel = canonical_channel(block, 8)
            diagonal = channel_to_diagonal[channel]
            diagonals.append(diagonal)
            denominator *= variables[diagonal]
        quadrangulation = tuple(sorted(diagonals))
        assert quadrangulation not in result
        convention_sign = (-1) ** (8 // 2 - 1)
        result[quadrangulation] = (
            convention_sign * numerator / denominator
        )
    assert len(result) == 12
    return result


def select_terms(polynomial, predicate):
    """Select Laurent monomials satisfying a predicate on exponent tuples."""

    return LaurentPolynomial(
        {
            powers: coefficient
            for powers, coefficient in polynomial.terms.items()
            if predicate(powers)
        }
    )


def negative_support(powers):
    """Indices of variables appearing in a Laurent denominator."""

    return tuple(index for index, exponent in enumerate(powers) if exponent < 0)


def scalar_flip_graph(triangulation_list):
    """The one-skeleton of the scalar associahedron."""

    adjacency = {triangulation: set() for triangulation in triangulation_list}
    for first, second in combinations(triangulation_list, 2):
        if len(first ^ second) == 2:
            adjacency[first].add(second)
            adjacency[second].add(first)
    return adjacency


def rotate_diagonal(diagonal, amount=1):
    """Rotate an unoriented octagon diagonal."""

    return tuple(sorted(((diagonal[0] + amount) % 8, (diagonal[1] + amount) % 8)))


def minimum_contact_matching(
    contact_occurrences,
    zero_core_cells,
    distance_to_fiber,
):
    """Match marked zero-core cells to QTDS contacts by associahedral distance.

    This is a diagnostic reconstruction using the target contact support.  It
    is not yet a scalar-only derivation of that support.
    """

    sources_by_variable = defaultdict(list)
    for triangulation in zero_core_cells:
        for diagonal in triangulation:
            sources_by_variable[diagonal].append(triangulation)

    targets_by_variable = defaultdict(list)
    for quadrangulation, diagonal in contact_occurrences:
        targets_by_variable[diagonal].append(quadrangulation)
    assert set(sources_by_variable) == set(targets_by_variable)

    matching = set()
    for diagonal, sources in sources_by_variable.items():
        targets = targets_by_variable[diagonal]
        assert len(sources) == len(targets)
        candidates = []
        for target_order in permutations(targets):
            score = sum(
                distance_to_fiber[source][target]
                for source, target in zip(
                    sources, target_order, strict=True
                )
            )
            candidates.append((score, target_order))
        minimum = min(score for score, _ in candidates)
        minimizers = [
            target_order
            for score, target_order in candidates
            if score == minimum
        ]
        assert len(minimizers) == 1
        for source, target in zip(
            sources, minimizers[0], strict=True
        ):
            assert distance_to_fiber[source][target] == 2
            matching.add((source, diagonal, target))
    assert len(matching) == 20
    return matching


def expected_contact_grammar(variables, *, first_is_plus):
    """Compact C_i/M_i formula for the exact QTDS contact sector."""

    cycle = quadrangulation_cellulation()[2]
    outer = tuple(
        canonical_edge(cycle[index], cycle[(index + 1) % 8])
        for index in range(8)
    )
    matching = tuple(
        canonical_edge(cycle[index], cycle[index + 4])
        for index in range(4)
    )
    zero = LaurentPolynomial.constant(0)

    def short(index):
        return variables[
            tuple(sorted((index % 8, (index + 2) % 8)))
        ]

    def diameter(index):
        return variables[
            tuple(sorted((index % 8, (index + 4) % 8)))
        ]

    result = {
        quadrangulation: zero
        for quadrangulation in quadrangulation_cellulation()[4]
    }
    if first_is_plus:
        for index in range(4):
            contact = -(
                short(2 * index - 3) + short(2 * index - 2)
            )
            result[outer[2 * index]] = contact
            result[outer[2 * index + 1]] = contact
        result[matching[0]] = -(diameter(0) + diameter(3))
        result[matching[2]] = -(diameter(1) + diameter(2))
    else:
        for index in range(4):
            contact = -(
                short(2 * index) + short(2 * index + 1)
            )
            result[outer[(2 * index - 1) % 8]] = contact
            result[outer[2 * index]] = contact
        result[matching[1]] = -(diameter(0) + diameter(1))
        result[matching[3]] = -(diameter(2) + diameter(3))
    return result


def transfer_audit() -> None:
    """Prove the core-stratified decomposition of both QTDS polarities."""

    diagonals, variables, s = planar_symbolic_kinematics()
    variable_index = {
        diagonal: index for index, diagonal in enumerate(diagonals)
    }
    groups, individual = scalar_grade_by_core(variables)
    quadrangulations = set(quadrangulation_cellulation()[4])
    physical = set(admissible_octagon_diagonals())
    zero = LaurentPolynomial.constant(0)

    assert {core for core in groups if len(core) == 2} == quadrangulations
    assert {core[0] for core in groups if len(core) == 1} == physical
    assert () in groups
    assert sum(
        (value for triangulation, value in individual.items() if not any(
            (diagonal[0] - diagonal[1]) % 2 for diagonal in triangulation
        )),
        zero,
    ) == groups[()]

    one_core = {
        core[0]: value for core, value in groups.items() if len(core) == 1
    }
    full_core = {
        core: value for core, value in groups.items() if len(core) == 2
    }
    for diagonal, value in one_core.items():
        expected = (variable_index[diagonal],)
        assert {
            negative_support(powers) for powers in value.terms
        } == {expected}
    assert {
        negative_support(powers) for powers in groups[()].terms
    } <= {()}

    polarity_contacts = {}
    for first_is_plus in (True, False):
        qtds = qtds_diagrams(
            s, variables, first_is_plus=first_is_plus
        )
        assert set(qtds) == quadrangulations
        remainder = {
            quadrangulation: qtds[quadrangulation]
            - full_core[quadrangulation]
            for quadrangulation in quadrangulations
        }

        # Full-core fibers reproduce every double-pole contribution.
        for quadrangulation, value in remainder.items():
            allowed_indices = {
                variable_index[diagonal] for diagonal in quadrangulation
            }
            for powers in value.terms:
                support = set(negative_support(powers))
                assert len(support) <= 1
                assert support <= allowed_indices

        # Each one-core fiber is redistributed only among the three
        # quadrangulations containing that physical channel.
        for diagonal in physical:
            index = variable_index[diagonal]
            allocated = sum(
                (
                    select_terms(
                        value,
                        lambda powers, index=index: negative_support(powers)
                        == (index,),
                    )
                    for quadrangulation, value in remainder.items()
                    if diagonal in quadrangulation
                ),
                zero,
            )
            assert allocated == one_core[diagonal]
            assert all(
                not select_terms(
                    value,
                    lambda powers, index=index: negative_support(powers)
                    == (index,),
                )
                for quadrangulation, value in remainder.items()
                if diagonal not in quadrangulation
            )

        # What remains after the triangle transfers is exactly the sum of the
        # four zero-core scalar cells.
        contacts = {
            quadrangulation: select_terms(
                value, lambda powers: not negative_support(powers)
            )
            for quadrangulation, value in remainder.items()
        }
        assert contacts == expected_contact_grammar(
            variables, first_is_plus=first_is_plus
        )
        assert sum(contacts.values(), zero) == groups[()]
        assert sum(qtds.values(), zero) == sum(groups.values(), zero)
        contact_occurrences = []
        for quadrangulation, contact in contacts.items():
            for powers, coefficient in contact.terms.items():
                support = [
                    index
                    for index, exponent in enumerate(powers)
                    if exponent
                ]
                assert len(support) == 1
                assert powers[support[0]] == 1
                assert coefficient == -1
                contact_occurrences.append(
                    (quadrangulation, diagonals[support[0]])
                )
        assert len(contact_occurrences) == 20
        polarity_contacts[first_is_plus] = tuple(contact_occurrences)

        polarity = "+" if first_is_plus else "-"
        print(
            f"n=8 polarity {polarity}: 12 full-core double-pole fibers, "
            "8 one-core triangle transfers, and the zero-core contact sum "
            "match exactly"
        )

    # Each zero-core scalar cell contributes -sum_{d in T} X_d, so its
    # twenty marked occurrences can be compared directly with the twenty
    # contact monomials of either QTDS polarity.
    triangulation_list = triangulations(tuple(range(8)))
    core = {
        triangulation: tuple(
            sorted(
                diagonal
                for diagonal in triangulation
                if (diagonal[0] - diagonal[1]) % 2
            )
        )
        for triangulation in triangulation_list
    }
    zero_core_cells = tuple(
        triangulation
        for triangulation in triangulation_list
        if not core[triangulation]
    )
    adjacency = scalar_flip_graph(triangulation_list)
    fibers = {
        quadrangulation: tuple(
            triangulation
            for triangulation in triangulation_list
            if core[triangulation] == quadrangulation
        )
        for quadrangulation in quadrangulations
    }
    distance_to_fiber = {}
    for source in zero_core_cells:
        distances = {source: 0}
        queue = [source]
        for triangulation in queue:
            for neighbor in adjacency[triangulation]:
                if neighbor not in distances:
                    distances[neighbor] = distances[triangulation] + 1
                    queue.append(neighbor)
        distance_to_fiber[source] = {
            quadrangulation: min(
                distances[target] for target in fiber
            )
            for quadrangulation, fiber in fibers.items()
        }

    matchings = {
        polarity: minimum_contact_matching(
            contact_occurrences,
            zero_core_cells,
            distance_to_fiber,
        )
        for polarity, contact_occurrences in polarity_contacts.items()
    }

    # Rotation exchanges the two alternating matchings exactly.
    rotated_plus = {
        (
            frozenset(rotate_diagonal(diagonal) for diagonal in source),
            rotate_diagonal(marked),
            tuple(
                sorted(
                    rotate_diagonal(diagonal)
                    for diagonal in target
                )
            ),
        )
        for source, marked, target in matchings[True]
    }
    assert rotated_plus == matchings[False]

    # The four central diameters label square carriers, but their individual
    # contact monomials do not stay inside those squares.  This rules out the
    # naive cell-by-cell square allocation and forces genuine edge transport.
    def source_square_contains(source, target):
        diameter = next(
            diagonal
            for diagonal in source
            if diagonal[1] - diagonal[0] == 4
        )
        return all(
            not diagonals_cross(diameter, diagonal)
            for diagonal in target
        )

    assert any(
        not source_square_contains(source, target)
        for matching in matchings.values()
        for source, _, target in matching
    )
    print(
        "n=8 contacts: each polarity gives a unique minimum-distance "
        "matching of 20 marked zero-core cells to 20 QTDS contacts; all "
        "transfers have scalar flip distance 2 and rotation exchanges them"
    )
    print(
        "n=8 contacts: naive confinement of each central cell to its "
        "diameter square is false; edge transport is essential"
    )

    print(
        "all exact eight-point scalar-cell/QTDS transfer checks passed"
    )


if __name__ == "__main__":
    transfer_audit()
