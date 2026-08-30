"""Exact audit of the doubled prime reciprocal-exchange constructor."""

import json
from pathlib import Path

import sympy as sp


p, q, s, t = sp.symbols("p q s t", positive=True)


def exchange(prime):
    return sp.Matrix([[0, prime ** (-s)], [prime ** (s - 1), 0]])


Ep = exchange(p)
Eq = exchange(q)
identity = sp.eye(2)
square_residual = sp.simplify(Ep**2 - p**-1 * identity)
inverse_residual = sp.simplify((identity - Ep) * (identity + Ep) - (1 - p**-1) * identity)
determinant_residual = sp.simplify((identity - Ep).det() - (1 - p**-1))
commutator = sp.simplify(Ep * Eq - Eq * Ep)

upper_seam = sp.simplify(
    commutator[0, 0].subs(s, sp.Rational(1, 2) + sp.I * t)
)
upper_expected = 2 * sp.I / sp.sqrt(p * q) * sp.sin(t * sp.log(q / p))

checks = {
    "exchange_square": square_residual == sp.zeros(2),
    "inverse_identity": inverse_residual == sp.zeros(2),
    "determinant_identity": determinant_residual == 0,
    "commutator_diagonal": commutator[0, 1] == 0 and commutator[1, 0] == 0,
    "commutator_traceless": sp.simplify(sp.trace(commutator)) == 0,
    "seam_sine_orientation": sp.simplify(
        sp.trigsimp(upper_seam.rewrite(sp.exp) - upper_expected.rewrite(sp.exp))
    ) == 0,
}

result = {
    "schema": "marici.grothendieck.prime_reciprocal_exchange.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "local_square": "E_p(s)^2=p^-1 I",
    "local_determinant": "det(I-E_p)=1-p^-1",
    "seam_eigenvalues_of_I_minus_E": ["1-p^-1/2", "1+p^-1/2"],
    "two_prime_upper_commutator": "2i(pq)^-1/2 sin(t log(q/p))",
    "global_determinant_obstruction": "product_p(1-p^-1)=0",
}

output = Path(__file__).parents[1] / "results" / "prime_reciprocal_exchange.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
