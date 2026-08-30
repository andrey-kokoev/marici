import json
from pathlib import Path


DIMENSION = 10


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(DIMENSION)) for j in range(DIMENSION)]
        for i in range(DIMENSION)
    ]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]


def projection(rank):
    return [[int(i == j and i < rank) for j in range(DIMENSION)] for i in range(DIMENSION)]


def nonzero(a):
    return [(i, j, a[i][j]) for i in range(DIMENSION) for j in range(DIMENSION) if a[i][j]]


identity = projection(DIMENSION)
shift = [[int(j == i + 1) for j in range(DIMENSION)] for i in range(DIMENSION)]
rank = 5
p = projection(rank)
q = sub(identity, p)

incoming = matmul(matmul(p, shift), q)
outgoing = matmul(matmul(q, shift), p)
commutator = sub(matmul(p, shift), matmul(shift, p))
block_reconstruction = sub(incoming, outgoing)

assert commutator == block_reconstruction
assert nonzero(incoming) == [(rank - 1, rank, 1)]
assert nonzero(outgoing) == []
assert nonzero(commutator) == [(rank - 1, rank, 1)]

reducing = identity
reducing_commutator = sub(matmul(p, reducing), matmul(reducing, p))
assert nonzero(reducing_commutator) == []

result = {
    "schema": "marici.nima.authorized-quasidiagonality-gate.v1",
    "cutoff_rank": rank,
    "incoming_leakage": nonzero(incoming),
    "outgoing_leakage": nonzero(outgoing),
    "commutator": nonzero(commutator),
    "hostile_commutator_norm": 1,
    "reducing_fixture_commutator_norm": 0,
    "verdict": "uniform two-sided descent is asymptotic commutation on the authorized filtration",
}

out = Path(__file__).parents[1] / "results" / "authorized-quasidiagonality-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

