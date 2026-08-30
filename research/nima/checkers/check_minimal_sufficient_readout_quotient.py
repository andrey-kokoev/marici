"""Exact finite-dimensional controls for the minimal sufficient quotient."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "minimal_sufficient_readout_quotient.json"


def rank(matrix):
    rows = [list(map(F, row)) for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for index in range(len(rows)):
            if index == pivot_row:
                continue
            scale = rows[index][column]
            rows[index] = [a - scale * b for a, b in zip(rows[index], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


def main():
    d12 = ((F(1), F(3, 2)), (F(1), F(1)))
    single_ranks = [rank((row,)) for row in d12]
    joint_rank = rank(d12)

    # Exhaust the kernel-inclusion theorem for all 2-column binary readout
    # matrices and all one-row binary quotient maps. Over F2, R factors through
    # q precisely when every vector killed by q is also killed by R.
    exhaustive_cases = 0
    equivalence_failures = 0
    vectors = tuple(itertools.product(range(2), repeat=2))
    rows = tuple(itertools.product(range(2), repeat=2))
    for readout_rows in itertools.product(rows, repeat=2):
        ker_r = {
            vector for vector in vectors
            if all(sum(a * b for a, b in zip(row, vector)) % 2 == 0 for row in readout_rows)
        }
        for quotient_row in rows[1:]:
            ker_q = {
                vector for vector in vectors
                if sum(a * b for a, b in zip(quotient_row, vector)) % 2 == 0
            }
            kernel_condition = ker_q <= ker_r
            # A two-row R factors through one-bit q iff each R row is 0 or q.
            factorization_condition = all(row in ((0, 0), quotient_row) for row in readout_rows)
            exhaustive_cases += 1
            equivalence_failures += int(kernel_condition != factorization_condition)

    packet = {
        "schema": "marici.minimal-sufficient-readout-quotient.v1",
        "theorem": "V/ker(R) is the coarsest quotient preserving the declared readout family R",
        "d12_control": {
            "dimension": 2,
            "single_readout_ranks": single_ranks,
            "joint_rank": joint_rank,
            "joint_kernel_dimension": 2 - joint_rank,
            "minimal_sufficient_dimension": joint_rank,
        },
        "f2_exhaustive_factorization_control": {
            "cases": exhaustive_cases,
            "kernel_inclusion_equivalence_failures": equivalence_failures,
        },
        "cosmology_t7_restricted_family": {
            "domain_dimension": 7,
            "declared_readout_count": 3,
            "joint_rank_upper_bound": 3,
            "minimal_sufficient_dimension_upper_bound": 3,
            "invisible_kernel_dimension_lower_bound": 4,
            "status": "restricted-family bound, not the incomplete four-map physical protocol",
        },
    }
    packet["passed"] = (
        single_ranks == [1, 1]
        and joint_rank == 2
        and equivalence_failures == 0
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
