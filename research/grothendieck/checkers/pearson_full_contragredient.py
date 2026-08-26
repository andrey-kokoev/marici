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
                aug[r] = [aug[r][k] - scale * aug[col][k] for k in range(2 * n)]
    return [row[n:] for row in aug]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


checks = []
wall_injections = []
for j in range(8):
    c = F(7, 5)
    A = F(j) + F(19, 4)
    B = F(3, 2) * (F(j) + F(5, 4))
    M = [[A, -B, F(1)], [F(1), F(0), F(0)], [F(0), F(0), c]]
    dual = transpose(inverse(M))
    expected = [[F(0), -1 / B, F(0)], [F(1), A / B, F(0)], [F(0), 1 / (B * c), 1 / c]]
    x = [F(2), F(-3), F(5)]
    covector = [F(7), F(11), F(-2)]
    primal_x = [sum(M[i][k] * x[k] for k in range(3)) for i in range(3)]
    dual_covector = [sum(dual[i][k] * covector[k] for k in range(3)) for i in range(3)]
    checks.append(dual == expected and dot(primal_x, dual_covector) == dot(x, covector))
    wall_injections.append(str(dual[2][1]))

result = {
    "schema": "marici.grothendieck.pearson_full_contragredient.v1",
    "checks": {
        "inverse_transpose_formula_all_samples": all(checks),
        "tail_covector_injects_into_wall_covector": all(v != "0" for v in wall_injections),
    },
    "sample_wall_injection_coefficients": wall_injections,
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
