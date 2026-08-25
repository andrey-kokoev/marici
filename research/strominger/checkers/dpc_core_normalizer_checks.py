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
dynamic_reconfiguration_hostiles = {}
dynamic_reconfiguration_mutations = (
    ("predecessor_link", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["old_configuration"].update({"authority_resource":"cfg_auth_stale"}), "dynamic_reconfiguration_predecessor_link_failure"),
    ("epoch_gap", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["new_configuration"]["epoch"].update({"offset":3}), "dynamic_reconfiguration_nonadjacent_epoch"),
    ("unrealized_physical_step", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["physical_successor"].update({"realized":False}), "dynamic_reconfiguration_physical_correspondence_failure"),
    ("missing_joint_endorsement", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1].update({"new_quorum_endorsement":["r3","r4"]}), "dynamic_reconfiguration_joint_endorsement_failure"),
    ("empty_bridge", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["new_configuration"].update({"members":["r5","r6","r7"],"quorum":["r5","r6","r7"]}), "dynamic_reconfiguration_invalid_configuration_bridge"),
    ("whole_bridge_fault", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["admissible_bridge_fault_sets"].append(["r3","r4"]), "dynamic_reconfiguration_bridge_fault_unsafe"),
    ("common_cause_omitted", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1].update({"admissible_bridge_fault_sets":[["r3"]]}), "dynamic_reconfiguration_common_cause_omitted"),
    ("correlated_roots_unmodelled", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1].update({"bridge_authority_roots":{"r3":"admin_C","r4":"admin_C"}}), "dynamic_reconfiguration_common_cause_omitted"),
    ("global_root_omitted", lambda c: c["dynamic_reconfiguration_chain_audits"][0].update({"admissible_authority_root_fault_sets":[["admin_B"],["admin_C"],["admin_E"]]}), "dynamic_reconfiguration_global_root_fault_omitted"),
    ("global_correlated_fault", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["admissible_authority_root_fault_sets"].append(["admin_C","admin_D"]), "dynamic_reconfiguration_global_fault_unsafe"),
    ("authority_reuse", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["output_configuration"].update({"authority_resource":"cfg_auth_0"}), "dynamic_reconfiguration_linear_replacement_failure"),
    ("predecessor_retained", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1].update({"old_authority_retained":True,"live_authority_count_after":2}), "dynamic_reconfiguration_linear_replacement_failure"),
    ("support_drop", lambda c: c["dynamic_reconfiguration_chain_audits"][0]["steps"][1]["output_configuration"].update({"support":["charter_2","physical_2","proposal_2"]}), "dynamic_reconfiguration_support_not_monotone"),
)
for name, mutate_dynamic, expected in dynamic_reconfiguration_mutations:
    candidate = deepcopy(contract)
    mutate_dynamic(candidate)
    candidate_result = compile_contract(candidate, legacy)
    errors = candidate_result["dynamic_reconfiguration_chains"][0]["errors"]
    dynamic_reconfiguration_hostiles[name] = not candidate_result["passed"] and expected in errors
result["dynamic_reconfiguration_hostiles"] = dynamic_reconfiguration_hostiles
dynamic_prefix_replay = {}
base_dynamic_chain = contract["dynamic_reconfiguration_chain_audits"][0]
for prefix_length in range(1, len(base_dynamic_chain["steps"]) + 1):
    candidate = deepcopy(contract)
    candidate_chain = candidate["dynamic_reconfiguration_chain_audits"][0]
    candidate_chain["steps"] = candidate_chain["steps"][:prefix_length]
    candidate_chain["expected_terminal_configuration"] = deepcopy(candidate_chain["steps"][-1]["output_configuration"])
    candidate_result = compile_contract(candidate, legacy)
    dynamic_prefix_replay[str(prefix_length)] = candidate_result["dynamic_reconfiguration_chains"][0]["passed"]
result["dynamic_reconfiguration_prefix_replay"] = dynamic_prefix_replay
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
for name, rejected in dynamic_reconfiguration_hostiles.items():
    print(("PASS" if rejected else "FAIL") + " dynamic_reconfiguration hostile." + name)
for length, admitted in dynamic_prefix_replay.items():
    print(("PASS" if admitted else "FAIL") + " dynamic_reconfiguration prefix." + length)
raise SystemExit(0 if result["passed"] and result["rule_count"] == 7 and missing_coverage_rejected and defaulting_rejected and all(native_deletions.values()) and symbolic_epoch_enforced and all(successor_hostiles.values()) and all(attestation_hostiles.values()) and all(tcb_hostiles.values()) and all(execution_hostiles.values()) and cocircuit_complete and all(ssa_hostiles.values()) and all(projection_hostiles.values()) and all(chain_hostiles.values()) and all(reconfiguration_hostiles.values()) and all(dynamic_reconfiguration_hostiles.values()) and all(dynamic_prefix_replay.values()) else 1)
