"""Exact combinatorial audit for the scalar/Rees parity-core carrier.

This script checks the finite facts needed by the Frost handoff:

* preserving every non-planar ``c_ij`` leaves only the one-dimensional
  alternating scalar shift at even multiplicity;
* the six-point scalar associahedron resolves into three square physical
  channel facets and two parity-central vertices, each of which supplies a
  canonical tripod to those facets;
* the tripod gives a genuine cellular lift of the QTDS flip-triangle flow;
* at eight points the parity-core fibers have sizes 96, 32, and 4;
* the one-channel and parity-central fibers account for the eight triangles
  and four squares of the QTDS projective-plane cellulation;
* those twelve faces form a Mobius band whose boundary is exactly the
  unexplained octagon.
* the octagon is nevertheless fillable by a vacuous cone through the global
  associahedral barycenter, so the genuine obstruction lives in weights,
  locality, cuts, and the polarity local system rather than bare topology.

The audit does not construct the scalar-normal coefficient-system map.  It
isolates the unique remaining global cell that such a map must supply.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

from check_j_reconstruction import triangulations
from check_qtds_descent import (
    canonical_edge,
    diagonals_cross,
    matrix_rank,
    multiply_matrices,
    quadrangulation_cellulation,
)


Diagonal = tuple[int, int]
Triangulation = frozenset[Diagonal]


def chord(first: int, second: int, multiplicity: int) -> Diagonal | None:
    """Return an unoriented internal polygon chord, or ``None`` on the boundary."""

    first %= multiplicity
    second %= multiplicity
    if first == second or (first - second) % multiplicity in (1, multiplicity - 1):
        return None
    return tuple(sorted((first, second)))


def nonplanar_shift_matrix(multiplicity: int):
    """Linear constraints saying that every c_ij is unchanged by a shift."""

    variables = tuple(
        sorted(
            {
                current
                for first in range(multiplicity)
                for second in range(first + 1, multiplicity)
                if (current := chord(first, second, multiplicity)) is not None
            }
        )
    )
    variable_index = {current: index for index, current in enumerate(variables)}
    matrix = []
    for first in range(multiplicity):
        for separation in range(2, multiplicity - 1):
            second = (first + separation) % multiplicity
            if first > second:
                continue
            row = [0 for _ in variables]
            for left, right, coefficient in (
                (first, second, 1),
                (first + 1, second + 1, 1),
                (first, second + 1, -1),
                (first + 1, second, -1),
            ):
                current = chord(left, right, multiplicity)
                if current is not None:
                    row[variable_index[current]] += coefficient
            matrix.append(row)
    return variables, matrix


def pure_shift_uniqueness_audit() -> None:
    """The pure hidden-zero-preserving shift has no multi-normal refinement."""

    for multiplicity in (4, 6, 8, 10):
        variables, matrix = nonplanar_shift_matrix(multiplicity)
        rank = matrix_rank(matrix)
        assert len(variables) - rank == 1
        alternating = [
            1
            if first % 2 == 0 and second % 2 == 0
            else -1
            if first % 2 == 1 and second % 2 == 1
            else 0
            for first, second in variables
        ]
        assert any(alternating)
        assert all(
            sum(
                coefficient * value
                for coefficient, value in zip(row, alternating, strict=True)
            )
            == 0
            for row in matrix
        )
    print(
        "pure shifts: preserving every c_ij has nullity one at n=4,6,8,10"
    )


def physical_diagonal(diagonal: Diagonal) -> bool:
    """Even polygons factorize into even polygons across opposite-parity chords."""

    return (diagonal[0] - diagonal[1]) % 2 == 1


def flip_edges(triangulation_list: tuple[Triangulation, ...]):
    """Edges of the associahedral flip graph."""

    return tuple(
        frozenset((first, second))
        for first, second in combinations(triangulation_list, 2)
        if len(first ^ second) == 2
    )


def oriented_boundary(edges):
    """Boundary of a small oriented one-chain."""

    result = defaultdict(Fraction)
    for first, second, coefficient in edges:
        result[first] -= coefficient
        result[second] += coefficient
    return {vertex: value for vertex, value in result.items() if value}


def oriented_two_boundary(triangles):
    """Boundary of oriented two-simplices, retaining oriented edge signs."""

    result = defaultdict(Fraction)
    for first, second, third, coefficient in triangles:
        for left, right, sign in (
            (second, third, 1),
            (first, third, -1),
            (first, second, 1),
        ):
            edge = canonical_edge(left, right)
            orientation = 1 if edge == (left, right) else -1
            result[edge] += coefficient * sign * orientation
    return {edge: value for edge, value in result.items() if value}


def nullspace_basis(matrix, modulus: int | None = None):
    """A small exact RREF nullspace basis over Q or F_p."""

    if not matrix:
        return ()
    data = [
        [
            value % modulus if modulus else Fraction(value)
            for value in row
        ]
        for row in matrix
    ]
    row_count = len(data)
    column_count = len(data[0])
    pivot_columns = []
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if data[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        pivot_value = data[pivot_row][column]
        inverse = (
            pow(int(pivot_value), -1, modulus)
            if modulus
            else Fraction(1, 1) / pivot_value
        )
        data[pivot_row] = [
            value * inverse % modulus if modulus else value * inverse
            for value in data[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row or data[row][column] == 0:
                continue
            coefficient = data[row][column]
            data[row] = [
                (
                    (data[row][index] - coefficient * data[pivot_row][index])
                    % modulus
                    if modulus
                    else data[row][index]
                    - coefficient * data[pivot_row][index]
                )
                for index in range(column_count)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    free_columns = [
        column
        for column in range(column_count)
        if column not in pivot_columns
    ]
    basis = []
    for free in free_columns:
        vector = [0 for _ in range(column_count)]
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            value = -data[row][free]
            vector[pivot] = value % modulus if modulus else value
        basis.append(tuple(vector))
    return tuple(basis)


def six_point_tripod_audit() -> None:
    """Build the two canonical parity tripods in sd(K_5)."""

    multiplicity = 6
    all_triangulations = triangulations(tuple(range(multiplicity)))
    flips = set(flip_edges(all_triangulations))
    core = {
        triangulation: frozenset(
            diagonal
            for diagonal in triangulation
            if physical_diagonal(diagonal)
        )
        for triangulation in all_triangulations
    }
    physical = tuple(
        sorted({next(iter(current)) for current in core.values() if current})
    )
    assert len(physical) == 3
    fibers = {
        diagonal: tuple(
            triangulation
            for triangulation in all_triangulations
            if core[triangulation] == frozenset((diagonal,))
        )
        for diagonal in physical
    }
    central = tuple(
        triangulation
        for triangulation in all_triangulations
        if not core[triangulation]
    )
    assert len(central) == 2

    for fiber in fibers.values():
        induced = [edge for edge in flips if edge <= set(fiber)]
        degree = Counter(vertex for edge in induced for vertex in edge)
        assert len(fiber) == 4
        assert len(induced) == 4
        assert set(degree.values()) == {2}

    # A node is a face of K_5: a triangulation vertex, a flip edge, or one of
    # the three square facets.  Comparable faces are joined in sd(K_5).
    paths = {}
    for parity_center_index, center in enumerate(central):
        for diagonal, fiber in fibers.items():
            neighbors = tuple(
                vertex
                for vertex in fiber
                if frozenset((center, vertex)) in flips
            )
            assert len(neighbors) == 1
            corner = neighbors[0]
            flip = frozenset((center, corner))
            center_node = ("vertex", center)
            flip_node = ("edge", flip)
            corner_node = ("vertex", corner)
            facet_node = ("facet", diagonal)
            paths[(parity_center_index, diagonal)] = (
                (center_node, flip_node),
                (flip_node, corner_node),
                (corner_node, facet_node),
            )

    # Test a general sum-zero contact vector.  The triangle inverse-Laplacian
    # flow has the same boundary after every edge is replaced by its unique
    # route through either parity center.
    contacts = dict(zip(physical, (Fraction(2), Fraction(-5), Fraction(3))))
    assert sum(contacts.values(), Fraction(0)) == 0
    for parity_center_index in range(2):
        lifted_chain = []
        for diagonal, coefficient in contacts.items():
            lifted_chain.extend(
                (first, second, coefficient)
                for first, second in paths[(parity_center_index, diagonal)]
            )
        boundary = oriented_boundary(lifted_chain)
        assert boundary == {
            ("facet", diagonal): coefficient
            for diagonal, coefficient in contacts.items()
        }

    print(
        "n=6: three square channel facets and two central vertices give two "
        "canonical parity tripods; each lifts every sum-zero triangle flow"
    )


def face_edges(face):
    """Unoriented boundary edges of a cyclic face."""

    return {
        canonical_edge(face[index], face[(index + 1) % len(face)])
        for index in range(len(face))
    }


def eight_point_carrier_audit() -> None:
    """Identify the scalar parity-core carrier with RP2 minus its octagon."""

    multiplicity = 8
    all_triangulations = triangulations(tuple(range(multiplicity)))
    core = {
        triangulation: frozenset(
            diagonal
            for diagonal in triangulation
            if physical_diagonal(diagonal)
        )
        for triangulation in all_triangulations
    }
    size_counts = Counter(len(current) for current in core.values())
    assert size_counts == {2: 96, 1: 32, 0: 4}

    (
        physical,
        _,
        _,
        _,
        quadrangulations,
        flips,
        faces,
    ) = quadrangulation_cellulation()
    triangles = faces[:8]
    squares = faces[8:12]
    octagon = faces[12]

    core_two = defaultdict(list)
    core_one = defaultdict(list)
    core_zero = []
    for triangulation, current in core.items():
        if len(current) == 2:
            core_two[current].append(triangulation)
        elif len(current) == 1:
            core_one[next(iter(current))].append(triangulation)
        else:
            core_zero.append(triangulation)
    assert set(core_two) == {
        frozenset(quadrangulation) for quadrangulation in quadrangulations
    }
    assert set(len(fiber) for fiber in core_two.values()) == {8}
    assert set(core_one) == set(physical)
    assert set(len(fiber) for fiber in core_one.values()) == {4}

    triangle_by_diagonal = {
        diagonal: frozenset(
            quadrangulation
            for quadrangulation in quadrangulations
            if diagonal in quadrangulation
        )
        for diagonal in physical
    }
    assert set(triangle_by_diagonal.values()) == {
        frozenset(face) for face in triangles
    }

    square_sets = {frozenset(face) for face in squares}
    seen_squares = set()
    for triangulation in core_zero:
        diameters = tuple(
            diagonal
            for diagonal in triangulation
            if (diagonal[1] - diagonal[0]) % multiplicity == multiplicity // 2
        )
        assert len(diameters) == 1
        diameter = diameters[0]
        compatible = frozenset(
            quadrangulation
            for quadrangulation in quadrangulations
            if all(
                not diagonals_cross(diameter, diagonal)
                for diagonal in quadrangulation
            )
        )
        assert len(compatible) == 4
        assert compatible in square_sets
        seen_squares.add(compatible)
    assert seen_squares == square_sets

    # Remove the octagonal face from the exact RP2 cellulation.  The result
    # has one boundary component, Euler characteristic zero, and rational
    # Betti numbers (1,1,0): it is the Mobius-band carrier.
    carrier_faces = tuple(triangles) + tuple(squares)
    incidences = Counter(
        edge for face in carrier_faces for edge in face_edges(face)
    )
    boundary = {edge for edge, count in incidences.items() if count == 1}
    assert boundary == face_edges(octagon)
    assert set(incidences.values()) == {1, 2}
    assert len(quadrangulations) - len(flips) + len(carrier_faces) == 0

    vertex_index = {
        vertex: index for index, vertex in enumerate(quadrangulations)
    }
    edge_index = {edge: index for index, edge in enumerate(flips)}
    boundary_one = [[0 for _ in flips] for _ in quadrangulations]
    for column, (first, second) in enumerate(flips):
        boundary_one[vertex_index[first]][column] = -1
        boundary_one[vertex_index[second]][column] = 1
    boundary_two = [[0 for _ in carrier_faces] for _ in flips]
    for column, face in enumerate(carrier_faces):
        for index, first in enumerate(face):
            second = face[(index + 1) % len(face)]
            edge = canonical_edge(first, second)
            boundary_two[edge_index[edge]][column] += (
                1 if edge == (first, second) else -1
            )
    first_rank = matrix_rank(boundary_one)
    second_rank = matrix_rank(boundary_two)
    betti = (
        len(quadrangulations) - first_rank,
        len(flips) - first_rank - second_rank,
        len(carrier_faces) - second_rank,
    )
    assert betti == (1, 1, 0)

    print(
        "n=8: core counts are 96/32/4; scalar cones canonically account for "
        "8 triangles and 4 squares, a Mobius band bounded by the octagon"
    )


def vacuous_octagon_cone_audit() -> None:
    """Show that bare associahedral topology cannot be the obstruction.

    A target quadrangulation Q labels the associahedral face fixing its two
    diagonals. Adjacent octagon vertices Q,Q' share a physical diagonal D,
    so their barycenters connect through the barycenter of the facet fixing D.
    The resulting subdivided octagon can be coned to the barycenter of the
    whole associahedron. This uses no scalar grade or local coefficient data
    and is therefore deliberately *not* the desired QTDS filler.
    """

    octagon = quadrangulation_cellulation()[6][12]
    expanded_loop = []
    for index, quadrangulation in enumerate(octagon):
        following = octagon[(index + 1) % len(octagon)]
        shared = tuple(set(quadrangulation) & set(following))
        assert len(shared) == 1
        current_node = ("quadrangulation", quadrangulation)
        facet_node = ("physical facet", shared[0])
        following_node = ("quadrangulation", following)
        expanded_loop.extend(
            ((current_node, facet_node), (facet_node, following_node))
        )

    assert not oriented_boundary(
        (first, second, Fraction(1)) for first, second in expanded_loop
    )
    expected = defaultdict(Fraction)
    for first, second in expanded_loop:
        edge = canonical_edge(first, second)
        expected[edge] += 1 if edge == (first, second) else -1

    center = ("whole associahedron",)
    cone = [
        (center, first, second, Fraction(1))
        for first, second in expanded_loop
    ]
    assert oriented_two_boundary(cone) == dict(expected)

    print(
        "n=8: the subdivided octagon has a canonical bare cone through the "
        "global associahedral barycenter; only weighted/local/deck-equivariant "
        "filling can be obstructed"
    )


def orientation_local_system_audit() -> None:
    """Resolve the unique Z2 sector and its orientation double cover.

    This identifies the only possible rank-one sign system on the RP2
    presentation complex.  It does not assert that QTDS polarity transport
    realizes this system; that is a coefficient-level test.
    """

    (
        _,
        _,
        _,
        _,
        vertices,
        edges,
        faces,
    ) = quadrangulation_cellulation()
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
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

    # A Z2 voltage on edges is a one-cocycle when it sums to zero around
    # every face.  H^1(RP2;F2)=F2, so choose the unique non-coboundary class.
    cocycle_equations = [
        [boundary_two[edge][face] for edge in range(len(edges))]
        for face in range(len(faces))
    ]
    cocycles = nullspace_basis(cocycle_equations, 2)
    coboundary_rank = matrix_rank(boundary_one, 2)
    voltage = next(
        candidate
        for candidate in cocycles
        if matrix_rank(boundary_one + [list(candidate)], 2)
        == coboundary_rank + 1
    )
    assert all(
        sum(
            cocycle_equations[face][edge] * voltage[edge]
            for edge in range(len(edges))
        )
        % 2
        == 0
        for face in range(len(faces))
    )

    # Boundary matrices with transport (-1)^voltage.  Edge generators are
    # based at the first endpoint of their canonical orientation.
    twisted_one = [[0 for _ in edges] for _ in vertices]
    for column, (first, second) in enumerate(edges):
        transport = -1 if voltage[column] else 1
        twisted_one[vertex_index[first]][column] = -1
        twisted_one[vertex_index[second]][column] = transport

    twisted_two = [[0 for _ in faces] for _ in edges]
    for column, face in enumerate(faces):
        prefix_voltage = 0
        for index, first in enumerate(face):
            second = face[(index + 1) % len(face)]
            edge = canonical_edge(first, second)
            edge_number = edge_index[edge]
            prefix_transport = -1 if prefix_voltage else 1
            edge_transport = -1 if voltage[edge_number] else 1
            if edge == (first, second):
                coefficient = prefix_transport
            else:
                coefficient = -prefix_transport * edge_transport
            twisted_two[edge_number][column] += coefficient
            prefix_voltage ^= voltage[edge_number]
        assert prefix_voltage == 0
    assert all(
        value == 0
        for row in multiply_matrices(twisted_one, twisted_two)
        for value in row
    )

    twisted_ranks = (
        matrix_rank(twisted_one),
        matrix_rank(twisted_two),
    )
    twisted_betti = (
        len(vertices) - twisted_ranks[0],
        len(edges) - twisted_ranks[0] - twisted_ranks[1],
        len(faces) - twisted_ranks[1],
    )
    assert twisted_ranks == (12, 12)
    assert twisted_betti == (0, 0, 1)

    # Removing the octagon gives the Mobius carrier.  It is acyclic over Q
    # with the orientation system, while a unique relative fundamental chain
    # has boundary supported on the octagonal loop.
    carrier_two = [row[:-1] for row in twisted_two]
    carrier_betti = (
        len(vertices) - twisted_ranks[0],
        len(edges)
        - twisted_ranks[0]
        - matrix_rank(carrier_two),
        len(faces) - 1 - matrix_rank(carrier_two),
    )
    assert carrier_betti == (0, 0, 0)
    boundary_edges = face_edges(faces[-1])
    interior_rows = [
        carrier_two[index]
        for index, edge in enumerate(edges)
        if edge not in boundary_edges
    ]
    relative_cycles = nullspace_basis(interior_rows)
    assert len(relative_cycles) == 1
    relative_boundary = [
        sum(
            carrier_two[row][column] * relative_cycles[0][column]
            for column in range(len(faces) - 1)
        )
        for row in range(len(edges))
    ]
    assert all(
        (coefficient != 0) == (edge in boundary_edges)
        for edge, coefficient in zip(edges, relative_boundary, strict=True)
    )

    # Build the connected two-fold cover classified by the same cocycle.
    lifted_vertices = {
        (vertex, sheet) for vertex in vertices for sheet in (0, 1)
    }
    lifted_edges = set()
    adjacency = defaultdict(set)
    for edge_number, (first, second) in enumerate(edges):
        for sheet in (0, 1):
            lifted = canonical_edge(
                (first, sheet),
                (second, sheet ^ voltage[edge_number]),
            )
            lifted_edges.add(lifted)
            adjacency[lifted[0]].add(lifted[1])
            adjacency[lifted[1]].add(lifted[0])
    seen = set()
    stack = [next(iter(lifted_vertices))]
    while stack:
        vertex = stack.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        stack.extend(adjacency[vertex] - seen)
    assert seen == lifted_vertices
    assert len(lifted_vertices) == 24
    assert len(lifted_edges) == 48

    lifted_faces = []
    lifted_edge_incidence = Counter()
    for face in faces:
        for starting_sheet in (0, 1):
            sheet = starting_sheet
            lifted_face = []
            for index, first in enumerate(face):
                lifted_face.append((first, sheet))
                second = face[(index + 1) % len(face)]
                edge_number = edge_index[canonical_edge(first, second)]
                sheet ^= voltage[edge_number]
            assert sheet == starting_sheet
            lifted_faces.append(tuple(lifted_face))
            for index, first in enumerate(lifted_face):
                lifted_edge_incidence[
                    canonical_edge(
                        first,
                        lifted_face[(index + 1) % len(lifted_face)],
                    )
                ] += 1
    assert len(lifted_faces) == 26
    assert set(lifted_edge_incidence) == lifted_edges
    assert set(lifted_edge_incidence.values()) == {2}
    assert len(lifted_vertices) - len(lifted_edges) + len(lifted_faces) == 2

    # The octagonal attaching loop is sign-even, while a shortest crosscap
    # loop is sign-odd.  This is the concrete monodromy target for any QTDS
    # edge transport claiming to realize the orientation system.
    octagon_voltage = sum(
        voltage[
            edge_index[
                canonical_edge(
                    faces[-1][index],
                    faces[-1][(index + 1) % len(faces[-1])],
                )
            ]
        ]
        for index in range(len(faces[-1]))
    ) % 2
    assert octagon_voltage == 0

    deck_distances = []
    for base_vertex in vertices:
        start = (base_vertex, 0)
        target = (base_vertex, 1)
        queue = [(start, 0)]
        visited = {start}
        for current, distance in queue:
            if current == target:
                deck_distances.append(distance)
                break
            for neighbor in adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
    assert min(deck_distances) == 5

    print(
        "n=8 sign system: twisted Betti numbers are (0,0,1); the Mobius "
        "carrier is twisted-acyclic with one relative fundamental chain"
    )
    print(
        "n=8 sign system: the unique nontrivial connected double cover has "
        "V/E/F=24/48/26 and Euler characteristic 2, hence is the sphere"
    )
    print(
        "n=8 sign system: the octagonal attaching loop is sign-even and a "
        "shortest sign-odd crosscap loop uses 5 flips"
    )


def main() -> None:
    pure_shift_uniqueness_audit()
    six_point_tripod_audit()
    eight_point_carrier_audit()
    vacuous_octagon_cone_audit()
    orientation_local_system_audit()
    print("all exact scalar/Rees carrier checks passed")


if __name__ == "__main__":
    main()
