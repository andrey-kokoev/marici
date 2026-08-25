#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / "research" / "strominger"
sys.path.insert(0, str(S))

from partial_repair_compiler import compile_contract  # noqa: E402


contract_path = S / "contracts" / "dependency-aware-partial-repairs.v1.json"
result_path = S / "results" / "dependency_aware_partial_repairs.json"
contract = json.loads(contract_path.read_text(encoding="ascii"))
result = compile_contract(contract)

hostiles = {}
for name, mutate, expected in (
    ("missing_authority_root", lambda c: c["models"][0]["repairs"][0].update({"authority_root":None}), "repair_constructor_authority_untyped"),
    ("dependency_cycle", lambda c: (c["models"][1]["repairs"][0].update({"prerequisites":["B"]}), c["models"][1]["repairs"][1].update({"prerequisites":["A"]})), "repair_dependency_cycle"),
    ("wrong_independent_path_count", lambda c: c["models"][0]["expected"].update({"linear_extension_count":5}), "model_expectation_mismatch:linear_extension_count"),
    ("wrong_precedence_path_count", lambda c: c["models"][1]["expected"].update({"linear_extension_count":6}), "model_expectation_mismatch:linear_extension_count"),
    ("scalar_bytes_claim_typed_coherence", lambda c: c["models"][2]["expected"].update({"swap_component_count":1}), "model_expectation_mismatch:swap_component_count"),
    ("graph_norm_difference_hidden", lambda c: c["models"][2]["expected"].update({"typed_endpoint_count":1}), "model_expectation_mismatch:typed_endpoint_count"),
):
    candidate = deepcopy(contract)
    mutate(candidate)
    candidate_result = compile_contract(candidate)
    errors = {error for model in candidate_result["models"] for error in model["errors"]}
    hostiles[name] = not candidate_result["passed"] and expected in errors

result["hostiles"] = hostiles
result["all_hostiles_rejected"] = all(hostiles.values())
result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")

for model in result["models"]:
    print(("PASS" if model["passed"] else "FAIL") + " model." + model["id"])
for name, passed in hostiles.items():
    print(("PASS" if passed else "FAIL") + " hostile." + name)
print(f"SUMMARY {sum(model['passed'] for model in result['models'])}/{len(result['models'])}; HOSTILE {sum(hostiles.values())}/{len(hostiles)}")
raise SystemExit(0 if result["passed"] and result["all_hostiles_rejected"] else 1)
