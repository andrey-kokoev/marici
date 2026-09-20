"""Finite rational, commonly framed determinant transport; no source-lift claim.

Convention: I+K, K star L=K+L+KL. Matrices act on row vectors.
A frame at each retained state is INPUT, never inferred from scalar currents.
"""
from fractions import Fraction as Q


def matrix(a):
    a = tuple(tuple(Q(x) for x in row) for row in a)
    if not a or any(len(row) != len(a) for row in a):
        raise ValueError('expected a nonempty square rational matrix')
    return a


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b):
    if len(a) != len(b):
        raise ValueError('carrier mismatch')
    return matrix([[x+y for x, y in zip(r, s)] for r, s in zip(a, b)])


def neg(a):
    return matrix([[-x for x in r] for r in a])


def mul(a, b):
    if len(a) != len(b):
        raise ValueError('carrier mismatch')
    return matrix([[sum(a[i][k]*b[k][j] for k in range(len(a)))
                    for j in range(len(a))] for i in range(len(a))])


def eliminate(a):
    n = len(a)
    rows = [list(r)+list(s) for r, s in zip(a, identity(n))]
    det = Q(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if rows[j][i]), None)
        if pivot is None:
            raise ValueError('frame outside determinant-unit locus')
        if pivot != i:
            rows[i], rows[pivot] = rows[pivot], rows[i]
            det = -det
        p = rows[i][i]
        det *= p
        rows[i] = [x/p for x in rows[i]]
        for j in range(n):
            if j != i:
                p = rows[j][i]
                rows[j] = [x-p*y for x, y in zip(rows[j], rows[i])]
    return det, matrix([r[n:] for r in rows])


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def star(a, b):
    return add(add(a, b), mul(a, b))


def regularizer(k):
    return -trace(k)+trace(mul(k, k))/2


def anomaly(a, b):
    ab = mul(a, b)
    return trace(mul(mul(a, a), b))+trace(mul(a, mul(b, b)))+trace(mul(ab, ab))/2


class BasedPacket:
    def __init__(self, frames):
        if not frames:
            raise ValueError('source frames required; scalar moments are insufficient')
        self.frames = {s: matrix(f) for s, f in frames.items()}
        if len({len(f) for f in self.frames.values()}) != 1:
            raise ValueError('common carrier required before transport')
        self.inverses = {s: eliminate(f)[1] for s, f in self.frames.items()}

    def factor(self, source, target):
        return mul(self.inverses[source], self.frames[target])

    def relative(self, source, target):
        t = self.factor(source, target)
        return add(t, neg(identity(len(t))))

    def coordinates(self, source, target, expected_low=None):
        k = self.relative(source, target)
        low = (trace(k), trace(mul(k, k))/2)
        if expected_low is not None and low != tuple(expected_low):
            raise ValueError('source primitive/square compatibility failed')
        # Exact symbolic det3: determinant * exp(regularizer), no log branch.
        return {'primitive': low[0], 'square': low[1],
                'det3': (eliminate(self.factor(source, target))[0], regularizer(k))}
