#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json"
RESULT = ROOT / "research/aspect/results/relative_cech_de_rham_interferometer.json"


def rank_mod(matrix, p):
    if not matrix:
        return 0
    a = [list(map(lambda x: x % p, row)) for row in matrix]
    rows, cols, rank = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                f = a[r][col]
                a[r] = [(x - f * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def in_column_span(columns, target, p):
    if not columns:
        return False
    matrix = [list(row) for row in zip(*columns)]
    augmented = [row + [target[i]] for i, row in enumerate(matrix)]
    return rank_mod(matrix, p) == rank_mod(augmented, p)


def main():
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    target = c["target_relative_cocycle"]
    residue = c["residue_map"]
    assert [sum(row[i] * target[i] for i in range(2)) for row in residue] == [0, 0, 0]
    primes = [101, 103]
    checks = {}
    for regime in c["regimes"]:
        rid = regime["id"]
        spans = {str(p): in_column_span(regime["incoming_columns"], target, p) for p in primes}
        if rid == "residue_cancellation_without_total_lift":
            passed = not any(spans.values())
        elif rid == "sourced_exceptional_total_lift":
            passed = all(spans.values()) and not c["source_authority_gate"]["currently_constructed"]
        else:
            passed = not all(spans.values()) or regime.get("force_target_zero", False) or not regime.get("coherent", True)
        checks[rid] = {"passed": passed, "target_in_incoming_span": spans}
    readout_ranks = {
        name: {str(p): rank_mod(matrix, p) for p in primes}
        for name, matrix in c["readouts"].items()
    }
    assert all(v == 1 for v in readout_ranks["scalar_dark_port"].values())
    assert all(v == 2 for v in readout_ranks["complementary_phase_sensitive"].values())
    assert all(item["passed"] for item in checks.values())
    result = {
        "schema": "marici.aspect.relative-cech-de-rham-interferometer.result.v1",
        "status": "passed",
        "simulation_only": True,
        "primes": primes,
        "residue_cocycle_closed": True,
        "readout_ranks": readout_ranks,
        "regimes": checks,
        "exceptional_constructor_source_derived": False,
        "total_lift_constructed": False,
        "global_contour_constructed": False,
        "physical_period_constructed": False
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "regimes": len(checks), "result": str(RESULT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
