#!/usr/bin/env python3
"""Exact positive and hostile checks for partial authority composition."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / "research" / "strominger"
sys.path.insert(0, str(S))

from authority_grant_composition import compile_packet  # noqa: E402

CONTRACT = S / "contracts" / "authority-grant-composition.v1.json"
HOSTILES = S / "contracts" / "authority-grant-composition-hostile-fixtures.v1.json"
OUT = S / "results" / "authority_grant_composition.json"


def by_id(packet, collection, item_id):
    return next(item for item in packet[collection] if item["id"] == item_id)


def mutate(packet, mutations):
    candidate = copy.deepcopy(packet)
    for mutation in mutations:
        by_id(candidate, mutation["collection"], mutation["id"])[mutation["field"]] = mutation["value"]
    return candidate


def codes(compiled):
    return {item["code"] for item in compiled["errors"]}


def main():
    packet = json.loads(CONTRACT.read_text(encoding="ascii"))
    hostile_spec = json.loads(HOSTILES.read_text(encoding="ascii"))
    compiled = compile_packet(packet)

    hostile_results = {}
    for fixture in hostile_spec["fixtures"]:
        result = compile_packet(mutate(packet, fixture["mutations"]))
        expected = fixture["expected_code"]
        hostile_results[fixture["id"]] = {
            "description": fixture["description"],
            "valid": result["valid"],
            "expected_code": expected,
            "error_codes": sorted(codes(result)),
            "passed": not result["valid"] and expected in codes(result),
        }

    grants = {item["id"]: item for item in packet["authority_grants"]}
    compositions = {item["id"]: item for item in packet["compositions"]}
    cases = {item["id"]: item for item in packet["application_cases"]}
    transformations = {item["id"]: item for item in packet["transformations"]}

    left_result = grants[compositions["c_AC_CD"]["result"]]
    right_result = grants[compositions["c_AB_BD"]["result"]]
    result_signature = lambda grant: (
        grant["source_object"], grant["target_operation"], grant["target_object"],
        grant["authority_kind"], grant["evidence_domain"], grant["variance"],
    )

    gates = {
        "standalone_contract_compiles": compiled["valid"],
        "identity_laws_declared_twice": len(packet["identity_laws"]) == 2,
        "associativity_holds_on_typed_domain": result_signature(left_result) == result_signature(right_result)
            and packet["associativity_cells"][0]["coherence_defect"] == 0,
        "composition_preserves_authority_kind": all(
            len({grants[c["left"]]["authority_kind"], grants[c["right"]]["authority_kind"], grants[c["result"]]["authority_kind"]}) == 1
            for c in packet["compositions"]
        ),
        "transport_requires_authority_preservation": transformations["chart_transport"]["preserves_authority"],
        "theta_requires_explicit_seam_cell": cases["grothendieck_folded_theta"]["classification"] == "coherence_cell_required"
            and cases["grothendieck_folded_theta"]["explicit_coherence_cell"] == "moving-endpoint seam current plus reciprocal reflection",
        "theta_composite_remains_readout": cases["grothendieck_folded_theta"]["authority_result"] == "readout only",
        "kitaev_has_no_composable_physical_authority": cases["kitaev_logical_to_five_rail"]["classification"] == "no_composable_authority_map"
            and cases["kitaev_logical_to_five_rail"]["composition"] is None,
        "kitaev_rail_base_change_preserves_evidence_not_authority": transformations["rail_base_change"]["preserves_evidence"]
            and not transformations["rail_base_change"]["preserves_authority"],
        "all_hostiles_rejected": all(item["passed"] for item in hostile_results.values()),
    }
    passed = all(gates.values())
    payload = {
        "schema": "marici.authority-grant-composition-checks.v1",
        "passed": passed,
        "passed_gates": sum(gates.values()),
        "total_gates": len(gates),
        "gates": gates,
        "hostile_passed": sum(item["passed"] for item in hostile_results.values()),
        "hostile_total": len(hostile_results),
        "hostile": hostile_results,
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "hostile_fixture_sha256": hashlib.sha256(HOSTILES.read_bytes()).hexdigest(),
        "application_classification": {
            "grothendieck_folded_theta": "authority square commutes only with the explicit moving-endpoint seam/reflection coherence cell; result remains readout authority",
            "kitaev_logical_to_five_rail": "no composable authority map; conditional logical synthesis and rail-support evidence do not supply native coupler authority or encoded intertwining",
        },
        "verdict": "Authority grants form a partial category only on matching authority kind, variance, endpoints, and evidenced domains. Transport preserves kind, intersection restricts domains, extension requires fresh authority, and triple composition requires an explicit zero-defect coherence cell.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii")
    for name, value in gates.items():
        print(f"{'PASS' if value else 'FAIL'} gate.{name}: {value}")
    for name, value in hostile_results.items():
        print(f"{'PASS' if value['passed'] else 'FAIL'} hostile.{name}: {value['error_codes']}")
    print(f"SUMMARY {sum(gates.values())}/{len(gates)}; HOSTILE {sum(x['passed'] for x in hostile_results.values())}/{len(hostile_results)}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
