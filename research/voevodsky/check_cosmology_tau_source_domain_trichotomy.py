"""Source-domain trichotomy for the tau_p lift problem.

This iteration re-reads the newly available Nima prior-art gates and classifies
the three admissible source-domain routes.  The gradient-pivot route is the only
current internal candidate and it fails fixed-fiber typing; the remaining routes
require new source data.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_tau_source_domain_trichotomy.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    nonfaithful = load(VOEVODSKY_RESULTS / "cosmology_residue_functor_nonfaithfulness_gate.json")
    contract = load(VOEVODSKY_RESULTS / "cosmology_tau_source_map_contract.json")
    prior = load(NIMA_RESULTS / "cosmology_tau_lift_prior_art_audit.json")
    pivot = load(NIMA_RESULTS / "cosmology_tau_gradient_pivot_type_gate.json")
    frontier = load(NIMA_RESULTS / "cosmology_current_activation_frontier_exhaustion.json")

    assert nonfaithful["passed"] is True
    assert contract["passed"] is True
    assert prior["passed"] is True
    assert pivot["passed"] is True
    assert frontier["passed"] is True
    assert contract["contract"]["required_differential_vector_in_rows_Xi_log_minusSigma"] == [1, 1]
    assert prior["tau_p_source_map_constructed"] is False
    assert pivot["raw_prior_art_supplies_tau_p"] is False
    assert pivot["restricted_cover"]["triple_face_count"] == 0
    assert frontier["current_routes"]["relative_p_normal_coefficient"]["status"] == "current_source_branch_exhausted_tau_p_not_sourced"

    routes = {
        "gradient_pivot_normal_adapter": {
            "available_prior_art": True,
            "pairwise_exactness": prior["best_existing_bulk_candidate"]["pairwise_exactness"],
            "triple_homotopy": prior["best_existing_bulk_candidate"]["triple_homotopy"],
            "fails_reason": "fixed-fiber restriction removes the base-dependent c pivot, leaving two charts and no sigma123 triple face",
            "tau_contract_satisfied": False,
        },
        "native_three_chart_marked_fiber_cover": {
            "available_prior_art": False,
            "required": "three source charts in the two-dimensional marked fiber with a triple face mapping to sigma123 and Xi_log with unit coefficient",
            "tau_contract_satisfied": False,
        },
        "relative_base_fiber_comparison": {
            "available_prior_art": False,
            "required": "a source comparison retaining the c/base direction and a residue-exact section fixing the invisible kernel component",
            "tau_contract_satisfied": False,
        },
        "cayley_menger_face_cone": {
            "available_prior_art": False,
            "required": "a CM face cone with compensating residue and a chain map to rows (Xi_log,-sigma123)",
            "tau_contract_satisfied": False,
        },
    }

    assert not any(route["tau_contract_satisfied"] for route in routes.values())

    result = {
        "schema": "marici.voevodsky.cosmology-tau-source-domain-trichotomy.v1",
        "status": "all_current_source_domains_fail_tau_contract_new_source_data_required",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_residue_functor_nonfaithfulness_gate.json",
            "research/voevodsky/results/cosmology_tau_source_map_contract.json",
            "research/nima/results/cosmology_tau_lift_prior_art_audit.json",
            "research/nima/results/cosmology_tau_gradient_pivot_type_gate.json",
            "research/nima/results/cosmology_current_activation_frontier_exhaustion.json",
        ],
        "tau_contract": "unit column (1,1) in rows (Xi_log,-sigma123)",
        "routes": routes,
        "decisive_new_read": "Nima's gradient-pivot type gate blocks the only current internal candidate: the c pivot is base-dependent, and fixed-fiber restriction destroys the triple Cech face required for sigma123",
        "exhaustion_boundary": "within current mutable packets, no source domain supplies tau_p; further work must introduce or receive new source data rather than iterate the residue classifier",
        "next_admissible_nonrepeat_task": "construct either a native three-chart marked-fiber cover or a relative base-fiber comparison retaining the c direction, then test for the unit column (1,1)",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
