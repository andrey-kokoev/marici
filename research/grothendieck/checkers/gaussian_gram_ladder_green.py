"""Exact audit of the Gaussian Gram Green identity and finite-wall anomaly."""

import json
from pathlib import Path

import sympy as sp


def gram(j, k):
    r = j + k
    return sp.gamma(sp.Rational(2 * r + 1, 2)) / (2 ** (r + sp.Rational(1, 2)) * sp.sqrt(sp.pi))


def ladder(size):
    matrix = sp.zeros(size)
    for k in range(size):
        matrix[k, k] = 2 * k + sp.Rational(1, 2)
        if k + 1 < size:
            matrix[k + 1, k] = -2
    return matrix


checks = {}
residuals = {}
for size in range(1, 7):
    top = size - 1
    G = sp.Matrix(size, size, gram)
    A = ladder(size)
    residual = sp.simplify(A.T * G + G * A)
    expected = sp.zeros(size)
    for j in range(size):
        for k in range(size):
            expected[j, k] = (
                (2 * gram(top + 1, k) if j == top else 0)
                + (2 * gram(j, top + 1) if k == top else 0)
            )
    matches = residual.equals(expected)
    checks[f"size_{size}_wall_matches"] = bool(matches)
    checks[f"size_{size}_gram_positive"] = all(minor > 0 for minor in [sp.simplify(G[:n, :n].det()) for n in range(1, size + 1)])
    residuals[str(size)] = {"rank": int(residual.rank()), "determinant": str(sp.simplify(G.det()))}

result = {
    "schema": "marici.grothendieck.gaussian_gram_ladder_green.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "cutoff_residuals": residuals,
    "green_identity": "(2j+2k+1)G_jk-2G_(j+1,k)-2G_(j,k+1)=0",
    "finite_wall": "B_jk=2 delta_(jN)G_(N+1,k)+2 delta_(kN)G_(j,N+1)",
}

output = Path(__file__).parents[1] / "results" / "gaussian_gram_ladder_green.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

