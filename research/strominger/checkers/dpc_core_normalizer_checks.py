#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / "research" / "strominger"
sys.path.insert(0, str(S))
from dpc_core_normalizer import compile_contract  # noqa: E402

contract = json.loads((S / "contracts" / "dpc-core-normalizer.v1.json").read_text(encoding="ascii"))
legacy = json.loads((S / "contracts" / "authority-grant-composition.v1.json").read_text(encoding="ascii"))
result = compile_contract(contract, legacy)
hostile = deepcopy(contract)
del hostile["critical_pair_coverage"]["partition_flattening|typed_identity"]
hostile_result = compile_contract(hostile, legacy)
missing_coverage_rejected = not hostile_result["passed"] and any(
    not item["covered"] for item in hostile_result["generated_overlaps"]
)
result["hostile_missing_overlap_coverage_rejected"] = missing_coverage_rejected
defaulting = deepcopy(contract)
defaulting["legacy_projection_audit"]["permit_defaulting"] = True
defaulting_rejected = not compile_contract(defaulting, legacy)["passed"]
result["hostile_legacy_defaulting_rejected"] = defaulting_rejected
native_deletions = {}
for field in ("nominal_identity", "scope", "modality", "resource", "physical_support_roots", "epoch"):
    candidate = deepcopy(contract)
    del candidate["native_capabilities"][0][field]
    candidate_result = compile_contract(candidate, legacy)
    audit = candidate_result["native_capabilities"][0]
    native_deletions[field] = not candidate_result["passed"] and field in audit["missing_core_fields"]
result["native_constructor_deletions"] = native_deletions
native_epoch = contract["native_capabilities"][0]["epoch"]
symbolic_epoch_enforced = native_epoch == {"parameter": "e", "offset": 0}
result["native_symbolic_epoch_enforced"] = symbolic_epoch_enforced
successor_hostiles = {}
for field, value, expected in (
    ("competing_successor_constructible", True, "epoch_successor_fork_constructible"),
    ("successor_epoch", {"parameter":"e","offset":2}, "nonadjacent_or_cross_family_epoch_successor"),
    ("physical_state_correspondence", None, "epoch_successor_lacks_physical_correspondence"),
    ("authorized_signers", {"config_root_A":{"durable_non_equivocation":True,"independence_root":"admin_A"},"config_root_B":{"durable_non_equivocation":True,"independence_root":"admin_A"}}, "epoch_successor_signer_fault_model_unsafe"),
):
    candidate = deepcopy(contract)
    candidate["epoch_successor_events"][0][field] = value
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["epoch_successor_events"][0]["errors"]
    successor_hostiles[field] = not candidate_result["passed"] and expected in errors
result["epoch_successor_hostiles"] = successor_hostiles
attestation_hostiles = {}
for field, value in (
    ("certificate_nonce", "nonce:old"),
    ("monotone_boot_counter", 40),
    ("verifier_independence_root", "admin_A"),
):
    candidate = deepcopy(contract)
    candidate["epoch_successor_events"][0]["physical_state_correspondence"][field] = value
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["epoch_successor_events"][0]["errors"]
    attestation_hostiles[field] = not candidate_result["passed"] and "epoch_successor_attestation_stale_or_correlated" in errors
result["epoch_attestation_hostiles"] = attestation_hostiles
tcb_hostiles = {}
for field, value in (
    ("claims_absolute_unclonability", True),
    ("anti_rollback_storage", False),
    ("measured_ports", ["boot_state", "manifest_state"]),
):
    candidate = deepcopy(contract)
    candidate["epoch_successor_events"][0]["physical_state_correspondence"]["trusted_physical_base"][field] = value
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["epoch_successor_events"][0]["errors"]
    tcb_hostiles[field] = not candidate_result["passed"] and "epoch_successor_attestation_tcb_unbounded" in errors
result["attestation_tcb_hostiles"] = tcb_hostiles
execution_hostiles = {}
execution_mutations = (
    ("nonatomic_consumption", ("consumption", "atomic_compare_and_set"), False, "execution_trace_nonatomic_consumption"),
    ("replayable_nonce", ("consumption", "nonce_durably_recorded"), False, "execution_trace_replayable_nonce"),
    ("effect_outside_fence", ("execution", "effect_committed_atomically_with_fence"), False, "execution_trace_unattested_effect"),
    ("receipt_digest_mismatch", ("receipt", "effect_sha256"), "0" * 64, "execution_trace_receipt_mismatch"),
    ("history_erasure", ("history", "execution_fact_retained"), False, "execution_trace_erases_irreversible_history"),
)
for name, path, value, expected in execution_mutations:
    candidate = deepcopy(contract)
    candidate["native_execution_traces"][0][path[0]][path[1]] = value
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["native_execution_traces"][0]["errors"]
    execution_hostiles[name] = not candidate_result["passed"] and expected in errors
result["native_execution_hostiles"] = execution_hostiles
cocircuit_classes = {item["primitive_failure_class"] for item in result["trusted_base_cocircuits"]}
cocircuit_complete = cocircuit_classes == {"rollback", "hidden_port", "clone", "signer_fork", "attestation_replay"} and all(
    item["passed"] for item in result["trusted_base_cocircuits"]
)
result["trusted_base_cocircuit_basis_complete"] = cocircuit_complete
ssa_hostiles = {}
ssa_mutations = (
    ("resource_reuse", lambda c: c["resource_ssa_programs"][0]["nodes"].insert(4, {"id":"n_reuse","kind":"consume","input":"holdA","effect_output":"effectAgain","resource_region":"A"}), "linear_resource_reused_or_undefined"),
    ("partition_inflation", lambda c: c["resource_ssa_programs"][0]["nodes"][1].update({"outputs":{"rA":2,"rB":1}}), "ssa_partition_inflation"),
    ("release_without_authority", lambda c: c["resource_ssa_programs"][0]["nodes"][5].update({"release_authority":None}), "release_without_authority"),
    ("compensation_remints", lambda c: c["resource_ssa_programs"][0]["nodes"][7].update({"restores_original_capability":True}), "compensation_remints_consumed_capability"),
    ("concurrent_overlap", lambda c: c["resource_ssa_programs"][0]["nodes"][6].update({"resource_region":"A"}), "concurrent_resource_overlap_without_linearizer"),
)
for name, mutate_ssa, expected in ssa_mutations:
    candidate = deepcopy(contract)
    mutate_ssa(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["resource_ssa_programs"][0]["errors"]
    ssa_hostiles[name] = not candidate_result["passed"] and expected in errors
result["resource_ssa_hostiles"] = ssa_hostiles
projection_hostiles = {}
for field, value, expected in (
    ("claims_canonical_reverse_lift", True, "canonical_reverse_lift_laundered"),
    ("projection_constructor", None, "forgetful_projection_untyped"),
    ("legacy_fields", ["target_operation","authority_kind","source_authority_evidence","resource"], "forgetful_projection_wrong_legacy_signature"),
):
    candidate = deepcopy(contract)
    candidate["forgetful_projection_audits"][0][field] = value
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["forgetful_projections"][0]["errors"]
    projection_hostiles[field] = not candidate_result["passed"] and expected in errors
result["forgetful_projection_hostiles"] = projection_hostiles
chain_hostiles = {}
chain_mutations = (
    ("gap", lambda c: c["epoch_successor_chain_audits"][0]["steps"][1].update({"successor":{"parameter":"e","offset":3}}), "successor_chain_nonadjacent_step"),
    ("digest_break", lambda c: c["epoch_successor_chain_audits"][0]["steps"][1].update({"predecessor_state_sha256":"0" * 64}), "successor_chain_digest_link_failure"),
    ("fork", lambda c: c["epoch_successor_chain_audits"][0]["steps"][1].update({"competing_successor_constructible":True}), "successor_chain_uniqueness_failure"),
    ("support_drop", lambda c: c["epoch_successor_chain_audits"][0]["steps"][1].update({"support_added":[]}), "successor_chain_support_not_accumulated"),
)
for name, mutate_chain, expected in chain_mutations:
    candidate = deepcopy(contract)
    mutate_chain(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["epoch_successor_chains"][0]["errors"]
    chain_hostiles[name] = not candidate_result["passed"] and expected in errors
result["successor_chain_hostiles"] = chain_hostiles
reconfiguration_hostiles = {}
reconfiguration_mutations = (
    ("self_activation", lambda c: c["native_reconfiguration_constructors"][0].update({"new_only_may_self_activate":True}), "native_reconfiguration_self_authorization"),
    ("bridge_fault", lambda c: c["native_reconfiguration_constructors"][0]["admissible_bridge_fault_sets"].append(["r2","r3"]), "native_reconfiguration_bridge_fault_unsafe"),
    ("common_cause_omitted", lambda c: c["native_reconfiguration_constructors"][0].update({"admissible_bridge_fault_sets":[["r2"]]}), "native_reconfiguration_common_cause_omitted"),
    ("missing_old_support", lambda c: c["native_reconfiguration_constructors"][0]["output_signature"].update({"support":["configuration_transition_charter","executor_attestation_root","new_config_root"]}), "native_reconfiguration_support_loss"),
    ("authority_duplication", lambda c: c["native_reconfiguration_constructors"][0].update({"resource_law":"old and new configurations both remain live"}), "native_reconfiguration_duplicates_authority"),
)
for name, mutate_reconfiguration, expected in reconfiguration_mutations:
    candidate = deepcopy(contract)
    mutate_reconfiguration(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["native_reconfiguration_constructors"][0]["errors"]
    reconfiguration_hostiles[name] = not candidate_result["passed"] and expected in errors
result["native_reconfiguration_hostiles"] = reconfiguration_hostiles
configuration_path_hostiles = {}
configuration_path_mutations = (
    ("broken_incidence", lambda c: c["configuration_path_audits"][0]["edges"][1]["source_configuration"].update({"authority_resource":"cfg_auth_unrelated"}), "configuration_path_incidence_failure"),
    ("identity_edge", lambda c: c["configuration_path_audits"][0]["edges"][1]["target_configuration"].update({"vertex_id":"C1"}), "configuration_edge_untyped_or_identity"),
    ("fitted_correspondence", lambda c: c["configuration_path_audits"][0]["edges"][1]["state_correspondence"].update({"source_derived":False}), "configuration_state_correspondence_failure"),
    ("missing_joint_authorization", lambda c: c["configuration_path_audits"][0]["edges"][1].update({"target_quorum_endorsement":["r3","r4"]}), "configuration_path_joint_authorization_failure"),
    ("empty_bridge", lambda c: c["configuration_path_audits"][0]["edges"][1]["target_configuration"].update({"members":["r5","r6","r7"],"quorum":["r5","r6","r7"]}), "configuration_path_invalid_bridge"),
    ("whole_bridge_fault", lambda c: c["configuration_path_audits"][0]["edges"][1]["admissible_bridge_fault_sets"].append(["r3","r4"]), "configuration_path_bridge_fault_unsafe"),
    ("common_cause_omitted", lambda c: c["configuration_path_audits"][0]["edges"][1].update({"admissible_bridge_fault_sets":[["r3"]]}), "configuration_path_common_cause_omitted"),
    ("correlated_roots_unmodelled", lambda c: c["configuration_path_audits"][0]["edges"][1].update({"bridge_authority_roots":{"r3":"admin_C","r4":"admin_C"}}), "configuration_path_common_cause_omitted"),
    ("global_root_omitted", lambda c: c["configuration_path_audits"][0].update({"admissible_authority_root_fault_sets":[["admin_B"],["admin_C"],["admin_E"]]}), "configuration_path_global_root_fault_omitted"),
    ("global_correlated_fault", lambda c: c["configuration_path_audits"][0]["admissible_authority_root_fault_sets"].append(["admin_C","admin_D"]), "configuration_path_global_fault_unsafe"),
    ("authority_reuse", lambda c: c["configuration_path_audits"][0]["edges"][1]["output_configuration"].update({"authority_resource":"cfg_auth_C0"}), "configuration_path_linear_replacement_failure"),
    ("source_authority_duplicated", lambda c: c["configuration_path_audits"][0]["edges"][1].update({"source_authority_also_output":True,"output_authority_count":2}), "configuration_path_linear_replacement_failure"),
    ("support_drop", lambda c: c["configuration_path_audits"][0]["edges"][1]["output_configuration"].update({"support":["charter_rho_12","correspondence_rho_12","presentation_C2"]}), "configuration_path_support_union_failure"),
)
for name, mutate_path, expected in configuration_path_mutations:
    candidate = deepcopy(contract)
    mutate_path(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_paths"][0]["errors"]
    configuration_path_hostiles[name] = not candidate_result["passed"] and expected in errors
result["configuration_path_hostiles"] = configuration_path_hostiles
partial_composite_replay = {}
base_path = contract["configuration_path_audits"][0]
for edge_count in range(1, len(base_path["edges"]) + 1):
    candidate = deepcopy(contract)
    candidate_path = candidate["configuration_path_audits"][0]
    candidate_path["edges"] = candidate_path["edges"][:edge_count]
    candidate_path["expected_endpoint_configuration"] = deepcopy(candidate_path["edges"][-1]["output_configuration"])
    candidate_result = compile_contract(candidate, legacy)
    partial_composite_replay[str(edge_count)] = candidate_result["configuration_paths"][0]["passed"]
result["configuration_path_partial_composite_replay"] = partial_composite_replay
configuration_category_hostiles = {}
for name, mutate_category, expected in (
    ("identity_changes_signature", lambda c: c["configuration_category_audits"][0].update({"identity_preserves_full_signature":False}), "configuration_category_identity_failure"),
    ("associativity_witness_reordered", lambda c: c["configuration_category_audits"][0].update({"associativity_edge_ids":["rho_12","rho_01","rho_23"]}), "configuration_category_associativity_witness_untyped"),
    ("composition_seam_mismatch", lambda c: c["configuration_path_audits"][0]["edges"][1].update({"input_authority_resource":"cfg_auth_unrelated"}), "configuration_category_associativity_failure"),
):
    candidate = deepcopy(contract)
    mutate_category(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_category"][0]["errors"]
    configuration_category_hostiles[name] = not candidate_result["passed"] and expected in errors
result["configuration_category_hostiles"] = configuration_category_hostiles
configuration_coherence_hostiles = {}
def configuration_path(candidate, path_id):
    return next(path for path in candidate["configuration_path_audits"] if path["id"] == path_id)

for name, mutate_coherence, expected in (
    ("primitive_cell_injected", lambda c: c["configuration_path_coherence_audits"][0].update({"coherence_cell":{"id":"fitted"}}), "primitive_configuration_coherence_forbidden"),
    ("different_endpoint", lambda c: (configuration_path(c,"alternate_configuration_path")["edges"][-1]["target_configuration"].update({"vertex_id":"CZ"}), configuration_path(c,"alternate_configuration_path")["edges"][-1]["output_configuration"].update({"vertex_id":"CZ"}), configuration_path(c,"alternate_configuration_path")["expected_endpoint_configuration"].update({"vertex_id":"CZ"})), "configuration_coherence_boundary_mismatch"),
    ("different_support", lambda c: (configuration_path(c,"alternate_configuration_path")["edges"][-1]["target_configuration"]["support"].append("route_specific_support"), configuration_path(c,"alternate_configuration_path")["edges"][-1]["output_configuration"]["support"].append("route_specific_support"), configuration_path(c,"alternate_configuration_path")["expected_endpoint_configuration"]["support"].append("route_specific_support")), "configuration_coherence_support_mismatch"),
    ("fault_hypergraph_disagreement", lambda c: configuration_path(c,"alternate_configuration_path")["admissible_authority_root_fault_sets"].append(["admin_C","admin_E"]), "configuration_coherence_fault_descent_failure"),
    ("alternate_path_not_admissible", lambda c: configuration_path(c,"alternate_configuration_path")["edges"][0]["state_correspondence"].update({"source_derived":False}), "configuration_coherence_path_not_admissible"),
):
    candidate = deepcopy(contract)
    mutate_coherence(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_path_coherence"][0]["errors"]
    configuration_coherence_hostiles[name] = not candidate_result["passed"] and expected in errors
result["configuration_coherence_hostiles"] = configuration_coherence_hostiles
configuration_normalization_hostiles = {}
for name, mutate_normalization, expected_section, expected in (
    ("unauthorized_rewrite", lambda c: c["configuration_constructor_rewrites"][0].update({"source_authority_root":None}), "configuration_constructor_rewrites", "configuration_rewrite_unauthorized"),
    ("duplicate_rewrite", lambda c: c["configuration_constructor_rewrites"].append(deepcopy(c["configuration_constructor_rewrites"][0])), "configuration_constructor_rewrites", "configuration_rewrite_duplicate"),
    ("normal_form_target_fitted", lambda c: c["configuration_constructor_rewrites"][2].update({"normal_form_id":"NF_FITTED"}), "configuration_constructor_rewrites", "configuration_rewrite_target_fitted"),
    ("rewrite_cycle", lambda c: c["configuration_constructor_rewrites"].append({"id":"rewrite_tau_rho","source_path_id":"third_configuration_path","target_path_id":"varying_membership_configuration_path","source_authority_root":"factorization_charter","admissible_transformation":"factorization_substitution"}), "configuration_normalization", "configuration_rewrite_nonterminating"),
    ("nonconfluent_fork", lambda c: c["configuration_constructor_rewrites"].pop(1), "configuration_normalization", "configuration_rewrite_nonconfluent"),
    ("required_critical_pair_deleted", lambda c: c["configuration_constructor_rewrites"].pop(2), "configuration_normalization", "configuration_rewrite_required_critical_pair_missing"),
    ("triangle_target_fitted", lambda c: c["configuration_coherence_triangle_audits"][0].update({"normal_form_id":"NF_FITTED"}), "configuration_coherence_triangles", "configuration_coherence_triangle_target_fitted"),
):
    candidate = deepcopy(contract)
    mutate_normalization(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = [error for audit in candidate_result[expected_section] for error in audit["errors"]]
    configuration_normalization_hostiles[name] = not candidate_result["passed"] and expected in errors
result["configuration_normalization_hostiles"] = configuration_normalization_hostiles
contextual_rewrite_hostiles = {}
for name, mutate_contextual, expected in (
    ("nondecreasing_rank", lambda c: c["configuration_contextual_rewrite_theorems"][0]["rank"].update({"varying_membership_configuration_path":1}), "contextual_rewrite_rank_not_decreasing"),
    ("context_closure_removed", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"context_closure":False}), "contextual_rewrite_context_signature_not_preserved"),
    ("sequential_composition_smuggled", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"composition_kind":"sequential_path_composition","sequential_composition_claimed":True}), "contextual_rewrite_sequential_composition_smuggled"),
    ("hole_boundary_smeared", lambda c: c["configuration_contextual_rewrite_theorems"][0]["hole_type"].update({"endpoint_vertex":"C_any"}), "contextual_rewrite_hole_type_mismatch"),
    ("linear_authority_cloned", lambda c: c["configuration_contextual_rewrite_theorems"][0]["hole_type"].update({"resource_instances_pairwise_disjoint":False,"shared_authority_claimed":True}), "contextual_rewrite_hole_type_mismatch"),
    ("concrete_authority_reused", lambda c: c["configuration_contextual_rewrite_theorems"][0]["hole_type"].update({"input_authority_parameter":"cfg_auth_C0"}), "contextual_rewrite_hole_type_mismatch"),
    ("untagged_support_union", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"support_lift":"support"}), "contextual_rewrite_indexed_fiber_collision"),
    ("cross_hole_fault_smuggled", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"fault_hypergraph_composition":"shared_union","cross_hole_correlations_authorized":True}), "contextual_rewrite_indexed_fiber_collision"),
    ("untyped_context_grammar", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"context_grammar":"free_word_monoid"}), "contextual_rewrite_sequential_composition_smuggled"),
    ("support_not_preserved", lambda c: c["configuration_contextual_rewrite_theorems"][0]["preserved_semantic_fields"].remove("support_union"), "contextual_rewrite_context_signature_not_preserved"),
    ("rewrite_semantics_change", lambda c: (configuration_path(c,"alternate_configuration_path")["edges"][-1]["target_configuration"]["support"].append("context_visible_support"), configuration_path(c,"alternate_configuration_path")["edges"][-1]["output_configuration"]["support"].append("context_visible_support"), configuration_path(c,"alternate_configuration_path")["expected_endpoint_configuration"]["support"].append("context_visible_support")), "contextual_rewrite_context_signature_not_preserved"),
    ("disjoint_schema_omitted", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"critical_pair_schemas":["same_position_branch"]}), "contextual_rewrite_critical_schema_incomplete"),
    ("rewrite_coverage_omitted", lambda c: c["configuration_contextual_rewrite_theorems"][0]["rewrite_ids"].remove("rewrite_rho_tau"), "contextual_rewrite_rule_coverage_failure"),
    ("bounded_scope_substituted", lambda c: c["configuration_contextual_rewrite_theorems"][0].update({"theorem_scope":"words of length at most three"}), "contextual_rewrite_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_contextual(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_contextual_rewrite_theorems"][0]["errors"]
    contextual_rewrite_hostiles[name] = not candidate_result["passed"] and expected in errors
result["contextual_rewrite_hostiles"] = contextual_rewrite_hostiles
context_symmetry_hostiles = {}
for name, mutate_symmetry, expected in (
    ("nonbijective_action", lambda c: c["configuration_context_symmetry_theorems"][0].update({"symmetry":"all_hole_maps"}), "context_symmetry_nonbijective_or_bounded"),
    ("resource_aliasing_action", lambda c: c["configuration_context_symmetry_theorems"][0].update({"resource_action":"all_indices_share_alpha"}), "context_symmetry_fiber_action_not_faithful"),
    ("position_dependent_rewrite", lambda c: c["configuration_constructor_rewrites"][0].update({"hole_index":0}), "context_symmetry_rewrite_depends_on_position"),
    ("cross_hole_fault_action", lambda c: c["configuration_context_symmetry_theorems"][0].update({"cross_hole_fault_action":"identify_equal_root_labels"}), "context_symmetry_cross_hole_fault_laundered"),
    ("normalization_before_renaming_only", lambda c: c["configuration_context_symmetry_theorems"][0].update({"normal_form_action":"normalize_fixed_indices_only"}), "context_symmetry_normalization_not_equivariant"),
):
    candidate = deepcopy(contract)
    mutate_symmetry(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_context_symmetry_theorems"][0]["errors"]
    context_symmetry_hostiles[name] = not candidate_result["passed"] and expected in errors
result["context_symmetry_hostiles"] = context_symmetry_hostiles
correlated_context_hostiles = {}
for name, mutate_correlation, expected in (
    ("missing_constructor_authority", lambda c: c["configuration_correlated_context_theorems"][0].update({"source_authority_root":None}), "correlated_context_constructor_unauthorized"),
    ("support_identified", lambda c: c["configuration_correlated_context_theorems"][0].update({"support_identification":True}), "correlated_context_authority_or_support_laundered"),
    ("resources_identified", lambda c: c["configuration_correlated_context_theorems"][0].update({"resource_identification":True}), "correlated_context_authority_or_support_laundered"),
    ("single_hole_not_correlation", lambda c: c["configuration_correlated_context_theorems"][0].update({"correlation_hyperedges":[[["h0","admin_C"]]]}), "correlated_context_hyperedge_untyped"),
    ("correlation_exhausts_bridge", lambda c: c["configuration_correlated_context_theorems"][0]["correlation_hyperedges"].append([["h0","admin_B"],["h0","admin_C"],["h1","admin_C"]]), "correlated_context_exhausts_local_bridge"),
    ("full_symmetry_retained", lambda c: c["configuration_correlated_context_theorems"][0].update({"symmetry":"finite_bijections_of_hole_indices"}), "correlated_context_symmetry_group_incorrect"),
    ("wrong_stabilizer", lambda c: c["configuration_correlated_context_theorems"][0]["expected_automorphisms"].append(["h2","h1","h0"]), "correlated_context_symmetry_group_incorrect"),
    ("position_sensitive_normalization", lambda c: c["configuration_constructor_rewrites"][0].update({"hole_index":"h0"}), "correlated_context_normalization_not_equivariant"),
    ("scope_expanded_without_constructor", lambda c: c["configuration_correlated_context_theorems"][0].update({"theorem_scope":"all cross-hole relations"}), "correlated_context_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_correlation(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_correlated_context_theorems"][0]["errors"]
    correlated_context_hostiles[name] = not candidate_result["passed"] and expected in errors
result["correlated_context_hostiles"] = correlated_context_hostiles
correlation_cocircuit_hostiles = {}
for name, mutate_cocircuit, expected in (
    ("wrong_classification", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"classification":"all_indexed_root_singletons"}), "correlation_cocircuit_classification_untyped"),
    ("wrong_safety_law", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"safety_law":"safe_iff_each_hyperedge_is_small"}), "correlation_cocircuit_safety_law_untyped"),
    ("wrong_minimality_law", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"minimality_law":"proper_subsets_may_remain_fatal"}), "correlation_cocircuit_minimality_untyped"),
    ("wrong_symmetry_action", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"symmetry_action":"full_symmetric_group_orbits"}), "correlation_cocircuit_symmetry_action_untyped"),
    ("wrong_cocircuit_count", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"expected_cocircuit_count":5}), "correlation_cocircuit_count_mismatch"),
    ("wrong_orbit_count", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"expected_orbit_count":3}), "correlation_cocircuit_orbit_mismatch"),
    ("unsafe_admitted_hyperedge", lambda c: c["configuration_correlated_context_theorems"][0]["correlation_hyperedges"].append([["h0","admin_D"],["h0","admin_E"],["h2","admin_C"]]), "correlation_cocircuit_present_in_admitted_hyperedge"),
    ("bounded_scope", lambda c: c["configuration_correlation_cocircuit_theorems"][0].update({"theorem_scope":"three-hole fixture only"}), "correlation_cocircuit_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_cocircuit(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_correlation_cocircuit_theorems"][0]["errors"]
    correlation_cocircuit_hostiles[name] = not candidate_result["passed"] and expected in errors
result["correlation_cocircuit_hostiles"] = correlation_cocircuit_hostiles
correlation_composition_hostiles = {}
for name, mutate_composition, expected in (
    ("modes_conflated", lambda c: c["configuration_correlation_composition_theorems"][0].update({"family_union_semantics":"union_loci_into_one_hyperedge"}), "correlation_composition_modes_conflated"),
    ("fusion_has_no_constructor", lambda c: c["configuration_correlation_composition_theorems"][0].update({"fusion_constructor_id":None}), "correlation_composition_fusion_authority_laundered"),
    ("family_union_authorizes_fusion", lambda c: c["configuration_correlation_composition_theorems"][0].update({"family_union_authorizes_fusion":True}), "correlation_composition_fusion_authority_laundered"),
    ("seam_law_by_input_safety", lambda c: c["configuration_correlation_composition_theorems"][0].update({"seam_law":"safe_inputs_imply_safe_fusion"}), "correlation_composition_seam_law_untyped"),
    ("unsafe_fusion_claimed_safe", lambda c: c["configuration_correlation_composition_theorems"][0]["fixtures"][1]["expected"].update({"fused_safe":True}), "correlation_composition_fixture_mismatch"),
    ("split_cocircuit_hidden", lambda c: c["configuration_correlation_composition_theorems"][0]["fixtures"][1]["expected"].update({"split_cocircuit_count":0}), "correlation_composition_fixture_mismatch"),
    ("unsafe_fixture_deleted", lambda c: c["configuration_correlation_composition_theorems"][0].update({"fixtures":c["configuration_correlation_composition_theorems"][0]["fixtures"][:1]}), "correlation_composition_fixture_coverage_incomplete"),
    ("bounded_scope", lambda c: c["configuration_correlation_composition_theorems"][0].update({"theorem_scope":"two fixtures only"}), "correlation_composition_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_composition(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_correlation_composition_theorems"][0]["errors"]
    correlation_composition_hostiles[name] = not candidate_result["passed"] and expected in errors
result["correlation_composition_hostiles"] = correlation_composition_hostiles
finite_fusion_hostiles = {}
for name, mutate_fusion, expected in (
    ("fitted_bound", lambda c: c["configuration_finite_fusion_theorems"][0].update({"witness_bound_source":"fixture_search"}), "finite_fusion_witness_bound_not_source_derived"),
    ("wrong_bound", lambda c: c["configuration_finite_fusion_theorems"][0].update({"expected_witness_bound":3}), "finite_fusion_witness_bound_not_source_derived"),
    ("subfamily_law_removed", lambda c: c["configuration_finite_fusion_theorems"][0].update({"finite_subfamily_law":"global_check_only"}), "finite_fusion_subfamily_law_untyped"),
    ("pairwise_completeness_denied", lambda c: c["configuration_finite_fusion_theorems"][0].update({"pairwise_completeness_claimed":False}), "finite_fusion_pairwise_completeness_mismatch"),
    ("sharpness_denied", lambda c: c["configuration_finite_fusion_theorems"][0].update({"bound_sharp_on_fixture":False}), "finite_fusion_witness_bound_not_sharp"),
    ("unsafe_family_claimed_safe", lambda c: c["configuration_finite_fusion_theorems"][0]["fixtures"][0]["expected"].update({"globally_safe":True}), "finite_fusion_fixture_mismatch"),
    ("witness_arity_hidden", lambda c: c["configuration_finite_fusion_theorems"][0]["fixtures"][0]["expected"].update({"minimum_unsafe_arity":None}), "finite_fusion_fixture_mismatch"),
    ("bounded_scope", lambda c: c["configuration_finite_fusion_theorems"][0].update({"theorem_scope":"three-input fixture only"}), "finite_fusion_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_fusion(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_finite_fusion_theorems"][0]["errors"]
    finite_fusion_hostiles[name] = not candidate_result["passed"] and expected in errors
result["finite_fusion_hostiles"] = finite_fusion_hostiles
correlation_repair_hostiles = {}
for name, mutate_repair, expected in (
    ("fitted_repair", lambda c: c["configuration_correlation_repair_theorems"][0].update({"repair_classification":"smallest_fixture_deletion"}), "correlation_repair_classification_untyped"),
    ("missing_repair_constructor", lambda c: c["configuration_correlation_repair_theorems"][0].update({"repair_constructor_id":None}), "correlation_repair_authority_laundered"),
    ("diagnosis_authorizes_mutation", lambda c: c["configuration_correlation_repair_theorems"][0].update({"diagnosis_authorizes_repair":True}), "correlation_repair_authority_laundered"),
    ("repair_adds_authority", lambda c: c["configuration_correlation_repair_theorems"][0].update({"repair_effect":"mint_replacement_authority"}), "correlation_repair_authority_laundered"),
    ("shared_repair_hidden", lambda c: c["configuration_correlation_repair_theorems"][0]["fixtures"][0]["expected"].update({"minimal_repair_count":1}), "correlation_repair_fixture_mismatch"),
    ("repair_sizes_fitted", lambda c: c["configuration_correlation_repair_theorems"][0]["fixtures"][0]["expected"].update({"minimal_repair_sizes":[1,1]}), "correlation_repair_fixture_mismatch"),
    ("bounded_scope", lambda c: c["configuration_correlation_repair_theorems"][0].update({"theorem_scope":"one fixture only"}), "correlation_repair_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_repair(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_correlation_repair_theorems"][0]["errors"]
    correlation_repair_hostiles[name] = not candidate_result["passed"] and expected in errors
result["correlation_repair_hostiles"] = correlation_repair_hostiles
repair_selection_hostiles = {}
for name, mutate_selection, expected in (
    ("untyped_valuation", lambda c: c["configuration_repair_selection_theorems"][0].update({"valuation_kind":"arbitrary_scores"}), "repair_selection_valuation_untyped"),
    ("missing_selector_authority", lambda c: c["configuration_repair_selection_theorems"][0].update({"selector_source_authority_root":None}), "repair_selection_authority_laundered"),
    ("safety_selects", lambda c: c["configuration_repair_selection_theorems"][0].update({"safety_authorizes_selection":True}), "repair_selection_authority_laundered"),
    ("selection_executes", lambda c: c["configuration_repair_selection_theorems"][0].update({"selection_authorizes_execution":True}), "repair_selection_authority_laundered"),
    ("wrong_selection_law", lambda c: c["configuration_repair_selection_theorems"][0].update({"selection_law":"fewest_loci_without_valuation"}), "repair_selection_law_untyped"),
    ("zero_cost", lambda c: c["configuration_repair_selection_theorems"][0]["valuation_profiles"][0]["weights"][0].update({"cost":0}), "repair_selection_profile_mismatch"),
    ("profile_missing_locus", lambda c: c["configuration_repair_selection_theorems"][0]["valuation_profiles"][0].update({"weights":c["configuration_repair_selection_theorems"][0]["valuation_profiles"][0]["weights"][:2]}), "repair_selection_profile_mismatch"),
    ("fitted_winner", lambda c: c["configuration_repair_selection_theorems"][0]["valuation_profiles"][0].update({"expected_selected_repair":[["h0","admin_C"]]}), "repair_selection_profile_mismatch"),
    ("canonical_selector_claimed", lambda c: c["configuration_repair_selection_theorems"][0].update({"no_canonical_selector_from_safety":False}), "repair_selection_canonical_choice_smuggled"),
    ("bounded_scope", lambda c: c["configuration_repair_selection_theorems"][0].update({"theorem_scope":"two valuation profiles only"}), "repair_selection_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_selection(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_repair_selection_theorems"][0]["errors"]
    repair_selection_hostiles[name] = not candidate_result["passed"] and expected in errors
result["repair_selection_hostiles"] = repair_selection_hostiles
repair_execution_hostiles = {}
for name, mutate_repair_execution, expected in (
    ("certificate_omits_valuation", lambda c: c["configuration_repair_execution_theorems"][0].update({"certificate_binding_fields":["unsafe_hyperedge","primitive_repair_family","selected_repair"]}), "repair_execution_certificate_underbound"),
    ("missing_executor_root", lambda c: c["configuration_repair_execution_theorems"][0].update({"executor_source_authority_root":None}), "repair_execution_authority_laundered"),
    ("reusable_capability", lambda c: c["configuration_repair_execution_theorems"][0].update({"capability_modality":"unrestricted"}), "repair_execution_authority_laundered"),
    ("selection_record_executes", lambda c: c["configuration_repair_execution_theorems"][0].update({"selection_record_is_nonexecuting":False}), "repair_execution_authority_laundered"),
    ("nonatomic_execution", lambda c: c["configuration_repair_execution_theorems"][0].update({"execution_semantics":"compare_then_later_apply"}), "repair_execution_nonatomic_or_unverified"),
    ("postcheck_omitted", lambda c: c["configuration_repair_execution_theorems"][0].update({"postcondition":"assume_selected_repair_safe"}), "repair_execution_nonatomic_or_unverified"),
    ("configuration_changed", lambda c: c["configuration_repair_execution_theorems"][0]["execution_requests"][0]["observed_hyperedge"].append(["h2","admin_E"]), "repair_execution_request_mismatch"),
    ("different_repair_requested", lambda c: c["configuration_repair_execution_theorems"][0]["execution_requests"][0].update({"requested_repair":[["h0","admin_C"]]}), "repair_execution_request_mismatch"),
    ("capability_not_consumed", lambda c: c["configuration_repair_execution_theorems"][0]["execution_requests"][0].update({"uses_after":1}), "repair_execution_request_mismatch"),
    ("bounded_scope", lambda c: c["configuration_repair_execution_theorems"][0].update({"theorem_scope":"one execution request only"}), "repair_execution_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_repair_execution(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_repair_execution_theorems"][0]["errors"]
    repair_execution_hostiles[name] = not candidate_result["passed"] and expected in errors
result["repair_execution_hostiles"] = repair_execution_hostiles
repair_decomposition_hostiles = {}
for name, mutate_decomposition, expected in (
    ("atomic_capability_split", lambda c: c["configuration_repair_execution_decomposition_theorems"][0].update({"atomic_capability_partition_authorized":True}), "repair_decomposition_authority_laundered"),
    ("subrepair_called_endpoint", lambda c: c["configuration_repair_execution_decomposition_theorems"][0].update({"decomposition_law":"every_effect_partition_inherits_endpoint_authority"}), "repair_decomposition_authority_laundered"),
    ("intermediate_authority_omitted", lambda c: c["configuration_repair_execution_decomposition_theorems"][0].update({"authorized_options":["joint_atomic_execution","untyped_staged_execution"]}), "repair_decomposition_options_untyped"),
    ("joint_option_omitted", lambda c: c["configuration_repair_execution_decomposition_theorems"][0].update({"authorized_options":["staged_execution_with_intermediate_state_authority"]}), "repair_decomposition_options_untyped"),
    ("partial_repair_claimed_safe", lambda c: c["configuration_repair_execution_decomposition_theorems"][0]["expected"].update({"all_proper_subrepairs_endpoint_unsafe":False}), "repair_decomposition_fixture_mismatch"),
    ("joint_repair_claimed_unsafe", lambda c: c["configuration_repair_execution_decomposition_theorems"][0]["expected"].update({"joint_repair_safe":False}), "repair_decomposition_fixture_mismatch"),
    ("bounded_scope", lambda c: c["configuration_repair_execution_decomposition_theorems"][0].update({"theorem_scope":"two-locus fixture only"}), "repair_decomposition_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_decomposition(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_repair_execution_decomposition_theorems"][0]["errors"]
    repair_decomposition_hostiles[name] = not candidate_result["passed"] and expected in errors
result["repair_decomposition_hostiles"] = repair_decomposition_hostiles
staged_repair_hostiles = {}
for name, mutate_staged, expected in (
    ("missing_intermediate_root", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"intermediate_state_authority_root":None}), "staged_repair_intermediate_authority_untyped"),
    ("intermediate_called_safe", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"intermediate_inherits_endpoint_safety":True}), "staged_repair_intermediate_authority_untyped"),
    ("residual_omits_target", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"residual_certificate_binding_fields":["source_configuration","applied_subrepair","remaining_subrepair"]}), "staged_repair_residual_certificate_underbound"),
    ("residual_reusable", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"residual_capability_modality":"unrestricted"}), "staged_repair_residual_certificate_underbound"),
    ("fitted_coherence", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"primitive_or_fitted_coherence_cell":True}), "staged_repair_coherence_not_generated"),
    ("wrong_coherence_source", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"coherence_cell_source":"declared_endpoint_equality"}), "staged_repair_coherence_not_generated"),
    ("duplicate_path", lambda c: c["configuration_staged_repair_path_theorems"][0]["factorization_paths"][1].update({"order":[["h0","admin_B"],["h0","admin_D"]]}), "staged_repair_path_fixture_mismatch"),
    ("path_omits_locus", lambda c: c["configuration_staged_repair_path_theorems"][0]["factorization_paths"][0].update({"order":[["h0","admin_B"]]}), "staged_repair_path_fixture_mismatch"),
    ("bounded_scope", lambda c: c["configuration_staged_repair_path_theorems"][0].update({"theorem_scope":"displayed fixture only"}), "staged_repair_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_staged(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_staged_repair_path_theorems"][0]["errors"]
    staged_repair_hostiles[name] = not candidate_result["passed"] and expected in errors
result["staged_repair_hostiles"] = staged_repair_hostiles
finite_staged_hostiles = {}
for name, mutate_finite_staged, expected in (
    ("nonprimitive_selected_repair", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"selected_primitive_repair":[["h0","admin_B"],["h0","admin_C"],["h1","admin_B"]]}), "finite_staged_selected_repair_not_primitive"),
    ("wrong_generators", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"path_generators":"arbitrary_endpoint_equalities"}), "finite_staged_generators_untyped"),
    ("involution_omitted", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"coherence_relations":["far_commutation","braid"]}), "finite_staged_coxeter_relations_incomplete"),
    ("braid_omitted", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"coherence_relations":["involution","far_commutation"]}), "finite_staged_coxeter_relations_incomplete"),
    ("wrong_completion", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"coherence_completion":"pairwise_diamonds_only"}), "finite_staged_coxeter_relations_incomplete"),
    ("fitted_higher_cells", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"primitive_or_fitted_higher_cells":True}), "finite_staged_coxeter_relations_incomplete"),
    ("intermediate_called_safe", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"intermediate_authority_kind":"safe_endpoint"}), "finite_staged_intermediate_authority_laundered"),
    ("path_count_fitted", lambda c: c["configuration_finite_staged_coherence_theorems"][0]["expected"].update({"path_count":5}), "finite_staged_coherence_fixture_mismatch"),
    ("bounded_scope", lambda c: c["configuration_finite_staged_coherence_theorems"][0].update({"theorem_scope":"three-locus fixture only"}), "finite_staged_scope_laundered"),
):
    candidate = deepcopy(contract)
    mutate_finite_staged(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["configuration_finite_staged_coherence_theorems"][0]["errors"]
    finite_staged_hostiles[name] = not candidate_result["passed"] and expected in errors
result["finite_staged_hostiles"] = finite_staged_hostiles
candidate = deepcopy(contract)
candidate["configuration_path_coherence_audits"] = []
candidate_result = compile_contract(candidate, legacy)
coherence_omission_rejected = not candidate_result["passed"] and "configuration_coherence_required_pair_uncovered" in candidate_result["configuration_coherence_coverage"][0]["errors"]
result["configuration_coherence_omission_rejected"] = coherence_omission_rejected
out = S / "results" / "dpc_core_normalizer.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
for item in result["critical_pairs"]:
    print(("PASS" if item["passed"] else "FAIL") + " " + item["id"])
for item in result["normalization_cases"]:
    print(("PASS" if item["passed"] else "FAIL") + " " + item["id"])
for item in result["generated_overlaps"]:
    print(("PASS" if item["covered"] else "FAIL") + " overlap " + " / ".join(item["rules"]))
passed = sum(item["passed"] for item in result["critical_pairs"] + result["normalization_cases"])
total = len(result["critical_pairs"] + result["normalization_cases"])
print(f"SUMMARY {passed}/{total}")
print(("PASS" if missing_coverage_rejected else "FAIL") + " hostile missing_overlap_coverage")
print(("PASS" if defaulting_rejected else "FAIL") + " hostile legacy_defaulting")
print(f"LEGACY {result['legacy_projection']['importable_count']}/{result['legacy_projection']['grant_count']} core-importable")
for field, rejected in native_deletions.items():
    print(("PASS" if rejected else "FAIL") + " delete native." + field)
print(("PASS" if symbolic_epoch_enforced else "FAIL") + " native symbolic_epoch")
for field, rejected in successor_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " successor hostile." + field)
for field, rejected in attestation_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " attestation hostile." + field)
for field, rejected in tcb_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " attestation_tcb hostile." + field)
for name, rejected in execution_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " execution hostile." + name)
for item in result["trusted_base_cocircuits"]:
    print(("PASS" if item["passed"] else "FAIL") + " cocircuit." + item["primitive_failure_class"])
for name, rejected in ssa_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " resource_ssa hostile." + name)
for name, rejected in projection_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " projection hostile." + name)
for name, rejected in chain_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " successor_chain hostile." + name)
for name, rejected in reconfiguration_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " reconfiguration hostile." + name)
for name, rejected in configuration_path_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " configuration_path hostile." + name)
for edge_count, admitted in partial_composite_replay.items():
    print(("PASS" if admitted else "FAIL") + " configuration_path partial_composite." + edge_count)
for name, rejected in configuration_category_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " configuration_category hostile." + name)
for name, rejected in configuration_coherence_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " configuration_coherence hostile." + name)
for name, rejected in configuration_normalization_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " configuration_normalization hostile." + name)
for name, rejected in contextual_rewrite_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " contextual_rewrite hostile." + name)
for name, rejected in context_symmetry_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " context_symmetry hostile." + name)
for name, rejected in correlated_context_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " correlated_context hostile." + name)
for name, rejected in correlation_cocircuit_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " correlation_cocircuit hostile." + name)
for name, rejected in correlation_composition_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " correlation_composition hostile." + name)
for name, rejected in finite_fusion_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " finite_fusion hostile." + name)
for name, rejected in correlation_repair_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " correlation_repair hostile." + name)
for name, rejected in repair_selection_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " repair_selection hostile." + name)
for name, rejected in repair_execution_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " repair_execution hostile." + name)
for name, rejected in repair_decomposition_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " repair_decomposition hostile." + name)
for name, rejected in staged_repair_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " staged_repair hostile." + name)
for name, rejected in finite_staged_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " finite_staged hostile." + name)
print(("PASS" if coherence_omission_rejected else "FAIL") + " configuration_coherence hostile.omitted_required_comparison")
raise SystemExit(0 if result["passed"] and result["rule_count"] == 7 and missing_coverage_rejected and defaulting_rejected and all(native_deletions.values()) and symbolic_epoch_enforced and all(successor_hostiles.values()) and all(attestation_hostiles.values()) and all(tcb_hostiles.values()) and all(execution_hostiles.values()) and cocircuit_complete and all(ssa_hostiles.values()) and all(projection_hostiles.values()) and all(chain_hostiles.values()) and all(reconfiguration_hostiles.values()) and all(configuration_path_hostiles.values()) and all(partial_composite_replay.values()) and all(configuration_category_hostiles.values()) and all(configuration_coherence_hostiles.values()) and all(configuration_normalization_hostiles.values()) and all(contextual_rewrite_hostiles.values()) and all(context_symmetry_hostiles.values()) and all(correlated_context_hostiles.values()) and all(correlation_cocircuit_hostiles.values()) and all(correlation_composition_hostiles.values()) and all(finite_fusion_hostiles.values()) and all(correlation_repair_hostiles.values()) and all(repair_selection_hostiles.values()) and all(repair_execution_hostiles.values()) and all(repair_decomposition_hostiles.values()) and all(staged_repair_hostiles.values()) and all(finite_staged_hostiles.values()) and coherence_omission_rejected else 1)
