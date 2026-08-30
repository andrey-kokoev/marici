"""Exact three-mode Gaussian purity-ideal audit."""

import json
from fractions import Fraction
from pathlib import Path


Z = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
J = ((Fraction(0), Fraction(1)), (Fraction(-1), Fraction(0)))
I = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))


def scale(s, a):
    return tuple(tuple(s * x for x in row) for row in a)


def add(*matrices):
    return tuple(tuple(sum(m[i][j] for m in matrices) for j in range(2)) for i in range(2))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


zero = scale(Fraction(0), I)

# Rational counterexample: every diagonal determinant relation holds, while
# every off-diagonal symplectic coherence block is nonzero.
a = Fraction(9, 14)
c = Fraction(2, 7)
A = [scale(a, I) for _ in range(3)]
C = {}
for i in range(3):
    for j in range(i + 1, 3):
        C[i, j] = scale(c, Z)


def cross(i, j):
    return C[i, j] if i < j else transpose(C[j, i])


diagonal_residuals = []
for i in range(3):
    residual = det2(A[i]) - Fraction(1, 4)
    for k in range(3):
        if k != i:
            residual += det2(cross(i, k))
    diagonal_residuals.append(residual)
    assert residual == 0

off_diagonal = {}
for i in range(3):
    for j in range(i + 1, 3):
        k = 3 - i - j
        block = add(
            mul(mul(A[i], J), cross(i, j)),
            mul(mul(cross(i, j), J), A[j]),
            mul(mul(cross(i, k), J), transpose(cross(j, k))),
        )
        # In this symmetric ansatz the first two terms cancel and block=-c^2 J.
        expected = scale(-c * c, J)
        assert block == expected
        assert block != zero
        off_diagonal[f"{i}{j}"] = [[str(x) for x in row] for row in block]

packet = {
    "schema": "marici.three-mode-symplectic-purity.v1",
    "purity_equation": "V Omega V=Omega/4",
    "generator_packet": {
        "diagonal": "3 scalar equations det(A_i)+sum_(k!=i) det(C_ik)=1/4",
        "off_diagonal": "3 labelled 2x2 equations A_i J C_ij+C_ij J A_j+sum_(k!=i,j) C_ik J C_jk^T=0",
        "raw_scalar_count": "3+12=15 before syzygies",
    },
    "counterexample": {
        "A_i": "(9/14) I2",
        "C_ij": "(2/7) diag(1,-1)",
        "diagonal_residuals": [str(x) for x in diagonal_residuals],
        "off_diagonal_residuals": off_diagonal,
    },
    "conclusion": "the three determinant vertex-edge relations do not generate Gaussian purity; symplectic off-diagonal coherence generators are required",
    "interpretation": "Gaussian purity is an Omega-contracted exterior-square refinement, not the plain determinant tower",
}

out = Path(__file__).parent / "results" / "three-mode-symplectic-purity.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
