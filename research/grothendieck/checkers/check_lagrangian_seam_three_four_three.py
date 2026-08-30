from fractions import Fraction


def rank(rows):
    a = [list(map(Fraction, row)) for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


# Quadratic monomials in tangent variables x0,x1 and normal variables y0,y1.
# Coordinates are coefficients of the ten symmetric monomials.
tangent = [[1 if j == i else 0 for j in range(10)] for i in [0, 1, 2]]
mixed = [[1 if j == i else 0 for j in range(10)] for i in [3, 4, 5, 6]]
normal = [[1 if j == i else 0 for j in range(10)] for i in [7, 8, 9]]

gates = [
    len(tangent) == 3,
    len(mixed) == 4,
    len(normal) == 3,
    rank(tangent) == 3,
    rank(mixed) == 4,
    rank(normal) == 3,
    rank(tangent + mixed + normal) == 10,
    2 * 3 // 2 == 3,
    2 * 2 == 4,
]

passed = sum(gates)
total = len(gates)
print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
