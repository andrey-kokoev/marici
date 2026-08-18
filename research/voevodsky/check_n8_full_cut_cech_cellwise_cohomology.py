"""Compute the cellwise Cech cohomology of the eight loaded Cut charts."""

from collections import Counter, defaultdict
from itertools import combinations

import check_n8_full_twisted_cut_cech_lift as full
import check_n8_six_by_four_cut_boundary as polygon


def components(vertices, edges):
    remaining = set(vertices)
    count = 0
    while remaining:
        count += 1
        stack = [remaining.pop()]
        while stack:
            vertex = stack.pop()
            neighbors = {
                b if a == vertex else a
                for a, b in edges
                if a == vertex or b == vertex
            }
            fresh = neighbors & remaining
            remaining -= fresh
            stack.extend(fresh)
    return count


def main():
    all_diagonals = polygon.diagonals(full.N)
    cuts = tuple(sorted({full.normalized(i, i + 3) for i in range(full.N)}))
    cut_edges = tuple(
        (a, b) for a, b in combinations(cuts, 2) if not polygon.crosses(a, b)
    )

    charts = {}
    occurrences = defaultdict(set)
    for cut in cuts:
        link = tuple(
            d for d in all_diagonals if d != cut and not polygon.crosses(d, cut)
        )
        cells = set(full.loaded_cells(link))
        assert len(cells) == 1075
        charts[cut] = cells
        for cell in cells:
            occurrences[cell].add(cut)

    h0_by_degree = Counter()
    h1_by_degree = Counter()
    labels_by_degree = Counter()
    graph_types = Counter()
    disconnected = []
    cyclic = []

    for cell, vertices in occurrences.items():
        face, marked = cell
        degree = full.DIMENSION - len(face) + len(marked)
        edges = tuple((a, b) for a, b in cut_edges if a in vertices and b in vertices)
        component_count = components(vertices, edges)
        beta = len(edges) - len(vertices) + component_count
        assert beta >= 0
        labels_by_degree[degree] += 1
        h0_by_degree[degree] += component_count
        h1_by_degree[degree] += beta
        graph_types[(len(vertices), len(edges), component_count, beta)] += 1
        if component_count > 1:
            disconnected.append((cell, vertices, edges))
        if beta:
            cyclic.append((cell, vertices, edges, beta))

    # Direct sums over labels reproduce the full Cech module ranks.
    chart_rank = sum(len(vertices) for vertices in occurrences.values())
    edge_rank = sum(
        sum(a in vertices and b in vertices for a, b in cut_edges)
        for vertices in occurrences.values()
    )
    assert (chart_rank, edge_rank) == (8600, 1500)
    assert sum(h0_by_degree.values()) - sum(h1_by_degree.values()) == chart_rank - edge_rank

    print(f"unique_loaded_cell_labels: {len(occurrences)}")
    print("labels_by_chain_degree: " + ",".join(str(labels_by_degree[d]) for d in range(5)))
    print("cellwise_Cech_H0_by_degree: " + ",".join(str(h0_by_degree[d]) for d in range(5)))
    print("cellwise_Cech_H1_by_degree: " + ",".join(str(h1_by_degree[d]) for d in range(5)))
    print(f"cellwise_Cech_H1_total_rank: {sum(h1_by_degree.values())}")
    print(f"cyclic_cell_labels: {len(cyclic)}")
    print(f"disconnected_cell_labels: {len(disconnected)}")
    print(f"excess_H0_component_rank: {sum(h0_by_degree.values()) - len(occurrences)}")
    print("integral_Cech_torsion: NONE_GRAPH_INCIDENCE")
    for graph_type, multiplicity in sorted(graph_types.items()):
        print(f"graph_type_V_E_C_B={graph_type}: {multiplicity}")
    print("physical_section_uniqueness_from_Cech_alone: NO")
    print("next_gate: COMPUTE_CARRIER_DIFFERENTIAL_ON_CELLWISE_H1")


if __name__ == "__main__":
    main()
