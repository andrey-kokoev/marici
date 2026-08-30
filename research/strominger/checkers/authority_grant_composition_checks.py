#!/usr/bin/env python3
"""Exact positive and hostile checks for partial authority composition."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / "research" / "strominger"
sys.path.insert(0, str(S))

from authority_grant_composition import compile_packet  # noqa: E402

CONTRACT = S / "contracts" / "authority-grant-composition.v1.json"
HOSTILES = S / "contracts" / "authority-grant-composition-hostile-fixtures.v1.json"
OUT = S / "results" / "authority_grant_composition.json"


def by_id(packet, collection, item_id):
    items = packet
    for part in collection.split("."):
        items = items[part]
    return next(item for item in items if item["id"] == item_id)


def mutate(packet, mutations):
    candidate = copy.deepcopy(packet)
    for mutation in mutations:
        by_id(candidate, mutation["collection"], mutation["id"])[mutation["field"]] = mutation["value"]
    return candidate


def codes(compiled):
    return {item["code"] for item in compiled["errors"]}


def main():
    packet = json.loads(CONTRACT.read_text(encoding="ascii"))
    hostile_spec = json.loads(HOSTILES.read_text(encoding="ascii"))
    compiled = compile_packet(packet)

    hostile_results = {}
    for fixture in hostile_spec["fixtures"]:
        result = compile_packet(mutate(packet, fixture["mutations"]))
        expected = fixture["expected_code"]
        hostile_results[fixture["id"]] = {
            "description": fixture["description"],
            "valid": result["valid"],
            "expected_code": expected,
            "error_codes": sorted(codes(result)),
            "passed": not result["valid"] and expected in codes(result),
        }

    grants = {item["id"]: item for item in packet["authority_grants"]}
    compositions = {item["id"]: item for item in packet["compositions"]}
    cases = {item["id"]: item for item in packet["application_cases"]}
    transformations = {item["id"]: item for item in packet["transformations"]}
    representation_tests = {item["id"]: item for item in packet["representation_change_tests"]}
    presentation_cells = {item["id"]: item for item in packet["presentation_coherence_cells"]}
    presentation_atlases = {item["id"]: item for item in packet["presentation_atlas_coherence"]}
    descent_objects = {item["id"]: item for item in packet["authority_descent_objects"]}
    refinements = {item["id"]: item for item in packet["presentation_refinement_coherence"]}
    deletions = {item["id"]: item for item in packet["presentation_deletion_tests"]}
    provenance_nodes = {item["id"]: item for item in packet["source_provenance"]["nodes"]}
    provenance_edges = packet["source_provenance"]["edges"]
    interventions = {item["id"]: item for item in packet["source_intervention_tests"]}
    mechanism_audits = {item["id"]: item for item in packet["mechanism_identification_audits"]}
    rival_audits = {item["id"]: item for item in packet["rival_extension_audits"]}
    rival_admissions = {item["id"]: item for item in packet["rival_admissions"]}
    rival_reviews = {item["id"]: item for item in packet["rival_admission_reviews"]}
    identity_audits = {item["id"]: item for item in packet["proposer_identity_invariance_audits"]}
    review_roots = {item["id"]: item for item in packet["review_authority_root_certifications"]}
    root_audits = {item["id"]: item for item in packet["review_root_independence_audits"]}
    temporal_audits = {item["id"]: item for item in packet["temporal_review_authority_audits"]}
    temporal_atlases = {item["id"]: item for item in packet["temporal_replay_atlas_audits"]}
    temporal_cocycles = {item["id"]: item for item in packet["temporal_governance_cocycle_audits"]}
    stack_certificates = {item["id"]: item for item in packet["finite_authority_stack_certificates"]}
    capability_executions = {item["id"]: item for item in packet["authority_capability_execution_audits"]}
    distributed_audits = {item["id"]: item for item in packet["distributed_capability_consumption_audits"]}
    trilemma_audits = {item["id"]: item for item in packet["distributed_linearity_trilemma_audits"]}
    constructor_networks = {item["id"]: item for item in packet["linearization_constructor_networks"]}
    fault_audits = {item["id"]: item for item in packet["fault_parametric_quorum_audits"]}
    hypergraph_audits = {item["id"]: item for item in packet["fault_hypergraph_quorum_audits"]}
    discovery_audits = {item["id"]: item for item in packet["common_cause_discovery_audits"]}
    probe_grammar_audits = {item["id"]: item for item in packet["probe_grammar_authority_audits"]}
    probe_grammar_boundaries = {item["id"]: item for item in packet["probe_grammar_boundary_audits"]}
    probe_grammar_epochs = {item["id"]: item for item in packet["probe_grammar_epoch_audits"]}
    distributed_manifest_audits = {item["id"]: item for item in packet["distributed_manifest_epoch_audits"]}
    reconfiguration_audits = {item["id"]: item for item in packet["configuration_reconfiguration_audits"]}

    certificate_deletion_results = {}
    generator_collections = (
        "rival_admissions", "rival_admission_reviews", "review_authority_root_certifications",
        "temporal_replay_atlas_audits", "temporal_governance_cocycle_audits",
    )
    certificate = stack_certificates["current_delta_challenge_standing_certificate"]
    witnesses = {item["generator_id"]: item for item in certificate["minimality_witnesses"]}
    for generator in certificate["generators"]:
        candidate = copy.deepcopy(packet)
        removed = False
        for collection in generator_collections:
            retained = [item for item in candidate[collection] if item["id"] != generator["object_ref"]]
            if len(retained) != len(candidate[collection]):
                candidate[collection] = retained
                removed = True
                break
        deletion_result = compile_packet(candidate)
        expected = witnesses[generator["id"]]["expected_failure_code"]
        deletion_codes = sorted(codes(deletion_result))
        certificate_deletion_results[generator["id"]] = {
            "object_ref": generator["object_ref"],
            "removed": removed,
            "expected_failure_code": expected,
            "error_codes": deletion_codes,
            "passed": removed and not deletion_result["valid"] and expected in deletion_codes,
        }

    left_result = grants[compositions["c_AC_CD"]["result"]]
    right_result = grants[compositions["c_AB_BD"]["result"]]
    result_signature = lambda grant: (
        grant["source_object"], grant["target_operation"], grant["target_object"],
        grant["authority_kind"], grant["evidence_domain"], grant["variance"],
    )

    gates = {
        "standalone_contract_compiles": compiled["valid"],
        "identity_laws_declared_twice": len(packet["identity_laws"]) == 2,
        "associativity_holds_on_typed_domain": result_signature(left_result) == result_signature(right_result)
            and packet["associativity_cells"][0]["coherence_defect"] == 0,
        "composition_preserves_authority_kind": all(
            len({grants[c["left"]]["authority_kind"], grants[c["right"]]["authority_kind"], grants[c["result"]]["authority_kind"]}) == 1
            for c in packet["compositions"]
        ),
        "transport_requires_authority_preservation": transformations["chart_transport"]["preserves_authority"],
        "theta_requires_explicit_seam_cell": cases["grothendieck_folded_theta"]["classification"] == "coherence_cell_required"
            and cases["grothendieck_folded_theta"]["explicit_coherence_cell"] == "moving-endpoint seam current plus reciprocal reflection",
        "theta_composite_remains_readout": cases["grothendieck_folded_theta"]["authority_result"] == "readout only",
        "kitaev_has_no_composable_physical_authority": cases["kitaev_logical_to_five_rail"]["classification"] == "no_composable_authority_map"
            and cases["kitaev_logical_to_five_rail"]["composition"] is None,
        "kitaev_rail_base_change_preserves_evidence_not_authority": transformations["rail_base_change"]["preserves_evidence"]
            and not transformations["rail_base_change"]["preserves_authority"],
        "removing_B_preserves_process_only_with_direct_source_grant":
            representation_tests["remove_B_direct_source_route"]["verdict"] == "process_explained_strictly"
            and representation_tests["remove_B_direct_source_route"]["direct_grant"] == "g_AC_direct",
        "changing_B_requires_source_derived_natural_coherence":
            representation_tests["replace_B_by_Bprime"]["verdict"] == "process_explained_coherently"
            and presentation_cells[representation_tests["replace_B_by_Bprime"]["coherence_cell_id"]]["source_derived"]
            and presentation_cells[representation_tests["replace_B_by_Bprime"]["coherence_cell_id"]]["naturality_defect"] == 0,
        "presentation_cells_are_invertible_and_kind_preserving": all(
            cell["invertible"] and cell["preserves_authority_kind"]
            for cell in packet["presentation_coherence_cells"]
        ),
        "presentation_atlas_has_zero_holonomy":
            presentation_atlases["atlas_B_Bprime_Bdoubleprime"]["holonomy_defect"] == 0
            and len(presentation_atlases["atlas_B_Bprime_Bdoubleprime"]["paths"]) == 2,
        "flat_descent_is_effective_and_unique":
            descent_objects["descent_process_AC"]["effective"]
            and descent_objects["descent_process_AC"]["reconstruction_defect"] == 0
            and descent_objects["descent_process_AC"]["ambiguity_kernel_rank"] == 0,
        "descent_stabilizer_is_source_authorized":
            set(descent_objects["descent_process_AC"]["stabilizer"]).issubset(
                descent_objects["descent_process_AC"]["source_authorized_stabilizer"]
            ),
        "source_authorized_gauge_descends_stackily":
            descent_objects["descent_process_AC_stacky"]["ambiguity_kernel_rank"] == 1
            and descent_objects["descent_process_AC_stacky"]["stabilizer_quotient_declared"]
            and descent_objects["descent_process_AC_stacky"]["quotient_ambiguity_rank"] == 0
            and set(descent_objects["descent_process_AC_stacky"]["stabilizer"]).issubset(
                descent_objects["descent_process_AC_stacky"]["source_authorized_stabilizer"]
            ),
        "explanatory_provenance_is_forward_and_source_rooted":
            provenance_nodes["prov_source"]["role"] == "source_constructor"
            and provenance_nodes["prov_readout"]["role"] == "readout"
            and all(
                provenance_nodes[edge["source"]]["stage"] < provenance_nodes[edge["target"]]["stage"]
                and edge["source_derived"]
                for edge in provenance_edges
            ),
        "coherence_is_prior_target_independent_and_recomputable": all(
            cell["derived_before_target"] and cell["target_independent"] and cell["counterfactual_recomputable"]
            for cell in packet["presentation_coherence_cells"]
        ),
        "source_intervention_regenerates_coherence":
            "prov_coherence" in interventions["intervene_on_source_constructor"]["observed_affected_nodes"]
            and interventions["intervene_on_source_constructor"]["fresh_recomputation"],
        "target_intervention_cannot_rewrite_upstream_authority":
            interventions["intervene_on_target_readout"]["observed_affected_nodes"] == ["prov_readout"],
        "source_deletion_revokes_authority_not_cached_output":
            interventions["delete_source_constructor"]["cached_output_may_survive"]
            and not interventions["delete_source_constructor"]["authority_survives"],
        "finite_interventions_identify_declared_mechanisms":
            mechanism_audits["finite_three_mechanism_identification"]["observation_matrix"]
            == [[1, 0, 1], [0, 1, 1], [1, 1, 0]]
            and mechanism_audits["finite_three_mechanism_identification"]["source_authorized_gauge_dimension"] == 0,
        "mechanism_identification_is_explicitly_bounded": all(
            audit["bounded_claim_scope"] and audit["no_universal_extrapolation"]
            for audit in packet["mechanism_identification_audits"]
        ),
        "stacky_mechanism_kernel_equals_authorized_gauge":
            mechanism_audits["finite_stacky_mechanism_identification"]["source_authorized_gauge_dimension"] == 1
            and len(mechanism_audits["finite_stacky_mechanism_identification"]["candidate_mechanisms"]) == 3
            and len(mechanism_audits["finite_stacky_mechanism_identification"]["intervention_ports"]) == 2,
        "new_rival_suspends_identification_authority":
            rival_audits["new_rival_opens_identification_challenge"]["status"] == "challenge_open"
            and not rival_audits["new_rival_opens_identification_challenge"]["identification_authority_retained"],
        "source_derived_probe_revalidates_extended_family":
            rival_audits["new_source_probe_revalidates_extended_family"]["status"] == "revalidated"
            and bool(rival_audits["new_source_probe_revalidates_extended_family"]["new_discriminator_source_derived"])
            and rival_audits["new_source_probe_revalidates_extended_family"]["identification_authority_retained"],
        "rival_protocol_remains_open_world": all(
            not audit["claims_closed_under_all_future_rivals"] for audit in packet["rival_extension_audits"]
        ),
        "new_rival_has_independent_constructor_authority":
            rival_admissions["admit_mechanism_delta"]["status"] == "admitted"
            and rival_admissions["admit_mechanism_delta"]["independent_of_incumbent_fit"]
            and rival_admissions["admit_mechanism_delta"]["predicts_all_existing_ports"]
            and bool(rival_admissions["admit_mechanism_delta"]["non_gauge_witness"]),
        "gauge_copy_is_not_a_distinct_rival":
            rival_admissions["reject_gauge_copy_as_rival"]["status"] == "rejected"
            and rival_admissions["reject_gauge_copy_as_rival"]["non_gauge_witness"] is None,
        "incomplete_speculation_cannot_open_challenge":
            rival_admissions["pending_port_incomplete_speculation"]["status"] == "pending"
            and not rival_admissions["pending_port_incomplete_speculation"]["predicts_all_existing_ports"],
        "rival_admission_has_separated_governance_roles": all(
            review["incumbent"] not in review["reviewers"]
            and review["proposer"] not in review["reviewers"]
            and not set(review["reviewers"]) & set(review["appeal_reviewers"])
            for review in packet["rival_admission_reviews"]
        ),
        "rival_reviewers_have_independent_authority_roots": all(
            len(review["reviewers"]) == len(set(review["reviewer_authority_roots"]))
            for review in packet["rival_admission_reviews"]
        ),
        "rival_review_is_content_addressed_and_precommitted": all(
            review["immutable_evidence_packet_sha256"]
            and review["criteria_committed_before_response"]
            for review in packet["rival_admission_reviews"]
        ),
        "rival_review_preserves_operative_authority_kind": all(
            review["authority_kind_before"] == review["authority_kind_after"]
            and review["grants_only_challenge_standing"]
            for review in packet["rival_admission_reviews"]
        ),
        "proposer_identity_does_not_change_admission":
            identity_audits["same_delta_packet_two_pseudonyms"]["packet_sha256_left"]
            == identity_audits["same_delta_packet_two_pseudonyms"]["packet_sha256_right"]
            and identity_audits["same_delta_packet_two_pseudonyms"]["decision_left"]
            == identity_audits["same_delta_packet_two_pseudonyms"]["decision_right"]
            and identity_audits["same_delta_packet_two_pseudonyms"]["identity_blinded_during_merits_review"],
        "every_rival_disposition_has_review_and_appeal":
            {review["admission_id"] for review in rival_reviews.values()} == set(rival_admissions)
            and all(review["appeal_available"] and review["appeal_reviewers"] for review in rival_reviews.values()),
        "review_authority_roots_are_externally_certified": all(
            root["issuing_charter"] != root["id"]
            and root["issuing_charter"]
            and root["id"] not in root["provenance_chain"]
            for root in review_roots.values()
        ),
        "review_root_scope_is_strictly_procedural": all(
            root["authority_kind"] == "procedural_review"
            and root["operative_authority_ceiling"] == "challenge_standing"
            and not root["may_select_mechanism_truth"]
            and root["revocable"]
            for root in review_roots.values()
        ),
        "review_root_independence_has_zero_coherence_defect":
            root_audits["merits_roots_A_B_independent"]["shared_controlling_ancestors"] == []
            and bool(root_audits["merits_roots_A_B_independent"]["source_derived_comparison"])
            and root_audits["merits_roots_A_B_independent"]["coherence_defect"] == 0,
        "appeal_authority_is_certified_and_separate": all(
            all(root in review_roots and review_roots[root]["jurisdiction"] == "rival_admission_appeal"
                for root in review["appeal_authority_roots"])
            and not set(review["appeal_authority_roots"]) & set(review["reviewer_authority_roots"])
            for review in rival_reviews.values()
        ),
        "revocation_preserves_history_but_suspends_live_standing":
            temporal_audits["revoke_merits_root_then_replay"]["historical_decision_preserved"]
            and not temporal_audits["revoke_merits_root_then_replay"]["prospective_authority_before_replay"],
        "temporal_replay_uses_same_frozen_packet":
            temporal_audits["revoke_merits_root_then_replay"]["replay_packet_sha256"]
            == rival_reviews["review_mechanism_delta"]["immutable_evidence_packet_sha256"],
        "live_successor_roots_restore_prospective_standing":
            temporal_audits["revoke_merits_root_then_replay"]["replay_completed"]
            and temporal_audits["revoke_merits_root_then_replay"]["prospective_authority_after_replay"]
            and all(
                root in review_roots
                and review_roots[root]["valid_from"] <= temporal_audits["revoke_merits_root_then_replay"]["replayed_at"]
                and (review_roots[root]["revoked_at"] is None
                     or temporal_audits["revoke_merits_root_then_replay"]["replayed_at"] < review_roots[root]["revoked_at"])
                for root in temporal_audits["revoke_merits_root_then_replay"]["replay_roots"]
            ),
        "independent_successor_atlases_are_flat":
            len({path["decision"] for path in temporal_atlases["two_successor_atlases_same_packet"]["paths"]}) == 1
            and temporal_atlases["two_successor_atlases_same_packet"]["disposition_defect"] == 0
            and temporal_atlases["two_successor_atlases_same_packet"]["prospective_authority_restored"],
        "temporal_replay_paths_have_disjoint_roots":
            all(
                not set(temporal_atlases["two_successor_atlases_same_packet"]["paths"][i]["roots"])
                & set(temporal_atlases["two_successor_atlases_same_packet"]["paths"][j]["roots"])
                for i in range(len(temporal_atlases["two_successor_atlases_same_packet"]["paths"]))
                for j in range(i + 1, len(temporal_atlases["two_successor_atlases_same_packet"]["paths"]))
            ),
        "higher_appeal_cell_compares_without_selecting_truth":
            temporal_atlases["two_successor_atlases_same_packet"]["higher_appeal_cell"]["role"]
            == "compare_procedure_not_truth"
            and not temporal_atlases["two_successor_atlases_same_packet"]["higher_appeal_cell"]["may_override_disagreement"],
        "three_atlas_comparison_cells_form_zero_cocycle":
            temporal_cocycles["triangle_AB_CD_EF"]["cocycle_defect"] == 0
            and temporal_cocycles["triangle_AB_CD_EF"]["global_standing_restored"]
            and len(temporal_cocycles["triangle_AB_CD_EF"]["comparison_cells"]) == 3,
        "temporal_comparison_cells_are_procedural_and_natural": all(
            cell["authority_kind"] == "procedural_review"
            and not cell["may_select_truth"]
            and cell["invertible"]
            and cell["naturality_defect"] == 0
            for cell in temporal_cocycles["triangle_AB_CD_EF"]["comparison_cells"]
        ),
        "authority_stack_has_finite_replayable_generator_basis":
            len(stack_certificates["current_delta_challenge_standing_certificate"]["generators"]) == 11
            and bool(stack_certificates["current_delta_challenge_standing_certificate"]["deterministic_replay_checker"])
            and stack_certificates["current_delta_challenge_standing_certificate"]["terminal_claim_node"] == "current_challenge_standing",
        "certificate_minimality_is_bounded_and_deletion_witnessed":
            not stack_certificates["current_delta_challenge_standing_certificate"]["claims_absolute_minimality"]
            and len(stack_certificates["current_delta_challenge_standing_certificate"]["minimality_witnesses"])
            == len(stack_certificates["current_delta_challenge_standing_certificate"]["generators"])
            and all(witness["deletion_breaks_terminal_claim"] for witness in stack_certificates["current_delta_challenge_standing_certificate"]["minimality_witnesses"]),
        "certificate_digest_identifies_but_does_not_authorize":
            stack_certificates["current_delta_challenge_standing_certificate"]["replay_checker_sha256"]
            == hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
            and not stack_certificates["current_delta_challenge_standing_certificate"]["digest_confers_authority"],
        "certificate_generator_deletions_are_replayed": all(
            item["passed"] for item in certificate_deletion_results.values()
        ),
        "capability_execution_is_atomic_and_epoch_fresh":
            capability_executions["execute_delta_challenge_once"]["atomic_revocation_check"]
            and capability_executions["execute_delta_challenge_once"]["root_revocation_epoch_snapshot"]
            == capability_executions["execute_delta_challenge_once"]["execution_revocation_epochs"]
            and capability_executions["execute_delta_challenge_once"]["execution_time"]
            <= capability_executions["execute_delta_challenge_once"]["lease_expires"],
        "capability_execution_is_scoped_and_single_use":
            capability_executions["execute_delta_challenge_once"]["operation"]
            in stack_certificates["current_delta_challenge_standing_certificate"]["allowed_operations"]
            and capability_executions["execute_delta_challenge_once"]["target_scope"]
            == stack_certificates["current_delta_challenge_standing_certificate"]["target_scope"]
            and capability_executions["execute_delta_challenge_once"]["nonce_consumed"]
            and not capability_executions["execute_delta_challenge_once"]["second_use_permitted"],
        "two_site_indistinguishability_no_go_is_exact":
            distributed_audits["two_site_partitioned_single_use_no_go"]["symmetric_deterministic_outcomes"] == [[0, 0], [1, 1]]
            and all(sum(outcome) != 1 for outcome in distributed_audits["two_site_partitioned_single_use_no_go"]["symmetric_deterministic_outcomes"])
            and not distributed_audits["two_site_partitioned_single_use_no_go"]["local_protocol_guarantees_exactly_one"],
        "distributed_consumption_trichotomy_is_typed":
            {repair["kind"] for repair in distributed_audits["two_site_partitioned_single_use_no_go"]["repairs"]}
            == {"shared_linearization", "site_partition", "bounded_multiplicity"},
        "shared_linearizer_is_minimal_true_single_use_repair":
            distributed_audits["two_site_partitioned_single_use_no_go"]["minimal_single_use_repair"] == "shared_linearization"
            and next(repair for repair in distributed_audits["two_site_partitioned_single_use_no_go"]["repairs"] if repair["kind"] == "shared_linearization")["state_cardinality"] == 2
            and next(repair for repair in distributed_audits["two_site_partitioned_single_use_no_go"]["repairs"] if repair["kind"] == "shared_linearization")["global_outcome"] == [1, 0],
        "distributed_linearity_trilemma_has_exact_three_frontier_designs":
            {
                (design["single_use_safety"], design["availability_at_both_sites"], design["partition_tolerance"])
                for design in trilemma_audits["single_use_safety_availability_partition_trilemma"]["maximal_designs"]
            } == {(True, True, False), (True, False, True), (False, True, True)}
            and not trilemma_audits["single_use_safety_availability_partition_trilemma"]["claims_all_three"],
        "safe_partition_run_fails_closed_with_fencing":
            trilemma_audits["single_use_safety_availability_partition_trilemma"]["safe_partition_run"]["quorum_outcome"] == 1
            and trilemma_audits["single_use_safety_availability_partition_trilemma"]["safe_partition_run"]["minority_outcome"] == 0
            and trilemma_audits["single_use_safety_availability_partition_trilemma"]["safe_partition_run"]["new_fencing_epoch"]
            > trilemma_audits["single_use_safety_availability_partition_trilemma"]["safe_partition_run"]["old_fencing_epoch"]
            and not trilemma_audits["single_use_safety_availability_partition_trilemma"]["safe_partition_run"]["stale_epoch_execution_permitted"],
        "majority_quorums_intersect_pairwise": all(
            set(constructor_networks["three_replica_majority_linearizer"]["authorized_quorums"][i])
            & set(constructor_networks["three_replica_majority_linearizer"]["authorized_quorums"][j])
            for i in range(len(constructor_networks["three_replica_majority_linearizer"]["authorized_quorums"]))
            for j in range(i + 1, len(constructor_networks["three_replica_majority_linearizer"]["authorized_quorums"]))
        ),
        "intersection_replica_enforces_durable_non_equivocation":
            constructor_networks["three_replica_majority_linearizer"]["conflict_exclusion_proof"]["intersection_witness"] == ["r2"]
            and constructor_networks["three_replica_majority_linearizer"]["conflict_exclusion_proof"]["witness_rejects_second_vote"]
            and not constructor_networks["three_replica_majority_linearizer"]["conflict_exclusion_proof"]["second_certificate_constructible"]
            and all(
                replica["durable_append_only_vote_cell"] and replica["survives_restart"] and replica["monotone_epoch"]
                for replica in constructor_networks["three_replica_majority_linearizer"]["replicas"]
            ),
        "physical_non_equivocation_boundary_is_explicit":
            constructor_networks["three_replica_majority_linearizer"]["implementation_boundary"]["durable_cell_status"]
            == "explicit_constructor_assumption"
            and constructor_networks["three_replica_majority_linearizer"]["implementation_boundary"]["requires_storage_authority"]
            and not constructor_networks["three_replica_majority_linearizer"]["implementation_boundary"]["claims_derived_from_quorum_math"],
        "crash_and_byzantine_thresholds_are_distinguished":
            fault_audits["crash_recovery_n3_q2_f1"]["claimed_safe"]
            and fault_audits["crash_recovery_n3_q2_f1"]["safety_condition"] == "minimum_intersection>=1"
            and not fault_audits["byzantine_n3_q2_f1_no_go"]["claimed_safe"]
            and fault_audits["byzantine_n3_q2_f1_no_go"]["safety_condition"] == "minimum_intersection>fault_bound"
            and fault_audits["byzantine_n4_q3_f1"]["claimed_safe"],
        "byzantine_safety_requires_honest_quorum_overlap":
            fault_audits["byzantine_n3_q2_f1_no_go"]["minimum_intersection"]
            <= fault_audits["byzantine_n3_q2_f1_no_go"]["fault_bound"]
            and fault_audits["byzantine_n4_q3_f1"]["minimum_intersection"]
            > fault_audits["byzantine_n4_q3_f1"]["fault_bound"]
            and fault_audits["byzantine_n3_q2_f1_no_go"]["conflict_witness"]["both_certificates_constructible"],
        "correlated_fault_hypergraph_falsifies_nominal_n4_q3":
            not hypergraph_audits["correlated_n4_q3_unsafe"]["claimed_safe"]
            and hypergraph_audits["correlated_n4_q3_unsafe"]["violation_witness"]["honest_overlap"] == [],
        "diversification_or_quorum_expansion_repairs_common_causes":
            hypergraph_audits["diversified_n4_q3_safe"]["claimed_safe"]
            and hypergraph_audits["correlated_n5_q4_safe"]["claimed_safe"]
            and len(set(hypergraph_audits["diversified_n4_q3_safe"]["replica_authority_roots"].values())) == 4,
        "common_cause_fault_sets_are_derived_from_authority_roots": all(
            all(
                sorted(replica for replica, value in audit["replica_authority_roots"].items() if value == root)
                in [sorted(fault_set) for fault_set in audit["admissible_fault_sets"]]
                for root in set(audit["replica_authority_roots"].values())
            )
            for audit in hypergraph_audits.values()
        ),
        "intervention_response_support_discovers_new_fault_edge":
            discovery_audits["discover_shared_build_pipeline_edge"]["intervention_response_matrix"][-1] == [1, 1, 0, 0]
            and discovery_audits["discover_shared_build_pipeline_edge"]["derived_fault_set"] == ["r1", "r2"]
            and ["r1", "r2"] in discovery_audits["discover_shared_build_pipeline_edge"]["extended_fault_sets"],
        "new_common_cause_suspends_then_revalidates_safety":
            discovery_audits["discover_shared_build_pipeline_edge"]["status"] == "challenge_open"
            and not discovery_audits["discover_shared_build_pipeline_edge"]["old_safety_authority_retained"]
            and discovery_audits["discover_shared_build_pipeline_edge"]["repair_status"] == "revalidated"
            and hypergraph_audits[discovery_audits["discover_shared_build_pipeline_edge"]["repair_fault_audit"]]["claimed_safe"],
        "common_cause_discovery_remains_open_world":
            bool(discovery_audits["discover_shared_build_pipeline_edge"]["bounded_tested_constructor_grammar"])
            and not discovery_audits["discover_shared_build_pipeline_edge"]["claims_universal_independence"],
        "probe_grammar_coverage_is_source_relative":
            probe_grammar_audits["common_cause_probe_grammar_v2"]["coverage_kind"] == "relative_exhaustion"
            and bool(probe_grammar_audits["common_cause_probe_grammar_v2"]["authority_root"])
            and not probe_grammar_audits["common_cause_probe_grammar_v2"]["claims_constructor_universality"],
        "grammar_refinement_expires_negative_but_preserves_positive_evidence":
            probe_grammar_audits["common_cause_probe_grammar_v2"]["predecessor_negative_certificate_expired"]
            and probe_grammar_audits["common_cause_probe_grammar_v2"]["replay_required_after_refinement"]
            and probe_grammar_audits["common_cause_probe_grammar_v2"]["replay_status"] == "passed"
            and ["r1", "r2"] in probe_grammar_audits["common_cause_probe_grammar_v2"]["discovered_faults_preserved_under_refinement"],
        "manifest_boundary_terminates_authority_without_claiming_omniscience":
            bool(probe_grammar_boundaries["deployment_manifest_boundary_v2"]["accountable_declarer"])
            and not probe_grammar_boundaries["deployment_manifest_boundary_v2"]["self_certifying_root"]
            and not probe_grammar_boundaries["deployment_manifest_boundary_v2"]["totality_authority"],
        "open_constructor_frontier_has_live_refinement_port":
            bool(probe_grammar_boundaries["deployment_manifest_boundary_v2"]["open_frontier"])
            and probe_grammar_boundaries["deployment_manifest_boundary_v2"]["challenge_port_live"]
            and not probe_grammar_boundaries["deployment_manifest_boundary_v2"]["frontier_emptiness_claimed"],
        "probe_grammar_capability_is_atomically_epoch_bound":
            probe_grammar_epochs["manifest_v2_epoch_binding"]["audit_epoch"]
            == probe_grammar_epochs["manifest_v2_epoch_binding"]["execution_epoch"]
            and probe_grammar_epochs["manifest_v2_epoch_binding"]["atomic_manifest_epoch_check"],
        "manifest_drift_fences_stale_negative_authority":
            not probe_grammar_epochs["manifest_v2_epoch_binding"]["drift_scenario"]["old_negative_certificate_live"]
            and not probe_grammar_epochs["manifest_v2_epoch_binding"]["drift_scenario"]["old_capability_execution_permitted"]
            and probe_grammar_epochs["manifest_v2_epoch_binding"]["drift_scenario"]["grammar_replay_required"],
        "same_epoch_local_views_can_fork_on_manifest_digest":
            distributed_manifest_audits["two_site_manifest_fork_and_repair"]["local_views"][0]["epoch"]
            == distributed_manifest_audits["two_site_manifest_fork_and_repair"]["local_views"][1]["epoch"]
            and distributed_manifest_audits["two_site_manifest_fork_and_repair"]["local_views"][0]["manifest_sha256"]
            != distributed_manifest_audits["two_site_manifest_fork_and_repair"]["local_views"][1]["manifest_sha256"]
            and not distributed_manifest_audits["two_site_manifest_fork_and_repair"]["local_checks_imply_global_consistency"],
        "quorum_certificate_linearizes_epoch_digest_pair":
            set(distributed_manifest_audits["two_site_manifest_fork_and_repair"]["repair"]["certificate_value_fields"])
            == {"epoch", "manifest_sha256"}
            and distributed_manifest_audits["two_site_manifest_fork_and_repair"]["repair"]["durable_non_equivocation"]
            and not distributed_manifest_audits["two_site_manifest_fork_and_repair"]["repair"]["conflicting_same_epoch_digest_certificate_constructible"],
        "configuration_transition_requires_joint_consensus":
            reconfiguration_audits["joint_transition_epoch_12_to_13"]["joint_consensus_required"]
            and not reconfiguration_audits["joint_transition_epoch_12_to_13"]["old_only_may_activate_successor"]
            and not reconfiguration_audits["joint_transition_epoch_12_to_13"]["new_only_may_self_activate"],
        "reconfiguration_bridge_prevents_split_brain":
            reconfiguration_audits["joint_transition_epoch_12_to_13"]["bridge_witness"] == ["r2"]
            and reconfiguration_audits["joint_transition_epoch_12_to_13"]["bridge_durable_non_equivocation"]
            and not reconfiguration_audits["joint_transition_epoch_12_to_13"]["conflicting_transition_constructible"],
        "reconfiguration_threshold_depends_on_fault_model":
            len(reconfiguration_audits["joint_transition_epoch_12_to_13"]["bridge_witness"]) == 1
            and reconfiguration_audits["joint_transition_epoch_12_to_13"]["fault_kind"] == "crash_recovery"
            and len(reconfiguration_audits["byzantine_joint_transition_epoch_13_to_14"]["bridge_witness"])
            > reconfiguration_audits["byzantine_joint_transition_epoch_13_to_14"]["fault_bound"],
        "reconfiguration_bridge_survives_every_admitted_fault_edge": all(
            bool(set(reconfiguration_audits["byzantine_joint_transition_epoch_13_to_14"]["bridge_witness"]) - set(fault))
            for fault in reconfiguration_audits["byzantine_joint_transition_epoch_13_to_14"]["admissible_bridge_fault_sets"]
        ),
        "atlas_refinement_preserves_global_reconstruction":
            refinements["refine_B_atlas_by_Bprime"]["reconstruction_defect"] == 0
            and refinements["refine_B_atlas_by_Bprime"]["authority_kind_before"]
            == refinements["refine_B_atlas_by_Bprime"]["authority_kind_after"],
        "counterfactual_deletion_separates_presentation_from_source":
            deletions["delete_redundant_Bprime"]["expected_process_survives"]
            and bool(deletions["delete_redundant_Bprime"]["source_derived_reconstruction"])
            and not deletions["delete_source_gluing_mechanism"]["expected_process_survives"]
            and deletions["delete_source_gluing_mechanism"]["surviving_global_grant"] is None,
        "missing_alternative_executor_is_presentation_only":
            representation_tests["kitaev_remove_logical_presentation"]["verdict"] == "presentation_only"
            and representation_tests["kitaev_remove_logical_presentation"].get("alternative_composition") is None
            and representation_tests["kitaev_remove_logical_presentation"].get("direct_grant") is None,
        "all_hostiles_rejected": all(item["passed"] for item in hostile_results.values()),
    }
    passed = all(gates.values())
    payload = {
        "schema": "marici.authority-grant-composition-checks.v1",
        "passed": passed,
        "passed_gates": sum(gates.values()),
        "total_gates": len(gates),
        "gates": gates,
        "hostile_passed": sum(item["passed"] for item in hostile_results.values()),
        "hostile_total": len(hostile_results),
        "hostile": hostile_results,
        "certificate_deletion_replay": certificate_deletion_results,
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "hostile_fixture_sha256": hashlib.sha256(HOSTILES.read_bytes()).hexdigest(),
        "application_classification": {
            "grothendieck_folded_theta": "authority square commutes only with the explicit moving-endpoint seam/reflection coherence cell; result remains readout authority",
            "kitaev_logical_to_five_rail": "no composable authority map; conditional logical synthesis and rail-support evidence do not supply native coupler authority or encoded intertwining",
        },
        "representation_change_verdict": "A claimed explanation survives removal or replacement of B only when the induced A-to-C grant keeps its process signature and any non-identical presentation is joined by a source-derived invertible natural coherence cell. Otherwise it explains a presentation.",
        "descent_verdict": "Flat local presentation coherence is necessary but insufficient: the local grants must glue effectively and uniquely to a global authority grant, remain invariant under atlas refinement, and survive deletion only when an independent source reconstruction remains.",
        "provenance_verdict": "Even effective descent is explanatory only when every coherence and gluing witness is generated along an acyclic source-to-readout provenance order, independently of the desired target, and can be regenerated in a source-preserving replay.",
        "intervention_verdict": "A provenance graph becomes explanatory only when source interventions regenerate downstream coherence, target interventions leave upstream authority fixed, and source deletion revokes authority even if cached output persists.",
        "identification_verdict": "Interventions identify a mechanism only relative to a declared candidate family: the exact observation matrix must have no kernel beyond source-authorized gauge, the ports must be source-derived, and finite rank may not be extrapolated to a universal explanatory claim.",
        "open_world_verdict": "A new rival that enlarges the non-gauge kernel suspends identification authority. Authority returns only after a newly source-derived discriminator makes the extended family jointly faithful; no finite repair closes the space of future rivals.",
        "rival_admission_verdict": "A rival may enter the explanatory competition only through an independently generated constructor grammar, total predictions on existing ports, a non-gauge difference witness, and admission before response selection. Gauge copies and incomplete speculations cannot manufacture challenges.",
        "rival_governance_verdict": "Rival admission is a separate, content-addressed authority process: proposer and incumbent are excluded from merits adjudication, independent reviewer roots and a disjoint appeal path are required, proposer identity cannot change the decision, and review grants challenge standing without upgrading operative authority.",
        "review_root_verdict": "Reviewer independence is derived from externally chartered, revocable procedural roots with no shared controlling ancestry and a challenge-standing ceiling. Distinct labels are insufficient, self-certification is circular, and appeal requires its own certified jurisdiction.",
        "temporal_authority_verdict": "Revocation preserves the historical review record but suspends prospective challenge standing. Live authority returns only after the identical frozen evidence packet is replayed through roots certified at replay time; cached decisions are not continuing grants.",
        "temporal_atlas_verdict": "Replay is path-independent only when disjoint certified successor atlases reviewing the same frozen packet under a precommitted comparison law agree. Disagreement is governance holonomy that suspends standing; a higher appeal cell may compare or restart procedure but cannot overwrite it into truth.",
        "temporal_cocycle_verdict": "Pairwise agreement of three replay dispositions is insufficient: the direct comparison cell must equal the two-step comparison up to zero cocycle defect. Nonzero triangular holonomy makes the governance explanation factorization-dependent even when every output agrees.",
        "compression_verdict": "The current authority stack compresses to a finite proof-carrying capability: eleven typed bundle generators, an acyclic replay DAG, and eleven deletion witnesses actually replayed against the compiler. Minimality is relative to the declared DPC constructor grammar, and the checker digest identifies the replay program but carries no authority.",
        "capability_execution_verdict": "A replayed certificate becomes executable only through an atomic revocation-epoch lease binding one exact operation, target, and single-use nonce. Epoch change aborts execution; the lease cannot widen scope, survive expiry, or upgrade challenge standing.",
        "distributed_consumption_verdict": "Two sites with identical valid local views and no pre-execution communication cannot deterministically guarantee exactly one success: symmetry permits only (0,0) or (1,1). True global single use requires a source-authorized shared linearizer; pre-distribution site partition restricts the eligible locus, while concurrent success changes the resource to bounded multiplicity.",
        "distributed_linearity_trilemma_verdict": "For one globally linear capability, single-use safety, availability at both authority loci, and partition tolerance cannot coexist. A safe partitioned linearizer serves only the source-authorized quorum component, fences stale epochs, and fails closed elsewhere; eventual recovery is not availability during partition.",
        "linearizer_constructor_verdict": "The atomic linearizer is realized by a three-replica majority network: every two winning quorums intersect, and the shared replica's durable monotone vote cell forbids conflicting certificates in one epoch. Quorum math proves safety conditional on that storage constructor; signatures authenticate votes but do not prevent double-signing, and liveness is not implied.",
        "fault_parametric_quorum_verdict": "Quorum authority is fault-model dependent. Crash/recovery safety with durable non-equivocation requires only a nonempty overlap I_min>=1, so n=3,q=2 is safe. Byzantine safety requires I_min>f: n=3,q=2,f=1 is unsafe, while n=4,q=3,f=1 is safe.",
        "fault_hypergraph_verdict": "Replica cardinality is insufficient under correlated faults. Safety requires (Q1 intersection Q2) minus F to be nonempty for every winning-quorum pair and every source-authorized common-cause fault set F. Shared authority-root fibers are mandatory fault sets; the unsafe correlated 3-of-4 design is repaired either by root diversification or by the verified 4-of-5 geometry.",
        "common_cause_discovery_verdict": "A source-derived intervention row generates a fault hyperedge from its nonzero replica support. Discovering the shared-build edge {r1,r2} enlarges the fault family and suspends the former 3-of-4 safety claim; safety is revalidated only on a topology whose catalog retains that edge. Independence remains relative to the tested constructor grammar.",
        "verdict": "Authority grants form a partial category only on matching authority kind, variance, endpoints, and evidenced domains. Transport preserves kind, intersection restricts domains, extension requires fresh authority, and both triple composition and representation change require explicit zero-defect coherence.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii")
    for name, value in gates.items():
        print(f"{'PASS' if value else 'FAIL'} gate.{name}: {value}")
    for name, value in hostile_results.items():
        print(f"{'PASS' if value['passed'] else 'FAIL'} hostile.{name}: {value['error_codes']}")
    print(f"SUMMARY {sum(gates.values())}/{len(gates)}; HOSTILE {sum(x['passed'] for x in hostile_results.values())}/{len(hostile_results)}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
