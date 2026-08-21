def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


# Pullback matrices for C4 -> C2 -> 1 on coefficient bases.
P_q = [
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
]
P_r = [[1], [1]]
P_composite = multiply(P_q, P_r)

# Perfect standard pairings force the Betti maps to be transposes.
S_q = transpose(P_q)
S_r = transpose(P_r)
S_composite = transpose(P_composite)

assert S_q == [[1, 0, 1, 0], [0, 1, 0, 1]]
assert S_composite == multiply(S_r, S_q)
assert multiply(S_q, P_q) == [[2, 0], [0, 2]]
assert multiply(S_composite, P_composite) == [[4]]

# Every source basis chain maps with coefficient one to its quotient label.
columns = [[S_q[row][column] for row in range(2)] for column in range(4)]
assert columns == [[1, 0], [0, 1], [1, 0], [0, 1]]

print({
    "tower": "C4->C2->1",
    "forced_pushforward_C4_to_C2": S_q,
    "basis_chain_images": columns,
    "strict_composition": True,
    "pull_push_norms": [2, 4],
    "checks": "pass",
})
