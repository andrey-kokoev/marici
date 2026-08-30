"""Deep-source correlated Taylor budget for endpoint-cell Hessian variation."""
import itertools, json, math, os
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_pivot_taylor_interval as P

I = P.I
P.ORDER = int(os.environ.get('MARICI_TAYLOR_ORDER', '7'))
P.multiindices = [key for key in itertools.product(range(P.ORDER + 1), repeat=P.VARIABLES)
                  if sum(key) <= P.ORDER]
ROOT = Path(__file__).parents[1]
payload = json.loads((ROOT / 'results' / 'central-H-degree-eleven-interval.json').read_text())
f = [(D(a), D(b)) for a, b in
     payload['F_coefficients_through_degree_forty_nine']]
CHART_CENTER = tuple(D(x) for x in os.environ.get(
    'MARICI_TAYLOR_CENTER', ','.join(['.01'] * P.VARIABLES)).split(','))
if len(CHART_CENTER) != P.VARIABLES:
    raise ValueError('MARICI_TAYLOR_CENTER must contain one coordinate per Taylor variable')


def up_pow(base, exponent):
    return I.up.power(base, D(exponent))


def tail_derivative(i, j, degree):
    order = i + j + degree
    value = D(0)
    for p in range(len(f), 201):
        falling = math.factorial(p) // math.factorial(p - order)
        term = I.up.multiply(P.M, I.up.multiply(
            D(falling), up_pow(P.CENTER, p - order)))
        value = I.up.add(value, I.up.divide(
            term, D(math.factorial(i) * math.factorial(j))))
    first = I.up.divide(
        I.up.multiply(P.M, I.up.multiply(
            D(201 ** order), up_pow(P.CENTER, 201 - order))),
        D(math.factorial(i) * math.factorial(j)))
    return I.up.add(value, I.up.divide(first, D('.989')))


def inject_tail(jet, i, j):
    out = dict(jet)
    for key in P.multiindices:
        denominator = math.prod(math.factorial(component) for component in key)
        error = I.up.divide(tail_derivative(i, j, sum(key)), D(denominator))
        out[key] = I.add(out.get(key, I.box(0)), (error.copy_negate(), error))
    return out


nodes = []
for variable in range(P.VARIABLES):
    key = tuple(1 if i == variable else 0 for i in range(P.VARIABLES))
    nodes.append({P.zero: I.box(CHART_CENTER[variable]), key: I.box(1)})
tables = []
h = [P.constant(1)] + [P.constant(0)] * (len(f) - 1)
for node in nodes:
    powers = [P.power(node, q) for q in range(len(f))]
    h = [P.add_all(P.mul(h[d-q], powers[q]) for q in range(d+1))
         for d in range(len(f))]
    tables.append(h)
matrix = []
for i in range(P.VARIABLES):
    row = []
    for j in range(P.VARIABLES):
        value = P.constant(0)
        for n in range(1, len(f)):
            for k in range(i, n):
                ell = n - 1 - k
                if ell >= j:
                    value = P.add(value, P.scale(
                        P.mul(tables[i][k-i], tables[j][ell-j]), f[n]))
        row.append(inject_tail(value, i, j))
    matrix.append(row)
lower = [[P.constant(0) for _ in range(P.VARIABLES)] for _ in range(P.VARIABLES)]
diagonal = []
for k in range(P.VARIABLES):
    pivot = matrix[k][k]
    for j in range(k):
        pivot = P.sub(pivot, P.mul(P.mul(lower[k][j], lower[k][j]), diagonal[j]))
    diagonal.append(pivot)
    lower[k][k] = P.constant(1)
    for row in range(k + 1, P.VARIABLES):
        value = matrix[row][k]
        for j in range(k):
            value = P.sub(value, P.mul(P.mul(lower[row][j], lower[k][j]), diagonal[j]))
        lower[row][k] = P.div(value, pivot)

fifth = diagonal[-1]
R = D('.0005')


def falling(component, count):
    if component < count:
        return 0
    return math.factorial(component) // math.factorial(component - count)


degree_budgets = {}
row_variation = [D(0)] * P.VARIABLES
for degree in range(3, P.ORDER + 1):
    rows = []
    for v in range(P.VARIABLES):
        total = D(0)
        for w in range(P.VARIABLES):
            for key, interval in fifth.items():
                if sum(key) != degree:
                    continue
                factor = key[v] * (key[w] - (1 if v == w else 0))
                if factor > 0:
                    term = I.up.multiply(
                        I.up.multiply(max(abs(interval[0]), abs(interval[1])),
                                      D(factor)),
                        up_pow(R, degree - 2))
                    total = I.up.add(total, term)
        rows.append(total)
        row_variation[v] = I.up.add(row_variation[v], total)
    degree_budgets[str(degree)] = [str(x) for x in rows]

result = {
    'source_degree': len(f) - 1,
    'taylor_degree': P.ORDER,
    'taylor_center': [str(x) for x in CHART_CENTER],
    'budget_radius': str(R),
    'hessian_row_variation_budgets_by_degree': degree_budgets,
    'hessian_row_variation_through_degree_seven': [str(x) for x in row_variation],
    'maximum_hessian_row_variation_through_degree_seven': str(max(row_variation)),
    'degree_eight_and_higher_remainder_included': False,
    'directed_decimal_rounding': True,
    'directed_scalar_arithmetic_version': 2,
    'interval_certified_for_finite_jet': True,
    'rh_proved': False,
}

if __name__ == '__main__':
    output = ROOT / 'results' / 'central-rank-five-hessian-taylor-deep.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
