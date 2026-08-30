#!/usr/bin/env python3
"""Bound the terminal rank of the complete currently declared cyclic family."""

import hashlib
import json
from pathlib import Path


def main():
    domain_dimension = 7
    nearby_rank = 0
    declared_cyclic_leray_germs = 3
    joint_rank_upper_bound = nearby_rank + declared_cyclic_leray_germs
    residual_lower_bound = domain_dimension - joint_rank_upper_bound
    assert joint_rank_upper_bound == 3
    assert residual_lower_bound == 4

    expected = {
        "schema": "marici.nima.cosmology_source_cycle_family_rank_bound.v1",
        "domain": "T7",
        "domain_dimension": domain_dimension,
        "nearby_rank_on_T7": nearby_rank,
        "source_declared_finite_family": {
            "kind": "three cyclic local Leray residue germs from one meromorphic source packet",
            "cardinality": declared_cyclic_leray_germs,
            "source": "Entries 180 and 365"
        },
        "joint_rank_upper_bound": joint_rank_upper_bound,
        "residual_kernel_dimension_lower_bound": residual_lower_bound,
        "verdict": "the complete currently declared finite continuation family is not jointly conservative on T7",
        "open_question": "the span of the unrestricted global Gauss-Manin/monodromy orbit of the canonical physical germ"
    }
    result_path = Path(__file__).parents[1] / "results" / "cosmology-source-cycle-family-rank-bound.json"
    payload = result_path.read_text(encoding="utf-8")
    assert json.loads(payload) == expected
    print(json.dumps({"passed": True, "rank_upper_bound": 3, "residual_lower_bound": 4, "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
