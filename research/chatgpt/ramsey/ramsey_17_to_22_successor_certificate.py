#!/usr/bin/env python3
"""Symmetry-sector Ramsey construction: 13 -> 17 -> 22.

Standard library only; exact integer-bitset enumeration.

The construction *does not supply the target graph*. It selects the 17-vertex
sector from C13 using its order-four automorphism, then builds a candidate
five-vertex successor from two opposite pairs of the new C4 and maximum
independent sets of the C13 core. It derives the compatible triples and all
five new edge colors by exhaustive Ramsey admissibility tests.

Scope: exhaustive within the declared attachment family, not completeness of
that family among all possible Ramsey extensions or a general R(3,k) formula.
"""
from collections import Counter
from itertools import product, combinations


def add_edge(adj, u, v):
    assert u != v
    adj[u] |= 1 << v
    adj[v] |= 1 << u


def is_independent(adj, mask):
    while mask:
        b = mask & -mask
        v = b.bit_length() - 1
        mask ^= b
        if adj[v] & mask:
            return False
    return True


def alpha_dp(adj):
    """Exact alpha of every induced vertex subset."""
    table = bytearray(1 << len(adj))
    for mask in range(1, len(table)):
        b = mask & -mask
        v = b.bit_length() - 1
        remaining = mask ^ b
        table[mask] = max(table[remaining], 1 + table[remaining & ~adj[v]])
    return table


def rotate_mask(mask, sigma):
    result = 0
    while mask:
        b = mask & -mask
        v = b.bit_length() - 1
        result |= 1 << sigma[v]
        mask ^= b
    return result


def orbit(mask, sigma):
    states = [mask]
    for _ in range(3):
        states.append(rotate_mask(states[-1], sigma))
    assert rotate_mask(states[-1], sigma) == mask
    return states


def human(mask, n):
    return tuple(i for i in range(n) if mask & (1 << i))


def independence_number_direct(adj):
    """Independent verification without subset DP."""
    maximum = 0
    stack = [((1 << len(adj)) - 1, 0)]
    while stack:
        available, count = stack.pop()
        if not available:
            maximum = max(maximum, count)
            continue
        if count + available.bit_count() <= maximum:
            continue
        b = available & -available
        v = b.bit_length() - 1
        stack.append((available ^ b, count))
        stack.append(((available ^ b) & ~adj[v], count + 1))
    return maximum



def independent_sets(adj):
    """Enumerate all independent masks; used for terminality certificates."""
    allmask = (1 << len(adj)) - 1
    out = []
    def visit(available, chosen):
        if not available:
            out.append(chosen)
            return
        b = available & -available
        v = b.bit_length() - 1
        visit(available ^ b, chosen)
        visit((available ^ b) & ~adj[v], chosen | b)
    visit(allmask, 0)
    return out

def run():
    # 13-vertex Ramsey graph, generated without a target graph.
    n0 = 13
    G13 = [0] * n0
    for u in range(n0):
        for d in (1, 5, 8, 12):
            add_edge(G13, u, (u + d) % n0)
    sigma13 = [(5 * i) % n0 for i in range(n0)]
    alpha13 = alpha_dp(G13)
    assert alpha13[-1] == 4
    assert all(rotate_mask(G13[v], sigma13) == G13[sigma13[v]] for v in range(n0))

    # Derive the three quarter-turn orbits of nonzero labels.
    unvisited = set(range(1, 13))
    orbits = []
    while unvisited:
        v = min(unvisited)
        orbit4 = [(v * pow(5, i, 13)) % 13 for i in range(4)]
        assert len(set(orbit4)) == 4
        orbits.append(orbit4)
        unvisited.difference_update(orbit4)
    assert len(orbits) == 3

    eligible_seeds = []
    for seed in product(*orbits):
        M = sum(1 << i for i in seed)
        if not is_independent(G13, M):
            continue
        stages = orbit(M, sigma13)
        residual = ((1 << 13) - 1) & ~(stages[0] | stages[2])
        if alpha13[residual] <= 3:
            eligible_seeds.append(M)
    assert len(eligible_seeds) == 4
    seed = eligible_seeds[0]

    # Attach a red C4 (the first, previously derived quarter-turn successor).
    G17 = G13[:] + [0] * 4
    for t, S in enumerate(orbit(seed, sigma13)):
        for u in human(S, 13):
            add_edge(G17, 13 + t, u)
        add_edge(G17, 13 + t, 13 + (t + 1) % 4)
    sigma17 = sigma13 + [13 + (i + 1) % 4 for i in range(4)]
    assert all(is_independent(G17, G17[u]) for u in range(17))
    alpha17 = alpha_dp(G17)
    assert alpha17[-1] == 5
    assert all(rotate_mask(G17[u], sigma17) == G17[sigma17[u]] for u in range(17))

    # Test whether an entire four-vertex C4 orbit can be appended at k=7.
    # No target size is supplied: we generate every independent neighborhood
    # and take its orbit under the inherited quarter turn.
    viable_c4 = []
    for S in range(1 << 17):
        if not is_independent(G17, S):
            continue
        stages = orbit(S, sigma17)
        if any(stages[t] & stages[(t + 1) % 4] for t in range(4)):
            continue
        # Independent subsets of a C4: empty, four singletons, two opposite pairs.
        valid = True
        for J in (0, 1, 2, 4, 8, 5, 10):
            union = 0
            for t in range(4):
                if J & (1 << t):
                    union |= stages[t]
            if J.bit_count() + alpha17[((1 << 17) - 1) & ~union] > 6:
                valid = False
                break
        if valid:
            viable_c4.append(S)
    assert len(viable_c4) == 20
    reps_c4 = {}
    for S in viable_c4:
        key = min(orbit(S, sigma17))
        reps_c4.setdefault(key, S)
    assert len(reps_c4) == 5
    for S in reps_c4.values():
        G21 = G17[:] + [0] * 4
        for t, neighborhood in enumerate(orbit(S, sigma17)):
            for u in human(neighborhood, 17):
                add_edge(G21, 17 + t, u)
            add_edge(G21, 17 + t, 17 + (t + 1) % 4)
        subsets = independent_sets(G21)
        maximum = max(m.bit_count() for m in subsets)
        assert maximum == 6
        maxsets = [m for m in subsets if m.bit_count() == 6]
        assert not any(all(Snew & I for I in maxsets) for Snew in subsets)

    # Natural first pair: the two opposite independent pairs of the C4.
    L0 = (1 << 13) | (1 << 15)
    L1 = (1 << 14) | (1 << 16)
    assert rotate_mask(L0, sigma17) == L1

    # Candidate right-side neighborhoods: all maximum independent sets in
    # the inherited 13-vertex core, without specifying a preferred triple.
    M4 = [m for m in range(1 << 13) if m.bit_count() == 4 and is_independent(G13, m)]
    assert len(M4) == 39
    fixed = [m for m in M4 if rotate_mask(m, sigma13) == m]
    assert len(fixed) == 1

    # If two right-side vertices remain blue, their residual must have
    # independence number at most four (2 + 4 = 6).
    compatibility = set()
    for a, b in combinations(M4, 2):
        if alpha17[((1 << 17) - 1) & ~(a | b)] <= 4:
            compatibility.add(frozenset((a, b)))
    assert len(compatibility) == 129

    triangles = []
    for trio in combinations(M4, 3):
        if all(frozenset(p) in compatibility for p in combinations(trio, 2)):
            triangles.append(trio)
    assert len(triangles) == 4
    assert all(alpha17[((1 << 17) - 1) & ~ (a|b|c)] <= 3 for a,b,c in triangles)
    # The four triangles must form one orbit under simultaneous rotation.
    t0 = set(triangles[0])
    four_orbit = set()
    for _ in range(4):
        four_orbit.add(tuple(sorted(t0)))
        t0 = {rotate_mask(s, sigma13) for s in t0}
    assert four_orbit == {tuple(sorted(t)) for t in triangles}

    right = tuple(triangles[0])
    five_neighbors = (L0, L1, *right)
    edges = list(combinations(range(5), 2))
    valid_patterns = []
    failures = Counter()
    oldmask = (1 << 17) - 1
    # No new edge graph F is supplied: exhaust all 2^10 possibilities.
    for pattern in range(1 << len(edges)):
        F = [0] * 5
        for bit, (a, b) in enumerate(edges):
            if pattern & (1 << bit):
                add_edge(F, a, b)
        if any(not is_independent(F, F[v]) for v in range(5)):
            failures['new_red_triangle'] += 1
            continue
        if any((F[a] & (1 << b)) and (five_neighbors[a] & five_neighbors[b])
               for a,b in edges):
            failures['old_new_red_triangle'] += 1
            continue
        good = True
        for J in range(1 << 5):
            if not is_independent(F, J):
                continue
            removed = 0
            for i in range(5):
                if J & (1 << i):
                    removed |= five_neighbors[i]
            if J.bit_count() + alpha17[oldmask & ~removed] > 6:
                good = False
                break
        if good:
            valid_patterns.append((pattern, F))
        else:
            failures['blue_seven_set'] += 1
    assert failures == Counter({
        'new_red_triangle': 636,
        'old_new_red_triangle': 141,
        'blue_seven_set': 246,
    }), failures
    assert len(valid_patterns) == 1
    pattern, F = valid_patterns[0]
    assert {frozenset((a,b)) for a,b in edges if F[a] & (1<<b)} == {
        frozenset((a,b)) for a in (0,1) for b in (2,3,4)
    }

    G22 = G17[:] + [0] * 5
    for i, neighborhood in enumerate(five_neighbors):
        for u in human(neighborhood,17):
            add_edge(G22,17+i,u)
    for a,b in edges:
        if F[a] & (1 << b):
            add_edge(G22,17+a,17+b)
    assert all(is_independent(G22,G22[v]) for v in range(22))
    assert independence_number_direct(G22) == 6
    assert sum(v.bit_count() for v in G22)//2 == 64
    print('13 -> 17: successful quarter-turn seeds =',len(eligible_seeds), '(one orbit)')
    print('17 -> 21: viable C4 orbit attachments =',len(viable_c4),'(five rotation orbits; all terminal)')
    print('17 -> 22: inherited core maximum four-sets =',len(M4))
    print('17 -> 22: pairwise compatibility edges =',len(compatibility))
    print('17 -> 22: compatible triples =',len(triangles),'(one orbit)')
    print('17 -> 22: unique invariant old four-set =',human(fixed[0],13))
    print('17 -> 22: representative triple =',*[human(s,13) for s in right])
    print('17 -> 22: tested new-edge colorings =',1<<len(edges))
    print('17 -> 22: valid new-edge colorings =',len(valid_patterns))
    print('17 -> 22: forced new graph = K_{2,3}')
    print('22-vertex witness: edges = 64, triangle-free, alpha = 6')
    print('Reproducible 22-vertex red edge list:')
    print([(i,j) for i in range(22) for j in range(i+1,22) if G22[i] & (1<<j)])

if __name__ == '__main__':
    run()
