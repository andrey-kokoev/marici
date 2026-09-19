from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/coherent-resolution-programme-frontier.v3.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    prior = load("research/nima/results/coherent-resolution-programme-frontier.v2.json")
    evans = load("research/voevodsky/results/first-xi-zero-unchanged-evans-adjoint-hilbert-residual.interval.v1.json")
    repairs = load("research/voevodsky/results/evans-modified-state-candidate-audit.json")
    tail = load("research/nima/results/full-tail-reciprocal-sewing-frontier.json")
    placement = load("research/nima/results/evans-to-full-tail-placement-frontier.json")
    trace = load("research/nima/results/conservative-cyclic-trace-coordinate-frontier.json")
    ident = load("research/nima/results/conservative-trace-identifiability.json")
    g4 = load("research/aspect/contracts/theta-rh-interaction-net-state.v17.json")

    checks = {
        "v2_frontier_passed": prior["status"] == "audited_frontier_reclassified",
        "unchanged_evans_state_rigorously_rejected": evans["status"] == "certified_strictly_negative",
        "no_materialized_modified_state_passes": repairs["status"] == "unchanged_state_rejected_no_existing_modified_candidate_admissible",
        "one_sided_full_tail_closed_but_augmented_sewing_open": tail["status"] == "scalar_xi_square_sewing_closed_typed_augmented_six_port_identity_open",
        "evans_linear_observer_components_exist_but_chain_square_open": placement["status"] == "linear_observer_components_identified_joint_chain_square_open",
        "native_bordered_packet_complete": trace["checks"]["all_native_coordinate_formulas_constructed"],
        "three_independent_trace_equalities_open": trace["status"] == "native_four_coordinate_packet_complete_three_independent_trace_equalities_open",
        "combined_rows_leave_one_parameter": ident["status"] == "combined_shell_and_stokes_data_leave_one_coordinate_ambiguity",
        "canonical_g4_closed_definitionally": g4["claim_boundary"]["analytical_G4_forward_realization_constructed"] and g4["claim_boundary"]["canonical_counterflow_cancellation"],
        "canonical_g4_not_independent_xi_criterion": not g4["claim_boundary"]["independent_Xi_RH_criterion"],
    }

    out = {
        "schema": "marici.nima.coherent-resolution-programme-frontier.v3",
        "status": "post_interval_evans_and_trace_identifiability_frontier" if all(checks.values()) else "failed",
        "checks": checks,
        "delta_from_v2": [
            "unchanged Evans membership is now rigorously falsified, not merely numerically hostile",
            "the full tail-state modification has a source-derived one-sided conservative factorization",
            "its doubled off-divisor augmented sewing and Evans chain placement remain open",
            "the pair-to-Euler cyclic response already carries all four bordered coordinates",
            "independent conservative trace comparison is open only on E, W, and R",
            "even granting combined R+2E and Stokes equality leaves one scalar ambiguity",
        ],
        "active_routes": [
            {
                "route": "modified full-tail Evans state",
                "next": "materialize K,V and prove B_Ev R_Xi=d_5cell B_Ev, then test augmented reciprocal Green sewing off divisor",
            },
            {
                "route": "independent conservative cyclic trace",
                "next": "source-identify one of E,W,R independently; with separately authorized combined and Stokes comparisons the remaining two follow algebraically",
            },
        ],
        "closed_or_rejected": {
            "canonical_G4": "closed definitionally under v17; not independent Xi evidence",
            "unchanged_Evans": "rigorously rejected at the first Xi zero in the tested positive horn",
            "scalar_endpoint_repair": "cannot realize normalized conservative transfer defect",
            "exponential_homotopy": "outside rapid bordered domain with diagonal pole",
        },
        "claim_boundary": "Integrated status only. Neither active route is completed and no RH implication is asserted.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
