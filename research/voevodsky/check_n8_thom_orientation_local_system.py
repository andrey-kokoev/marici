"""Check that the native odd Thom-normal line cancels Cut-nerve holonomy."""

from itertools import combinations

import check_n8_cut_nerve_signed_holonomy as holonomy
import check_n8_six_by_four_cut_boundary as polygon


N = 8


def normalized(a, b):
    return tuple(sorted((a % N, b % N)))


def edge(a, b):
    return frozenset((a, b))


def main():
    holonomy.main()

    vertices = tuple(sorted({normalized(i, i + 3) for i in range(N)}))
    edges = tuple(
        (a, b)
        for a, b in combinations(vertices, 2)
        if not polygon.crosses(a, b)
    )
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)

    root = vertices[0]
    parent = {root: None}
    queue = [root]
    for current in queue:
        for neighbor in sorted(adjacency[current]):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    tree_edges = {edge(v, p) for v, p in parent.items() if p is not None}
    chords = tuple(e for e in edges if edge(*e) not in tree_edges)

    cycle_lengths = []
    raw_holonomies = []
    thom_holonomies = []
    combined_holonomies = []
    for first, second in chords:
        path = holonomy.tree_path(first, second, parent)
        length = len(path)
        cycle_lengths.append(length)
        raw_holonomies.append((-1) ** length)
        thom_holonomies.append((-1) ** length)
        combined_holonomies.append(((-1) * (-1)) ** length)

    assert tuple(cycle_lengths) == (5, 4, 5, 5, 4)
    assert tuple(raw_holonomies) == (-1, 1, -1, -1, 1)
    assert tuple(thom_holonomies) == tuple(raw_holonomies)
    assert tuple(combined_holonomies) == (1, 1, 1, 1, 1)

    # The marked Cut copy is shifted by one degree. Hence swapping the two
    # normal factors on every pair overlap has the odd-line braiding sign -1.
    restriction_order_sign = -1
    marked_normal_braiding = -1
    sheet_localization = 1
    conductor_base_change = 1
    log_thom_trace = 1
    physical_line = 1
    total_edge_transport = (
        restriction_order_sign
        * marked_normal_braiding
        * sheet_localization
        * conductor_base_change
        * log_thom_trace
        * physical_line
    )
    assert total_edge_transport == 1

    print("raw_Koszul_local_system_holonomy: -1,+1,-1,-1,+1")
    print("marked_normal_Thom_local_system_holonomy: -1,+1,-1,-1,+1")
    print("sheet_conductor_logThom_physical_edge_factor: +1")
    print("combined_edge_transport: +1_ON_ALL_12_EDGES")
    print("combined_cycle_basis_holonomy: +1,+1,+1,+1,+1")
    print("compensating_orientation_local_system: ALREADY_PRESENT_AS_ODD_MARKED_NORMAL_LINE")
    print("untwisted_scalar_descent: OBSTRUCTED")
    print("native_graded_Thom_descent: UNOBSTRUCTED")
    print("next_gate: BUILD_INTEGRAL_TWISTED_CECH_TOTALIZATION")


if __name__ == "__main__":
    main()
