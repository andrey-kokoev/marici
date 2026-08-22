"""Directed fifth-pivot Hessian at a chosen rank-five anchor."""
import json, math, os
from decimal import Decimal as D
from functools import lru_cache
from pathlib import Path

if os.environ.get('MARICI_RANK') == '6':
    import central_rank_six_loewner_anchor as G
else:
    import central_rank_five_loewner_grid as G

I = G.I
N = G.N
Z = I.box(0)
payload = json.loads((Path(__file__).parents[1] / 'results' /
                      'central-H-degree-eleven-interval.json').read_text())
F = [(D(a), D(b)) for a, b in payload['F_coefficients_through_degree_thirty_nine']]
DEPTH = len(F)


def dconstant(value):
    return value, [Z for _ in range(N)], [[Z for _ in range(N)] for _ in range(N)]


def dadd(a, b):
    return (I.add(a[0], b[0]),
            [I.add(a[1][v], b[1][v]) for v in range(N)],
            [[I.add(a[2][v][w], b[2][v][w]) for w in range(N)] for v in range(N)])


def dneg(a):
    return I.neg(a[0]), [I.neg(x) for x in a[1]], [[I.neg(x) for x in row] for row in a[2]]


def dsub(a, b):
    return dadd(a, dneg(b))


def dmul(a, b):
    value = I.mul(a[0], b[0])
    gradient = [I.add(I.mul(a[1][v], b[0]), I.mul(a[0], b[1][v])) for v in range(N)]
    hessian = [[I.add(
        I.mul(a[2][v][w], b[0]), I.mul(a[1][v], b[1][w]),
        I.mul(a[1][w], b[1][v]), I.mul(a[0], b[2][v][w]))
        for w in range(N)] for v in range(N)]
    return value, gradient, hessian


def dinv(a):
    inverse = I.inv(a[0]); inverse2 = I.mul(inverse, inverse); inverse3 = I.mul(inverse2, inverse)
    gradient = [I.neg(I.mul(a[1][v], inverse2)) for v in range(N)]
    hessian = [[I.sub(I.scale(I.mul(I.mul(a[1][v], a[1][w]), inverse3), 2),
                       I.mul(a[2][v][w], inverse2))
                for w in range(N)] for v in range(N)]
    return inverse, gradient, hessian


def ddiv(a, b):
    return dmul(a, dinv(b))


def homogeneous(nodes):
    h = [I.box(1)] + [Z] * (DEPTH - 1)
    for node in nodes:
        powers = [I.powi(I.box(node), q) for q in range(DEPTH)]
        h = [I.add(*(I.mul(h[d-q], powers[q]) for q in range(d+1))) for d in range(DEPTH)]
    return h


def derivative_h(h, x):
    return [Z] + [I.add(*(I.scale(I.mul(I.powi(I.box(x), q-1), h[d-q]), q)
                          for q in range(1, d+1))) for d in range(1, DEPTH)]


def second_h(h, dh, nodes, i, v, w):
    if v > i or w > i:
        return [Z] * DEPTH
    out = [Z]
    for degree in range(1, DEPTH):
        terms = []
        for q in range(1, degree + 1):
            if v == w and q >= 2:
                terms.append(I.scale(I.mul(I.powi(I.box(nodes[v]), q - 2), h[i][degree - q]), q * (q - 1)))
            terms.append(I.scale(I.mul(I.powi(I.box(nodes[v]), q - 1), dh[i][w][degree - q]), q))
        out.append(I.add(*terms))
    return out


@lru_cache(maxsize=None)
def analytic_tail(i, j, derivative_degree, multiplicity):
    order = i + j + 1 + derivative_degree
    value = D(0)
    for p in range(DEPTH - 1, 201):
        falling = math.factorial(p) // math.factorial(p - order)
        value = I.up.add(value, I.up.divide(I.up.multiply(D(multiplicity) * G.M, D(falling) * G.R ** (p - order)),
                                            D(math.factorial(i) * math.factorial(j))))
    first = I.up.divide(I.up.multiply(D(multiplicity) * G.M, D(201 ** order) * G.R ** (201 - order)),
                        D(math.factorial(i) * math.factorial(j)))
    return I.up.add(value, I.up.divide(first, D('.989')))


def evaluate(nodes):
    nodes = [D(x) for x in nodes]
    h = [homogeneous(nodes[:i + 1]) for i in range(N)]
    dh = [[derivative_h(h[i], nodes[v]) if v <= i else [Z] * DEPTH for v in range(N)] for i in range(N)]
    d2h = [[[[Z] * DEPTH for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for v in range(N):
            for w in range(N):
                d2h[i][v][w] = second_h(h, dh, nodes, i, v, w)

    base = G.matrix(nodes)
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            gradients = [Z for _ in range(N)]
            hessians = [[Z for _ in range(N)] for _ in range(N)]
            for v in range(N):
                value = Z
                for n in range(1, len(F)):
                    for k in range(i, n):
                        ell = n - 1 - k
                        if ell < j: continue
                        factor = Z
                        if v <= i: factor = I.add(factor, I.mul(dh[i][v][k-i], h[j][ell-j]))
                        if v <= j: factor = I.add(factor, I.mul(h[i][k-i], dh[j][v][ell-j]))
                        value = I.add(value, I.mul(F[n], factor))
                error = analytic_tail(i, j, 1, int(v <= i) + int(v <= j))
                gradients[v] = I.add(value, (error.copy_negate(), error))
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
                    error2 = analytic_tail(i, j, 2, 4)
                    hessians[v][w] = I.add(value2, (error2.copy_negate(), error2))
            row.append((base[i][j], gradients, hessians))
        matrix.append(row)

    lower = [[dconstant(Z) for _ in range(N)] for _ in range(N)]
    diagonal = []
    for k in range(N):
        pivot = matrix[k][k]
        for j in range(k): pivot = dsub(pivot, dmul(dmul(lower[k][j], lower[k][j]), diagonal[j]))
        diagonal.append(pivot); lower[k][k] = dconstant(I.box(1))
        for row in range(k + 1, N):
            value = matrix[row][k]
            for j in range(k): value = dsub(value, dmul(dmul(lower[row][j], lower[k][j]), diagonal[j]))
            lower[row][k] = ddiv(value, pivot)
    final = diagonal[-1]
    row_sums = [sum((max(abs(x[0]), abs(x[1])) for x in final[2][v]), D(0)) for v in range(N)]
    return {'anchor': [str(x) for x in nodes],
            'derivative_intervals': [[str(a), str(b)] for a,b in final[1]],
            'hessian_intervals': [[[str(a),str(b)] for a,b in row] for row in final[2]],
            'hessian_absolute_row_sums': [str(x) for x in row_sums],
            'half_grid_l1_derivative_variation_bounds': [str(D('.0005') * x) for x in row_sums],
            'analytic_tail_bounds_included': True, 'rh_proved': False}


if __name__ == '__main__':
    if N == 6:
        anchors = [['0'] * N, ['.01'] * N,
                   ['0', '0', '.002', '.004', '.007', '.01']]
        result = {'anchors': [evaluate(anchor) for anchor in anchors],
                  'rh_proved': False}
        output = Path(__file__).parents[1] / 'results' / 'central-rank-six-hessian-interval-anchor.json'
        output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({'anchors': [
            {k:v for k,v in row.items() if k != 'hessian_intervals'}
            for row in result['anchors']], 'rh_proved': False}, indent=2))
    else:
        result = evaluate(['.01'] * 5)
        output = Path(__file__).parents[1] / 'results' / 'central-rank-five-hessian-interval-anchor.json'
        output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({k:v for k,v in result.items() if k != 'hessian_intervals'}, indent=2))
