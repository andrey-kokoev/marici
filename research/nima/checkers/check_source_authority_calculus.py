"""Cross-sector checks for completion, authority, and conditioned reliability."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "nima"))

from data_descent_kernel import compile_packet  # noqa: E402


PACKETS = {
    "magnetic": ROOT / "research/strominger/contracts/magnetic-generic-completion.v1.json",
    "theta": ROOT / "research/strominger/contracts/grothendieck-theta-completion-test.v1.json",
    "topological": ROOT / "research/kitaev/contracts/d-s3-resource-relative-capability.v2.json",
    "flavor": ROOT / "research/flavor/contracts/flavor-uv-ensemble-data-descent.v2.json",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def codes(packet: dict) -> set[str]:
    return {item["code"] for item in compile_packet(packet)["errors"]}


authority_packet = load(ROOT / "research/nima/contracts/source-authority-reliability.v1.json")


positive = {name: compile_packet(load(path)) for name, path in PACKETS.items()}
positive["authority_reliability"] = compile_packet(authority_packet)

hostile: dict[str, dict] = {}

case = copy.deepcopy(load(PACKETS["magnetic"]))
case["completion_interfaces"][0]["constructor_kind"] = "ordinary_base_change"
hostile["completion_erasure"] = compile_packet(case)

case = copy.deepcopy(load(PACKETS["magnetic"]))
case["kernel_comparisons"][0]["class_groups"][0]["tor_object"] = "invented_tor"
hostile["ordinary_kernel_mistyped_as_derived"] = compile_packet(case)

case = copy.deepcopy(load(PACKETS["magnetic"]))
case["finite_linear_observation_fibers"][0]["ports"][0]["availability"] = "unavailable"
hostile["unavailable_port_as_zero"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["authority_grants"].append({
    "id": "faithfulness_selector",
    "source_authority": "physical16_probe",
    "authority_kind": "selector",
    "subject": "physical flavor state",
    "evidence": "hostile attempted promotion",
})
hostile["faithfulness_promoted_to_selector"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["authority_grants"].append({
    "id": "rank60_observer",
    "source_authority": "cosmology_rank60",
    "authority_kind": "observer",
    "subject": "physical cosmology contour",
    "evidence": "hostile attempted promotion",
})
hostile["algebraic_cosmology_promoted_to_observer"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["conditioned_reliability_certificates"][0]["gamma"] = "0"
hostile["zero_margin_reliability"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["authority_transports"] = [{
    "id": "readout_to_selector",
    "source_grant": "thermal_readout",
    "target_authority_kind": "selector",
    "evidence": "hostile transport",
}]
hostile["authority_upgrade_by_transport"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["source_relative_capability_audits"][0]["verification_model"]["id"] = "logical_nonlinear_compiler"
hostile["producer_is_its_own_verifier"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["source_relative_capability_audits"][0]["counterfactual"]["removes_descendants"] = False
hostile["counterfactual_retains_descendants"] = compile_packet(case)

case = copy.deepcopy(authority_packet)
case["source_relative_capability_audits"][0]["claims_universal_law"] = True
hostile["bounded_audit_promoted_to_metaphysics"] = compile_packet(case)

expected = {
    "completion_erasure": "completion_as_ordinary_base_change",
    "ordinary_kernel_mistyped_as_derived": "completion_only_class_mistyped",
    "unavailable_port_as_zero": "unavailable_port_is_not_zero_port",
    "faithfulness_promoted_to_selector": "unauthorized_authority_promotion",
    "algebraic_cosmology_promoted_to_observer": "unauthorized_authority_promotion",
    "zero_margin_reliability": "nonpositive_reliability_margin",
    "authority_upgrade_by_transport": "authority_transport_upgrade",
    "producer_is_its_own_verifier": "producer_verifier_conflation",
    "counterfactual_retains_descendants": "counterfactual_leaves_resource_descendants",
    "bounded_audit_promoted_to_metaphysics": "bounded_audit_promoted_to_universal_law",
}

checks = {
    "positive_packets_compile": all(item["valid"] for item in positive.values()),
    "hostile_packets_rejected": all(not item["valid"] for item in hostile.values()),
    "hostile_codes_exactly_witnessed": all(
        code in {error["code"] for error in hostile[name]["errors"]}
        for name, code in expected.items()
    ),
    "cosmology_withheld": not any(
        grant.get("source_authority") == "cosmology_rank60"
        for grant in authority_packet["authority_grants"]
    ),
}

result = {
    "schema": "marici.source-authority-calculus-result.v1",
    "positive": positive,
    "hostile": hostile,
    "expected_hostile_codes": expected,
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "verdict": (
        "Completion, operational authority, conditioned reliability, and resource-relative "
        "capability compile across sectors without promoting algebraic evidence to physical authority."
    ),
}

out = ROOT / "research/nima/results/source_authority_calculus.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
