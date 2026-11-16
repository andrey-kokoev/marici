#!/usr/bin/env python3
"""Exact, solver-free capacity/composition audit for the (3,7,23) support system.

Conditional prerequisite: any counterexample would be 6-regular. The
regularity deduction uses the known lower bound e(3,6,17) >= 40.

No fractional programming, fitted graph model, cycle condition, or phase choice.
The 695 cases are support-multiset isomorphism classes, not graphs.
This script enumerates classes and applies sound necessary conditions only.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

DIRECTIONS = range(6)
PAIRS = tuple(combinations(DIRECTIONS, 2))
TRIPLES = tuple(combinations(DIRECTIONS, 3))
PAIR_MASKS = tuple((1 << a) | (1 << b) for a, b in PAIRS)
TRIPLE_MASKS = tuple(sum(1 << a for a in x) for x in TRIPLES)
EXPECTED_LABELLED = (79, 922, 6028, 27690, 103975)


def relabel(mask, permutation):
    return sum(1 << permutation[i] for i in DIRECTIONS if mask >> i & 1)


def stabilizing_permutations(r):
    k = r + 2
    return [a + b for a in permutations(range(k))
                  for b in permutations(range(k, 6))]


def pair_multisets(needed, singleton_sites):
    caps = tuple(1 if a in singleton_sites or b in singleton_sites else 2
                 for a, b in PAIRS)
    remains = list(needed)
    counts = [0] * 15

    def visit(j):
        if j == 15:
            if not any(remains):
                yield tuple(counts)
            return
        a, b = PAIRS[j]
        for count in range(min(caps[j], remains[a], remains[b]) + 1):
            remains[a] -= count
            remains[b] -= count
            counts[j] = count
            if all(remains[i] <= sum(caps[l] for l in range(j + 1, 15)
                                     if i in PAIRS[l]) for i in DIRECTIONS):
                yield from visit(j + 1)
            remains[a] += count
            remains[b] += count
    yield from visit(0)


def support_classes(r):
    """Canonical representatives with r triple support occurrences.

    There are 2+r singleton supports and 14-2r pair supports. Singleton
    directions are relabelled to 0..r+1. Pair repetition caps follow from
    the three-vertex independence-capacity rule, not an added assumption.
    """
    perm = stabilizing_permutations(r)
    singles = set(range(r+2))
    todo = {tuple(sorted(x)) for x in
            combinations_with_replacement(TRIPLE_MASKS, r)}
    classes = set()
    while todo:
        triples = min(todo)
        todo.difference_update({tuple(sorted(relabel(x, p) for x in triples))
                                for p in perm})
        stab = [p for p in perm
                if tuple(sorted(relabel(x, p) for x in triples)) == triples]
        needed = [5 - (i in singles) - sum((x >> i) & 1 for x in triples)
                  for i in DIRECTIONS]
        if min(needed) < 0:
            continue
        seen_pairs = set()
        for counts in pair_multisets(needed, singles):
            pairs = tuple(sorted(mask for mask, count in zip(PAIR_MASKS, counts)
                                 for _ in range(count)))
            if pairs in seen_pairs:
                continue
            seen_pairs.update(tuple(sorted(relabel(x, p) for x in pairs))
                              for p in stab)
            support = tuple(sorted([1 << i for i in singles] + list(pairs)
                                   + list(triples)))
            assert len(support) == 16
            assert all(sum((x >> i) & 1 for x in support) == 5
                       for i in DIRECTIONS)
            classes.add(support)
    return sorted(classes)


def label_orbit_size(support, r):
    return len({tuple(sorted(relabel(x, p) for x in support))
                for p in stabilizing_permutations(r)})


def constraints(support):
    """Allowed edges, deficient-set clauses, triangle clauses, exact degrees."""
    edges = tuple((i, j) for i, j in combinations(range(16), 2)
                  if not (support[i] & support[j]))
    lookup = {e: j for j, e in enumerate(edges)}
    degrees = [[] for _ in support]
    for j, (a, b) in enumerate(edges):
        degrees[a].append(j)
        degrees[b].append(j)
    need = tuple(6-x.bit_count() for x in support)
    hall = []
    for size in (2, 3, 4, 5):
        for U in combinations(range(16), size):
            union = 0
            for i in U:
                union |= support[i]
            if union.bit_count() < size:
                hall.append((U, tuple(lookup[e] for e in combinations(U, 2)
                                      if e in lookup)))
    triangles = [(U, tuple(lookup[e] for e in combinations(U, 2)))
                 for U in combinations(range(16), 3)
                 if all(e in lookup for e in combinations(U, 2))]
    return edges, degrees, need, hall, triangles


def propagate(data, seed=()):
    """Sound unit propagation. Values -1/0/1 mean undetermined/blue/red."""
    edges, degrees, need, hall, triangles = data
    assigned = [-1]*len(edges)
    for index, value in seed:
        assert value in (0, 1) and assigned[index] < 0
        assigned[index] = value
    while True:
        changed = {}
        def force(j, v):
            if assigned[j] != -1:
                return assigned[j] == v
            if j in changed and changed[j] != v:
                return False
            changed[j] = v
            return True
        for i, incident in enumerate(degrees):
            ones = sum(assigned[e] == 1 for e in incident)
            unknown = [e for e in incident if assigned[e] == -1]
            if ones > need[i] or ones + len(unknown) < need[i]:
                return 'degree', assigned
            if ones == need[i]:
                for e in unknown:
                    if not force(e, 0):return 'incompatible-forces', assigned
            if ones + len(unknown) == need[i]:
                for e in unknown:
                    if not force(e, 1):return 'incompatible-forces', assigned
        for U, inside in hall:
            if not any(assigned[e] == 1 for e in inside):
                possible = [e for e in inside if assigned[e] == -1]
                if not possible:return 'capacity', assigned
                if len(possible) == 1 and not force(possible[0], 1):
                    return 'incompatible-forces', assigned
        for U, inside in triangles:
            ones = sum(assigned[e] == 1 for e in inside)
            if ones == 3:return 'triangle', assigned
            if ones == 2:
                for e in inside:
                    if assigned[e] == -1 and not force(e, 0):
                        return 'incompatible-forces', assigned
        if not changed:
            return 'open', assigned
        for j, v in changed.items():assigned[j] = v


def verify():
    totals = Counter()
    by_profile = []
    exceptions = []
    for r in range(5):
        reps = support_classes(r)
        labelled = sum(label_orbit_size(s, r) for s in reps)
        assert labelled == EXPECTED_LABELLED[r]
        tally = Counter()
        for s in reps:
            d = constraints(s)
            status, state = propagate(d)
            tally[status] += 1
            totals[status] += 1
            if status == 'open':
                exceptions.append((r, s, d, state))
        by_profile.append((r, len(reps), labelled, dict(tally)))
    assert sum(totals.values()) == 695
    assert totals['open'] == len(exceptions) == 1
    assert sum(count for key, count in totals.items() if key != 'open') == 694
    # Every assignment chooses one edge in the ONE remaining class; the chosen
    # edge has both branches refuted by the same sound propagation procedure.
    r, supports, data, state = exceptions[0]
    edges = data[0]
    splits = []
    for j, edge in enumerate(edges):
        if state[j] == -1:
            negative = propagate(data, ((j, 0),))[0]
            positive = propagate(data, ((j, 1),))[0]
            if negative != 'open' and positive != 'open':
                splits.append((edge, negative, positive))
    assert splits
    print('PROFILE/CASES/ORBIT-WEIGHT/RESOLUTION:')
    for row in by_profile:print(*row)
    print('ALL:',dict(totals))
    print('EXCEPTIONAL SUPPORTS:',supports)
    print('BOTH-BRANCH REFUTATION:',splits[0])
    print('CERTIFIED: 694 unit-resolution contradictions, 1 two-branch contradiction.')
    print('No LP/SAT solver, graph-isomorphism package, or Ramsey oracle used.')

if __name__ == '__main__':
    verify()
