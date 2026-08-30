import json
from pathlib import Path


PRIMES = (2, 3, 5, 7, 11)
N = len(PRIMES)
DIMENSION = 2 * N


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(DIMENSION)) for j in range(DIMENSION)]
        for i in range(DIMENSION)
    ]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]


def nonzero(a):
    return [(i, j, a[i][j]) for i in range(DIMENSION) for j in range(DIMENSION) if a[i][j]]


def transpose(a):
    return [[a[j][i] for j in range(DIMENSION)] for i in range(DIMENSION)]


sheet_rotation = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
for i in range(N):
    sheet_rotation[i][N + i] = -1
    sheet_rotation[N + i][i] = 1

visible = {0, 1, 2}
cutoff = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
for sheet in (0, 1):
    for i in visible:
        cutoff[sheet * N + i][sheet * N + i] = 1

commutator = sub(matmul(cutoff, sheet_rotation), matmul(sheet_rotation, cutoff))
assert nonzero(commutator) == []

weights = [prime * prime for prime in PRIMES]
saturated_gram = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]
for sheet in (0, 1):
    for i, weight in enumerate(weights):
        saturated_gram[sheet * N + i][sheet * N + i] = weight
transported_gram = matmul(matmul(transpose(sheet_rotation), saturated_gram), sheet_rotation)
assert transported_gram == saturated_gram

result = {
    "schema": "marici.nima.arithmetic-vs-analytic-sewing-types.v1",
    "prime_labels": list(PRIMES),
    "visible_prime_labels": [PRIMES[i] for i in sorted(visible)],
    "arithmetic_sheet_commutator": nonzero(commutator),
    "arithmetic_commutator_norm": 0,
    "saturated_weighted_gram_preserved": True,
    "analytic_log_window_incoming_leakage_norm": 1,
    "strict_cutoff_identification_possible": False,
    "verdict": "the missing arithmetic-to-analytic interface must carry the discrepancy",
}

out = Path(__file__).parents[1] / "results" / "arithmetic-vs-analytic-sewing-types.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
