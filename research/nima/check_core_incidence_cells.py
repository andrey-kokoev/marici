"""Exact rank-two coherence audit for the scalar Catalan transfer.

The direct transfer associates to every marked zero-core triangulation a
disjoint union of ordered flip chains.  Its core-incidence coherences are not
uniformly cubical:

* next flips in two distinct chains commute and span an actual square face of
  the scalar associahedron;
* two consecutive flips in one chain span three vertices of an actual
  pentagon face, whose complementary three-edge path is the required
  rank-two homotopy.

The script verifies every available square and pentagon occurrence, mark
preservation, and one-step deck covariance through twelve points.  Regional
core-filtered transfers are products of these zero-core local models.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product

from check_j_reconstruction import triangulations
from check_scalar_catalan_map import (
    canonical_diagonal,
    direct_endpoint,
    flip_diagonal,
    physical_core,
    rotate_diagonal,
    rotate_triangulation,
)


Diagonal = tuple[int, int]
Triangulation = frozenset[Diagonal]
FaceKey = frozenset[Diagonal]
Path = tuple[Triangulation, ...]


def zero_core_cells(multiplicity: int) -> tuple[Triangulation, ...]:
    """All empty-physical-core scalar triangulations."""

    return tuple(
        triangulation
        for triangulation in triangulations(tuple(range(multiplicity)))
        if not physical_core(triangulation)
    )


def rank_two_face_index(
    multiplicity: int,
) -> dict[FaceKey, tuple[Triangulation, ...]]:
    """Index every codimension-two associahedral face by its dissection."""

    index = defaultdict(list)
    for triangulation in triangulations(tuple(range(multiplicity))):
        for removed in combinations(triangulation, 2):
            common = frozenset(set(triangulation) - set(removed))
            index[common].append(triangulation)
    result = {
        common: tuple(sorted(set(vertices), key=triangulation_key))
        for common, vertices in index.items()
    }
    assert set(map(len, result.values())) <= {4, 5}
    return result


def triangulation_key(triangulation: Triangulation):
    """Stable ordering key."""

    return tuple(sorted(triangulation))


def path_key(path: Path):
    """Stable ordering key for a path in the flip graph."""

    return tuple(map(triangulation_key, path))


def canonical_edge(
    first: Triangulation, second: Triangulation
) -> tuple[Triangulation, Triangulation, int]:
    """Canonicalize an oriented edge and retain its orientation sign."""

    assert len(first.symmetric_difference(second)) == 2
    if triangulation_key(first) < triangulation_key(second):
        return first, second, 1
    return second, first, -1


def path_chain(path: Path) -> Counter:
    """The signed cellular one-chain carried by an oriented path."""

    result = Counter()
    for first, second in zip(path, path[1:]):
        low, high, sign = canonical_edge(first, second)
        result[(low, high)] += sign
    return Counter(
        {
            key: coefficient
            for key, coefficient in result.items()
            if coefficient
        }
    )


def signed_difference(first: Counter, second: Counter) -> Counter:
    """Subtract signed counters without Counter's positivity truncation."""

    result = Counter(first)
    result.subtract(second)
    return Counter(
        {
            key: coefficient
            for key, coefficient in result.items()
            if coefficient
        }
    )


def vertex_boundary(chain: Counter) -> Counter:
    """Cellular boundary of a signed flip-edge chain."""

    result = Counter()
    for (first, second), coefficient in chain.items():
        result[first] -= coefficient
        result[second] += coefficient
    return Counter(
        {
            key: coefficient
            for key, coefficient in result.items()
            if coefficient
        }
    )


def face_edge_set(
    vertices: tuple[Triangulation, ...],
) -> set[tuple[Triangulation, Triangulation]]:
    """Unoriented flip edges in one rank-two associahedral face."""

    adjacency = face_adjacency(vertices)
    result = set()
    for first, neighbors in adjacency.items():
        for second in neighbors:
            low, high, _ = canonical_edge(first, second)
            result.add((low, high))
    return result


def coherence_boundary(
    direct: Path,
    alternate: Path,
    vertices: tuple[Triangulation, ...],
) -> Counter:
    """Verify the signed boundary equation for one square or pentagon."""

    assert direct[0] == alternate[0]
    assert direct[-1] == alternate[-1]
    cycle = signed_difference(
        path_chain(direct), path_chain(alternate)
    )
    assert not vertex_boundary(cycle)
    assert set(cycle) == face_edge_set(vertices)
    assert set(map(abs, cycle.values())) == {1}
    return cycle


def rotate_path(path: Path, multiplicity: int) -> Path:
    """Rotate every vertex of an oriented flip path."""

    return tuple(
        rotate_triangulation(vertex, multiplicity) for vertex in path
    )


def canonical_square_routes(first: Path, second: Path) -> tuple[Path, Path]:
    """Forget the arbitrary ordering of the two commuting routes."""

    return tuple(sorted((first, second), key=path_key))


def flip_once(
    triangulation: Triangulation,
    diagonal: Diagonal,
    multiplicity: int,
) -> Triangulation:
    """Apply one flip and discard the replacement label."""

    result, _ = flip_diagonal(
        triangulation, diagonal, multiplicity
    )
    return result


def state_at_prefixes(
    source: Triangulation,
    chains: tuple[tuple[Diagonal, ...], ...],
    positions: tuple[int, ...],
    multiplicity: int,
) -> Triangulation:
    """Apply a prefix of every dependency chain.

    Whole chain prefixes may be applied chain by chain because flips belonging
    to distinct chains commute.  The checks below independently reverify this
    local commutation at every state.
    """

    current = source
    for chain, position in zip(chains, positions, strict=True):
        for diagonal in chain[:position]:
            current = flip_once(current, diagonal, multiplicity)
    assert len(physical_core(current)) == sum(positions)
    return current


def face_adjacency(
    vertices: tuple[Triangulation, ...],
) -> dict[Triangulation, set[Triangulation]]:
    """Flip adjacency within a rank-two associahedral face."""

    adjacency = {vertex: set() for vertex in vertices}
    for first, second in combinations(vertices, 2):
        if len(first.symmetric_difference(second)) == 2:
            adjacency[first].add(second)
            adjacency[second].add(first)
    assert set(map(len, adjacency.values())) == {2}
    return adjacency


def complementary_pentagon_path(
    first: Triangulation,
    middle: Triangulation,
    last: Triangulation,
    vertices: tuple[Triangulation, ...],
) -> tuple[Triangulation, ...]:
    """The three-edge side complementary to first-middle-last."""

    assert len(vertices) == 5
    adjacency = face_adjacency(vertices)
    assert middle in adjacency[first]
    assert last in adjacency[middle]
    current = next(
        neighbor for neighbor in adjacency[first] if neighbor != middle
    )
    path = [first, current]
    previous = first
    while current != last:
        following = next(
            neighbor
            for neighbor in adjacency[current]
            if neighbor != previous
        )
        previous, current = current, following
        path.append(current)
    assert len(path) == 4
    assert middle not in path
    return tuple(path)


def rotate_face_key(
    common: FaceKey, multiplicity: int
) -> FaceKey:
    """Rotate a rank-two dissection by one external label."""

    return frozenset(
        rotate_diagonal(diagonal, multiplicity)
        for diagonal in common
    )


def polarity_audit(
    multiplicity: int,
    *,
    first_is_plus: bool,
    face_index: dict[FaceKey, tuple[Triangulation, ...]],
):
    """Audit every local rank-two cell for one polarity."""

    square_occurrences = 0
    pentagon_occurrences = 0
    square_faces = set()
    pentagon_faces = set()
    pentagon_core_profiles = Counter()
    incidence_records = Counter()
    coherence_records = Counter()
    signed_boundary_profiles = Counter()

    for source in zero_core_cells(multiplicity):
        for mark in source:
            endpoint, _, chains, _ = direct_endpoint(
                source,
                mark,
                multiplicity,
                first_is_plus=first_is_plus,
            )
            position_ranges = tuple(
                range(len(chain) + 1) for chain in chains
            )
            for positions in product(*position_ranges):
                current = state_at_prefixes(
                    source, chains, positions, multiplicity
                )

                # Incomparable next flips give the two orders around a
                # genuine square face.
                active = tuple(
                    index
                    for index, chain in enumerate(chains)
                    if positions[index] < len(chain)
                )
                for first_index, second_index in combinations(active, 2):
                    first_flip = chains[first_index][
                        positions[first_index]
                    ]
                    second_flip = chains[second_index][
                        positions[second_index]
                    ]
                    after_first = flip_once(
                        current, first_flip, multiplicity
                    )
                    after_second = flip_once(
                        current, second_flip, multiplicity
                    )
                    first_then_second = flip_once(
                        after_first, second_flip, multiplicity
                    )
                    second_then_first = flip_once(
                        after_second, first_flip, multiplicity
                    )
                    assert first_then_second == second_then_first
                    common = frozenset.intersection(
                        current,
                        after_first,
                        after_second,
                        first_then_second,
                    )
                    assert len(common) == multiplicity - 5
                    assert mark in common
                    vertices = face_index[common]
                    assert len(vertices) == 4
                    assert set(vertices) == {
                        current,
                        after_first,
                        after_second,
                        first_then_second,
                    }
                    face_adjacency(vertices)
                    first_route = (
                        current,
                        after_first,
                        first_then_second,
                    )
                    second_route = (
                        current,
                        after_second,
                        first_then_second,
                    )
                    for route in (first_route, second_route):
                        assert tuple(
                            len(physical_core(vertex))
                            - len(physical_core(current))
                            for vertex in route
                        ) == (0, 1, 2)
                    cycle = coherence_boundary(
                        first_route, second_route, vertices
                    )
                    signed_boundary_profiles[
                        ("square", len(cycle))
                    ] += 1
                    routes = canonical_square_routes(
                        first_route, second_route
                    )
                    square_occurrences += 1
                    square_faces.add(common)
                    incidence_records[
                        (source, mark, common, "square")
                    ] += 1
                    coherence_records[
                        (source, mark, common, "square", routes)
                    ] += 1

                # Comparable consecutive flips give one two-edge side of a
                # pentagon.  The other side is the canonical local homotopy.
                for chain_index, chain in enumerate(chains):
                    position = positions[chain_index]
                    if position + 1 >= len(chain):
                        continue
                    first_flip = chain[position]
                    second_flip = chain[position + 1]
                    middle = flip_once(
                        current, first_flip, multiplicity
                    )
                    last = flip_once(
                        middle, second_flip, multiplicity
                    )
                    common = current & middle & last
                    assert len(common) == multiplicity - 5
                    assert mark in common
                    vertices = face_index[common]
                    assert len(vertices) == 5
                    complement = complementary_pentagon_path(
                        current, middle, last, vertices
                    )
                    direct = (current, middle, last)
                    assert tuple(
                        len(physical_core(vertex))
                        - len(physical_core(current))
                        for vertex in direct
                    ) == (0, 1, 2)
                    relative_core_profile = tuple(
                        len(physical_core(vertex))
                        - len(physical_core(current))
                        for vertex in complement
                    )
                    assert relative_core_profile == (0, 0, 1, 2)
                    cycle = coherence_boundary(
                        direct, complement, vertices
                    )
                    signed_boundary_profiles[
                        ("pentagon", len(cycle))
                    ] += 1
                    pentagon_core_profiles[relative_core_profile] += 1
                    pentagon_occurrences += 1
                    pentagon_faces.add(common)
                    incidence_records[
                        (source, mark, common, "pentagon")
                    ] += 1
                    coherence_records[
                        (
                            source,
                            mark,
                            common,
                            "pentagon",
                            direct,
                            complement,
                        )
                    ] += 1

            assert state_at_prefixes(
                source,
                chains,
                tuple(map(len, chains)),
                multiplicity,
            ) == endpoint

    return {
        "square_occurrences": square_occurrences,
        "pentagon_occurrences": pentagon_occurrences,
        "square_faces": len(square_faces),
        "pentagon_faces": len(pentagon_faces),
        "pentagon_core_profiles": pentagon_core_profiles,
        "incidence_records": incidence_records,
        "coherence_records": coherence_records,
        "signed_boundary_profiles": signed_boundary_profiles,
    }


def multiplicity_audit(multiplicity: int):
    """Both polarities and their one-step deck transformation."""

    face_index = rank_two_face_index(multiplicity)
    plus = polarity_audit(
        multiplicity,
        first_is_plus=True,
        face_index=face_index,
    )
    minus = polarity_audit(
        multiplicity,
        first_is_plus=False,
        face_index=face_index,
    )

    rotated_plus = Counter()
    for (source, mark, common, kind), count in plus[
        "incidence_records"
    ].items():
        rotated_plus[
            (
                rotate_triangulation(source, multiplicity),
                rotate_diagonal(mark, multiplicity),
                rotate_face_key(common, multiplicity),
                kind,
            )
        ] += count
    assert rotated_plus == minus["incidence_records"]

    rotated_coherence = Counter()
    for record, count in plus["coherence_records"].items():
        source, mark, common, kind, *paths = record
        if kind == "square":
            routes = canonical_square_routes(
                *(
                    rotate_path(path, multiplicity)
                    for path in paths[0]
                )
            )
            rotated_record = (
                rotate_triangulation(source, multiplicity),
                rotate_diagonal(mark, multiplicity),
                rotate_face_key(common, multiplicity),
                kind,
                routes,
            )
        else:
            assert kind == "pentagon"
            direct, complement = paths
            rotated_record = (
                rotate_triangulation(source, multiplicity),
                rotate_diagonal(mark, multiplicity),
                rotate_face_key(common, multiplicity),
                kind,
                rotate_path(direct, multiplicity),
                rotate_path(complement, multiplicity),
            )
        rotated_coherence[rotated_record] += count
    assert rotated_coherence == minus["coherence_records"]

    expected_boundaries = Counter()
    if plus["square_occurrences"]:
        expected_boundaries[("square", 4)] = plus[
            "square_occurrences"
        ]
    if plus["pentagon_occurrences"]:
        expected_boundaries[("pentagon", 5)] = plus[
            "pentagon_occurrences"
        ]
    assert plus["signed_boundary_profiles"] == expected_boundaries

    for key in (
        "square_occurrences",
        "pentagon_occurrences",
        "square_faces",
        "pentagon_faces",
        "pentagon_core_profiles",
        "signed_boundary_profiles",
    ):
        assert plus[key] == minus[key]
    return plus


def main() -> None:
    for multiplicity in (6, 8, 10, 12):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} core-incidence rank two: "
            f"{result['square_occurrences']} marked square occurrences "
            f"on {result['square_faces']} scalar faces; "
            f"{result['pentagon_occurrences']} marked pentagon occurrences "
            f"on {result['pentagon_faces']} scalar faces"
        )
        print(
            f"n={multiplicity} complementary pentagon core profiles: "
            f"{dict(result['pentagon_core_profiles'])}"
        )
        print(
            f"n={multiplicity} signed boundary profiles: "
            f"{dict(result['signed_boundary_profiles'])}"
        )
    print(
        "all exact signed, deck-covariant rank-two scalar core-incidence "
        "checks through twelve points passed"
    )


if __name__ == "__main__":
    main()
