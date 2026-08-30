"""Exact extended-quotient audit of the messenger-generated portal threshold."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp478 = load("wp478_messenger_portal_threshold.json")
wp492 = load("wp492_canonical_messenger_tensor_grammar.json")
wp543 = load("wp543_existing_source_constraint_kernel.json")
wp546 = load("wp546_selector_transversality_normal_form.json")

# Extended log-coordinate order:
# a, w, g_F^2, g_P^2, y_Q, y_Phi, eta, k_Phi.
J0 = sp.Matrix([[sp.sympify(x) for x in row] + [0, 0, 0, 0] for row in wp543["authorized_equalities"]["jacobian"]])
threshold_row = sp.Matrix([[1, 0, 0, 0, -2, -2, 1, -1]])
J = J0.col_join(threshold_row)

old_tangent = sp.Matrix([2, -1, 0, 0, 0, 0, 0, 0])
compensated_yq = sp.Matrix([2, -1, 0, 0, 1, 0, 0, 0])
compensated_yphi = sp.Matrix([2, -1, 0, 0, 0, 1, 0, 0])
target_gradient = sp.Matrix([[-sp.Rational(1, 2), 0, sp.Rational(1, 2), 0, 0, 0, 0, 0]])
portal_combination_gradient = sp.Matrix([[0, 0, 0, 0, 2, 2, -1, 1]])

width_yq_row = sp.Matrix([[0, 0, 0, 0, 2, 0, 0, 0]])
residue_yphi_row = sp.Matrix([[0, 0, 0, 0, 0, 2, 0, 0]])
instrument_augmented = J.col_join(width_yq_row).col_join(residue_yphi_row)

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in (wp478, wp492, wp543, wp546)),
    "threshold_is_source_derived": "source-generated" in wp478["classification"].lower(),
    "projected_threshold_row_is_transverse": (threshold_row * old_tangent)[0] == 2,
    "extended_source_jacobian_has_rank_four": J.rank() == 4,
    "extended_source_kernel_has_dimension_four": len(J.nullspace()) == 4,
    "yq_compensated_tangent_survives": J * compensated_yq == sp.zeros(4, 1),
    "yphi_compensated_tangent_survives": J * compensated_yphi == sp.zeros(4, 1),
    "compensated_tangent_changes_target": (target_gradient * compensated_yq)[0] == -1,
    "threshold_moves_freedom_into_portal_combination": (
        portal_combination_gradient * compensated_yq
    )[0]
    == 2,
    "two_formal_spectral_rows_still_leave_source_kernel": instrument_augmented.rank() < 8,
    "messenger_packet_has_unfixed_normalizations": len(wp492["tensor_packet"]) == 10,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP547",
    "domain": "The WP543 fixed-v source quotient extended by the messenger-threshold coordinates log y_Q, log y_Phi, log eta, and log k_Phi.",
    "coordinate_order": [
        "log a",
        "log w",
        "log g_F^2",
        "log g_P^2",
        "log y_Q",
        "log y_Phi",
        "log eta",
        "log k_Phi",
    ],
    "threshold_relation": "log a-2 log y_Q-2 log y_Phi+log eta-log k_Phi=constant",
    "extended_jacobian": [[str(x) for x in row] for row in J.tolist()],
    "rank": J.rank(),
    "kernel_dimension": len(J.nullspace()),
    "projected_old_tangent_contraction": str((threshold_row * old_tangent)[0]),
    "surviving_hostile_tangents": {
        "y_Q_compensated": [str(x) for x in compensated_yq],
        "y_Phi_compensated": [str(x) for x in compensated_yphi],
        "target_derivative": str((target_gradient * compensated_yq)[0]),
    },
    "factorization": {
        "first_arrow": "The finite messenger loop fixes the sign and functional form and relates a to the portal combination y_Q^2 y_Phi^2 k_Phi/eta.",
        "first_nonfaithful_arrow": "Projection from the extended source packet to a alone forgets the continuously variable portal combination.",
        "readout_arrow": "Messenger widths or residues may identify realized Yukawa combinations if independently calibrated, but they do not reduce the source-label family.",
    },
    "theorem": "The WP478 messenger threshold is transverse to the old four-coordinate t tangent, but it is not a numerical selector on the faithful extended source quotient. The exact compensated tangent (2,-1,0,0,1,0,0,0) preserves every admitted source equality and the threshold relation while changing log(g_F f/v) by -1. The threshold transfers the ambiguity from a into a messenger normalization.",
    "classification": "Source-derived interaction rigidifier and transverse conditional relation; not a numerical selector on the extended source quotient.",
    "selector": bool(wp478["selector"]),
    "rigidifier": bool(wp478["rigidifier"]),
    "instrument": "Independently calibrated messenger widths and residues could identify the realized compensating normalization, but would remain readouts rather than source equations.",
    "smallest_exact_falsifier": "Increase t with d log a=2 and d log w=-1 while rescaling y_Q with d log y_Q=1. The fixed-v and messenger-threshold equations remain exact, but d log(g_F f/v)=-1.",
    "remaining_gate": "Derive the portal combination y_Q^2 y_Phi^2 k_Phi/eta from the WP545-complete source dynamics. Only after that selection may widths and residues be recomputed and independently calibrated as tests.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp547_threshold_kernel_transfer.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
