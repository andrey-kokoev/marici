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
raise SystemExit(0 if result["passed"] and result["rule_count"] == 7 and missing_coverage_rejected and defaulting_rejected and all(native_deletions.values()) and symbolic_epoch_enforced else 1)
