from fractions import Fraction
import json

g = [Fraction(1), Fraction(-1), Fraction(0)]
d = len(g)
augmentation = sum(g)

edges = []
for i in range(d):
    for j in range(i + 1, d):
        edges.append((i, j, g[j] - g[i]))

edge_energy = sum(value * value for _, _, value in edges)
vertex_energy = sum(value * value for value in g)

# Adjoint incidence with the convention delta(g)_{ij}=g_j-g_i.
laplacian_g = [Fraction(0) for _ in range(d)]
for i, j, value in edges:
    laplacian_g[i] -= value
    laplacian_g[j] += value

checks = {
    "scalar_augmentation_vanishes": augmentation == 0,
    "edge_current_is_nonzero": edge_energy > 0,
    "gram_identity_exact": edge_energy == d * vertex_energy - augmentation**2,
    "laplacian_recovers_scalar_null_state": laplacian_g == [d * x for x in g],
    "left_inverse_exact": [x / d for x in laplacian_g] == g,
}

out = {
    "schema": "marici.grothendieck.complete-graph-seam-coboundary.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "g": [str(x) for x in g],
        "edges": [[i, j, str(value)] for i, j, value in edges],
        "edge_energy": str(edge_energy),
        "vertex_energy": str(vertex_energy),
        "laplacian_g": [str(x) for x in laplacian_g],
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

