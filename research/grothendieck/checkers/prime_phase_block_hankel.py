"""Exact rational realification audit of the order-one block Hankel Gram."""

from fractions import Fraction as F
import json
from pathlib import Path


atoms = [
    (F(1, 2), F(1), F(3, 5), F(4, 5)),
    (F(1, 3), F(2), F(5, 13), F(-12, 13)),
    (F(1, 5), F(3), F(-7, 25), F(24, 25)),
    (F(1, 7), F(4), F(-15, 17), F(8, 17)),
    (F(1, 11), F(5), F(7, 25), F(-24, 25)),
]
assert all(cosine**2 + sine**2 == 1 for _, _, cosine, sine in atoms)


def moment(k):
    return sum(weight * displacement**k for weight, displacement, _, _ in atoms)


def twisted(k):
    real = sum(weight * displacement**k * cosine for weight, displacement, cosine, _ in atoms)
    imag = sum(weight * displacement**k * sine for weight, displacement, _, sine in atoms)
    return real, imag


H = [[moment(i + j) for j in range(2)] for i in range(2)]
Z = [[twisted(i + j) for j in range(2)] for i in range(2)]

# Complex Hermitian B=[[H,conj(Z)],[Z,H]], represented as A+iC.
size = 4
A = [[F(0) for _ in range(size)] for _ in range(size)]
C = [[F(0) for _ in range(size)] for _ in range(size)]
for i in range(2):
    for j in range(2):
        A[i][j] = H[i][j]
        A[i + 2][j + 2] = H[i][j]
        real, imag = Z[i][j]
        A[i + 2][j] = A[j][i + 2] = real
        C[i + 2][j] = imag
        C[j][i + 2] = -imag

# Realification [[A,-C],[C,A]] preserves Hermitian positivity.
realified = [
    [
        (A[i][j] if i < size and j < size else
         -C[i][j - size] if i < size else
         C[i - size][j] if j < size else
         A[i - size][j - size])
        for j in range(2 * size)
    ]
    for i in range(2 * size)
]
assert all(realified[i][j] == realified[j][i] for i in range(2 * size) for j in range(2 * size))

# Exact LDL decomposition. Five distinct atoms make this witness positive
# definite at order one, so no pivoting or semidefinite zero handling is needed.
L = [[F(0) for _ in range(2 * size)] for _ in range(2 * size)]
D = [F(0) for _ in range(2 * size)]
for i in range(2 * size):
    L[i][i] = F(1)
    for j in range(i):
        numerator = realified[i][j] - sum(L[i][k] * D[k] * L[j][k] for k in range(j))
        L[i][j] = numerator / D[j]
    D[i] = realified[i][i] - sum(L[i][k] ** 2 * D[k] for k in range(i))
    assert D[i] > 0

result = {
    "order": 1,
    "atom_count": len(atoms),
    "complex_block_size": size,
    "realified_size": 2 * size,
    "exact_LDL_pivots": [str(value) for value in D],
    "all_pivots_positive": True,
    "block_Hankel_Gram_positive": True,
    "contact_hierarchy_is_necessary_not_sufficient": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "prime-phase-block-hankel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
