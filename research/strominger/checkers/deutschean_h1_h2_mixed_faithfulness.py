#!/usr/bin/env python3
"""Exact finite-jet joint-faithfulness test for the corrected H1/H2 block."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_h1_h2_mixed_faithfulness.json"
T, k = s.symbols("T k")
db, dc = s.symbols("db dc")
aa = s.symbols("a2:7")
variables = (*aa, db, dc)
N = 7


def tr(expression):
    expression = s.series(expression, k, 0, 2).removeO()
    return s.series(expression, T, 0, N).removeO().expand()


g = sum(aa[j - 2] * T**j for j in range(2, 7))
b = s.Rational(5, 4) + k * db
c = s.Rational(3, 2) + k * dc
z = tr(T * s.exp(-T) - k * T * s.diff(g, T))
zprime = tr(s.diff(z, T))


def E(expression):
    return tr(tr(z / zprime) * s.diff(expression, T))


h = tr(T * zprime / z)
S0 = tr(1 + s.log(T / z) + (s.exp(-T) - 1 + k * g) / z)
S1 = tr(-(b + 1) * T + s.log(T / z) - s.log(h) / 2)
F3 = tr(2 + T**3 / z * (-s.exp(-T) + k * s.diff(g, T, 3)))
F4 = tr(-6 + T**4 / z * (s.exp(-T) + k * s.diff(g, T, 4)))
A = b + 1
S2 = tr(
    c * z * s.exp(T) + A**2 * T**2 / (2 * h)
    - A * T * F3 / (2 * h**2) + F4 / (8 * h**2)
    + s.Rational(5, 24) * F3**2 / h**3 - s.Rational(1, 12)
)
A0 = tr(S0 + E(S0))
A1 = E(S1)
A2 = tr(E(S2) - S2)
Q0 = tr(1 + E(A0))
Q1 = tr(-s.Rational(1, 2) * (E(E(A0)) - E(A0)) + E(A1) - A1)
Q2 = tr(
    s.Rational(1, 3) * E(A0) - s.Rational(1, 2) * E(E(A0))
    + s.Rational(1, 6) * E(E(E(A0))) - A1
    + s.Rational(3, 2) * E(A1) - s.Rational(1, 2) * E(E(A1))
    + E(A2) - 2 * A2
)
V0 = tr(1 - 1 / Q0)
V1 = tr(Q1 / Q0**2)
V2 = tr(Q2 / Q0**2 - Q1**2 / Q0**3)


def dR(expression):
    return tr(s.diff(expression, T) / s.diff(V0, T))


W0 = tr(s.log(V0 / z))
H1 = tr(V1 / V0 - (V1 - 4 * V0) * dR(W0))
d1 = tr(V1 - 4 * V0)
d2 = tr(V2 - 4 * V1)
H2 = tr(
    V2 / V0 - s.Rational(1, 2) * (V1 / V0)**2 - d2 * dR(W0)
    - s.Rational(1, 2) * d1**2 * dR(dR(W0)) - 4 * H1 - d1 * dR(H1)
)


def fixed_leading_variation(expression):
    return tr(
        s.diff(expression, k).subs(k, 0)
        - s.diff(expression.subs(k, 0), T) * s.diff(V0, k).subs(k, 0)
    )


DH1 = fixed_leading_variation(H1)
DH2 = fixed_leading_variation(H2)
observations = [DH1.coeff(T, j) for j in range(1, 5)]
observations += [DH2.coeff(T, j) for j in range(2, 5)]
matrix, offset = s.linear_eq_to_matrix(observations, variables)
checks = {
    "variation_block_is_homogeneous": offset == s.zeros(7, 1),
    "corrected_joint_block_is_square": matrix.shape == (7, 7),
    "corrected_joint_block_has_full_rank": matrix.rank() == 7,
    "corrected_joint_block_determinant_is_nonzero": matrix.det() != 0,
}
payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "variables": [str(v) for v in variables],
        "H1_grades": list(range(1, 5)),
        "H2_grades": list(range(2, 5)),
        "shape": list(matrix.shape),
        "rank": matrix.rank(),
        "determinant": str(s.factor(matrix.det())),
        "nullity": len(matrix.nullspace()),
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Exact initial-block certificate for the all-orders normalized tangent "
        "theorem. Combined with the independently derived nonzero H1 tail "
        "recurrence, it proves joint H1/H2 faithfulness for arbitrary analytic "
        "primitive-phase jets and both amplitude tangents. It does not address "
        "nonanalytic deformations or nonlinear finite equivalence."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
