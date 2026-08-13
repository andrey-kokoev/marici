"""Exact rank-three saturation audit for the scalar Catalan transfer.

Rank-two transfer homotopies are carried by squares and pentagons.  This
script tests whether they already satisfy their first higher compatibility.
Three physicalizing steps span one of three associahedral faces:

* three independent dependency chains: a cube;
* two consecutive steps and one independent step: pentagon x interval;
* three consecutive steps in one chain: the associahedron of a hexagon.

The inherited carriers cover every cube facet but not every prism or
hexagon-associahedron facet.  The script classifies the missing cells,
computes the topology of the covered and complementary subcomplexes, then
performs the minimal scalar-side saturation by adjoining the actual missing
associahedral facets.  The completed signed two-sphere boundaries and their
one-step deck covariance are checked through twelve points.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product

from check_j_reconstruction import triangulations
from check_scalar_catalan_map import (
    direct_endpoint,
    rotate_diagonal,
    rotate_triangulation,
)
from check_core_incidence_cells import (
    FaceKey,
    Path,
    Triangulation,
    canonical_edge,
    face_adjacency,
    face_edge_set,
    path_chain,
    polarity_audit,
    rank_two_face_index,
    rotate_face_key,
    signed_difference,
    state_at_prefixes,
    triangulation_key,
    vertex_boundary,
    zero_core_cells,
)


RankThreeKind = str


def face_key(common: FaceKey):
    """Stable key for a common dissection."""

    return tuple(sorted(common))


def edge_key(edge: tuple[Triangulation, Triangulation]):
    """Stable key for a canonically oriented flip edge."""

    return tuple(map(triangulation_key, edge))


def prune(counter: Counter) -> Counter:
    """Retain nonzero signed coefficients."""

    return Counter(
        {
            key: coefficient
            for key, coefficient in counter.items()
            if coefficient
        }
    )


def scale(counter: Counter, coefficient: int) -> Counter:
    """Multiply a signed counter by an integer."""

    return Counter(
        {
            key: coefficient * value
            for key, value in counter.items()
            if coefficient * value
        }
    )


def add_scaled(target: Counter, source: Counter, coefficient: int) -> None:
    """Add a signed multiple without Counter positivity truncation."""

    for key, value in source.items():
        target[key] += coefficient * value


def oriented_cycle_key(cycle: Counter):
    """Serializable key retaining the orientation of an edge cycle."""

    return tuple(
        (edge_key(edge), cycle[edge])
        for edge in sorted(cycle, key=edge_key)
    )


def canonical_cycle(cycle: Counter) -> Counter:
    """Canonicalize a polygonal boundary up to global orientation."""

    assert cycle
    assert not vertex_boundary(cycle)
    forward = oriented_cycle_key(cycle)
    backward = oriented_cycle_key(scale(cycle, -1))
    return cycle if forward < backward else scale(cycle, -1)


def rank_three_face_index(
    multiplicity: int,
) -> dict[FaceKey, tuple[Triangulation, ...]]:
    """Index every codimension-three associahedral face."""

    index = defaultdict(list)
    for triangulation in triangulations(tuple(range(multiplicity))):
        for removed in combinations(triangulation, 3):
            common = frozenset(set(triangulation) - set(removed))
            index[common].append(triangulation)
    result = {
        common: tuple(sorted(set(vertices), key=triangulation_key))
        for common, vertices in index.items()
    }
    assert set(map(len, result.values())) <= {8, 10, 14}
    return result


def rank_two_carriers(
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> dict[tuple[object, FaceKey], Counter]:
    """One unoriented signed transfer cycle for every marked rank-two face."""

    audit = polarity_audit(
        multiplicity,
        first_is_plus=first_is_plus,
        face_index=rank_two_face_index(multiplicity),
    )
    result: dict[tuple[object, FaceKey], Counter] = {}
    for record in audit["coherence_records"]:
        source, mark, common, kind, *paths = record
        assert mark in source
        if kind == "square":
            routes = paths[0]
            cycle = signed_difference(
                path_chain(routes[0]), path_chain(routes[1])
            )
        else:
            assert kind == "pentagon"
            direct, complement = paths
            cycle = signed_difference(
                path_chain(direct), path_chain(complement)
            )
        cycle = canonical_cycle(cycle)
        key = (mark, common)
        if key in result:
            assert oriented_cycle_key(result[key]) == oriented_cycle_key(
                cycle
            )
        else:
            result[key] = cycle
    return result


def state_with_increments(
    source: Triangulation,
    chains: tuple[tuple[object, ...], ...],
    positions: tuple[int, ...],
    increments: dict[int, int],
    multiplicity: int,
) -> Triangulation:
    """Apply a bounded increment to selected dependency-chain prefixes."""

    target = tuple(
        position + increments.get(index, 0)
        for index, position in enumerate(positions)
    )
    assert all(
        target[index] <= len(chain)
        for index, chain in enumerate(chains)
    )
    return state_at_prefixes(source, chains, target, multiplicity)


def common_dissection(states: tuple[Triangulation, ...]) -> FaceKey:
    """Intersection of a nonempty collection of triangulations."""

    assert states
    return frozenset.intersection(*states)


def physical_degree(common: FaceKey) -> int:
    """Number of opposite-color diagonals in an alternating dissection."""

    return sum((first - second) % 2 for first, second in common)


def direct_rank_three_occurrences(
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> Counter:
    """All marked rank-three blocks in the dependency-chain transfer."""

    records = Counter()
    for source in zero_core_cells(multiplicity):
        for mark in source:
            _, _, chains, _ = direct_endpoint(
                source,
                mark,
                multiplicity,
                first_is_plus=first_is_plus,
            )
            ranges = tuple(range(len(chain) + 1) for chain in chains)
            for positions in product(*ranges):
                active = tuple(
                    index
                    for index, chain in enumerate(chains)
                    if positions[index] < len(chain)
                )

                # Three independent steps give a cube.
                for selected in combinations(active, 3):
                    states = tuple(
                        state_with_increments(
                            source,
                            chains,
                            positions,
                            {
                                selected[index]: bit
                                for index, bit in enumerate(bits)
                            },
                            multiplicity,
                        )
                        for bits in product((0, 1), repeat=3)
                    )
                    common = common_dissection(states)
                    assert len(common) == multiplicity - 6
                    assert mark in common
                    records[(source, mark, common, "cube")] += 1

                # A consecutive pair and one independent step give a
                # pentagonal prism.
                for repeated in active:
                    if positions[repeated] + 2 > len(chains[repeated]):
                        continue
                    for independent in active:
                        if independent == repeated:
                            continue
                        states = tuple(
                            state_with_increments(
                                source,
                                chains,
                                positions,
                                {
                                    repeated: repeated_increment,
                                    independent: independent_increment,
                                },
                                multiplicity,
                            )
                            for repeated_increment in range(3)
                            for independent_increment in range(2)
                        )
                        common = common_dissection(states)
                        assert len(common) == multiplicity - 6
                        assert mark in common
                        records[
                            (source, mark, common, "pentagonal_prism")
                        ] += 1

                # Three consecutive dependent steps give the
                # three-dimensional associahedron of a hexagon.
                for repeated in active:
                    if positions[repeated] + 3 > len(chains[repeated]):
                        continue
                    states = tuple(
                        state_with_increments(
                            source,
                            chains,
                            positions,
                            {repeated: increment},
                            multiplicity,
                        )
                        for increment in range(4)
                    )
                    common = common_dissection(states)
                    assert len(common) == multiplicity - 6
                    assert mark in common
                    records[
                        (source, mark, common, "hexagon_associahedron")
                    ] += 1
    return records


def rank_two_facets(
    common: FaceKey,
    vertices: tuple[Triangulation, ...],
) -> dict[FaceKey, tuple[Triangulation, ...]]:
    """All polygonal facets in one rank-three associahedral face."""

    extras = set().union(*vertices) - set(common)
    result = {}
    for diagonal in extras:
        facet_common = frozenset(set(common) | {diagonal})
        facet_vertices = tuple(
            vertex for vertex in vertices if diagonal in vertex
        )
        assert len(facet_vertices) in {4, 5}
        result[facet_common] = facet_vertices
    return result


def polygon_cycle(vertices: tuple[Triangulation, ...]) -> Counter:
    """Canonical signed boundary of a square or pentagon."""

    adjacency = face_adjacency(vertices)
    start = min(vertices, key=triangulation_key)
    following = min(adjacency[start], key=triangulation_key)
    path = [start, following]
    previous, current = start, following
    while current != start:
        following = next(
            neighbor
            for neighbor in adjacency[current]
            if neighbor != previous
        )
        previous, current = current, following
        path.append(current)
    assert len(path) == len(vertices) + 1
    return canonical_cycle(path_chain(tuple(path)))


def component_count(nodes, neighbors) -> int:
    """Connected-component count of a finite adjacency graph."""

    unseen = set(nodes)
    count = 0
    while unseen:
        count += 1
        pending = [unseen.pop()]
        while pending:
            current = pending.pop()
            for neighbor in neighbors(current):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    pending.append(neighbor)
    return count


def subcomplex_profile(
    facets: dict[FaceKey, tuple[Triangulation, ...]],
    selected: set[FaceKey],
) -> tuple[int, int, int, int, int, int]:
    """Cell counts and boundary topology of a selected facet union."""

    if not selected:
        return (0, 0, 0, 0, 0, 0)

    facet_edges = {
        facet: face_edge_set(facets[facet])
        for facet in selected
    }
    edges = set().union(*facet_edges.values())
    vertices = set().union(
        *(set(facets[facet]) for facet in selected)
    )
    edge_multiplicity = Counter(
        edge
        for facet in selected
        for edge in facet_edges[facet]
    )
    boundary_edges = {
        edge
        for edge, multiplicity in edge_multiplicity.items()
        if multiplicity == 1
    }
    assert set(edge_multiplicity.values()) <= {1, 2}

    facet_components = component_count(
        selected,
        lambda facet: {
            other
            for other in selected
            if other != facet
            and facet_edges[facet] & facet_edges[other]
        },
    )

    if boundary_edges:
        boundary_vertices = set().union(
            *(set(edge) for edge in boundary_edges)
        )
        boundary_adjacency = defaultdict(set)
        for first, second in boundary_edges:
            boundary_adjacency[first].add(second)
            boundary_adjacency[second].add(first)
        assert set(
            len(boundary_adjacency[vertex])
            for vertex in boundary_vertices
        ) == {2}
        boundary_components = component_count(
            boundary_vertices,
            lambda vertex: boundary_adjacency[vertex],
        )
    else:
        boundary_components = 0

    return (
        len(selected),
        len(vertices),
        len(edges),
        len(vertices) - len(edges) + len(selected),
        facet_components,
        boundary_components,
    )


EXPECTED = {
    "cube": {
        "vertices": 8,
        "facets": Counter({"square": 6}),
    },
    "pentagonal_prism": {
        "vertices": 10,
        "facets": Counter({"square": 5, "pentagon": 2}),
    },
    "hexagon_associahedron": {
        "vertices": 14,
        "facets": Counter({"square": 3, "pentagon": 6}),
    },
}


def orient_surface(
    facets: dict[FaceKey, tuple[Triangulation, ...]],
    cycles: dict[FaceKey, Counter],
) -> dict[FaceKey, Counter]:
    """Orient all polygonal facets so their signed edge boundary vanishes."""

    edge_incidence = defaultdict(list)
    for facet, cycle in cycles.items():
        assert set(cycle) == face_edge_set(facets[facet])
        assert set(map(abs, cycle.values())) == {1}
        for edge, coefficient in cycle.items():
            edge_incidence[edge].append((facet, coefficient))

    assert edge_incidence
    assert set(map(len, edge_incidence.values())) == {2}

    first = min(facets, key=face_key)
    signs = {first: 1}
    pending = [first]
    while pending:
        facet = pending.pop()
        for edge, coefficient in cycles[facet].items():
            incidences = edge_incidence[edge]
            other, other_coefficient = (
                incidences[1]
                if incidences[0][0] == facet
                else incidences[0]
            )
            required = (
                -signs[facet] * coefficient // other_coefficient
            )
            assert required in {-1, 1}
            if other in signs:
                assert signs[other] == required
            else:
                signs[other] = required
                pending.append(other)

    assert set(signs) == set(facets)
    total = Counter()
    oriented = {}
    for facet in facets:
        oriented[facet] = scale(cycles[facet], signs[facet])
        add_scaled(total, oriented[facet], 1)
    assert not prune(total)
    return oriented


def raw_surface_key(surface: dict[FaceKey, Counter]):
    """Serializable oriented two-sphere boundary."""

    return tuple(
        (face_key(facet), oriented_cycle_key(surface[facet]))
        for facet in sorted(surface, key=face_key)
    )


def canonical_surface_key(surface: dict[FaceKey, Counter]):
    """Canonicalize the orientation of a closed surface up to one sign."""

    forward = raw_surface_key(surface)
    backward = raw_surface_key(
        {facet: scale(cycle, -1) for facet, cycle in surface.items()}
    )
    return min(forward, backward)


def rotate_cycle(cycle: Counter, multiplicity: int) -> Counter:
    """Push a signed edge cycle through one-step rotation."""

    result = Counter()
    for (first, second), coefficient in cycle.items():
        rotated_first = rotate_triangulation(first, multiplicity)
        rotated_second = rotate_triangulation(second, multiplicity)
        low, high, sign = canonical_edge(
            rotated_first, rotated_second
        )
        result[(low, high)] += coefficient * sign
    return prune(result)


def rotate_surface(
    surface: dict[FaceKey, Counter],
    multiplicity: int,
) -> dict[FaceKey, Counter]:
    """Push an oriented facet surface through one-step rotation."""

    return {
        rotate_face_key(facet, multiplicity): rotate_cycle(
            cycle, multiplicity
        )
        for facet, cycle in surface.items()
    }


def polarity_rank_three_audit(
    multiplicity: int,
    *,
    first_is_plus: bool,
    face_index: dict[FaceKey, tuple[Triangulation, ...]],
):
    """Facet coverage and signed closure for one polarity."""

    carriers = rank_two_carriers(
        multiplicity, first_is_plus=first_is_plus
    )
    occurrences = direct_rank_three_occurrences(
        multiplicity, first_is_plus=first_is_plus
    )
    surfaces: dict[
        tuple[object, FaceKey, RankThreeKind],
        dict[FaceKey, Counter],
    ] = {}
    occurrence_profiles = Counter()
    face_sets = defaultdict(set)
    coverage_profiles = Counter()
    coverage_topology_profiles = Counter()
    missing_facet_profiles = Counter()
    missing_facet_ids = set()

    for (source, mark, common, kind), count in occurrences.items():
        assert source
        vertices = face_index[common]
        expected = EXPECTED[kind]
        assert len(vertices) == expected["vertices"]
        facets = rank_two_facets(common, vertices)
        profile = Counter(
            "square" if len(facet_vertices) == 4 else "pentagon"
            for facet_vertices in facets.values()
        )
        assert profile == expected["facets"]

        covered = {
            facet
            for facet in facets
            if (mark, facet) in carriers
        }
        missing = set(facets) - covered
        covered_profile = Counter(
            "square" if len(facets[facet]) == 4 else "pentagon"
            for facet in covered
        )
        missing_profile = Counter(
            "square" if len(facets[facet]) == 4 else "pentagon"
            for facet in missing
        )
        coverage_profiles[
            (
                kind,
                covered_profile["square"],
                covered_profile["pentagon"],
                missing_profile["square"],
                missing_profile["pentagon"],
            )
        ] += count

        for facet in missing:
            extra = next(iter(set(facet) - set(common)))
            facet_kind = (
                "square" if len(facets[facet]) == 4 else "pentagon"
            )
            extra_kind = (
                "physical"
                if (extra[0] - extra[1]) % 2
                else "scalar"
            )
            missing_facet_profiles[
                (
                    kind,
                    facet_kind,
                    extra_kind,
                    physical_degree(common),
                    physical_degree(facet),
                )
            ] += count
            missing_facet_ids.add((mark, facet))

        occurrence_profiles[kind] += count
        face_sets[kind].add(common)
        for label, selected in (
            ("covered", covered),
            ("missing", missing),
        ):
            coverage_topology_profiles[
                (kind, label)
                + subcomplex_profile(facets, selected)
            ] += count

        cycles = {
            facet: polygon_cycle(facet_vertices)
            for facet, facet_vertices in facets.items()
        }
        for facet in covered:
            assert oriented_cycle_key(cycles[facet]) == (
                oriented_cycle_key(carriers[(mark, facet)])
            )
        surface = orient_surface(facets, cycles)
        surface_id = (mark, common, kind)
        if surface_id in surfaces:
            assert canonical_surface_key(
                surfaces[surface_id]
            ) == canonical_surface_key(surface)
        else:
            surfaces[surface_id] = surface

    return {
        "occurrences": occurrences,
        "occurrence_profiles": occurrence_profiles,
        "face_counts": Counter(
            {
                kind: len(faces)
                for kind, faces in face_sets.items()
                if faces
            }
        ),
        "coverage_profiles": coverage_profiles,
        "coverage_topology_profiles": coverage_topology_profiles,
        "missing_facet_profiles": missing_facet_profiles,
        "missing_facet_ids": missing_facet_ids,
        "direct_carrier_count": len(carriers),
        "saturated_carrier_count": len(
            set(carriers) | missing_facet_ids
        ),
        "completed_surface_count": len(surfaces),
        "surfaces": surfaces,
    }


def multiplicity_audit(multiplicity: int):
    """Both polarities and full one-step deck covariance."""

    face_index = rank_three_face_index(multiplicity)
    plus = polarity_rank_three_audit(
        multiplicity,
        first_is_plus=True,
        face_index=face_index,
    )
    minus = polarity_rank_three_audit(
        multiplicity,
        first_is_plus=False,
        face_index=face_index,
    )

    rotated_occurrences = Counter()
    for (source, mark, common, kind), count in plus[
        "occurrences"
    ].items():
        rotated_occurrences[
            (
                rotate_triangulation(source, multiplicity),
                rotate_diagonal(mark, multiplicity),
                rotate_face_key(common, multiplicity),
                kind,
            )
        ] += count
    assert rotated_occurrences == minus["occurrences"]

    for (mark, common, kind), surface in plus["surfaces"].items():
        target = (
            rotate_diagonal(mark, multiplicity),
            rotate_face_key(common, multiplicity),
            kind,
        )
        assert canonical_surface_key(
            rotate_surface(surface, multiplicity)
        ) == canonical_surface_key(minus["surfaces"][target])

    rotated_missing = {
        (
            rotate_diagonal(mark, multiplicity),
            rotate_face_key(facet, multiplicity),
        )
        for mark, facet in plus["missing_facet_ids"]
    }
    assert rotated_missing == minus["missing_facet_ids"]

    for key in (
        "occurrence_profiles",
        "face_counts",
        "coverage_profiles",
        "coverage_topology_profiles",
        "missing_facet_profiles",
        "direct_carrier_count",
        "saturated_carrier_count",
        "completed_surface_count",
    ):
        assert plus[key] == minus[key]
    return plus


def main() -> None:
    for multiplicity in (6, 8, 10, 12):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} rank-three occurrences: "
            f"{dict(result['occurrence_profiles'])}"
        )
        print(
            f"n={multiplicity} distinct rank-three faces: "
            f"{dict(result['face_counts'])}"
        )
        print(
            f"n={multiplicity} facet coverage profiles "
            f"(kind, covered squares, covered pentagons, "
            f"missing squares, missing pentagons): "
            f"{dict(result['coverage_profiles'])}"
        )
        print(
            f"n={multiplicity} coverage topology profiles "
            f"(kind, subset, F, V, E, chi, components, "
            f"boundary components): "
            f"{dict(result['coverage_topology_profiles'])}"
        )
        print(
            f"n={multiplicity} missing facet profiles: "
            f"{dict(result['missing_facet_profiles'])}"
        )
        print(
            f"n={multiplicity} distinct marked missing facets: "
            f"{len(result['missing_facet_ids'])}"
        )
        print(
            f"n={multiplicity} marked rank-two carrier saturation: "
            f"{result['direct_carrier_count']} -> "
            f"{result['saturated_carrier_count']}; "
            f"{result['completed_surface_count']} completed "
            f"rank-three surfaces"
        )
    print(
        "exact deck-covariant rank-three obstruction and "
        "associahedral-saturation audit through twelve points passed"
    )


if __name__ == "__main__":
    main()
