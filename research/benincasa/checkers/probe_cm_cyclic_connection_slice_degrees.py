#!/usr/bin/env python3
"""Probe minimal univariate rational degrees of the cyclic quotient connection."""

import json
from pathlib import Path

from check_cm_cyclic_connection_poles import run_case


ROOT = Path(__file__).resolve().parent.parent
PRIMES = (32003, 65521)
SLICES = ((7, 11), (11, 17))
X_VALUES = tuple(range(2, 27))


def solve_linear(matrix, rhs, prime):
    augmented = [
        [value % prime for value in row] + [value % prime]
        for row, value in zip(matrix, rhs)
    ]
    rows = len(augmented)
    columns = len(matrix[0])
    pivot_row = 0
    pivots = []
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if augmented[row][column]), None)
        if pivot is None:
            continue
        augmented[pivot_row], augmented[pivot] = augmented[pivot], augmented[pivot_row]
        inverse = pow(augmented[pivot_row][column], -1, prime)
        augmented[pivot_row] = [(value * inverse) % prime for value in augmented[pivot_row]]
        for row in range(rows):
            if row != pivot_row and augmented[row][column]:
                factor = augmented[row][column]
                augmented[row] = [
                    (left - factor*right) % prime
                    for left, right in zip(augmented[row], augmented[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    if len(pivots) != columns:
        return None
    if any(all(row[column] == 0 for column in range(columns)) and row[-1] for row in augmented):
        return None
    solution = [0] * columns
    for row, column in enumerate(pivots):
        solution[column] = augmented[row][-1]
    return solution


def evaluate(poly, value, prime):
    result = 0
    for coefficient in reversed(poly):
        result = (result*value + coefficient) % prime
    return result


def fit(data, numerator_degree, denominator_degree, prime):
    unknowns = numerator_degree + 1 + denominator_degree
    training = data[:unknowns]
    matrix = []
    rhs = []
    for x, y in training:
        matrix.append(
            [pow(x, degree, prime) for degree in range(numerator_degree + 1)]
            + [(-y*pow(x, degree, prime)) % prime for degree in range(denominator_degree)]
        )
        rhs.append(y*pow(x, denominator_degree, prime) % prime)
    solution = solve_linear(matrix, rhs, prime)
    if solution is None:
        return None
    numerator = solution[:numerator_degree + 1]
    denominator = solution[numerator_degree + 1:] + [1]
    for x, y in data:
        den = evaluate(denominator, x, prime)
        if den == 0 or evaluate(numerator, x, prime) != y*den % prime:
            return None
    return numerator, denominator


def minimal_fit(data, prime, max_total_degree=16):
    for total in range(max_total_degree + 1):
        candidates = []
        for denominator_degree in range(total + 1):
            numerator_degree = total - denominator_degree
            candidate = fit(data, numerator_degree, denominator_degree, prime)
            if candidate is not None:
                candidates.append((numerator_degree, denominator_degree, candidate))
        if candidates:
            return candidates
    return []


def main():
    runs = []
    for prime in PRIMES:
        for fixed_s2, fixed_s3 in SLICES:
            values = [
                (s1, run_case((s1, fixed_s2, fixed_s3), prime))
                for s1 in X_VALUES
            ]
            fits = []
            for direction in range(3):
                data = [(s1, omega[direction]) for s1, omega in values]
                candidates = minimal_fit(data, prime)
                fits.append([
                    {
                        "numerator_degree": numerator_degree,
                        "denominator_degree": denominator_degree,
                        "numerator": candidate[0],
                        "denominator": candidate[1],
                    }
                    for numerator_degree, denominator_degree, candidate in candidates
                ])
            runs.append({
                "prime": prime,
                "slice": {"s2": fixed_s2, "s3": fixed_s3},
                "sample_count": len(values),
                "minimal_fits_by_direction": fits,
            })
    packet = {
        "schema": "marici.cm_cyclic_connection_slice_degrees.v1",
        "runs": runs,
    }
    output = ROOT / "results" / "cm-cyclic-connection-slice-degrees.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    summary = [
        {
            "prime": run["prime"],
            "slice": run["slice"],
            "degrees": [
                [[fit["numerator_degree"], fit["denominator_degree"]] for fit in direction]
                for direction in run["minimal_fits_by_direction"]
            ],
        }
        for run in runs
    ]
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
