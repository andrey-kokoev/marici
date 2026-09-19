from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research/nima/results"
OUT = RESULTS / "six-point-bcj-koszul-frontier.json"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def main() -> None:
    exact = load("six-point-bcj-worldsheet-exactness.json")
    quotient = load("six-point-worldsheet-universal-quotient.json")
    pt_boundary = load("mbar06-parke-taylor-boundary-functor.json")
    se_boundary = load("mbar06-scattering-equation-boundary-naturality.json")
    raw_chain = load("six-point-nmhv-bcj-chain-relation.json")
    repair = load("six-point-minimal-bcj-chain-repair.json")

    checks = {
        "fundamental_bcj_generator_is_scattering_equation_exact":
            exact["checks"]["weighted_parke_taylor_sum_equals_minus_scattering_equation"],
        "full_cross_order_kernel_is_rank18_bcj_module":
            quotient["checks"]["bcj_relation_rank_18"]
            and quotient["checks"]["quotient_kernel_is_bcj_rowspace"],
        "all_25_stable_divisors_have_parke_taylor_residue_data":
            pt_boundary["checks"]["mbar06_has_25_stable_divisors"]
            and pt_boundary["checks"]["all_600_ordering_divisor_pairs_checked"],
        "scattering_equations_factorize_on_all_stable_divisors":
            se_boundary["checks"]["all_25_stable_divisors"]
            and se_boundary["checks"]["cluster_equations_factorize"]
            and se_boundary["checks"]["complement_equations_factorize_with_nodal_momentum"],
        "raw_cr_chain_map_is_obstructed":
            raw_chain["status"] == "raw_chain_obstruction"
            and not raw_chain["assertions"]["any_raw_chain_relation"]
            and not raw_chain["assertions"]["any_parke_taylor_dressed_chain_relation"],
        "finite_fixture_defect_extension_is_exact":
            repair["checks"]["all_24_relations_repaired"]
            and repair["checks"]["repaired_H4_zero"],
    }

    out = {
        "schema": "marici.nima.six-point-bcj-koszul-frontier.result.v1",
        "status": "worldsheet_koszul_target_constructed_cr_comparison_open"
        if all(checks.values()) else "failed",
        "checks": checks,
        "constructed_target": {
            "degree_zero": "24-dimensional DDM ordering module modulo the rank-18 BCJ rowspace",
            "degree_one": "scattering-equation ideal generators E_i with Parke-Taylor coefficients",
            "boundary_transport": "factorization on all 25 stable divisors of Mbar_0,6",
            "quotient_dimension": quotient["quotient_dimension"],
        },
        "source_side": {
            "raw_nmhv_chain_relation": "obstructed",
            "finite_fixture_repair": "four defect lifts and four null-homotopies repair all 24 tested relations",
            "repair_is_source_authorized_global_map": False,
        },
        "decision": "The BCJ relation target and its stable-boundary transport are already constructed. The remaining gate is an independently sourced map from the NMHV CR chain complex into this worldsheet/Koszul target; cubic numerator fitting is not required for that gate.",
        "next_acceptance_test": [
            "define the CR source generators and differential without target-fitted coefficients",
            "map each source generator to a Parke-Taylor/Koszul cochain",
            "verify d_target F = F d_CR symbolically",
            "show the four defect lifts are induced by that map rather than adjoined post hoc",
            "verify residue naturality of F on all 25 stable divisors",
        ],
        "claim_boundary": "This integrates existing exact certificates. It does not construct the missing CR-to-worldsheet chain map and does not promote the finite-fixture repair to a source-authorized global cocycle.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
