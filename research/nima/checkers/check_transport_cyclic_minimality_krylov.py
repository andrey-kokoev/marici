"""Finite Krylov closure checks for transport-cyclic minimality."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def hstack(columns):
    return [[col[i][0] for col in columns] for i in range(len(columns[0]))]


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(m[0])):
        p = next((i for i in range(r, len(m)) if m[i][c]), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        q = m[r][c]
        m[r] = [x / q for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [x - q * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


j = [[1], [0], [0]]
t = [[0, 0, 0], [1, 0, 0], [0, 1, 0]]
zero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

tj = mul(t, j)
t2j = mul(t, tj)
ranks = [rank(j), rank(hstack([j, tj])), rank(hstack([j, tj, t2j]))]
assert ranks == [1, 2, 3]

seed_gram = mul(transpose(j), j)
assert seed_gram == [[1]]
assert mul(transpose(j), j) == seed_gram  # same seed for zero transport
assert rank(hstack([j, mul(zero, j)])) == 1

# Word moments expose the source difference before the seed Gram can.
moment_t_t = mul(transpose(tj), tj)
moment_zero = mul(transpose(mul(zero, j)), mul(zero, j))
assert moment_t_t == [[1]]
assert moment_zero == [[0]]

print("Krylov ranks by word length:", ranks)
print("shared scalar seed Gram:", seed_gram)
print("first transport moment, shift versus zero:", moment_t_t, moment_zero)
print("PASS: stabilized transport orbit, not static image, is the minimal carrier")
