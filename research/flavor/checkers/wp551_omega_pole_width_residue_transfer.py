"""Exact Omega transfer for WP534 poles, widths, and residues."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp534 = load("wp534_invariant_complex_pole_packet.json")
wp550 = load("wp550_omega_scale_setting_constructor.json")

# Six complex pole squares, six widths, and six dimensionless signed residues.
dimensions = sp.Matrix([2] * 6 + [1] * 6 + [0] * 6)
J = sp.zeros(18, 20)
for i, dimension in enumerate(dimensions):
    J[i, i] = 1
    J[i, 18] = -dimension
    J[i, 19] = dimension

# Under a lattice-unit reparameterization, a dimension-d raw coordinate moves
# by d and a*m_Omega moves by one. The physical Omega convention is fixed.
lattice_unit_tangent = sp.Matrix(list(dimensions) + [1, 0])
external_omega_tangent = sp.Matrix([0] * 19 + [1])

scale_lattice_variance, scale_physical_variance = sp.symbols(
    "s_scale_lattice s_scale_physical", positive=True
)
shared_scale_variance = scale_lattice_variance**2 + scale_physical_variance**2
scale_covariance = sp.simplify(shared_scale_variance * dimensions * dimensions.T)

dimensionful = [i for i, d in enumerate(dimensions) if d != 0]
dimensionless = [i for i, d in enumerate(dimensions) if d == 0]

signed_residues = wp534["signed_bs_pole_residues"]
checks = {
    "dependencies_passed": bool(wp534["passed"] and wp550["passed"]),
    "six_signed_residues_are_present": len(signed_residues) == 6,
    "typed_transfer_has_rank_eighteen": J.rank() == 18,
    "lattice_unit_reparameterization_cancels": J * lattice_unit_tangent
    == sp.zeros(18, 1),
    "external_omega_moves_outputs_by_mass_dimension": J * external_omega_tangent
    == dimensions,
    "twelve_dimensionful_outputs_depend_on_scale": len(dimensionful) == 12
    and all(any(scale_covariance[i, j] != 0 for j in range(18)) for i in dimensionful),
    "six_residues_have_zero_scale_covariance": len(dimensionless) == 6
    and all(scale_covariance[i, j] == 0 for i in dimensionless for j in range(18)),
    "pole_width_cross_covariance_is_shared": all(
        scale_covariance[i, j] == 2 * shared_scale_variance
        for i in range(6)
        for j in range(6, 12)
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP551",
    "domain": "The six signed simple poles of the frozen WP534 source witness, composed with the unexecuted same-ensemble Omega scale-setting architecture of WP550.",
    "quantity_types": {
        "complex_pole_squared": {"count": 6, "mass_dimension": 2},
        "tree_width": {"count": 6, "mass_dimension": 1},
        "signed_resolvent_residue": {"count": 6, "mass_dimension": 0},
    },
    "transfer_rule": "q_physical=q_hat*(m_Omega_physical/(a*m_Omega))^d",
    "log_jacobian": [[str(x) for x in row] for row in J.tolist()],
    "rank": J.rank(),
    "dimension_vector": [int(x) for x in dimensions],
    "covariance": {
        "rule": "C_physical=J C_joint J^T",
        "common_scale_block": [[str(x) for x in row] for row in scale_covariance.tolist()],
        "interpretation": "The shared Omega latent variable correlates every pole-square and width output but contributes zero covariance to dimensionless residues.",
    },
    "deletion_replay": {
        "invalidated_output_indices": dimensionful,
        "scale_valid_output_indices": dimensionless,
        "rule": "Deleting either Omega scale input invalidates all twelve dimensionful outputs together. Residues remain scale-independent but still require current normalization and operator covariance.",
    },
    "correction": "WP550's statement that scale deletion invalidates residues was too broad. The WP534 resolvent residues are dimensionless; their authority gate is renormalization and operator normalization, not the energy-unit transfer.",
    "classification": "Exact dimension-typed scale and covariance transfer on a frozen benchmark; identification architecture, neither selector nor executed calibration.",
    "selector": bool(wp550["selector"]),
    "instrument": "Not yet executed. Requires WP542 same-ensemble Omega, flow, pole-kernel, width, and current-normalization measurements with one full covariance and timestamped calibration state.",
    "smallest_exact_falsifier": "Assign a nonzero Omega-scale covariance to a dimensionless residue, or delete the shared Omega latent variable while retaining any dimensionful pole-square or width as calibrated.",
    "remaining_gate": "Generate the actual WP542 joint ensemble data, drift record, disturbances, renormalized current response, and full covariance. Selection additionally requires an independent source equation with nonzero WP546 transversality.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp551_omega_pole_width_residue_transfer.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
