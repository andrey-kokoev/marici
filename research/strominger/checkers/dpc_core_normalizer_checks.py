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
raise SystemExit(0 if result["passed"] and result["rule_count"] == 7 and missing_coverage_rejected and defaulting_rejected and all(native_deletions.values()) and symbolic_epoch_enforced and all(successor_hostiles.values()) and all(attestation_hostiles.values()) and all(tcb_hostiles.values()) and all(execution_hostiles.values()) else 1)
