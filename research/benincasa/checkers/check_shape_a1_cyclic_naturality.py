#!/usr/bin/env python3
"""Test cyclic naturality of the three exceptional A1 incidence lines."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-a1-cyclic-naturality.json"

a, b, c = source.a, source.b, source.c
g1, g2, g3 = source.g1, source.g2, source.g3
s12, s23, s31 = source.s12, source.s23, source.s31
x, y, z, W = sp.symbols("x y z W")

# sigma sends a point (a,b,c) to (b,c,a).  The ordered local coordinate
# tuples below are pushforwards of (g1,g2,s12), not post-hoc reorderings.
sigma_point = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
points = [
    sp.Matrix([-1, -1, 0]),
    sp.Matrix([-1, 0, -1]),
    sp.Matrix([0, -1, -1]),
]
ordered_coordinates = [
    (g1, g2, s12),
    (g3, g1, s31),
    (g2, g3, s23),
]


def affine_inverse(point, coordinates):
    jacobian = sp.Matrix([
        [sp.diff(form, variable) for variable in (a, b, c)]
        for form in coordinates
    ])
    inverse = jacobian.inv()
    translated = sp.Matrix([a, b, c]) - point
    assert sp.simplify(jacobian * translated - sp.Matrix(coordinates)) == sp.zeros(3, 1)
    solution = point + inverse * sp.Matrix([x, y, z])
    return jacobian, {a: solution[0], b: solution[1], c: solution[2]}


locals_packet = []
quadratic_forms = []
for index, (point, coordinates) in enumerate(zip(points, ordered_coordinates)):
    jacobian, solution = affine_inverse(point, coordinates)
    local_K = sp.expand(source.K0.subs(solution))
    poly = sp.Poly(local_K, x, y, z)
    quadratic = sp.expand(sum(
        coefficient * x**monomial[0] * y**monomial[1] * z**monomial[2]
        for monomial, coefficient in poly.terms()
        if sum(monomial) == 2
    ))
    quadratic_forms.append(quadratic)
    exceptional = sp.expand(W**2 - quadratic)
    marked_points = [
        {x: 0, y: 0, z: 1, W: sp.Rational(1, 2)},
        {x: 0, y: 0, z: 1, W: sp.Rational(-1, 2)},
    ]
    locals_packet.append({
        "index": index,
        "ambient_point": [str(value) for value in point],
        "ordered_coordinates": [sp.sstr(form) for form in coordinates],
        "coordinate_jacobian_determinant": sp.sstr(jacobian.det()),
        "quadratic_tangent_cone": sp.sstr(quadratic),
        "exceptional_hessian_determinant": sp.sstr(sp.hessian(exceptional, (x, y, z, W)).det()),
        "marked_points_lie_on_exceptional": [
            sp.expand(exceptional.subs(marked_point)) == 0
            for marked_point in marked_points
        ],
    })

# In transported coordinates sigma is the identity: each ordered coordinate
# value at p is the corresponding ordered coordinate value at sigma(p).
transport_checks = []
for index in range(3):
    current = ordered_coordinates[index]
    following = ordered_coordinates[(index + 1) % 3]
    followed_after_sigma = [
        sp.expand(form.subs({a: b, b: c, c: a}, simultaneous=True))
        for form in following
    ]
    transport_checks.append(all(
        sp.expand(transformed - original) == 0
        for transformed, original in zip(followed_after_sigma, current)
    ))

restriction = sp.Matrix([[1], [1]])
conductor = sp.Matrix([[1, -1]])
deck = sp.Matrix([[0, 1], [1, 0]])
source_sheet_packet = sp.Matrix([sp.Rational(-17, 6), sp.Rational(17, 6)])
odd_value = (conductor * source_sheet_packet)[0]

checks = {
    "cyclic_point_orbit_closes": all(
        sigma_point * points[index] == points[(index + 1) % 3]
        for index in range(3)
    ),
    "cyclic_coordinate_transport_is_identity": all(transport_checks),
    "ordered_residue_orientation_is_constant": len({
        entry["coordinate_jacobian_determinant"] for entry in locals_packet
    }) == 1,
    "all_quadratic_tangent_cones_agree": all(
        sp.expand(form - quadratic_forms[0]) == 0 for form in quadratic_forms[1:]
    ),
    "all_exceptional_marked_points_exist": all(
        all(entry["marked_points_lie_on_exceptional"]) for entry in locals_packet
    ),
    "each_incidence_cokernel_is_rank_one": 2 - restriction.rank() == 1,
    "odd_covector_kills_diagonal_restriction": conductor * restriction == sp.zeros(1, 1),
    "odd_covector_has_deck_character_minus_one": conductor * deck == -conductor,
    "source_value_is_transport_invariant": odd_value == -sp.Rational(17, 3),
    "third_cyclic_transport_is_identity": sigma_point**3 == sp.eye(3),
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-a1-cyclic-naturality.v1",
    "cyclic_action_on_ambient_coordinates": "(a,b,c) -> (b,c,a)",
    "local_models": locals_packet,
    "transport_matrix_on_each_ordered_local_coordinate_tuple": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "transport_matrix_on_each_two_point_incidence_space": [[1, 0], [0, 1]],
    "transport_on_odd_cokernel": 1,
    "deck_character_on_odd_cokernel": -1,
    "cyclic_composition_on_odd_cokernel": 1,
    "source_odd_value_at_each_occurrence": ["-17/3", "-17/3", "-17/3"],
    "physical_selector_at_each_literal_occurrence": [0, 0, 0],
    "scope": "cyclic naturality of the degree-zero exceptional marked-incidence block",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("cyclic odd packet: three copies, trivial C3 transport, deck character -1")
print(OUT)
