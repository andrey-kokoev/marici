"""Spectator-stability audit for the mixed Beck--Chevalley transport.

The minimal ten-point prism has zero occurrence-level curvature.  This script
tests whether that result survives a pre-existing physical core and arbitrary
regional contact marks.  It constructs the regional marked Catalan map in the
forward direction, applies one additional physical cut, and then uses the
regional inverse from check_mixed_prism_curvature.py.

For every distinct mixed prism at n=10 and n=12, on both polarity sheets, and
for every componentwise scalar mark common to the lower refinement edge, the
audit proves:

* regional forward and inverse Catalan maps are exact inverses;
* the two lower endpoints have the same component marks;
* cut support is natural: the new edge occurs at both endpoints or neither;
* when supported, the cut has the same source quadrilateral and scalar slots;
* its two Laurent occurrence terms agree exactly;
* both matched terms reconstruct genuine upper scalar-refinement edges;
* one edge is the forced prism edge and one is the parallel slot edge;
* the complete atlas is one-step rotation/deck covariant.

At twelve points this includes prisms over a nonempty base core.  It therefore
checks the first spectator/product extension of the ten-point result.  It
still makes no claim about a finite-alpha-prime loaded-current realization.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import product

from check_core_filtered_transfer import core_regions
from check_core_incidence_cells import (
    face_adjacency,
    rank_two_face_index,
    triangulation_key,
)
from check_mixed_prism_curvature import (
    regional_inverse_source,
    rotate_core_tuple,
    rotate_marks,
    rotate_monomial,
    to_global_cell,
    to_global_diagonal,
    to_local_diagonal,
)
from check_mixed_prism_squares import core, polarity_audit
from check_qtds_cut_coaction import (
    apply_cut,
    directed_edges,
    forest_sinks,
    marks_key,
    monomial_key,
    rotate_cell,
    sink_slots,
)
from check_scalar_catalan_map import (
    alternating_coorientation,
    cell_side,
    direct_endpoint,
    directed_sink_flow,
    is_boundary,
    physical_core,
    rotate_diagonal,
    rotate_triangulation,
)


Diagonal = tuple[int, int]
Cell = tuple[int, int, int, int]
Triangulation = frozenset[Diagonal]
Core = tuple[Diagonal, ...]
Marks = tuple[tuple[Cell, Diagonal], ...]
Monomial = tuple[tuple[Diagonal, int], ...]
TermKey = tuple[Marks, Monomial]


def regional_internal_edges(
    source: Triangulation,
    cut_core: Core,
    region: tuple[int, ...],
) -> Triangulation:
    """Restrict one partial-core scalar source to a cut region."""

    local_edges = []
    region_set = set(region)
    for diagonal in source:
        if diagonal in cut_core:
            continue
        if not set(diagonal) <= region_set:
            continue
        local_diagonal = to_local_diagonal(
            diagonal, region
        )
        if not is_boundary(local_diagonal, len(region)):
            local_edges.append(local_diagonal)
    result = frozenset(local_edges)
    assert len(result) == len(region) - 3
    assert not physical_core(result)
    return result


def direction_matches_global_sheet(
    local_core: Core,
    region: tuple[int, ...],
    *,
    local_polarity: bool,
    global_polarity: bool,
) -> bool:
    """Whether all local directed edges map to the global coorientation."""

    _, _, _, directions = directed_sink_flow(
        local_core,
        len(region),
        first_is_plus=local_polarity,
    )
    for local_edge, (local_source, local_target) in (
        directions.items()
    ):
        global_edge = to_global_diagonal(
            local_edge, region
        )
        global_source = to_global_cell(
            local_source, region
        )
        global_target = to_global_cell(
            local_target, region
        )
        target_side = alternating_coorientation(
            global_edge,
            first_is_plus=global_polarity,
        )
        if cell_side(global_edge, global_target) != target_side:
            return False
        if cell_side(global_edge, global_source) == target_side:
            return False
    return True


@lru_cache(None)
def regional_forward_source(
    source: Triangulation,
    cut_core: Core,
    component_marks: tuple[Diagonal, ...],
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> tuple[Core, Marks]:
    """Apply the marked Catalan map in every component of a cut source."""

    regions = core_regions(cut_core, multiplicity)
    assert len(regions) == len(component_marks)
    quadrangulation = set(cut_core)
    global_marks = {}

    for region, global_mark in zip(
        regions, component_marks, strict=True
    ):
        local_source = regional_internal_edges(
            source, cut_core, region
        )
        local_mark = to_local_diagonal(
            global_mark, region
        )
        assert local_mark in local_source

        candidates = set()
        if len(region) == 4:
            # direct_endpoint starts at the first nontrivial Catalan case.
            # A quadrilateral has empty physical core and its sole cell is
            # the sink independently of polarity.
            candidates.add(((), tuple(sorted(region))))
        else:
            for local_polarity in (True, False):
                (
                    _,
                    local_core,
                    _,
                    _,
                ) = direct_endpoint(
                    local_source,
                    local_mark,
                    len(region),
                    first_is_plus=local_polarity,
                )
                if not direction_matches_global_sheet(
                    local_core,
                    region,
                    local_polarity=local_polarity,
                    global_polarity=first_is_plus,
                ):
                    continue
                _, local_sink, _, _ = directed_sink_flow(
                    local_core,
                    len(region),
                    first_is_plus=local_polarity,
                )
                candidates.add(
                    (
                        tuple(
                            sorted(
                                to_global_diagonal(
                                    diagonal, region
                                )
                                for diagonal in local_core
                            )
                        ),
                        to_global_cell(local_sink, region),
                    )
                )

        # The two formal polarity labels coincide only for the empty local
        # core; after forgetting that duplicate the regional image is unique.
        assert len(candidates) == 1
        regional_core, global_sink = candidates.pop()
        quadrangulation.update(regional_core)
        assert global_sink not in global_marks
        global_marks[global_sink] = global_mark

    quadrangulation = tuple(sorted(quadrangulation))
    assert len(quadrangulation) == multiplicity // 2 - 2
    sinks = forest_sinks(
        quadrangulation,
        cut_core,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    assert set(sinks) == set(global_marks)
    for sink, mark in global_marks.items():
        assert mark in sink_slots(sink)

    marks = marks_key(global_marks)
    assert regional_inverse_source(
        quadrangulation,
        cut_core,
        marks,
        multiplicity,
        first_is_plus=first_is_plus,
    ) == source
    return quadrangulation, marks


def initial_regional_term(
    cut_core: Core, marks: Marks
) -> Counter:
    """One component-marked Laurent occurrence at a fixed core."""

    powers = {diagonal: -1 for diagonal in cut_core}
    for _, mark in marks:
        powers[mark] = powers.get(mark, 0) + 1
    coefficient = (-1) ** (len(cut_core) + 1)
    return Counter(
        {
            (
                marks,
                monomial_key(powers),
            ): coefficient
        }
    )


def common_component_marks(
    left: Triangulation,
    right: Triangulation,
    cut_core: Core,
    multiplicity: int,
) -> tuple[tuple[Diagonal, ...], ...]:
    """All mark choices preserved by one regional scalar flip."""

    choices = []
    for region in core_regions(cut_core, multiplicity):
        region_set = set(region)
        candidates = tuple(
            sorted(
                diagonal
                for diagonal in left & right
                if diagonal not in cut_core
                and set(diagonal) <= region_set
                and not is_boundary(
                    to_local_diagonal(diagonal, region),
                    len(region),
                )
            )
        )
        assert candidates
        choices.append(candidates)
    return tuple(product(*choices))


def rotate_transport_record(record, multiplicity: int):
    """Rotate one spectator-stable transport record."""

    (
        endpoint_data,
        cut_core,
        cut_edge,
        base_marks,
        cut_source,
        lifted_terms,
    ) = record
    return (
        frozenset(
            (
                rotate_triangulation(source, multiplicity),
                rotate_core_tuple(
                    quadrangulation, multiplicity
                ),
                (
                    None
                    if direction is None
                    else tuple(
                        rotate_cell(cell, multiplicity)
                        for cell in direction
                    )
                ),
            )
            for source, quadrangulation, direction in endpoint_data
        ),
        rotate_core_tuple(cut_core, multiplicity),
        rotate_diagonal(cut_edge, multiplicity),
        rotate_marks(base_marks, multiplicity),
        (
            None
            if cut_source is None
            else rotate_cell(cut_source, multiplicity)
        ),
        frozenset(
            (
                (
                    rotate_marks(term_key[0], multiplicity),
                    rotate_monomial(
                        term_key[1], multiplicity
                    ),
                ),
                coefficient,
                frozenset(
                    rotate_triangulation(
                        source, multiplicity
                    )
                    for source in upper_edge
                ),
                is_forced,
            )
            for (
                term_key,
                coefficient,
                upper_edge,
                is_forced,
            ) in lifted_terms
        ),
    )


def strict_transport(
    lower: tuple[Triangulation, Triangulation],
    upper: set[Triangulation],
    cut_core: Core,
    cut_edge: Diagonal,
    component_marks: tuple[Diagonal, ...],
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """Verify strict mixed naturality for one decorated lower edge."""

    left_core, left_marks = regional_forward_source(
        lower[0],
        cut_core,
        component_marks,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    right_core, right_marks = regional_forward_source(
        lower[1],
        cut_core,
        component_marks,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    assert left_core != right_core
    assert left_marks == right_marks

    _, left_directions = directed_edges(
        left_core,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    _, right_directions = directed_edges(
        right_core,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    left_supported = cut_edge in left_directions
    right_supported = cut_edge in right_directions
    assert left_supported == right_supported
    if not left_supported:
        record = (
            frozenset(
                {
                    (lower[0], left_core, None),
                    (lower[1], right_core, None),
                }
            ),
            cut_core,
            cut_edge,
            left_marks,
            None,
            frozenset(),
        )
        profile = (
            len(cut_core),
            tuple(
                sorted(
                    map(
                        len,
                        core_regions(
                            cut_core, multiplicity
                        ),
                    )
                )
            ),
            "absent",
            0,
            0,
            0,
            0,
        )
        return record, profile

    left_direction = left_directions[cut_edge]
    right_direction = right_directions[cut_edge]
    assert left_direction[0] == right_direction[0]
    assert sink_slots(left_direction[0]) == sink_slots(
        right_direction[0]
    )
    targets_agree = (
        left_direction[1] == right_direction[1]
    )

    left_output = apply_cut(
        initial_regional_term(cut_core, left_marks),
        left_core,
        cut_core,
        cut_edge,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    right_output = apply_cut(
        initial_regional_term(cut_core, right_marks),
        right_core,
        cut_core,
        cut_edge,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    assert left_output == right_output
    assert len(left_output) == 2

    new_core = tuple(sorted((*cut_core, cut_edge)))
    forced_count = 0
    parallel_count = 0
    lifted_terms = set()
    for term_key, coefficient in left_output.items():
        left_source = regional_inverse_source(
            left_core,
            new_core,
            term_key[0],
            multiplicity,
            first_is_plus=first_is_plus,
        )
        right_source = regional_inverse_source(
            right_core,
            new_core,
            term_key[0],
            multiplicity,
            first_is_plus=first_is_plus,
        )
        assert physical_core(left_source) == new_core
        assert physical_core(right_source) == new_core
        assert len(left_source ^ right_source) == 2
        for _, mark in term_key[0]:
            assert mark in left_source
            assert mark in right_source

        removed = next(iter(left_source - right_source))
        added = next(iter(right_source - left_source))
        assert not (removed[0] - removed[1]) % 2
        assert not (added[0] - added[1]) % 2

        is_forced = {left_source, right_source} == upper
        forced_count += int(is_forced)
        parallel_count += int(not is_forced)
        lifted_terms.add(
            (
                term_key,
                coefficient,
                frozenset(
                    {left_source, right_source}
                ),
                is_forced,
            )
        )

    assert forced_count == 1
    assert parallel_count == 1
    record = (
        frozenset(
            {
                (
                    lower[0],
                    left_core,
                    left_direction,
                ),
                (
                    lower[1],
                    right_core,
                    right_direction,
                ),
            }
        ),
        cut_core,
        cut_edge,
        left_marks,
        left_direction[0],
        frozenset(lifted_terms),
    )
    profile = (
        len(cut_core),
        tuple(
            sorted(
                map(
                    len,
                    core_regions(cut_core, multiplicity),
                )
            )
        ),
        "fixed_target"
        if targets_agree
        else "sliding_target",
        len(left_output),
        forced_count,
        parallel_count,
        0,
    )
    return record, profile


def mixed_squares(
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """Distinct scalar mixed-square carriers, forgetting source duplicates."""

    data = polarity_audit(
        multiplicity,
        first_is_plus=first_is_plus,
    )
    return {
        (
            occurrence[4],
            tuple(sorted(occurrence[7])),
            occurrence[8],
        )
        for occurrence in data["records"]
    }


def polarity_audit_spectators(
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """Every common regional marking of every mixed square."""

    face_index = rank_two_face_index(multiplicity)
    records = Counter()
    profiles = Counter()
    squares = mixed_squares(
        multiplicity,
        first_is_plus=first_is_plus,
    )

    for scalar_facet, cut_core, cut_edge in squares:
        vertices = face_index[scalar_facet]
        adjacency = face_adjacency(vertices)
        lower = tuple(
            sorted(
                (
                    vertex
                    for vertex in vertices
                    if physical_core(vertex) == cut_core
                ),
                key=triangulation_key,
            )
        )
        upper = {
            vertex
            for vertex in vertices
            if physical_core(vertex)
            == tuple(sorted((*cut_core, cut_edge)))
        }
        assert len(lower) == 2
        assert len(upper) == 2
        assert lower[1] in adjacency[lower[0]]

        for component_marks in common_component_marks(
            lower[0],
            lower[1],
            cut_core,
            multiplicity,
        ):
            record, profile = strict_transport(
                lower,
                upper,
                cut_core,
                cut_edge,
                component_marks,
                multiplicity,
                first_is_plus=first_is_plus,
            )
            records[record] += 1
            profiles[profile] += 1

    return {
        "square_count": len(squares),
        "transport_count": sum(records.values()),
        "distinct_transport_count": len(records),
        "records": records,
        "profiles": profiles,
    }


def multiplicity_audit(multiplicity: int):
    """Both sheets and exact rotation of every spectator transport."""

    plus = polarity_audit_spectators(
        multiplicity,
        first_is_plus=True,
    )
    minus = polarity_audit_spectators(
        multiplicity,
        first_is_plus=False,
    )
    rotated = Counter()
    for record, count in plus["records"].items():
        rotated[
            rotate_transport_record(record, multiplicity)
        ] += count
    assert rotated == minus["records"]
    for key in (
        "square_count",
        "transport_count",
        "distinct_transport_count",
        "profiles",
    ):
        assert plus[key] == minus[key]
    return plus


def main() -> None:
    for multiplicity in (10, 12):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} mixed squares "
            f"{result['square_count']}; decorated transports "
            f"{result['transport_count']} "
            f"({result['distinct_transport_count']} distinct)"
        )
        print(
            f"n={multiplicity} spectator profiles "
            "(base degree, region sizes, target behavior, "
            "cut terms, forced, parallel, curvature): "
            f"{dict(result['profiles'])}"
        )
    print(
        "all exact spectator-stable and deck-covariant mixed "
        "Beck--Chevalley checks through twelve points passed"
    )


if __name__ == "__main__":
    main()
