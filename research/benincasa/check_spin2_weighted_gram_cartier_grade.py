#!/usr/bin/env python3
"""Spin-two Cartier grade at the collinear external Gram wall."""

import json
from pathlib import Path

import sympy as sp


uy, uz, theta, w = sp.symbols("uy uz theta w", real=True)

quadrupole = sp.Matrix([uy**2 - uz**2, 2 * uy * uz])
origin = {uy: 0, uz: 0}
assert quadrupole.subs(origin) == sp.zeros(2, 1)
assert quadrupole.jacobian([uy, uz]).subs(origin) == sp.zeros(2, 2)

# The second-normal map Sym^2(N) -> Sym^2_0 has rank two and radial kernel.
second_normal_basis = sp.Matrix([uy**2, uy * uz, uz**2])
coefficient_matrix = sp.Matrix([[1, 0, -1], [0, 2, 0]])
assert quadrupole == coefficient_matrix * second_normal_basis
assert coefficient_matrix.rank() == 2
assert coefficient_matrix.nullspace() == [sp.Matrix([1, 0, 1])]

# The physical triangle approaches the wall in one labelled transverse
# direction.  Its weighted coordinate is w=theta^2.
physical_path = {uy: theta, uz: 0}
physical_quadrupole = quadrupole.subs(physical_path)
assert physical_quadrupole == sp.Matrix([theta**2, 0])
weighted_quadrupole = physical_quadrupole.subs(theta**2, w)
assert weighted_quadrupole == sp.Matrix([w, 0])

# Ordinary value and first theta jet vanish; the first w grade maps by a unit.
assert physical_quadrupole.subs(theta, 0) == sp.zeros(2, 1)
assert physical_quadrupole.diff(theta).subs(theta, 0) == sp.zeros(2, 1)
assert weighted_quadrupole.diff(w).subs(w, 0) == sp.Matrix([1, 0])

# The local two-term physical path complex is rank one -> rank one with unit
# differential, hence has zero kernel and cokernel.
cartier_map = sp.Matrix([[1]])
assert cartier_map.rank() == 1
assert len(cartier_map.nullspace()) == 0
assert cartier_map.T.nullspace() == []

packet = {
    "schema": "marici.benincasa.spin2-weighted-gram-cartier-grade.v1",
    "status": "passed",
    "gram_stabilizer": "SO(2) rotations around the collinear external axis",
    "ordinary_tensor_fiber": {
        "spin2_invariants": 0,
        "physical_value": 0,
        "first_theta_jet": 0,
    },
    "second_normal_map": {
        "formula": ["uy^2-uz^2", "2*uy*uz"],
        "domain_rank": 3,
        "image_rank": coefficient_matrix.rank(),
        "kernel": "radial trace uy^2+uz^2",
    },
    "physical_weighted_path": {
        "normal": "u=(theta,0)",
        "weight": "w=theta^2",
        "observer_image": ["w", "0"],
        "first_w_grade_rank": 1,
        "cartier_map": [[1]],
        "cone_homology_rank": 0,
    },
    "rank60_compatibility": {
        "source": "Entry 2439",
        "weighted_interaction_rank": 7,
        "additional_tensor_kernel": 0,
    },
    "support": {
        "wall": "existing external Gram divisor Lambda=0",
        "exception": "soft support where the weighted chart determinant -P1*P2 vanishes",
        "new_carrier_support": False,
    },
    "scope_warning": (
        "This is the universal local spin-two normal representation and its "
        "one-direction physical path. It does not normalize a global period "
        "or assert activation of the cross port on the rotational quotient."
    ),
}

output = Path(__file__).with_name("spin2-weighted-gram-cartier-grade.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
