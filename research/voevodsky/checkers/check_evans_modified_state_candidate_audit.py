from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/voevodsky/results/evans-modified-state-candidate-audit.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    unchanged = load("research/voevodsky/results/first-xi-zero-unchanged-evans-adjoint-hilbert-residual.interval.v1.json")
    abstract = load("research/voevodsky/a-one-way-arithmetic-feature-channel-can-repair-the-negative-theta-radiation-kernel-without-moving-the-xi-evans-divisor.v1.json")
    causal = load("research/voevodsky/the-causal-one-sided-theta-transfer-gives-an-exact-positive-kernel-repair-but-confinement-still-requires-a-green-balance-identity.v1.json")
    causal_no_go = load("research/voevodsky/correction-the-scalar-causal-kernel-repair-cannot-by-itself-be-a-normalized-conservative-transfer-defect.v1.json")
    exponential = load("research/voevodsky/correction-the-explicit-xi-homotopy-leg-is-not-in-the-rapid-pair-to-border-domain-and-develops-a-diagonal-laplace-pole.v1.json")
    tail = load("research/voevodsky/the-mixed-theta-forcing-reservoir-has-an-exact-source-derived-sum-difference-gram-factorization.v1.json")

    candidates = [
        {
            "name": "abstract one-way arithmetic feature",
            "sourced_construction": False,
            "unchanged_xi_divisor": True,
            "typed_target_domain": False,
            "membership_or_green_identity": False,
            "reason": "Triangular determinant preservation is algebraic, but E and h are requirements rather than constructed source objects; finite-packet positivity and membership are targets.",
        },
        {
            "name": "scalar causal theta feature h=m",
            "sourced_construction": causal["source_feature"]["not_fitted"].startswith("the feature is fixed"),
            "unchanged_xi_divisor": "divisor remains Xi" in causal["triangular_realization"]["determinant"],
            "typed_target_domain": True,
            "membership_or_green_identity": False,
            "reason": causal_no_go["scalar_schur_no_go"]["conclusion"],
        },
        {
            "name": "explicit exponential Xi homotopy leg",
            "sourced_construction": True,
            "unchanged_xi_divisor": True,
            "typed_target_domain": False,
            "membership_or_green_identity": False,
            "reason": exponential["domain_obstruction"]["consequence"],
        },
        {
            "name": "full tail-state sum/difference passive node",
            "sourced_construction": tail["status"] == "one_sided_polarized_conservative_factorization_closed",
            "unchanged_xi_divisor": False,
            "typed_target_domain": "bounded on the declared tail graph rigging" in tail["sum_difference_ports"]["properties"],
            "membership_or_green_identity": False,
            "one_sided_green_identity": True,
            "reason": tail["doubled_system_gate"]["remaining"],
        },
    ]
    for candidate in candidates:
        candidate["passes_all_four"] = all(
            candidate[key]
            for key in (
                "sourced_construction",
                "unchanged_xi_divisor",
                "typed_target_domain",
                "membership_or_green_identity",
            )
        )

    checks = {
        "unchanged_state_rigorously_rejected": unchanged["status"] == "certified_strictly_negative",
        "abstract_feature_is_only_architecture": abstract["source_authority_gate"]["required"].startswith("derive h"),
        "causal_scalar_positive_repair_retained": causal_no_go["positive_fact_retained"].startswith("K_aug"),
        "causal_scalar_conservative_identity_rejected": causal_no_go["status"] == "positive_repair_retained_conservative_realization_claim_rejected",
        "exponential_leg_outside_rapid_domain": exponential["status"] == "algebraic_relative_lift_retained_bordered_chain_lift_not_constructed",
        "full_tail_one_sided_green_identity_closed": tail["status"] == "one_sided_polarized_conservative_factorization_closed",
        "full_tail_doubled_sewing_open": "remaining" in tail["doubled_system_gate"],
        "no_candidate_passes_acceptance_contract": not any(c["passes_all_four"] for c in candidates),
    }
    out = {
        "schema": "marici.voevodsky.evans-modified-state-candidate-audit.v1",
        "status": "unchanged_state_rejected_no_existing_modified_candidate_admissible" if all(checks.values()) else "failed",
        "acceptance_contract": [
            "source-derived construction fixed before inspecting the hostile residual",
            "Xi divisor preserved with multiplicity",
            "state belongs to the declared pair/bordered or conservative target domain",
            "a polarized Green/membership identity for that same lifted state",
        ],
        "checks": checks,
        "candidates": candidates,
        "next_executable_gate": "The full tail-state one-sided Green factorization is now closed. Write the reciprocal sewing action on both incoming sum ports and both outgoing endpoint-plus-difference ports, then verify equality of their complete Gram operators with wall and arithmetic labels before Xi specialization.",
        "claim_boundary": "This rejects three materialized repair candidates under the four-part acceptance contract. It does not prove that no modified sourced Evans state exists.",
        "rh_implication": False,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
