#!/usr/bin/env python3
"""Reject the naive double-soft square as a physical-coupling necessity test."""

from __future__ import annotations

import json
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
MARICI = NIMA.parents[1]
BENINCASA = MARICI / "research" / "benincasa"
RESULT = NIMA / "results" / "double-soft-coupling-necessity-candidate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    leray = load(NIMA / "results" / "double-soft-leray-local-constructor.json")
    tensor = load(NIMA / "results" / "double-soft-transverse-tensor-explanation.json")
    primary = load(BENINCASA / "soft-support-nine-master-certificate.json")
    replication = load(BENINCASA / "soft-support-nine-master-replication-certificate.json")

    checks = {
        "local_double_leray_constructor_exists": bool(leray["local_constructor_exists"]),
        "global_source_to_norm_comparison_absent": not bool(
            leray["global_source_to_norm_comparison_exists"]
        ),
        "physical_supported_tensor_not_admitted": not bool(
            tensor["physical_supported_tensor_admitted"]
        ),
        "primary_supported_extension_zero": bool(
            primary["full_nine_master_supported_extension_zero"]
        ),
        "replication_supported_extension_zero": bool(
            replication["full_nine_master_supported_extension_zero"]
        ),
        "independent_primes": primary["prime"] != replication["prime"],
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.double-soft-coupling-necessity-candidate.v1",
        "status": "pass",
        "candidate_classification": "rejected_before_defect_test",
        "reason": (
            "The local double-Leray object exists, but no global physical "
            "comparison/tensor is admitted; the independent nine-master "
            "supported-extension controls are zero."
        ),
        "conjecture_update": (
            "The naive double-soft square supplies no evidence of coupling "
            "necessity. Search must move to a source-defined CM relative "
            "boundary composition, not another soft coefficient quotient."
        ),
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
