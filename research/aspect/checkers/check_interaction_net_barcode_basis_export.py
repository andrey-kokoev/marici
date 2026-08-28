#!/usr/bin/env python3
"""Readiness and hostile audit for the sparse barcode-basis export."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ASPECT = ROOT / "research" / "aspect"
CONTRACT = ASPECT / "contracts" / "interaction-net-barcode-basis-export.v1.json"
RESULT = ASPECT / "results" / "interaction_net_barcode_basis_export.json"

def rank(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, pivot = len(a), len(a[0]), 0
    for col in range(cols):
        hit = next((r for r in range(pivot, rows) if a[r][col]), None)
        if hit is None:
            continue
        a[pivot], a[hit] = a[hit], a[pivot]
        inv = pow(a[pivot][col], -1, prime)
        a[pivot] = [(x * inv) % prime for x in a[pivot]]
        for r in range(rows):
            if r != pivot and a[r][col]:
                factor = a[r][col]
                a[r] = [(a[r][j] - factor * a[pivot][j]) % prime for j in range(cols)]
        pivot += 1
        if pivot == rows:
            break
    return pivot

def matvec(matrix, vector, prime):
    return [sum(a * b for a, b in zip(row, vector)) % prime for row in matrix]

def synthetic_hostile_audit():
    p = 101
    # Five source coordinates: two first deaths, one second death, two survivors.
    t4 = [[0,0,0,1,0], [0,0,0,0,1], [0,0,1,0,0]]
    t5 = [[0,0,0,1,0], [0,0,0,0,1]]
    first = [[1,0,0,0,0], [0,1,0,0,0]]
    second = [[0,0,1,0,0]]
    survive = [[0,0,0,1,0], [0,0,0,0,1]]
    return {
        "rank_pattern": [rank(t4,p), rank(t5,p)] == [3,2],
        "first_deaths_in_kernel_t4": all(matvec(t4,row,p) == [0,0,0] for row in first),
        "second_death_survives_t4": matvec(t4,second[0],p) != [0,0,0],
        "second_death_in_kernel_t5": matvec(t5,second[0],p) == [0,0],
        "survivors_independent": rank(survive,p) == 2,
        "wrong_block_assignment_detected": matvec(t4,survive[0],p) != [0,0,0]
    }

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    export_path = ROOT / contract["expected_locator"]
    hostiles = synthetic_hostile_audit()
    export_present = export_path.exists()
    if export_present:
        packet = json.loads(export_path.read_text(encoding="utf-8"))
        required = {
            "schema", "prime", "source_label_order_depth3", "source_label_order_depth4",
            "adapted_depth3_quotient_basis", "depth4_emergence_complement_rows",
            "transition_matrices", "dual_pairing_matrices", "chart_transports"
        }
        export_shape_valid = required <= set(packet) and packet["prime"] == contract["field_prime"]
        status = "export_present_shape_valid" if export_shape_valid else "export_present_shape_invalid"
    else:
        export_shape_valid = None
        status = "awaiting_source_export"
    passed = all(hostiles.values()) and (not export_present or export_shape_valid)
    out = {
        "schema": "marici.aspect.interaction-net-barcode-basis-export-result.v1",
        "passed": passed,
        "export_present": export_present,
        "export_shape_valid": export_shape_valid,
        "status": status,
        "synthetic_hostiles": hostiles,
        "scientific_conclusion": "no_optical_compilation_until_source_labelled_basis_export_is_present"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
