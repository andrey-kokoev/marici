#!/usr/bin/env python3
"""Local composition verification for the hypothetical 6-regular R(3,7,23) graph.

No LP/SAT solver or external certificate file required. Standard Python 3 only.

A and B colors are edges and nonedges of a triangle-free graph G with alpha(G)<=6.
Fix a vertex v of A-degree 6, let L=N_A(v) have six vertices, and let X have 16.
Each contact set C(x)=N_A(x) intersect L has size 1,2,3; each label occurs 5
 times, each singleton label occurs once, and each singleton must be in a triple.
The preceding analytic reductions exclude 2 or 3 singleton contacts.

Enumeration:
  4/5/6 singleton labels; 10/8/6 double contacts; 2/3/4 triple contacts.
  A repeated double is possible only on the nonsingleton pair {4,5}
  for s=4 (at most two copies). All other doubles form a simple graph.
  Double supports forming a triangle on singleton labels are excluded.
  Singleton closure excludes contacts violating |{x:C(x) subseteq D_i}|<=|D_i|.

Local constraints:
  Each pair with disjoint contacts is an eligible A-edge.
  Each exterior vertex has A-degree 6-|C(x)|.
  For each T of size <=5 with |union C(T)|<|T|, at least one eligible
  A-edge within T must be present. (Hall-deficient composition.)
  A-triangles are forbidden.

Propagation rules (sound, not necessarily complete):
  - A Hall-deficient T with no possible A-edge is a contradiction;
    with exactly one possible edge, force it A.
  - Two forced A-edges of a triangle force the third B.
  - Degree saturation forces the remaining A/B choices, or contradicts.

The only surviving system is the exceptional pattern:
 s_0..s_5; t_i={0} union ({1,2,3} minus {i}) for i=1,2,3;
 t_*={0,4,5}; doubles d_{i,q}={i,q} for i=1,2,3 and q=4,5.
 For P={s_1,s_2,s_3}, the sum of A-degrees is 15, but four disjoint
 classes of forced demands contribute at least 6+3+3+6=18:
   6: all A-edges s_i--s_q, i=1..3, q=4,5, from Hall triples;
   3: t_* must A-connect to all s_1,s_2,s_3 to have exterior degree 3;
   3: for each i, Hall on {s_0,s_i,t_1,t_2,t_3} forces
      A(s_0,s_i) or A(s_i,t_i);
   6: for each {i,j} subset {1,2,3} and q=4,5, Hall on
      {s_i,s_j,d_iq,d_jq} forces one of
      A(s_i,s_j), A(s_i,d_jq), A(s_j,d_iq). Summing these six
      inequalities yields >=6 P-degree incidences, because each
      A(s_i,s_j) occurs in two inequalities and counts twice in degrees.
 Contradiction: 18>15.

This finite verification is conditional on the analytic reductions above;
it does not by itself eliminate degree-5 vertices of G.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations

LABELS = range(6)
EDGES = list(combinations(LABELS, 2))
TRIPLES = list(combinations(LABELS, 3))


def triple_representatives(s):
    singleton_labels = set(range(s))
    hcount = s - 2
    action = [p + q for p in permutations(range(s))
              for q in permutations(range(s, 6))]
    seen = set()
    for H in combinations_with_replacement(TRIPLES, hcount):
        if not singleton_labels <= set().union(*map(set, H)):
            continue
        if H in seen:
            continue
        for perm in action:
            seen.add(tuple(sorted(tuple(sorted(perm[i] for i in tri))
                                  for tri in H)))
        yield H


def double_lookup():
    by_degrees = defaultdict(list)
    for mask in range(1 << len(EDGES)):
        B = [EDGES[j] for j in range(len(EDGES)) if mask & (1 << j)]
        deg = tuple(sum(i in e for e in B) for i in LABELS)
        by_degrees[deg].append(B)
    return by_degrees


def admissible_contact_systems():
    by_deg = double_lookup()
    for s in (4, 5, 6):
        singles = set(range(s))
        other = set(range(s, 6))
        for H in triple_representatives(s):
            target = tuple(5 - int(i in singles) - sum(i in h for h in H)
                           for i in LABELS)
            options = list(by_deg.get(target, []))
            if s == 4:
                target2 = tuple(target[i] - int(i in other) for i in LABELS)
                options += [B + [(4, 5)] for B in by_deg.get(target2, [])
                            if (4, 5) in B]
            for B in options:
                if len(B) != 18 - 2*s:
                    continue
                supports = set(B)
                if any((i, j) in supports and (i, k) in supports
                       and (j, k) in supports
                       for i, j, k in combinations(range(s), 3)):
                    continue
                C = [(i,) for i in range(s)] + list(H) + list(B)
                assert len(C) == 16
                assert all(sum(i in c for c in C) == 5 for i in LABELS)
                forbidden = False
                for i in range(s):
                    D = set().union(*(set(b) - {i} for b in B if i in b))
                    if sum(set(c) <= D for c in C) > len(D):
                        forbidden = True
                        break
                if not forbidden:
                    yield s, C


def local_propagation(C, max_hall_size=5):
    n = len(C)
    masks = [sum(1 << i for i in c) for c in C]
    eligible = [e for e in combinations(range(n), 2)
                if not (masks[e[0]] & masks[e[1]])]
    index = {edge: j for j, edge in enumerate(eligible)}

    hall_clauses = set()
    for k in range(2, max_hall_size+1):
        for T in combinations(range(n), k):
            union = 0
            for x in T:
                union |= masks[x]
            if union.bit_count() < k:
                hall_clauses.add(tuple(index[e] for e in combinations(T, 2)
                                       if e in index))

    hall_clauses = sorted(hall_clauses)

    triangles = [tuple(index[e] for e in combinations(T, 2))
                 for T in combinations(range(n), 3)
                 if all(e in index for e in combinations(T, 2))]
    incident = [[index[e] for e in eligible if x in e] for x in range(n)]
    need = [6 - len(c) for c in C]
    state = [-1] * len(eligible)  # -1 unknown, 0 B, 1 A

    while True:
        changed = False
        for clause in hall_clauses:
            if any(state[j] == 1 for j in clause):
                continue
            undecided = [j for j in clause if state[j] == -1]
            if not undecided:
                return 'Hall'
            if len(undecided) == 1:
                state[undecided[0]] = 1
                changed = True

        for tri in triangles:
            countA = sum(state[j] == 1 for j in tri)
            if countA == 3:
                return 'triangle'
            if countA == 2:
                for j in tri:
                    if state[j] == -1:
                        state[j] = 0
                        changed = True

        for x, edges in enumerate(incident):
            currentA = sum(state[j] == 1 for j in edges)
            undecided = [j for j in edges if state[j] == -1]
            if currentA > need[x] or currentA + len(undecided) < need[x]:
                return 'degree'
            if undecided and currentA == need[x]:
                for j in undecided:
                    state[j] = 0
                changed = True
            elif undecided and currentA + len(undecided) == need[x]:
                for j in undecided:
                    state[j] = 1
                changed = True

        if not changed:
            return 'survived'


def exceptional_capacity_contradiction(C):
    """Check the 15-clause degree-capacity certificate directly."""
    actual = Counter(map(frozenset, C))
    P = (1, 2, 3)
    Q = (4, 5)
    expected = Counter([frozenset([i]) for i in range(6)] +
                       [frozenset([0] + [j for j in P if j != i])
                        for i in P] +
                       [frozenset([0, 4, 5])] +
                       [frozenset([i, j]) for i in P for j in Q])
    assert actual == expected
    pos = {frozenset(contact): k for k, contact in enumerate(C)}
    def ss(i): return pos[frozenset([i])]
    def tt(i): return pos[frozenset([0] + [j for j in P if j != i])]
    def dd(i, q): return pos[frozenset([i, q])]
    star = pos[frozenset([0, 4, 5])]
    U = {ss(i) for i in P}
    clauses = []
    for i in P:
        for q in Q:
            clauses.append((ss(i), ss(q), dd(i, q)))
    for i in P:
        clauses.append((ss(0), ss(i), *(tt(j) for j in P)))
    for i, j in combinations(P, 2):
        for q in Q:
            clauses.append((ss(i), ss(j), dd(i, q), dd(j, q)))
    edge_counts = Counter()
    for T in clauses:
        labels = set().union(*(set(C[x]) for x in T))
        assert len(labels) < len(T)
        choices = [tuple(sorted((u, v))) for u, v in combinations(T, 2)
                   if not set(C[u]) & set(C[v])]
        assert choices
        edge_counts.update(choices)
    assert all(mult <= sum(x in U for x in edge)
               for edge, mult in edge_counts.items())
    assert len(clauses) == 15
    eligible_star = {x for x in range(len(C)) if x != star
                     and not set(C[star]) & set(C[x])}
    assert eligible_star == U and 6 - len(C[star]) == len(U) == 3
    assert all(tuple(sorted((star, u))) not in edge_counts for u in U)
    budget = sum(6 - len(C[x]) for x in U)
    demand = len(clauses) + len(U)
    assert budget == 15 and demand == 18
    return demand > budget


def main():
    count = Counter()
    for s, C in admissible_contact_systems():
        result = local_propagation(C)
        if result == 'survived':
            assert exceptional_capacity_contradiction(C)
            result = 'exceptional_capacity'
        count[(s, result)] += 1
    assert sum(count.values()) == 478, count
    assert [sum(num for (ss, _), num in count.items() if ss == s)
            for s in (4, 5, 6)] == [78, 113, 287]
    assert count[(6, 'exceptional_capacity')] == 1
    assert sum(num for (s, kind), num in count.items() if kind != 'exceptional_capacity') == 477
    print('All 478 contact systems excluded by local composition + one capacity lemma.')
    print('Branch counts:', {s: {kind: num for (ss, kind), num in count.items() if ss == s}
                             for s in (4, 5, 6)})
    print('Only exceptional system: s0..s5, t_i={0}∪({1,2,3}\\{i}), t*={0,4,5},'
          ' d_iq={i,q} (i=1,2,3; q=4,5).')
    print('Exceptional capacity contradiction: 18 required degree-incidences > 15 available.')


if __name__ == '__main__':
    main()
