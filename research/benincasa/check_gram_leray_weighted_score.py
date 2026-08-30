#!/usr/bin/env python3
"""Exact generic Gram Leray-support and weighted-score recovery audit."""

import json
from pathlib import Path

import sympy as sp


P1, P2, P3 = sp.symbols("P1 P2 P3", positive=True)
t = sp.symbols("t")
u, v, w = sp.symbols("u v w")
r = sp.symbols("r", positive=True)
alpha, beta, A, B = sp.symbols("alpha beta A B", real=True)

distance_a = sp.sqrt(r**2 + 2 * alpha * r + A)
distance_b = sp.sqrt(r**2 + 2 * beta * r + B)
physical_infinity_limit = sp.limit(distance_a / distance_b, r, sp.oo)
assert physical_infinity_limit == 1

F = P1**2 * t**4 - (P1**2 + P2**2 - P3**2) * t**2 + P2**2
assert sp.factor(F.subs(t, 1)) == P3**2

walls = {
    "f1": {
        "substitution": {P1: P2 + P3},
        "node_polynomial": P1 * t**2 - P2,
    },
    "f2": {
        "substitution": {P2: P1 + P3},
        "node_polynomial": P1 * t**2 - P2,
    },
    "f3": {
        "substitution": {P3: P1 + P2},
        "node_polynomial": P1 * t**2 + P2,
    },
}

wall_checks = []
for name, data in walls.items():
    substitution = data["substitution"]
    node = sp.factor(data["node_polynomial"].subs(substitution))
    F_wall = sp.factor(F.subs(substitution))
    node_at_physical_infinity = sp.factor(node.subs(t, 1))
    assert sp.expand(F_wall - node**2) == 0
    # On each labelled physical wall this is +P3 or -P3 after the wall relation.
    assert sp.factor(node_at_physical_infinity**2 - P3**2).subs(substitution) == 0
    wall_checks.append(
        {
            "wall": name,
            "elliptic_wall_polynomial": str(F_wall),
            "node_polynomial": str(node),
            "node_polynomial_at_t_equals_1": str(node_at_physical_infinity),
            "collision_condition": "P3=0",
            "generic_nonsoft_support_disjoint": True,
        }
    )

# At the f3 branch, use physical source parameters u=delta(P1^2),
# v=delta(P2^2), and w=theta^2.  cos(theta)=1-w/2+O(w^2).
P1u = sp.sqrt(P1**2 + u)
P2v = sp.sqrt(P2**2 + v)
nu1 = u
nu2 = v
nu3 = (
    P1u**2
    + P2v**2
    + 2 * P1u * P2v * (1 - w / 2)
    - (P1 + P2) ** 2
)
normal_coordinates = sp.Matrix([nu1, nu2, nu3])
physical_coordinates = sp.Matrix([u, v, w])
jacobian = normal_coordinates.jacobian(physical_coordinates).subs({u: 0, v: 0, w: 0})
jacobian = sp.simplify(jacobian)
jacobian_det = sp.factor(jacobian.det())
assert jacobian_det == -P1 * P2

# The associated weighted coordinate change is already invertible at its
# linear term.  Pull the complete ten-label interaction presentation through
# L=nu3(u,v,w); here w=theta^2 has physical angle order two.
L = sp.factor(jacobian[2, 0] * u + jacobian[2, 1] * v + jacobian[2, 2] * w)
pulled_labels = [
    u,
    v,
    L,
    u**2,
    v**2,
    L**2,
    u * v,
    u * L,
    v * L,
    u * v * L,
]
monomials = sorted(
    {
        monomial
        for polynomial in pulled_labels
        for monomial in sp.Poly(sp.expand(polynomial), u, v, w).monoms()
    }
)
pullback_matrix = sp.Matrix(
    [
        [sp.Poly(sp.expand(polynomial), u, v, w).coeff_monomial(monomial) for polynomial in pulled_labels]
        for monomial in monomials
    ]
)
pullback_rank = pullback_matrix.rank()
assert pullback_rank == 10

# Order: L1,L2,L3,D1,D2,D3,C12,C13,C23,U.
source_relations = sp.Matrix(
    [
        [0, 0, 0, P3**2 - P2**2, -P2**2, P3**2, -P2**2, P3**2, 0, 0],
        [0, 0, 0, -P1**2, P3**2 - P1**2, P3**2, -P1**2, 0, P3**2, 0],
        [0, 0, 0, -1, -1, 0, -1, 0, 0, P3**2],
    ]
)
source_relation_rank = source_relations.rank()
assert source_relation_rank == 3

packet = {
    "schema": "marici.benincasa.gram-leray-weighted-score.v1",
    "status": "passed",
    "physical_infinity_support": {
        "distance_ratio": "t=a/b",
        "large_loop_limit": f"t={physical_infinity_limit}",
        "F_at_t_equals_1": str(sp.factor(F.subs(t, 1))),
    },
    "wall_checks": wall_checks,
    "leray_pairing": {
        "generic_nonsoft_value": 0,
        "reason": "the physical infinity boundary current at t=1 is disjoint from every Gram node",
        "first_possible_collision": "existing soft-Gram support P3=0, cyclically relabelled in the other infinity charts",
    },
    "weighted_physical_chart": {
        "coordinates": ["u=delta(P1^2)", "v=delta(P2^2)", "w=theta^2"],
        "normal_coordinates": ["nu1", "nu2", "nu3"],
        "jacobian_at_f3": [[str(value) for value in row] for row in jacobian.tolist()],
        "determinant": str(jacobian_det),
        "generic_rank": 3,
        "interpretation": "two first-grade tangent directions plus one second-Rees physical angle direction recover all three magnitude normals",
    },
    "complete_interaction_tower": {
        "raw_label_count": 10,
        "weighted_pullback_rank": pullback_rank,
        "source_relation_rank": source_relation_rank,
        "faithful_quotient_rank": pullback_rank - source_relation_rank,
        "maximum_normal_degree": 3,
        "maximum_required_physical_angle_order": 6,
        "reason": "w=theta^2 and the cubic normal tower can contain w^3",
    },
    "classification": {
        "elliptic_coefficient_nearby_cycle": "rank one",
        "physical_Leray_activation_generic_nonsoft": False,
        "weighted_score_recovery": "faithful",
        "new_carrier_support": False,
    },
    "scope_warning": (
        "The vanishing follows from support disjointness for the source UV boundary current. "
        "Soft-Gram intersections remain governed by the existing resolved soft complex; "
        "global UV-renormalized finite parts are not recomputed."
    ),
}

output = Path(__file__).with_name("gram-leray-weighted-score.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
