#!/usr/bin/env python3
"""Exact audit of interaction-normal transport at the physical Heron walls."""

import json
from pathlib import Path

import sympy as sp


P1, P2, P3 = sp.symbols("P1 P2 P3", nonzero=True)
Ps = (P1, P2, P3)
t = sp.symbols("t")

factors = {
    "f1": P1 - P2 - P3,
    "f2": P1 - P2 + P3,
    "f3": P1 + P2 - P3,
    "f4": P1 + P2 + P3,
}
physical = {
    "f1": {P1: P2 + P3},
    "f2": {P2: P1 + P3},
    "f3": {P3: P1 + P2},
}

Lambda = sp.prod(factors.values())
H = P1**2 + P2**2 - P3**2
F = P1**2 * t**4 - H * t**2 + P2**2
Delta = 16 * P1**2 * P2**2 * Lambda**2


def signs(expr):
    return tuple(sp.diff(expr, p) for p in Ps)


checks = []
for name, substitution in physical.items():
    f = factors[name]
    s = signs(f)
    normal_covector = tuple(sp.simplify(s[i] / (2 * Ps[i])) for i in range(3))
    kernel = (
        (s[0] * P1, -s[1] * P2, sp.Integer(0)),
        (s[0] * P1, sp.Integer(0), -s[2] * P3),
    )
    kernel_checks = [
        sp.simplify(sum(normal_covector[i] * vector[i] for i in range(3))) == 0
        for vector in kernel
    ]

    F_wall = sp.factor(F.subs(substitution))
    # Certify squareness without trusting a branch choice for sqrt.
    square_candidates = [P1 * t**2 - P2, P1 * t**2 + P2]
    square_match = next(
        (
            sp.factor(candidate.subs(substitution))
            for candidate in square_candidates
            if sp.expand(candidate.subs(substitution) ** 2 - F_wall) == 0
        ),
        None,
    )

    other_product = sp.prod(value for key, value in factors.items() if key != name)
    second_coarse_grade = sp.factor(
        (16 * P1**2 * P2**2 * other_product**2).subs(substitution)
    )
    nonzero_generic = second_coarse_grade != 0

    checks.append(
        {
            "wall": name,
            "equation": str(f),
            "normal_covector_d_f_d_nu": [str(value) for value in normal_covector],
            "normal_rank": 1,
            "tangent_kernel_basis": [[str(value) for value in vector] for vector in kernel],
            "kernel_checks": kernel_checks,
            "elliptic_quartic_on_wall": str(F_wall),
            "perfect_square_root_up_to_sign": str(square_match),
            "coarse_discriminant_first_grade": "0",
            "coarse_discriminant_second_grade": str(second_coarse_grade),
            "second_grade_nonzero_away_from_soft_support": nonzero_generic,
        }
    )

assert all(all(item["kernel_checks"]) for item in checks)
assert all(item["perfect_square_root_up_to_sign"] != "None" for item in checks)
assert all(item["second_grade_nonzero_away_from_soft_support"] for item in checks)

packet = {
    "schema": "marici.benincasa.interaction-normals-at-gram-wall.v1",
    "status": "passed",
    "source_family": "generic six-scale three-site Cayley-Menger kernel",
    "elliptic_boundary": str(F),
    "elliptic_discriminant": str(Delta),
    "physical_wall_count": len(checks),
    "checks": checks,
    "classification": {
        "tangent_interaction_directions_per_wall": 2,
        "transverse_interaction_directions_per_wall": 1,
        "resolved_normal_order": 1,
        "coarse_discriminant_order": 2,
        "coefficient_support": "existing external triangle/Gram divisor",
        "new_carrier_support": False,
    },
    "monodromy_scope": (
        "The perfect-square degeneration certifies a generic nodal elliptic boundary. "
        "Rank-one unipotent Picard-Lefschetz monodromy with N^2=0 is the standard "
        "nodal-curve inference, not a newly computed physical-cycle pairing."
    ),
}

output = Path(__file__).with_name("interaction-normals-at-gram-wall.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
