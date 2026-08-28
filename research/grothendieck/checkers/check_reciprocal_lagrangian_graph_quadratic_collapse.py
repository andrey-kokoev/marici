from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


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


J = [[0, 1], [-1, 0]]
R = [[0, 1], [-1, 0]]  # Fourier quarter-turn
graph = [[1, 0], [0, 1], [0, 1], [-1, 0]]
omega_difference = [
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, -1],
    [0, 0, 1, 0],
]
omega_sum = [
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, -1, 0],
]

pullback_difference = matmul(matmul(transpose(graph), omega_difference), graph)
pullback_sum = matmul(matmul(transpose(graph), omega_sum), graph)

passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


gate(pullback_difference == [[0, 0], [0, 0]])
gate(pullback_sum != [[0, 0], [0, 0]])
gate(rank(transpose(graph)) == 2)

# Restrict the ten symmetric quadratic forms on four variables to the graph.
restricted = []
for i in range(4):
    for j in range(i, 4):
        a = [[Fraction(0) for _ in range(4)] for _ in range(4)]
        a[i][j] = 1
        a[j][i] = 1
        if i == j:
            a[i][j] = 1
        b = matmul(matmul(transpose(graph), a), graph)
        restricted.append([b[0][0], b[0][1] + b[1][0], b[1][1]])

gate(len(restricted) == 10)
gate(rank(restricted) == 3)
gate(10 - rank(restricted) == 7)

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
