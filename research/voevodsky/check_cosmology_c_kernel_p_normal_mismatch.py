"""c-kernel versus p-normal mismatch for the tau_p source route.

Repeat iteration 4 tests whether the retained c pivot can itself be identified
with the p-normal direction required for Xi_log.  It cannot: the known c covector
is proportional to dx+dy+dz, while the source p-normal is dx+dy+3dz.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_c_kernel_p_normal_mismatch.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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
    relative_gate = load(VOEVODSKY_RESULTS / "cosmology_relative_base_fiber_comparison_gate.json")
    source = load(NIMA_RESULTS / "cosmology_source_principal_wall_cell.json")
    pivot = load(NIMA_RESULTS / "cosmology_tau_gradient_pivot_type_gate.json")

    assert relative_gate["passed"] is True
    assert source["passed"] is True
    assert pivot["passed"] is True
    assert relative_gate["projection_kernel_generator"] == [0, 0, 1]
    assert source["induced_base_first_jet"] == [1, 1, 3]
    assert pivot["c_pivot_role"] == "base-dependent c=-(x+y+z), not a target fiber direction"

    p_covector = [1, 1, 3]
    c_covector = [-1, -1, -1]
    candidate_rows = [p_covector, c_covector]
    assert rank_mod_prime(candidate_rows, 0x7fffffff) == 2  # ordinary integer-safe path not using modulus wrap for small entries

    witnesses = {}
    for prime in (101, 103):
        rank = rank_mod_prime(candidate_rows, prime)
        assert rank == 2
        witnesses[str(prime)] = {
            "p_covector": [value % prime for value in p_covector],
            "c_covector": [value % prime for value in c_covector],
            "span_rank": rank,
            "c_is_p_normal_unit_multiple": False,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-c-kernel-p-normal-mismatch.v1",
        "status": "c_kernel_not_identified_with_p_normal",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_relative_base_fiber_comparison_gate.json",
            "research/nima/results/cosmology_source_principal_wall_cell.json",
            "research/nima/results/cosmology_tau_gradient_pivot_type_gate.json",
        ],
        "p_normal_covector_dx_dy_dz": p_covector,
        "c_pivot_covector_dx_dy_dz": c_covector,
        "rank_of_p_and_c_covectors": 2,
        "finite_field_witnesses": witnesses,
        "decision": "retaining the c pivot restores a relative three-chart cover but does not by itself identify the c-kernel with the p-normal Xi_log leg",
        "missing_comparison": "a source-derived base comparison from the c-kernel direction to the p-normal residue class, not a scalar normalization of c",
        "forbidden_shortcut": "treating c=-(x+y+z) as the p=x+y+3z normal",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
