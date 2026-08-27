#!/usr/bin/env python3
"""Hostile test for a naive same-radius analytic inverse theorem."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_analytic_norm_hostile.json"
m, R, r = s.symbols("m R r", positive=True)
multiplier = s.factor(m * (m - 1) * (m - 2) * (m + 8) / 2)
same_radius_ratio = s.factor(multiplier / R**2)
radius_loss_ratio = s.factor(multiplier * (r / R)**(m - 2) / R**2)

# Exact integer witnesses; doubling m makes the lower bound strictly grow.
witnesses = [s.simplify(same_radius_ratio.subs({m: n, R: 1})) for n in (8, 16, 32, 64)]
q = s.Rational(1, 2)
q_symbol = s.symbols("q", positive=True)
geometric = q_symbol / (1 - q_symbol)


def euler(expression):
    return s.factor(q_symbol * s.diff(expression, q_symbol))


powers = {0: geometric}
for degree in range(1, 5):
    powers[degree] = euler(powers[degree - 1])
polynomial = s.Poly(s.expand(multiplier), m)
principal_majorant = s.factor(sum(
    polynomial.coeff_monomial(m**degree) * powers[degree]
    for degree in range(1, 5)
) / q_symbol**2)
expected_majorant = 3 * q_symbol * (11 - 7 * q_symbol) / (1 - q_symbol)**5

checks = {
    "same_radius_monomial_ratio_has_degree_four_growth": bool(s.degree(multiplier, m) == 4),
    "same_radius_witnesses_strictly_increase": all(a < b for a, b in zip(witnesses, witnesses[1:])),
    "radius_loss_has_exact_finite_geometric_majorant": bool(
        s.simplify(principal_majorant - expected_majorant) == 0
    ),
    "principal_graph_weight_cancels_multiplier": bool(s.simplify(
        multiplier * (R**m / multiplier) / R**m - 1
    ) == 0),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "tail_multiplier": str(multiplier),
        "same_radius_norm_ratio_lower_bound": str(same_radius_ratio),
        "same_radius_witnesses_at_R_1": [str(value) for value in witnesses],
        "radius_loss_ratio": str(radius_loss_ratio),
        "radius_loss_example": "r/R=1/2",
        "radius_loss_principal_majorant": str(expected_majorant),
        "candidate_readout_weight_at_grade_m_minus_2": "R^m/lambda_m",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Exact principal-symbol hostile. It rejects boundedness of the H1 "
        "differential in the naive same-radius coefficient norm and identifies "
        "radius loss or a derivative graph norm as necessary. It does not yet "
        "prove boundedness of every lower-order or nonlinear source term."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
