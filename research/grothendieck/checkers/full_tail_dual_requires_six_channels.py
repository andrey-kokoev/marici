import json
from fractions import Fraction as F


def transpose(A):
    return [list(row) for row in zip(*A)]


def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A):
    n = len(A)
    aug = [A[i][:] + [F(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for r in range(n):
            if r != col:
                scale = aug[r][col]
                aug[r] = [aug[r][j] - scale * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def block_diag(A, B):
    z1 = [[F(0)] * len(B) for _ in A]
    z2 = [[F(0)] * len(A) for _ in B]
    return [A[i] + z1[i] for i in range(len(A))] + [z2[i] + B[i] for i in range(len(B))]


A = [[F(2), F(1), F(0)], [F(1), F(2), F(1)], [F(0), F(1), F(2)]]
dual = transpose(inverse(A))
lift = block_diag(A, dual)
zero = [[F(0)] * 3 for _ in range(3)]
identity = [[F(i == j) for j in range(3)] for i in range(3)]
Q6 = [zero[i] + identity[i] for i in range(3)] + [identity[i] + zero[i] for i in range(3)]

# On T + W + det(T)^* + W^*, scalar tail rescaling has weights
# (lambda, lambda, 1, lambda^-2, 1). No weight pairs involving T multiply to 1.
weights = [1, 1, 0, -2, 0]
allowed = [[weights[i] + weights[j] == 0 for j in range(5)] for i in range(5)]
tail_rows_forced_zero = all(not allowed[i][j] for i in (0, 1) for j in range(5))

result = {
    "schema": "marici.grothendieck.full_tail_dual_requires_six_channels.v1",
    "checks": {
        "five_channel_tail_is_radical_under_tail_scaling_naturality": tail_rows_forced_zero,
        "six_channel_evaluation_form_is_preserved": multiply(transpose(lift), multiply(Q6, lift)) == Q6,
    },
    "five_channel_weights": weights,
    "six_channel_signature": [3, 3],
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
