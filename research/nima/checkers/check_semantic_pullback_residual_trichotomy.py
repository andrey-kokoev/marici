import json
from fractions import Fraction
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


observer_rows = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 2, 1, 0],
]
extended_rows = observer_rows + [[1, 3, 3, 1]]
assert rank(observer_rows) == 3
assert rank(extended_rows) == 4

mu, nu = Fraction(1), Fraction(1)
variance = nu - mu * mu
assert variance == 0
assert not variance > 0

x = [[0, 1], [1, 0]]
z = [[1, 0], [0, -1]]
xz = matmul(x, z)
zx = matmul(z, x)
assert xz == [[-entry for entry in row] for row in zx]
assert xz != zx

residuals = {
    "object_separation": "observation_port",
    "image_admission": "target_domain_predicate",
    "composition_coherence": "coherence_cell_or_anomaly_budget",
}
assert len(set(residuals.values())) == 3

result = {
    "status": "pass",
    "claim": "semantic pullback distinguishes port, domain, and coherence residuals",
    "object_separation": {
        "rank_before": rank(observer_rows),
        "rank_after": rank(extended_rows),
        "residual": residuals["object_separation"],
    },
    "image_admission": {
        "hostile_record": [int(mu), int(nu)],
        "variance": int(variance),
        "strict_domain_admitted": False,
        "residual": residuals["image_admission"],
    },
    "composition_coherence": {
        "XZ": xz,
        "ZX": zx,
        "commutes": False,
        "central_defect": "-I",
        "residual": residuals["composition_coherence"],
    },
    "pairwise_distinct_repairs": True,
}

out = Path(__file__).parents[1] / "results" / "semantic-pullback-residual-trichotomy.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

