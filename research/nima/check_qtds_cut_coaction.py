"""Exact occurrence-level cut coaction for the QTDS/scalar coefficient system.

For every unique-sink directed quadrangulation through twelve points, cutting
a physical edge creates a new forest component.  The source quadrilateral of
that directed edge becomes the new sink and contributes either scalar slot.
The corresponding coefficient map multiplies by -X_slot / X_edge.

The script proves computationally, for all cut subsets and every cut order:

* every cut forest has one sink per component;
* the two-slot transition is order independent;
* its closed formula is a product over cut-edge sources;
* weights reproduce (-1)^(|P|+1) prod X_mark / prod X_edge;
* one-step rotation exchanges the two polarity sheets;
* initial occurrence counts match marked zero-core scalar sources.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import permutations, product

from check_core_filtered_transfer import (
    core_subsets,
    full_cores,
)
from check_scalar_catalan_map import (
    alternating_coorientation,
    canonical_diagonal,
    cell_side,
    quadrangulation_cells,
)
from check_core_incidence_cells import zero_core_cells


Diagonal = tuple[int, int]
Cell = tuple[int, int, int, int]
Core = tuple[Diagonal, ...]
Marks = tuple[tuple[Cell, Diagonal], ...]
Monomial = tuple[tuple[Diagonal, int], ...]
Term = tuple[Marks, Monomial]


def prune(counter: Counter) -> Counter:
    """Retain every nonzero signed coefficient."""

    return Counter(
        {
            key: coefficient
            for key, coefficient in counter.items()
            if coefficient
        }
    )


def directed_edges(
    quadrangulation: Core,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> tuple[tuple[Cell, ...], dict[Diagonal, tuple[Cell, Cell]]]:
    """Directed dual-tree edges from alternating scalar coorientation."""

    cells = quadrangulation_cells(quadrangulation, multiplicity)
    result = {}
    for diagonal in quadrangulation:
        adjacent = tuple(
            cell for cell in cells if set(diagonal) <= set(cell)
        )
        assert len(adjacent) == 2
        target_side = alternating_coorientation(
            diagonal, first_is_plus=first_is_plus
        )
        target = next(
            cell
            for cell in adjacent
            if cell_side(diagonal, cell) == target_side
        )
        source = next(cell for cell in adjacent if cell != target)
        result[diagonal] = (source, target)
    return cells, result


def forest_sinks(
    quadrangulation: Core,
    cut_core: Core,
    multiplicity: int,
    *,
    first_is_plus: bool,
    allow_nonunique: bool = False,
) -> tuple[Cell, ...]:
    """The unique sink in every component after deleting cut_core."""

    cells, directions = directed_edges(
        quadrangulation,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    cut = set(cut_core)
    adjacency = defaultdict(set)
    outgoing = defaultdict(set)
    for diagonal, (source, target) in directions.items():
        if diagonal in cut:
            continue
        adjacency[source].add(target)
        adjacency[target].add(source)
        outgoing[source].add(diagonal)

    seen = set()
    sinks = []
    for cell in cells:
        if cell in seen:
            continue
        component = {cell}
        pending = [cell]
        seen.add(cell)
        while pending:
            current = pending.pop()
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        component_sinks = tuple(
            member for member in component if not outgoing[member]
        )
        if len(component_sinks) != 1:
            assert allow_nonunique
            return ()
        sinks.append(component_sinks[0])

    assert len(sinks) == len(cut_core) + 1
    return tuple(sorted(sinks))


def sink_slots(cell: Cell) -> tuple[Diagonal, Diagonal]:
    """The two scalar diagonal slots of a QTDS quadrilateral."""

    first, second, third, fourth = cell
    return tuple(
        sorted(
            (
                canonical_diagonal(first, third),
                canonical_diagonal(second, fourth),
            )
        )
    )


def monomial_key(powers: dict[Diagonal, int]) -> Monomial:
    """Sparse Laurent monomial key."""

    return tuple(
        sorted(
            (
                (diagonal, exponent)
                for diagonal, exponent in powers.items()
                if exponent
            )
        )
    )


def multiply_monomial(
    monomial: Monomial,
    numerator: Diagonal,
    denominator: Diagonal,
) -> Monomial:
    """Multiply by X_numerator / X_denominator."""

    powers = dict(monomial)
    powers[numerator] = powers.get(numerator, 0) + 1
    powers[denominator] = powers.get(denominator, 0) - 1
    return monomial_key(powers)


def marks_key(marks: dict[Cell, Diagonal]) -> Marks:
    """Stable component-sink decoration."""

    return tuple(sorted(marks.items()))


def initial_terms(global_sink: Cell, mark: Diagonal) -> Counter:
    """The one marked zero-core occurrence with weight -X_mark."""

    return Counter(
        {
            (
                ((global_sink, mark),),
                ((mark, 1),),
            ): -1
        }
    )


def apply_cut(
    terms: Counter,
    quadrangulation: Core,
    cut_core: Core,
    edge: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> Counter:
    """Apply the two-slot physical Gysin/coaction map for one edge."""

    assert edge in quadrangulation
    assert edge not in cut_core
    old_sinks = set(
        forest_sinks(
            quadrangulation,
            cut_core,
            multiplicity,
            first_is_plus=first_is_plus,
        )
    )
    new_core = tuple(sorted((*cut_core, edge)))
    new_sinks = set(
        forest_sinks(
            quadrangulation,
            new_core,
            multiplicity,
            first_is_plus=first_is_plus,
        )
    )
    _, directions = directed_edges(
        quadrangulation,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    source, _ = directions[edge]
    assert new_sinks == old_sinks | {source}
    assert source not in old_sinks

    result = Counter()
    for (marks, monomial), coefficient in terms.items():
        marks_dict = dict(marks)
        assert set(marks_dict) == old_sinks
        for slot in sink_slots(source):
            new_marks = dict(marks_dict)
            new_marks[source] = slot
            result[
                (
                    marks_key(new_marks),
                    multiply_monomial(monomial, slot, edge),
                )
            ] -= coefficient
    return prune(result)


def closed_expansion(
    quadrangulation: Core,
    cut_core: Core,
    global_sink: Cell,
    global_mark: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> Counter:
    """Order-free product formula for an arbitrary set of cuts."""

    _, directions = directed_edges(
        quadrangulation,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    cut_sources = tuple(
        directions[edge][0] for edge in cut_core
    )
    assert len(set(cut_sources)) == len(cut_sources)
    expected_sinks = {global_sink, *cut_sources}
    assert set(
        forest_sinks(
            quadrangulation,
            cut_core,
            multiplicity,
            first_is_plus=first_is_plus,
        )
    ) == expected_sinks

    result = Counter()
    for slots in product(
        *(sink_slots(source) for source in cut_sources)
    ):
        marks = {global_sink: global_mark}
        powers = {global_mark: 1}
        coefficient = (-1) ** (len(cut_core) + 1)
        for edge, source, slot in zip(
            cut_core, cut_sources, slots, strict=True
        ):
            marks[source] = slot
            powers[slot] = powers.get(slot, 0) + 1
            powers[edge] = powers.get(edge, 0) - 1
        result[(marks_key(marks), monomial_key(powers))] += coefficient
    return prune(result)


def ordered_expansion(
    quadrangulation: Core,
    cut_order: tuple[Diagonal, ...],
    global_sink: Cell,
    global_mark: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> Counter:
    """Iterate elementary cuts in a prescribed order."""

    terms = initial_terms(global_sink, global_mark)
    cut_core: Core = ()
    for edge in cut_order:
        terms = apply_cut(
            terms,
            quadrangulation,
            cut_core,
            edge,
            multiplicity,
            first_is_plus=first_is_plus,
        )
        cut_core = tuple(sorted((*cut_core, edge)))
    return terms


def rotate_diagonal(diagonal: Diagonal, multiplicity: int) -> Diagonal:
    """Rotate one diagonal by one external label."""

    return canonical_diagonal(
        (diagonal[0] + 1) % multiplicity,
        (diagonal[1] + 1) % multiplicity,
    )


def rotate_cell(cell: Cell, multiplicity: int) -> Cell:
    """Rotate a quadrilateral while restoring cyclic sorted representation."""

    return tuple(sorted((vertex + 1) % multiplicity for vertex in cell))


def rotate_core(core: Core, multiplicity: int) -> Core:
    """Rotate a physical core."""

    return tuple(
        sorted(rotate_diagonal(edge, multiplicity) for edge in core)
    )


def rotate_terms(terms: Counter, multiplicity: int) -> Counter:
    """Rotate every mark and Laurent variable in an expansion."""

    result = Counter()
    for (marks, monomial), coefficient in terms.items():
        rotated_marks = tuple(
            sorted(
                (
                    rotate_cell(cell, multiplicity),
                    rotate_diagonal(mark, multiplicity),
                )
                for cell, mark in marks
            )
        )
        rotated_monomial = tuple(
            sorted(
                (
                    rotate_diagonal(diagonal, multiplicity),
                    exponent,
                )
                for diagonal, exponent in monomial
            )
        )
        result[(rotated_marks, rotated_monomial)] += coefficient
    return prune(result)


def polarity_audit(
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """All unique-sink quadrangulations and all cut orders."""

    initial_occurrences = 0
    cut_profiles = Counter()
    records = {}

    for quadrangulation in full_cores(multiplicity):
        empty_sinks = forest_sinks(
            quadrangulation,
            (),
            multiplicity,
            first_is_plus=first_is_plus,
            allow_nonunique=True,
        )
        if len(empty_sinks) != 1:
            continue
        global_sink = empty_sinks[0]
        for global_mark in sink_slots(global_sink):
            initial_occurrences += 1
            for cut_core in core_subsets(quadrangulation):
                cut_core = tuple(sorted(cut_core))
                closed = closed_expansion(
                    quadrangulation,
                    cut_core,
                    global_sink,
                    global_mark,
                    multiplicity,
                    first_is_plus=first_is_plus,
                )
                assert len(closed) == 2 ** len(cut_core)
                for order in permutations(cut_core):
                    assert ordered_expansion(
                        quadrangulation,
                        order,
                        global_sink,
                        global_mark,
                        multiplicity,
                        first_is_plus=first_is_plus,
                    ) == closed
                cut_profiles[
                    (len(cut_core), len(closed))
                ] += 1
                records[
                    (
                        quadrangulation,
                        cut_core,
                        global_sink,
                        global_mark,
                    )
                ] = closed

    scalar_occurrences = sum(
        len(triangulation)
        for triangulation in zero_core_cells(multiplicity)
    )
    assert initial_occurrences == scalar_occurrences
    return {
        "initial_occurrences": initial_occurrences,
        "cut_profiles": cut_profiles,
        "records": records,
    }


def multiplicity_audit(multiplicity: int):
    """Both sheets and exact rotation of every closed cut expansion."""

    plus = polarity_audit(multiplicity, first_is_plus=True)
    minus = polarity_audit(multiplicity, first_is_plus=False)

    for (
        quadrangulation,
        cut_core,
        global_sink,
        global_mark,
    ), expansion in plus["records"].items():
        target = (
            rotate_core(quadrangulation, multiplicity),
            rotate_core(cut_core, multiplicity),
            rotate_cell(global_sink, multiplicity),
            rotate_diagonal(global_mark, multiplicity),
        )
        assert rotate_terms(expansion, multiplicity) == minus[
            "records"
        ][target]

    assert plus["initial_occurrences"] == minus[
        "initial_occurrences"
    ]
    assert plus["cut_profiles"] == minus["cut_profiles"]
    return plus


def main() -> None:
    for multiplicity in (4, 6, 8, 10, 12):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} initial marked sink occurrences: "
            f"{result['initial_occurrences']}"
        )
        print(
            f"n={multiplicity} cut profiles "
            f"(cut rank, terms per expansion): "
            f"{dict(result['cut_profiles'])}"
        )
    print(
        "all exact occurrence-level physical cut-coaction and "
        "deck-covariance checks through twelve points passed"
    )


if __name__ == "__main__":
    main()
