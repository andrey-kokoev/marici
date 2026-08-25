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
    ("unauthorized_relation", lambda c: c["configuration_constructor_relations"][0].update({"source_authority_root":None}), "configuration_normalization", "configuration_normalization_relation_unauthorized"),
    ("word_mismatch", lambda c: c["configuration_constructor_relations"][0].update({"edge_word":["rho_01","rho_23"]}), "configuration_normalization", "configuration_normalization_word_mismatch"),
    ("duplicate_normal_form_witness", lambda c: c["configuration_constructor_relations"].append(deepcopy(c["configuration_constructor_relations"][0])), "configuration_normalization", "configuration_normalization_not_unique"),
    ("normal_form_target_fitted", lambda c: c["configuration_constructor_relations"][2].update({"normal_form_id":"NF_FITTED"}), "configuration_normalization", "configuration_normalization_target_fitted"),
    ("triangle_target_fitted", lambda c: c["configuration_coherence_triangle_audits"][0].update({"normal_form_id":"NF_FITTED"}), "configuration_coherence_triangles", "configuration_coherence_triangle_target_fitted"),
):
    candidate = deepcopy(contract)
    mutate_normalization(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = [error for audit in candidate_result[expected_section] for error in audit["errors"]]
    configuration_normalization_hostiles[name] = not candidate_result["passed"] and expected in errors
result["configuration_normalization_hostiles"] = configuration_normalization_hostiles
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
print(("PASS" if coherence_omission_rejected else "FAIL") + " configuration_coherence hostile.omitted_required_comparison")
raise SystemExit(0 if result["passed"] and result["rule_count"] == 7 and missing_coverage_rejected and defaulting_rejected and all(native_deletions.values()) and symbolic_epoch_enforced and all(successor_hostiles.values()) and all(attestation_hostiles.values()) and all(tcb_hostiles.values()) and all(execution_hostiles.values()) and cocircuit_complete and all(ssa_hostiles.values()) and all(projection_hostiles.values()) and all(chain_hostiles.values()) and all(reconfiguration_hostiles.values()) and all(configuration_path_hostiles.values()) and all(partial_composite_replay.values()) and all(configuration_category_hostiles.values()) and all(configuration_coherence_hostiles.values()) and all(configuration_normalization_hostiles.values()) and coherence_omission_rejected else 1)
