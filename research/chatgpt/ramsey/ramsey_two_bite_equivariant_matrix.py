#!/usr/bin/env python3
"""Finite, deterministic two-layer Ramsey test prompted by Hefty--Horn--King--Pfender.

No asymptotic claim is made.  Base layers are triangle-free 13-cycles.
For the lifted layers, mixed-triangle deletion is performed by Boolean
square masks, precisely the paper's mixed-triangle deletion rule.

Requires scipy and numpy for mixed-integer independence-number optimization.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import isclose
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

MOD = 13
QUARTER = 5


def adjacency(labeled_vertices, step_coord, offsets):
    n = len(labeled_vertices)
    edges = set()
    for i in range(n):
        for j in range(i + 1, n):
            difference = (labeled_vertices[j][step_coord] - labeled_vertices[i][step_coord]) % MOD
            if difference in offsets:
                edges.add((i, j))
    return edges


def neighbors_from_edges(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    return adj


def triangle_count(n, edges):
    N = neighbors_from_edges(n, edges)
    return sum(len(N[i] & N[j] & set(range(j + 1, n)))
               for i in range(n) for j in N[i] if i < j)


def mixed_repair(n, red, blue):
    assert triangle_count(n, red) == 0
    assert triangle_count(n, blue) == 0
    NR = neighbors_from_edges(n, red)
    NB = neighbors_from_edges(n, blue)
    # An edge in one layer is removed if it closes a two-edge path in the other.
    repaired_red = {(i, j) for i, j in red if not (NB[i] & NB[j])}
    repaired_blue = {(i, j) for i, j in blue if not (NR[i] & NR[j])}
    final = repaired_red | repaired_blue
    assert triangle_count(n, final) == 0
    return final, repaired_red, repaired_blue


def independence_number(n, edges):
    constraints = lil_matrix((len(edges), n), dtype=np.float64)
    for row, (i, j) in enumerate(sorted(edges)):
        constraints[row, i] = 1
        constraints[row, j] = 1
    res = milp(
        c=-np.ones(n),
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(constraints.tocsr(), -np.inf, np.ones(len(edges))),
        options={'time_limit': 30.0, 'mip_rel_gap': 1e-10},
    )
    if res.status != 0 or res.mip_gap > 1e-8:
        raise RuntimeError(f'MIP did not finish: {res.message}; gap={res.mip_gap}')
    answer = round(-res.fun)
    assert isclose(-res.fun, answer, abs_tol=1e-5)
    assert isclose(-res.mip_dual_bound, answer, abs_tol=1e-5)
    chosen = {i for i, value in enumerate(res.x) if value > .5}
    assert len(chosen) == answer and all(i not in chosen or j not in chosen for i,j in edges)
    return answer


def build(shift_set):
    S = sorted(shift_set)
    vertices = [(a, (a + t) % MOD) for a in range(MOD) for t in S]
    n = len(vertices)
    red = adjacency(vertices, 0, {1, MOD-1})
    blue = adjacency(vertices, 1, {QUARTER, MOD-QUARTER})
    result, red_after, blue_after = mixed_repair(n, red, blue)
    lookup = {point: index for index, point in enumerate(vertices)}

    invariant = set((-QUARTER*t) % MOD for t in S) == set(S)
    if invariant:
        phase = [lookup[(QUARTER*b % MOD, QUARTER*a % MOD)] for a,b in vertices]
        def moved(edges):
            return {tuple(sorted((phase[i], phase[j]))) for i,j in edges}
        assert moved(red) == blue
        assert moved(blue) == red
        assert moved(red_after) == blue_after
        assert moved(blue_after) == red_after
        assert moved(result) == result
        assert all(phase[phase[phase[phase[i]]]] == i for i in range(n))
        assert all(phase[phase[i]] == lookup[(-a % MOD, -b % MOD)]
                   for i, (a,b) in enumerate(vertices))
    return dict(n=n, shifts=S, invariant=invariant, before=len(red | blue),
                after=len(result), alpha=independence_number(n, result),
                red=len(red_after), blue=len(blue_after))


def small_cycle_certificate():
    result = build({0})
    assert result['n'] == 13 and result['alpha'] == 4 and result['after'] == 26
    # Independently count independent sets to verify 13-vertex polynomial.
    vertices = [(a,a) for a in range(13)]
    E = adjacency(vertices, 0, {1,12}) | adjacency(vertices, 1, {5,8})
    counts = [0] * 14
    for mask in range(1 << 13):
        if all(not ((mask >> i & 1) and (mask >> j & 1)) for i, j in E):
            counts[mask.bit_count()] += 1
    assert counts[:5] == [1,13,52,78,39]
    assert counts[5:] == [0]*9
    print('13-vertex independence polynomial:', counts[:5])


def main():
    assert QUARTER**2 % MOD == MOD-1
    assert QUARTER**4 % MOD == 1
    small_cycle_certificate()
    examples = {
       'diagonal': {0},
       'quarter_orbit': {1,5,8,12},
       'quarter_orbit_with_center': {0,1,5,8,12},
       'five_consecutive_shifts': {0,1,2,3,4},
       'four_consecutive_shifts': {0,1,2,3},
       'two_quarter_orbits': {1,2,3,5,8,10,11,12},
    }
    print('name | n | edges before/after | alpha | quarter-turn invariant')
    results = {}
    for name, shifts in examples.items():
        result = build(shifts)
        results[name] = result
        print(f"{name} | {result['n']} | {result['before']}/{result['after']} | "
              f"{result['alpha']} | {result['invariant']}")
    assert results['quarter_orbit']['alpha'] == 14
    assert results['quarter_orbit_with_center']['alpha'] == 16
    assert results['five_consecutive_shifts']['alpha'] == 20
    assert results['four_consecutive_shifts']['alpha'] == 16
    assert results['two_quarter_orbits']['alpha'] == 26
    assert results['quarter_orbit_with_center']['after'] < results['five_consecutive_shifts']['after']
    assert results['quarter_orbit_with_center']['alpha'] < results['five_consecutive_shifts']['alpha']

if __name__ == '__main__':
    main()
