#!/usr/bin/env python3
"""Dimension-only falsifier for the literal terminal T7 readout pair."""

import hashlib
import json
from pathlib import Path


def main():
    t7_dimension = 7
    nearby_rank = 0
    literal_physical_chain_count = 1
    physical_rank_upper_bound = literal_physical_chain_count
    joint_rank_upper_bound = nearby_rank + physical_rank_upper_bound
    residual_kernel_lower_bound = t7_dimension - joint_rank_upper_bound

    assert joint_rank_upper_bound == 1
    assert residual_kernel_lower_bound == 6
    assert joint_rank_upper_bound < t7_dimension

    expected = {
        "schema": "marici.nima.cosmology_terminal_t7_rank_bound.v1",
        "domain": "T7",
        "domain_dimension": t7_dimension,
        "nearby_cycle": {
            "locus": "generic nonsoft total-energy cusp E=0",
            "rank_on_T7": nearby_rank,
            "source": "Entry 289"
        },
        "physical_readout": {
            "interpretation": "literal frozen Bunch-Davies chain",
            "declared_chain_count": literal_physical_chain_count,
            "rank_upper_bound": physical_rank_upper_bound,
            "matrix_required_for_bound": False
        },
        "joint_rank_upper_bound": joint_rank_upper_bound,
        "residual_kernel_dimension_lower_bound": residual_kernel_lower_bound,
        "verdict": "fail for the literal nearby-cycle plus one-chain physical terminal pair",
        "scope_boundary": "does not exclude a predeclared larger family of independent physical cycles or a different typed terminal readout"
    }

    result_path = Path(__file__).parents[1] / "results" / "cosmology-terminal-t7-rank-bound.json"
    payload = result_path.read_text(encoding="utf-8")
    assert json.loads(payload) == expected
    print(json.dumps({"passed": True, "verdict": "fail", "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
