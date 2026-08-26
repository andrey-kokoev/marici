"""Exact preregistration checker for the bounded threshold experiment."""

import json
from pathlib import Path

import sympy as sp


gamma = sp.Symbol("Gamma_c", positive=True, real=True)
omega = sp.Symbol("omega_c", real=True)

rivals = (
    "R_two_adjoint",
    "R_auxiliary",
    "R_contact",
)
readouts = (
    "loss_minus",
    "loss_center",
    "loss_plus",
    "contact_far",
)
offsets = (sp.Integer(-2), sp.Integer(0), sp.Integer(2), sp.Integer(6))
frequencies = tuple(omega + offset * gamma for offset in offsets)
sigma = gamma / 2
window = (omega - 3 * gamma, omega + 7 * gamma)

packet = {
    "work_package": "WP428",
    "title": "Threshold experiment preregistration",
    "status": "frozen_before_response_calculation",
    "scope": "bounded three-rival non-gauge class; no open-world authority",
    "rivals": list(rivals),
    "low_energy_matching_rule": "same frozen low-energy coefficient packet before threshold unblinding",
    "preparation": {
        "command": "common calibrated scalar-current impulse u(t)",
        "fluence": "one detector-control unit",
        "normalization_channel": "inclusive control channel disjoint from selector-facing bins",
        "authority": "conditional until a common physical portal is demonstrated",
    },
    "readouts": list(readouts),
    "frequency_offsets_in_Gamma_c": [str(value) for value in offsets],
    "frequencies": [str(value) for value in frequencies],
    "detector": {
        "kernel": "normalized Gaussian",
        "sigma": str(sigma),
        "scan_window": [str(value) for value in window],
        "contact_subtraction": "sideband coefficients frozen before unblinding",
    },
    "successor_acceptance": {
        "bounded_contextual_rank": len(rivals),
        "robustness": "smallest singular value positive on separately declared uncertainty set",
        "selection_authority": "requires independently sourced WP128 preparation law in addition to rank",
    },
    "falsifiers": [
        "no common physical preparation portal",
        "two rival columns identical after smearing and subtraction",
        "rank below three",
        "smallest singular value reaches zero under admitted uncertainty",
        "normalization or subtraction uses selector-facing bins",
        "a predeclared external rival reproduces all four readouts",
        "threshold settings moved after inspecting the outcome",
    ],
}

forbidden_outcome_keys = {
    "response_matrix", "rank", "determinant", "singular_values",
    "smallest_singular_value", "passed_rank",
}
checks = {
    "exactly_three_unique_rivals_frozen": len(rivals) == 3 and len(set(rivals)) == 3,
    "exactly_four_unique_readouts_frozen": len(readouts) == 4 and len(set(readouts)) == 4,
    "frequency_offsets_are_predeclared_and_distinct": offsets == (-2, 0, 2, 6) and len(set(offsets)) == 4,
    "gaussian_resolution_is_positive": sigma.is_positive,
    "scan_window_contains_all_centers": all(sp.simplify(value - window[0]) >= 0 and sp.simplify(window[1] - value) >= 0 for value in frequencies),
    "control_normalization_is_disjoint_by_declaration": "disjoint" in packet["preparation"]["normalization_channel"],
    "bounded_rank_target_matches_rival_count": packet["successor_acceptance"]["bounded_contextual_rank"] == len(rivals),
    "physical_portal_authority_remains_conditional": packet["preparation"]["authority"].startswith("conditional"),
    "no_response_or_rank_outcome_is_present": forbidden_outcome_keys.isdisjoint(packet.keys()) and forbidden_outcome_keys.isdisjoint(packet["detector"].keys()),
    "falsifier_list_is_frozen_and_nonempty": len(packet["falsifiers"]) == 7 and len(set(packet["falsifiers"])) == 7,
}
checks = {name: bool(value) for name, value in checks.items()}
packet["checks"] = checks
packet["passed"] = all(checks.values())

out = Path(__file__).parents[1] / "results" / "wp428_threshold_experiment_preregistration.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
raise SystemExit(0 if packet["passed"] else 1)
