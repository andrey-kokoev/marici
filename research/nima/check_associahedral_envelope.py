"""All-block audit for the marked associahedral-envelope lemma.

For every marked zero-core source, polarity, dependency-chain prefix, and
nonempty consecutive block through twelve points, verify:

* the common direct-state dissection is exactly the current triangulation
  with the selected block diagonals removed;
* selected diagonals from one dependency-chain block form one path component
  in the triangulation dual tree;
* distinct chain blocks give distinct components;
* a component with r selected dual edges exposes an (r+3)-gon and therefore
  contributes the r-dimensional associahedron K_r;
* the complete scalar face has product-Catalan vertex count;
* the complete block record is exchanged by one-step rotation.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb

from check_scalar_catalan_map import (
    canonical_diagonal,
    direct_endpoint,
    is_boundary,
    rotate_diagonal,
    rotate_triangulation,
)
from check_core_incidence_cells import (
    Triangulation,
    rotate_face_key,
    state_at_prefixes,
    zero_core_cells,
)
from check_core_incidence_rank_three import state_with_increments


Diagonal = tuple[int, int]


def catalan(index: int) -> int:
    """The exact Catalan number C_index."""

    return comb(2 * index, index) // (index + 1)


def triangulation_triangles(
    triangulation: Triangulation,
    multiplicity: int,
) -> tuple[tuple[int, int, int], ...]:
    """All ordinary triangular regions of a polygon triangulation."""

    result = []
    for vertices in combinations(range(multiplicity), 3):
        first, second, third = vertices
        edges = (
            canonical_diagonal(first, second),
            canonical_diagonal(second, third),
            canonical_diagonal(first, third),
        )
        if all(
            is_boundary(edge, multiplicity)
            or edge in triangulation
            for edge in edges
        ):
            result.append(vertices)
    assert len(result) == multiplicity - 2
    return tuple(result)


def triangle_edges(
    triangle: tuple[int, int, int],
) -> frozenset[Diagonal]:
    """The three edges of one triangle."""

    first, second, third = triangle
    return frozenset(
        {
            canonical_diagonal(first, second),
            canonical_diagonal(second, third),
            canonical_diagonal(first, third),
        }
    )


def graph_components(nodes, adjacency):
    """Connected components of a finite graph."""

    unseen = set(nodes)
    result = []
    while unseen:
        start = unseen.pop()
        component = {start}
        pending = [start]
        while pending:
            current = pending.pop()
            for neighbor in adjacency[current]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    pending.append(neighbor)
        result.append(frozenset(component))
    return tuple(result)


def selected_dual_components(
    triangulation: Triangulation,
    selected: frozenset[Diagonal],
    multiplicity: int,
):
    """Connected selected-edge components in the triangulation dual tree."""

    triangles = triangulation_triangles(triangulation, multiplicity)
    edges_by_triangle = tuple(map(triangle_edges, triangles))
    incidence = defaultdict(set)
    for index, edges in enumerate(edges_by_triangle):
        for edge in edges:
            incidence[edge].add(index)

    adjacency = {edge: set() for edge in selected}
    for edges in edges_by_triangle:
        hits = tuple(selected & edges)
        for first, second in combinations(hits, 2):
            adjacency[first].add(second)
            adjacency[second].add(first)

    components = graph_components(selected, adjacency)
    profiles = []
    for component in components:
        incident_triangles = set().union(
            *(incidence[edge] for edge in component)
        )
        assert all(len(incidence[edge]) == 2 for edge in component)
        assert len(incident_triangles) == len(component) + 1
        polygon_vertices = set().union(
            *(set(triangles[index]) for index in incident_triangles)
        )
        assert len(polygon_vertices) == len(component) + 3
        profiles.append(
            (
                component,
                frozenset(incident_triangles),
                frozenset(polygon_vertices),
            )
        )
    return tuple(profiles)


def polarity_audit(
    multiplicity: int,
    *,
    first_is_plus: bool,
):
    """Audit every nonempty block for one polarity sheet."""

    records = Counter()
    block_profiles = Counter()

    for source in zero_core_cells(multiplicity):
        for mark in source:
            _, _, chains, _ = direct_endpoint(
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
                remaining = tuple(
                    len(chain) - positions[index]
                    for index, chain in enumerate(chains)
                )
                increment_ranges = tuple(
                    range(count + 1) for count in remaining
                )
                for increments in product(*increment_ranges):
                    rank = sum(increments)
                    if not rank:
                        continue

                    chain_blocks = tuple(
                        frozenset(
                            chains[index][
                                positions[index] :
                                positions[index] + increment
                            ]
                        )
                        for index, increment in enumerate(increments)
                        if increment
                    )
                    selected = frozenset().union(*chain_blocks)
                    assert len(selected) == rank
                    assert selected <= current
                    assert mark not in selected

                    local_ranges = tuple(
                        range(increment + 1)
                        for increment in increments
                    )
                    states = tuple(
                        state_with_increments(
                            source,
                            chains,
                            positions,
                            {
                                index: local[index]
                                for index in range(len(chains))
                                if local[index]
                            },
                            multiplicity,
                        )
                        for local in product(*local_ranges)
                    )
                    common = frozenset.intersection(*states)
                    assert common == current - selected
                    assert len(current) - len(common) == rank
                    assert mark in common

                    dual_profiles = selected_dual_components(
                        current, selected, multiplicity
                    )
                    dual_components = {
                        profile[0] for profile in dual_profiles
                    }
                    assert dual_components == set(chain_blocks)

                    partition = tuple(
                        sorted(increments, reverse=True)
                    )
                    partition = tuple(
                        value for value in partition if value
                    )
                    exposed_polygon_sizes = tuple(
                        sorted(
                            (
                                len(profile[2])
                                for profile in dual_profiles
                            ),
                            reverse=True,
                        )
                    )
                    assert exposed_polygon_sizes == tuple(
                        size + 3 for size in partition
                    )
                    expected_vertices = 1
                    for size in partition:
                        expected_vertices *= catalan(size + 1)

                    block_profiles[
                        (rank, partition, expected_vertices)
                    ] += 1
                    records[
                        (
                            source,
                            mark,
                            current,
                            common,
                            partition,
                            expected_vertices,
                        )
                    ] += 1

    return {
        "records": records,
        "block_profiles": block_profiles,
    }


def multiplicity_audit(multiplicity: int):
    """Both polarity sheets and their full block-record rotation."""

    plus = polarity_audit(multiplicity, first_is_plus=True)
    minus = polarity_audit(multiplicity, first_is_plus=False)

    rotated = Counter()
    for (
        source,
        mark,
        current,
        common,
        partition,
        expected_vertices,
    ), count in plus["records"].items():
        rotated[
            (
                rotate_triangulation(source, multiplicity),
                rotate_diagonal(mark, multiplicity),
                rotate_triangulation(current, multiplicity),
                rotate_face_key(common, multiplicity),
                partition,
                expected_vertices,
            )
        ] += count
    assert rotated == minus["records"]
    assert plus["block_profiles"] == minus["block_profiles"]
    return plus


def main() -> None:
    for multiplicity in (6, 8, 10, 12):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} marked dependency-block profiles "
            f"(rank, partition, complete face vertices): "
            f"{dict(result['block_profiles'])}"
        )
    print(
        "all exact marked product-associahedral block-face checks "
        "through twelve points passed"
    )


if __name__ == "__main__":
    main()
