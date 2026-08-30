#!/usr/bin/env python3
"""Test mixed flatness of the source-labelled rank-four CM connection."""

import json
import os
from pathlib import Path

from check_cm_rank_four_connection_matrices import run_case
from probe_cm_cyclic_connection_slice_degrees import evaluate, minimal_fit


ROOT = Path(__file__).resolve().parent.parent
PRIME = int(os.environ.get("CM_FLATNESS_PRIME", "32003"))
BASE = (5, 7, 11)
X_VALUES = tuple(range(2, 27))


def polynomial_derivative(poly, value, prime):
    result = 0
    for degree in range(1, len(poly)):
        result = (result + degree*poly[degree]*pow(value, degree-1, prime)) % prime
    return result


def rational_derivative(candidate, value, prime):
    numerator, denominator = candidate
    p = evaluate(numerator, value, prime)
    q = evaluate(denominator, value, prime)
    dp = polynomial_derivative(numerator, value, prime)
    dq = polynomial_derivative(denominator, value, prime)
    return (dp*q-p*dq)*pow(q, -2, prime) % prime


def zero_matrix():
    return [[0 for _ in range(4)] for _ in range(4)]


def matrix_product(left, right, prime):
    return [
        [sum(left[row][inner]*right[inner][column] for inner in range(4)) % prime for column in range(4)]
        for row in range(4)
    ]


def matrix_subtract(*matrices):
    result = zero_matrix()
    for index, matrix in enumerate(matrices):
        sign = 1 if index == 0 else -1
        for row in range(4):
            for column in range(4):
                result[row][column] = (result[row][column]+sign*matrix[row][column]) % PRIME
    return result


def main():
    base_matrices = run_case("A", PRIME, BASE)["matrices"]
    derivatives = [[zero_matrix() for _ in range(3)] for _ in range(3)]
    degree_bounds = []
    for varying_direction in range(3):
        samples = []
        for value in X_VALUES:
            point = list(BASE)
            point[varying_direction] = value
            samples.append((value, run_case("A", PRIME, tuple(point))["matrices"]))
        for matrix_direction in range(3):
            for row in range(4):
                for column in range(4):
                    data = [
                        (value, matrices[matrix_direction][row][column])
                        for value, matrices in samples
                    ]
                    candidates = minimal_fit(data, PRIME, max_total_degree=16)
                    if not candidates:
                        raise RuntimeError("no rational slice fit within the frozen degree bound")
                    candidate_derivatives = {
                        rational_derivative(candidate, BASE[varying_direction], PRIME)
                        for numerator_degree, denominator_degree, candidate in candidates
                    }
                    if len(candidate_derivatives) != 1:
                        raise RuntimeError("minimal slice fits disagree on the derivative")
                    derivatives[varying_direction][matrix_direction][row][column] = candidate_derivatives.pop()
                    degree_bounds.extend(
                        (numerator_degree, denominator_degree)
                        for numerator_degree, denominator_degree, candidate in candidates
                    )
    curvatures = {}
    opposite_sign_curvatures = {}
    for first, second in ((0, 1), (0, 2), (1, 2)):
        commutator = matrix_subtract(
            matrix_product(base_matrices[first], base_matrices[second], PRIME),
            matrix_product(base_matrices[second], base_matrices[first], PRIME),
        )
        curvature = matrix_subtract(
            derivatives[first][second],
            derivatives[second][first],
            [[(-value) % PRIME for value in row] for row in commutator],
        )
        curvatures[f"F_{first+1}{second+1}"] = curvature
        opposite_sign_curvatures[f"F_{first+1}{second+1}"] = matrix_subtract(
            derivatives[first][second],
            derivatives[second][first],
            commutator,
        )
    nonzero_counts = {
        name: sum(value != 0 for row in matrix for value in row)
        for name, matrix in curvatures.items()
    }
    opposite_nonzero_counts = {
        name: sum(value != 0 for row in matrix for value in row)
        for name, matrix in opposite_sign_curvatures.items()
    }
    checks = {
        "all_slice_degrees_within_frozen_bound": bool(degree_bounds) and max(sum(pair) for pair in degree_bounds) <= 16,
        "all_three_mixed_curvatures_vanish": all(count == 0 for count in nonzero_counts.values()),
    }
    packet = {
        "schema": "marici.cm_rank_four_mixed_flatness.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "prime": PRIME,
        "base_squared_momenta": list(BASE),
        "sample_values_per_axis": list(X_VALUES),
        "maximum_minimal_total_slice_degree": max(sum(pair) for pair in degree_bounds),
        "curvatures": curvatures,
        "opposite_commutator_sign_curvatures": opposite_sign_curvatures,
        "nonzero_counts": nonzero_counts,
        "opposite_sign_nonzero_counts": opposite_nonzero_counts,
        "checks": checks,
    }
    output = ROOT / "results" / f"cm-rank-four-mixed-flatness-p{PRIME}.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": packet["status"],
        "maximum_minimal_total_slice_degree": packet["maximum_minimal_total_slice_degree"],
        "nonzero_counts": nonzero_counts,
        "opposite_sign_nonzero_counts": opposite_nonzero_counts,
        "checks": checks,
    }, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
