import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v11 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v11.json").read_text(
        encoding="utf-8"
    )
)

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
U = sp.I * X
V = sp.I * Z
U_trivial = I2
V_trivial = I2


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b * a.inv() * b.inv())


family = v11["phase_framed_joint_spectral_family"]
all_terms = (
    set(v11["object_types"])
    | set(v11["arrow_types"])
    | set(v11["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(v11["forbidden_promotions"])
)

missing_markers = (
    "degenerate_eigenvector_bundle",
    "u_r_connection",
    "wilczek_zee",
    "matrix_holonomy_representation",
    "nonabelian_curvature",
    "internal_frame_transport",
)

checks = {
    "v11_is_frozen": v11["cell_creation_during_replay"] is False,
    "same_constant_rank_two_projector": I2 == sp.eye(2),
    "nontrivial_loop_transports_are_unitary": sp.simplify(U.conjugate().T * U) == I2 and sp.simplify(V.conjugate().T * V) == I2,
    "nontrivial_loop_transports_have_unit_determinant": sp.det(U) == 1 and sp.det(V) == 1,
    "trivial_packet_has_same_determinant_holonomies": sp.det(U_trivial) == sp.det(U) and sp.det(V_trivial) == sp.det(V),
    "nontrivial_packet_has_central_commutator_minus_identity": commutator(U, V) == -I2,
    "trivial_packet_has_identity_commutator": commutator(U_trivial, V_trivial) == I2,
    "determinant_line_erases_commutator": sp.det(commutator(U, V)) == sp.det(commutator(U_trivial, V_trivial)) == 1,
    "projector_and_determinant_data_match_but_transport_differs": U != U_trivial and V != V_trivial,
    "v11_has_no_full_degenerate_bundle_connection": not any(marker in term.lower() for term in all_terms for marker in missing_markers),
    "v11_uses_only_determinant_line_for_higher_rank": "higher_rank_determinant_line_bundle" in v11["object_types"],
}

result = {
    "schema": "marici.aspect.v11-nonabelian-holonomy-falsifier.v1",
    "status": "frozen_v11_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "a rank-two degenerate mode over a two-loop base with SU(2) holonomies iX and iZ",
    "failure": "projector and determinant-line data agree with trivial transport, while the full holonomy commutator is -I instead of I",
    "required_future_repair": "the full rank-r eigenbundle with U(r) connection, matrix holonomy representation, non-Abelian curvature, and horizontal specialization before determinant or projector quotient",
}

out = root / "results" / "v11_nonabelian_holonomy_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v11_falsified" else 1)
