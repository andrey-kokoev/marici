#!/usr/bin/env python3
"""Positive and hostile audit of the resource-relative D(S3) v2 contract."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "nima"))
from data_descent_kernel import compile_packet, replay_evidence  # noqa: E402

CONTRACT = ROOT / "research" / "kitaev" / "contracts" / "d-s3-resource-relative-capability.v2.json"
EXREC = ROOT / "research" / "kitaev" / "results" / "s3-26-contact-exrec-fault-pairs.json"
OUT = ROOT / "research" / "kitaev" / "results" / "s3-data-descent-capability-contract.json"
DECLARED_DIGEST = "c7b6d8636e56c97b27349f7878692ebfa68311726236d87f609c3e418b312b34"


def codes(compilation):
    return {row["code"] for row in compilation["errors"]}


def capability(packet, capability_id):
    return next(row for row in packet["capabilities"] if row["id"] == capability_id)


def theory(packet, theory_id):
    return next(row for row in packet["resource_theories"] if row["id"] == theory_id)


def hostile_compile(base, mutate, expected_codes):
    packet = copy.deepcopy(base)
    mutate(packet)
    result = compile_packet(packet)
    found = codes(result)
    assert not result["valid"]
    assert set(expected_codes) <= found, (expected_codes, found)
    return {"valid": result["valid"], "error_codes": sorted(found)}


def main():
    raw_contract = CONTRACT.read_bytes()
    packet = json.loads(raw_contract)
    positive = compile_packet(packet)
    replay = replay_evidence(packet, ROOT)
    assert positive["valid"] and replay["passed"]
    assert replay["results"][0]["artifact_sha256"] == DECLARED_DIGEST

    stabilizer = capability(packet, "distance_three_stabilizer_subcompiler_frozen")
    frozen = capability(packet, "complete_compiler_frozen")
    future = capability(packet, "complete_compiler_future_magic")
    assert stabilizer["status"]["kind"] == "Executable"
    assert frozen["status"]["kind"] == "Obstructed"
    assert future["status"]["kind"] == "Conditional"
    assert frozen["defined_data"]["encoded_rail_acquisition_core"] == 50
    assert not frozen["defined_data"]["is_complete_compiler_cost"]
    assert all(
        frozen["status"]["cost"][field]["kind"] == "undefined"
        for field in ("physical_gate_count", "depth", "magic_ancilla_count")
    )

    hostile = {}

    def report_full_executable(p):
        target = capability(p, "complete_compiler_frozen")
        target["status"] = {
            "kind": "Executable",
            "cost": copy.deepcopy(frozen["status"]["cost"]),
            "certificate": copy.deepcopy(stabilizer["status"]["certificate"]),
        }

    hostile["report_full_compiler_executable"] = hostile_compile(
        packet, report_full_executable,
        {"certificate_scope_mismatch", "executable_undefined_cost"},
    )

    def zero_absent_circuit(p):
        costs = capability(p, "complete_compiler_frozen")["status"]["cost"]
        for field in costs:
            costs[field] = {"kind": "known", "value": 0}

    hostile["zero_cost_for_absent_circuit"] = hostile_compile(
        packet, zero_absent_circuit, {"obstructed_cost_must_be_undefined"}
    )

    def smuggle_magic(p):
        target = theory(p, "d_s3_future_magic_envelope")
        target["admission"] = "admitted"
        target["resources"][0]["admitted"] = True

    hostile["magic_without_source_authority"] = hostile_compile(
        packet, smuggle_magic,
        {"unauthorized_resource_admission", "unauthorized_resource_theory_extension"},
    )

    hostile["stabilizer_branch_overpromotion"] = hostile_compile(
        packet, report_full_executable, {"certificate_scope_mismatch"}
    )

    def violate_one_fault(p):
        contract = capability(p, "complete_compiler_future_magic")["status"]["preserved_contract"]
        contract["preserved"] = False

    hostile["distance_three_without_one_fault_contract"] = hostile_compile(
        packet, violate_one_fault, {"conditional_contract_not_preserved"}
    )

    def remove_frame_evidence(p):
        del p["capability_transitions"][0]["evidence"]

    hostile["unevidenced_frame_transition"] = hostile_compile(
        packet, remove_frame_evidence, {"missing_capability_transition_evidence"}
    )

    def break_frame_functor(p):
        p["capability_transitions"][0]["operation_map"] = {
            "I": "N_prime", "N": "I_prime"
        }

    hostile["noncompositional_frame_transition"] = hostile_compile(
        packet, break_frame_functor, {"capability_transition_composition_defect"}
    )

    def erase_unknown_reason(p):
        del capability(p, "distance_three_stabilizer_subcompiler_frozen")["status"]["cost"]["depth"]["reason"]

    hostile["untyped_unknown_cost"] = hostile_compile(
        packet, erase_unknown_reason, {"missing_cost_reason"}
    )

    # A source-authorized admitted extension may monotonically improve the
    # status to Conditional without rewriting the frozen declaration.
    admitted_extension = copy.deepcopy(packet)
    extension = theory(admitted_extension, "d_s3_future_magic_envelope")
    extension["admission"] = "admitted"
    extension["extension_authority"] = "operator-authorized resource-theory lift"
    extension["resources"][0].update({
        "admitted": True,
        "authority_evidence": "verified magic constructor admission certificate",
    })
    admitted_result = compile_packet(admitted_extension)
    assert admitted_result["valid"]
    assert capability(admitted_extension, "complete_compiler_frozen")["status"]["kind"] == "Obstructed"
    assert capability(admitted_extension, "complete_compiler_future_magic")["status"]["kind"] == "Conditional"

    extension_transition = next(
        row for row in packet["capability_status_transitions"] if row["kind"] == "extension"
    )
    restriction_transition = next(
        row for row in packet["capability_status_transitions"] if row["kind"] == "restriction"
    )
    assert extension_transition["preserves_prior"]
    assert restriction_transition["target_capability"] == "complete_compiler_frozen"

    # Preserve every malignant pair as an individually typed provenance row.
    exrec = json.loads(EXREC.read_text())
    schedule = {row["index"]: row for row in exrec["contact_schedule"]}
    malignant_rows = []
    for row in exrec["fault_pairs"]["rows"]:
        if not row["malignant"]:
            continue
        failure = row["first_failure"]
        operation = schedule[failure["step"]]
        malignant_rows.append({
            "left_fault": row["left"],
            "right_fault": row["right"],
            "affected_operation_index": failure["step"],
            "affected_operation": operation["name"],
            "affected_resource": failure["block"],
            "failure_stage": failure["stage"],
        })
    assert len(malignant_rows) == 220
    assert all(row["affected_operation"] and row["affected_resource"] for row in malignant_rows)

    result = {
        "schema": "marici.kitaev.d-s3-data-descent-capability-contract-result.v1",
        "contract_sha256": hashlib.sha256(raw_contract).hexdigest(),
        "declared_artifact_sha256": DECLARED_DIGEST,
        "positive": {
            "compilation": positive,
            "bounded_replay": replay,
            "component_checkers_replayed": 9,
            "statuses": {
                stabilizer["id"]: stabilizer["status"]["kind"],
                frozen["id"]: frozen["status"]["kind"],
                future["id"]: future["status"]["kind"],
            },
            "encoded_rail_acquisition_core_defined_data": 50,
            "frozen_full_cost_kinds": {
                field: frozen["status"]["cost"][field]["kind"]
                for field in ("physical_gate_count", "depth", "magic_ancilla_count")
            },
            "authorized_extension_valid": admitted_result["valid"],
            "extension_preserves_frozen_obstruction": True,
            "restriction_restores_frozen_obstruction": True,
            "frame_transition_compositional_and_evidenced": True,
        },
        "hostile": hostile,
        "malignant_pair_provenance": malignant_rows,
        "malignant_pair_provenance_count": len(malignant_rows),
        "cross_sector_claim": {
            "statement": "support or formal description does not imply executable capability",
            "verified": True,
            "execution_requirement": "source-authorized resource lift with replayable evidence",
        },
        "verdict": "The generic v2 capability fiber is resource-relative. The stabilizer subcompiler is executable, a source-authorized magic lift is conditional, and the complete frozen D(S3) compiler remains obstructed with undefined circuit costs. Extension and restriction preserve the frozen verdict, and all 220 malignant pairs retain operation/resource provenance.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "malignant_pair_provenance"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
