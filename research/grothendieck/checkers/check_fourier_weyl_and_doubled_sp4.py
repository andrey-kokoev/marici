from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(4)] for i in range(4)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def inverse_symplectic(s):
    # For the signed-permutation matrices used here, inverse equals transpose.
    return transpose(s)


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


def flatten(a):
    return [x for row in a for x in row]


J = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [-1, 0, 0, 0],
    [0, -1, 0, 0],
]


def symmetric_basis(i, j):
    a = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    a[i][j] = 1
    a[j][i] = 1
    if i == j:
        a[i][j] = 1
    return a


# Hamiltonian matrices for every quadratic in (q+,q-,p+,p-).
quadratics = [matmul(J, symmetric_basis(i, j)) for i in range(4) for j in range(i, 4)]
local_indices = [(0, 0), (0, 2), (2, 2), (1, 1), (1, 3), (3, 3)]
mixed_indices = [(0, 1), (0, 3), (1, 2), (2, 3)]
local = [matmul(J, symmetric_basis(i, j)) for i, j in local_indices]
mixed = [matmul(J, symmetric_basis(i, j)) for i, j in mixed_indices]

passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


gate(rank([flatten(x) for x in local]) == 6)
gate(rank([flatten(x) for x in mixed]) == 4)
gate(rank([flatten(x) for x in local + mixed]) == 10)

# Closure of all quadratic Hamiltonians under commutator.
basis_rows = [flatten(x) for x in quadratics]
gate(rank(basis_rows) == 10)
for x in quadratics:
    for y in quadratics:
        bracket = sub(matmul(x, y), matmul(y, x))
        gate(rank(basis_rows + [flatten(bracket)]) == 10)

# Fourier quarter-turn in the plus phase plane preserves that local factor.
S = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, 1],
]
for x in local[:3]:
    conjugate = matmul(matmul(S, x), inverse_symplectic(S))
    gate(rank([flatten(y) for y in local[:3]] + [flatten(conjugate)]) == 3)

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
