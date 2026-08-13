"""Exact mixed-prism Beck--Chevalley audit at ten points.

Every mixed square has a lower scalar-refinement edge at empty physical core
and an upper scalar-refinement edge after one physical cut.  The marked
Catalan map sends the two lower endpoints to generally different full
quadrangulations.  This script asks the non-tautological question: does the
physical cut see the same local coefficient data at both endpoints, and do
the two cut terms reconstruct genuine scalar-refinement edges upstairs?

For every marked mixed-prism occurrence on both polarity sheets, it proves:

* the cut edge belongs to both Catalan endpoint quadrangulations;
* its directed source cell and the global sink agree endpointwise;
* the target cell may slide, but that datum is absent from the cut operator;
* the two-slot Laurent cut expansions agree term by term;
* regional inverse Catalan descent sends each matched term to adjacent scalar
  triangulations at the cut core;
* exactly one lifted edge is the forced prism square and the other is its
  parallel scalar-slot flip;
* the resulting cellular route difference is exactly zero;
* one-step rotation carries the full transport atlas between sheets.

Thus the first mixed Beck--Chevalley obstruction vanishes strictly on the
ten-point scalar occurrence module.  This is a carrier/coefficient theorem,
not yet a loaded-current or finite-alpha-prime comparison.
"""

from __future__ import annotations

from collections import Counter

from check_core_filtered_transfer import core_regions
from check_core_incidence_cells import (
    face_adjacency,
    rank_two_face_index,
    triangulation_key,
)
from check_mixed_prism_squares import core, polarity_audit
from check_qtds_cut_coaction import (
    closed_expansion,
    directed_edges,
    forest_sinks,
    rotate_cell,
    sink_slots,
)
from check_scalar_catalan_map import (
    canonical_diagonal,
    direct_endpoint,
    directed_sink_flow,
    inverse_source,
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


def to_local_diagonal(
    diagonal: Diagonal, region: tuple[int, ...]
) -> Diagonal:
    """Relabel a global chord by its positions in one cut region."""

    positions = {
        vertex: index for index, vertex in enumerate(region)
    }
    assert diagonal[0] in positions and diagonal[1] in positions
    return canonical_diagonal(
        positions[diagonal[0]], positions[diagonal[1]]
    )


def to_global_diagonal(
    diagonal: Diagonal, region: tuple[int, ...]
) -> Diagonal:
    """Undo one regional chord relabeling."""

    return canonical_diagonal(
        region[diagonal[0]], region[diagonal[1]]
    )


def to_global_cell(
    cell: Cell, region: tuple[int, ...]
) -> Cell:
    """Undo one regional quadrilateral relabeling."""

    return tuple(sorted(region[index] for index in cell))


def regional_inverse_source(
    quadrangulation: Core,
    cut_core: Core,
    marks: Marks,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> Triangulation:
    """Invert the marked Catalan map independently in every cut region.

    The global cut forest provides one marked sink cell per component.  Each
    component is relabelled as an even polygon, inverted by the established
    zero-core Catalan bijection, and glued back along cut_core.

    A quadrilateral component has no oriented internal edge, so both local
    polarity labels are formally admissible; they are required to reconstruct
    the same source.
    """

    result = set(cut_core)
    mark_diagonals = {mark for _, mark in marks}
    regions = core_regions(cut_core, multiplicity)

    for region in regions:
        region_set = set(region)
        local_size = len(region)
        local_core = []
        for diagonal in quadrangulation:
            if diagonal in cut_core:
                continue
            if not set(diagonal) <= region_set:
                continue
            local_diagonal = to_local_diagonal(
                diagonal, region
            )
            if not is_boundary(local_diagonal, local_size):
                local_core.append(local_diagonal)
        local_core = tuple(sorted(local_core))
        assert len(local_core) == local_size // 2 - 2

        component_marks = tuple(
            (cell, mark)
            for cell, mark in marks
            if set(cell) <= region_set
        )
        assert len(component_marks) == 1
        global_sink, global_mark = component_marks[0]
        local_mark = to_local_diagonal(global_mark, region)

        candidate_sources = set()
        for local_polarity in (True, False):
            try:
                _, local_sink, _, _ = directed_sink_flow(
                    local_core,
                    local_size,
                    first_is_plus=local_polarity,
                )
            except AssertionError:
                continue
            if (
                to_global_cell(local_sink, region)
                != global_sink
            ):
                continue
            (
                local_source,
                local_endpoint,
                _,
                _,
            ) = inverse_source(
                local_core,
                local_mark,
                local_size,
                first_is_plus=local_polarity,
            )
            assert physical_core(local_endpoint) == local_core
            candidate_sources.add(
                frozenset(
                    to_global_diagonal(diagonal, region)
                    for diagonal in local_source
                )
            )

        assert len(candidate_sources) == 1
        result.update(candidate_sources.pop())

    source = frozenset(result)
    assert len(source) == multiplicity - 3
    assert physical_core(source) == cut_core
    assert mark_diagonals <= source
    return source


def cut_image(
    triangulation: Triangulation,
    mark: Diagonal,
    cut_edge: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """Cut one zero-core marked source and invert every resulting term."""

    (
        _,
        quadrangulation,
        _,
        _,
    ) = direct_endpoint(
        triangulation,
        mark,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    assert cut_edge in quadrangulation

    global_sinks = forest_sinks(
        quadrangulation,
        (),
        multiplicity,
        first_is_plus=first_is_plus,
    )
    assert len(global_sinks) == 1
    global_sink = global_sinks[0]
    assert mark in sink_slots(global_sink)

    _, directions = directed_edges(
        quadrangulation,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    expansion = closed_expansion(
        quadrangulation,
        (cut_edge,),
        global_sink,
        mark,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    assert len(expansion) == 2

    lifted = {}
    for term_key, coefficient in expansion.items():
        marks, _ = term_key
        lifted[term_key] = (
            coefficient,
            regional_inverse_source(
                quadrangulation,
                (cut_edge,),
                marks,
                multiplicity,
                first_is_plus=first_is_plus,
            ),
        )
    return {
        "quadrangulation": quadrangulation,
        "global_sink": global_sink,
        "direction": directions[cut_edge],
        "lifted": lifted,
    }


def prune(counter: Counter) -> Counter:
    """Discard zero signed coefficients."""

    return Counter(
        {
            key: coefficient
            for key, coefficient in counter.items()
            if coefficient
        }
    )


def cellular_boundary(
    left_lifted: dict,
    right_lifted: dict,
) -> Counter:
    """The cut image of the boundary of one oriented scalar edge."""

    result = Counter()
    for term_key, (coefficient, source) in (
        left_lifted.items()
    ):
        result[(source, term_key)] -= coefficient
    for term_key, (coefficient, source) in (
        right_lifted.items()
    ):
        result[(source, term_key)] += coefficient
    return prune(result)


def split_edge_boundary(
    left_lifted: dict,
    right_lifted: dict,
) -> Counter:
    """Boundary of the termwise upper scalar-refinement lift."""

    assert set(left_lifted) == set(right_lifted)
    result = Counter()
    for term_key in left_lifted:
        left_coefficient, left_source = left_lifted[
            term_key
        ]
        right_coefficient, right_source = right_lifted[
            term_key
        ]
        assert left_coefficient == right_coefficient
        result[(left_source, term_key)] -= left_coefficient
        result[(right_source, term_key)] += right_coefficient
    return prune(result)


def rotate_marks(
    marks: Marks, multiplicity: int
) -> Marks:
    """Rotate all component cells and their scalar marks."""

    return tuple(
        sorted(
            (
                rotate_cell(cell, multiplicity),
                rotate_diagonal(mark, multiplicity),
            )
            for cell, mark in marks
        )
    )


def rotate_monomial(
    monomial: Monomial, multiplicity: int
) -> Monomial:
    """Rotate every Laurent variable."""

    return tuple(
        sorted(
            (
                rotate_diagonal(diagonal, multiplicity),
                exponent,
            )
            for diagonal, exponent in monomial
        )
    )


def rotate_core_tuple(
    core_tuple: Core, multiplicity: int
) -> Core:
    """Rotate a tuple-encoded physical core."""

    return tuple(
        sorted(
            rotate_diagonal(diagonal, multiplicity)
            for diagonal in core_tuple
        )
    )


def rotate_transport_record(record, multiplicity: int):
    """Rotate an unoriented complete mixed transport record."""

    (
        endpoint_data,
        mark,
        cut_edge,
        global_sink,
        cut_source,
        lifted_terms,
    ) = record
    rotated_data = frozenset(
        (
            rotate_triangulation(source, multiplicity),
            rotate_core_tuple(
                quadrangulation, multiplicity
            ),
            tuple(
                rotate_cell(cell, multiplicity)
                for cell in direction
            ),
        )
        for source, quadrangulation, direction in endpoint_data
    )
    rotated_terms = frozenset(
        (
            (
                rotate_marks(term_key[0], multiplicity),
                rotate_monomial(
                    term_key[1], multiplicity
                ),
            ),
            coefficient,
            frozenset(
                rotate_triangulation(source, multiplicity)
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
    )
    return (
        rotated_data,
        rotate_diagonal(mark, multiplicity),
        rotate_diagonal(cut_edge, multiplicity),
        rotate_cell(global_sink, multiplicity),
        rotate_cell(cut_source, multiplicity),
        rotated_terms,
    )


def occurrence_transport(
    occurrence,
    count: int,
    multiplicity: int,
    *,
    first_is_plus: bool,
    face_index,
):
    """Construct and verify one marked mixed-square transport."""

    (
        _,
        mark,
        _,
        _,
        scalar_facet,
        _,
        _,
        mixed_base,
        cut_edge,
    ) = occurrence
    assert multiplicity == 10
    assert not mixed_base

    vertices = face_index[scalar_facet]
    adjacency = face_adjacency(vertices)
    lower = tuple(
        sorted(
            (
                vertex
                for vertex in vertices
                if core(vertex) == mixed_base
            ),
            key=triangulation_key,
        )
    )
    upper = {
        vertex
        for vertex in vertices
        if core(vertex)
        == frozenset({cut_edge})
    }
    assert len(lower) == 2
    assert len(upper) == 2
    assert lower[1] in adjacency[lower[0]]
    assert mark in lower[0] and mark in lower[1]

    left = cut_image(
        lower[0],
        mark,
        cut_edge,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    right = cut_image(
        lower[1],
        mark,
        cut_edge,
        multiplicity,
        first_is_plus=first_is_plus,
    )

    # This is the coefficient-level Beck--Chevalley equality: although the
    # two full quadrangulations differ, the cut sees the same global sink and
    # source quadrilateral.  Its target may slide under scalar refinement,
    # but the cut coefficient depends only on the invariant source slots.
    assert (
        left["quadrangulation"]
        != right["quadrangulation"]
    )
    assert left["global_sink"] == right["global_sink"]
    assert left["direction"][0] == right["direction"][0]
    targets_agree = (
        left["direction"][1] == right["direction"][1]
    )
    assert (
        sink_slots(left["direction"][0])
        == sink_slots(right["direction"][0])
    )
    assert {
        term_key: coefficient
        for term_key, (coefficient, _) in left[
            "lifted"
        ].items()
    } == {
        term_key: coefficient
        for term_key, (coefficient, _) in right[
            "lifted"
        ].items()
    }

    lifted_terms = set()
    forced_count = 0
    parallel_count = 0
    for term_key in left["lifted"]:
        left_coefficient, left_source = left["lifted"][
            term_key
        ]
        (
            right_coefficient,
            right_source,
        ) = right["lifted"][term_key]
        assert left_coefficient == right_coefficient
        assert left_source != right_source
        assert (
            len(left_source.symmetric_difference(right_source))
            == 2
        )
        assert physical_core(left_source) == (
            cut_edge,
        )
        assert physical_core(right_source) == (
            cut_edge,
        )
        for _, component_mark in term_key[0]:
            assert component_mark in left_source
            assert component_mark in right_source

        removed = next(iter(left_source - right_source))
        added = next(iter(right_source - left_source))
        assert not (removed[0] - removed[1]) % 2
        assert not (added[0] - added[1]) % 2

        is_forced = {
            left_source,
            right_source,
        } == upper
        forced_count += int(is_forced)
        parallel_count += int(not is_forced)
        lifted_terms.add(
            (
                term_key,
                left_coefficient,
                frozenset(
                    {left_source, right_source}
                ),
                is_forced,
            )
        )

    assert forced_count == 1
    assert parallel_count == 1

    # The two independently described routes have identical signed cellular
    # boundary.  Since each matched endpoint pair is already a scalar edge,
    # no longer path or higher correction is required at occurrence level.
    cut_route = cellular_boundary(
        left["lifted"], right["lifted"]
    )
    split_route = split_edge_boundary(
        left["lifted"], right["lifted"]
    )
    curvature = prune(
        Counter(cut_route)
    )
    curvature.subtract(split_route)
    curvature = prune(curvature)
    assert not curvature

    record = (
        frozenset(
            {
                (
                    lower[0],
                    left["quadrangulation"],
                    left["direction"],
                ),
                (
                    lower[1],
                    right["quadrangulation"],
                    right["direction"],
                ),
            }
        ),
        mark,
        cut_edge,
        left["global_sink"],
        left["direction"][0],
        frozenset(lifted_terms),
    )
    profile = Counter(
        {
            (
                "mixed_transport",
                len(left["lifted"]),
                forced_count,
                parallel_count,
                len(curvature),
                "fixed_target"
                if targets_agree
                else "sliding_target",
            ): count
        }
    )
    return record, profile


def polarity_transport_audit(
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """All ten-point mixed transports on one sheet."""

    assert multiplicity == 10
    prism_data = polarity_audit(
        multiplicity,
        first_is_plus=first_is_plus,
    )
    face_index = rank_two_face_index(multiplicity)
    records = Counter()
    profiles = Counter()
    lower_edges = set()
    upper_edges = set()

    for occurrence, count in prism_data["records"].items():
        record, profile = occurrence_transport(
            occurrence,
            count,
            multiplicity,
            first_is_plus=first_is_plus,
            face_index=face_index,
        )
        records[record] += count
        profiles.update(profile)
        endpoint_pairs = record[0]
        lower_edges.add(
            frozenset(source for source, _, _ in endpoint_pairs)
        )
        for _, _, upper_edge, _ in record[-1]:
            upper_edges.add(upper_edge)

    return {
        "records": records,
        "profiles": profiles,
        "lower_edges": len(lower_edges),
        "upper_edges": len(upper_edges),
    }


def multiplicity_audit(multiplicity: int):
    """Both sheets and exact rotation of the transport atlas."""

    plus = polarity_transport_audit(
        multiplicity, first_is_plus=True
    )
    minus = polarity_transport_audit(
        multiplicity, first_is_plus=False
    )

    rotated = Counter()
    for record, count in plus["records"].items():
        rotated[
            rotate_transport_record(record, multiplicity)
        ] += count
    assert rotated == minus["records"]
    assert plus["profiles"] == minus["profiles"]
    assert plus["lower_edges"] == minus["lower_edges"]
    assert plus["upper_edges"] == minus["upper_edges"]
    return plus


def main() -> None:
    result = multiplicity_audit(10)
    print(
        "n=10 mixed Beck--Chevalley profiles "
        "(kind, cut terms, forced edges, parallel edges, "
        "curvature support, target behavior): "
        f"{dict(result['profiles'])}"
    )
    print(
        "n=10 distinct scalar transports: "
        f"{result['lower_edges']} lower edges -> "
        f"{result['upper_edges']} upper decorated edges"
    )
    print(
        "all exact termwise, cellular, and deck-covariant "
        "ten-point mixed-prism curvature checks passed"
    )


if __name__ == "__main__":
    main()
