"""Exact Ramsey circuit-closure proof (Python standard library only).

Every Hall circuit of T-supports requires an A-edge. An A-edge can connect
only disjoint supports. Mandatory edges propagate through:
  (i) circuit demand, (ii) triangle avoidance, (iii) vertex degree budget.
A final local packing (two-terminal bottleneck) excludes two residual cases.

For R(3,6) on 17 vertices the computation runs conditional on the negation of
our theorem: no B-pair has >= 3 common A-neighbors. Exhaustive 11
support patterns are generated up to S5 relabeling.

For R(3,7) the test is ONE proposed 16-vertex support pattern, not all cases.
"""
from itertools import combinations, permutations, product
from collections import Counter


def patterns17():
    base = tuple(combinations(range(5), 2))
    seen = set()
    for deficit in range(4):
        for missing in combinations(base, deficit + 1):
            missing_counts = Counter(i for p in missing for i in p)
            for eps in product((0, 1, 2), repeat=5):
                if sum(eps) != deficit: continue
                singleton_counts = {i: missing_counts[i] - eps[i] for i in range(5)}
                if any(x not in (0, 1) for x in singleton_counts.values()): continue
                D = tuple(map(frozenset, (p for p in base if p not in missing)))
                D += tuple(frozenset([i]) for i in range(5) if singleton_counts[i])
                assert len(D) == 11
                canonical = min(tuple(sorted(tuple(sorted(p[i] for i in x)) for x in D))
                                for p in permutations(range(5)))
                if canonical in seen: continue
                seen.add(canonical)
                yield deficit, D


def minimal_hall_circuits(D, max_arity):
    circuits = []
    for r in range(2, min(max_arity, len(D)) + 1):
        for C in combinations(range(len(D)), r):
            union = set().union(*(D[i] for i in C))
            if len(union) >= r: continue
            # A Hall circuit is minimally dependent, so every deletion
            # gives a matchable set (for transversal matroids).
            if all(len(set().union(*(D[i] for i in C if i != j))) >= r - 1
                   for j in C):
                assert len(union) == r - 1
                circuits.append(C)
    return circuits


def system(D, t, arity=4):
    E = tuple(e for e in combinations(range(len(D)), 2)
              if D[e[0]].isdisjoint(D[e[1]]))
    idx = {e: k for k, e in enumerate(E)}
    C = minimal_hall_circuits(D, arity)
    circuit_edges = [tuple(idx[e] for e in combinations(c, 2) if e in idx) for c in C]
    assert all(circuit_edges)
    triangles = [tuple(idx[e] for e in combinations(tri, 2))
                 for tri in combinations(range(len(D)), 3)
                 if all(e in idx for e in combinations(tri, 2))]
    incident = [tuple(k for k, e in enumerate(E) if v in e) for v in range(len(D))]
    capacity = [t - 1 - len(s) for s in D]
    return E, C, circuit_edges, triangles, incident, capacity


def closure(D, t, arity=4):
    E, C, CE, Tri, Inc, Cap = system(D, t, arity)
    x = [-1] * len(E)  # unknown -1, forbidden 0, mandatory 1
    proof = []
    def force(edge, val, why):
        if x[edge] == -1:
            x[edge] = val
            proof.append((E[edge], val, why))
            return True
        if x[edge] != val:
            raise Contradiction('inconsistent edge value', (E[edge], why))
        return False
    try:
        for _ in range(100):
            progress = False
            for ci, cand in enumerate(CE):
                if any(x[i] == 1 for i in cand): continue
                possible = [i for i in cand if x[i] == -1]
                if not possible:
                    raise Contradiction('uncovered Hall circuit', C[ci])
                if len(possible) == 1:
                    progress |= force(possible[0], 1, ('Hall circuit', C[ci]))
            for tri in Tri:
                mandatory = [i for i in tri if x[i] == 1]
                if len(mandatory) == 3:
                    raise Contradiction('A-triangle', tuple(E[i] for i in tri))
                if len(mandatory) == 2:
                    for i in tri:
                        if x[i] == -1:
                            progress |= force(i, 0, ('triangle closure', tuple(E[j] for j in mandatory)))
            for v, inc in enumerate(Inc):
                deg = sum(x[i] == 1 for i in inc)
                if deg > Cap[v]:
                    raise Contradiction('degree capacity', (v, deg, Cap[v]))
                if deg == Cap[v]:
                    for i in inc:
                        if x[i] == -1:
                            progress |= force(i, 0, ('degree saturation', v))
            if not progress: break
        else:
            raise AssertionError('Propagation failed to stabilize')
    except Contradiction as err:
        return {'kind': 'propagation', 'reason': err.args, 'proof': proof}

    # Search for an edge-disjoint family of outstanding Hall demands whose
    # candidate edges all meet a small vertex set W, while its remaining
    # degree capacity is too small. No edge can satisfy two demands in the
    # selected family, so each uses at least one free capacity unit in W.
    unmet = []
    for ci, cand in enumerate(CE):
        if any(x[i] == 1 for i in cand): continue
        active = frozenset(i for i in cand if x[i] == -1)
        if not active: raise AssertionError('Propagation missed empty circuit')
        unmet.append((C[ci], active))
    for wsize in (1, 2):
        for W in combinations(range(len(D)), wsize):
            Wset = set(W)
            rem = sum(Cap[v] - sum(x[i] == 1 for i in Inc[v]) for v in W)
            if rem < 0: raise AssertionError('capacity mismatch')
            eligible = [(c, a) for c, a in unmet
                        if all((E[i][0] in Wset or E[i][1] in Wset) for i in a)]
            # Search up to rem+1 pairwise edge-disjoint unmet demands.
            def search(start, chosen, occupied):
                if len(chosen) > rem: return chosen
                for j in range(start, len(eligible)):
                    c, a = eligible[j]
                    if occupied.isdisjoint(a):
                        got = search(j+1, chosen + [(c, tuple(E[i] for i in a))], occupied | a)
                        if got: return got
                return None
            witness = search(0, [], frozenset())
            if witness:
                return {'kind': 'capacity bottleneck', 'terminals': W,
                        'residual_capacity': rem, 'demands': witness, 'proof': proof}
    return {'kind': 'not excluded', 'unmet': len(unmet), 'proof': proof}

class Contradiction(Exception): pass


def rooted_triangle_forcing(D, t):
    """All edges forced by the 4-circuit {a},{a,i},{a,j},{i,j}."""
    support_types = set(D)
    report = []
    for u, du in enumerate(D):
        if len(du) != 1: continue
        a = next(iter(du))
        forced = []
        for w, dw in enumerate(D):
            if len(dw) != 2 or a in dw: continue
            i, j = tuple(dw)
            if frozenset((a,i)) in support_types and frozenset((a,j)) in support_types:
                forced.append(w)
        report.append((u, a, len(forced), t-2, tuple(forced)))
    return report


def main():
    cases = list(patterns17())
    assert len(cases) == 11, len(cases)
    outcomes = Counter()
    for i, (k, D) in enumerate(cases):
        a = closure(D, 6, 4)
        outcomes[a['kind']] += 1
        assert a['kind'] != 'not excluded', (i, k, D)
        extra = (a['reason'] if a['kind'] == 'propagation' else
                 {'terminals':a['terminals'], 'capacity':a['residual_capacity'],
                  'demands':a['demands']})
        print('17-case', i, 'deficit', k, 'type', a['kind'], extra)
    print('TOTAL:', dict(outcomes))
    assert outcomes == Counter({'propagation': 9, 'capacity bottleneck': 2})
    D7 = tuple(frozenset(p) for p in combinations(range(6), 2) if p != (0, 1))
    D7 += (frozenset((0,)), frozenset((1,)))
    a = closure(D7, 7, 4)
    stars = rooted_triangle_forcing(D7, 7)
    assert len(stars) == 2 and all(count == 6 and cap == 5 for _,_,count,cap,_ in stars)
    print('23-vertex candidate support pattern:', a['kind'], a.get('reason'))
    print('Rooted support triangles force A-degree (actual, capacity):', [(x[2],x[3]) for x in stars])
    assert a['kind'] == 'propagation'
    print('All tests pass (integer-exact; no external dependencies).')

if __name__ == '__main__':
    main()
