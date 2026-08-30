from fractions import Fraction as F
import json
from pathlib import Path


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


ranks = {}
determinants = {}
for n in range(1, 9):
    points = [F(i) for i in range(1, n + 1)]
    vandermonde = [[u**k for k in range(n)] for u in points]
    ranks[str(n)] = rank(vandermonde)
    determinant = F(1)
    for j in range(n):
        for i in range(j):
            determinant *= points[j] - points[i]
    determinants[str(n)] = str(determinant)
    assert ranks[str(n)] == n
    assert determinant != 0

result = {
    "schema": "marici.rh-moment-orbit-infinite.v1",
    "spectral_generator": "multiplication_by_scale_u",
    "dual_orbit": ["1", "u", "u^2", "..."],
    "cutoff_ranks": ranks,
    "vandermonde_determinants": determinants,
    "finite_rank_closure": False,
    "source_condition": "support_has_arbitrarily_many_distinct_points",
    "conclusion": "forced_infinite_endpoint_dual_orbit",
}

out = Path(__file__).parents[1] / "results" / "rh-moment-orbit-infinite.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
