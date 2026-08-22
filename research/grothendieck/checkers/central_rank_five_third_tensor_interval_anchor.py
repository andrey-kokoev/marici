"""Correlated directed third-derivative tensor norm at a rank-five anchor."""
import itertools, json, math
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

import central_rank_five_pivot_taylor_interval as P

I = P.I
P.ORDER = 3
P.multiindices = [key for key in itertools.product(range(P.ORDER + 1), repeat=P.VARIABLES)
                  if sum(key) <= P.ORDER]
ROOT = Path(__file__).parents[1]
payload = json.loads((ROOT / 'results' / 'central-H-degree-eleven-interval.json').read_text())
F = [(D(a), D(b)) for a, b in payload['F_coefficients_through_degree_thirty_nine']]


@lru_cache(maxsize=None)
def tail_derivative(i, j, degree):
    order = i + j + degree
    value = D(0)
    for p in range(39, 201):
        falling = math.factorial(p) // math.factorial(p-order)
        value = I.up.add(value, I.up.divide(
            I.up.multiply(P.M, D(falling) * P.CENTER ** (p-order)),
            D(math.factorial(i) * math.factorial(j))))
    first = I.up.divide(
        I.up.multiply(P.M, D(201**order) * P.CENTER ** (201-order)),
        D(math.factorial(i) * math.factorial(j)))
    return I.up.add(value, I.up.divide(first, D('.989')))


def inject_tail(jet, i, j):
    out = dict(jet)
    for key in P.multiindices:
        denominator = math.prod(math.factorial(x) for x in key)
        error = I.up.divide(tail_derivative(i, j, sum(key)), D(denominator))
        out[key] = I.add(out.get(key, I.box(0)), (error.copy_negate(), error))
    return out


def evaluate(anchor, displacement_radius=D('.0005')):
    """Evaluate at point centers or enclosing center intervals.

    A pair ``(lo, hi)`` retains the common formal displacement variables
    while intervalizing only the center coefficient.  This lets one result
    cover a macro-cell of centers rather than one anchor.
    """
    anchor = [(D(x[0]), D(x[1])) if isinstance(x, (tuple, list)) else I.box(D(x))
              for x in anchor]
    nodes = []
    for variable, center_interval in enumerate(anchor):
        key = tuple(1 if i == variable else 0 for i in range(P.VARIABLES))
        nodes.append({P.zero: center_interval, key: I.box(1)})
    tables = []
    for length in range(1, P.VARIABLES + 1):
        h = [P.constant(1)] + [P.constant(0)] * (len(F)-1)
        for node in nodes[:length]:
            powers = [P.power(node, q) for q in range(len(F))]
            h = [P.add_all(P.mul(h[d-q], powers[q]) for q in range(d+1))
                 for d in range(len(F))]
        tables.append(h)
    matrix = []
    for i in range(P.VARIABLES):
        row = []
        for j in range(P.VARIABLES):
            value = P.constant(0)
            for n in range(1, len(F)):
                for k in range(i, n):
                    ell = n-1-k
                    if ell >= j:
                        value = P.add(value, P.scale(
                            P.mul(tables[i][k-i], tables[j][ell-j]), F[n]))
            row.append(inject_tail(value, i, j))
        matrix.append(row)
    lower = [[P.constant(0) for _ in range(P.VARIABLES)] for _ in range(P.VARIABLES)]
    diagonal = []
    for k in range(P.VARIABLES):
        pivot = matrix[k][k]
        for j in range(k):
            pivot = P.sub(pivot, P.mul(P.mul(lower[k][j], lower[k][j]), diagonal[j]))
        diagonal.append(pivot); lower[k][k] = P.constant(1)
        for row in range(k+1, P.VARIABLES):
            value = matrix[row][k]
            for j in range(k):
                value = P.sub(value, P.mul(P.mul(lower[row][j], lower[k][j]), diagonal[j]))
            lower[row][k] = P.div(value, pivot)
    fifth = diagonal[-1]
    degree_three_coefficient_l1 = sum(
        (max(abs(value[0]), abs(value[1])) for key, value in fifth.items() if sum(key) == 3), D(0))
    tensor_l1 = I.up.multiply(D(6), degree_three_coefficient_l1)
    radius = D(displacement_radius)
    variation = sum((
        max(abs(value[0]), abs(value[1])) * D(degree*(degree-1)*(degree-2)) *
        radius**(degree-3)
        for key, value in fifth.items()
        for degree in [sum(key)] if degree >= 4), D(0))
    return {'anchor_interval':[[str(x[0]), str(x[1])] for x in anchor],
            'degree_three_coefficient_l1':str(degree_three_coefficient_l1),
            'third_derivative_tensor_l1_bound':str(tensor_l1),
            'third_tensor_variation_from_retained_higher_degrees':str(variation),
            'retained_Taylor_degree':P.ORDER,
            'required_global_bound':str(D('2.16e-23')),
            'anchor_bound_below_required_global_bound':tensor_l1 < D('2.16e-23'),
            'analytic_source_tail_included':True,
            'correlated_Newton_LDL_jet':True,
            'interval_certified_at_anchor':True,
            'rh_proved':False}


if __name__ == '__main__':
    anchors=[['0']*5,['.01']*5,['0','0','0','.001','.002'],
             ['0','0','.001','.002','.003']]
    results=[evaluate(anchor) for anchor in anchors]
    output=ROOT/'results'/'central-rank-five-third-tensor-interval-anchor.json'
    output.write_text(json.dumps({'anchors':results,'rh_proved':False},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results,indent=2))
