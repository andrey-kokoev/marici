"""Post-candidate authority status for triple-incidence cosmology.

A candidate contour-authority contract now exists.  This checker verifies that
its existence changes the planning surface but not the source-authority status:
it is admitted as a research program, remains inconclusive, and does not assign
a physical period.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_post_candidate_authority_status.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    exhaustion = load("cosmology_current_activation_frontier_exhaustion.json")
    candidate = load("cosmology_contour_authority_candidate.json")
    continuation = load("cosmology_analytic_continuation_authority_gate.json")
    monodromy = load("cosmology_triple_incidence_scaled_monodromy.json")
    p_normal = load("cosmology_relative_p_normal_bockstein_candidate.json")

    assert exhaustion["currently_assignable_physical_period"] is False
    assert exhaustion["currently_open_internal_route"] is False
    assert exhaustion["open_internal_route"] is None
    assert candidate["candidate_admitted_as_research_program"] is True
    assert candidate["certifies_source_authority"] is False
    assert candidate["activates_physical_period"] is False
    assert candidate["decision"] == "inconclusive_pending_source_derivation"
    assert continuation["source_authorized_local_boundary_germ_present"] is True
    assert continuation["source_authorized_contour_present"] is False
    assert continuation["continued_scalar_period_assigned"] is False
    assert monodromy["local_picard_lefschetz_variation_rank"] == 0
    assert monodromy["primitive_mu2_odd_thimble_generated_by_p_loop"] is False

    packet = {
        "schema": "marici.cosmology-post-candidate-authority-status.v1",
        "target": "triple-incidence mu2-odd logarithmic nearby line",
        "candidate_contract_exists": True,
        "candidate_contract_status": candidate["candidate_status"],
        "source_authorized_local_boundary_germ": True,
        "candidate_certifies_global_contour_authority": False,
        "candidate_activates_physical_period": False,
        "currently_assignable_physical_period": False,
        "current_internal_routes_exhausted": True,
        "current_internal_route": exhaustion["open_internal_route"],
        "relative_p_normal_bockstein_defined": p_normal["bockstein_defined"],
        "relative_p_normal_first_failed_gate": p_normal["first_failed_gate"],
        "local_picard_lefschetz_variation_rank": 0,
        "missing_authority_certificates": [
            "independently_sourced_global_contour_with_remote_singularity_coupling",
            "source-derived relative carrier and surviving p-normal coefficient class",
            "source-normalized mu2-odd physical test chain",
            "continued_physical_period_covector"
        ],
        "promotion_rule": (
            "the local p-i0 germ has source authority, but promotion requires all "
            "listed transport/pairing certificates and a rerun before any period assignment"
        ),
        "next_gate": "supply a source-level p-normal factorization identity or a sourced five-mark to principal-three-wall comparison morphism",
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
