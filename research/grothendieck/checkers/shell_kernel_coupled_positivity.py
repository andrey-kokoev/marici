"""Dependency-free exact audit of shell-kernel coupled positivity."""

from fractions import Fraction as F


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def determinant(a):
    a = [row[:] for row in a]
    out = F(1)
    for j in range(len(a)):
        pivot = next(i for i in range(j, len(a)) if a[i][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        p = a[j][j]
        out *= p
        for i in range(j + 1, len(a)):
            q = a[i][j] / p
            for ell in range(j, len(a)):
                a[i][ell] -= q * a[j][ell]
    return out


B = [[F(1, 2), F(-1, 3)], [F(2, 5), F(1, 7)], [F(-1, 4), F(3, 8)]]
BTB = matmul(transpose(B), B)
gram = [[F(i == j) + BTB[i][j] for j in range(2)] for i in range(2)]
block = [
    [F(1), F(0), -B[0][0], -B[1][0], -B[2][0]],
    [F(0), F(1), -B[0][1], -B[1][1], -B[2][1]],
    [B[0][0], B[0][1], F(1), F(0), F(0)],
    [B[1][0], B[1][1], F(0), F(1), F(0)],
    [B[2][0], B[2][1], F(0), F(0), F(1)],
]

assert determinant(block) == determinant(gram)
assert gram[0][0] > 0 and determinant(gram) > 0  # Sylvester criterion.
assert BTB[0][0] + BTB[1][1] == sum(x * x for row in B for x in row)

result = {
    "exact_block_schur_identity": True,
    "gram_correction_positive_definite": True,
    "hilbert_schmidt_square_is_trace_correction": True,
    "block_determinant": str(determinant(block)),
    "identity": "det_2(I+J_B)=det(I+B*B)>0",
    "scope": "universal algebraic theorem; no Xi or RH identification",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "shell-kernel-coupled-positivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
