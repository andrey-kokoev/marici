"""Exact rank-four saturation audit for the scalar Catalan transfer.

At twelve points the direct transfer has four physicalizing steps.  Their
dependency-chain partitions predict five four-dimensional associahedral
faces.  The script tests whether the rank-three saturation already covers
every three-dimensional facet, classifies any deficit, completes it with the
actual scalar associahedral facets, verifies exact signed three-sphere
closure, and checks one-step deck covariance.
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
    Triangulation,
    rotate_face_key,
    triangulation_key,
    zero_core_cells,
)
from check_core_incidence_rank_three import (
    canonical_surface_key,
    face_key,
    orient_surface,
    oriented_cycle_key,
    physical_degree,
    polygon_cycle,
    polarity_rank_three_audit,
    rank_three_face_index,
    rank_two_facets,
    raw_surface_key,
    rotate_surface,
    scale,
    state_with_increments,
)


RankFourKind = str
RankThreeKind = str


PARTITION_KIND = {
    (1, 1, 1, 1): "four_cube",
    (2, 1, 1): "pentagon_x_square",
    (2, 2): "pentagon_x_pentagon",
    (3, 1): "hexagon_associahedron_x_interval",
    (4,): "heptagon_associahedron",
}


EXPECTED = {
    "four_cube": {
        "vertices": 16,
        "facets": Counter({"cube": 8}),
    },
    "pentagon_x_square": {
        "vertices": 20,
        "facets": Counter(
            {"cube": 5, "pentagonal_prism": 4}
        ),
    },
    "pentagon_x_pentagon": {
        "vertices": 25,
        "facets": Counter({"pentagonal_prism": 10}),
    },
    "hexagon_associahedron_x_interval": {
        "vertices": 28,
        "facets": Counter(
            {
                "cube": 3,
                "pentagonal_prism": 6,
                "hexagon_associahedron": 2,
            }
        ),
    },
    "heptagon_associahedron": {
        "vertices": 42,
        "facets": Counter(
            {
                "pentagonal_prism": 7,
                "hexagon_associahedron": 7,
            }
        ),
    },
}


def rank_three_kind(vertex_count: int) -> RankThreeKind:
    """Rank-three face type from its associahedral vertex count."""

    return {
        8: "cube",
        10: "pentagonal_prism",
        14: "hexagon_associahedron",
    }[vertex_count]


def rank_four_face_index(
    multiplicity: int,
) -> dict[FaceKey, tuple[Triangulation, ...]]:
    """Index every codimension-four associahedral face."""

    index = defaultdict(list)
    for triangulation in triangulations(tuple(range(multiplicity))):
        for removed in combinations(triangulation, 4):
            common = frozenset(set(triangulation) - set(removed))
            index[common].append(triangulation)
    result = {
        common: tuple(sorted(set(vertices), key=triangulation_key))
        for common, vertices in index.items()
    }
    assert set(map(len, result.values())) <= {16, 20, 25, 28, 42}
    return result


def common_dissection(states: tuple[Triangulation, ...]) -> FaceKey:
    """Intersection of a nonempty state set."""

    assert states
    return frozenset.intersection(*states)


def direct_rank_four_occurrences(
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> Counter:
    """All marked rank-four dependency blocks."""

    records = Counter()
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
                remaining = tuple(
                    len(chain) - positions[index]
                    for index, chain in enumerate(chains)
                )
                increment_ranges = tuple(
                    range(count + 1) for count in remaining
                )
                for increments in product(*increment_ranges):
                    if sum(increments) != 4:
                        continue
                    partition = tuple(
                        sorted(
                            (
                                increment
                                for increment in increments
                                if increment
                            ),
                            reverse=True,
                        )
                    )
                    kind = PARTITION_KIND[partition]
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
                    common = common_dissection(states)
                    assert len(common) == multiplicity - 7
                    assert mark in common
                    records[(source, mark, common, kind)] += 1
    return records


def rank_three_facets(
    common: FaceKey,
    vertices: tuple[Triangulation, ...],
) -> dict[FaceKey, tuple[Triangulation, ...]]:
    """Every three-dimensional facet in one rank-four face."""

    extras = set().union(*vertices) - set(common)
    result = {}
    for diagonal in extras:
        facet_common = frozenset(set(common) | {diagonal})
        facet_vertices = tuple(
            vertex for vertex in vertices if diagonal in vertex
        )
        assert len(facet_vertices) in {8, 10, 14}
        result[facet_common] = facet_vertices
    return result


def canonical_surface(surface: dict[FaceKey, Counter]):
    """Choose one of the two orientations of a closed polygonal surface."""

    opposite = {
        facet: scale(cycle, -1)
        for facet, cycle in surface.items()
    }
    return (
        surface
        if raw_surface_key(surface) < raw_surface_key(opposite)
        else opposite
    )


def scalar_rank_three_surface(
    common: FaceKey,
    vertices: tuple[Triangulation, ...],
) -> dict[FaceKey, Counter]:
    """Complete signed boundary surface of an actual rank-three face."""

    facets = rank_two_facets(common, vertices)
    cycles = {
        facet: polygon_cycle(facet_vertices)
        for facet, facet_vertices in facets.items()
    }
    return canonical_surface(orient_surface(facets, cycles))


def surface_relation(
    first: dict[FaceKey, Counter],
    second: dict[FaceKey, Counter],
) -> int:
    """Whether two oriented copies of one surface agree or are opposite."""

    if raw_surface_key(first) == raw_surface_key(second):
        return 1
    if raw_surface_key(first) == raw_surface_key(
        {
            facet: scale(cycle, -1)
            for facet, cycle in second.items()
        }
    ):
        return -1
    raise AssertionError("rank-three facet surfaces do not agree up to sign")


def orient_hypersurface(
    facets: dict[FaceKey, tuple[Triangulation, ...]],
    surfaces: dict[FaceKey, dict[FaceKey, Counter]],
) -> dict[FaceKey, dict[FaceKey, Counter]]:
    """Orient rank-three facets so the total rank-two boundary vanishes."""

    incidence = defaultdict(list)
    for facet, surface in surfaces.items():
        assert facet in facets
        for ridge, cycle in surface.items():
            incidence[ridge].append((facet, cycle))
    assert incidence
    assert set(map(len, incidence.values())) == {2}

    first = min(facets, key=face_key)
    signs = {first: 1}
    pending = [first]
    while pending:
        facet = pending.pop()
        for ridge, cycle in surfaces[facet].items():
            entries = incidence[ridge]
            other, other_cycle = (
                entries[1]
                if entries[0][0] == facet
                else entries[0]
            )
            relation = surface_relation(
                {ridge: cycle},
                {ridge: other_cycle},
            )
            required = -signs[facet] * relation
            if other in signs:
                assert signs[other] == required
            else:
                signs[other] = required
                pending.append(other)

    assert set(signs) == set(facets)
    oriented = {
        facet: {
            ridge: scale(cycle, signs[facet])
            for ridge, cycle in surfaces[facet].items()
        }
        for facet in facets
    }

    for ridge, entries in incidence.items():
        first_facet, first_cycle = entries[0]
        second_facet, second_cycle = entries[1]
        signed_first = {
            ridge: scale(first_cycle, signs[first_facet])
        }
        signed_second = {
            ridge: scale(second_cycle, signs[second_facet])
        }
        assert surface_relation(signed_first, signed_second) == -1
    return oriented


def raw_hypersurface_key(
    hypersurface: dict[FaceKey, dict[FaceKey, Counter]],
):
    """Serializable oriented rank-four boundary."""

    return tuple(
        (face_key(facet), raw_surface_key(hypersurface[facet]))
        for facet in sorted(hypersurface, key=face_key)
    )


def canonical_hypersurface_key(
    hypersurface: dict[FaceKey, dict[FaceKey, Counter]],
):
    """Forget the one global orientation choice."""

    forward = raw_hypersurface_key(hypersurface)
    backward = raw_hypersurface_key(
        {
            facet: {
                ridge: scale(cycle, -1)
                for ridge, cycle in surface.items()
            }
            for facet, surface in hypersurface.items()
        }
    )
    return min(forward, backward)


def rotate_hypersurface(
    hypersurface: dict[FaceKey, dict[FaceKey, Counter]],
    multiplicity: int,
):
    """Push a complete rank-four boundary through one-step rotation."""

    return {
        rotate_face_key(facet, multiplicity): rotate_surface(
            surface, multiplicity
        )
        for facet, surface in hypersurface.items()
    }


def polarity_rank_four_audit(
    multiplicity: int,
    *,
    first_is_plus: bool,
    face_index: dict[FaceKey, tuple[Triangulation, ...]],
):
    """Coverage, saturation, and signed closure for one polarity."""

    rank_three_index = rank_three_face_index(multiplicity)
    inherited_audit = polarity_rank_three_audit(
        multiplicity,
        first_is_plus=first_is_plus,
        face_index=rank_three_index,
    )
    inherited = inherited_audit["surfaces"]
    occurrences = direct_rank_four_occurrences(
        multiplicity, first_is_plus=first_is_plus
    )

    occurrence_profiles = Counter()
    face_sets = defaultdict(set)
    coverage_profiles = Counter()
    missing_facet_profiles = Counter()
    missing_facet_ids = set()
    hypersurfaces = {}

    for (source, mark, common, kind), count in occurrences.items():
        assert source
        vertices = face_index[common]
        expected = EXPECTED[kind]
        assert len(vertices) == expected["vertices"]
        facets = rank_three_facets(common, vertices)
        profile = Counter(
            rank_three_kind(len(facet_vertices))
            for facet_vertices in facets.values()
        )
        assert profile == expected["facets"]

        covered = set()
        for facet, facet_vertices in facets.items():
            facet_kind = rank_three_kind(len(facet_vertices))
            if (mark, facet, facet_kind) in inherited:
                covered.add(facet)
        missing = set(facets) - covered

        coverage_profiles[
            (
                kind,
                *(profile_kind_count(facets, covered)),
                *(profile_kind_count(facets, missing)),
            )
        ] += count

        for facet in missing:
            extra = next(iter(set(facet) - set(common)))
            facet_kind = rank_three_kind(len(facets[facet]))
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
            missing_facet_ids.add((mark, facet, facet_kind))

        surfaces = {}
        for facet, facet_vertices in facets.items():
            facet_kind = rank_three_kind(len(facet_vertices))
            scalar_surface = scalar_rank_three_surface(
                facet, facet_vertices
            )
            inherited_key = (mark, facet, facet_kind)
            if inherited_key in inherited:
                assert canonical_surface_key(
                    inherited[inherited_key]
                ) == canonical_surface_key(scalar_surface)
            surfaces[facet] = scalar_surface

        hypersurface = orient_hypersurface(facets, surfaces)
        hypersurface_id = (mark, common, kind)
        if hypersurface_id in hypersurfaces:
            assert canonical_hypersurface_key(
                hypersurfaces[hypersurface_id]
            ) == canonical_hypersurface_key(hypersurface)
        else:
            hypersurfaces[hypersurface_id] = hypersurface

        occurrence_profiles[kind] += count
        face_sets[kind].add(common)

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
        "missing_facet_profiles": missing_facet_profiles,
        "missing_facet_ids": missing_facet_ids,
        "inherited_surface_count": len(inherited),
        "saturated_surface_count": len(
            set(inherited) | missing_facet_ids
        ),
        "completed_hypersurface_count": len(hypersurfaces),
        "hypersurfaces": hypersurfaces,
    }


def profile_kind_count(
    facets: dict[FaceKey, tuple[Triangulation, ...]],
    selected: set[FaceKey],
) -> tuple[int, int, int]:
    """Counts of cube, prism, and hexagon-associahedron facets."""

    profile = Counter(
        rank_three_kind(len(facets[facet]))
        for facet in selected
    )
    return (
        profile["cube"],
        profile["pentagonal_prism"],
        profile["hexagon_associahedron"],
    )


def multiplicity_audit(multiplicity: int):
    """Both polarity sheets and exact one-step deck covariance."""

    face_index = rank_four_face_index(multiplicity)
    plus = polarity_rank_four_audit(
        multiplicity,
        first_is_plus=True,
        face_index=face_index,
    )
    minus = polarity_rank_four_audit(
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

    rotated_missing = {
        (
            rotate_diagonal(mark, multiplicity),
            rotate_face_key(facet, multiplicity),
            kind,
        )
        for mark, facet, kind in plus["missing_facet_ids"]
    }
    assert rotated_missing == minus["missing_facet_ids"]

    for (mark, common, kind), hypersurface in plus[
        "hypersurfaces"
    ].items():
        target = (
            rotate_diagonal(mark, multiplicity),
            rotate_face_key(common, multiplicity),
            kind,
        )
        assert canonical_hypersurface_key(
            rotate_hypersurface(hypersurface, multiplicity)
        ) == canonical_hypersurface_key(
            minus["hypersurfaces"][target]
        )

    for key in (
        "occurrence_profiles",
        "face_counts",
        "coverage_profiles",
        "missing_facet_profiles",
        "inherited_surface_count",
        "saturated_surface_count",
        "completed_hypersurface_count",
    ):
        assert plus[key] == minus[key]
    return plus


def main() -> None:
    multiplicity = 12
    result = multiplicity_audit(multiplicity)
    print(
        f"n={multiplicity} rank-four occurrences: "
        f"{dict(result['occurrence_profiles'])}"
    )
    print(
        f"n={multiplicity} distinct rank-four faces: "
        f"{dict(result['face_counts'])}"
    )
    print(
        "rank-four facet coverage profiles "
        "(kind, covered cubes, covered prisms, covered K3, "
        "missing cubes, missing prisms, missing K3): "
        f"{dict(result['coverage_profiles'])}"
    )
    print(
        f"rank-four missing facet profiles: "
        f"{dict(result['missing_facet_profiles'])}"
    )
    print(
        f"distinct marked missing rank-three facets: "
        f"{len(result['missing_facet_ids'])}"
    )
    print(
        "marked rank-three carrier saturation: "
        f"{result['inherited_surface_count']} -> "
        f"{result['saturated_surface_count']}; "
        f"{result['completed_hypersurface_count']} completed "
        "rank-four hypersurfaces"
    )
    print(
        "exact signed, deck-covariant rank-four obstruction and "
        "associahedral-saturation audit passed"
    )


if __name__ == "__main__":
    main()
