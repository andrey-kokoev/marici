#!/usr/bin/env python3
"""Test the quadratic numerator top symbol modulo the verified linear grade."""

import json
import os
from pathlib import Path

import numpy as np

import check_five_site_projective_labelled_order_one_linear_numerators as linear
import check_five_site_projective_labelled_order_one_exactness as constant

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/five-site-projective-quadratic-top-symbol.json"
SAMPLE_COUNT = int(os.environ.get("MARICI_QUADRATIC_TOP_SAMPLES", "1500"))
PRIMES = tuple(int(x) for x in os.environ.get("MARICI_QUADRATIC_TOP_PRIMES", "1009,1013").split(","))
SCALAR_DEGREE = 3


def left_nullspace(rows, prime):
    """Return row vectors l with l*M=0 by tracking exact row operations."""
    matrix = np.asarray(rows, dtype=np.int64) % prime
    row_count, column_count = matrix.shape
    augmented = np.concatenate(
        [matrix, np.eye(row_count, dtype=np.int64)], axis=1
    )
    pivot_row = 0
    for column in range(column_count):
        candidates = np.flatnonzero(augmented[pivot_row:, column])
        if candidates.size == 0:
            continue
        pivot = pivot_row + int(candidates[0])
        if pivot != pivot_row:
            augmented[[pivot_row, pivot]] = augmented[[pivot, pivot_row]]
        inverse = pow(int(augmented[pivot_row, column]), prime - 2, prime)
        augmented[pivot_row] = augmented[pivot_row] * inverse % prime
        factors = augmented[:, column].copy()
        factors[pivot_row] = 0
        nonzero = np.flatnonzero(factors)
        if nonzero.size:
            augmented[nonzero] = (
                augmented[nonzero]
                - factors[nonzero, None] * augmented[pivot_row][None, :]
            ) % prime
        pivot_row += 1
        if pivot_row == row_count:
            break
    assert not np.any(augmented[pivot_row:, :column_count])
    return augmented[pivot_row:, column_count:] % prime, pivot_row


def quadratic_top_row(sample, prime):
    u1, u2, u3 = sample["u"]
    monomials = (
        u1 * u1 % prime,
        u1 * u2 % prime,
        u1 * u3 % prime,
        u2 * u2 % prime,
        u2 * u3 % prime,
        u3 * u3 % prime,
    )
    row = []
    # Linear checker ordering is term, derivative, (1,u1,u2,u3).
    for term_index in range(len(linear.LABELS)):
        for derivative in range(3):
            div = sample["primitive"][4 * (3 * term_index + derivative)]
            row.extend(div * monomial % prime for monomial in monomials)
    return row


def main():
    results = []
    for prime in PRIMES:
        samples = []
        keys = set()
        for seed in range(1, max(30000, 50 * SAMPLE_COUNT)):
            sample = linear.sample_row(prime, seed)
            key = (sample["t"], *sample["u"])
            if key not in keys:
                keys.add(key)
                samples.append(sample)
            if len(samples) == SAMPLE_COUNT:
                break
        assert len(samples) == SAMPLE_COUNT

        width = SCALAR_DEGREE + 1
        lower = []
        derivative = []
        quadratic = []
        for sample in samples:
            p0 = [sample["target"] * pow(sample["t"], k, prime) % prime for k in range(width)]
            p1 = [sample["target_dt"] * pow(sample["t"], k, prime) % prime for k in range(width)]
            lower.append(sample["primitive"] + p0)
            derivative.append(p1)
            quadratic.append(quadratic_top_row(sample, prime))

        left, lower_rank = left_nullspace(lower, prime)
        quadratic_array = np.asarray(quadratic, dtype=np.int64)
        derivative_array = np.asarray(derivative, dtype=np.int64)
        projected_quadratic = left @ quadratic_array % prime
        projected_derivative = left @ derivative_array % prime
        quadratic_rank = constant.modular_rank(projected_quadratic.tolist(), prime)
        joined = np.concatenate([projected_quadratic, projected_derivative], axis=1)
        joined_rank = constant.modular_rank(joined.tolist(), prime)
        relation_dimension = width - (joined_rank - quadratic_rank)
        results.append({
            "prime": prime,
            "samples": SAMPLE_COUNT,
            "lower_rank": lower_rank,
            "left_nullity": int(left.shape[0]),
            "quadratic_top_columns": int(projected_quadratic.shape[1]),
            "projected_quadratic_rank": quadratic_rank,
            "projected_joined_rank": joined_rank,
            "dt_relation_dimension": relation_dimension,
            "constraint_space_exhausted": quadratic_rank == left.shape[0],
        })

    output = {
        "schema": "marici.five_site.projective_quadratic_top_symbol.v1",
        "filtration": "homogeneous quadratic numerator symbols modulo the full linear-numerator grade",
        "cyclic_averaging_used": False,
        "cyclic_averaging_prohibited_by": "Entry 1404: the asymmetric Kummer profile has no affine C5 lift",
        "scalar_degree": SCALAR_DEGREE,
        "results": results,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
