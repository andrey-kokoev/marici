import itertools
import json
from pathlib import Path


def connected(vertex_count, edges):
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == vertex_count


def degrees(vertex_count, edges):
    result = [0] * vertex_count
    for left, right in edges:
        result[left] += 1
        result[right] += 1
    return result


def mixed_distance(vertex_count, edges, anchor=0):
    unanchored = [v for v in range(vertex_count) if v != anchor]
    best = None
    for size in range(1, len(unanchored) + 1):
        for subset_tuple in itertools.combinations(unanchored, size):
            subset = set(subset_tuple)
            cut = sum((left in subset) != (right in subset)
                      for left, right in edges)
            weight = size + cut
            best = weight if best is None else min(best, weight)
    return best


def main():
    census = []
    for vertices in range(3, 6):
        possible = [(i, j) for i in range(vertices)
                    for j in range(i + 1, vertices)]
        connected_count = 0
        correcting_count = 0
        minimum_edges = None
        for mask in range(1 << len(possible)):
            edges = [edge for bit, edge in enumerate(possible)
                     if (mask >> bit) & 1]
            if not connected(vertices, edges):
                continue
            connected_count += 1
            distance = mixed_distance(vertices, edges)
            local_criterion = all(degree >= 2
                                  for degree in degrees(vertices, edges)[1:])
            assert (distance >= 3) == local_criterion
            if distance >= 3:
                correcting_count += 1
                minimum_edges = (len(edges) if minimum_edges is None
                                 else min(minimum_edges, len(edges)))
        assert minimum_edges == vertices
        census.append({
            "vertices": vertices,
            "connected_labelled_graphs": connected_count,
            "one_fault_correcting_graphs": correcting_count,
            "minimum_edges": minimum_edges,
        })

    for vertices in range(3, 8):
        cycle = [(i, i + 1) for i in range(vertices - 1)] + [(vertices - 1, 0)]
        assert len(cycle) == vertices
        assert mixed_distance(vertices, cycle) == 3

        path = [(i, i + 1) for i in range(vertices - 1)]
        assert mixed_distance(vertices, path) == 2

    # A cycle plus a dangling unanchored leaf has enough edges but distance two.
    dangling = [(0, 1), (1, 2), (2, 0), (2, 3)]
    assert len(dangling) == 4
    assert mixed_distance(4, dangling) == 2

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_one_joint_fault_graph_synthesis_theorem",
        "exhaustive_vertex_range": [3, 5],
        "census": census,
        "distance_three_criterion": "all_unanchored_degrees_at_least_2",
        "minimum_edges": "n",
        "minimum_cycle_rank": 1,
        "anchored_tree_distance": 2,
        "cycle_distance": 3,
        "edge_count_without_placement_sufficient": False,
        "dangling_leaf_hostile_distance": 2,
    }
    out = Path(__file__).parents[1] / "results" / "bell-reference-edge-minimum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
