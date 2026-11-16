"""Exact preliminary checks for a compositional witness-rank target.
Requires Python 3.10+, NetworkX and SymPy.
This does NOT construct a rank-16 certificate for the 13-vertex graph.
"""
from __future__ import annotations
import json
from pathlib import Path
import networkx as nx
import sympy as sp


def independent_sets(G: nx.Graph) -> tuple[list[int], list[int]]:
    maximal = sorted(sum(1 << v for v in S)
                     for S in nx.find_cliques(nx.complement(G)))
    a = max(map(int.bit_count, maximal))
    return [S for S in maximal if S.bit_count() == a], maximal


def exact_clique(adj: list[int]) -> list[int]:
    best: list[int] = []
    def color(P: int) -> tuple[list[int], list[int]]:
        vertices, bounds, c = [], [], 0
        while P:
            c += 1
            Q = P
            while Q:
                b = Q & -Q
                v = b.bit_length() - 1
                vertices.append(v)
                bounds.append(c)
                P ^= b
                Q ^= b
                Q &= ~adj[v]
        return vertices, bounds
    def expand(C: list[int], P: int) -> None:
        nonlocal best
        if not P:
            if len(C) > len(best):
                best = C.copy()
            return
        vertices, bounds = color(P)
        for j in range(len(vertices)-1, -1, -1):
            if len(C)+bounds[j] <= len(best):
                return
            v = vertices[j]
            expand(C+[v], P & adj[v])
            P &= ~(1 << v)
    expand([], (1 << len(adj))-1)
    return best


def vertices(mask: int) -> list[int]:
    return [i for i in range(mask.bit_length()) if mask >> i & 1]


def obstruction_audit(G: nx.Graph) -> dict:
    ts, ms = independent_sets(G)
    pairs = [(T, S) for T in ts for S in ms if not T & S]
    adj = [sum(1 << j for j, (U, V) in enumerate(pairs)
               if S & U and V & T) for T, S in pairs]
    clique = exact_clique(adj)
    chosen = [pairs[i] for i in clique]
    # Cross-pair upper bound alone need not be attained by an obstruction;
    # verify incompatibility separately.
    assert all(any(not M & T for T, _ in chosen) for M in ms)
    assert all(not T & S and all(S & U for j, (U, _) in enumerate(chosen) if j != i)
               for i, (T, S) in enumerate(chosen))
    return {'alpha': ts[0].bit_count(), 'exact_largest_obstruction': len(chosen),
            'requirements': [vertices(T) for T, _ in chosen],
            'deletion_witnesses': [vertices(S) for _, S in chosen]}


def rank_mod_2(rows: list[list[int]]) -> int:
    basis = {}
    for r in rows:
        x = sum((int(v) % 2) << i for i, v in enumerate(r))
        while x:
            p = x.bit_length()-1
            if p not in basis:
                basis[p] = x
                break
            x ^= basis[p]
    return len(basis)


def main() -> None:
    c5 = obstruction_audit(nx.cycle_graph(5))
    two_c5 = obstruction_audit(nx.disjoint_union(nx.cycle_graph(5), nx.cycle_graph(5)))
    assert c5['exact_largest_obstruction'] == 3
    assert two_c5['exact_largest_obstruction'] == 10

    G = nx.circulant_graph(13, [1, 5])
    ts, ms = independent_sets(G)
    assert len(ts) == len(ms) == 39
    D = [[int(not T & S) for S in ms] for T in ts]
    # Greedy search is used only to FIND a certificate; validity below is exact.
    import random
    rng = random.Random(1)
    bits = [sum(v << j for j, v in enumerate(row)) for row in D]
    best = []
    for _ in range(10000):
        live, pivots = (1 << len(ms))-1, []
        while live:
            rows = [i for i, row in enumerate(bits) if row & live]
            if not rows:
                break
            degree = min((bits[i] & live).bit_count() for i in rows)
            i = rng.choice([i for i in rows if (bits[i] & live).bit_count() == degree])
            j = rng.choice([j for j in range(len(ms)) if (bits[i] & live) >> j & 1])
            pivots.append((i, j))
            live &= ~bits[i]
        if len(pivots) > len(best):
            best = pivots
        if len(best) >= 16:
            break
    assert len(best) >= 16
    best = best[:16]
    assert all(D[i][j] == 1 for i, j in best)
    assert all(D[best[i][0]][best[j][1]] == 0 for i in range(16) for j in range(i+1,16))
    # The displayed submatrix is triangular with a forced nonzero diagonal.
    # Thus EVERY matrix with this exact zero/nonzero pattern has rank >=16,
    # over any field. No claim of attaining rank 16 is made.
    result = {
        'single_pentagon': c5, 'two_disjoint_pentagons': two_c5,
        'c13': {'matrix_shape': [39, 39], 'ordinary_rank_Q': int(sp.Matrix(D).rank()),
                'ordinary_rank_GF2': rank_mod_2(D),
                'universal_support_rank_lower_bound': 16,
                'triangular_rows': [vertices(ts[i]) for i, j in best],
                'triangular_columns': [vertices(ms[j]) for i, j in best],
                'rank_16_real_realization': 'not established'},
        'interpretation': 'These matrices describe readout compatibility only; path histories are not identified.'}
    path = Path(__file__).with_name('compositional_witness_target_results.json')
    path.write_text(json.dumps(result, indent=2))
    print(json.dumps({'h(C5)': c5['exact_largest_obstruction'],
                      'h(C5 disjoint union C5)': two_c5['exact_largest_obstruction'],
                      'C13_support_rank_lower_bound': 16,
                      'C13_unweighted_rank_Q': result['c13']['ordinary_rank_Q'],
                      'results': str(path)}, indent=2))


if __name__ == '__main__':
    main()
