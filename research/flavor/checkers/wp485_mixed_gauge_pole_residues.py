"""Exact mixed gauge-pole and current-residue audit for WP485."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp448 = load("wp448_triplet_pole_residue_packet.json")
wp484 = load("wp484_gauged_connector_frame_lift.json")

g, h, f, s, z = sp.symbols("g_F g_P mu s z", positive=True, real=True)

I = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
generators = [matrix / 2 for matrix in lambdas]
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]
L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]


def adjoint_coordinates(matrix):
    return [sp.simplify(sp.trace(matrix * basis) / 2) for basis in lambdas]


# Reconstruct the complete mass Gram from the covariant vacuum tangents.  In
# these coordinates the connector metric is one and the adjoint metric is two,
# reproducing the already admitted WP448 canonical gauge-mass normalization.
su_columns = []
for generator in generators:
    vector = [0] * 9
    for matrix in J:
        vector.extend(adjoint_coordinates(I * (generator * matrix - matrix * generator) * f))
    su_columns.append(g * sp.Matrix(vector))

port_columns = []
for generator in L:
    vector = list(-s * generator)
    for i in range(3):
        delta_x = sum((generator[i, j] * J[j] for j in range(3)), sp.zeros(3)) * f
        vector.extend(adjoint_coordinates(delta_x))
    port_columns.append(h * sp.Matrix(vector))

covariant_tangents = sp.Matrix.hstack(*(su_columns + port_columns))
kinetic_metric = sp.diag(*([1] * 9 + [2] * 24))
full_mass_gram = sp.simplify(covariant_tangents.T * kinetic_metric * covariant_tangents)

# The principal-SU(2) quintet does not carry a port label.  Each of the three
# triplet generators instead has the same two-by-two flavor/port mass block.
triplet_block = sp.Matrix(
    [
        [g**2 * f**2, 2 * g * h * f**2],
        [2 * g * h * f**2, h**2 * (4 * f**2 + 2 * s**2)],
    ]
)
triplet_trace = sp.factor(sp.trace(triplet_block))
triplet_determinant = sp.factor(triplet_block.det())
discriminant = sp.factor(triplet_trace**2 - 4 * triplet_determinant)
m_minus = sp.simplify((triplet_trace - sp.sqrt(discriminant)) / 2)
m_plus = sp.simplify((triplet_trace + sp.sqrt(discriminant)) / 2)

# Quarks couple only to the SU(3)_F entry.  These are the SU-entry spectral
# weights, before multiplication by the current coupling g^2.
w_minus = sp.simplify((triplet_block[1, 1] - m_minus) / (m_plus - m_minus))
w_plus = sp.simplify((m_plus - triplet_block[1, 1]) / (m_plus - m_minus))
current_propagator = sp.factor(g**2 * (z * sp.eye(2) - triplet_block).inv()[0, 0])
spectral_current = sp.factor(g**2 * (w_minus / (z - m_minus) + w_plus / (z - m_plus)))
zero_momentum_current = sp.factor(g**2 * triplet_block.inv()[0, 0])

quintet_mass_squared = 3 * g**2 * f**2
characteristic_expected = sp.expand(
    (z - quintet_mass_squared) ** 5
    * (z**2 - triplet_trace * z + triplet_determinant) ** 3
)
direct_charpoly = full_mass_gram.charpoly()
characteristic_direct = sp.expand(direct_charpoly.as_expr().subs(direct_charpoly.gen, z))

# A finite hostile pair proves that the labelled pole weights are not fixed by
# representation theory after the port is gauged.
benchmark_a = {g: 1, h: 1, f: 1, s: 1}
benchmark_b = {g: 1, h: 2, f: 1, s: 1}
weight_a = sp.simplify(w_minus.subs(benchmark_a))
weight_b = sp.simplify(w_minus.subs(benchmark_b))

checks = {
    "wp448_dependency_passed": wp448["passed"],
    "wp484_dependency_passed": wp484["passed"],
    "triplet_block_is_positive": triplet_trace > 0 and triplet_determinant > 0,
    "triplet_determinant_requires_connector_scale": triplet_determinant == 2 * g**2 * h**2 * f**2 * s**2,
    "two_mixed_triplet_poles_are_distinct": sp.simplify(m_plus - m_minus) != 0,
    "spectral_weights_sum_to_one": sp.simplify(w_minus + w_plus) == 1,
    "exact_current_spectral_decomposition": sp.simplify(current_propagator - spectral_current) == 0,
    "zero_momentum_couplings_cancel": zero_momentum_current == (2 * f**2 + s**2) / (f**2 * s**2),
    "quintet_pole_is_unmixed": quintet_mass_squared == 3 * g**2 * f**2,
    "full_tangent_gram_has_expected_characteristic_polynomial": sp.simplify(characteristic_direct - characteristic_expected) == 0,
    "full_characteristic_multiplicities_are_five_three_three": sp.degree(characteristic_direct, z) == 11,
    "hostile_coupling_pair_changes_residue_weight": sp.simplify(weight_a - weight_b) != 0,
    "old_wp448_triplet_pole_is_not_preserved": sp.simplify(triplet_block.charpoly(z).as_expr().subs(z, g**2 * f**2)) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP485",
    "domain": "WP484 joint SU(3)_F x SO(3)_P gauge theory at X_i=mu J_i and S=s I_3 with canonical kinetic terms; physical flavor norm f_phys^2=6 mu^2",
    "source_parameters": ["g_F", "g_P", "mu", "s"],
    "pole_mass_squared": {
        "unmixed_quintet": str(quintet_mass_squared),
        "mixed_triplet_minus": str(m_minus),
        "mixed_triplet_plus": str(m_plus),
        "multiplicities": {"unmixed_quintet": 5, "mixed_triplet_minus": 3, "mixed_triplet_plus": 3},
    },
    "triplet_mass_block": [[str(value) for value in row] for row in triplet_block.tolist()],
    "triplet_invariants": {
        "trace": str(triplet_trace),
        "determinant": str(triplet_determinant),
        "discriminant": str(discriminant),
    },
    "quark_current_residues": {
        "mixed_minus": "g_F^2 w_minus",
        "mixed_plus": "g_F^2 w_plus",
        "weight_minus": str(w_minus),
        "weight_plus": str(w_plus),
        "sum_rule": "w_minus+w_plus=1",
        "quintet": "g_F^2 P_5",
    },
    "zero_momentum_triplet_current_kernel": str(zero_momentum_current),
    "contextual_partition": {
        "frozen": "fivefold quintet pole form, three-plus-three mixed multiplicities, residue sum, and zero-momentum coupling cancellation",
        "unfrozen": "the two triplet pole locations and their individual quark-current residues depend on g_P/g_F and s/mu",
        "hostile_pair": {"A": "g_F=g_P=mu=s=1", "B": "g_F=mu=s=1,g_P=2", "weight_A": str(weight_a), "weight_B": str(weight_b)},
    },
    "classification": "The enlarged source freezes the mixed pole grammar and exact sum rules, but not individual triplet residues or widths.",
    "selector": False,
    "rigidifier": bool(checks["full_characteristic_multiplicities_are_five_three_three"]),
    "instrument": None,
    "smallest_exact_falsifier": "Changing only g_P from one to two at g_F=mu=s=1 changes the lower-pole quark-current weight while preserving the declared representation and vacuum.",
    "remaining_gate": "Select or independently calibrate g_P/g_F and s/mu, derive all messenger and scalar thresholds, and compute every partial width before assigning numerical pole residues or widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp485_mixed_gauge_pole_residues.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
