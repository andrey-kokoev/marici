#!/usr/bin/env python3
"""Exact Bonferroni-order test on the 11 extremal (3,k) Ramsey graphs, k=4..6.

No graph-algorithm or numerical-optimization dependency is required.  Graphs
are stored as graph6, and every independent candidate neighborhood is checked.
Checks the terminality statement independently of the Bonferroni certificate.
"""
from collections import Counter
from math import comb

CRITICAL = {
    4: [
        'G@hZCc',
        'G`_gqK',
        'GsOiho',
    ],
    5: [
        'Ls`?XGRQR@B`Kc',
    ],
    6: [
        'P??GaOo`XMGsIcT?pSLaGuA?',
        'P?C?I_h`SDEQQcLAh`dU?tG?',
        'P@oGQA?`ACcdCtDYC]Ah?goC',
        'PG?OSAKccKGiGwJSI[@oWUA_',
        'PGD?OkeO_WAEGQobP_s`cgU?',
        'Ps`A?WIDGeCdGsQEKK?oLL_O',
        'Ps`A?_KChFCiBoQSKCOoXL_O',
    ],
}


def decode_graph6(code):
    """Read an unprefixed graph6 string of order < 63."""
    n = ord(code[0]) - 63
    assert 0 <= n < 63
    payload = [ord(c) - 63 for c in code[1:]]
    bits = [((a >> shift) & 1) for a in payload for shift in range(5, -1, -1)]
    assert len(bits) >= n * (n - 1) // 2
    adj = [0] * n
    index = 0
    for j in range(1, n):
        for i in range(j):
            if bits[index]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            index += 1
    return adj


def max_independent_sets(adj):
    n = len(adj)
    nsubs = 1 << n
    full = nsubs - 1
    independent = bytearray(nsubs)
    independent[0] = 1
    dominated = [0] * nsubs
    alpha = 0
    maximum = []
    maximal = []
    for s in range(1, nsubs):
        bit = s & -s
        i = bit.bit_length() - 1
        tail = s ^ bit
        independent[s] = independent[tail] and not (adj[i] & tail)
        dominated[s] = dominated[tail] | bit | adj[i]
        if independent[s]:
            d = s.bit_count()
            if d > alpha:
                alpha = d
                maximum = [s]
            elif d == alpha:
                maximum.append(s)
            if dominated[s] == full:
                maximal.append(s)
    if not alpha:  # empty graph, not part of the catalog
        maximum = [0]
        maximal = [0]
    return alpha, maximum, maximal


def mask_vertices(s, n):
    return [i for i in range(n) if s & (1 << i)]


def f_odd(d, h):
    """Odd Bonferroni upper approximation of 1_[h >= 1]."""
    assert d % 2 == 1
    if h == 0:
        return 0
    return 1 + comb(h - 1, d) if h > d else 1


def calculate_graph(k, code):
    adj = decode_graph6(code)
    n = len(adj)
    assert all((adj[u] & adj[v]) == 0 for u in range(n)
               for v in range(u + 1, n) if adj[u] & (1 << v))
    alpha, maximum, maximal = max_independent_sets(adj)
    assert alpha == k - 1
    N = len(maximum)
    maxima = {d: (-1, None, None) for d in range(1, k, 2)}
    terminal = True
    failing = {d: [] for d in maxima}
    for S in maximal:
        overlaps = Counter((S & I).bit_count() for I in maximum)
        true_covered = N - overlaps.get(0, 0)
        if true_covered == N:
            terminal = False
        for d in maxima:
            upper = sum(count * f_odd(d, h) for h, count in overlaps.items())
            assert upper >= true_covered
            if upper > maxima[d][0]:
                maxima[d] = (upper, S, true_covered)
            if upper >= N:
                failing[d].append({
                    'S': mask_vertices(S, n),
                    'actual_coverage': true_covered,
                    'upper': upper,
                    'overlap_histogram': dict(sorted(overlaps.items())),
                })
    assert terminal, 'This graph is not terminal at the indicated k'
    assert max(sum(bool(S & I) for I in maximum) for S in maximal) < N
    out = {
        'k': k,
        'n': n,
        'graph6': code,
        'maximum_independent_sets': N,
        'maximal_independent_sets': len(maximal),
        'max_bonferroni': {d: maxima[d][0] for d in maxima},
        'failing_candidates': {d: failing[d] for d in maxima},
        'terminal': terminal,
    }
    return out


def disjoint_c5_family(t, ds=(1, 3, 5, 7, 9)):
    """Maximum-set overlap counts for t disjoint 5-cycles.

    Fix a maximum independent set on each C5.  For that component the
    intersection with an arbitrary maximum independent set has distribution
    0:2, 1:2, 2:1.  Multiply t copies of 2 + 2z + z^2.
    """
    counts = Counter({0: 1})
    for _ in range(t):
        nxt = Counter()
        for a, av in counts.items():
            for b, bv in {0: 2, 1: 2, 2: 1}.items():
                nxt[a + b] += av * bv
        counts = nxt
    N = 5 ** t
    assert sum(counts.values()) == N
    assert counts[0] == 2 ** t
    actual = N - 2 ** t
    vals = {d: sum(freq * f_odd(d, h) for h, freq in counts.items()) for d in ds}
    return {'t': t, 'k': 2 * t + 1, 'n': 5 * t,
            'N': N, 'actual_coverage': actual, 'upper_bounds': vals}


def main():
    results = []
    for k, codes in CRITICAL.items():
        for i, code in enumerate(codes, 1):
            row = calculate_graph(k, code)
            results.append(row)
            fails = {d: len(c) for d,c in row['failing_candidates'].items() if c}
            print(f"k={k}, graph={i}, n={row['n']}, "
                  f"N={row['maximum_independent_sets']}, "
                  f"U={row['max_bonferroni']}, failures={fails}")
            for d, c in row['failing_candidates'].items():
                if d == 3 and c:
                    for f in c:
                        print('  d=3 failure',f)
    # Graph-specific regression against direct exact independent-set checks.
    assert [r['max_bonferroni'][3] < r['maximum_independent_sets']
            for r in results if r['k'] == 6] == [False, True, True, True, True, True, True]
    assert [r['max_bonferroni'][3] < r['maximum_independent_sets']
            for r in results if r['k'] == 4] == [True, True, True]
    assert [r['max_bonferroni'][3] < r['maximum_independent_sets']
            for r in results if r['k'] == 5] == [True]
    assert len(results[4]['failing_candidates'][3]) == 3
    assert disjoint_c5_family(3)['upper_bounds'][3] == 169
    for t in range(1, 7):
        print('disjoint C5',disjoint_c5_family(t))
    print(f'PASS: {len(results)} catalog graphs, independent certificates, C5^t exact family')


if __name__ == '__main__':
    main()
