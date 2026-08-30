import json
from pathlib import Path


h1 = (1, -1, 0)
h2 = (0, 1, -1)


def root_weight(i, j):
    return (h1[i] - h1[j], h2[i] - h2[j])


roots = {(i, j): root_weight(i, j) for i in range(3) for j in range(3) if i != j}
root_values = set(roots.values())
assert len(roots) == 6
assert len(root_values) == 6
assert all((-a, -b) in root_values for a, b in root_values)

positive_roots = {
    root_weight(0, 1),
    root_weight(1, 2),
    root_weight(0, 2),
}
assert root_weight(0, 2) == tuple(
    x + y for x, y in zip(root_weight(0, 1), root_weight(1, 2))
)
assert len(positive_roots) == 3
assert 2 + len(root_values) == 8

# Label almost-positive roots abstractly. Their A2 compatibility graph is a
# five-cycle; vertices are cluster variables, and adjacent pairs are clusters.
almost_positive = ["-a1", "a2", "a1+a2", "a1", "-a2"]
edges = {
    frozenset((almost_positive[i], almost_positive[(i + 1) % 5]))
    for i in range(5)
}
degree = {vertex: 0 for vertex in almost_positive}
for edge in edges:
    for vertex in edge:
        degree[vertex] += 1
assert len(almost_positive) == 5
assert len(edges) == 5
assert set(degree.values()) == {2}

result = {
    "lie_algebra": "sl3",
    "root_system": "A2",
    "cartan_dimension": 2,
    "root_space_count": len(root_values),
    "positive_root_count": len(positive_roots),
    "lie_dimension": 2 + len(root_values),
    "standard_plus_dual_dimension": 6,
    "almost_positive_root_count": len(almost_positive),
    "a2_exchange_graph": "five-cycle",
    "unlabelled_exchange_automorphism_group": "D5",
    "source_cluster_mutations_constructed": False,
    "orientation_implied": False,
    "root_weights": {
        f"E{i + 1}{j + 1}": list(weight)
        for (i, j), weight in sorted(roots.items())
    },
    "verdict": "the finite operator algebra is type A2; its canonical coherence shadow is pentagonal, but source mutations remain unconstructed",
}

out = Path(__file__).parents[1] / "results" / "rh-a2-root-and-pentagon-census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
