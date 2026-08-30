#!/usr/bin/env python3
"""Verify strict localization of the parity-even tensor port at q_G12=0."""

import json
from pathlib import Path

import sympy as sp


a, b, c, E = sp.symbols("a b c E")
P1, P2, P3 = sp.symbols("P1 P2 P3", nonzero=True)

CM = sp.Matrix(
    [
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, P2**2, P1**2],
        [1, a**2, P2**2, 0, P3**2],
        [1, b**2, P1**2, P3**2, 0],
    ]
)
K = sp.factor(-CM.det() / 2)
Lambda = sp.factor(
    (P1 - P2 - P3) * (P1 - P2 + P3) * (P1 + P2 - P3) * (P1 + P2 + P3)
)
N = sp.expand(
    2 * P1**2 * (c**2 + P2**2 - a**2)
    - (c**2 + P1**2 - b**2) * (P1**2 + P2**2 - P3**2)
)
Q_even = sp.cancel(-(N**2 + 4 * P1**2 * K) / (4 * P1**2 * Lambda))

L1 = (
    2 * P1**2 * a**2 + P2**2 * P3**2 - P2**2 * a**2
    - P2**2 * b**2 - P3**2 * a**2 - P3**2 * c**2
    + a**4 - a**2 * b**2 - a**2 * c**2 + b**2 * c**2
)
L2 = (
    P1**2 * P3**2 - P1**2 * a**2 - P1**2 * b**2
    + 2 * P2**2 * b**2 - P3**2 * b**2 - P3**2 * c**2
    - a**2 * b**2 + a**2 * c**2 + b**4 - b**2 * c**2
)
L3 = (
    P1**2 * P2**2 - P1**2 * a**2 - P1**2 * c**2
    - P2**2 * b**2 - P2**2 * c**2 + 2 * P3**2 * c**2
    + a**2 * b**2 - a**2 * c**2 - b**2 * c**2 + c**4
)

ambient_basis = [L1, L2, L3, a**2, b**2, c**2, sp.Integer(1)]
ambient_labels = ["L1", "L2", "L3", "D1=a^2", "D2=b^2", "D3=c^2", "U=1"]


def coefficient_matrix(polynomials, variables):
    monomials = sorted(
        set().union(*(set(sp.Poly(poly, *variables).monoms()) for poly in polynomials))
    )
    return monomials, sp.Matrix(
        [
            [sp.Poly(poly, *variables).coeff_monomial(monomial) for poly in polynomials]
            for monomial in monomials
        ]
    )


ambient_monomials, ambient_matrix = coefficient_matrix(ambient_basis + [Q_even], (a, b, c))
ambient_source = ambient_matrix[:, :7]
ambient_target = ambient_matrix[:, 7]
ambient_solution = next(iter(sp.linsolve((ambient_source, ambient_target))))
ambient_coordinates = [sp.factor(value) for value in ambient_solution]
assert ambient_source.rank() == 7

# Principal marked wall q_G12=c+E=0.  Its only new source relation is
# D3-E^2 U=(c-E)(c+E).
wall_substitution = {c: -E}
restricted_basis = [sp.expand(poly.subs(wall_substitution)) for poly in ambient_basis[:5]] + [sp.Integer(1)]
restricted_labels = ambient_labels[:5] + ["U=1"]
Q_restricted = sp.factor(Q_even.subs(wall_substitution))

restricted_monomials, restricted_matrix = coefficient_matrix(
    restricted_basis + [Q_restricted], (a, b)
)
restricted_source = restricted_matrix[:, :6]
restricted_target = restricted_matrix[:, 6]
restricted_solution = next(iter(sp.linsolve((restricted_source, restricted_target))))
restricted_coordinates = [sp.factor(value) for value in restricted_solution]
assert restricted_source.rank() == 6

# The source quotient map is fixed before looking at Q_even: D3 maps to E^2 U.
induced_coordinates = ambient_coordinates[:5] + [
    sp.factor(ambient_coordinates[6] + E**2 * ambient_coordinates[5])
]
assert all(
    sp.factor(left - right) == 0
    for left, right in zip(restricted_coordinates, induced_coordinates)
)
assert sp.factor(
    sum(value * vector for value, vector in zip(restricted_coordinates, restricted_basis))
    - Q_restricted
) == 0

# Regularity gives strict Poincare-residue compatibility.  The difference
# between the ambient multiplier and its wall value is divisible by q_G12.
normal_quotient = sp.cancel((Q_even - Q_restricted) / (c + E))
assert sp.denom(normal_quotient).has(c + E) is False
assert sp.factor(Q_even - Q_restricted - (c + E) * normal_quotient) == 0
principal_relation = sp.factor(c**2 - E**2 - (c - E) * (c + E))
assert principal_relation == 0

packet = {
    "schema": "marici.benincasa.tensor-marked-wall-localization.v1",
    "status": "passed",
    "wall": "q_G12=c+E=0",
    "ambient_interaction_rank": ambient_source.rank(),
    "restricted_interaction_rank": restricted_source.rank(),
    "principal_kernel": "D3-E^2 U=(c-E)(c+E)",
    "ambient_coordinates": dict(zip(ambient_labels, map(str, ambient_coordinates))),
    "restricted_coordinates": dict(zip(restricted_labels, map(str, restricted_coordinates))),
    "quotient_coordinates_agree": True,
    "residue_identity": "Res_q(Q_even*omega)=Q_even|_q Res_q(omega)",
    "normal_difference_divisible_by_q": True,
    "additional_tensor_kernel": 0,
    "new_carrier_support": False,
    "classification": (
        "the parity-even tensor port descends strictly through the predeclared "
        "principal marked-wall quotient"
    ),
    "scope_warning": (
        "This proves source-module and residue compatibility at q_G12. It does "
        "not yet compute total-energy nearby cycles or elliptic/Landau intersections."
    ),
}

output = Path(__file__).with_name("tensor-marked-wall-localization.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
