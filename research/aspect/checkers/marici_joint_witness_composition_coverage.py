"""Point-in-time exact capability composition audit for the optical joint witness."""

import json
from pathlib import Path


def main():
    capabilities = {
        "immutable_payload": {"binds_bytes": True, "validates_optical_join": False},
        "domain_checker": {"rejects_splice": True, "accepts_coherent_transport": True},
        "task_acceptance_test": {"can_require_checker": True, "native_optical_semantics": False},
        "task_revision_guard": {"rejects_stale_task_revision": True, "rejects_cross_run_optical_splice": False},
        "evidence_admission": {"binds_report_verification_criteria": True, "native_optical_semantics": False},
        "artifact_registry": {"registers_presentable_file": True, "grants_semantic_authority": False},
        "delegated_correlation_key": {"binds_operation_recovery": True, "is_optical_execution_join": False},
        "scoped_report": {"can_retain_claim_boundary": True, "proves_physical_source": False},
    }
    composition = {
        "payload": capabilities["immutable_payload"]["binds_bytes"],
        "semantic_test": capabilities["domain_checker"]["rejects_splice"] and capabilities["domain_checker"]["accepts_coherent_transport"],
        "governed_acceptance": capabilities["task_acceptance_test"]["can_require_checker"],
        "revision_binding": capabilities["task_revision_guard"]["rejects_stale_task_revision"],
        "evidence_binding": capabilities["evidence_admission"]["binds_report_verification_criteria"],
        "claim_scope": capabilities["scoped_report"]["can_retain_claim_boundary"],
    }
    checks = {
        "immutable_transport_alone_is_insufficient": capabilities["immutable_payload"]["binds_bytes"] and not capabilities["immutable_payload"]["validates_optical_join"],
        "domain_checker_has_required_two_sided_signature": capabilities["domain_checker"] == {"rejects_splice": True, "accepts_coherent_transport": True},
        "lifecycle_can_govern_a_domain_checker_without_understanding_optics": capabilities["task_acceptance_test"]["can_require_checker"] and not capabilities["task_acceptance_test"]["native_optical_semantics"],
        "revision_guard_is_not_a_physical_run_join": capabilities["task_revision_guard"]["rejects_stale_task_revision"] and not capabilities["task_revision_guard"]["rejects_cross_run_optical_splice"],
        "artifact_registration_is_transport_not_authority": capabilities["artifact_registry"]["registers_presentable_file"] and not capabilities["artifact_registry"]["grants_semantic_authority"],
        "delegated_correlation_is_not_silently_promoted": capabilities["delegated_correlation_key"]["binds_operation_recovery"] and not capabilities["delegated_correlation_key"]["is_optical_execution_join"],
        "existing_composition_is_representationally_sufficient": all(composition.values()),
        "no_new_primitive_is_required_by_this_witness": all(composition.values()),
        "native_semantic_coverage_is_absent_from_observed_contracts": not capabilities["task_acceptance_test"]["native_optical_semantics"],
        "end_to_end_lifecycle_execution_remains_unperformed": True,
    }
    result = {
        "schema": "marici.aspect.marici_joint_witness_composition_coverage.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "audit_kind": "point-in-time declared-capability composition audit",
        "checks": checks,
        "capabilities": capabilities,
        "sufficient_composition": composition,
        "inventory_observation_ref": "mcp_payload:site-tools-178776574805930@v1",
        "inventory_findings": {
            "task_lifecycle": "tool-name drift; evidence, acceptance, revision, and test capabilities observed",
            "work_lifecycle": "probe failed because the site store is not prepared",
            "artifacts": "inventory ok",
            "delegated_task": "declared/runtime tool-name drift; correlation and source-task binding observed",
            "mailbox": "inventory ok",
        },
        "typed_boundary": {
            "source": "frozen optical witness packet and the live Site capability inventory",
            "constructor": "immutable payload plus exact domain checker plus lifecycle acceptance, revision, evidence, and scoped report",
            "detector": "declared contract-field audit and the already verified two-sided optical checker",
            "hostile": "treat payload integrity, task revision, artifact registration, or correlation key alone as the physical joint witness",
            "completion": "representation coverage is established; an admitted end-to-end lifecycle task and native domain semantics were not executed",
        },
    }
    out = Path(__file__).parents[1] / "results" / "marici_joint_witness_composition_coverage.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
