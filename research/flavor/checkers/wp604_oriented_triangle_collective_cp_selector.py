"""Exact WP604 oriented-triangle collective CP selector."""

import itertools
import json
from pathlib import Path

import sympy as sp


theta_1, theta_2, theta_3, epsilon = sp.symbols(
    "theta_1 theta_2 theta_3 epsilon", real=True
)
angles = (theta_1, theta_2, theta_3)

base = 3 + 2 * (
    sp.cos(theta_1 - theta_2)
    + sp.cos(theta_2 - theta_3)
    + sp.cos(theta_3 - theta_1)
)
orientation = (
    sp.cos(theta_1 + 2 * theta_2 - 3 * theta_3)
    + sp.cos(theta_2 + 2 * theta_3 - 3 * theta_1)
    + sp.cos(theta_3 + 2 * theta_1 - 3 * theta_2)
)
potential = base * (1 + epsilon * orientation)

vacuum = {theta_1: 0, theta_2: 2 * sp.pi / 3, theta_3: 4 * sp.pi / 3}
conjugate_vacuum = {
    theta_1: 0,
    theta_2: -2 * sp.pi / 3,
    theta_3: -4 * sp.pi / 3,
}

# The cosine charge set makes the exact permutation symmetry transparent.
positive_charges = ((1, 2, -3), (-3, 1, 2), (2, -3, 1))
oriented_charge_set = set(positive_charges) | {
    tuple(-entry for entry in charge) for charge in positive_charges
}


def permute_charge(charge, permutation):
    inverse = [permutation.index(index) for index in range(3)]
    return tuple(charge[inverse[index]] for index in range(3))


permutation_symmetries = []
for permutation in itertools.permutations(range(3)):
    transformed = {
        permute_charge(charge, permutation) for charge in oriented_charge_set
    }
    if transformed == oriented_charge_set:
        permutation_symmetries.append(permutation)

cyclic_permutations = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]

# The complete pair graph in B forces every torus-preserving diagonal
# rephasing to be common.  Its incidence kernel is the global U(1) direction.
pair_incidence = sp.Matrix([[1, -1, 0], [0, 1, -1], [1, 0, -1]])
rephasing_kernel = pair_incidence.nullspace()

cyclic_difference = sp.trigsimp(
    orientation.subs(
        {theta_1: theta_2, theta_2: theta_3, theta_3: theta_1},
        simultaneous=True,
    )
    - orientation
)
cp_difference = sp.trigsimp(
    orientation.subs(
        {theta_1: -theta_1, theta_2: -theta_2, theta_3: -theta_3},
        simultaneous=True,
    )
    - orientation
)
reflection_difference = sp.trigsimp(
    orientation.subs({theta_2: theta_3, theta_3: theta_2}, simultaneous=True)
    - orientation
)
reflection_witness = sp.simplify(
    reflection_difference.subs(
        {theta_1: 0, theta_2: sp.pi / 3, theta_3: sp.pi / 2}
    )
)

gauge_fixed_potential = potential.subs(theta_1, 0)
gauge_hessian = sp.simplify(
    sp.hessian(gauge_fixed_potential, (theta_2, theta_3)).subs(vacuum)
)
gauge_hessian_eigenvalues = gauge_hessian.eigenvals()

omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
phase_vacuum = sp.Matrix([1, omega, omega**2])
phase_conjugate = sp.conjugate(phase_vacuum)
cyclic_matrix = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
reflection_matrix = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])


def proportional(left, right):
    return all(
        sp.simplify(left[first] * right[second] - left[second] * right[first])
        == 0
        for first in range(3)
        for second in range(first + 1, 3)
    )


cyclic_cp_stabilizers = [
    power
    for power in range(3)
    if proportional(cyclic_matrix**power * phase_conjugate, phase_vacuum)
]
reflection_cp_stabilizes = proportional(
    reflection_matrix * phase_conjugate, phase_vacuum
)

checks = {
    "triangle_base_vanishes_on_equilateral_vacuum": sp.simplify(
        base.subs(vacuum)
    )
    == 0,
    "orientation_carrier_value_is_minus_three_halves": sp.simplify(
        orientation.subs(vacuum)
    )
    == sp.Rational(-3, 2),
    "orientation_carrier_is_cyclic": cyclic_difference == 0,
    "orientation_carrier_is_bare_cp_even": cp_difference == 0,
    "orientation_carrier_breaks_reflection": reflection_witness
    == sp.Rational(3, 2) - sp.sqrt(3) / 2,
    "exact_permutation_symmetry_is_c3": set(permutation_symmetries)
    == set(cyclic_permutations),
    "base_rephasing_kernel_is_only_common_u1": rephasing_kernel
    == [sp.Matrix([1, 1, 1])],
    "gauge_fixed_hessian_has_positive_modes_in_declared_domain": (
        gauge_hessian_eigenvalues
        == {1 - 3 * epsilon / 2: 1, 3 - 9 * epsilon / 2: 1}
    ),
    "no_cyclic_generalized_cp_stabilizes_vacuum": cyclic_cp_stabilizers == [],
    "restoring_reflection_would_restore_generalized_cp": reflection_cp_stabilizes,
    "conjugate_vacuum_is_also_zero": sp.simplify(base.subs(conjugate_vacuum))
    == 0,
}

if not all(checks.values()):
    raise SystemExit(f"WP604 check failed: {checks}")

result = {
    "work_package": "WP604",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "state_domain": "three labelled unit-modulus source phases, quotiented by common U(1) phase and internal cyclic permutation C3",
    "positive_source_family": "V=|z1+z2+z3|^2*(1+epsilon*F), with |epsilon|<1/3 and F the declared cyclic CP-even orientation carrier",
    "selected_zero_set": "equilateral phase triples and their common-phase translates",
    "selected_relation": "pairwise phase separation 2*pi/3 with two CP-conjugate chiral orbits",
    "permutation_group": "exactly C3; the transposition that would repair CP is not a symmetry",
    "classification": "progressive coefficient-independent collective CP selector on the source phase quotient; not yet a physical16 flavor selector",
    "smallest_exact_falsifier": "adding the missing reflection makes reflection composed with CP stabilize the selected vacuum",
    "hard_to_vary_content": "for every |epsilon|<1/3 the positive carrier has the same zero set and positive gauge-fixed Hessian modes",
    "source_authority_gate": "derive the oriented cyclic carrier and its higher-degree interaction from microscopic fields rather than declaring it because it removes generalized CP",
    "instrument_gate": "resolve the orientation-carrier mediators and their sign-sensitive shared-channel interference, then derive descent to physical16",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp604_oriented_triangle_collective_cp_selector.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
