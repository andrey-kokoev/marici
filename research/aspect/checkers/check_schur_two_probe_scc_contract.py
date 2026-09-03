#!/usr/bin/env python3
"""Validate the SCC-facing Schur two-probe contract and source digests."""

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACT_PATH = ROOT / "research/aspect/contracts/schur-two-probe-scc-cell.v1.json"
contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

source_digests = {}
for source in contract["sources"]:
    path = ROOT / source["path"]
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    source_digests[source["path"]] = actual
    assert actual == source["sha256"], (path, actual, source["sha256"])

fixture = {key: Q(value) for key, value in contract["exact_fixture"].items()}
A, B, C, E = fixture["A"], fixture["B"], fixture["C"], fixture["E"]
Ap, Bp, Cp, Ep = fixture["A_prime"], fixture["B_prime"], fixture["C_prime"], fixture["E_prime"]
joint = E - C / A * B
cross_effect = joint - E - E + E
joint_prime = Ep - Cp / A * B + C / A * Ap / A * B - C / A * Bp

fixture_ids = {item["id"] for item in contract["hostile_fixtures"]}
checks = {
    "four_typed_ports_declared": set(contract["ports"]) == {"retained_response", "entry_incidence", "exit_incidence", "local_response"},
    "all_four_configurations_declared": set(contract["configurations"]) == {"empty", "entry_only", "exit_only", "joint"},
    "joint_fixture_matches": joint == fixture["joint"],
    "cross_effect_fixture_matches": cross_effect == fixture["cross_effect"],
    "first_jet_fixture_matches": joint_prime == fixture["joint_first_jet"],
    "required_hostiles_present": fixture_ids == {"erase_entry", "erase_exit", "noninvertible_retained", "local_shadow"},
    "source_digests_match": len(source_digests) == 3,
    "live_scc_admission_not_claimed": "not_admitted_into_live_scc_registry" in contract["nonclaims"],
    "deformation_coordinate_not_temporal": contract["deformation_coordinate_has_temporal_meaning"] is False,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.schur-two-probe-scc-contract-check.v1",
    "status": "passed",
    "checks": checks,
    "source_digests": source_digests,
    "computed": {"joint": str(joint), "cross_effect": str(cross_effect), "joint_first_jet": str(joint_prime)},
    "claim_boundary": "SCC-facing contract validation only; the live SCC registry is unchanged."
}
output = ROOT / "research/aspect/results/schur_two_probe_scc_contract.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
