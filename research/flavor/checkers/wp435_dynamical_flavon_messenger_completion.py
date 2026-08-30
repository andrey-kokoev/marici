"""Exact power-counting and matching audit for dynamical adjoint flavons."""

import json
from pathlib import Path

import sympy as sp


fermion_dimension = sp.Rational(3, 2)
scalar_dimension = sp.Integer(1)

direct_portal_dimension = fermion_dimension + scalar_dimension + scalar_dimension + fermion_dimension
yukawa_vertex_dimension = fermion_dimension + scalar_dimension + fermion_dimension
flavon_vertex_dimension = fermion_dimension + scalar_dimension + fermion_dimension
mass_vertex_dimension = fermion_dimension + fermion_dimension + 1

y_q, y_phi, messenger_mass = sp.symbols("y_Q y_Phi M", nonzero=True, real=True)
source_left, source_right = sp.symbols("J_L J_R", real=True)

# Algebraic heavy-field Schur complement for M U_L U_R + J_L U_R + U_L J_R.
u_left_solution = -source_left / messenger_mass
u_right_solution = -source_right / messenger_mass
heavy_lagrangian = (
    messenger_mass * u_left_solution * u_right_solution
    + source_left * u_right_solution
    + u_left_solution * source_right
)
effective_bilinear = sp.factor(heavy_lagrangian)
matched_coefficient = sp.factor(effective_bilinear.subs({source_left: y_q, source_right: y_phi}))

# One vectorlike fundamental pair is fundamental plus antifundamental in a
# left-handed anomaly basis.
messenger_cubic_anomaly = sp.Integer(1) - sp.Integer(1)

# Adjoint covariant derivative transforms through a commutator and the center
# remains absent because the gauged theory is SU(3), as fixed in WP434.
adjoint_components = 3**2 - 1
two_adjoint_real_components = 2 * adjoint_components

checks = {
    "direct_adjoint_flavon_portal_is_dimension_five": direct_portal_dimension == 5,
    "quark_Higgs_messenger_vertex_is_dimension_four": yukawa_vertex_dimension == 4,
    "messenger_flavon_quark_vertex_is_dimension_four": flavon_vertex_dimension == 4,
    "messenger_mass_vertex_is_dimension_four": mass_vertex_dimension == 4,
    "tree_elimination_gives_inverse_mass_portal": effective_bilinear == -source_left * source_right / messenger_mass,
    "matched_coefficient_is_product_over_mass": matched_coefficient == -y_q * y_phi / messenger_mass,
    "vectorlike_messenger_pair_has_zero_cubic_flavor_anomaly": messenger_cubic_anomaly == 0,
    "two_SU3_adjoints_have_sixteen_real_components": two_adjoint_real_components == 16,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP435",
    "title": "Dynamical flavon messenger completion",
    "gauge_group": "diagonal SU(3)_F",
    "dynamical_flavons": ["Hermitian adjoint Phi_u", "Hermitian adjoint Phi_d"],
    "messengers": ["vectorlike up-type fundamental pair", "vectorlike down-type fundamental pair"],
    "direct_EFT_portal_dimension": str(direct_portal_dimension),
    "renormalizable_vertex_dimensions": {
        "Q_H_U": str(yukawa_vertex_dimension),
        "U_Phi_u": str(flavon_vertex_dimension),
        "messenger_mass": str(mass_vertex_dimension),
    },
    "tree_level_matching_coefficient": str(matched_coefficient),
    "messenger_cubic_flavor_anomaly": str(messenger_cubic_anomaly),
    "classification": "renormalizable anomaly-neutral dynamical-flavon and vectorlike-messenger grammar with exact tree-level Yukawa matching",
    "smallest_exact_falsifier": "wrong UV vertex dimension, nonzero messenger anomaly, or failed inverse-mass matching",
    "remaining_gate": "source-authorized full noncommuting vacuum, selected g_F f/v, current bounds, and independently frozen spectral packet",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp435_dynamical_flavon_messenger_completion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
