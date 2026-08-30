#!/usr/bin/env python3
"""Exact all-orders Neumann bound for the conjugated H1 tail."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
INITIAL = ROOT / "research/strominger/results/deutschean_h1_h2_mixed_faithfulness.json"
RESULT = ROOT / "research/strominger/results/deutschean_tail_neumann_bound.json"
T, m = s.symbols("T m")
b = s.Rational(5, 4)
falling = lambda order: s.prod(m - index for index in range(order))
P4 = T - T**2
P3 = 2*b*T**3 + T**3 - 4*b*T**2 + 4*T**2 + 2*b*T - 14*T + 11
P2 = 4*b*T**3 + 2*T**3 - 6*b*T**2 + 13*T**2 - 2*b*T - 37*T + 4*b + 26
P1 = 2*b*T**3 + T**3 - 2*b*T**2 + 8*T**2 - 4*b*T - 22*T + 4*b + 15
Q = s.Poly(s.expand(
    P4 * falling(4) / T + P3 * falling(3)
    + T * P2 * falling(2) + T**2 * P1 * falling(1)
), T)
q = [s.factor(Q.coeff_monomial(T**j)) for j in range(6)]
coarse = [sum(abs(value) for value in s.Poly(poly, m).all_coeffs()) for poly in q]

R = s.Rational(1, 10000)
B_upper = 1 / (2 * (1 - R)**2)
B_tail_upper = R * (2 - R) / (2 * (1 - R)**2)
polynomial_tail = sum(coarse[j] * R**j for j in range(1, 6))
contraction_bound = s.factor(s.Rational(256, 9) * (
    coarse[0] * B_tail_upper + B_upper * polynomial_tail
))
initial = json.loads(INITIAL.read_text(encoding="utf-8"))
lam = s.factor(m * (m - 1) * (m - 2) * (m + 8) / 2)

checks = {
    "column_polynomial_has_degree_five": Q.degree() == 5,
    "column_diagonal_matches_twice_lambda": s.simplify(q[0] / 2 - lam) == 0,
    "coarse_polynomial_majorants_are_exact": coarse == [44, 109, 95, 34, s.Rational(17, 2), s.Rational(7, 2)],
    "tail_contraction_bound_is_below_one": contraction_bound < 1,
    "finite_initial_block_is_invertible": initial["observed"]["determinant"] != "0",
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "initial_result_sha256": hashlib.sha256(INITIAL.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "radius": str(R),
        "column_polynomial": str(Q.as_expr()),
        "coefficient_majorants": [str(value) for value in coarse],
        "wiener_prefactor_upper_bound": str(B_upper),
        "conjugated_tail_norm_upper_bound": str(contraction_bound),
        "conjugated_tail_norm_upper_bound_decimal": str(s.N(contraction_bound, 16)),
        "initial_determinant": initial["observed"]["determinant"],
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact all-orders absolute majorant for the H1 differential at the "
        "physical source. Together with the finite initial determinant it gives "
        "a bounded linear inverse at R=1/10000. The resulting analytic inverse "
        "theorem is local in the weighted Wiener topology; it is not a global "
        "source classification and the radius is deliberately nonoptimal."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
