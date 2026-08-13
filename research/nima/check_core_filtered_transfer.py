"""Exact core-filtered scalar/QTDS transfer audit through twelve points.

For every partial physical core P, this script computes the same Laurent
polynomial in four independent ways:

1. directly from the scalar t^(n-2) associated grade;
2. as the product of zero-core contact polynomials in the even regions cut
   out by P;
3. directly from the complete symbolic QTDS numerator expansion, grouped by
   its remaining denominator support P;
4. from the directed-dual-tree rule after deleting P, requiring one sink in
   every connected component.

The raw scalar coefficient is evaluated by its exact weak-composition
formula, avoiding construction of irrelevant lower series coefficients.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache

from check_eight_point_transfer import planar_symbolic_kinematics
from check_j_reconstruction import canonical_channel, triangulations
from check_qtds_descent import LaurentPolynomial
from check_qtds_lift import qtds_raw_terms
from check_scalar_catalan_map import (
    alternating_coorientation,
    cell_side,
    physical_core,
    quadrangulation_cells,
)


Diagonal = tuple[int, int]
Core = tuple[Diagonal, ...]


@lru_cache(None)
def weak_compositions(
    total: int, part_count: int
) -> tuple[tuple[int, ...], ...]:
    """All weak compositions of total into part_count ordered parts."""

    assert part_count >= 1
    if part_count == 1:
        return ((total,),)
    return tuple(
        (first,) + tail
        for first in range(total + 1)
        for tail in weak_compositions(
            total - first, part_count - 1
        )
    )


def full_cores(multiplicity: int) -> tuple[Core, ...]:
    """All quadrangulation cores derived from scalar triangulations."""

    core_size = multiplicity // 2 - 2
    return tuple(
        sorted(
            {
                core
                for triangulation in triangulations(
                    tuple(range(multiplicity))
                )
                if len(
                    core := physical_core(triangulation)
                )
                == core_size
            }
        )
    )


def core_subsets(core: Core) -> tuple[Core, ...]:
    """Every subset of a full physical core."""

    return tuple(
        tuple(
            core[index]
            for index in range(len(core))
            if (mask >> index) & 1
        )
        for mask in range(1 << len(core))
    )


def all_partial_cores(multiplicity: int) -> tuple[Core, ...]:
    """All noncrossing partial physical cores."""

    return tuple(
        sorted(
            {
                partial
                for core in full_cores(multiplicity)
                for partial in core_subsets(core)
            }
        )
    )


def core_regions(
    core: Core, multiplicity: int
) -> tuple[tuple[int, ...], ...]:
    """Even polygonal regions obtained by cutting along a partial core."""

    regions = [tuple(range(multiplicity))]
    for first, second in core:
        candidates = []
        for region_index, region in enumerate(regions):
            if first not in region or second not in region:
                continue
            first_index = region.index(first)
            second_index = region.index(second)
            cyclic_distance = (
                second_index - first_index
            ) % len(region)
            if cyclic_distance not in (1, len(region) - 1):
                candidates.append(
                    (
                        region_index,
                        first_index,
                        second_index,
                    )
                )
        assert len(candidates) == 1
        (
            region_index,
            first_index,
            second_index,
        ) = candidates[0]
        region = regions.pop(region_index)
        if first_index > second_index:
            first_index, second_index = (
                second_index,
                first_index,
            )
        regions.extend(
            (
                region[first_index : second_index + 1],
                region[second_index:]
                + region[: first_index + 1],
            )
        )
    assert len(regions) == len(core) + 1
    assert all(len(region) % 2 == 0 for region in regions)
    return tuple(sorted(regions))


def direct_scalar_grade(
    multiplicity: int,
    diagonals: tuple[Diagonal, ...],
) -> dict[Core, LaurentPolynomial]:
    """Raw scalar associated grade grouped by exact physical core.

    If P has p physical edges, a scalar cell has n-3-p shifted
    propagators.  Reaching degree n-2 requires p+1 excess powers.  The
    weak-composition formula below is exactly the coefficient of that grade.
    """

    diagonal_index = {
        diagonal: index
        for index, diagonal in enumerate(diagonals)
    }
    groups = defaultdict(lambda: defaultdict(Fraction))
    for triangulation in triangulations(
        tuple(range(multiplicity))
    ):
        core = physical_core(triangulation)
        scalar_edges = tuple(
            sorted(set(triangulation) - set(core))
        )
        excess_degree = len(core) + 1
        base_powers = [0] * len(diagonals)
        for diagonal in core:
            base_powers[diagonal_index[diagonal]] = -1

        for excesses in weak_compositions(
            excess_degree, len(scalar_edges)
        ):
            powers = base_powers.copy()
            coefficient = Fraction(
                (-1) ** excess_degree
            )
            for diagonal, excess in zip(
                scalar_edges, excesses, strict=True
            ):
                powers[diagonal_index[diagonal]] = excess
                shift_sign = (
                    1 if diagonal[0] % 2 else -1
                )
                coefficient *= shift_sign ** (excess + 1)
            groups[core][tuple(powers)] += coefficient
    return {
        core: LaurentPolynomial(terms)
        for core, terms in groups.items()
    }


def regional_scalar_grade(
    multiplicity: int,
    diagonals: tuple[Diagonal, ...],
    variables: dict[Diagonal, LaurentPolynomial],
) -> dict[Core, LaurentPolynomial]:
    """Product of one zero-core marked-contact polynomial per region."""

    diagonal_index = {
        diagonal: index
        for index, diagonal in enumerate(diagonals)
    }

    @lru_cache(None)
    def local_contact(region: tuple[int, ...]):
        terms = defaultdict(Fraction)
        local_size = len(region)
        for triangulation in triangulations(
            tuple(range(local_size))
        ):
            if physical_core(triangulation):
                continue
            for first, second in triangulation:
                diagonal = tuple(
                    sorted((region[first], region[second]))
                )
                powers = [0] * len(diagonals)
                powers[diagonal_index[diagonal]] = 1
                terms[tuple(powers)] -= 1
        return LaurentPolynomial(terms)

    result = {}
    for core in all_partial_cores(multiplicity):
        value = LaurentPolynomial.constant(1)
        for region in core_regions(core, multiplicity):
            value *= local_contact(region)
        for diagonal in core:
            value /= variables[diagonal]
        result[core] = value
    return result


def direct_qtds_by_support(
    multiplicity: int,
    diagonals: tuple[Diagonal, ...],
    variables: dict[Diagonal, LaurentPolynomial],
    kinematics,
    *,
    first_is_plus: bool,
) -> dict[Core, LaurentPolynomial]:
    """Raw symbolic QTDS expansion grouped by denominator support."""

    channel_to_diagonal = {}
    for diagonal in diagonals:
        if not (diagonal[0] - diagonal[1]) % 2:
            continue
        first, second = diagonal
        channel = canonical_channel(
            tuple(range(first, second)), multiplicity
        )
        assert channel not in channel_to_diagonal
        channel_to_diagonal[channel] = diagonal

    groups = defaultdict(lambda: defaultdict(Fraction))
    convention_sign = (-1) ** (multiplicity // 2 - 1)
    for numerator, propagators in qtds_raw_terms(
        tuple(range(multiplicity)),
        kinematics,
        first_is_plus=first_is_plus,
    ):
        denominator = LaurentPolynomial.constant(1)
        for block in propagators:
            denominator *= variables[
                channel_to_diagonal[
                    canonical_channel(block, multiplicity)
                ]
            ]
        diagram = convention_sign * numerator / denominator
        for powers, coefficient in diagram.terms.items():
            support = tuple(
                sorted(
                    diagonals[index]
                    for index, exponent in enumerate(powers)
                    if exponent < 0
                )
            )
            assert all(
                exponent >= -1 for exponent in powers
            )
            groups[support][powers] += coefficient
    return {
        core: LaurentPolynomial(terms)
        for core, terms in groups.items()
    }


def component_sink_polynomial(
    quadrangulation: Core,
    remaining_core: Core,
    multiplicity: int,
    variables: dict[Diagonal, LaurentPolynomial],
    *,
    first_is_plus: bool,
) -> LaurentPolynomial:
    """QTDS numerator sector leaving exactly remaining_core uncancelled."""

    cells = quadrangulation_cells(
        quadrangulation, multiplicity
    )
    canceled_edges = set(quadrangulation) - set(
        remaining_core
    )
    adjacency = defaultdict(set)
    outgoing = defaultdict(set)
    for diagonal in quadrangulation:
        adjacent = tuple(
            cell for cell in cells if set(diagonal) <= set(cell)
        )
        assert len(adjacent) == 2
        if diagonal not in canceled_edges:
            continue
        adjacency[adjacent[0]].add(adjacent[1])
        adjacency[adjacent[1]].add(adjacent[0])
        target_side = alternating_coorientation(
            diagonal, first_is_plus=first_is_plus
        )
        target = next(
            cell
            for cell in adjacent
            if cell_side(diagonal, cell) == target_side
        )
        source = next(
            cell for cell in adjacent if cell != target
        )
        outgoing[source].add(diagonal)

    components = []
    seen = set()
    for cell in cells:
        if cell in seen:
            continue
        component = {cell}
        queue = [cell]
        seen.add(cell)
        for current in queue:
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        components.append(component)
    assert len(components) == len(remaining_core) + 1

    value = LaurentPolynomial.constant(
        (-1) ** len(components)
    )
    for component in components:
        sinks = tuple(
            cell for cell in component if not outgoing[cell]
        )
        if len(sinks) != 1:
            return LaurentPolynomial.constant(0)
        first, second, third, fourth = sinks[0]
        value *= (
            variables[tuple(sorted((first, third)))]
            + variables[tuple(sorted((second, fourth)))]
        )
    for diagonal in remaining_core:
        value /= variables[diagonal]
    return value


def regional_qtds_by_support(
    multiplicity: int,
    variables: dict[Diagonal, LaurentPolynomial],
    *,
    first_is_plus: bool,
) -> dict[Core, LaurentPolynomial]:
    """Sum the componentwise unique-sink formula over full cores."""

    result = {
        core: LaurentPolynomial.constant(0)
        for core in all_partial_cores(multiplicity)
    }
    for quadrangulation in full_cores(multiplicity):
        for remaining_core in core_subsets(quadrangulation):
            result[remaining_core] += component_sink_polynomial(
                quadrangulation,
                remaining_core,
                multiplicity,
                variables,
                first_is_plus=first_is_plus,
            )
    return result


def multiplicity_audit(multiplicity: int):
    """Four-way equality at every core of one multiplicity."""

    diagonals, variables, kinematics = (
        planar_symbolic_kinematics(multiplicity)
    )
    scalar_direct = direct_scalar_grade(
        multiplicity, diagonals
    )
    scalar_regional = regional_scalar_grade(
        multiplicity, diagonals, variables
    )
    assert scalar_direct == scalar_regional

    polarity_data = {}
    for polarity in (True, False):
        qtds_direct = direct_qtds_by_support(
            multiplicity,
            diagonals,
            variables,
            kinematics,
            first_is_plus=polarity,
        )
        qtds_regional = regional_qtds_by_support(
            multiplicity,
            variables,
            first_is_plus=polarity,
        )
        assert qtds_direct == qtds_regional
        assert qtds_direct == scalar_direct
        polarity_data[polarity] = qtds_direct
    assert polarity_data[True] == polarity_data[False]

    return (
        len(scalar_direct),
        sum(
            len(polynomial.terms)
            for polynomial in scalar_direct.values()
        ),
    )


def main() -> None:
    for multiplicity in (4, 6, 8, 10, 12):
        core_count, term_count = multiplicity_audit(
            multiplicity
        )
        print(
            f"n={multiplicity} core-filtered transfer: "
            f"{core_count} physical cores and {term_count} Laurent "
            "monomials agree in all four constructions"
        )
    print(
        "all exact core-filtered scalar/QTDS checks through twelve "
        "points passed"
    )


if __name__ == "__main__":
    main()
