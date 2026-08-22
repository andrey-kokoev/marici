"""Directed Newton--LDL certificate for one central rank-six anchor."""
import json, math
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT = Path(__file__).parents[1]
N = 6
SOURCE_DEGREE = 39
M = D('6.038308')
R = D('.01')
payload = json.loads((ROOT / 'results' / 'central-H-degree-eleven-interval.json').read_text())
f = [(D(a), D(b)) for a, b in
     payload['F_coefficients_through_degree_thirty_nine']]


@lru_cache(maxsize=None)
def tail(i, j):
    order = i + j
    value = D(0)
    for p in range(SOURCE_DEGREE, 201):
        falling = math.factorial(p) // math.factorial(p - order)
        term = I.up.multiply(M, D(falling) * R ** (p - order))
        value = I.up.add(value, I.up.divide(
            term, D(math.factorial(i) * math.factorial(j))))
    first = I.up.divide(
        I.up.multiply(M, D(201 ** order) * R ** (201 - order)),
        D(math.factorial(i) * math.factorial(j)))
    return I.up.add(value, I.up.divide(first, D('.989')))


def homogeneous(nodes):
    h = [I.box(1)] + [I.box(0)] * SOURCE_DEGREE
    for node in nodes:
        powers = [I.powi(I.box(node), q) for q in range(SOURCE_DEGREE + 1)]
        h = [I.add(*(I.mul(h[d-q], powers[q]) for q in range(d+1)))
             for d in range(SOURCE_DEGREE + 1)]
    return h


def matrix(nodes):
    tables = [homogeneous(nodes[:i+1]) for i in range(N)]
    out = []
    for i in range(N):
        row = []
        for j in range(N):
            value = I.box(0)
            for n in range(1, len(f)):
                for k in range(i, n):
                    ell = n - 1 - k
                    if ell >= j:
                        value = I.add(value, I.mul(
                            f[n], I.mul(tables[i][k-i], tables[j][ell-j])))
            error = tail(i, j)
            row.append(I.add(value, (error.copy_negate(), error)))
        out.append(row)
    return out


def pivots(a):
    lower = [[I.box(0) for _ in range(N)] for _ in range(N)]
    diagonal = []
    for k in range(N):
        pivot = a[k][k]
        for j in range(k):
            pivot = I.sub(pivot, I.mul(
                I.mul(lower[k][j], lower[k][j]), diagonal[j]))
        diagonal.append(pivot)
        lower[k][k] = I.box(1)
        if pivot[0] <= 0:
            break
        for row in range(k + 1, N):
            value = a[row][k]
            for j in range(k):
                value = I.sub(value, I.mul(
                    I.mul(lower[row][j], lower[k][j]), diagonal[j]))
            lower[row][k] = I.div(value, pivot)
    return diagonal


def evaluate(nodes):
    nodes = [D(x) for x in nodes]
    if len(nodes) != N or nodes != sorted(nodes):
        raise ValueError('nodes must be six nondecreasing decimals')
    diagonal = pivots(matrix(nodes))
    certified = len(diagonal) == N and all(pivot[0] > 0 for pivot in diagonal)
    return {
        'anchor': [str(x) for x in nodes],
        'pivots': [[str(a), str(b)] for a, b in diagonal],
        'sixth_pivot_interval': ([str(x) for x in diagonal[-1]]
                                 if len(diagonal) == N else None),
        'all_six_Newton_LDL_pivots_strictly_positive': certified,
        'source_degree': SOURCE_DEGREE,
        'analytic_source_tail_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': certified,
        'rh_proved': False,
    }


if __name__ == '__main__':
    anchors = [['0'] * N, ['.01'] * N,
               ['0', '0', '.002', '.004', '.007', '.01']]
    result = {'anchors': [evaluate(anchor) for anchor in anchors],
              'rh_proved': False}
    output = ROOT / 'results' / 'central-rank-six-loewner-anchor.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
