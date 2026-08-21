#!/usr/bin/env python3
"""Exact invariant-scalar audit for the standard D3 memory plane."""

import json
from pathlib import Path


r = ((0, -1), (1, -1))
s = ((1, 0), (1, -1))


def act(matrix, point):
    a, b = point
    return (
        matrix[0][0] * a + matrix[0][1] * b,
        matrix[1][0] * a + matrix[1][1] * b,
    )


def compose(g, h):
    return tuple(tuple(sum(g[i][k] * h[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


identity = ((1, 0), (0, 1))
elements = set()
rk = identity
for _ in range(3):
    elements.add(rk)
    elements.add(compose(s, rk))
    rk = compose(r, rk)
assert len(elements) == 6


def q2(point):
    a, b = point
    return a * a - a * b + b * b


def q3(point):
    a, b = point
    return a * b * (a - b)


checks = 0
for a in range(-12, 13):
    for b in range(-12, 13):
        point = (a, b)
        for g in elements:
            image = act(g, point)
            assert q2(image) == q2(point)
            assert q3(image) == q3(point)
            checks += 2

# The pair separates every orbit on the bounded exact control grid.
points = [(a, b) for a in range(-12, 13) for b in range(-12, 13)]
unseen = set(points)
orbit_count = 0
while unseen:
    point = next(iter(unseen))
    orbit = {act(g, point) for g in elements}
    within = orbit & set(points)
    key = (q2(point), q3(point))
    same_key = {p for p in points if (q2(p), q3(p)) == key}
    assert same_key == within
    unseen -= within
    orbit_count += 1

result = {
    "schema": "marici.nima.radiative_memory_d3_invariants.v1",
    "representation": "rank-two standard D3 memory-difference plane",
    "quadratic_generator": "q2=a^2-a*b+b^2",
    "cubic_generator": "q3=a*b*(a-b)",
    "invariant_ring": "Q[a,b]^D3 = Q[q2,q3]",
    "exact_invariance_checks": checks,
    "bounded_grid": "[-12,12]^2",
    "bounded_orbit_count": orbit_count,
    "bounded_orbits_separated": True,
    "passed": True,
}
out = Path(__file__).with_name("results") / "radiative-memory-d3-invariants.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
