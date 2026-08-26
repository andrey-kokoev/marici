"""Exact cubic-order ablation of nonlinear source curvature."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = (
    ROOT
    / "research"
    / "strominger"
    / "deutschean-primitive-cumulant-completion-explanation.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "deutschean_cumulant_curvature_ablation.json"
)

t, x, q = sp.symbols("t x q")
alpha, gamma, kappa = sp.symbols("alpha gamma kappa")
order = 3
tail = -kappa * sum(
    x ** (degree + 1) * t**degree / sp.factorial(degree + 1)
    for degree in range(1, order + 1)
)
carrier = sp.series(
    (sp.exp(x * t) - alpha * t)
    * sp.exp(gamma * x * t)
    * sp.exp(tail),
    t,
    0,
    order + 1,
).removeO().expand()


def expectation(polynomial: sp.Expr) -> sp.Expr:
    return sp.expand(
        sum(
            coefficient * sp.rf(q + 1, monomial[0])
            for monomial, coefficient in sp.Poly(polynomial, x).terms()
        )
    )


partition = sum(
    expectation(carrier.coeff(t, degree)) * t**degree
    for degree in range(order + 1)
)
log_partition = sp.series(sp.log(partition), t, 0, order + 1).removeO()
d = 1 / q
variance_step = 1 / q**2
skew_step = 2 / q**3
for degree in range(1, order + 1):
    coefficient = sp.expand(log_partition).coeff(t, degree)
    d += (
        sp.diff(coefficient, q)
        - sp.diff(coefficient, q).subs(q, q - 1)
    ) * t**degree
    variance_step += (
        sp.diff(coefficient, q, 2).subs(q, q - 1)
        - sp.diff(coefficient, q, 2)
    ) * t**degree
    skew_step += (
        sp.diff(coefficient, q, 3)
        - sp.diff(coefficient, q, 3).subs(q, q - 1)
    ) * t**degree

A = 1 - q * d
margin = sp.series(
    (3 * A * variance_step + d**2 * (2 + A) - q * skew_step) / d**2,
    t,
    0,
    order + 1,
).removeO().expand()
coefficients = {
    degree: sp.factor(margin.coeff(t, degree))
    for degree in range(order + 1)
}
physical_cubic = sp.factor(coefficients[3].subs(kappa, 1))
flat_cubic = sp.factor(coefficients[3].subs(kappa, 0))
physical_matching_polynomial = sp.factor(
    coefficients[3] / q**3 - 4
)
quadratic_discriminant = sp.discriminant(12 * kappa**2 + 3 * kappa + 4, kappa)

checks = {
    "orders_zero_through_two_vanish_for_symbolic_source_family": all(
        coefficients[degree] == 0 for degree in range(3)
    ),
    "cubic_jet_is_independent_of_affine_and_density_parameters": (
        alpha not in coefficients[3].free_symbols
        and gamma not in coefficients[3].free_symbols
    ),
    "physical_curvature_produces_four_q_cubed": physical_cubic == 4 * q**3,
    "removing_nonlinear_curvature_changes_cubic_jet": (
        flat_cubic != physical_cubic
    ),
    "physical_cubic_uniquely_recovers_real_curvature": (
        bool(
            physical_matching_polynomial
            == (kappa - 1) * (12 * kappa**2 + 3 * kappa + 4)
        )
        and bool(quadratic_discriminant < 0)
    ),
    "curvature_ablation_is_not_reported_as_completion": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "symbolic_margin_coefficients": {
            str(degree): str(value) for degree, value in coefficients.items()
        },
        "physical_cubic_jet": str(physical_cubic),
        "zero_curvature_cubic_jet": str(flat_cubic),
        "physical_matching_polynomial": str(physical_matching_polynomial),
        "nonphysical_quadratic_discriminant": str(quadratic_discriminant),
        "completion_bridge_status": "open",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "This exact ablation identifies the nonlinear source curvature seen "
        "by the cubic cumulant readout. It does not prove completed-cone "
        "preservation."
    ),
}

RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
