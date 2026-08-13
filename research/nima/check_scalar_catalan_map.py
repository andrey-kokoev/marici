"""Direct Catalan construction of the scalar marked contact transfer.

The earlier audits found the contact map by solving a global minimum-distance
assignment.  This script removes that solver from the construction.

A zero-core triangulation of a 2m-gon is a triangulated parity m-gon together
with its m ear edges.  Mark one edge of that parity triangulation and root its
triangle dual forest there.  In every triangle select the predecessor or
successor of the parent edge according to the alternating sheet/polarity.
The selected edges form disjoint chains.  Flip each chain leaf-first, with
arbitrary interleaving between chains.

Through fourteen points the resulting endpoint is independent of interleaving,
is the unique closest marked full-core refinement, and its physical core is
bijective with the unique-sink slots of the alternating quadrangulations.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

from check_j_reconstruction import triangulations


Diagonal = tuple[int, int]
Triangulation = frozenset[Diagonal]
Quadrangulation = tuple[Diagonal, ...]
Cell = tuple[int, int, int, int]


def canonical_diagonal(first: int, second: int) -> Diagonal:
    """Canonical encoding of an unoriented chord."""

    return tuple(sorted((first, second)))


def is_boundary(diagonal: Diagonal, multiplicity: int) -> bool:
    """Whether a chord is an edge of the original polygon."""

    difference = diagonal[1] - diagonal[0]
    return difference in (1, multiplicity - 1)


def physical_core(triangulation: Triangulation) -> Quadrangulation:
    """Opposite-color diagonals in a scalar triangulation."""

    return tuple(
        sorted(
            diagonal
            for diagonal in triangulation
            if (diagonal[0] - diagonal[1]) % 2
        )
    )


def rotate_diagonal(
    diagonal: Diagonal, multiplicity: int, amount: int = 1
) -> Diagonal:
    """Rotate one unoriented chord."""

    return canonical_diagonal(
        (diagonal[0] + amount) % multiplicity,
        (diagonal[1] + amount) % multiplicity,
    )


def rotate_triangulation(
    triangulation: Triangulation,
    multiplicity: int,
    amount: int = 1,
) -> Triangulation:
    """Rotate a scalar triangulation."""

    return frozenset(
        rotate_diagonal(diagonal, multiplicity, amount)
        for diagonal in triangulation
    )


def rotate_quadrangulation(
    quadrangulation: Quadrangulation,
    multiplicity: int,
    amount: int = 1,
) -> Quadrangulation:
    """Rotate a quadrangulation."""

    return tuple(
        sorted(
            rotate_diagonal(diagonal, multiplicity, amount)
            for diagonal in quadrangulation
        )
    )


def boundary_edges(multiplicity: int) -> frozenset[Diagonal]:
    """Boundary edges of the original polygon."""

    return frozenset(
        canonical_diagonal(vertex, (vertex + 1) % multiplicity)
        for vertex in range(multiplicity)
    )


def quadrangulation_cells(
    quadrangulation: Quadrangulation, multiplicity: int
) -> tuple[Cell, ...]:
    """Quadrilateral regions cut out by a full physical core."""

    edges = set(quadrangulation) | set(boundary_edges(multiplicity))
    cells = tuple(
        vertices
        for vertices in combinations(range(multiplicity), 4)
        if all(
            canonical_diagonal(
                vertices[index],
                vertices[(index + 1) % 4],
            )
            in edges
            for index in range(4)
        )
    )
    assert len(cells) == multiplicity // 2 - 1
    return cells


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

    plus_side = 1 if diagonal[0] % 2 == 0 else 0
    return plus_side if first_is_plus else 1 - plus_side


def sink_contact_slots(
    quadrangulation: Quadrangulation,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> frozenset[Diagonal]:
    """The two scalar diagonals of the unique directed-dual-tree sink."""

    cells = quadrangulation_cells(quadrangulation, multiplicity)
    outdegree = Counter()
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
        outdegree[source] += 1
    sinks = tuple(cell for cell in cells if not outdegree[cell])
    if len(sinks) != 1:
        return frozenset()
    first, second, third, fourth = sinks[0]
    return frozenset(
        (
            canonical_diagonal(first, third),
            canonical_diagonal(second, fourth),
        )
    )


def directed_sink_flow(
    quadrangulation: Quadrangulation,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> tuple[
    tuple[Cell, ...],
    Cell,
    dict[Cell, Diagonal],
    dict[Diagonal, tuple[Cell, Cell]],
]:
    """Root a unique-sink quadrangulation dual tree at its sink.

    The returned cell-to-edge map records the unique outgoing/parent edge of
    every non-sink cell.  The edge map records (source, target).
    """

    cells = quadrangulation_cells(quadrangulation, multiplicity)
    outgoing = {}
    directions = {}
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
        assert source not in outgoing
        outgoing[source] = diagonal
        directions[diagonal] = (source, target)
    sinks = tuple(cell for cell in cells if cell not in outgoing)
    assert len(sinks) == 1
    return cells, sinks[0], outgoing, directions


def parity_triangles(
    triangulation: Triangulation, multiplicity: int
) -> tuple[tuple[tuple[int, int, int], tuple[Diagonal, ...]], ...]:
    """Faces of the central triangulated parity polygon."""

    vertices = tuple(sorted(set().union(*map(set, triangulation))))
    assert len(vertices) == multiplicity // 2
    assert len({vertex % 2 for vertex in vertices}) == 1
    result = []
    for first, second, third in combinations(vertices, 3):
        edges = (
            canonical_diagonal(first, second),
            canonical_diagonal(second, third),
            canonical_diagonal(first, third),
        )
        if all(edge in triangulation for edge in edges):
            result.append(((first, second, third), edges))
    assert len(result) == multiplicity // 2 - 2
    return tuple(result)


def rooted_flip_chains(
    triangulation: Triangulation,
    mark: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> tuple[tuple[Diagonal, ...], ...]:
    """Construct the leaf-first chains of scalar edges to physicalize."""

    triangles = parity_triangles(triangulation, multiplicity)
    incidence = defaultdict(list)
    for index, (_, edges) in enumerate(triangles):
        for edge in edges:
            incidence[edge].append(index)
    assert mark in incidence

    # Adjoin an artificial root at the marked edge.  If the mark is internal,
    # the triangle dual tree splits into two rooted components.
    parent_edge = {}
    queue = deque()
    for index in incidence[mark]:
        parent_edge[index] = mark
        queue.append(index)
    while queue:
        index = queue.popleft()
        for edge in triangles[index][1]:
            if edge == parent_edge[index]:
                continue
            for neighbor in incidence[edge]:
                if neighbor != index and neighbor not in parent_edge:
                    parent_edge[neighbor] = edge
                    queue.append(neighbor)
    assert len(parent_edge) == len(triangles)

    sheet_is_even = triangles[0][0][0] % 2 == 0
    choose_predecessor = first_is_plus == sheet_is_even
    selected = {}
    for index, (_, edges) in enumerate(triangles):
        parent_position = edges.index(parent_edge[index])
        selected[index] = edges[
            (parent_position - 1) % 3
            if choose_predecessor
            else (parent_position + 1) % 3
        ]
    assert mark not in selected.values()
    assert len(set(selected.values())) == len(triangles)

    # A selected internal child edge continues the same chain.  Because every
    # non-root triangle has one parent, the selected-edge graph is a disjoint
    # union of chains rather than a branching forest.
    successor = {}
    for index, edge in selected.items():
        neighbors = tuple(
            neighbor for neighbor in incidence[edge] if neighbor != index
        )
        if neighbors:
            assert len(neighbors) == 1
            child = neighbors[0]
            assert parent_edge[child] == edge
            successor[index] = child
    children = set(successor.values())
    starts = tuple(
        index for index in range(len(triangles)) if index not in children
    )
    chains = []
    for start in starts:
        forward = []
        index = start
        while True:
            forward.append(selected[index])
            if index not in successor:
                break
            index = successor[index]
        chains.append(tuple(reversed(forward)))
    chains = tuple(sorted(chains))
    assert sum(map(len, chains)) == len(triangles)
    assert len(set().union(*map(set, chains))) == len(triangles)
    return chains


def edge_is_present(
    diagonal: Diagonal,
    triangulation: Triangulation,
    multiplicity: int,
) -> bool:
    """Whether a chord is a boundary edge or a current triangulation edge."""

    return is_boundary(diagonal, multiplicity) or diagonal in triangulation


def flip_diagonal(
    triangulation: Triangulation,
    diagonal: Diagonal,
    multiplicity: int,
) -> tuple[Triangulation, Diagonal]:
    """Flip one current diagonal and return its replacement."""

    first, second = diagonal
    opposite = tuple(
        vertex
        for vertex in range(multiplicity)
        if vertex not in diagonal
        and edge_is_present(
            canonical_diagonal(first, vertex),
            triangulation,
            multiplicity,
        )
        and edge_is_present(
            canonical_diagonal(second, vertex),
            triangulation,
            multiplicity,
        )
    )
    assert len(opposite) == 2
    replacement = canonical_diagonal(*opposite)
    assert not is_boundary(replacement, multiplicity)
    assert replacement not in triangulation
    result = frozenset(
        (set(triangulation) - {diagonal}) | {replacement}
    )
    return result, replacement


def chain_interleavings(
    chains: tuple[tuple[Diagonal, ...], ...],
) -> tuple[tuple[Diagonal, ...], ...]:
    """All shuffles preserving the order within every flip chain."""

    result = []
    positions = [0] * len(chains)

    def visit(prefix):
        if all(
            positions[index] == len(chain)
            for index, chain in enumerate(chains)
        ):
            result.append(tuple(prefix))
            return
        for index, chain in enumerate(chains):
            if positions[index] == len(chain):
                continue
            edge = chain[positions[index]]
            positions[index] += 1
            visit(prefix + [edge])
            positions[index] -= 1

    visit([])
    expected = factorial(sum(map(len, chains)))
    for chain in chains:
        expected //= factorial(len(chain))
    assert len(result) == expected
    assert len(set(result)) == len(result)
    return tuple(sorted(result))


def route_square_profile(
    orders: tuple[tuple[Diagonal, ...], ...]
) -> tuple[int, int]:
    """Connectivity graph under adjacent swaps of independent chain flips."""

    adjacency = {order: set() for order in orders}
    for first, second in combinations(orders, 2):
        differences = tuple(
            index
            for index, (left, right) in enumerate(
                zip(first, second, strict=True)
            )
            if left != right
        )
        if (
            len(differences) == 2
            and differences[1] == differences[0] + 1
            and first[differences[0]] == second[differences[1]]
            and first[differences[1]] == second[differences[0]]
        ):
            adjacency[first].add(second)
            adjacency[second].add(first)
    found = {orders[0]}
    queue = [orders[0]]
    for order in queue:
        for neighbor in adjacency[order]:
            if neighbor not in found:
                found.add(neighbor)
                queue.append(neighbor)
    assert found == set(orders)
    return (
        len(orders),
        sum(map(len, adjacency.values())) // 2,
    )


def direct_endpoint(
    triangulation: Triangulation,
    mark: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> tuple[
    Triangulation,
    Quadrangulation,
    tuple[tuple[Diagonal, ...], ...],
    tuple[tuple[Diagonal, ...], ...],
]:
    """Apply every chain shuffle and return their common endpoint."""

    chains = rooted_flip_chains(
        triangulation,
        mark,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    orders = chain_interleavings(chains)
    endpoints = set()
    for order in orders:
        current = triangulation
        for diagonal in order:
            current, replacement = flip_diagonal(
                current, diagonal, multiplicity
            )
            assert (replacement[0] - replacement[1]) % 2
        endpoints.add(current)
    assert len(endpoints) == 1
    endpoint = endpoints.pop()
    assert mark in endpoint
    core = physical_core(endpoint)
    assert len(core) == multiplicity // 2 - 2
    return endpoint, core, chains, orders


def inverse_source(
    quadrangulation: Quadrangulation,
    mark: Diagonal,
    multiplicity: int,
    *,
    first_is_plus: bool,
) -> tuple[
    Triangulation,
    Triangulation,
    tuple[tuple[Diagonal, ...], ...],
    tuple[tuple[Diagonal, ...], ...],
]:
    """Invert the direct Catalan map using only a marked sink slot.

    Refine every quadrilateral by the scalar diagonal of the marked color.
    In each non-sink cell, select the predecessor/successor boundary edge of
    its outgoing parent edge.  Selected physical child edges continue an
    inverse chain.  Flip those chains from the sink outward.
    """

    (
        cells,
        sink,
        outgoing,
        directions,
    ) = directed_sink_flow(
        quadrangulation,
        multiplicity,
        first_is_plus=first_is_plus,
    )
    sink_first, sink_second, sink_third, sink_fourth = sink
    assert mark in {
        canonical_diagonal(sink_first, sink_third),
        canonical_diagonal(sink_second, sink_fourth),
    }
    sheet_parity = mark[0] % 2

    endpoint_edges = set(quadrangulation)
    for first, second, third, fourth in cells:
        scalar_diagonals = (
            canonical_diagonal(first, third),
            canonical_diagonal(second, fourth),
        )
        chosen = tuple(
            diagonal
            for diagonal in scalar_diagonals
            if diagonal[0] % 2 == sheet_parity
        )
        assert len(chosen) == 1
        endpoint_edges.add(chosen[0])
    endpoint = frozenset(endpoint_edges)
    assert len(endpoint) == multiplicity - 3
    assert mark in endpoint

    choose_predecessor = first_is_plus == (sheet_parity == 0)
    successor = {}
    for cell, parent in outgoing.items():
        first, second, third, fourth = cell
        boundary = (
            canonical_diagonal(first, second),
            canonical_diagonal(second, third),
            canonical_diagonal(third, fourth),
            canonical_diagonal(first, fourth),
        )
        parent_position = boundary.index(parent)
        selected = boundary[
            (parent_position - 1) % 4
            if choose_predecessor
            else (parent_position + 1) % 4
        ]
        if selected in quadrangulation:
            assert selected != parent
            child, target = directions[selected]
            assert target == cell
            assert child != cell
            successor[parent] = selected

    children = set(successor.values())
    starts = tuple(
        diagonal
        for diagonal in quadrangulation
        if diagonal not in children
    )
    chains = []
    for start in starts:
        chain = []
        diagonal = start
        while True:
            chain.append(diagonal)
            if diagonal not in successor:
                break
            diagonal = successor[diagonal]
        chains.append(tuple(chain))
    chains = tuple(sorted(chains))
    assert sum(map(len, chains)) == len(quadrangulation)
    assert len(set().union(*map(set, chains))) == len(quadrangulation)

    orders = chain_interleavings(chains)
    sources = set()
    for order in orders:
        current = endpoint
        for diagonal in order:
            current, replacement = flip_diagonal(
                current, diagonal, multiplicity
            )
            assert replacement[0] % 2 == sheet_parity
            assert replacement[1] % 2 == sheet_parity
        sources.add(current)
    assert len(sources) == 1
    source = sources.pop()
    assert not physical_core(source)
    assert mark in source
    return source, endpoint, chains, orders


def catalan(index: int) -> int:
    """Catalan number C_index."""

    return comb(2 * index, index) // (index + 1)


def fuss_catalan_quadrangulations(multiplicity: int) -> int:
    """Number of quadrangulations of a 2m-gon."""

    region_count = multiplicity // 2 - 1
    return comb(3 * region_count, region_count) // (
        2 * region_count + 1
    )


def multiplicity_audit(multiplicity: int):
    """Verify the direct marked bijection at one even arity."""

    half = multiplicity // 2
    triangulation_list = triangulations(tuple(range(multiplicity)))
    zero_core_cells = tuple(
        triangulation
        for triangulation in triangulation_list
        if not physical_core(triangulation)
    )
    assert len(zero_core_cells) == 2 * catalan(half - 2)

    fibers = defaultdict(list)
    for triangulation in triangulation_list:
        core = physical_core(triangulation)
        if len(core) == half - 2:
            fibers[core].append(triangulation)
    quadrangulations = tuple(sorted(fibers))
    assert len(quadrangulations) == fuss_catalan_quadrangulations(
        multiplicity
    )
    assert set(map(len, fibers.values())) == {2 ** (half - 1)}

    direct_by_polarity = {}
    chain_profiles = {}
    route_profiles = {}
    for polarity in (True, False):
        direct = set()
        chain_profile = Counter()
        route_profile = Counter()
        for source in zero_core_cells:
            for mark in source:
                endpoint, target, chains, orders = direct_endpoint(
                    source,
                    mark,
                    multiplicity,
                    first_is_plus=polarity,
                )
                assert mark in sink_contact_slots(
                    target,
                    multiplicity,
                    first_is_plus=polarity,
                )
                (
                    recovered_source,
                    recovered_endpoint,
                    inverse_chains,
                    inverse_orders,
                ) = inverse_source(
                    target,
                    mark,
                    multiplicity,
                    first_is_plus=polarity,
                )
                assert recovered_source == source
                assert recovered_endpoint == endpoint
                assert sorted(map(len, inverse_chains)) == sorted(
                    map(len, chains)
                )
                assert len(inverse_orders) == len(orders)

                # Any path to a full core needs at least half-2 physicalizing
                # flips.  The direct endpoint attains that bound.  It is the
                # only marked target refinement differing in only half-2
                # source edges, so it is the unique closest endpoint.
                closest_candidates = tuple(
                    candidate
                    for candidate in fibers[target]
                    if mark in candidate
                    and len(source - candidate) == half - 2
                )
                assert closest_candidates == (endpoint,)

                occurrence = (source, mark, target)
                assert occurrence not in direct
                direct.add(occurrence)
                chain_profile[
                    tuple(sorted(map(len, chains), reverse=True))
                ] += 1
                route_profile[route_square_profile(orders)] += 1

        sink_occurrences = {
            (target, mark)
            for target in quadrangulations
            for mark in sink_contact_slots(
                target,
                multiplicity,
                first_is_plus=polarity,
            )
        }
        target_occurrences = {
            (target, mark) for _, mark, target in direct
        }
        assert len(target_occurrences) == len(direct)
        assert target_occurrences == sink_occurrences
        expected_marked = (
            2 * (2 * half - 3) * catalan(half - 2)
        )
        assert len(direct) == expected_marked
        direct_by_polarity[polarity] = frozenset(direct)
        chain_profiles[polarity] = chain_profile
        route_profiles[polarity] = route_profile

    rotated_plus = frozenset(
        (
            rotate_triangulation(source, multiplicity),
            rotate_diagonal(mark, multiplicity),
            rotate_quadrangulation(target, multiplicity),
        )
        for source, mark, target in direct_by_polarity[True]
    )
    assert rotated_plus == direct_by_polarity[False]
    assert chain_profiles[True] == chain_profiles[False]
    assert route_profiles[True] == route_profiles[False]

    return {
        "zero_core": len(zero_core_cells),
        "marked": len(direct_by_polarity[True]),
        "quadrangulations": len(quadrangulations),
        "unique_sinks": len(direct_by_polarity[True]) // 2,
        "distance": half - 2,
        "chain_profiles": chain_profiles[True],
        "route_profiles": route_profiles[True],
    }


def main() -> None:
    for multiplicity in (6, 8, 10, 12, 14):
        result = multiplicity_audit(multiplicity)
        print(
            f"n={multiplicity} direct Catalan map: "
            f"{result['zero_core']} zero cells, "
            f"{result['marked']} marked sources, "
            f"{result['quadrangulations']} quadrangulations, "
            f"{result['unique_sinks']} unique sinks per polarity, "
            f"distance {result['distance']}"
        )
        print(
            f"n={multiplicity} chain profiles "
            f"{dict(result['chain_profiles'])}; "
            f"square-route profiles {dict(result['route_profiles'])}"
        )
    print(
        "all direct scalar Catalan-map checks through fourteen points passed"
    )


if __name__ == "__main__":
    main()
