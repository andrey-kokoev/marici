def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def subtract(left, right):
    return [[a - b for a, b in zip(x, y)] for x, y in zip(left, right)]


S = [[1, 0, 1, 0], [0, 1, 0, 1]]
P = transpose(S)
I4 = [[int(i == j) for j in range(4)] for i in range(4)]
I2 = [[int(i == j) for j in range(2)] for i in range(2)]

omega_compatible = subtract(multiply(I2, S), multiply(S, I4))
assert omega_compatible == [[0] * 4, [0] * 4]

D_G = [
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
]
D_H = I2
omega_hostile = subtract(multiply(D_H, S), multiply(S, D_G))
assert omega_hostile == [[0, 0, 0, 0], [0, 1, 0, 1]]

cochain_commutator = subtract(multiply(P, transpose(D_H)), multiply(transpose(D_G), P))
assert cochain_commutator == transpose(omega_hostile)

print({
    "forced_pushforward": S,
    "compatible_boundary_commutator": omega_compatible,
    "hostile_boundary_commutator": omega_hostile,
    "cochain_commutator_is_transpose": True,
    "checks": "pass",
})
