"""Prefix-cached audit of all 48,048 rank-six anchor derivatives."""
import itertools, json
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

import central_rank_six_derivative_interval_anchor as A
import central_rank_six_loewner_grid as P

G, I = A.G, A.I
GRID = tuple(D(i) / D(1000) for i in range(11))


@lru_cache(maxsize=None)
def derivative_h_prefix(prefix, variable):
    if variable >= len(prefix):
        return (I.box(0),) * (G.SOURCE_DEGREE + 1)
    h = P.homogeneous_prefix(prefix)
    return tuple(A.derivative_h(h, prefix[variable]))


@lru_cache(maxsize=None)
def derivative_entry(i, j, variable, governing_prefix):
    left_prefix = governing_prefix[:i+1]
    right_prefix = governing_prefix[:j+1]
    left = P.homogeneous_prefix(left_prefix)
    right = P.homogeneous_prefix(right_prefix)
    dleft = derivative_h_prefix(left_prefix, variable)
    dright = derivative_h_prefix(right_prefix, variable)
    value = I.box(0)
    for n in range(1, len(G.f)):
        for k in range(i, n):
            ell = n - 1 - k
            if ell < j:
                continue
            factor = I.box(0)
            if variable <= i:
                factor = I.add(factor, I.mul(dleft[k-i], right[ell-j]))
            if variable <= j:
                factor = I.add(factor, I.mul(left[k-i], dright[ell-j]))
            value = I.add(value, I.mul(G.f[n], factor))
    error = A.derivative_tail(i, j, variable)
    return I.add(value, (error.copy_negate(), error))


def evaluate(nodes):
    matrix = P.matrix(nodes)
    da = [[[I.box(0) for _ in range(G.N)] for _ in range(G.N)]
          for _ in range(G.N)]
    for i in range(G.N):
        for j in range(i, G.N):
            governing = nodes[:max(i, j)+1]
            for variable in range(max(i, j)+1):
                value = derivative_entry(i, j, variable, governing)
                da[i][j][variable] = value
                da[j][i][variable] = value

    lower = [[I.box(0) for _ in range(G.N)] for _ in range(G.N)]
    dlower = [[[I.box(0) for _ in range(G.N)] for _ in range(G.N)]
              for _ in range(G.N)]
    diagonal, ddiagonal = [], []
    for k in range(G.N):
        pivot = matrix[k][k]
        dpivot = list(da[k][k])
        for j in range(k):
            pivot = I.sub(pivot, I.mul(
                I.mul(lower[k][j], lower[k][j]), diagonal[j]))
            for v in range(G.N):
                dpivot[v] = I.sub(dpivot[v], I.add(
                    I.mul(I.mul(I.scale(lower[k][j], 2), dlower[k][j][v]),
                          diagonal[j]),
                    I.mul(I.mul(lower[k][j], lower[k][j]), ddiagonal[j][v])))
        diagonal.append(pivot)
        ddiagonal.append(dpivot)
        lower[k][k] = I.box(1)
        for row in range(k+1, G.N):
            value = matrix[row][k]
            dvalue = list(da[row][k])
            for j in range(k):
                value = I.sub(value, I.mul(
                    I.mul(lower[row][j], lower[k][j]), diagonal[j]))
                for v in range(G.N):
                    dvalue[v] = I.sub(dvalue[v], I.add(
                        I.mul(I.mul(dlower[row][j][v], lower[k][j]), diagonal[j]),
                        I.mul(I.mul(lower[row][j], dlower[k][j][v]), diagonal[j]),
                        I.mul(I.mul(lower[row][j], lower[k][j]), ddiagonal[j][v])))
            lower[row][k] = I.div(value, pivot)
            for v in range(G.N):
                dlower[row][k][v] = I.div(I.sub(
                    dvalue[v], I.mul(lower[row][k], dpivot[v])), pivot)
    return diagonal[-1], ddiagonal[-1]


def main():
    count = 0
    failures = []
    closest = None
    most_negative = None
    for nodes in itertools.combinations_with_replacement(GRID, G.N):
        count += 1
        pivot, derivatives = evaluate(nodes)
        for variable, interval in enumerate(derivatives):
            candidate_upper = (interval[1], nodes, variable, interval)
            candidate_lower = (interval[0], nodes, variable, interval)
            if closest is None or candidate_upper[0] > closest[0]:
                closest = candidate_upper
            if most_negative is None or candidate_lower[0] < most_negative[0]:
                most_negative = candidate_lower
            if interval[1] >= 0:
                failures.append({'anchor': [str(x) for x in nodes],
                                 'variable': variable,
                                 'interval': [str(x) for x in interval]})
    result = {
        'grid': [str(x) for x in GRID],
        'anchor_count': count,
        'coordinate_derivative_count': G.N * count,
        'uncertified_derivative_count': len(failures),
        'all_anchor_derivatives_strictly_negative': not failures,
        'closest_upper_endpoint_to_zero': {
            'value': str(closest[0]), 'anchor': [str(x) for x in closest[1]],
            'variable': closest[2], 'interval': [str(x) for x in closest[3]]},
        'most_negative_lower_endpoint': {
            'value': str(most_negative[0]),
            'anchor': [str(x) for x in most_negative[1]],
            'variable': most_negative[2],
            'interval': [str(x) for x in most_negative[3]]},
        'derivative_entry_cache_size': derivative_entry.cache_info().currsize,
        'analytic_source_tail_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': not failures and count == 8008,
        'failures': failures[:10],
        'rh_proved': False,
    }
    output = Path(__file__).parents[1] / 'results' / 'central-rank-six-derivative-interval-grid.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
