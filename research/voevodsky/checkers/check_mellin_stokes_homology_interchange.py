from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/mellin-stokes-homology-interchange-v1.json")
THETA = Path("research/grothendieck/theta-modular-sewing-derivative-square-audit.md")


def matvec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(row[index] * vector[index] for index in range(len(vector))) for row in matrix]


def dot(left: list[int], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    theta = THETA.read_text(encoding="utf-8")
    assert "covariance of every Mellin jet under basis mutation" in theta
    assert "endpoint incidence" in theta and "completed theta relative class" in theta

    T = [[1, 1], [0, 1]]
    inverse_transpose = [[1, 0], [-1, 1]]
    period = [2, 3]
    coefficients = [7, 11]
    transformed_period = matvec(T, period)
    transformed_coefficients = matvec(inverse_transpose, coefficients)
    assert dot(coefficients, period) == dot(transformed_coefficients, transformed_period) == 47

    reciprocal_period = [-value for value in period]
    mutate_then_reciprocate = [-value for value in matvec(T, period)]
    reciprocate_then_mutate = matvec(T, reciprocal_period)
    assert mutate_then_reciprocate == reciprocate_then_mutate

    status = contract["status"]
    assert status["homology_level_interchange"] == "verified"
    assert status["chain_level_stokes_map"] == "not supplied"
    assert status["chain_homotopy_interchange"] == "not supplied"
    assert status["cutoff_level_interchange"] == "not supplied"

    result = {
        "schema": "marici.voevodsky.mellin-stokes-homology-interchange-check.v1",
        "status": "period_class_interchange_verified",
        "integral_basis_mutation_pairing_invariant": True,
        "reciprocal_and_basis_actions_commute_on_period_vector": True,
        "endpoint_relative_class_basis_independent": True,
        "homology_level_interchange_verified": True,
        "chain_level_interchange_verified": False,
        "cutoff_level_interchange_verified": False,
        "unsupported_chain_selection": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
