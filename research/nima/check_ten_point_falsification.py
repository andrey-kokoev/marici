"""Exact ten-point falsification of the scalar coorientation rule.

The eight-point construction is frozen here without a ten-point repair:

* odd (physical) diagonals receive the same alternating coorientation;
* the directed dual tree of a quadrangulation contributes the two diagonals
  of its unique sink quadrilateral;
* marked zero-core scalar triangulations are assigned to those slots by the
  same marked associahedral distance functional;
* only after that scalar construction are the endpoints compared with the
  independent QTDS numerator recursion.

The audit uses exact standard-library arithmetic throughout.  Its diagnostic
prints deliberately expose the finite counts that would falsify the rule.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations

from check_eight_point_transfer import (
    negative_support,
    planar_symbolic_kinematics,
    scalar_flip_graph,
    select_terms,
)
from check_j_reconstruction import canonical_channel, triangulations
from check_qtds_lift import qtds_raw_terms


MULTIPLICITY = 10

Diagonal = tuple[int, int]
Triangulation = frozenset[Diagonal]
Quadrangulation = tuple[Diagonal, ...]
Cell = tuple[int, int, int, int]


def rotate_diagonal(diagonal: Diagonal, amount: int = 1) -> Diagonal:
    """Rotate an unoriented decagon diagonal."""

    return tuple(
        sorted(
            (
                (diagonal[0] + amount) % MULTIPLICITY,
                (diagonal[1] + amount) % MULTIPLICITY,
            )
        )
    )


def rotate_triangulation(
    triangulation: Triangulation, amount: int = 1
) -> Triangulation:
    """Rotate a scalar triangulation in the labelled decagon."""

    return frozenset(
        rotate_diagonal(diagonal, amount) for diagonal in triangulation
    )


def rotate_quadrangulation(
    quadrangulation: Quadrangulation, amount: int = 1
) -> Quadrangulation:
    """Rotate a decagon quadrangulation."""

    return tuple(
        sorted(
            rotate_diagonal(diagonal, amount)
            for diagonal in quadrangulation
        )
    )


def boundary_edges() -> frozenset[Diagonal]:
    """Boundary edges of the labelled decagon."""

    return frozenset(
        tuple(sorted((vertex, (vertex + 1) % MULTIPLICITY)))
        for vertex in range(MULTIPLICITY)
    )


def physical_diagonals() -> tuple[Diagonal, ...]:
    """Diagonals splitting the decagon into two even polygons."""

    boundary = boundary_edges()
    result = tuple(
        diagonal
        for diagonal in combinations(range(MULTIPLICITY), 2)
        if diagonal not in boundary and (diagonal[0] - diagonal[1]) % 2
    )
    assert len(result) == 15
    return result


def diagonals_cross(first: Diagonal, second: Diagonal) -> bool:
    """Whether two decagon diagonals cross in the open polygon."""

    first_start, first_end = first
    second_start, second_end = second
    return (
        first_start < second_start < first_end < second_end
        or second_start < first_start < second_end < first_end
    )


@lru_cache(None)
def quadrangulations() -> tuple[Quadrangulation, ...]:
    """All 55 noncrossing three-diagonal decagon quadrangulations."""

    result = tuple(
        candidate
        for candidate in combinations(physical_diagonals(), 3)
        if all(
            not diagonals_cross(first, second)
            for first, second in combinations(candidate, 2)
        )
    )
    assert len(result) == 55
    return result


@lru_cache(None)
def quadrangulation_cells(
    quadrangulation: Quadrangulation,
) -> tuple[Cell, ...]:
    """The four quadrilateral regions cut out by a quadrangulation."""

    edges = set(quadrangulation) | set(boundary_edges())
    result = tuple(
        vertices
        for vertices in combinations(range(MULTIPLICITY), 4)
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
    assert len(result) == 4
    return result


def cell_side(diagonal: Diagonal, cell: Cell) -> int:
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
    """The unchanged alternating endpoint-coloring coorientation."""

    first, second = diagonal
    assert (first - second) % 2
    plus_side = 1 if first % 2 == 0 else 0
    return plus_side if first_is_plus else 1 - plus_side


def cell_contact_slots(cell: Cell) -> frozenset[Diagonal]:
    """The two scalar diagonals of a quadrilateral cell."""

    first, second, third, fourth = cell
    return frozenset(
        (
            tuple(sorted((first, third))),
            tuple(sorted((second, fourth))),
        )
    )


def directed_dual_tree(
    quadrangulation: Quadrangulation,
    coorientations: dict[Diagonal, int],
) -> tuple[tuple[Cell, Cell, Diagonal], ...]:
    """Direct each dual edge toward its cooriented polygonal side."""

    cells = quadrangulation_cells(quadrangulation)
    result = []
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
        result.append((source, target, diagonal))
    return tuple(result)


def sink_cells(
    quadrangulation: Quadrangulation,
    coorientations: dict[Diagonal, int],
) -> tuple[Cell, ...]:
    """All sinks of the cooriented quadrangulation dual tree."""

    cells = quadrangulation_cells(quadrangulation)
    outdegree = Counter(
        source
        for source, _, _ in directed_dual_tree(
            quadrangulation, coorientations
        )
    )
    return tuple(cell for cell in cells if not outdegree[cell])


def sink_contact_slots(
    quadrangulation: Quadrangulation,
    coorientations: dict[Diagonal, int],
) -> frozenset[Diagonal]:
    """Return the unique sink's two slots, or no slots if nonunique."""

    sinks = sink_cells(quadrangulation, coorientations)
    return cell_contact_slots(sinks[0]) if len(sinks) == 1 else frozenset()


def scalar_contact_slots(
    quadrangulation: Quadrangulation, *, first_is_plus: bool
) -> frozenset[Diagonal]:
    """Contact slots from scalar coorientation alone."""

    coorientations = {
        diagonal: alternating_coorientation(
            diagonal, first_is_plus=first_is_plus
        )
        for diagonal in physical_diagonals()
    }
    return sink_contact_slots(quadrangulation, coorientations)


def rotated_side(diagonal: Diagonal, side: int) -> int:
    """Transport a cooriented side through one cyclic rotation."""

    first, second = diagonal
    increasing_arc = set(range(first + 1, second))
    region = (
        increasing_arc
        if side == 0
        else set(range(MULTIPLICITY))
        - increasing_arc
        - set(diagonal)
    )
    rotated_region = {
        (vertex + 1) % MULTIPLICITY for vertex in region
    }
    rotated = rotate_diagonal(diagonal)
    rotated_first, rotated_second = rotated
    rotated_increasing_arc = set(
        range(rotated_first + 1, rotated_second)
    )
    if rotated_region == rotated_increasing_arc:
        return 0
    assert (
        rotated_region
        == set(range(MULTIPLICITY))
        - rotated_increasing_arc
        - set(rotated)
    )
    return 1


def scalar_core_data():
    """Scalar triangulations, zero cells, full fibers, and flip graph."""

    triangulation_list = triangulations(tuple(range(MULTIPLICITY)))
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
    fibers = {
        quadrangulation: tuple(
            triangulation
            for triangulation in triangulation_list
            if cores[triangulation] == quadrangulation
        )
        for quadrangulation in quadrangulations()
    }
    assert len(triangulation_list) == 1430
    assert len(zero_core_cells) == 10
    assert set(map(len, fibers.values())) == {16}
    adjacency = scalar_flip_graph(triangulation_list)
    return triangulation_list, zero_core_cells, fibers, adjacency


def coorientation_uniqueness_audit(
    zero_core_cells: tuple[Triangulation, ...],
) -> tuple[int, int, int]:
    """Enumerate all 2^15 local flows before selecting the alternating pair."""

    physical = physical_diagonals()
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
            for quadrangulation in quadrangulations()
            for diagonal in sink_contact_slots(
                quadrangulation, coorientations
            )
        )
        if target_multiplicity == source_multiplicity:
            conservative_patterns.append(bits)

        if all(
            (
                bits
                >> physical_index[rotate_diagonal(diagonal)]
            )
            & 1
            == 1 - rotated_side(
                diagonal, coorientations[diagonal]
            )
            for diagonal in physical
        ):
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
    # Unlike the octagon, the decagon's physical diagonals have two cyclic
    # orbits: ten short diagonals and five diameters.  Rotation reversal leaves
    # one independent polarity choice on each orbit and hence four patterns.
    # Contact conservation is the extra scalar condition correlating the two
    # choices and selecting the alternating pair.
    rotation_reversing = set(rotation_reversing_patterns)
    assert len(rotation_reversing) == 4
    assert expected <= rotation_reversing
    joint = set(conservative_patterns) & rotation_reversing
    assert joint == expected
    return (
        len(conservative_patterns),
        len(rotation_reversing_patterns),
        len(joint),
    )


def scalar_distances(zero_core_cells, adjacency):
    """All associahedral distances from the ten zero-core sources."""

    result = {}
    for source in zero_core_cells:
        distances = {source: 0}
        queue = deque((source,))
        while queue:
            triangulation = queue.popleft()
            for neighbor in adjacency[triangulation]:
                if neighbor not in distances:
                    distances[neighbor] = distances[triangulation] + 1
                    queue.append(neighbor)
        assert len(distances) == 1430
        result[source] = distances
    return result


def derived_marked_matching(
    *,
    first_is_plus: bool,
    zero_core_cells,
    fibers,
    distances,
):
    """Minimize the unchanged marked scalar flip-distance functional."""

    sources_by_mark = defaultdict(list)
    for source in zero_core_cells:
        for mark in source:
            sources_by_mark[mark].append(source)
    targets_by_mark = defaultdict(list)
    for quadrangulation in quadrangulations():
        for mark in scalar_contact_slots(
            quadrangulation, first_is_plus=first_is_plus
        ):
            targets_by_mark[mark].append(quadrangulation)
    assert {
        mark: len(values) for mark, values in sources_by_mark.items()
    } == {
        mark: len(values) for mark, values in targets_by_mark.items()
    }

    marked_distance_cache = {}

    def marked_distance(source, mark, target):
        key = (source, mark, target)
        if key not in marked_distance_cache:
            endpoints = tuple(
                triangulation
                for triangulation in fibers[target]
                if mark in triangulation
            )
            assert endpoints
            marked_distance_cache[key] = min(
                distances[source][endpoint] for endpoint in endpoints
            )
        return marked_distance_cache[key]

    matching = set()
    minimizer_counts = Counter()
    transfer_distances = Counter()
    for mark, sources in sources_by_mark.items():
        sources = tuple(sorted(sources, key=lambda value: tuple(sorted(value))))
        targets = tuple(sorted(targets_by_mark[mark]))
        candidates = []
        for target_order in permutations(targets):
            score = sum(
                marked_distance(source, mark, target)
                for source, target in zip(
                    sources, target_order, strict=True
                )
            )
            candidates.append((score, target_order))
        minimum = min(score for score, _ in candidates)
        minimizers = tuple(
            target_order
            for score, target_order in candidates
            if score == minimum
        )
        minimizer_counts[len(minimizers)] += 1
        assert len(minimizers) == 1
        for source, target in zip(
            sources, minimizers[0], strict=True
        ):
            distance = marked_distance(source, mark, target)
            transfer_distances[distance] += 1
            matching.add((source, mark, target))
    assert len(matching) == 70
    assert transfer_distances == {3: 70}
    return frozenset(matching), minimizer_counts, transfer_distances


def marked_geodesics(source, mark, target, fibers, adjacency, distances):
    """All shortest paths to the uniquely closest marked full-core lift."""

    distance = min(
        distances[source][endpoint]
        for endpoint in fibers[target]
        if mark in endpoint
    )
    endpoints = tuple(
        endpoint
        for endpoint in fibers[target]
        if mark in endpoint and distances[source][endpoint] == distance
    )
    assert len(endpoints) == 1
    endpoint = endpoints[0]
    paths = []

    def visit(vertex, path):
        if len(path) == distance + 1:
            if vertex == endpoint:
                paths.append(tuple(path))
            return
        for neighbor in adjacency[vertex]:
            if distances[source][neighbor] == distances[source][vertex] + 1:
                visit(neighbor, path + [neighbor])

    visit(source, [source])
    assert paths
    return endpoint, tuple(
        sorted(
            paths,
            key=lambda path: tuple(
                tuple(sorted(vertex)) for vertex in path
            ),
        )
    )


def route_square_graph(paths):
    """Connect geodesics differing by one commuting-flip square move."""

    adjacency = {path: set() for path in paths}
    for first, second in combinations(paths, 2):
        differences = tuple(
            index
            for index, (left, right) in enumerate(
                zip(first, second, strict=True)
            )
            if left != right
        )
        if len(differences) == 1:
            index = differences[0]
            assert 0 < index < len(first) - 1
            adjacency[first].add(second)
            adjacency[second].add(first)
    return adjacency


def endpoint_and_path_audit(matching, fibers, adjacency, distances):
    """Test unique endpoints and coherence of every shortest route family."""

    endpoint_counts = Counter()
    path_counts = Counter()
    square_graph_edges = Counter()
    for source, mark, target in matching:
        endpoint, paths = marked_geodesics(
            source, mark, target, fibers, adjacency, distances
        )
        assert mark in endpoint
        endpoint_counts[1] += 1
        path_counts[len(paths)] += 1

        route_graph = route_square_graph(paths)
        found = {paths[0]}
        queue = [paths[0]]
        for path in queue:
            for neighbor in route_graph[path]:
                if neighbor not in found:
                    found.add(neighbor)
                    queue.append(neighbor)
        assert found == set(paths)
        edge_count = sum(map(len, route_graph.values())) // 2
        square_graph_edges[(len(paths), edge_count)] += 1
    return endpoint_counts, path_counts, square_graph_edges


def triangulation_key(triangulation: Triangulation):
    """Total ordering key for scalar triangulations."""

    return tuple(sorted(triangulation))


def canonical_scalar_edge(
    first: Triangulation, second: Triangulation
) -> tuple[Triangulation, Triangulation]:
    """Canonical orientation of an associahedral flip edge."""

    return (
        (first, second)
        if triangulation_key(first) < triangulation_key(second)
        else (second, first)
    )


def add_oriented_scalar_edge(
    transport,
    first: Triangulation,
    second: Triangulation,
    mark: Diagonal,
    coefficient: Fraction,
) -> None:
    """Add one marked path coefficient with its cellular orientation."""

    edge = canonical_scalar_edge(first, second)
    orientation = 1 if edge == (first, second) else -1
    transport[edge][mark] += orientation * coefficient


def averaged_scalar_transport(matchings, fibers, adjacency, distances):
    """Average every shortest route and form the deck-odd contact chain."""

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
    for key in plus:
        source, mark = key
        plus_endpoint, plus_paths = marked_geodesics(
            source, mark, plus[key], fibers, adjacency, distances
        )
        minus_endpoint, minus_paths = marked_geodesics(
            source, mark, minus[key], fibers, adjacency, distances
        )
        endpoints[key] = (minus_endpoint, plus_endpoint)

        # -X_d times (average plus path - average minus path).
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
    return cleaned, endpoints


def scalar_transport_boundary(transport):
    """Cellular boundary of the marked scalar-associahedral one-chain."""

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


def rotate_scalar_transport(transport):
    """One-step rotation of a marked scalar cellular chain."""

    result = defaultdict(lambda: defaultdict(Fraction))
    for (first, second), values in transport.items():
        rotated_first = rotate_triangulation(first)
        rotated_second = rotate_triangulation(second)
        edge = canonical_scalar_edge(rotated_first, rotated_second)
        orientation = 1 if edge == (rotated_first, rotated_second) else -1
        for mark, coefficient in values.items():
            result[edge][rotate_diagonal(mark)] += orientation * coefficient
    return {
        edge: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for edge, values in result.items()
        if any(values.values())
    }


def negate_scalar_transport(transport):
    """Negate every coefficient of a scalar cellular chain."""

    return {
        edge: {
            mark: -coefficient
            for mark, coefficient in values.items()
        }
        for edge, values in transport.items()
    }


def qtds_contact_coefficients(*, first_is_plus: bool):
    """Extract ten-point contacts from QTDS only after scalar matching."""

    diagonals, variables, kinematics = planar_symbolic_kinematics(
        MULTIPLICITY
    )
    channel_to_diagonal = {}
    for diagonal in physical_diagonals():
        start, end = diagonal
        channel = canonical_channel(
            tuple(range(start, end)), MULTIPLICITY
        )
        assert channel not in channel_to_diagonal
        channel_to_diagonal[channel] = diagonal

    coefficients = {}
    diagram_count = 0
    for numerator, propagators in qtds_raw_terms(
        tuple(range(MULTIPLICITY)),
        kinematics,
        first_is_plus=first_is_plus,
    ):
        assert len(propagators) == 3
        denominator = type(next(iter(variables.values()))).constant(1)
        diagram_diagonals = []
        for block in propagators:
            diagonal = channel_to_diagonal[
                canonical_channel(block, MULTIPLICITY)
            ]
            diagram_diagonals.append(diagonal)
            denominator *= variables[diagonal]
        quadrangulation = tuple(sorted(diagram_diagonals))
        assert quadrangulation in quadrangulations()
        diagram_count += 1
        diagram = (
            (-1) ** (MULTIPLICITY // 2 - 1)
            * numerator
            / denominator
        )
        contact = select_terms(
            diagram, lambda powers: not negative_support(powers)
        )
        for powers, coefficient in contact.terms.items():
            support = tuple(
                index
                for index, exponent in enumerate(powers)
                if exponent
            )
            assert len(support) == 1
            assert powers[support[0]] == 1
            key = (quadrangulation, diagonals[support[0]])
            assert key not in coefficients
            coefficients[key] = coefficient
    assert diagram_count == 55
    return coefficients


def zero_core_marked_coefficients(zero_core_cells):
    """The t^8 coefficient of each marked all-shifted scalar cell."""

    result = {}
    for triangulation in zero_core_cells:
        signs = {
            diagonal: (1 if diagonal[0] % 2 else -1)
            for diagonal in triangulation
        }
        base_sign = 1
        for sign in signs.values():
            base_sign *= sign
        for mark, sign in signs.items():
            result[(triangulation, mark)] = Fraction(
                -base_sign * sign
            )
    return result


def factorization_naturality_audit(*, first_is_plus: bool) -> int:
    """Cut every unique-sink dual tree and test restriction to both factors."""

    coorientations = {
        diagonal: alternating_coorientation(
            diagonal, first_is_plus=first_is_plus
        )
        for diagonal in physical_diagonals()
    }
    cut_checks = 0
    for quadrangulation in quadrangulations():
        directed = directed_dual_tree(quadrangulation, coorientations)
        sinks = sink_cells(quadrangulation, coorientations)
        if len(sinks) != 1:
            continue
        global_sink = sinks[0]
        global_slots = cell_contact_slots(global_sink)
        cells = quadrangulation_cells(quadrangulation)
        for cut_source, cut_target, cut_diagonal in directed:
            remaining = tuple(
                edge for edge in directed if edge[2] != cut_diagonal
            )
            undirected = defaultdict(set)
            for source, target, _ in remaining:
                undirected[source].add(target)
                undirected[target].add(source)

            def component(start):
                found = {start}
                queue = [start]
                for cell in queue:
                    for neighbor in undirected[cell]:
                        if neighbor not in found:
                            found.add(neighbor)
                            queue.append(neighbor)
                return found

            source_component = component(cut_source)
            target_component = set(cells) - source_component
            assert cut_target in target_component

            def component_sinks(component_cells):
                outgoing = Counter(
                    source
                    for source, _, _ in remaining
                    if source in component_cells
                )
                return tuple(
                    cell
                    for cell in component_cells
                    if not outgoing[cell]
                )

            source_sinks = component_sinks(source_component)
            target_sinks = component_sinks(target_component)
            assert source_sinks == (cut_source,)
            assert target_sinks == (global_sink,)
            assert cell_contact_slots(target_sinks[0]) == global_slots
            cut_checks += 1
    return cut_checks


def main() -> None:
    (
        _,
        zero_core_cells,
        fibers,
        adjacency,
    ) = scalar_core_data()
    (
        conservative_count,
        rotation_count,
        joint_count,
    ) = coorientation_uniqueness_audit(zero_core_cells)
    distances = scalar_distances(zero_core_cells, adjacency)
    matchings = {}
    minimizer_data = {}
    transfer_data = {}
    for polarity in (True, False):
        (
            matchings[polarity],
            minimizer_data[polarity],
            transfer_data[polarity],
        ) = derived_marked_matching(
            first_is_plus=polarity,
            zero_core_cells=zero_core_cells,
            fibers=fibers,
            distances=distances,
        )

    rotated_plus = frozenset(
        (
            rotate_triangulation(source),
            rotate_diagonal(mark),
            rotate_quadrangulation(target),
        )
        for source, mark, target in matchings[True]
    )
    assert rotated_plus == matchings[False]

    source_coefficients = zero_core_marked_coefficients(zero_core_cells)
    assert set(source_coefficients.values()) == {Fraction(-1)}
    for polarity in (True, False):
        derived = {
            (target, mark): source_coefficients[(source, mark)]
            for source, mark, target in matchings[polarity]
        }
        qtds = qtds_contact_coefficients(first_is_plus=polarity)
        assert derived == qtds

    endpoint_data = {
        polarity: endpoint_and_path_audit(
            matchings[polarity], fibers, adjacency, distances
        )
        for polarity in (True, False)
    }
    scalar_transport, scalar_endpoints = averaged_scalar_transport(
        matchings, fibers, adjacency, distances
    )
    expected_boundary = defaultdict(lambda: defaultdict(Fraction))
    for (source, mark), (
        minus_endpoint,
        plus_endpoint,
    ) in scalar_endpoints.items():
        expected_boundary[minus_endpoint][mark] += 1
        expected_boundary[plus_endpoint][mark] -= 1
    expected_boundary = {
        vertex: {
            mark: coefficient
            for mark, coefficient in values.items()
            if coefficient
        }
        for vertex, values in expected_boundary.items()
        if any(values.values())
    }
    assert scalar_transport_boundary(scalar_transport) == expected_boundary
    assert rotate_scalar_transport(
        scalar_transport
    ) == negate_scalar_transport(scalar_transport)
    transport_denominators = Counter(
        coefficient.denominator
        for values in scalar_transport.values()
        for coefficient in values.values()
    )
    assert set(transport_denominators) <= {1, 2, 3, 6}
    cut_checks = {
        polarity: factorization_naturality_audit(
            first_is_plus=polarity
        )
        for polarity in (True, False)
    }

    unique_sink_counts = {
        polarity: sum(
            bool(
                scalar_contact_slots(
                    quadrangulation, first_is_plus=polarity
                )
            )
            for quadrangulation in quadrangulations()
        )
        for polarity in (True, False)
    }
    assert unique_sink_counts == {True: 35, False: 35}

    print(
        "n=10 scalar cores: 1430 triangulations, 10 zero-core cells, "
        "70 marked sources, 55 quadrangulations, and 16 refinements per "
        "full core"
    )
    print(
        "n=10 scalar coorientation: all 2^15 flows audited; contact "
        f"conservation selects {conservative_count}; rotation reversal alone "
        f"selects {rotation_count} because the short and diameter diagonals "
        f"are separate cyclic orbits; their intersection has {joint_count}, "
        "exactly the alternating pair"
    )
    print(
        "n=10 scalar matching: each polarity has 35 unique-sink "
        "quadrangulations and 70 slots; every marked assignment is uniquely "
        "minimal at scalar flip distance 3"
    )
    print(
        "n=10 QTDS: the independently expanded numerator recursion gives "
        "the same 70 coefficient -1 contact occurrences for both polarities"
    )
    print(
        "n=10 marked lift diagnostics: "
        f"plus endpoints/paths={endpoint_data[True]}, "
        f"minus endpoints/paths={endpoint_data[False]}"
    )
    print(
        "n=10 scalar lift: every route family is connected by commuting "
        "flip squares; its all-geodesic average has the exact contact "
        "boundary and is deck odd, with coefficient denominators "
        f"{dict(sorted(transport_denominators.items()))}"
    )
    print(
        "n=10 factorization: unique-sink transport restricts naturally on "
        f"all directed cut sides ({cut_checks[True]} checks per polarity)"
    )
    print("all exact ten-point scalar coorientation checks passed")


if __name__ == "__main__":
    main()
