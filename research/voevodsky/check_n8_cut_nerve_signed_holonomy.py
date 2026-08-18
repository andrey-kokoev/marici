"""Compute the Koszul sign holonomy of the physical octagon Cut nerve."""

from itertools import combinations, permutations

import check_n8_physical_cut_nerve_dimension as nerve
import check_n8_six_by_four_cut_boundary as polygon


N = 8


def normalized(a, b):
    return tuple(sorted((a % N, b % N)))


def edge(a, b):
    return frozenset((a, b))


def tree_path(first, second, parent):
    first_ancestors = []
    current = first
    while current is not None:
        first_ancestors.append(current)
        current = parent[current]
    second_ancestors = []
    current = second
    while current is not None:
        second_ancestors.append(current)
        current = parent[current]
    meet = next(v for v in first_ancestors if v in second_ancestors)
    return (
        first_ancestors[: first_ancestors.index(meet) + 1]
        + list(reversed(second_ancestors[: second_ancestors.index(meet)]))
    )


def main():
    nerve.main()

    vertices = tuple(sorted({normalized(i, i + 3) for i in range(N)}))
    edges = tuple(
        (a, b)
        for a, b in combinations(vertices, 2)
        if not polygon.crosses(a, b)
    )
    edge_set = {edge(a, b) for a, b in edges}
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)

    # Exhibit the graph as the eight-vertex Moebius ladder: an 8-cycle plus
    # the matching joining opposite vertices of that cycle.
    root = vertices[0]
    hamiltonian = None
    for tail in permutations(vertices[1:]):
        cycle = (root,) + tail
        if all(edge(cycle[i], cycle[(i + 1) % 8]) in edge_set for i in range(8)):
            rim = {edge(cycle[i], cycle[(i + 1) % 8]) for i in range(8)}
            spokes = edge_set - rim
            opposite = {edge(cycle[i], cycle[i + 4]) for i in range(4)}
            if spokes == opposite:
                hamiltonian = cycle
                break
    assert hamiltonian is not None

    # A deterministic spanning tree produces five fundamental cycles.
    parent = {root: None}
    queue = [root]
    for current in queue:
        for neighbor in sorted(adjacency[current]):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    tree_edges = {edge(v, p) for v, p in parent.items() if p is not None}
    chords = tuple(e for e in edges if edge(*e) not in tree_edges)
    assert len(chords) == 5

    cycle_lengths = []
    holonomies = []
    for first, second in chords:
        path = tree_path(first, second, parent)
        length = len(path)  # tree path has len(path)-1 edges, plus the chord
        cycle_lengths.append(length)
        holonomies.append((-1) ** length)
    assert tuple(cycle_lengths) == (5, 4, 5, 5, 4)
    assert tuple(holonomies) == (-1, 1, -1, -1, 1)

    # A constant -1 transition is a vertex-sign coboundary exactly when the
    # graph is bipartite. The displayed odd cycles prove that it is not.
    assert any(length % 2 for length in cycle_lengths)
    assert sum(h == -1 for h in holonomies) == 3

    print("physical_cut_compatibility_graph: EIGHT_VERTEX_MOEBIUS_LADDER")
    print("fundamental_cycle_basis_lengths: 5,4,5,5,4")
    print("Koszul_edge_sign: -1")
    print("cycle_basis_holonomies: -1,+1,-1,-1,+1")
    print("nontrivial_Z2_holonomy_generators: 3_OF_5")
    print("vertex_sign_trivialization: IMPOSSIBLE")
    print("global_Cut_descent_obstruction: NONZERO_Z2_CLASS")
    print("next_gate: IDENTIFY_OR_CONSTRUCT_COMPENSATING_ORIENTATION_LOCAL_SYSTEM")


if __name__ == "__main__":
    main()
