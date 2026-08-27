"""Exact Pauli-algebra audit for two normalized prime exchanges."""

import json
from pathlib import Path

import sympy as sp


alpha, beta = sp.symbols("alpha beta", real=True)
I = sp.I
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
identity = sp.eye(2)


def axis(theta):
    return sp.cos(theta) * sigma1 + sp.sin(theta) * sigma2


Xp = axis(alpha)
Xq = axis(beta)
delta = beta - alpha
product_expected = sp.cos(delta) * identity + I * sp.sin(delta) * sigma3
commutator_expected = 2 * I * sp.sin(delta) * sigma3
orthogonal = sp.simplify(-I * sigma3 * Xp)

orthogonal_residual = (orthogonal - axis(alpha + sp.pi / 2)).applyfunc(
    lambda entry: sp.simplify(sp.expand_complex(entry))
)

checks = {
    "prime_axis_involution": sp.simplify(Xp**2 - identity) == sp.zeros(2),
    "prime_axis_hermitian": Xp.conjugate().T.equals(Xp),
    "two_prime_product": sp.simplify(Xp * Xq - product_expected) == sp.zeros(2),
    "two_prime_commutator": sp.simplify(Xp * Xq - Xq * Xp - commutator_expected) == sp.zeros(2),
    "orthogonal_axis": all(entry == 0 for entry in orthogonal_residual),
}

# Vectorize I, Xp, sigma3, and the orthogonal axis. Their determinant is
# nonzero independently of alpha, proving full M2 generation once sigma3 is
# available from a nonzero commutator.
generators = [identity, Xp, sigma3, orthogonal]
coordinate_matrix = sp.Matrix.hstack(*[sp.Matrix(g).reshape(4, 1) for g in generators])
generation_determinant = sp.simplify(sp.expand_complex(coordinate_matrix.det()))
checks["four_generators_independent"] = generation_determinant != 0

result = {
    "schema": "marici.grothendieck.two_prime_reciprocal_matrix_generation.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "generation_determinant": str(generation_determinant),
    "resonance": "t log(q/p) in pi Z",
    "generic_algebra": "M_2(C)",
}

output = Path(__file__).parents[1] / "results" / "two_prime_reciprocal_matrix_generation.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
