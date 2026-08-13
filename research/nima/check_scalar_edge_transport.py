"""Scalar-only derivation of the eight-point marked QTDS edge transport.

The preceding coefficient audit reconstructed the QTDS contact endpoints and
then matched scalar zero-core cells to those endpoints.  This audit removes
that circular input.

The alternating coloring coorients each physical diagonal.  Those
coorientations direct the dual tree of a quadrangulation.  If the directed
tree has a unique sink, the two scalar diagonals of the sink quadrilateral
are its contact slots.  Conservation of the twenty marked zero-core
occurrences selects exactly two opposite coorientation patterns among all
2^8 possibilities: the two alternating polarities.

The scalar flip metric then gives a unique minimum assignment from marked
zero-core cells to those independently constructed slots.  Pairing the two
polarities produces length-two paths in the quadrangulation flip graph.  The
four diameter marks have two routes around their scalar-labelled squares;
averaging the two routes is the unique cyclic-equivariant transport over Q.

Only after this construction is complete are its endpoints compared with the
QTDS numerator calculation.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

from check_j_reconstruction import triangulations
from check_qtds_descent import (
    canonical_edge,
    matrix_rank,
    quadrangulation_cellulation,
)
from check_eight_point_transfer import (
    negative_support,
    planar_symbolic_kinematics,
    qtds_diagrams,
    rotate_diagonal,
    scalar_grade_by_core,
    scalar_flip_graph,
    select_terms,
)
from check_surface_rees_carrier import nullspace_basis


Diagonal = tuple[int, int]
Quadrangulation = tuple[Diagonal, Diagonal]
Triangulation = frozenset[Diagonal]
Edge = tuple[Quadrangulation, Quadrangulation]
LinearCoefficient = dict[Diagonal, Fraction]
EdgeTransport = dict[Edge, LinearCoefficient]
ScalarEdge = tuple[Triangulation, Triangulation]
ScalarEdgeTransport = dict[ScalarEdge, LinearCoefficient]


def polygon_boundary_edges() -> set[Diagonal]:
    """Boundary edges of the labelled octagon."""

    return {
        tuple(sorted((vertex, (vertex + 1) % 8)))
        for vertex in range(8)
    }


def quadrangulation_cells(
    quadrangulation: Quadrangulation,
) -> tuple[tuple[int, int, int, int], ...]:
    """The three quadrilateral regions cut out by a quadrangulation."""

    edges = set(quadrangulation) | polygon_boundary_edges()
    cells = tuple(
        vertices
        for vertices in combinations(range(8), 4)
        if all(
            tuple(
                sorted(
                    (
                        vertices[index],
                        vertices[(index + 1) % 4],
                    )
                )
            )
            in edges
            for index in range(4)
        )
    )
    assert len(cells) == 3
    return cells


def cell_side(
    diagonal: Diagonal,
    cell: tuple[int, int, int, int],
) -> int:
    """Return 0 on the increasing-arc side and 1 on its complement."""

    first, second = diagonal
    increasing_arc = set(range(first + 1, second))
    other_vertices = set(cell) - set(diagonal)
    if other_vertices <= increasing_arc:
        return 0
    assert other_vertices.isdisjoint(increasing_arc)
    return 1


def alternating_coorientation(
    diagonal: Diagonal, *, first_is_plus: bool
) -> int:
    """Coorient an odd diagonal using the alternating endpoint coloring.

    In the chosen cyclic lift, even vertices carry the first polarity.  Point
    an odd diagonal transversely to the same side of its orientation from its
    even endpoint to its odd endpoint.  In canonical increasing-arc
    coordinates this is the outside side for an even first endpoint and the
    inside side for an odd first endpoint.  Reversing polarity reverses every
    coorientation.
    """

    first, second = diagonal
    assert (first - second) % 2
    plus_side = 1 if first % 2 == 0 else 0
    return plus_side if first_is_plus else 1 - plus_side


def sink_contact_slots(
    quadrangulation: Quadrangulation,
    coorientations: dict[Diagonal, int],
) -> frozenset[Diagonal]:
    """Return the two scalar diagonals of the unique dual-tree sink.

    Every physical diagonal separates two quadrilateral cells.  Direct the
    corresponding dual edge toward its cooriented side.  If the directed
    three-vertex tree has one sink, that cell supplies two marked contact
    slots.  If it has two sinks, it supplies none.
    """

    cells = quadrangulation_cells(quadrangulation)
    outdegree = {cell: 0 for cell in cells}
    for diagonal in quadrangulation:
        adjacent = tuple(
            cell for cell in cells if set(diagonal) <= set(cell)
        )
        assert len(adjacent) == 2
        target = next(
            cell
            for cell in adjacent
            if cell_side(diagonal, cell) == coorientations[diagonal]
        )
        source = next(cell for cell in adjacent if cell != target)
        outdegree[source] += 1

    sinks = tuple(cell for cell, degree in outdegree.items() if degree == 0)
    if len(sinks) != 1:
        assert len(sinks) == 2
        return frozenset()
    first, second, third, fourth = sinks[0]
    return frozenset(
        (
            tuple(sorted((first, third))),
            tuple(sorted((second, fourth))),
        )
    )


def scalar_contact_slots(
    quadrangulation: Quadrangulation, *, first_is_plus: bool
) -> frozenset[Diagonal]:
    """Contact slots constructed only from scalar polygon geometry."""

    physical = quadrangulation_cellulation()[0]
    coorientations = {
        diagonal: alternating_coorientation(
            diagonal, first_is_plus=first_is_plus
        )
        for diagonal in physical
    }
    return sink_contact_slots(quadrangulation, coorientations)


def rotate_quadrangulation(
    quadrangulation: Quadrangulation, amount: int = 1
) -> Quadrangulation:
    """Rotate a quadrangulation in the labelled octagon."""

    return tuple(
        sorted(
            rotate_diagonal(diagonal, amount)
            for diagonal in quadrangulation
        )
    )


def rotate_triangulation(
    triangulation: Triangulation, amount: int = 1
) -> Triangulation:
    """Rotate a scalar triangulation."""

    return frozenset(
        rotate_diagonal(diagonal, amount)
        for diagonal in triangulation
    )


def rotated_side(diagonal: Diagonal, side: int) -> int:
    """Transport a cooriented side through one-step cyclic rotation."""

    first, second = diagonal
    increasing_arc = set(range(first + 1, second))
    region = (
        increasing_arc
        if side == 0
        else set(range(8)) - increasing_arc - set(diagonal)
    )
    rotated_region = {(vertex + 1) % 8 for vertex in region}
    rotated_diagonal = rotate_diagonal(diagonal)
    rotated_first, rotated_second = rotated_diagonal
    rotated_increasing_arc = set(
        range(rotated_first + 1, rotated_second)
    )
    if rotated_region == rotated_increasing_arc:
        return 0
    assert (
        rotated_region
        == set(range(8))
        - rotated_increasing_arc
        - set(rotated_diagonal)
    )
    return 1


def coorientation_uniqueness_audit(
    zero_core_cells: tuple[Triangulation, ...],
) -> None:
    """Classify local dual-flow rules satisfying scalar contact conservation."""

    (
        physical,
        _,
        _,
        _,
        quadrangulations,
        _,
        _,
    ) = quadrangulation_cellulation()
    physical_index = {
        diagonal: index for index, diagonal in enumerate(physical)
    }
    source_multiplicity = Counter(
        diagonal
        for triangulation in zero_core_cells
        for diagonal in triangulation
    )

    conservative_patterns = []
    rotation_reversing_patterns = []
    for bits in range(1 << len(physical)):
        coorientations = {
            diagonal: (bits >> physical_index[diagonal]) & 1
            for diagonal in physical
        }
        target_multiplicity = Counter(
            diagonal
            for quadrangulation in quadrangulations
            for diagonal in sink_contact_slots(
                quadrangulation, coorientations
            )
        )
        if target_multiplicity == source_multiplicity:
            conservative_patterns.append(bits)

        rotation_reverses = all(
            (
                bits
                >> physical_index[rotate_diagonal(diagonal)]
            )
            & 1
            == 1 - rotated_side(
                diagonal, coorientations[diagonal]
            )
            for diagonal in physical
        )
        if rotation_reverses:
            rotation_reversing_patterns.append(bits)

    plus_pattern = sum(
        alternating_coorientation(
            diagonal, first_is_plus=True
        )
        << physical_index[diagonal]
        for diagonal in physical
    )
    minus_pattern = ((1 << len(physical)) - 1) ^ plus_pattern
    expected = {plus_pattern, minus_pattern}
    assert set(conservative_patterns) == expected
    assert set(rotation_reversing_patterns) == expected


def scalar_core_data():
    """Return scalar triangulations, cores, zero cells, fibers, and graph."""

    triangulation_list = triangulations(tuple(range(8)))
    cores = {
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
        if not cores[triangulation]
    )
    quadrangulations = quadrangulation_cellulation()[4]
    fibers = {
        quadrangulation: tuple(
            triangulation
            for triangulation in triangulation_list
            if cores[triangulation] == quadrangulation
        )
        for quadrangulation in quadrangulations
    }
    adjacency = scalar_flip_graph(triangulation_list)
    assert len(zero_core_cells) == 4
    return (
        triangulation_list,
        cores,
        zero_core_cells,
        fibers,
        adjacency,
    )


def scalar_distances(
    zero_core_cells: tuple[Triangulation, ...],
    adjacency,
) -> dict[Triangulation, dict[Triangulation, int]]:
    """All associahedral distances from the four zero-core sources."""

    result = {}
    for source in zero_core_cells:
        distances = {source: 0}
        queue = [source]
        for triangulation in queue:
            for neighbor in adjacency[triangulation]:
                if neighbor not in distances:
                    distances[neighbor] = distances[triangulation] + 1
                    queue.append(neighbor)
        result[source] = distances
    return result


def derived_marked_matching(
    *,
    first_is_plus: bool,
    zero_core_cells: tuple[Triangulation, ...],
    fibers: dict[Quadrangulation, tuple[Triangulation, ...]],
    distances: dict[Triangulation, dict[Triangulation, int]],
) -> frozenset[tuple[Triangulation, Diagonal, Quadrangulation]]:
    """Derive the marked assignment from scalar slots and flip distance."""

    quadrangulations = quadrangulation_cellulation()[4]
    sources_by_mark = defaultdict(list)
    for source in zero_core_cells:
        for mark in source:
            sources_by_mark[mark].append(source)

    targets_by_mark = defaultdict(list)
    for quadrangulation in quadrangulations:
        for mark in scalar_contact_slots(
            quadrangulation, first_is_plus=first_is_plus
        ):
            targets_by_mark[mark].append(quadrangulation)
    assert Counter(
        {
            mark: len(sources)
            for mark, sources in sources_by_mark.items()
        }
    ) == Counter(
        {
            mark: len(targets)
            for mark, targets in targets_by_mark.items()
        }
    )

    matching = set()
    for mark, sources in sources_by_mark.items():
        targets = targets_by_mark[mark]
        assert len(sources) == len(targets)

        def marked_distance(source, target):
            marked_fiber = tuple(
                triangulation
                for triangulation in fibers[target]
                if mark in triangulation
            )
            assert marked_fiber
            return min(
                distances[source][triangulation]
                for triangulation in marked_fiber
            )

        candidates = []
        for target_order in permutations(targets):
            score = sum(
                marked_distance(source, target)
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
            assert marked_distance(source, target) == 2
            matching.add((source, mark, target))

    assert len(matching) == 20
    return frozenset(matching)


def triangulation_key(triangulation: Triangulation):
    """Total ordering key for scalar triangulations."""

    return tuple(sorted(triangulation))


def canonical_scalar_edge(
    first: Triangulation, second: Triangulation
) -> ScalarEdge:
    """Canonical orientation of an associahedral flip edge."""

    return (
        (first, second)
        if triangulation_key(first) < triangulation_key(second)
        else (second, first)
    )


def marked_scalar_geodesics(
    source: Triangulation,
    mark: Diagonal,
    target: Quadrangulation,
    fibers: dict[Quadrangulation, tuple[Triangulation, ...]],
    adjacency,
) -> tuple[tuple[Triangulation, ...], ...]:
    """All length-two scalar paths to the marked target fiber."""

    paths = tuple(
        sorted(
            (
                (source, middle, endpoint)
                for middle in adjacency[source]
                for endpoint in adjacency[middle]
                if endpoint in fibers[target] and mark in endpoint
            ),
            key=lambda path: tuple(
                triangulation_key(vertex) for vertex in path
            ),
        )
    )
    assert len(paths) in (1, 2)
    assert len({path[-1] for path in paths}) == 1
    return paths


def add_oriented_scalar_edge(
    transport,
    first: Triangulation,
    second: Triangulation,
    mark: Diagonal,
    coefficient: Fraction,
) -> None:
    """Add a marked coefficient to a scalar flip edge."""

    edge = canonical_scalar_edge(first, second)
    orientation = 1 if edge == (first, second) else -1
    transport[edge][mark] += orientation * coefficient


def scalar_associahedral_transport(matchings, fibers, adjacency):
    """Lift the contact transport to actual scalar associahedron edges.

    For each source mark, average its commuting length-two paths to the plus
    endpoint and subtract the corresponding average to the minus endpoint.
    This gives a genuine scalar cellular one-chain before core forgetting.
    """

    plus = {
        (source, mark): target
        for source, mark, target in matchings[True]
    }
    minus = {
        (source, mark): target
        for source, mark, target in matchings[False]
    }
    assert plus.keys() == minus.keys()
    transport = defaultdict(lambda: defaultdict(Fraction))
    endpoints = {}
    path_counts = Counter()
    for key in plus:
        source, mark = key
        plus_paths = marked_scalar_geodesics(
            source, mark, plus[key], fibers, adjacency
        )
        minus_paths = marked_scalar_geodesics(
            source, mark, minus[key], fibers, adjacency
        )
        endpoints[key] = (minus_paths[0][-1], plus_paths[0][-1])
        path_counts[(len(minus_paths), len(plus_paths))] += 1

        # -X_d times (plus path - minus path).
        for paths, sign in ((plus_paths, -1), (minus_paths, 1)):
            coefficient = Fraction(sign, len(paths))
            for path in paths:
                for first, second in zip(path, path[1:]):
                    add_oriented_scalar_edge(
                        transport,
                        first,
                        second,
                        mark,
                        coefficient,
                    )
    cleaned = {
        edge: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for edge, values in transport.items()
        if any(values.values())
    }
    return cleaned, endpoints, path_counts


def scalar_transport_boundary(transport: ScalarEdgeTransport):
    """Boundary of an actual scalar-associahedral edge chain."""

    boundary = defaultdict(lambda: defaultdict(Fraction))
    for (first, second), values in transport.items():
        for mark, coefficient in values.items():
            boundary[first][mark] -= coefficient
            boundary[second][mark] += coefficient
    return {
        vertex: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for vertex, values in boundary.items()
        if any(values.values())
    }


def rotate_scalar_transport(
    transport: ScalarEdgeTransport,
) -> ScalarEdgeTransport:
    """One-step rotation of a marked scalar cellular chain."""

    result = defaultdict(lambda: defaultdict(Fraction))
    for (first, second), values in transport.items():
        rotated_first = rotate_triangulation(first)
        rotated_second = rotate_triangulation(second)
        rotated_edge = canonical_scalar_edge(
            rotated_first, rotated_second
        )
        orientation = (
            1
            if rotated_edge == (rotated_first, rotated_second)
            else -1
        )
        for mark, coefficient in values.items():
            result[rotated_edge][rotate_diagonal(mark)] += (
                orientation * coefficient
            )
    return {
        edge: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for edge, values in result.items()
        if any(values.values())
    }


def qt_ds_contact_occurrences(
    *, first_is_plus: bool
) -> frozenset[tuple[Quadrangulation, Diagonal]]:
    """Extract actual QTDS contacts only after the scalar construction."""

    diagonals, variables, kinematics = planar_symbolic_kinematics()
    scalar_groups, _ = scalar_grade_by_core(variables)
    full_core = {
        core: value
        for core, value in scalar_groups.items()
        if len(core) == 2
    }
    diagrams = qtds_diagrams(
        kinematics,
        variables,
        first_is_plus=first_is_plus,
    )
    result = set()
    for quadrangulation, diagram in diagrams.items():
        remainder = diagram - full_core[quadrangulation]
        polynomial = select_terms(
            remainder,
            lambda powers: not negative_support(powers),
        )
        for powers, coefficient in polynomial.terms.items():
            support = tuple(
                index
                for index, exponent in enumerate(powers)
                if exponent
            )
            assert len(support) == 1
            assert coefficient == -1
            result.add((quadrangulation, diagonals[support[0]]))
    assert len(result) == 20
    return frozenset(result)


def quadrangulation_adjacency():
    """Adjacency in the twelve-vertex quadrangulation flip graph."""

    quadrangulations = quadrangulation_cellulation()[4]
    flips = quadrangulation_cellulation()[5]
    adjacency = {quadrangulation: set() for quadrangulation in quadrangulations}
    for first, second in flips:
        adjacency[first].add(second)
        adjacency[second].add(first)
    return adjacency


def shortest_quadrangulation_paths(
    first: Quadrangulation,
    second: Quadrangulation,
    adjacency,
) -> tuple[tuple[Quadrangulation, ...], ...]:
    """All geodesics between two quadrangulations."""

    distances = {first: 0}
    queue = [first]
    for vertex in queue:
        for neighbor in adjacency[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    paths = []

    def visit(vertex, path):
        if vertex == second:
            paths.append(tuple(path))
            return
        for neighbor in adjacency[vertex]:
            if (
                distances.get(neighbor) == distances[vertex] + 1
                and distances[neighbor] <= distances[second]
            ):
                visit(neighbor, path + [neighbor])

    visit(first, [first])
    return tuple(sorted(paths))


def add_oriented_edge(
    transport,
    first: Quadrangulation,
    second: Quadrangulation,
    mark: Diagonal,
    coefficient: Fraction,
) -> None:
    """Add a marked coefficient to an oriented canonical edge."""

    edge = canonical_edge(first, second)
    orientation = 1 if edge == (first, second) else -1
    transport[edge][mark] += orientation * coefficient


def edge_transport(
    matchings,
    *,
    route_choices: tuple[int, ...] | None = None,
) -> tuple[EdgeTransport, tuple]:
    """Transport minus slots to plus slots along scalar-selected geodesics.

    A marked contact has coefficient -X_d.  The canonical rational transport
    averages the two routes across each diameter square.  Supplying four
    route choices instead constructs one of the sixteen integral routings.
    """

    adjacency = quadrangulation_adjacency()
    plus = {
        (source, mark): quadrangulation
        for source, mark, quadrangulation in matchings[True]
    }
    minus = {
        (source, mark): quadrangulation
        for source, mark, quadrangulation in matchings[False]
    }
    assert plus.keys() == minus.keys()

    transport = defaultdict(lambda: defaultdict(Fraction))
    records = []
    ambiguous_index = 0
    for key in sorted(
        plus,
        key=lambda item: (
            tuple(sorted(item[0])),
            item[1],
        ),
    ):
        paths = shortest_quadrangulation_paths(
            minus[key], plus[key], adjacency
        )
        assert len(paths) in (1, 2)
        assert all(len(path) == 3 for path in paths)
        if len(paths) == 2 and route_choices is not None:
            selected_paths = (paths[route_choices[ambiguous_index]],)
            ambiguous_index += 1
        else:
            selected_paths = paths
        weight = Fraction(-1, len(selected_paths))
        for path in selected_paths:
            for first, second in zip(path, path[1:]):
                add_oriented_edge(
                    transport,
                    first,
                    second,
                    key[1],
                    weight,
                )
        records.append((key, paths))

    if route_choices is not None:
        assert ambiguous_index == 4
    cleaned = {
        edge: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for edge, values in transport.items()
    }
    return cleaned, tuple(records)


def transport_boundary(transport: EdgeTransport):
    """Ordinary cellular boundary of the marked edge transport."""

    vertices = quadrangulation_cellulation()[4]
    boundary = {
        vertex: defaultdict(Fraction) for vertex in vertices
    }
    for (first, second), values in transport.items():
        for mark, coefficient in values.items():
            boundary[first][mark] -= coefficient
            boundary[second][mark] += coefficient
    return {
        vertex: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for vertex, values in boundary.items()
    }


def expected_contact_boundary():
    """Scalar-derived plus-minus contact difference at each vertex."""

    vertices = quadrangulation_cellulation()[4]
    result = {}
    for vertex in vertices:
        coefficients = defaultdict(Fraction)
        for mark in scalar_contact_slots(vertex, first_is_plus=True):
            coefficients[mark] -= 1
        for mark in scalar_contact_slots(vertex, first_is_plus=False):
            coefficients[mark] += 1
        result[vertex] = {
            mark: coefficient
            for mark, coefficient in coefficients.items()
            if coefficient
        }
    return result


def rotate_transport(transport: EdgeTransport) -> EdgeTransport:
    """Rotate labels once, including edge orientation and marked variable."""

    result = defaultdict(lambda: defaultdict(Fraction))
    for (first, second), values in transport.items():
        rotated_first = rotate_quadrangulation(first)
        rotated_second = rotate_quadrangulation(second)
        rotated_edge = canonical_edge(rotated_first, rotated_second)
        orientation = (
            1
            if rotated_edge == (rotated_first, rotated_second)
            else -1
        )
        for mark, coefficient in values.items():
            result[rotated_edge][rotate_diagonal(mark)] += (
                orientation * coefficient
            )
    return {
        edge: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for edge, values in result.items()
    }


def negate_transport(transport: EdgeTransport) -> EdgeTransport:
    """Negate all edge coefficients."""

    return {
        edge: {
            mark: -coefficient
            for mark, coefficient in values.items()
        }
        for edge, values in transport.items()
    }


def face_circulation(
    transport: EdgeTransport,
    face: tuple[Quadrangulation, ...],
) -> LinearCoefficient:
    """Ordinary oriented circulation of an edge coefficient around a face."""

    result = defaultdict(Fraction)
    for first, second in zip(face, face[1:] + face[:1]):
        edge = canonical_edge(first, second)
        orientation = 1 if edge == (first, second) else -1
        for mark, coefficient in transport.get(edge, {}).items():
            result[mark] += orientation * coefficient
    return {
        mark: coefficient
        for mark, coefficient in result.items()
        if coefficient
    }


def orientation_voltage():
    """A representative of the unique nontrivial RP2 sign local system."""

    (
        _,
        _,
        _,
        _,
        vertices,
        edges,
        faces,
    ) = quadrangulation_cellulation()
    vertex_index = {
        vertex: index for index, vertex in enumerate(vertices)
    }
    edge_index = {edge: index for index, edge in enumerate(edges)}
    boundary_one = [[0 for _ in edges] for _ in vertices]
    for column, (first, second) in enumerate(edges):
        boundary_one[vertex_index[first]][column] = -1
        boundary_one[vertex_index[second]][column] = 1
    boundary_two = [[0 for _ in faces] for _ in edges]
    for column, face in enumerate(faces):
        for index, first in enumerate(face):
            second = face[(index + 1) % len(face)]
            edge = canonical_edge(first, second)
            boundary_two[edge_index[edge]][column] += (
                1 if edge == (first, second) else -1
            )
    equations = [
        [
            boundary_two[edge][face]
            for edge in range(len(edges))
        ]
        for face in range(len(faces))
    ]
    coboundary_rank = matrix_rank(boundary_one, 2)
    voltage = next(
        candidate
        for candidate in nullspace_basis(equations, 2)
        if matrix_rank(
            boundary_one + [list(candidate)], 2
        )
        == coboundary_rank + 1
    )
    return {
        edge: voltage[index]
        for index, edge in enumerate(edges)
    }


def twisted_face_circulation(
    transport: EdgeTransport,
    face: tuple[Quadrangulation, ...],
    voltage: dict[Edge, int],
) -> LinearCoefficient:
    """Circulation in local frames for the nontrivial sign system."""

    result = defaultdict(Fraction)
    prefix_voltage = 0
    for first, second in zip(face, face[1:] + face[:1]):
        edge = canonical_edge(first, second)
        edge_voltage = voltage[edge]
        prefix_transport = -1 if prefix_voltage else 1
        edge_transport = -1 if edge_voltage else 1
        coefficient = (
            prefix_transport
            if edge == (first, second)
            else -prefix_transport * edge_transport
        )
        for mark, value in transport.get(edge, {}).items():
            result[mark] += coefficient * value
        prefix_voltage ^= edge_voltage
    assert prefix_voltage == 0
    return {
        mark: coefficient
        for mark, coefficient in result.items()
        if coefficient
    }


def route_torsor_audit(records) -> None:
    """Show that cyclic covariance forces the half-sum of square routes."""

    ambiguous = {
        key: paths for key, paths in records if len(paths) == 2
    }
    assert len(ambiguous) == 4
    assert {
        mark for (_, mark) in ambiguous
    } == {(0, 4), (1, 5), (2, 6), (3, 7)}

    # Rotation exchanges polarity, so rotate a minus-to-plus path and reverse
    # it before comparing it with the next minus-to-plus path.
    swaps = {}
    for key, paths in ambiguous.items():
        rotated_key = (
            rotate_triangulation(key[0]),
            rotate_diagonal(key[1]),
        )
        rotated_paths = ambiguous[rotated_key]
        image = tuple(
            reversed(
                tuple(
                    rotate_quadrangulation(vertex)
                    for vertex in paths[0]
                )
            )
        )
        image_index = rotated_paths.index(image)
        swaps[key] = image_index == 1

    start = next(
        key for key in ambiguous if key[1] == (0, 4)
    )
    key = start
    total_swap = False
    for _ in range(4):
        total_swap ^= swaps[key]
        key = (
            rotate_triangulation(key[0]),
            rotate_diagonal(key[1]),
        )
    assert key == start
    assert total_swap

    # An affine route weight lambda transforms as lambda or 1-lambda.
    # Odd monodromy forces lambda=1/2, and then every square has weight 1/2.
    weight = Fraction(1, 2)
    key = start
    for _ in range(4):
        weight = 1 - weight if swaps[key] else weight
        assert weight == Fraction(1, 2)
        key = (
            rotate_triangulation(key[0]),
            rotate_diagonal(key[1]),
        )


def main() -> None:
    (
        _,
        _,
        zero_core_cells,
        fibers,
        scalar_adjacency,
    ) = scalar_core_data()
    coorientation_uniqueness_audit(zero_core_cells)
    distances = scalar_distances(zero_core_cells, scalar_adjacency)
    matchings = {
        polarity: derived_marked_matching(
            first_is_plus=polarity,
            zero_core_cells=zero_core_cells,
            fibers=fibers,
            distances=distances,
        )
        for polarity in (True, False)
    }

    # Rotation exchanges the scalar-derived endpoints before any QTDS check.
    rotated_plus = frozenset(
        (
            rotate_triangulation(source),
            rotate_diagonal(mark),
            rotate_quadrangulation(target),
        )
        for source, mark, target in matchings[True]
    )
    assert rotated_plus == matchings[False]

    # Independent target verification, deliberately after the construction.
    for polarity in (True, False):
        derived_occurrences = frozenset(
            (target, mark)
            for _, mark, target in matchings[polarity]
        )
        assert derived_occurrences == qt_ds_contact_occurrences(
            first_is_plus=polarity
        )

    # A genuine one-chain in the scalar associahedron exists before core
    # forgetting.  Its endpoints are unique marked full-core refinements;
    # only the order of two commuting flips can be ambiguous.
    scalar_transport, scalar_endpoints, scalar_path_counts = (
        scalar_associahedral_transport(
            matchings, fibers, scalar_adjacency
        )
    )
    expected_scalar_boundary = defaultdict(
        lambda: defaultdict(Fraction)
    )
    plus_targets = {
        (source, mark): target
        for source, mark, target in matchings[True]
    }
    minus_targets = {
        (source, mark): target
        for source, mark, target in matchings[False]
    }
    for key, (minus_endpoint, plus_endpoint) in scalar_endpoints.items():
        source, mark = key
        expected_scalar_boundary[minus_endpoint][mark] += 1
        expected_scalar_boundary[plus_endpoint][mark] -= 1
        assert mark in minus_endpoint and mark in plus_endpoint
        assert tuple(
            sorted(
                diagonal
                for diagonal in minus_endpoint
                if (diagonal[0] - diagonal[1]) % 2
            )
        ) == minus_targets[(source, mark)]
        assert tuple(
            sorted(
                diagonal
                for diagonal in plus_endpoint
                if (diagonal[0] - diagonal[1]) % 2
            )
        ) == plus_targets[(source, mark)]
    expected_scalar_boundary = {
        vertex: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for vertex, values in expected_scalar_boundary.items()
        if any(values.values())
    }
    assert scalar_transport_boundary(
        scalar_transport
    ) == expected_scalar_boundary
    assert rotate_scalar_transport(
        scalar_transport
    ) == negate_transport(scalar_transport)
    assert sum(scalar_path_counts.values()) == 20

    transport, records = edge_transport(matchings)
    assert transport_boundary(transport) == expected_contact_boundary()
    assert rotate_transport(transport) == negate_transport(transport)
    assert sum(len(paths) == 1 for _, paths in records) == 16
    assert sum(len(paths) == 2 for _, paths in records) == 4
    route_torsor_audit(records)

    faces = quadrangulation_cellulation()[6]
    octagon = faces[-1]
    octagon_edges = {
        canonical_edge(first, second)
        for first, second in zip(
            octagon, octagon[1:] + octagon[:1]
        )
    }
    assert set(transport).isdisjoint(octagon_edges)
    assert face_circulation(transport, octagon) == {}
    voltage = orientation_voltage()
    assert twisted_face_circulation(
        transport, octagon, voltage
    ) == {}

    # Every integral square-route choice has zero ordinary octagonal
    # curvature, but none is cyclic/deck odd.  The rational half-sum is the
    # unique equivariant descent of this two-route torsor.
    for route_choices in product((0, 1), repeat=4):
        integral_transport, _ = edge_transport(
            matchings, route_choices=route_choices
        )
        assert set(integral_transport).isdisjoint(octagon_edges)
        assert face_circulation(integral_transport, octagon) == {}
        assert (
            rotate_transport(integral_transport)
            != negate_transport(integral_transport)
        )

    print(
        "n=8 scalar coorientation: contact conservation and one-step "
        "rotation select exactly the two alternating dual-tree flows"
    )
    print(
        "n=8 scalar matching: 20 marked zero-core occurrences map uniquely "
        "at distance two to scalar-derived sink slots for each polarity"
    )
    print(
        "n=8 local transport: 16 unique geodesics and 4 square route "
        "torsors give the exact contact boundary; the half-sum is deck odd"
    )
    print(
        "n=8 scalar lift: commuting two-flip paths give an exact deck-odd "
        "one-chain in the octagon associahedron before core forgetting"
    )
    print(
        "n=8 octagon: ordinary and orientation-twisted contact circulation "
        "vanish exactly; no integral absolute route choice is cyclic"
    )
    print("all exact scalar edge-transport checks passed")


if __name__ == "__main__":
    main()
