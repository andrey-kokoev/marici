import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


identity4 = [[int(i == j) for j in range(4)] for i in range(4)]
preparation = [
    [2, 0, 0, 0],
    [0, 3, 0, 0],
    [0, 0, 5, 0],
    [0, 0, 0, 7],
]
assert matmul(identity4, preparation) == matmul(preparation, identity4)

fourier = [
    [1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
project = [[1, 0, 0, 0], [0, 1, 0, 0]]
cutoff_complement = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
leakage = matmul(matmul(project, fourier), cutoff_complement)
expected = [[0, 0, 1, 1], [0, 0, -1, -1]]
assert leakage == expected
assert leakage[0] != [0, 0, 0, 0]
assert leakage[1] == [-x for x in leakage[0]]

result = {
    "schema": "marici.nima.no-finite-completed-source-intertwiner.v1",
    "finite_labelled_naturality": True,
    "fourier_cutoff_residual": leakage,
    "fourier_cutoff_residual_rank": 1,
    "finite_beck_chevalley_square": False,
    "verdict": "completed sewing precedes finite diagnostic projection",
}

out = Path(__file__).parents[1] / "results" / "no-finite-completed-source-intertwiner.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

