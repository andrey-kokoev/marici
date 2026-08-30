"""Finite checks for the hidden-constructor gate."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][c]
        m[r] = [x / p for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [x - q * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def compress(j, x):
    return mul(mul(transpose(j), x), j)


q = [[1, 0], [0, 1]]
j_min = [[1, 0], [0, 1]]
j_dark = [[1, 0], [0, 1], [0, 0]]
z = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
m = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]

assert mul(transpose(j_min), j_min) == q
assert mul(transpose(j_dark), j_dark) == q
assert len(j_min) - rank(j_min) == 0
assert len(j_dark) - rank(j_dark) == 1
assert compress(j_dark, z) == [[0, 0], [0, 0]]
assert compress(j_dark, m) == [[0, 0], [0, 0]]

# Rational surrogate for the pi/4 rotation: columns are scaled by sqrt(2).
# Scaling does not affect the zero/nonzero exposure claim.
u_scaled = [[1, 0, -1], [0, 1, 0], [1, 0, 1]]
j_rot_scaled = mul(u_scaled, j_dark)
exposed_scaled = compress(j_rot_scaled, m)
assert exposed_scaled == [[2, 0], [0, 0]]

print("minimal Gram rank:", rank(j_min))
print("nonminimal dark dimension:", len(j_dark) - rank(j_dark))
print("initial hidden compression:", compress(j_dark, m))
print("transport-exposed compression (scaled):", exposed_scaled)
print("PASS: positivity alone does not exclude a hidden constructor")
