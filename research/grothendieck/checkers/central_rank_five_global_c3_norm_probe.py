"""Global absolute C3 norm probe for the fifth Newton-LDL pivot."""
import json, math
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_hessian_interval_anchor as H

I, N, F = H.I, H.N, H.F
ROOT = Path(__file__).parents[1]
floors = [D(x) for x in json.loads(
    (ROOT / 'results' / 'central-rank-four-global-pivot-denominators.json').read_text()
)['global_first_four_pivot_lower_bounds']]


def add(a, b):
    return tuple(I.up.add(a[k], b[k]) for k in range(4))


def mul(a, b):
    return (I.up.multiply(a[0], b[0]),
            I.up.add(I.up.multiply(a[1], b[0]), I.up.multiply(a[0], b[1])),
            I.up.add(I.up.add(I.up.multiply(a[2], b[0]),
                              I.up.multiply(D(2), I.up.multiply(a[1], b[1]))),
                     I.up.multiply(a[0], b[2])),
            I.up.add(I.up.add(I.up.multiply(a[3], b[0]),
                              I.up.multiply(D(3), I.up.multiply(a[2], b[1]))),
                     I.up.add(I.up.multiply(D(3), I.up.multiply(a[1], b[2])),
                              I.up.multiply(a[0], b[3]))))


def inv(a, lower):
    m2, m3, m4 = lower**2, lower**3, lower**4
    return (I.up.divide(D(1), lower),
            I.up.divide(a[1], m2),
            I.up.add(I.up.divide(a[2], m2), I.up.divide(D(2)*a[1]**2, m3)),
            I.up.add(I.up.add(I.up.divide(a[3], m2),
                              I.up.divide(D(6)*a[1]*a[2], m3)),
                     I.up.divide(D(6)*a[1]**3, m4)))


def div(a, b, lower):
    return mul(a, inv(b, lower))


def f_derivative(order):
    value = D(0)
    for n in range(order, len(F)):
        falling = math.factorial(n) // math.factorial(n-order)
        coefficient = max(abs(F[n][0]), abs(F[n][1]))
        value = I.up.add(value, I.up.multiply(coefficient, D(falling)*H.G.R**(n-order)))
    for n in range(max(len(F)-1, order), 201):
        value = I.up.add(value, I.up.multiply(H.G.M, D(n**order)*H.G.R**(n-order)))
    first = I.up.multiply(H.G.M, D(201**order)*H.G.R**(201-order))
    return I.up.add(value, I.up.divide(first, D('.989')))


derivatives = [f_derivative(order) for order in range(13)]
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        base = i + j + 1
        denominator = D(math.factorial(i)*math.factorial(j))
        row.append(tuple(I.up.divide(D(5**r)*derivatives[base+r], denominator)
                         for r in range(4)))
    matrix.append(row)

zero = (D(0),)*4
one = (D(1),D(0),D(0),D(0))
lower = [[zero for _ in range(N)] for _ in range(N)]
diagonal = []
for k in range(N):
    pivot = matrix[k][k]
    for j in range(k): pivot = add(pivot, mul(mul(lower[k][j], lower[k][j]), diagonal[j]))
    diagonal.append(pivot); lower[k][k] = one
    if k == N-1: break
    for row in range(k+1, N):
        value = matrix[row][k]
        for j in range(k): value = add(value, mul(mul(lower[row][j], lower[k][j]), diagonal[j]))
        lower[row][k] = div(value, pivot, floors[k])

threshold = D('2.16e-23')
result = {
    'domain': ['0','0.01'],
    'global_denominator_floors': [str(x) for x in floors],
    'fifth_pivot_absolute_norms_orders_zero_through_three': [str(x) for x in diagonal[-1]],
    'third_derivative_total_norm_bound': str(diagonal[-1][3]),
    'required_third_derivative_bound': str(threshold),
    'coarse_global_norm_sufficient': diagonal[-1][3] < threshold,
    'cancellation_retained': False,
    'directed_decimal_rounding': True,
    'rh_proved': False,
}

if __name__ == '__main__':
    output = ROOT / 'results' / 'central-rank-five-global-c3-norm-probe.json'
    output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
