from fractions import Fraction


def zero(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = 1
    return out


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def comm(a, b):
    return add(mul(a, b), scale(-1, mul(b, a)))


def endpoint_matrices(highest_weight):
    # Basis x^(n-k)y^k, k=0,...,n.
    n = highest_weight
    dim = n + 1
    e, f, h = zero(dim), zero(dim), zero(dim)
    for k in range(dim):
        h[k][k] = n - 2 * k
        if k > 0:
            e[k - 1][k] = k
        if k < n:
            f[k + 1][k] = n - k
    return e, f, h


passed = 0
total = 0

for grade in range(13):
    e, f, h = endpoint_matrices(2 * grade)
    dim = 2 * grade + 1
    omega = add(add(mul(h, h), scale(2, h)), scale(4, mul(f, e)))
    gates = [
        comm(h, e) == scale(2, e),
        comm(h, f) == scale(-2, f),
        comm(e, f) == h,
        omega == scale(4 * grade * (grade + 1), eye(dim)),
        Fraction(4 * grade * (grade + 1)) != Fraction(-3, 4),
    ]
    passed += sum(gates)
    total += len(gates)

# Direct oscillator Casimir on monomials q^k. H q^k=(k+1/2)q^k and
# 4FE q^k=-(k+2)(k+1)q^k.
for degree in range(21):
    h = Fraction(2 * degree + 1, 2)
    omega = h * h + 2 * h - (degree + 2) * (degree + 1)
    passed += omega == Fraction(-3, 4)
    total += 1

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
