"""Classify the two forced squares in every pentagonal-prism carrier.

For each rank-three dependency block of type 2+1, the direct rank-two system
misses exactly two square facets.  This audit proves through twelve points:

* the physical fixed-diagonal facet is a Boolean square of two physical cuts;
* the scalar fixed-diagonal facet contains two scalar-refinement edges at
  cores P and P+e, joined by two physical incidence edges;
* one-step rotation carries the complete classification between sheets.

The first square is filled by the strict cut coaction.  Only the second is a
genuinely mixed scalar/physical Beck--Chevalley condition.
"""

from __future__ import annotations

from collections import Counter

from check_scalar_catalan_map import physical_core, rotate_diagonal, rotate_triangulation
from check_core_incidence_cells import (
    face_adjacency,
    rotate_face_key,
)
from check_core_incidence_rank_three import (
    direct_rank_three_occurrences,
    rank_three_face_index,
    rank_two_carriers,
    rank_two_facets,
)


def core(vertex):
    """Physical-core set of one scalar triangulation."""

    return frozenset(physical_core(vertex))


def powerset_two(first, second):
    """The four subsets of two elements."""

    return {
        frozenset(),
        frozenset({first}),
        frozenset({second}),
        frozenset({first, second}),
    }


def classify_physical_square(common, vertices):
    """A square with one fixed physical diagonal is a Boolean cut square."""

    base = frozenset(
        diagonal
        for diagonal in common
        if (diagonal[0] - diagonal[1]) % 2
    )
    cores = {core(vertex) for vertex in vertices}
    assert len(cores) == 4
    assert all(base <= item for item in cores)
    variables = set().union(*cores) - set(base)
    assert len(variables) == 2
    first, second = sorted(variables)
    assert cores == {
        base | subset
        for subset in powerset_two(first, second)
    }

    adjacency = face_adjacency(vertices)
    for vertex, neighbors in adjacency.items():
        for neighbor in neighbors:
            assert len(core(vertex) ^ core(neighbor)) == 1
    return base, (first, second)


def classify_mixed_square(common, vertices):
    """A scalar-refinement pair transported across one physical cut."""

    base = frozenset(
        diagonal
        for diagonal in common
        if (diagonal[0] - diagonal[1]) % 2
    )
    core_counts = Counter(map(core, vertices))
    assert core_counts[base] == 2
    upper_cores = tuple(
        item for item in core_counts if item != base
    )
    assert len(upper_cores) == 1
    upper = upper_cores[0]
    assert core_counts[upper] == 2
    assert len(upper - base) == 1
    assert base <= upper
    physical_edge = next(iter(upper - base))

    adjacency = face_adjacency(vertices)
    scalar_edges = set()
    physical_edges = set()
    for vertex, neighbors in adjacency.items():
        for neighbor in neighbors:
            edge = frozenset({vertex, neighbor})
            if core(vertex) == core(neighbor):
                scalar_edges.add(edge)
            else:
                assert core(vertex) ^ core(neighbor) == {
                    physical_edge
                }
                physical_edges.add(edge)
    assert len(scalar_edges) == 2
    assert len(physical_edges) == 2
    assert {
        core(next(iter(edge)))
        for edge in scalar_edges
    } == {base, upper}
    return base, physical_edge


def polarity_audit(multiplicity: int, *, first_is_plus: bool):
    """Every prism and its two missing squares for one sheet."""

    face_index = rank_three_face_index(multiplicity)
    carriers = rank_two_carriers(
        multiplicity, first_is_plus=first_is_plus
    )
    occurrences = direct_rank_three_occurrences(
        multiplicity, first_is_plus=first_is_plus
    )
    profiles = Counter()
    records = Counter()

    for (source, mark, common, kind), count in occurrences.items():
        if kind != "pentagonal_prism":
            continue
        facets = rank_two_facets(common, face_index[common])
        missing = {
            facet: vertices
            for facet, vertices in facets.items()
            if (mark, facet) not in carriers
        }
        assert len(missing) == 2

        physical_facets = {
            facet: vertices
            for facet, vertices in missing.items()
            if (
                extra := next(iter(set(facet) - set(common)))
            )[0] % 2
            != extra[1] % 2
        }
        scalar_facets = {
            facet: vertices
            for facet, vertices in missing.items()
            if facet not in physical_facets
        }
        assert len(physical_facets) == 1
        assert len(scalar_facets) == 1

        physical_facet, physical_vertices = next(
            iter(physical_facets.items())
        )
        scalar_facet, scalar_vertices = next(
            iter(scalar_facets.items())
        )
        physical_base, physical_variables = (
            classify_physical_square(
                physical_facet, physical_vertices
            )
        )
        mixed_base, mixed_edge = classify_mixed_square(
            scalar_facet, scalar_vertices
        )
        assert len(physical_base) == len(mixed_base) + 1

        profiles[
            (
                len(mixed_base),
                "boolean_physical_square",
            )
        ] += count
        profiles[
            (
                len(mixed_base),
                "mixed_beck_chevalley_square",
            )
        ] += count
        records[
            (
                source,
                mark,
                common,
                physical_facet,
                scalar_facet,
                physical_base,
                physical_variables,
                mixed_base,
                mixed_edge,
            )
        ] += count

    return {
        "profiles": profiles,
        "records": records,
    }


def rotate_core(core_set, multiplicity):
    """Rotate a frozenset of physical diagonals."""

    return frozenset(
        rotate_diagonal(diagonal, multiplicity)
        for diagonal in core_set
    )


def multiplicity_audit(multiplicity: int):
    """Both sheets and full classification rotation."""

    plus = polarity_audit(multiplicity, first_is_plus=True)
    minus = polarity_audit(multiplicity, first_is_plus=False)

    rotated = Counter()
    for (
        source,
        mark,
        common,
        physical_facet,
        scalar_facet,
        physical_base,
        physical_variables,
        mixed_base,
        mixed_edge,
    ), count in plus["records"].items():
        rotated[
            (
                rotate_triangulation(source, multiplicity),
                rotate_diagonal(mark, multiplicity),
                rotate_face_key(common, multiplicity),
                rotate_face_key(physical_facet, multiplicity),
                rotate_face_key(scalar_facet, multiplicity),
                rotate_core(physical_base, multiplicity),
                tuple(
                    sorted(
                        rotate_diagonal(edge, multiplicity)
                        for edge in physical_variables
                    )
                ),
                rotate_core(mixed_base, multiplicity),
                rotate_diagonal(mixed_edge, multiplicity),
            )
        ] += count
    assert rotated == minus["records"]
    assert plus["profiles"] == minus["profiles"]
    return plus


def main() -> None:
    for multiplicity in (6, 8, 10, 12):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} forced-prism square profiles: "
            f"{dict(result['profiles'])}"
        )
    print(
        "all exact physical-versus-mixed prism square checks "
        "through twelve points passed"
    )


if __name__ == "__main__":
    main()
