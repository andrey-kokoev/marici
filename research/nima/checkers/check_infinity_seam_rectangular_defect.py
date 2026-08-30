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
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if m[r][col]), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        scale = m[pivot_row][col]
        m[pivot_row] = [x / scale for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col]:
                scale = m[r][col]
                m[r] = [x - scale * y for x, y in zip(m[r], m[pivot_row])]
        pivot_row += 1
    return pivot_row


w = [
    [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
]
wwt = matmul(w, transpose(w))
defect = subtract(identity(4), matmul(transpose(w), w))

assert wwt == identity(2)
assert rank(w) == 2
assert rank(defect) == 2

w0 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
assert rank(w0) == 1
assert matmul(w0, transpose(w0)) != identity(2)

unitary = identity(2)
unitary_defect = subtract(identity(2), matmul(transpose(unitary), unitary))
assert rank(unitary_defect) == 0

result = {
    "schema": "marici.nima.infinity-seam-rectangular-defect.v1",
    "surjective_rectangular_rank": rank(w),
    "surjective_rectangular_defect_rank": rank(defect),
    "equal_dimension_singular_rank": rank(w0),
    "unitary_defect_rank": rank(unitary_defect),
    "surjectivity_implies_zero_defect": False,
    "equal_dimensions_imply_coherence": False,
}
print(json.dumps(result, indent=2, sort_keys=True))

