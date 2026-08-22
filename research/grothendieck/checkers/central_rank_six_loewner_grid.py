"""Prefix-cached directed audit of all 8008 rank-six grid anchors."""
import itertools, json
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

import central_rank_six_loewner_anchor as G

I = G.I
GRID = tuple(D(i) / D(1000) for i in range(11))
ANCHORS = itertools.combinations_with_replacement(GRID, G.N)


@lru_cache(maxsize=None)
def powers(node):
    return tuple(I.powi(I.box(node), q) for q in range(G.SOURCE_DEGREE + 1))


@lru_cache(maxsize=None)
def homogeneous_prefix(prefix):
    if not prefix:
        return (I.box(1),) + (I.box(0),) * G.SOURCE_DEGREE
    prior = homogeneous_prefix(prefix[:-1])
    node_powers = powers(prefix[-1])
    return tuple(I.add(*(I.mul(prior[d-q], node_powers[q])
                         for q in range(d+1)))
                 for d in range(G.SOURCE_DEGREE + 1))


@lru_cache(maxsize=None)
def entry(i, j, governing_prefix):
    left = homogeneous_prefix(governing_prefix[:i+1])
    right = homogeneous_prefix(governing_prefix[:j+1])
    value = I.box(0)
    for n in range(1, len(G.f)):
        for k in range(i, n):
            ell = n - 1 - k
            if ell >= j:
                value = I.add(value, I.mul(
                    G.f[n], I.mul(left[k-i], right[ell-j])))
    error = G.tail(i, j)
    return I.add(value, (error.copy_negate(), error))


def matrix(nodes):
    out = [[I.box(0) for _ in range(G.N)] for _ in range(G.N)]
    for i in range(G.N):
        for j in range(i, G.N):
            governing = nodes[:max(i, j)+1]
            value = entry(i, j, governing)
            out[i][j] = value
            out[j][i] = value
    return out


def main():
    count = 0
    failures = []
    weakest = [None] * G.N
    for nodes in ANCHORS:
        count += 1
        diagonal = G.pivots(matrix(nodes))
        if len(diagonal) != G.N or any(pivot[0] <= 0 for pivot in diagonal):
            failures.append({'anchor': [str(x) for x in nodes],
                             'pivots': [[str(a), str(b)] for a, b in diagonal]})
            continue
        for k, pivot in enumerate(diagonal):
            if weakest[k] is None or pivot[0] < weakest[k][0][0]:
                weakest[k] = (pivot, nodes)
    result = {
        'grid': [str(x) for x in GRID],
        'nondecreasing_anchor_count': count,
        'expected_anchor_count': 8008,
        'uncertified_anchor_count': len(failures),
        'all_rank_six_Newton_LDL_pivots_strictly_positive': not failures,
        'coordinatewise_weakest_pivots': [
            {'pivot_index': k+1,
             'anchor': [str(x) for x in row[1]],
             'interval': [str(x) for x in row[0]]}
            for k, row in enumerate(weakest) if row is not None],
        'prefix_table_cache_size': homogeneous_prefix.cache_info().currsize,
        'matrix_entry_cache_size': entry.cache_info().currsize,
        'source_degree': G.SOURCE_DEGREE,
        'analytic_source_tail_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': not failures and count == 8008,
        'failures': failures[:10],
        'rh_proved': False,
    }
    output = Path(__file__).parents[1] / 'results' / 'central-rank-six-loewner-grid.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
