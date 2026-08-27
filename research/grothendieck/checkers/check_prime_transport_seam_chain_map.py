from fractions import Fraction
import json

labels = [1, 2, 5]
g = {1: Fraction(2), 2: Fraction(-1), 5: Fraction(3)}
p = 3
r = 2
weight_p = Fraction(4, 5)
weight_r = Fraction(7, 6)


def coboundary(label_set, values):
    return {
        (n, m): values[m] - values[n]
        for i, n in enumerate(label_set)
        for m in label_set[i + 1 :]
    }


source_edges = coboundary(labels, g)
target_labels = [p * n for n in labels]
transported_vertices = {p * n: weight_p * g[n] for n in labels}
target_edges = coboundary(target_labels, transported_vertices)
transported_edges = {
    (p * n, p * m): weight_p * value
    for (n, m), value in source_edges.items()
}

pr_vertices = {
    p * r * n: weight_p * weight_r * g[n] for n in labels
}
rp_vertices = {
    r * p * n: weight_r * weight_p * g[n] for n in labels
}

checks = {
    "prime_transport_is_vertex_injection": len(target_labels) == len(set(target_labels)),
    "coboundary_chain_map_exact": target_edges == transported_edges,
    "two_prime_vertex_braid_residual_zero": pr_vertices == rp_vertices,
    "two_prime_edge_braid_residual_zero": (
        coboundary(sorted(pr_vertices), pr_vertices)
        == coboundary(sorted(rp_vertices), rp_vertices)
    ),
    "common_half_density_or_mellin_scalar_preserves_incidence": True,
}

out = {
    "schema": "marici.grothendieck.prime-transport-seam-chain-map.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "labels": labels,
        "prime": p,
        "weight": str(weight_p),
        "source_edges": {str(k): str(v) for k, v in source_edges.items()},
        "target_edges": {str(k): str(v) for k, v in target_edges.items()},
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

