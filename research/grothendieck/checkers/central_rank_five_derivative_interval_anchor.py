"""Directed fifth-pivot derivatives at a chosen rank-five grid anchor."""
import json, math
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

import central_rank_five_loewner_grid as G

I = G.I
N = 5


def derivative_h(h, x):
    return [I.box(0)] + [
        I.add(*(I.scale(I.mul(I.powi(I.box(x), q - 1), h[d - q]), q)
                for q in range(1, d + 1)))
        for d in range(1, 30)
    ]


@lru_cache(maxsize=None)
def derivative_tail(i, j, variable):
    multiplicity = int(variable <= i) + int(variable <= j)
    order = i + j + 1
    value = D(0)
    for p in range(29, 201):
        falling = math.factorial(p) // math.factorial(p - order)
        term = I.up.multiply(D(multiplicity) * G.M,
                             D(falling) * G.R ** (p - order))
        value = I.up.add(value, I.up.divide(
            term, D(math.factorial(i) * math.factorial(j))))
    first = I.up.divide(
        I.up.multiply(D(multiplicity) * G.M,
                      D(201 ** order) * G.R ** (201 - order)),
        D(math.factorial(i) * math.factorial(j)))
    return I.up.add(value, I.up.divide(first, D('.989')))


def evaluate(nodes):
    """Return directed fifth-pivot and coordinate-derivative intervals."""
    nodes = [D(x) for x in nodes]
    if len(nodes) != N or nodes != sorted(nodes):
        raise ValueError('nodes must be five nondecreasing decimals')
    h = [G.homogeneous(nodes[:i + 1]) for i in range(N)]
    dh = [[derivative_h(h[i], nodes[v]) if v <= i else [I.box(0)] * 30
           for v in range(N)] for i in range(N)]

    def derivative_entry(i, j, variable):
        value = I.box(0)
        for n in range(1, len(G.f)):
            for k in range(i, n):
                ell = n - 1 - k
                if ell < j:
                    continue
                factor = I.box(0)
                if variable <= i:
                    factor = I.add(factor, I.mul(
                        dh[i][variable][k - i], h[j][ell - j]))
                if variable <= j:
                    factor = I.add(factor, I.mul(
                        h[i][k - i], dh[j][variable][ell - j]))
                value = I.add(value, I.mul(G.f[n], factor))
        error = derivative_tail(i, j, variable)
        return I.add(value, (error.copy_negate(), error))

    a = G.matrix(nodes)
    da = [[[derivative_entry(i, j, v) for v in range(N)]
           for j in range(N)] for i in range(N)]
    lower = [[I.box(0) for _ in range(N)] for _ in range(N)]
    dlower = [[[I.box(0) for _ in range(N)] for _ in range(N)]
              for _ in range(N)]
    diagonal = []
    ddiagonal = []
    for k in range(N):
        pivot = a[k][k]
        dpivot = [da[k][k][v] for v in range(N)]
        for j in range(k):
            pivot = I.sub(pivot, I.mul(
                I.mul(lower[k][j], lower[k][j]), diagonal[j]))
            for v in range(N):
                dpivot[v] = I.sub(dpivot[v], I.add(
                    I.mul(I.mul(I.scale(lower[k][j], 2),
                                dlower[k][j][v]), diagonal[j]),
                    I.mul(I.mul(lower[k][j], lower[k][j]),
                          ddiagonal[j][v])))
        diagonal.append(pivot)
        ddiagonal.append(dpivot)
        lower[k][k] = I.box(1)
        for row in range(k + 1, N):
            value = a[row][k]
            dvalue = [da[row][k][v] for v in range(N)]
            for j in range(k):
                value = I.sub(value, I.mul(
                    I.mul(lower[row][j], lower[k][j]), diagonal[j]))
                for v in range(N):
                    dvalue[v] = I.sub(dvalue[v], I.add(
                        I.mul(I.mul(dlower[row][j][v], lower[k][j]),
                              diagonal[j]),
                        I.mul(I.mul(lower[row][j], dlower[k][j][v]),
                              diagonal[j]),
                        I.mul(I.mul(lower[row][j], lower[k][j]),
                              ddiagonal[j][v])))
            lower[row][k] = I.div(value, pivot)
            for v in range(N):
                dlower[row][k][v] = I.div(I.sub(
                    dvalue[v], I.mul(lower[row][k], dpivot[v])), pivot)

    derivatives = ddiagonal[-1]
    certified = all(x[1] < 0 for x in derivatives)
    return {
        'anchor': [str(x) for x in nodes],
        'fifth_pivot_interval': [str(x) for x in diagonal[-1]],
        'fifth_pivot_coordinate_derivative_intervals': [
            [str(a), str(b)] for a, b in derivatives],
        'all_five_derivatives_strictly_negative': certified,
        'analytic_tail_bounds_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': certified,
        'rh_proved': False,
    }


if __name__ == '__main__':
    result = evaluate(['.003', '.003', '.003', '.01', '.01'])
    assert result['interval_certified']
    output = (Path(__file__).parents[1] / 'results' /
              'central-rank-five-derivative-interval-anchor.json')
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    for key, value in result.items():
        print(f'{key}={value}')
