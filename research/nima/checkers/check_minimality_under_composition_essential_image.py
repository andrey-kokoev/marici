"""Finite essential-image and transport-closure checks."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


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


j = [[1, 0], [0, 1]]
l = [[1, 0], [0, 1], [0, 0]]
c = mul(l, j)
assert rank(j) == 2
assert rank(l) == 2  # faithful
assert rank(c) == 2 < len(c)  # nonminimal in ambient R^3

p = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
i = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
z = sub(i, p)
assert mul(mul(transpose(c), z), c) == [[0, 0], [0, 0]]

# Scaled pi/4 rotation between essential e1 and dark e3.
u = [[1, 0, -1], [0, 1, 0], [1, 0, 1]]
off_diagonal = mul(mul(sub(i, p), u), p)
assert off_diagonal != [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Onto lens preserves minimality.
l_onto = [[1, 0], [0, 1]]
assert rank(mul(l_onto, j)) == len(l_onto)

print("faithful lens rank:", rank(l))
print("ambient dimension:", len(l))
print("dark dimension:", len(l) - rank(c))
print("transport closure defect (I-P)UP:", off_diagonal)
print("PASS: essential surjectivity, not faithfulness, preserves minimality")
