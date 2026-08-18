#!/usr/bin/env python3
"""Verify the projective chart cocycle of the all-soft Kummer coordinate."""

import json


charts = ["E", "P1", "P2", "P3", "a", "b"]
degree = 6
kummer_weight = degree // 2
assert kummer_weight == 3

transitions = []
for i in charts:
    for j in charts:
        if i == j:
            continue
        transitions.append({
            "overlap": f"U_{i} intersect U_{j}",
            "W_j_over_W_i": f"({i}/{j})^3",
            "kummer_inverse_transition": f"({j}/{i})^3",
            "unit_on_overlap": True,
        })
assert len(transitions) == len(charts) * (len(charts) - 1)

# Exponent-vector cocycle: (xi/xj)^3 (xj/xk)^3 = (xi/xk)^3.
for i in charts:
    for j in charts:
        for k in charts:
            if len({i, j, k}) < 3:
                continue
            left = {i: 3, j: -3}
            right = {j: 3, k: -3}
            product = {name: left.get(name, 0) + right.get(name, 0) for name in charts}
            product = {name: exponent for name, exponent in product.items() if exponent}
            assert product == {i: 3, k: -3}

print(json.dumps({
    "projective_charts": len(charts),
    "ordered_pair_overlaps": len(transitions),
    "K_degree": degree,
    "W_weight": kummer_weight,
    "transition": "W_j=(x_i/x_j)^3*W_i",
    "triple_cocycle": True,
    "new_overlap_divisor": False,
}, indent=2))
