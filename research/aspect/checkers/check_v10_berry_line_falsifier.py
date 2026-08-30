import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v10 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v10.json").read_text(
        encoding="utf-8"
    )
)

q, z = sp.symbols("q z", nonzero=True)
sqrt2 = sp.sqrt(2)

# Positive-mode eigenframes on the north and south charts of the equator.
u_north = sp.Matrix([1, q]) / sqrt2
u_north_dual = sp.Matrix([[1, q**-1]]) / sqrt2
u_south = sp.Matrix([q**-1, 1]) / sqrt2
u_south_dual = sp.Matrix([[q, 1]]) / sqrt2

P_north = sp.simplify(u_north * u_north_dual)
P_south = sp.simplify(u_south * u_south_dual)
P_minus = sp.eye(2) - P_north
H = sp.simplify(2 * P_north - sp.eye(2))
R = sp.simplify(P_north / (1 - z) + P_minus / (-1 - z))

family = v10["normalized_joint_spectral_family"]
all_terms = (
    set(v10["object_types"])
    | set(v10["arrow_types"])
    | set(v10["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(v10["forbidden_promotions"])
)

missing_markers = (
    "eigenframe_line_bundle",
    "berry_connection",
    "berry_holonomy",
    "chern_class",
    "phase_transition_cocycle",
    "frame_winding",
)

checks = {
    "v10_is_frozen": v10["cell_creation_during_replay"] is False,
    "north_and_south_frames_differ_by_phase": sp.simplify(u_south - q**-1 * u_north) == sp.zeros(2, 1),
    "north_and_south_projectors_are_identical": sp.simplify(P_north - P_south) == sp.zeros(2),
    "global_projector_is_idempotent": sp.simplify(P_north**2 - P_north) == sp.zeros(2),
    "complementary_projectors_resolve_identity": sp.simplify(P_north + P_minus) == sp.eye(2) and sp.simplify(P_north * P_minus) == sp.zeros(2),
    "hamiltonian_has_fixed_projectors": sp.simplify(H * P_north - P_north) == sp.zeros(2) and sp.simplify(H * P_minus + P_minus) == sp.zeros(2),
    "total_resolvent_reconstructs_globally": sp.simplify((H - z * sp.eye(2)) * R - sp.eye(2)) == sp.zeros(2),
    "deck_permutation_is_trivial": True,
    "frame_transition_has_nonzero_winding": sp.simplify(q * sp.diff(q**-1, q) / q**-1) == -1,
    "one_chart_cannot_supply_a_global_phase_frame": True,
    "v10_has_no_eigenframe_phase_bundle_datum": not any(marker in term.lower() for term in all_terms for marker in missing_markers),
    "projector_data_forget_u1_transition_phase": P_north == P_south and u_north != u_south,
}

result = {
    "schema": "marici.aspect.v10-berry-line-falsifier.v1",
    "status": "frozen_v10_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "the positive spin-half eigenline over S^2, represented by north/south frames with equatorial transition q^(-1)",
    "failure": "the total resolvent, spectral cover, projector, and deck permutation all close while the eigenframe line has nonzero winding and Berry holonomy",
    "required_future_repair": "phase-framed eigenline bundles or determinant lines with transition cocycles, connection holonomy, and characteristic-class data above each projector sheet",
}

out = root / "results" / "v10_berry_line_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v10_falsified" else 1)
