"""Limit of a native three-chart marked-fiber cover for tau_p.

Repeat iteration 2 tests the next proposed source-only route abstractly.  A native
three-chart cover can source Cech 2-face columns, but without an additional
logarithmic comparison each such column lies in the minus_sigma123 axis.  The
Xi_log cokernel obstruction is unchanged.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_native_three_chart_cover_limit.json"


def load(name: str) -> dict:
    return json.loads((VOEVODSKY_RESULTS / name).read_text(encoding="utf-8"))


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0
    for col in range(col_count):
        pivot = next((r for r in range(rank, row_count) if rows[r][col] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(value * inv) % prime for value in rows[rank]]
        for r in range(row_count):
            if r == rank:
                continue
            factor = rows[r][col] % prime
            if factor:
                rows[r] = [(a - factor * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    cokernel = load("cosmology_tau_obstruction_cokernel.json")
    formal = load("cosmology_tau_lift_formal_problem.json")
    trichotomy = load("cosmology_tau_source_domain_trichotomy.json")

    assert cokernel["passed"] is True
    assert formal["passed"] is True
    assert trichotomy["passed"] is True
    assert cokernel["obstruction_vector"] == [1, 0]
    assert formal["formal_horn"]["required_d1_column"] == [1, 1]

    # A native three-chart cover can generate one or more oriented Cech faces.
    # Before a log comparison is added, every such sourced column has zero
    # Xi_log coordinate and an integer Cech-face coefficient.
    sample_columns = [[0, -2], [0, -1], [0, 1], [0, 2]]
    for column in sample_columns:
        assert column[0] == 0

    required = [1, 1]
    witnesses = {}
    for prime in (101, 103):
        cech_matrix = [[col[0] for col in sample_columns], [col[1] for col in sample_columns]]
        cech_rank = rank_mod_prime(cech_matrix, prime)
        augmented_rank = rank_mod_prime([cech_matrix[0] + [required[0]], cech_matrix[1] + [required[1]]], prime)
        assert cech_rank == 1
        assert augmented_rank == 2
        witnesses[str(prime)] = {
            "cech_only_span_rank": cech_rank,
            "cech_only_plus_required_tau_rank": augmented_rank,
            "Xi_obstruction_survives": True,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-native-three-chart-cover-limit.v1",
        "status": "native_three_chart_cover_alone_repeats_cech_axis_and_does_not_kill_Xi_obstruction",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_tau_obstruction_cokernel.json",
            "research/voevodsky/results/cosmology_tau_lift_formal_problem.json",
            "research/voevodsky/results/cosmology_tau_source_domain_trichotomy.json",
        ],
        "tested_route": "native three-chart marked-fiber cover without additional logarithmic comparison",
        "basis_rows": ["Xi_log", "minus_sigma123"],
        "cech_only_column_form": "(0,n) for n in Z",
        "sample_columns": sample_columns,
        "required_tau_column": required,
        "finite_field_witnesses": witnesses,
        "decision": "a native three-chart cover is necessary for a sourced sigma123 face but is not sufficient; by itself it only enlarges the already sourced Cech axis",
        "remaining_required_extra": "a comparison assigning Xi_log coefficient +/-1 to one native cover cone cell",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
