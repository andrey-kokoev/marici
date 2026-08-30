from fractions import Fraction
import json
from pathlib import Path


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def block_diag(a, b):
    n = len(a)
    m = len(b)
    out = [[Fraction(0)] * (n + m) for _ in range(n + m)]
    for i in range(n):
        for j in range(n):
            out[i][j] = a[i][j]
    for i in range(m):
        for j in range(m):
            out[n + i][n + j] = b[i][j]
    return out


def inverse_3(a):
    aug = [
        [Fraction(x) for x in row]
        + [Fraction(int(i == j)) for j in range(3)]
        for i, row in enumerate(a)
    ]
    for col in range(3):
        pivot = next(i for i in range(col, 3) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(3):
            if i != col:
                scale = aug[i][col]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[col])]
    return [row[3:] for row in aug]


zero = Fraction(0)
one = Fraction(1)
g = [
    [Fraction(2), zero, zero],
    [zero, Fraction(3), zero],
    [zero, zero, Fraction(5)],
]
g_inv = [
    [Fraction(1, 2), zero, zero],
    [zero, Fraction(1, 3), zero],
    [zero, zero, Fraction(1, 5)],
]

q = [[zero] * 6 for _ in range(6)]
generalized = [[zero] * 6 for _ in range(6)]
for i in range(3):
    q[i][i + 3] = one
    q[i + 3][i] = one
    for j in range(3):
        generalized[i][j + 3] = g_inv[i][j]
        generalized[i + 3][j] = g[i][j]

identity_6 = [[one if i == j else zero for j in range(6)] for i in range(6)]
assert matmul(generalized, generalized) == identity_6
energy = matmul(q, generalized)
assert energy == block_diag(g, g_inv)
assert [energy[i][i] for i in range(6)] == [
    Fraction(2), Fraction(3), Fraction(5),
    Fraction(1, 2), Fraction(1, 3), Fraction(1, 5),
]

# Covariance under v' = A v: g' = A^{-T} g A^{-1}.
a = [
    [Fraction(1), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(0), Fraction(2)],
]
a_inv = inverse_3(a)
g_prime = matmul(transpose(a_inv), matmul(g, a_inv))
h = block_diag(a, transpose(a_inv))
h_inv = block_diag(a_inv, transpose(a))
energy_prime_by_transport = matmul(transpose(h_inv), matmul(energy, h_inv))
expected_dual = inverse_3(g_prime)
assert energy_prime_by_transport == block_diag(g_prime, expected_dual)

# A fixed positive metric does not prevent t from reaching zero.
a_hostile = Fraction(3, 2)
t_values = {
    "left_crossing": (-a_hostile) ** 2 - a_hostile ** 2,
    "seam_value": Fraction(0) ** 2 - a_hostile ** 2,
    "right_crossing": a_hostile ** 2 - a_hostile ** 2,
}
assert t_values["left_crossing"] == 0
assert t_values["right_crossing"] == 0
assert t_values["seam_value"] != 0

result = {
    "hyperbolic_rank": 6,
    "generalized_metric_involution": True,
    "relationship_energy_positive_diagonal": [
        "2", "3", "5", "1/2", "1/3", "1/5"
    ],
    "source_presentation_covariance": True,
    "fixed_positive_metric_prevents_maslov_crossing": False,
    "missing_addition": "source-derived contractive or chamber-preserving transport law",
    "verdict": "a generalized metric types relationship energy, but RH needs a dynamical law preserving distance from the Maslov divisor",
}

out = Path(__file__).parents[1] / "results" / "rh-generalized-metric-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
