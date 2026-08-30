import json
from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def rank(a):
    m = [row[:] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = m[r][c]
        m[r] = [x / scale for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                scale = m[i][c]
                m[i] = [x - scale * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


# Compression of multiplication by z to span{1,z,z^2}.
t = [
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
]

# Reverse Hankel leakage of multiplication by conjugate(z): the constant mode
# crosses to the negative Hardy sector.
h = [[Fraction(1), Fraction(0), Fraction(0)]]

output_defect = subtract(identity(3), matmul(t, transpose(t)))
h_star_h = matmul(transpose(h), h)

assert output_defect == h_star_h
assert rank(output_defect) == 1

# The full four-mode cyclic boundary transport is unitary and therefore its
# total Gram is blind to the same phase shift.
u = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
]
assert matmul(transpose(u), u) == identity(4)

result = {
    "schema": "marici.nima.outer-normalized-hankel-defect.v1",
    "full_boundary_transport_unitary": True,
    "total_gram_detects_inner_shift": False,
    "ordered_cut_defect_rank": rank(output_defect),
    "toeplitz_hankel_identity": True,
    "one_matrix_element_is_finite_falsifier": True,
}
print(json.dumps(result, indent=2, sort_keys=True))

