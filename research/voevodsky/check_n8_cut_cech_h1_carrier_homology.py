"""Compute the carrier differential on the 157-dimensional Cut-Cech H1 page."""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations

import check_n8_full_twisted_cut_cech_lift as full
import check_n8_six_by_four_cut_boundary as polygon


def matrix_rank(matrix):
    if not matrix or not matrix[0]:
        return 0
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def rref_pivots(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    pivots = []
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    return work, tuple(pivots)


def multiply(left, right):
    if not left:
        return []
    if not right:
        return [[] for _ in left]
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def graph_data(vertices, ambient_edges):
    vertices = tuple(sorted(vertices))
    edges = tuple(edge for edge in ambient_edges if edge[0] in vertices and edge[1] in vertices)
    adjacency = defaultdict(list)
    for index, (a, b) in enumerate(edges):
        adjacency[a].append((b, index, 1))
        adjacency[b].append((a, index, -1))

    tree_edges = set()
    roots = []
    seen = set()
    for root in vertices:
        if root in seen:
            continue
        roots.append(root)
        seen.add(root)
        queue = deque([root])
        while queue:
            vertex = queue.popleft()
            for neighbor, edge_index, _ in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    tree_edges.add(edge_index)
                    queue.append(neighbor)
    chords = tuple(i for i in range(len(edges)) if i not in tree_edges)
    return vertices, edges, adjacency, tree_edges, roots, chords


def quotient_coordinates(data, edge_values):
    vertices, edges, adjacency, tree_edges, roots, chords = data
    potential = {}
    for root in roots:
        potential[root] = 0
        queue = deque([root])
        while queue:
            vertex = queue.popleft()
            for neighbor, edge_index, direction in adjacency[vertex]:
                if edge_index not in tree_edges or neighbor in potential:
                    continue
                # edge value minus (p_b-p_a); direction is +1 at a, -1 at b.
                value = edge_values.get(edges[edge_index], 0)
                potential[neighbor] = potential[vertex] + direction * value
                queue.append(neighbor)
    coordinates = []
    for edge_index in chords:
        a, b = edges[edge_index]
        coordinates.append(edge_values.get((a, b), 0) - (potential[b] - potential[a]))
    return tuple(coordinates)


def main():
    all_diagonals = polygon.diagonals(full.N)
    cuts = tuple(sorted({full.normalized(i, i + 3) for i in range(full.N)}))
    ambient_edges = tuple(
        (a, b) for a, b in combinations(cuts, 2) if not polygon.crosses(a, b)
    )

    occurrences = defaultdict(set)
    chart_cells = {}
    for cut in cuts:
        link = tuple(d for d in all_diagonals if d != cut and not polygon.crosses(d, cut))
        cells = set(full.loaded_cells(link))
        chart_cells[cut] = cells
        for cell in cells:
            occurrences[cell].add(cut)

    data = {cell: graph_data(vertices, ambient_edges) for cell, vertices in occurrences.items()}
    cyclic = {cell: value for cell, value in data.items() if value[-1]}
    assert sum(len(value[-1]) for value in cyclic.values()) == 157

    basis_by_degree = defaultdict(list)
    for cell, value in cyclic.items():
        degree = full.DIMENSION - len(cell[0]) + len(cell[1])
        for chord in value[-1]:
            basis_by_degree[degree].append((cell, chord))
    assert tuple(len(basis_by_degree[d]) for d in range(5)) == (0, 4, 32, 72, 49)

    # Generate every distinct loaded carrier arrow once. Its sign is independent
    # of the Cut chart in which it is observed.
    carrier_arrows = {}
    for cut, cells in chart_cells.items():
        link = tuple(d for d in all_diagonals if d != cut and not polygon.crosses(d, cut))
        for source, target, sign, kind in full.arrows(link, tuple(cells)):
            previous = carrier_arrows.setdefault((source, target), (sign, kind))
            assert previous == (sign, kind)

    matrices = {}
    for degree in range(1, 5):
        source_basis = basis_by_degree[degree]
        target_basis = basis_by_degree[degree - 1]
        target_index = {item: i for i, item in enumerate(target_basis)}
        matrix = [[0] * len(source_basis) for _ in target_basis]
        outgoing = defaultdict(list)
        for (source, target), (sign, kind) in carrier_arrows.items():
            if source in cyclic and target in cyclic:
                outgoing[source].append((target, sign, kind))

        for column, (source_cell, source_chord_index) in enumerate(source_basis):
            source_graph = cyclic[source_cell]
            source_edge = source_graph[1][source_chord_index]
            for target_cell, sign, _ in outgoing[source_cell]:
                target_graph = cyclic[target_cell]
                projected = {source_edge: sign} if source_edge in target_graph[1] else {}
                coordinates = quotient_coordinates(target_graph, projected)
                for local_index, coefficient in enumerate(coordinates):
                    row = target_index[(target_cell, target_graph[-1][local_index])]
                    matrix[row][column] += coefficient
        matrices[degree] = matrix

    # The induced maps must themselves form a complex.
    for degree in range(2, 5):
        product = multiply(matrices[degree - 1], matrices[degree])
        assert all(value == 0 for row in product for value in row)

    ranks = {degree: matrix_rank(matrices[degree]) for degree in range(1, 5)}
    homology = {}
    for degree in range(5):
        dimension = len(basis_by_degree[degree])
        outgoing_rank = ranks.get(degree, 0)
        incoming_rank = ranks.get(degree + 1, 0)
        homology[degree] = dimension - outgoing_rank - incoming_rank
        assert homology[degree] >= 0

    top_rref, top_pivots = rref_pivots(matrices[4])
    top_free = tuple(i for i in range(len(basis_by_degree[4])) if i not in top_pivots)
    empty_cell = ((), ())
    empty_columns = tuple(
        i for i, (cell, _) in enumerate(basis_by_degree[4]) if cell == empty_cell
    )
    assert len(empty_columns) == 5
    null_vectors = []
    for free_column in top_free:
        vector = [Fraction(0) for _ in basis_by_degree[4]]
        vector[free_column] = 1
        for row, pivot_column in enumerate(top_pivots):
            vector[pivot_column] = -top_rref[row][free_column]
        null_vectors.append(vector)
    empty_projection = [
        [vector[column] for vector in null_vectors] for column in empty_columns
    ]
    empty_projection_rank = matrix_rank(empty_projection)

    print("Cech_H1_carrier_chain_ranks: 0,4,32,72,49")
    print("Cech_H1_carrier_differential_ranks: " + ",".join(str(ranks[d]) for d in range(1, 5)))
    print("Cech_H1_carrier_homology_ranks: " + ",".join(str(homology[d]) for d in range(5)))
    print(f"distinct_loaded_carrier_arrows: {len(carrier_arrows)}")
    print("induced_carrier_d_squared: ZERO")
    print("rational_surviving_Cech_cycle_rank: " + str(sum(homology.values())))
    print(f"top_kernel_projection_to_empty_Wagner_rank: {empty_projection_rank}")
    print("next_gate: COMPUTE_INTEGRAL_SMITH_TORSION_AND_PHYSICAL_LINE_EDGE_MAP")


if __name__ == "__main__":
    main()
