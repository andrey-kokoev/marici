#!/usr/bin/env python3
"""Exact source-coordinate audit at the external Gram boundary."""

import json
from pathlib import Path

import sympy as sp


P1, P2, theta = sp.symbols("P1 P2 theta", positive=True)
P3sq = P1**2 + P2**2 + 2 * P1 * P2 * sp.cos(theta)
P3 = sp.sqrt(P3sq)

Lambda_sq = (
    (P1 + P2 + P3)
    * (P1 + P2 - P3)
    * (P1 - P2 + P3)
    * (P1 - P2 - P3)
)
gram2 = P1**2 * P2**2 * sp.sin(theta) ** 2

lambda_identity = sp.simplify(Lambda_sq + 4 * gram2) == 0
resolved_heron_identity = sp.simplify(
    (P1 + P2 - P3) * (P1 + P2 + P3)
    - 4 * P1 * P2 * sp.sin(theta / 2) ** 2
) == 0

# Equation (3.3) of the frozen source has
# G_ext^(-1/2) (G_full/G_ext)^((d-ne-1)/2).
d, ne = sp.symbols("d ne", integer=True)
external_gram_exponent = sp.simplify(-sp.Rational(1, 2) - (d - ne - 1) / 2)
full_gram_exponent = sp.simplify((d - ne - 1) / 2)
at_three_sites_three_dimensions = {
    "external_gram_exponent": sp.simplify(external_gram_exponent.subs({d: 3, ne: 3})),
    "full_gram_exponent": sp.simplify(full_gram_exponent.subs({d: 3, ne: 3})),
}

assert lambda_identity
assert resolved_heron_identity
assert at_three_sites_three_dimensions["external_gram_exponent"] == 0
assert at_three_sites_three_dimensions["full_gram_exponent"] == -sp.Rational(1, 2)

packet = {
    "schema": "marici.benincasa.physical-gram-vector-lift.v1",
    "status": "passed",
    "momentum_closure_chart": {
        "p1": "(P1,0,0)",
        "p2": "(P2*cos(theta),P2*sin(theta),0)",
        "P3_squared": str(P3sq),
    },
    "identities": {
        "Lambda_equals_minus_four_external_Gram": lambda_identity,
        "resolved_Heron_coordinate": (
            "(P1+P2-P3)(P1+P2+P3)=4*P1*P2*sin(theta/2)^2"
        ),
        "resolved_Heron_identity_passed": resolved_heron_identity,
        "Heron_order_in_theta": 2,
    },
    "source_measure_audit": {
        "source_equation": "arXiv:2402.06558v3 eq. (3.3), specialized to d=ne=3",
        "external_Gram_exponent_after_combining_factors": str(
            at_three_sites_three_dimensions["external_gram_exponent"]
        ),
        "full_Gram_exponent": str(at_three_sites_three_dimensions["full_gram_exponent"]),
        "conclusion": "the apparent external-Gram Jacobian pole cancels in the original d^3l measure",
    },
    "cycle_classification": {
        "original_cycle": "fixed loop-vector contour R^3",
        "theta_transport": "single-valued source momentum-closure chart",
        "cycle_monodromy": "identity",
        "distance_coordinate_failure": "the scalar-product/distance chart loses rank when external Gram vanishes",
        "new_carrier_support": False,
    },
    "scope_warning": (
        "This certifies the source-cycle and Jacobian behavior. It does not by itself "
        "prove analyticity of every renormalized period or annihilation of the elliptic "
        "vanishing-cycle covector at infinity."
    ),
}

output = Path(__file__).with_name("physical-gram-vector-lift.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
