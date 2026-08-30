import json
from pathlib import Path


DIMENSION = 16


def projection(rank):
    return [[int(i == j and i < rank) for j in range(DIMENSION)] for i in range(DIMENSION)]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(DIMENSION)) for j in range(DIMENSION)]
        for i in range(DIMENSION)
    ]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]


def nonzero_entries(a):
    return [(i, j, a[i][j]) for i in range(DIMENSION) for j in range(DIMENSION) if a[i][j]]


identity = projection(DIMENSION)
backward_shift = [[int(j == i + 1) for j in range(DIMENSION)] for i in range(DIMENSION)]

moving = {}
for rank in range(1, DIMENSION):
    p = projection(rank)
    residual = matmul(matmul(p, backward_shift), sub(identity, p))
    entries = nonzero_entries(residual)
    assert entries == [(rank - 1, rank, 1)]
    moving[str(rank)] = entries

fixed_rank = 3
p_fixed = projection(fixed_rank)
fixed = {}
for refinement in range(fixed_rank, DIMENSION + 1):
    p_refined = projection(refinement)
    residual = matmul(matmul(p_fixed, backward_shift), sub(identity, p_refined))
    entries = nonzero_entries(residual)
    if refinement == fixed_rank:
        assert entries == [(fixed_rank - 1, fixed_rank, 1)]
    else:
        assert entries == []
    fixed[str(refinement)] = entries

result = {
    "schema": "marici.nima.fixed-vs-uniform-leakage.v1",
    "dimension": DIMENSION,
    "fixed_diagnostic_rank": fixed_rank,
    "fixed_residuals": fixed,
    "moving_residuals": moving,
    "fixed_eventual_vanishing": True,
    "moving_cutoff_norm": 1,
    "uniform_strictification": False,
}

out = Path(__file__).parents[1] / "results" / "fixed-vs-uniform-leakage.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

