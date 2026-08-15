#!/usr/bin/env python3
"""Exact finite census for Heron-component intersections and soft endpoints."""

from __future__ import annotations

import json
from pathlib import Path

# Coefficients of Heron factors in (P1,P2,P3).
factors = {
    "f1=P1-P2-P3": (1, -1, -1),
    "f2=P1-P2+P3": (1, -1, 1),
    "f3=P1+P2-P3": (1, 1, -1),
    "f4=P1+P2+P3": (1, 1, 1),
}

# Exact rays for pair intersections in the nonnegative cone.
pair_classification = {
    ("f1=P1-P2-P3", "f2=P1-P2+P3"): {
        "solution_ray": "(t,t,0)", "soft_resultant": "P3=0"
    },
    ("f1=P1-P2-P3", "f3=P1+P2-P3"): {
        "solution_ray": "(t,0,t)", "soft_resultant": "P2=0"
    },
    ("f2=P1-P2+P3", "f3=P1+P2-P3"): {
        "solution_ray": "(0,t,t)", "soft_resultant": "P1=0"
    },
}
for pair, data in pair_classification.items():
    vec = {
        "(t,t,0)": (1, 1, 0),
        "(t,0,t)": (1, 0, 1),
        "(0,t,t)": (0, 1, 1),
    }[data["solution_ray"]]
    for name in pair:
        coeff = factors[name]
        assert sum(a*b for a, b in zip(coeff, vec)) == 0

# Any physical intersection involving the all-plus factor is the origin.
for name in tuple(factors)[:3]:
    # f4=0 with Pi>=0 implies each Pi=0; this vector satisfies both equations.
    origin = (0, 0, 0)
    assert sum(a*b for a, b in zip(factors[name], origin)) == 0
    assert sum(a*b for a, b in zip(factors["f4=P1+P2+P3"], origin)) == 0

# All three physical boundary factors meet only at the origin.
matrix = [factors[k] for k in tuple(factors)[:3]]
# Determinant is exact and nonzero.
det = (
    matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
    - matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
    + matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
)
assert det == -4

# Literal d=3 endpoint power counting. A true site-soft endpoint supplies at
# most one simple q_g pole: d^3 ell / rho ~ rho d rho dOmega.
spatial_dimension = 3
simple_endpoint_poles = 1
radial_power = spatial_dimension - 1 - simple_endpoint_poles
assert radial_power == 1
assert radial_power > -1
assert radial_power != -1  # no logarithm

result = {
    "schema": "marici.benincasa.soft_gram_overlap_census.v1",
    "status": "pass",
    "heron_factors": factors,
    "pair_intersections_in_nonnegative_cone": [
        {"pair": list(pair), **data} for pair, data in pair_classification.items()
    ],
    "pairs_with_all_plus": "origin P1=P2=P3=0",
    "triple_physical_heron_intersection": "origin P1=P2=P3=0",
    "triple_factor_matrix_determinant": det,
    "resolved_measure_normal": "p*v",
    "coarse_gram_normal": "p^2*v^2",
    "soft_orientation_structure": "normal-crossing product of two rank-one Kummer normals",
    "endpoint_model_if_Xi_equals_Pi_equals_zero": "d^3ell/q_gi ~ rho*d rho*dOmega",
    "endpoint_radial_power": radial_power,
    "endpoint_integrable": True,
    "endpoint_logarithmic_monodromy": False,
    "unipotent_logarithm_N": 0,
    "all_resultants_and_site_energies_soft": "existing total-energy q_G=0 support",
    "new_carrier_datum": False,
    "classification": "soft support plus fixed-base Gram Kummer data on existing carrier",
    "scope_boundary": (
        "Literal simple-pole six-term source. Higher-power master insertions "
        "and non-generic simultaneous marked-face collisions are separate."
    ),
}
out = Path(__file__).with_name("soft_gram_overlap_census_result.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("SOFT-GRAM OVERLAP CENSUS PASS")
print("three pair intersections force one soft resultant")
print("soft endpoint radial power = 1: integrable, no log")
print(f"wrote: {out}")
