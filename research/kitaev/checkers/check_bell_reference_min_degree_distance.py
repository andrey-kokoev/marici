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
    total_checked = 0
    for vertices in range(2, 7):
        possible = [(i, j) for i in range(vertices)
                    for j in range(i + 1, vertices)]
        connected_checked = 0
        distance_histogram = {}
        for mask in range(1 << len(possible)):
            edges = [edge for bit, edge in enumerate(possible)
                     if (mask >> bit) & 1]
            if not connected(vertices, edges):
                continue
            connected_checked += 1
            total_checked += 1
            minimum_unanchored_degree = min(degrees(vertices, edges)[1:])
            distance = mixed_distance(vertices, edges)
            assert distance == minimum_unanchored_degree + 1
            distance_histogram[str(distance)] = (
                distance_histogram.get(str(distance), 0) + 1)
        census.append({
            "vertices": vertices,
            "connected_graphs": connected_checked,
            "distance_histogram": distance_histogram,
        })

    for vertices in range(3, 9):
        complete = [(i, j) for i in range(vertices)
                    for j in range(i + 1, vertices)]
        assert mixed_distance(vertices, complete) == vertices
        cycle = [(i, i + 1) for i in range(vertices - 1)] + [(vertices - 1, 0)]
        assert mixed_distance(vertices, cycle) == 3

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_all_distance_simple_graph_code_theorem",
        "exhaustive_vertex_range": [2, 6],
        "connected_graphs_checked": total_checked,
        "census": census,
        "distance_formula": "1+minimum_unanchored_degree",
        "t_fault_criterion": "minimum_unanchored_degree>=2t",
        "complete_graph_distance": "n",
        "cycle_distance": 3,
        "prior_higher_t_insufficiency_statement": "falsified_and_repaired",
        "weighted_or_multigraph_extension_claimed": False,
    }
    out = Path(__file__).parents[1] / "results" / "bell-reference-min-degree-distance.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
