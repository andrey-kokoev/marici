"""Current exhaustion gate for the triple-incidence activation routes.

This checker only summarizes the presently recorded routes.  It does not claim
that no future source can reopen cosmology; it records that every currently
available activation route for the triple-incidence nearby line is either
closed or awaiting new external source authority.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_current_activation_frontier_exhaustion.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    activation = load("cosmology_triple_incidence_activation_obstruction.json")
    all_soft = load("cosmology_triple_incidence_all_soft_separation.json")
    bridge = load("cosmology_z3_to_mu2_bridge_no_go.json")
    continuation = load("cosmology_analytic_continuation_authority_gate.json")
    contour_candidate = load("cosmology_contour_authority_candidate.json")
    corner_transport = load("cosmology_triple_incidence_boundary_corner_transport.json")
    scaled_monodromy = load("cosmology_triple_incidence_scaled_monodromy.json")
    p_normal = load("cosmology_relative_p_normal_bockstein_candidate.json")
    pivot_type = load("cosmology_tau_gradient_pivot_type_gate.json")
    rank26_prior = load("cosmology_p_normal_rank26_relation_bockstein_prior_art.json")
    rank26_census = load("cosmology_p_normal_rank26_rees_census_summary.json")
    rank26_quotient = load("cosmology_p_normal_rank26_quotient_stability.json")
    rank26_syzygy = load("cosmology_p_normal_rank26_syzygy_bockstein_summary.json")
    c_kernel = load("cosmology_relative_c_kernel_section_no_go.json")
    half_twist = load("cosmology_p_normal_rank26_half_twist_gate.json")

    routes = {
        "literal_generic_positive_chain": {
            "status": "closed",
            "reason": "strict positive chamber does not meet p=0",
            "evidence": not activation[
                "literal_generic_physical_period_supported_on_nearby_line"
            ],
        },
        "all_soft_z3_activation": {
            "status": "closed",
            "reason": "all-soft Z/3 character is separated from mu2-odd nearby line",
            "evidence": all_soft["order_and_descent"][
                "canonical_hom_from_order3_to_mu2_supplied"
            ] is False,
        },
        "torsion_respecting_z3_to_mu2_bridge": {
            "status": "closed",
            "reason": "Hom(Z/3,Z/2) has no nonzero homomorphism",
            "evidence": bridge["nonzero_homomorphisms"] == 0,
        },
        "analytic_continuation_contour": {
            "status": "local_p_i0_route_closed_by_identity_monodromy",
            "reason": "the punctured boundary-corner family is scaling-trivial, its local variation has rank zero, and the p-loop generates no mu2-odd thimble",
            "evidence": continuation["analytic_continuation_required"]
            and continuation["source_authorized_local_boundary_germ_present"]
            and not continuation["source_authorized_contour_present"]
            and contour_candidate["candidate_admitted_as_research_program"]
            and contour_candidate["source_authorized_local_boundary_germ"]
            and corner_transport["transport_type"] == "relative marked-wall boundary-corner collision"
            and scaled_monodromy["local_picard_lefschetz_variation_rank"] == 0
            and not scaled_monodromy["primitive_mu2_odd_thimble_generated_by_p_loop"]
            and not contour_candidate["activates_physical_period"],
        },
        "relative_p_normal_coefficient": {
            "status": "physical_half_twist_images_through_degree16_are_p_tangent_no_finite_cutoff_promotion",
            "reason": "at gamma=-1/2 the resolved image ranks are 8, 7, 11, 14, and 18 through degrees 8 to 16; every image is exactly p-tangent over two primes, while further finite cutoffs cannot prove an unbounded factorization",
            "evidence": p_normal["carrier_gates"]["auxiliary_K_p_constructed"]
            and p_normal["carrier_gates"]["minimal_relative_carrier_B_cos_constructed"]
            and not p_normal["carrier_gates"]["Xi_survival_rank_test"]
            and not p_normal["carrier_gates"]["total_Cech_de_Rham_chain_map_constructed"]
            and not p_normal["bockstein_defined"]
            and not pivot_type["raw_prior_art_supplies_tau_p"]
            and pivot_type["restricted_cover"]["triple_face_count"] == 0
            and rank26_prior["currently_open_internal_test"]
            and rank26_census["support_excess"] == 13
            and rank26_census["elementary_length_census"]["length_1"] == 7
            and rank26_census["same_census_both_normals_both_primes"]
            and not rank26_census["bockstein_image_vectors_computed"]
            and rank26_quotient["all_unit_normal_extensions_after_tangent"] == 0
            and rank26_quotient["ambient_degrees"] == [8, 10, 12, 14]
            and not rank26_quotient["explicit_length_one_generators_extracted"]
            and rank26_syzygy["resolved_syzygy_image_rank_by_degree"] == {"8": 7, "10": 7, "12": 11, "14": 15}
            and rank26_syzygy["normal_image_equals_tangent_image"]
            and rank26_syzygy["p_normal_image_mod_tangent_rank"] == 0
            and not c_kernel["factorization_holds"]
            and not c_kernel["source_derived_kernel_section_constructed"]
            and half_twist["generic_gamma5_prior_results_are_not_physical_half_twist"]
            and half_twist["all_tested_half_twist_images_equal_p_tangent"]
            and all(rank == 0 for rank in half_twist["p_normal_image_mod_tangent_ranks"].values()),
        },
    }
    assert all(route["evidence"] for route in routes.values())
    assert routes["literal_generic_positive_chain"]["status"] == "closed"
    assert routes["all_soft_z3_activation"]["status"] == "closed"
    assert routes["torsion_respecting_z3_to_mu2_bridge"]["status"] == "closed"
    assert routes["analytic_continuation_contour"]["status"].startswith("local_p_i0_route_closed")
    assert routes["relative_p_normal_coefficient"]["status"].endswith("promotion")

    packet = {
        "schema": "marici.cosmology-current-activation-frontier-exhaustion.v1",
        "target": "triple-incidence mu2-odd logarithmic nearby line",
        "current_routes": routes,
        "currently_assignable_physical_period": False,
        "currently_open_internal_route": False,
        "open_internal_route": None,
        "contour_authority_candidate_exists": True,
        "source_authorized_local_boundary_germ_exists": True,
        "candidate_certifies_global_contour_authority": False,
        "candidate_activates_physical_period": False,
        "requires_new_external_source_authority_for_next_internal_test": True,
        "external_source_authority_may_still_be_required_for_physical_activation": True,
        "not_a_global_no_go": True,
        "conclusion": (
            "the source-authorized local p-i0 germ has identity local monodromy and generates no odd thimble; "
            "generic-twist rank-26 evidence was not physical; the corrected half-twist images through degree sixteen are all p-tangent; "
            "further finite cutoff growth is nonpromoting without a source-level identity and no physical period exists"
        ),
        "next_admissible_inputs": [
            "independently sourced global contour coupling to remote singularities",
            "source-derived bulk-face augmentation beyond the exact minimal marked-wall Cech carrier",
            "relative lift dH_p=p*Xi_p with two-prime survival certificate",
            "physical chain coupling outside the mu2-odd nearby line",
        ],
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
