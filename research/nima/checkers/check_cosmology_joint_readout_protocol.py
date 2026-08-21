"""Validate the frozen cosmology joint-readout falsifier without inventing maps."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
contract_path = HERE / "contracts" / "cosmology-joint-readout-falsifier.v1.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))


def rank(rows):
    matrix = [[Fraction(x) for x in row] for row in rows]
    if not matrix:
        return 0
    nrows, ncols = len(matrix), len(matrix[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((r for r in range(pivot_row, nrows) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [x/scale for x in matrix[pivot_row]]
        for row in range(nrows):
            if row != pivot_row and matrix[row][col]:
                scale = matrix[row][col]
                matrix[row] = [x-scale*y for x, y in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def decide(packet):
    required = ["residue", "infinity_gysin", "nearby_cycle", "physical_pairing"]
    maps = {item["readout_id"]: item for item in packet["required_readouts"]}
    assert list(maps) == required
    domain = packet["domain"]
    if domain["dimension"] is None or domain["basis_id"] is None or domain["basis_digest"] is None:
        return {"status": "inconclusive", "reason": "frozen domain packet incomplete"}
    stacked = []
    for name in required:
        item = maps[name]
        fields = ("matrix", "source_locator", "source_digest", "typing_certificate", "coherence_certificate")
        if item["status"] != "admissible" or any(item[field] is None for field in fields):
            return {"status": "inconclusive", "reason": f"required readout {name} is not fully admissible"}
        if item["typing_certificate"] != "passed" or item["coherence_certificate"] != "passed":
            return {"status": "inconclusive", "reason": f"required readout {name} lacks a passing certificate"}
        assert all(len(row) == domain["dimension"] for row in item["matrix"])
        stacked.extend(item["matrix"])
    stacked_rank = rank(stacked)
    return {
        "status": "pass" if stacked_rank == domain["dimension"] else "fail",
        "domain_dimension": domain["dimension"],
        "stacked_rank": stacked_rank,
        "joint_kernel_dimension": domain["dimension"]-stacked_rank,
    }


# Deliberate protocol self-tests: a jointly conservative fixture must pass,
# while a fixture with a shared invisible direction must fail.
def fixture(rows):
    packet = json.loads(json.dumps(contract))
    packet["domain"].update({"basis_id": "synthetic", "basis_digest": "synthetic", "dimension": 2})
    for item, matrix in zip(packet["required_readouts"], rows):
        item.update({
            "status": "admissible", "matrix": matrix,
            "source_locator": "synthetic", "source_digest": "synthetic",
            "typing_certificate": "passed", "coherence_certificate": "passed",
        })
    return packet


positive = decide(fixture([[[1, 0]], [[0, 1]], [], []]))
negative = decide(fixture([[[1, 0]], [[2, 0]], [], []]))
assert positive == {"status": "pass", "domain_dimension": 2, "stacked_rank": 2, "joint_kernel_dimension": 0}
assert negative == {"status": "fail", "domain_dimension": 2, "stacked_rank": 1, "joint_kernel_dimension": 1}

current = decide(contract)
assert current == {"status": "inconclusive", "reason": "frozen domain packet incomplete"}

payload = {
    "schema": "marici.cosmology-joint-readout-protocol-check.v1",
    "contract": str(contract_path.relative_to(HERE.parent.parent)),
    "contract_sha256": hashlib.sha256(contract_path.read_bytes()).hexdigest().upper(),
    "required_readouts": [x["readout_id"] for x in contract["required_readouts"]],
    "synthetic_positive_control": positive,
    "synthetic_negative_control": negative,
    "current_decision": current,
    "interpretation": "The falsifier is frozen and operational, but no cosmology result is claimed until independently source-derived map packets fill every required field.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = HERE / "results" / "cosmology-joint-readout-protocol-check.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"protocol_valid": True, "current": current["status"], "sha256": payload["content_sha256"]}))
