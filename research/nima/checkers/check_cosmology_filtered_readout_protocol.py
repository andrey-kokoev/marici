#!/usr/bin/env python3
"""Validate the filtration-aware cosmology joint-readout falsifier."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(cols)]
        r += 1
    return r


def verdict(terminal_dimension, readouts):
    if any(item.get("matrix") is None or not item.get("typed") or not item.get("coherent") for item in readouts):
        return "inconclusive"
    stacked = [row for item in readouts for row in item["matrix"]]
    return "pass" if rank(stacked) == terminal_dimension else "fail"


def main():
    contract_path = Path(__file__).parents[1] / "contracts" / "cosmology-filtered-readout-falsifier.v2.json"
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    assert contract["schema"].endswith(".v2")
    assert [s["domain_dimension"] - s["required_rank"] for s in contract["stages"]] == [9, 7]
    assert contract["terminal_domain"]["dimension"] == 7

    positive = [
        {"matrix": [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0]], "typed": True, "coherent": True},
        {"matrix": [[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]], "typed": True, "coherent": True},
    ]
    negative = [
        {"matrix": [[1,0,0,0,0,0,0]], "typed": True, "coherent": True},
        {"matrix": [[0,1,0,0,0,0,0]], "typed": True, "coherent": True},
    ]
    current = [{"matrix": None, "typed": False, "coherent": False} for _ in range(2)]
    assert verdict(7, positive) == "pass"
    assert verdict(7, negative) == "fail"
    assert verdict(7, current) == "inconclusive"

    result_path = Path(__file__).parents[1] / "results" / "cosmology-filtered-readout-protocol-check.json"
    payload = result_path.read_text(encoding="utf-8")
    result = json.loads(payload)
    assert result == {
        "schema": "marici.cosmology-filtered-readout-protocol-check.v2",
        "filtration_dimensions": [12, 9, 7],
        "peeled_quotient_dimensions": [3, 2],
        "terminal_dimension": 7,
        "synthetic_positive": "pass",
        "synthetic_negative": "fail",
        "current": "inconclusive",
        "reason": "terminal T7 basis and source-derived nearby-cycle/physical-pairing matrices are absent"
    }
    print(json.dumps({"passed": True, "current": "inconclusive", "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
