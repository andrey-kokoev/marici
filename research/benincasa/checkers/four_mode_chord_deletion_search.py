"""Exact search for a Gaussian four-cycle born on chord-determinant deletion."""

import itertools
import json
from fractions import Fraction as F
from pathlib import Path


J = [[F(0), F(1)], [F(-1), F(0)]]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def det(a):
    a = [list(row) for row in a]
    out = F(1)
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        pv = a[col][col]
        out *= pv
        for r in range(col + 1, len(a)):
            q = a[r][col] / pv
            for j in range(col + 1, len(a)):
                a[r][j] -= q * a[col][j]
    return out


def inverse(a):
    n = len(a)
    aug = [list(a[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col]:
                q = aug[r][col]
                aug[r] = [aug[r][j] - q * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def positive_definite(x):
    return all(det([row[:k] for row in x[:k]]) > 0 for k in range(1, 5))


def block(x, xi, i, j):
    return [[x[i][j] / 2, F(0)], [F(0), xi[i][j] / 2]]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def cycle(x, xi, order):
    product = [[F(1), F(0)], [F(0), F(1)]]
    for i, j in zip(order, order[1:] + order[:1]):
        product = mul(product, mul(J, block(x, xi, i, j)))
    return trace(product)


def packet(diag, edges):
    x = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        x[i][i] = F(diag[i])
    for (i, j), value in zip(((0, 1), (1, 2), (2, 3), (3, 0)), edges):
        x[i][j] = x[j][i] = F(value)
    if not positive_definite(x):
        return None
    xi = inverse(x)
    local = tuple(x[i][i] * xi[i][i] / 4 for i in range(4))
    pair = tuple(x[i][j] * xi[i][j] / 4 for i, j in itertools.combinations(range(4), 2))
    assert pair[1] == 0  # 02 chord
    assert pair[4] == 0  # 13 chord
    cycles = tuple(cycle(x, xi, list(order)) for order in ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)))
    return {"diag": tuple(diag), "edges": tuple(edges), "local": local, "pair": pair, "cycles": cycles}


seen = {}
witness = None
tested = 0
edge_values = (-3, -2, -1, 1, 2, 3)
for common_diag in range(4, 11):
    for edges in itertools.product(edge_values, repeat=4):
        item = packet((common_diag,) * 4, edges)
        if item is None:
            continue
        tested += 1
        signature = item["local"] + item["pair"]
        previous = seen.get(signature)
        if previous is not None and previous["cycles"] != item["cycles"]:
            witness = (previous, item)
            break
        seen[signature] = item
    if witness:
        break


def serial(item):
    return {key: [str(x) for x in value] for key, value in item.items()}


result = {
    "schema": "marici.four-mode-chord-deletion-search.v1",
    "family": "V=1/2 diag(X,X^-1) in mode ordering, with X_02=X_13=0",
    "tested_positive_packets": tested,
    "signature": "det(A_i) and all det(C_ij)",
    "witness_found": witness is not None,
    "witness": None if witness is None else [serial(witness[0]), serial(witness[1])],
}

out = Path(__file__).parent / "results" / "four-mode-chord-deletion-search.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
