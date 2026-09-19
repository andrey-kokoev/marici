from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/coherent-resolution-programme-frontier.v4.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    v3 = load("research/nima/results/coherent-resolution-programme-frontier.v3.json")
    a3 = load("research/benincasa/results/a3_candidate_bcfw_supports.json")
    a3_full = load("research/benincasa/results/a3_facet_to_bcfw_boundary_comparison.json")
    bcj_enlarge = load("research/nima/results/six-point-bcj-minimal-source-enlargement.json")
    bcj_boundary = load("research/nima/results/six-point-bcj-all-labelled-boundary-residues.json")
    flavor = load("research/nima/results/a3-to-flavor-reduced-portal-typing.json")
    evans_cross = load("research/voevodsky/results/first-zero-evans-cross-certificate.json")
    trace = load("research/nima/results/conservative-trace-identifiability.json")

    checks = {
        "v3_passed": v3["status"] == "post_interval_evans_and_trace_identifiability_frontier",
        "a3_three_composite_supports_fixed": a3["status"] == "three_composite_facet_supports_canonical_normalization_still_open",
        "a3_full_nine_map_absent": a3_full["summary"]["fully_authorized_nine_facet_preimages"] == 0,
        "bcj_minimum_enlargement_four": bcj_enlarge["ranks"]["new_source_directions"] == 4,
        "bcj_cyclic_labelled_boundary_candidate_falsified": bcj_boundary["status"] == "cyclically_labelled_pair_collision_module_still_does_not_factor_cr_defects",
        "flavor_reduced_target_typed_source_arrow_absent": flavor["status"] == "reduced_J2_portal_target_exists_but_CR_source_arrow_untyped",
        "evans_two_interval_certificates": evans_cross["status"] == "two_interval_strategies_certify_strict_negativity",
        "conservative_trace_one_parameter_ambiguity": trace["status"] == "combined_shell_and_stokes_data_leave_one_coordinate_ambiguity",
    }

    out = {
        "schema": "marici.nima.coherent-resolution-programme-frontier.v4",
        "status": "twenty_iteration_prior_research_audit_complete" if all(checks.values()) else "failed",
        "checks": checks,
        "branch_dispositions": [
            {
                "branch": "A3 weighted descent",
                "constructed": "three composite-root histories have canonical independent BCFW divisor supports of rank three",
                "blocked": "form coefficients and normalization; three untransported simple-root forms; three common-chart B_ii difference forms",
                "next_executable": "construct one untransported simple-root canonical form on the transported history's oriented chart and compare both residues coefficientwise",
            },
            {
                "branch": "six-point BCJ",
                "constructed": "rank-18 worldsheet quotient, scattering-equation exactness, all stable-boundary naturality, and minimal four-direction enlargement theorem",
                "blocked": "current CR defects violate dependencies even after retaining pair-collision normals and oriented cyclic lower-point PT labels",
                "next_executable": "either change the CR assignment or retain full stable-divisor flags/twisted orientation lines and rerun the dependency-kernel test",
            },
            {
                "branch": "flavor",
                "constructed": "nonfaithful reduced J^2 portal through WP359 rho=Q/M2",
                "blocked": "no CR-to-WP359 effective-action map and no authority fixing alpha",
                "next_executable": "do not identify the A3 rational scalar with dimensional Q; require a source packet supplying Z,q,M2",
            },
            {
                "branch": "Evans/G4",
                "constructed": "canonical G4 closure; one-sided full-tail Green factorization; pair-to-Euler response; two independent interval rejections of unchanged Evans",
                "blocked": "modified-state chain placement and independent conservative trace equality",
                "next_executable": "identify one independent E/W/R coordinate or materialize K,V and test the Evans-to-five-cell chain square",
            },
        ],
        "strongest_new_negative_results": [
            "unchanged Evans membership is rigorously false in the tested horn",
            "the fixed CR repair cannot factor through worldsheet BCJ relations",
            "a minimal repair needs four preprojection directions",
            "collision normals, even with cyclic lower-PT labels, still violate a CR defect dependency",
            "combined conservative shell and Stokes data leave one scalar coordinate ambiguity",
            "the A3 scalar cannot be substituted for WP359 Q",
        ],
        "claim_boundary": "This closes the requested prior-research audit and finite falsifier pass, not the scientific programme. Every surviving branch has a nonredundant construction listed above.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
