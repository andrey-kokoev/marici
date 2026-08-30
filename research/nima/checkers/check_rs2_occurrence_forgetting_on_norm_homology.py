"""Exact induced-map audit for occurrence forgetting on C3 norm homology."""

import json
from pathlib import Path


P = 3


def rref(a, p=P):
    a = [[x % p for x in row] for row in a]
    pivots = []
    row = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(inv * x) % p for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [(x - c * y) % p for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


def kernel_basis(a):
    rr, pivots = rref(a)
    free = [j for j in range(len(a[0])) if j not in pivots]
    basis = []
    for f in free:
        v = [0] * len(a[0])
        v[f] = 1
        for i, p in enumerate(pivots):
            v[p] = (-rr[i][f]) % P
        basis.append(v)
    return basis


N = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
N2 = [[0] * 6 for _ in range(6)]
for c in range(2):
    for i in range(3):
        for j in range(3):
            N2[2 * i + c][2 * j + c] = 1

# Source order is (12|23,12|31,23|31,23|12,31|12,31|23).
F = [
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1],
]
assert multiply(F, N2) == multiply(N, F)

ker_domain = kernel_basis(N2)
images = multiply(F, transpose(ker_domain))
im_target = transpose(N)  # column span of N
induced_rank = rank(transpose(im_target) + transpose(images)) - rank(transpose(im_target))
assert induced_rank == 1

domain_h_dim = len(ker_domain) - rank(N2)
target_h_dim = len(kernel_basis(N)) - rank(N)
assert (domain_h_dim, target_h_dim) == (2, 1)

# The all-positive scalar readout remains zero on ker(N2).
R6 = [[1, 1, 1, 1, 1, 1]]
assert rank(multiply(R6, transpose(ker_domain))) == 0

# Explicit orbit-difference representatives map to the same target class.
v_left = [[1], [0], [-1], [0], [0], [0]]
v_right = [[0], [1], [0], [-1], [0], [0]]
assert multiply(F, v_left) == multiply(F, v_right)

result = {
    "schema": "marici.rs2.occurrence-forgetting-norm-homology.v1",
    "domain": {"module": "F3[C3]^2", "homology_dimension": domain_h_dim},
    "target": {"module": "F3[C3]", "homology_dimension": target_h_dim},
    "source_map": "occurrence forgetting F: six lower-denominator occurrences to three marked Cuts",
    "chain_map": True,
    "induced_homology_rank": induced_rank,
    "induced_kernel_dimension": domain_h_dim - induced_rank,
    "all_positive_scalar_readout_rank_on_homology": 0,
    "verdict": (
        "Occurrence forgetting gives a canonical nonzero quotient H(N)^2 -> H(N) "
        "while the scalar period readout remains zero. This is a source-derived "
        "coefficient/relative readout, not yet a physical period."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs2-occurrence-forgetting-norm-homology.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
