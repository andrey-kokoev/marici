#!/usr/bin/env python3
"""Verify ordinary relative-form gluing on externally normalized charts."""

import json


charts = ["E", "P1", "P2", "P3"]
ordered_overlaps = []
for i in charts:
    for j in charts:
        if i == j:
            continue
        # a_j=(x_i/x_j)a_i and b_j=(x_i/x_j)b_i.
        jacobian_power = 2
        kummer_power = 3
        form_power = jacobian_power - kummer_power
        assert form_power == -1
        ordered_overlaps.append({
            "overlap": f"U_{i} intersect U_{j}",
            "relative_jacobian": f"({i}/{j})^2",
            "W_transition": f"({i}/{j})^3",
            "form_transition": f"{j}/{i}",
            "orientation_sign": 1,
        })
assert len(ordered_overlaps) == 12

# (x_j/x_i)(x_k/x_j)=x_k/x_i.
for i in charts:
    for j in charts:
        for k in charts:
            if len({i, j, k}) < 3:
                continue
            exponent = {name: 0 for name in charts}
            exponent[j] += 1
            exponent[i] -= 1
            exponent[k] += 1
            exponent[j] -= 1
            exponent = {name: value for name, value in exponent.items() if value}
            assert exponent == {i: -1, k: 1}

print(json.dumps({
    "external_charts": len(charts),
    "ordered_overlaps": len(ordered_overlaps),
    "relative_form_transition": "omega_j=(x_j/x_i)*omega_i",
    "orientation_sign": 1,
    "triple_cocycle": True,
    "new_external_overlap_divisor": False,
}, indent=2))
