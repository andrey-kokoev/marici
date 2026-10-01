"""Exact equal-weight quadratic spectrum of the 153 comparison rows.

Coordinates and rows match check_comparison_backaction_floor.py.
This checks a trial stored-energy functional, not the sequential projection
update law or a physical energy normalization. No external dependencies.
"""
from itertools import product


def state(side, i):
    x = [0] * 6
    if i:
        x[3 * side + i - 1] = 1
    return x


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def arrow(side, edge):
    return sub(state(side, edge[1]), state(side, edge[0]))


edges = [(i, j) for i in range(4) for j in range(4) if i != j]
rows = [sub(arrow(0, e), arrow(1, f)) for e, f in product(edges, repeat=2)]
rows += [sub(state(0, i), state(1, j))
         for i, j in product(range(1, 4), repeat=2)]
assert len(rows) == 153
H = [[sum(r[i] * r[j] for r in rows) for j in range(6)]
     for i in range(6)]
expected = [[(99 * (i == j) - 24) if i // 3 == j // 3 else -1
             for j in range(6)] for i in range(6)]
assert H == expected
modes = [
    (24, [1, 1, 1, 1, 1, 1]),
    (30, [1, 1, 1, -1, -1, -1]),
    (99, [1, -1, 0, 0, 0, 0]),
    (99, [1, 1, -2, 0, 0, 0]),
    (99, [0, 0, 0, 1, -1, 0]),
    (99, [0, 0, 0, 1, 1, -2]),
]
for eigenvalue, v in modes:
    assert [sum(H[i][j] * v[j] for j in range(6)) for i in range(6)] == [eigenvalue * x for x in v]
for (_, v), (_, w) in product(modes, repeat=2):
    if v != w:
        assert sum(a * b for a, b in zip(v, w)) == 0
assert sum(H[i][i] for i in range(6)) == sum(e for e, _ in modes) == 450
print('Exact spectrum: 24, 30, 99, 99, 99, 99')
print('For K=kappa*H and M=mu*I: omega^2=(kappa/mu)*eigenvalue.')
print('All six modes positive; overall frequency and energy scales remain inputs.')
