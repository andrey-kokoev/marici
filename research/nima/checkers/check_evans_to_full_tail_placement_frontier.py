from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/evans-to-full-tail-placement-frontier.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    observer = load("research/voevodsky/the-evans-to-five-cell-map-should-be-a-linear-observer-of-the-rosenbrock-state-not-a-tensor-coaction.v1.json")
    five = load("research/voevodsky/correction-the-fixed-forcing-vector-is-only-the-bulk-anchor-the-complete-evans-pair-bridge-is-the-pointed-five-cell-fourier-module.v1.json")
    pole = load("research/voevodsky/correction-the-explicit-xi-homotopy-leg-is-not-in-the-rapid-pair-to-border-domain-and-develops-a-diagonal-laplace-pole.v1.json")
    fixture = load("research/voevodsky/fixtures/five_cell_linear_endpoint_tail_representation_target.v1.json")

    components = observer["candidate_components"]
    checks = {
        "correct_domain_is_rosenbrock_state": observer["typing_correction"]["correct_domain"] == "X_st direct-sum C_theta, with state (f_-,f_+,c)",
        "linear_observer_not_copying_map": observer["typing_correction"]["correct_map_kind"].startswith("one linear observer"),
        "bulk_component_declared": "bulk_Phi" in components["bulk"],
        "endpoint_component_declared": "wall/jump trace" in components["endpoint"],
        "two_oriented_tail_components_declared": "K(f_-,f_+)" in components["tail"] and "V(f_-,f_+)" in components["tail"],
        "five_cell_linear_target_nondegenerate": fixture["disposition"]["linear_candidate"].startswith("nondegenerate"),
        "xi_multiplicity_preserved_linearly": "no tau^2" in observer["linearity_and_Xi"]["multiplicity"],
        "single_phi_anchor_insufficient": "cannot by itself" in five["why_Phi_alone_fails"]["consequence"],
        "exponential_homotopy_route_domain_obstructed": pole["status"] == "algebraic_relative_lift_retained_bordered_chain_lift_not_constructed",
        "joint_chain_square_open": observer["status"] == "correct_linear_bridge_type_identified_component_maps_partly_constructed_joint_chain_law_open",
    }

    out = {
        "schema": "marici.nima.evans-to-full-tail-placement-frontier.v1",
        "status": "linear_observer_components_identified_joint_chain_square_open" if all(checks.values()) else "failed",
        "checks": checks,
        "candidate_map": "B_Ev(f_-,f_+,c)=(c bulk_Phi, H_partial tau_boundary(f_-,f_+), K(f_-,f_+), V(f_-,f_+))",
        "constructed_strength": [
            "correct source and target types",
            "linear bulk and endpoint observations",
            "two oriented tail-coordinate slots",
            "multiplicity-preserving Evans seam readout",
            "nondegenerate order-four five-cell target representation",
        ],
        "missing_equalities": [
            "identify analytic stable-history tail observers with coefficient cells K and V on one closed domain",
            "prove B_Ev R_Xi(z)=d_5cell B_Ev with the seam mismatch retained as transverse output",
            "prove graph-norm continuity and compatible source normalization for the assembled direct sum",
            "only then compare the augmented full-tail Green identity",
        ],
        "rejected_shortcuts": [
            "Phi tensor history alone omits wall, odd endpoint, and oriented tail columns",
            "the explicit exponential homotopy leaves the rapid bordered domain and has a diagonal Laplace pole",
            "a diagonal copying/coaction is unnecessary and would distort the linear source type",
        ],
        "next_executable_packet": "Materialize K and V as operators on X_st with their target-basis coordinate formulas and the five-cell differential. The first test is the symbolic residual B_Ev R_Xi-d_5cell B_Ev before Xi specialization.",
        "claim_boundary": "The placement map is specified componentwise but is not yet a chain map. This result does not infer state membership from the endpoint observer alone.",
        "rh_implication": False,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
