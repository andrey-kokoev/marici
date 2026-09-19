from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/coherent-resolution-programme-frontier.v2.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    a3 = load("research/benincasa/results/a3_facet_to_bcfw_boundary_comparison.json")
    a3_degree = load("research/benincasa/results/a3_history_to_resolution_comparison.json")
    bcj = load("research/nima/results/six-point-bcj-koszul-frontier.json")
    bcj_factor = load("research/nima/results/six-point-bcj-defect-factorization.json")
    flavor = load("research/flavor/results/wp360_canonical_source_physical16_portal.json")
    g4 = load("research/voevodsky/correction-v17-closes-the-canonical-g4-crossing-and-removes-the-u-g4-defect-route.v1.json")
    g4_shell = load("research/voevodsky/the-combined-reciprocal-linking-shell-row-is-explicit-and-closes-the-strict-packet-residual-identically.v1.json")

    checks = {
        "a3_comparison_audited": a3["passed"] and a3_degree["passed"],
        "a3_has_only_three_candidate_unupdated_boundaries":
            a3["summary"]["candidate_actual_unupdated_history_boundaries"] == 3,
        "a3_nine_facet_map_not_authorized":
            a3["summary"]["fully_authorized_nine_facet_preimages"] == 0,
        "a3_labels_land_in_C2_not_uniquely_C0":
            not a3_degree["unique_C0_map_from_labels"],
        "bcj_worldsheet_target_constructed":
            bcj["status"] == "worldsheet_koszul_target_constructed_cr_comparison_open",
        "bcj_fixed_repair_does_not_factor":
            bcj_factor["status"] == "fixed_cr_defect_repair_does_not_factor_through_worldsheet_bcj_relations",
        "flavor_portal_is_rank_one_nonfaithful":
            flavor["constraint_rank"] == 1
            and flavor["checks"]["physical16_hostile_pair_collides_under_portal"],
        "canonical_g4_crossing_closed":
            g4["status"] == "canonical_crossing_constructed_legacy_defect_route_retracted_independent_xi_criterion_open",
        "canonical_g4_shell_identity_closed":
            g4_shell["strict_packet_identity"]["status"]
            == "constructed inside adopted U_G4:=T_pair_to_border packet",
        "independent_g4_divisor_information_absent":
            g4["logical_effect"]["independent_divisor_information"] == "not supplied",
    }

    out = {
        "schema": "marici.nima.coherent-resolution-programme-frontier.v2",
        "status": "audited_frontier_reclassified" if all(checks.values()) else "failed",
        "checks": checks,
        "frontier": [
            {
                "branch": "A3 weighted physical descent",
                "status": "typed comparison audited; zero of nine weighted facets has a fully authorized BCFW preimage",
                "constructed": "three unupdated composite histories have candidate boundary combinations",
                "next": "construct three untransported simple-root forms, three common-chart B_ii difference forms, and the nine-to-twenty component/residue pushforward",
            },
            {
                "branch": "six-point BCJ",
                "status": "worldsheet/Koszul relation target and all stable-boundary transports constructed",
                "obstruction": "the fixed abstract-simplex CR defect repair violates worldsheet relation dependencies and cannot factor linearly",
                "next": "replace or enlarge the CR carrier before defect projection; do not relabel the four free repair generators",
            },
            {
                "branch": "flavor",
                "status": "rank-one invariant J^2-cQ shell selector constructed but nonfaithful",
                "next": "derive Q, c, and calibration from a common source before attempting a reduced J^2 readout; full physical16 descent remains open",
            },
            {
                "branch": "G4/Evans",
                "status": "canonical crossing, unique return, and strict shell-jet cancellation closed under v17 adoption",
                "reclassification": "the old 0/64 canonical-population description is superseded",
                "next": "construct independent transverse Xi/divisor information or identify independently fixed conservative reciprocal/linking metrics",
            },
        ],
        "supersedes": [
            "research/nima/results/coherent-resolution-programme-frontier.json entries claiming BCJ requires cubic numerators as the only route",
            "research/nima/results/coherent-resolution-programme-frontier.json entry describing canonical G4 as 0/64",
        ],
        "claim_boundary": "Status integration only. Canonical G4 closure is definitional in the adopted v17 packet and supplies no independent Xi criterion. No open physical comparison map is constructed here.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
