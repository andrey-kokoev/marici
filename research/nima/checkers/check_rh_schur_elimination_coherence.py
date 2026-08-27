from fractions import Fraction as F
import json
from pathlib import Path


def inverse(matrix):
    n = len(matrix)
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(n):
            if i != col:
                scale = aug[i][col]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def feedback(indices, matrix, vector):
    block = [[matrix[i][j] for j in indices] for i in indices]
    b = [vector[i] for i in indices]
    inv = inverse(block)
    return sum(b[i] * inv[i][j] * b[j] for i in range(len(b)) for j in range(len(b)))


A = [[F(2), F(1, 2), F(1, 3)], [F(1, 2), F(3), F(1, 4)], [F(1, 3), F(1, 4), F(4)]]
B = [F(1), F(1, 2), -F(1, 3)]

q0 = feedback([0], A, B)
q01 = feedback([0, 1], A, B)
q02 = feedback([0, 2], A, B)
q012 = feedback([0, 1, 2], A, B)

path_12 = (q01 - q0, q012 - q01)
path_21 = (q02 - q0, q012 - q02)

assert path_12 != path_21
assert sum(path_12) == sum(path_21) == q012 - q0

show = lambda x: str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
result = {
    "schema": "marici.rh-schur-elimination-coherence.v1",
    "feedback": {"q0": show(q0), "q01": show(q01), "q02": show(q02), "q012": show(q012)},
    "path_add_1_then_2": [show(x) for x in path_12],
    "path_add_2_then_1": [show(x) for x in path_21],
    "local_increments_order_independent": False,
    "total_increment_path_independent": True,
    "coherencer": "determinant_factorization_comparison_cell",
}

out = Path(__file__).parents[1] / "results" / "rh-schur-elimination-coherence.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
