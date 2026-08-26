#!/usr/bin/env python3
"""Exact audit of the weighted augmented-mincut theorem."""

import hashlib
import json
from itertools import combinations, product
from pathlib import Path

from sympy import Rational


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/weighted-reference-augmented-mincut.json"


def nonempty_subsets(vertices):
    vertices = tuple(vertices)
    for size in range(1, len(vertices) + 1):
        yield from combinations(vertices, size)


def defining_distance(vertices, anchors, vertex_cost, edges):
    free = tuple(v for v in vertices if v not in anchors)
    values = []
    for subset in nonempty_subsets(free):
        chosen = set(subset)
        cost = sum((vertex_cost[v] for v in chosen), Rational(0))
        cost += sum((w for u, v, w in edges if (u in chosen) != (v in chosen)), Rational(0))
        values.append((cost, subset))
    return min(values)


def augmented_root_cut(vertices, anchors, vertex_cost, edges):
    # Enumerating root-complement cuts is independent of the fault expression:
    # first materialize the augmented edge list, then evaluate its cut capacity.
    root = "root"
    augmented = []
    for u, v, w in edges:
        uu = root if u in anchors else u
        vv = root if v in anchors else v
        if uu != vv:
            augmented.append((uu, vv, w))
    augmented.extend((root, v, vertex_cost[v]) for v in vertices if v not in anchors)
    free = tuple(v for v in vertices if v not in anchors)
    values = []
    for subset in nonempty_subsets(free):
        chosen = set(subset)
        cost = sum((w for u, v, w in augmented if (u in chosen) != (v in chosen)), Rational(0))
        values.append((cost, subset))
    return min(values)


def weighted_degree(v, edges):
    return sum((w for u, z, w in edges if u == v or z == v), Rational(0))


def main():
    exhaustive = 0
    # Three labelled vertices, vertex costs 1 or 2, and multiplicity/capacity
    # 0, 1, or 2 on each pair. Require connection to anchor 0.
    vertices = (0, 1, 2)
    anchors = {0}
    pairs = tuple(combinations(vertices, 2))
    for capacities in product(range(3), repeat=len(pairs)):
        edges = [(u, v, Rational(w)) for (u, v), w in zip(pairs, capacities) if w]
        reachable = {0}
        changed = True
        while changed:
            changed = False
            for u, v, _ in edges:
                if u in reachable and v not in reachable:
                    reachable.add(v); changed = True
                if v in reachable and u not in reachable:
                    reachable.add(u); changed = True
        if reachable != set(vertices):
            continue
        for costs in product((1, 2), repeat=2):
            alpha = {1: Rational(costs[0]), 2: Rational(costs[1])}
            direct = defining_distance(vertices, anchors, alpha, edges)
            augmented = augmented_root_cut(vertices, anchors, alpha, edges)
            assert direct == augmented
            exhaustive += 1

    # Simple unit graph specialization on every connected labelled graph n<=5.
    simple_checked = 0
    for n in range(2, 6):
        vs = tuple(range(n))
        ps = tuple(combinations(vs, 2))
        for mask in range(1 << len(ps)):
            edges = [(u, v, Rational(1)) for i, (u, v) in enumerate(ps) if mask & (1 << i)]
            reachable = {0}
            changed = True
            while changed:
                changed = False
                for u, v, _ in edges:
                    if u in reachable and v not in reachable:
                        reachable.add(v); changed = True
                    if v in reachable and u not in reachable:
                        reachable.add(u); changed = True
            if reachable != set(vs):
                continue
            alpha = {v: Rational(1) for v in vs if v != 0}
            distance, _ = defining_distance(vs, {0}, alpha, edges)
            delta = min(weighted_degree(v, edges) for v in vs if v != 0)
            assert distance == delta + 1
            simple_checked += 1

    hostile_edges = [
        (0, 1, Rational(1)), (0, 2, Rational(1)), (1, 2, Rational(5))
    ]
    hostile_alpha = {1: Rational(1), 2: Rational(1)}
    hostile_distance, hostile_set = defining_distance(vertices, anchors, hostile_alpha, hostile_edges)
    hostile_degree_formula = 1 + min(weighted_degree(v, hostile_edges) for v in (1, 2))
    assert hostile_distance == 4
    assert hostile_degree_formula == 7
    assert hostile_distance != hostile_degree_formula

    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = {
        "schema": "marici.kitaev.weighted_reference_augmented_mincut.v1",
        "status": "pass",
        "strength": "finite-cutoff theorem",
        "exact_arithmetic": "sympy.Rational",
        "weighted_multigraph_fixtures_checked": exhaustive,
        "connected_simple_graphs_checked": simple_checked,
        "hostile_parallel_edge_witness": {
            "vertices": 3,
            "anchors": [0],
            "minimizing_set": list(hostile_set),
            "actual_distance": str(hostile_distance),
            "degree_formula": str(hostile_degree_formula),
            "degree_formula_residual": str(hostile_degree_formula - hostile_distance),
        },
        "checker_sha256": digest,
        "scope_exclusions": [
            "correlated faults", "temporal faults", "hypergraphs",
            "quantum actuator repair", "physical interface cost"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
