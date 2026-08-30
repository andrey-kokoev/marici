"""Exact WP621 sign and center audit for finite positive Gaussian mediators."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

z = sp.symbols("z", real=True)
target_z = sp.Rational(576, 25)

couplings = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
masses_squared = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
offsets = [target_z * coupling for coupling in couplings]

A = sp.simplify(
    sum(
        coupling**2 / mass_squared
        for coupling, mass_squared in zip(couplings, masses_squared)
    )
)
B = sp.simplify(
    sum(
        coupling * offset / mass_squared
        for coupling, offset, mass_squared
        in zip(couplings, offsets, masses_squared)
    )
)
effective = sp.expand(
    -sp.Rational(1, 2)
    * sum(
        (coupling * z - offset) ** 2 / mass_squared
        for coupling, offset, mass_squared
        in zip(couplings, offsets, masses_squared)
    )
)
effective_curvature = sp.diff(effective, z, 2)
stationary_center = sp.simplify(B / A)

multiplicity = sp.symbols("N", positive=True, integer=True)
replicated_center = sp.simplify((multiplicity * B) / (multiplicity * A))

delta = sp.symbols("delta", real=True)
shifted_offsets = [
    offset + delta * coupling
    for offset, coupling in zip(offsets, couplings)
]
shifted_B = sp.simplify(
    sum(
        coupling * offset / mass_squared
        for coupling, offset, mass_squared
        in zip(couplings, shifted_offsets, masses_squared)
    )
)
shifted_center = sp.simplify(shifted_B / A)

zero_offset_effective = sp.expand(
    -sp.Rational(1, 2)
    * sum(
        coupling**2 * z**2 / mass_squared
        for coupling, mass_squared in zip(couplings, masses_squared)
    )
)

# Deliberate wrong-sign mass example: it yields positive z curvature but the
# mediator quadratic form itself has a negative eigenvalue.
wrong_sign_mass_matrix = sp.diag(1, 2, -1)
wrong_sign_inverse = wrong_sign_mass_matrix.inv()
coupling_vector = sp.Matrix(couplings)
wrong_sign_kappa = sp.simplify(
    -sp.Rational(1, 2)
    * (coupling_vector.T * wrong_sign_inverse * coupling_vector)[0]
)

checks = {
    "declared_mass_matrix_is_positive":
        all(value > 0 for value in masses_squared),
    "finite_tower_gram_coefficient_is_positive": A == 6,
    "tree_elimination_has_negative_curvature": effective_curvature == -A,
    "induced_quadratic_coefficient_is_negative":
        sp.expand(effective).coeff(z, 2) == -3,
    "target_center_requires_target_proportional_offsets":
        stationary_center == target_z,
    "stationary_center_is_a_maximum": effective_curvature < 0,
    "multiplicity_does_not_fix_or_move_center":
        replicated_center == target_z,
    "zero_offsets_select_only_zero_stationary_center":
        sp.solve(sp.diff(zero_offset_effective, z), z) == [0],
    "hostile_common_offset_deformation_moves_center":
        shifted_center == target_z + delta,
    "wrong_sign_mass_can_flip_curvature_only_with_instability":
        wrong_sign_kappa > 0
        and any(value < 0 for value in wrong_sign_mass_matrix.eigenvals()),
}

if not all(checks.values()):
    raise SystemExit(f"WP621 check failed: {checks}")
checks = {key: bool(value) for key, value in checks.items()}

result = {
    "work_package": "WP621",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "arbitrary finite towers of real Gaussian mediators with a positive mass-squared matrix and linear couplings to the relational coordinate z",
    "general_theorem": "eliminating sigma from one-half sigma^T M^2 sigma + sigma^T(g z-J) gives V_eff=-one-half(g z-J)^T(M^2)^-1(g z-J); the induced z^2 coefficient is nonpositive",
    "exact_example": {
        "couplings": ["1", "2", "3"],
        "masses_squared": ["1", "2", "3"],
        "gram_coefficient": "6",
        "induced_kappa": "-3",
        "offsets": ["576/25", "1152/25", "1728/25"],
        "stationary_center": "576/25",
    },
    "classification": "positive Gaussian mediation is a source-capable relational interaction and rigidifier, but cannot supply WP620's bounded positive curvature; its center is a free offset-to-coupling ratio and is a maximum before additional stabilization",
    "multiplicity_result": "replicating identical mediators rescales curvature and linear response equally, leaving the selected center unchanged",
    "smallest_exact_falsifier": "J_a -> J_a+delta g_a shifts z_star by exactly delta without changing masses, couplings, or multiplicities",
    "deliberate_failure": "a negative mediator mass-squared eigenvalue can make the induced z^2 coefficient positive, but the mediator source is then unstable",
    "physical_probe": "resolve mediator pole masses, residues proportional to g_a^2, and independently calibrated one-point offsets J_a; reconstruct both the curvature sign and z_star before comparing the flavor spectrum",
    "instrument_gate": "finite widths, mixing, offset calibration, and the root-vector mass/interference records must be evaluated in one source lineage",
    "remaining_source_gate": "derive a positive direct contact, loop effect, constrained auxiliary sector, or non-Gaussian stable completion together with its center; a positive Gaussian tower alone is closed",
}

out = ROOT / "results" / "wp621_positive_gaussian_center_migration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
