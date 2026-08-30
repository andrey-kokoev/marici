import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add(*matrices):
    return [
        [sum(matrix[i][j] for matrix in matrices) for j in range(len(matrices[0][0]))]
        for i in range(len(matrices[0]))
    ]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


fourier = [
    [1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
identity = [[int(i == j) for j in range(4)] for i in range(4)]


def projection(rank):
    return [[int(i == j and i < rank) for j in range(4)] for i in range(4)]


p0, p1, p2, p3 = (projection(rank) for rank in (1, 2, 3, 4))
total = matmul(matmul(p0, fourier), sub(identity, p0))
shell01 = matmul(matmul(p0, fourier), sub(p1, p0))
shell12 = matmul(matmul(p0, fourier), sub(p2, p1))
shell23 = matmul(matmul(p0, fourier), sub(p3, p2))

assert total == add(shell01, shell12, shell23)
assert add(add(shell01, shell12), shell23) == add(shell01, add(shell12, shell23))

coarse_shell = matmul(matmul(p0, fourier), sub(p2, p0))
outer_shell = matmul(matmul(p0, fourier), sub(identity, p2))
assert total == add(coarse_shell, outer_shell)
assert coarse_shell == add(shell01, shell12)

result = {
    "schema": "marici.nima.fourier-cutoff-leakage-cocycle.v1",
    "total_leakage": total,
    "shells": [shell01, shell12, shell23],
    "shell_additivity": True,
    "parenthesization_independence": True,
    "coarse_refinement_compatibility": True,
    "verdict": "finite diagnostic projection is lax with an additive leakage cocycle",
}

out = Path(__file__).parents[1] / "results" / "fourier-cutoff-leakage-cocycle.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

