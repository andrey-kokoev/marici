#!/usr/bin/env python3
"""R(3,7) hypothetical 23-vertex graph: catalog-free four-local LP audit.

Requires: scipy, numpy. Run: python ramsey_r37_four_local_lp_audit.py

The mathematical reduction (see companion README):
 * Red graph has 23 vertices, triangle-free, independence number <=6.
 * Use R(3,6)=18, e(3,6,17)>=40, Mantel to force 6-regularity.
 * Fix root v, its red neighborhood A of size 6, its blue neighborhood B of size16.
 * Each b in B has a nonempty support T_b=N(b) ∩ A of size <=3.
 * Every a in A is in exactly five supports.
 * The number a_i of size-i supports satisfies (a1,a2,a3)=(2+t,14-2*t,t), t=0..4.

For each support multiset up to relabeling of A, we check necessary conditions
on red edges within B with variables x_ij relaxed to [0,1].
     x_ij=0 if T_i and T_j intersect (red triangle through A).
     sum_j x_ij = 6-|T_i| (red degree six).
     x_ij+x_ik+x_jk <= 2 (red triangles within B).
     sum_{ij subset F} x_ij >= 1 for F subset B_J, |F|=|J|+1,
         J subset A, 1<=|J|<=4. (The complement of J in A plus F cannot be independent.)
All these are necessary; infeasibility of the LP proves no integer coloring exists.

We use symmetry of singleton labels, and simple duplicate-support exclusions:
 * Two vertices with identical singleton support are impossible.
 * Pair support {i,j} appears at most once if either i or j has a singleton
   support, otherwise at most twice.
 * Triple support appears at most twice (when t>=3, it must contain a
   singleton label, and three copies plus that singleton and the rest of A give 7
   independent vertices; when t<=2, only <=2 copies exist anyway).

This script does not use the catalog of 22-vertex Ramsey graphs. It does rely
on e(3,6,17)>=40 (Graver--Yackel) and numerical HiGHS LP infeasibility statuses.
For machine-certified formal proof, rational dual/Farkas certificates are needed.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from time import perf_counter

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

A = range(6)
PAIRS = tuple(combinations(A, 2))
TRIPLES = tuple(combinations(A, 3))


def triple_orbits(t, singles):
    if t == 0:
        yield (), 1
        return
    lookup = {T: i for i, T in enumerate(TRIPLES)}
    perms = (p for p in permutations(A)
             if {p[i] for i in singles} == set(singles))
    transformations = [tuple(lookup[tuple(sorted(p[i] for i in T))] for T in TRIPLES)
                       for p in perms]
    remaining = {m for m in combinations_with_replacement(range(20), t)
                 if all(m.count(i) <= 2 for i in m)}
    while remaining:
        m = min(remaining)
        orbit = {tuple(sorted(p[i] for i in m)) for p in transformations}
        remaining.difference_update(orbit)
        yield tuple(TRIPLES[i] for i in m), len(orbit)


def pair_multisets(degrees, singles):
    """All permissible pair multisets with the specified six incidence degrees."""
    singles = set(singles)
    cap = tuple(1 if set(p) & singles else 2 for p in PAIRS)
    residual = list(degrees)
    selected = [0] * len(PAIRS)
    future = [[sum(cap[j] for j in range(i+1, len(PAIRS)) if a in PAIRS[j])
               for a in A] for i in range(len(PAIRS))]

    def rec(i):
        if i == len(PAIRS):
            if not any(residual):
                yield tuple(PAIRS[j] for j, z in enumerate(selected) for _ in range(z))
            return
        a, b = PAIRS[i]
        for z in range(min(cap[i], residual[a], residual[b]) + 1):
            selected[i] = z
            residual[a] -= z
            residual[b] -= z
            if all(0 <= residual[k] <= future[i][k] for k in A):
                yield from rec(i + 1)
            residual[a] += z
            residual[b] += z
        selected[i] = 0

    yield from rec(0)


def lp_feasible(supports, max_local_dimension=4):
    """Return (feasible, reason). All constraints are linear and NECESSARY."""
    assert len(supports) == 16
    masks = [sum(1 << a for a in T) for T in supports]
    edges = [(i, j) for i in range(16) for j in range(i+1, 16)
             if not masks[i] & masks[j]]
    pos = {edge: k for k, edge in enumerate(edges)}

    eq_rows, eq_rhs, ineq_rows, ineq_rhs = [], [], [], []
    for v, support in enumerate(supports):
        incident = [k for k, (i, j) in enumerate(edges) if i == v or j == v]
        needed = 6 - len(support)
        if len(incident) < needed:
            return False, 'degree capacity'
        eq_rows.append((incident, 1.0))
        eq_rhs.append(float(needed))

    # All-red triangles among B forbidden.
    for triple in combinations(range(16), 3):
        ps = list(combinations(triple, 2))
        if all(e in pos for e in ps):
            ineq_rows.append(([pos[e] for e in ps], 1.0))
            ineq_rhs.append(2.0)

    # For every J of size <=4, forbid independent (|J|+1)-sets in B_J.
    for J in range(1, 1 << 6):
        d = J.bit_count()
        if d > max_local_dimension:
            continue
        members = [i for i, m in enumerate(masks) if (m & ~J) == 0]
        for F in combinations(members, d + 1):
            keys = [pos[p] for p in combinations(F, 2) if p in pos]
            if not keys:
                return False, 'forced independent seven'
            ineq_rows.append((keys, -1.0))
            ineq_rhs.append(-1.0)

    def matrix(rows):
        ii, jj, vv = [], [], []
        for r, (keys, multiplier) in enumerate(rows):
            ii.extend([r] * len(keys))
            jj.extend(keys)
            vv.extend([multiplier] * len(keys))
        return coo_matrix((vv, (ii, jj)),
                          shape=(len(rows), len(edges))).tocsr()

    ans = linprog(np.zeros(len(edges)),
                  A_ub=matrix(ineq_rows), b_ub=np.array(ineq_rhs),
                  A_eq=matrix(eq_rows), b_eq=np.array(eq_rhs),
                  bounds=(0.0, 1.0), method='highs')
    if ans.status == 0:
        return True, 'feasible relaxation'
    if ans.status == 2:
        return False, 'LP infeasible'
    raise RuntimeError('LP did not settle: ' + ans.message)


def audit():
    start = perf_counter()
    expected = [79, 202, 483, 643, 554]
    total = Counter()
    for t in range(5):
        singles = tuple(range(t + 2))
        a2 = 14 - 2*t
        c = Counter()
        for triples, orbit_size in triple_orbits(t, singles):
            c['triple_orbits'] += 1
            desired = tuple(5 - int(a in singles)
                            - sum(a in T for T in triples) for a in A)
            if min(desired) < 0:
                continue
            for pairs in pair_multisets(desired, singles):
                assert len(pairs) == a2
                supports = tuple((i,) for i in singles) + pairs + triples
                assert len(supports) == 16
                assert all(sum(i in T for T in supports) == 5 for i in A)
                c['patterns'] += 1
                feasible, why = lp_feasible(supports)
                c[why] += 1
                if feasible:
                    raise AssertionError(f'Unexcluded support pattern: t={t}, '
                                         f'supports={supports}')
        assert c['patterns'] == expected[t], (t, c)
        print(f't={t}: {c["patterns"]} patterns; '
              f'{c["forced independent seven"]} direct contradictions, '
              f'{c["degree capacity"]} degree contradictions, '
              f'{c["LP infeasible"]} LP contradictions, '
              f'0 feasible; {c["triple_orbits"]} triple orbits')
        total.update(c)
    assert total['patterns'] == 1961
    print('All 1,961 support patterns excluded by at most 4-label conditions.')
    print('No 22-vertex graph catalogue was used.')
    print(f'Elapsed: {perf_counter()-start:.2f} seconds')


if __name__ == '__main__':
    audit()
