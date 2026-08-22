"""Natural interval Hessian enclosure on one rank-five node cell."""
import json, math
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

import central_rank_five_hessian_interval_anchor as H

I, N, Z, F, DEPTH = H.I, H.N, H.Z, H.F, H.DEPTH


def homogeneous(nodes):
    out = [I.box(1)] + [Z] * (DEPTH - 1)
    for node in nodes:
        powers = [I.powi(node, q) for q in range(DEPTH)]
        out = [I.add(*(I.mul(out[d-q], powers[q]) for q in range(d+1)))
               for d in range(DEPTH)]
    return out


def derivative_h(h, x):
    return [Z] + [I.add(*(I.scale(I.mul(I.powi(x, q-1), h[d-q]), q)
                          for q in range(1, d+1))) for d in range(1, DEPTH)]


def second_h(h, dh, nodes, i, v, w):
    if v > i or w > i:
        return [Z] * DEPTH
    out = [Z]
    for degree in range(1, DEPTH):
        terms = []
        for q in range(1, degree + 1):
            if v == w and q >= 2:
                terms.append(I.scale(I.mul(I.powi(nodes[v], q-2), h[i][degree-q]),
                                     q * (q-1)))
            terms.append(I.scale(I.mul(I.powi(nodes[v], q-1), dh[i][w][degree-q]), q))
        out.append(I.add(*terms))
    return out


@lru_cache(maxsize=None)
def tail(i, j, derivative_degree, multiplicity):
    order = i + j + derivative_degree
    value = D(0)
    for p in range(DEPTH - 1, 201):
        falling = math.factorial(p) // math.factorial(p - order)
        value = I.up.add(value, I.up.divide(
            I.up.multiply(D(multiplicity) * H.G.M,
                          D(falling) * H.G.R ** (p-order)),
            D(math.factorial(i) * math.factorial(j))))
    first = I.up.divide(
        I.up.multiply(D(multiplicity) * H.G.M,
                      D(201**order) * H.G.R ** (201-order)),
        D(math.factorial(i) * math.factorial(j)))
    return I.up.add(value, I.up.divide(first, D('.989')))


def evaluate(bounds):
    nodes = [(D(a), D(b)) for a, b in bounds]
    h = [homogeneous(nodes[:i+1]) for i in range(N)]
    dh = [[derivative_h(h[i], nodes[v]) if v <= i else [Z] * DEPTH
           for v in range(N)] for i in range(N)]
    d2h = [[[[Z] * DEPTH for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for v in range(N):
            for w in range(N):
                d2h[i][v][w] = second_h(h, dh, nodes, i, v, w)

    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            value0 = Z
            gradients = [Z for _ in range(N)]
            hessians = [[Z for _ in range(N)] for _ in range(N)]
            for n in range(1, len(F)):
                for k in range(i, n):
                    ell = n - 1 - k
                    if ell < j: continue
                    value0 = I.add(value0, I.mul(F[n], I.mul(h[i][k-i], h[j][ell-j])))
            error0 = tail(i, j, 0, 1)
            value0 = I.add(value0, (error0.copy_negate(), error0))
            for v in range(N):
                value1 = Z
                for n in range(1, len(F)):
                    for k in range(i, n):
                        ell = n - 1 - k
                        if ell < j: continue
                        factor = Z
                        if v <= i: factor = I.add(factor, I.mul(dh[i][v][k-i], h[j][ell-j]))
                        if v <= j: factor = I.add(factor, I.mul(h[i][k-i], dh[j][v][ell-j]))
                        value1 = I.add(value1, I.mul(F[n], factor))
                error1 = tail(i, j, 1, int(v <= i) + int(v <= j))
                gradients[v] = I.add(value1, (error1.copy_negate(), error1))
                for w in range(N):
                    value2 = Z
                    for n in range(1, len(F)):
                        for k in range(i, n):
                            ell = n - 1 - k
                            if ell < j: continue
                            factor = Z
                            if v <= i: factor = I.add(factor, I.mul(d2h[i][v][w][k-i], h[j][ell-j]))
                            if w <= j and v <= i: factor = I.add(factor, I.mul(dh[i][v][k-i], dh[j][w][ell-j]))
                            if w <= i and v <= j: factor = I.add(factor, I.mul(dh[i][w][k-i], dh[j][v][ell-j]))
                            if v <= j: factor = I.add(factor, I.mul(h[i][k-i], d2h[j][v][w][ell-j]))
                            value2 = I.add(value2, I.mul(F[n], factor))
                    error2 = tail(i, j, 2, 4)
                    hessians[v][w] = I.add(value2, (error2.copy_negate(), error2))
            row.append((value0, gradients, hessians))
        matrix.append(row)

    lower = [[H.dconstant(Z) for _ in range(N)] for _ in range(N)]
    diagonal = []
    for k in range(N):
        pivot = matrix[k][k]
        for j in range(k): pivot = H.dsub(pivot, H.dmul(H.dmul(lower[k][j], lower[k][j]), diagonal[j]))
        diagonal.append(pivot); lower[k][k] = H.dconstant(I.box(1))
        for row in range(k+1, N):
            value = matrix[row][k]
            for j in range(k): value = H.dsub(value, H.dmul(H.dmul(lower[row][j], lower[k][j]), diagonal[j]))
            lower[row][k] = H.ddiv(value, pivot)
    final = diagonal[-1]
    row_sums = [sum((max(abs(x[0]), abs(x[1])) for x in final[2][v]), D(0)) for v in range(N)]
    ceiling = D('5.4134e-26')
    return {'node_intervals': [[str(a),str(b)] for a,b in nodes],
            'hessian_absolute_row_sums': [str(x) for x in row_sums],
            'maximum_hessian_absolute_row_sum': str(max(row_sums)),
            'required_ceiling': str(ceiling),
            'cell_hessian_bound_sufficient': max(row_sums) < ceiling,
            'analytic_tail_bounds_included': True,
            'natural_interval_extension': True, 'rh_proved': False}


if __name__ == '__main__':
    result = evaluate([('.0095','.01')] * 5)
    output = Path(__file__).parents[1] / 'results' / 'central-rank-five-hessian-interval-cell.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
