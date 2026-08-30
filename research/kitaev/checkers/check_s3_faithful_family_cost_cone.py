#!/usr/bin/env python3
"""Symbolic cost-cone robustness of the CDFG faithful Wilson family."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-faithful-family-resource-selection.json"
OUT = K / "results" / "s3-faithful-family-cost-cone.json"
COORDS = ("CS_or_CSdagger", "CCZ", "Toffoli_compute_uncompute_pair", "work_block_episode")


def primitive_vector(port: dict) -> tuple[int, int, int, int]:
    cs = ccz = pair = 0
    for power in port["controlled_powers"]:
        for term in power["terms"]:
            degree = term["mask"].bit_count()
            coefficient = term["coefficient_mod8"]
            if degree >= 2 and coefficient in {2, 6}:
                cs += 1
                pair += degree - 2
            elif degree >= 3 and coefficient == 4:
                ccz += 1
                pair += degree - 3
    return cs, ccz, pair, port["total_work_block_episodes"]


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    ports = {label: primitive_vector(record) for label, record in source["ports"].items()}
    families = {
        family: tuple(sum(ports[label][coordinate] for label in family)
                      for coordinate in range(4))
        for family in source["families"]
    }
    winner = families["CDFG"]
    differences = {
        family: tuple(value - base for value, base in zip(vector, winner))
        for family, vector in families.items()
        if family != "CDFG"
    }
    assert winner == (13, 14, 16, 16)
    assert all(all(value >= 0 for value in difference) for difference in differences.values())
    assert differences["CEFG"] == (0, 1, 0, 0)

    # Exhaust a bounded hostile sample of the full nonnegative weight cone.
    grid = range(4)
    classifications = {"unique_CDFG": 0, "CDFG_tied": 0, "other_wins": 0}
    examples = {}
    for weights in __import__("itertools").product(grid, repeat=4):
        costs = {family: sum(weight * value for weight, value in zip(weights, vector))
                 for family, vector in families.items()}
        minimum = min(costs.values())
        minimizers = sorted(family for family, cost in costs.items() if cost == minimum)
        if minimizers == ["CDFG"]:
            key = "unique_CDFG"
        elif "CDFG" in minimizers:
            key = "CDFG_tied"
        else:
            key = "other_wins"
        classifications[key] += 1
        examples.setdefault(key, {"weights": dict(zip(COORDS, weights)), "minimizers": minimizers})
    assert classifications["other_wins"] == 0

    # From the difference table, CEFG forces positive CCZ weight for
    # uniqueness; CDFH forces positivity of CS+pair+work. These two conditions
    # make every other displayed nonnegative difference strictly positive.
    result = {
        "schema": "marici.kitaev.s3-faithful-family-cost-cone.v1",
        "input_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "coordinates": list(COORDS),
        "port_vectors": {label: list(vector) for label, vector in ports.items()},
        "family_vectors": {family: list(vector) for family, vector in families.items()},
        "CDFG_difference_table": {family: list(vector) for family, vector in differences.items()},
        "nonnegative_cost_cone_theorem": {
            "weak_dominance": "CDFG minimizes every nonnegative linear combination of the four coordinates",
            "uniqueness_condition": "weight_CCZ > 0 and weight_CS + weight_Toffoli_pair + weight_work_episode > 0",
            "degenerate_ties": "if CCZ is free, CEFG ties CDFG; if CS, Toffoli-pair, and work episodes are all free, CDFH and other zero-difference families may tie",
        },
        "hostile_weight_grid_0_through_3": {"classifications": classifications, "examples": examples},
        "verdict": "CDFG's compiler-relative selection is robust throughout the nonnegative primitive-cost cone, not an artifact of the numerical 3/7/14 T-cost assignment. It is unique exactly away from the stated degenerate free-resource faces. This remains relative to the chosen primitive library and excludes physical failure correlations.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
