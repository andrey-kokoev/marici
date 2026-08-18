"""Determine the full compatibility nerve of the eight physical octagon Cuts."""

from collections import Counter
from itertools import combinations

import check_n8_codimension_two_cut_coherence as codim2
import check_n8_six_by_four_cut_boundary as polygon


N = 8


def normalized(a, b):
    return tuple(sorted((a % N, b % N)))


def pairwise_compatible(cuts):
    return all(not polygon.crosses(a, b) for a, b in combinations(cuts, 2))


def main():
    codim2.main()

    physical = tuple(sorted({normalized(i, i + 3) for i in range(N)}))
    compatible_pairs = tuple(p for p in combinations(physical, 2) if pairwise_compatible(p))
    compatible_triples = tuple(t for t in combinations(physical, 3) if pairwise_compatible(t))

    assert len(physical) == 8
    assert len(compatible_pairs) == 12
    assert compatible_triples == ()

    degrees = Counter(cut for pair in compatible_pairs for cut in pair)
    assert set(degrees.values()) == {3}
    assert sum(degrees.values()) == 24 == 2 * len(compatible_pairs)

    # The compatibility nerve is therefore a connected cubic graph with only
    # vertices and edges. Its first Betti number is E - V + 1 = 5.
    adjacency = {cut: set() for cut in physical}
    for a, b in compatible_pairs:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {physical[0]}
    frontier = [physical[0]]
    while frontier:
        current = frontier.pop()
        for neighbor in adjacency[current] - seen:
            seen.add(neighbor)
            frontier.append(neighbor)
    assert seen == set(physical)
    assert len(compatible_pairs) - len(physical) + 1 == 5

    print("physical_cut_nerve_f_vector: 8,12")
    print("physical_cut_nerve_vertex_degrees: 3_EACH")
    print("compatible_physical_cut_triples: 0")
    print("physical_cut_nerve_dimension: 1")
    print("physical_cut_nerve_first_betti_number: 5")
    print("codimension_three_local_Cut_coherence: VACUOUS")
    print("next_nontrivial_coherence_test: GRAPH_CYCLE_HOLONOMY")


if __name__ == "__main__":
    main()
