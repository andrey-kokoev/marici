#!/usr/bin/env python3
"""Reconstruct the cyclic quotient connection over the soft-triangle denominator."""

import json
import math
from pathlib import Path

from check_cm_cyclic_connection_poles import centered, run_case
from probe_cm_cyclic_connection_slice_degrees import solve_linear


ROOT = Path(__file__).resolve().parent.parent
PRIMES = (32003, 65521)
VALIDATION = ((5, 7, 11), (7, 11, 13), (11, 13, 17), (5, 13, 19), (7, 17, 23))
MONOMIALS = tuple(
    (i, j, 4-i-j)
    for i in range(5)
    for j in range(5-i)
)


def lambda_polynomial(point):
    s1, s2, s3 = point
    return s1*s1+s2*s2+s3*s3-2*(s1*s2+s1*s3+s2*s3)


def denominator(point, prime):
    s1, s2, s3 = point
    return s1*s2*s3*lambda_polynomial(point) % prime


def row(point, prime):
    s1, s2, s3 = point
    return [pow(s1, i, prime)*pow(s2, j, prime)*pow(s3, k, prime) % prime for i, j, k in MONOMIALS]


def evaluate(coefficients, point, prime):
    return sum(c*m for c, m in zip(coefficients, row(point, prime))) % prime


def matrix_rank(matrix, prime):
    work = [[value % prime for value in source_row] for source_row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(pivot_row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [(value*inverse) % prime for value in work[pivot_row]]
        for index in range(pivot_row + 1, len(work)):
            if work[index][column]:
                factor = work[index][column]
                work[index] = [
                    (left-factor*right) % prime
                    for left, right in zip(work[index], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def select_training_points():
    selected = []
    matrix = []
    for s1 in (2, 3, 5, 7, 11):
        for s2 in (3, 5, 7, 11, 13):
            for s3 in (5, 7, 11, 13, 17):
                point = (s1, s2, s3)
                if lambda_polynomial(point) == 0:
                    continue
                candidate = matrix + [row(point, PRIMES[0])]
                if matrix_rank(candidate, PRIMES[0]) > len(matrix):
                    selected.append(point)
                    matrix = candidate
                if len(selected) == len(MONOMIALS):
                    if matrix_rank([row(p, PRIMES[1]) for p in selected], PRIMES[1]) != len(MONOMIALS):
                        raise RuntimeError("selected basis degenerates at replication prime")
                    return tuple(selected)
    raise RuntimeError("could not select a full degree-four evaluation basis")


def reconstruct_prime(prime, training):
    matrix = [row(point, prime) for point in training]
    omega = {point: run_case(point, prime) for point in training + VALIDATION}
    coefficients = []
    for direction in range(3):
        rhs = [omega[point][direction]*denominator(point, prime) % prime for point in training]
        solution = solve_linear(matrix, rhs, prime)
        if solution is None:
            raise RuntimeError("degree-four interpolation matrix is singular")
        coefficients.append(solution)
    residuals = []
    for point in VALIDATION:
        for direction in range(3):
            residuals.append(
                (evaluate(coefficients[direction], point, prime)
                 - omega[point][direction]*denominator(point, prime)) % prime
            )
    return coefficients, residuals


def rational_reconstruct(residues, primes, denominator_limit=1024, numerator_limit=100000):
    for denominator in range(1, denominator_limit + 1):
        if math.gcd(denominator, math.prod(primes)) != 1:
            continue
        numerators = [centered(residue*denominator, prime) for residue, prime in zip(residues, primes)]
        if len(set(numerators)) == 1 and abs(numerators[0]) <= numerator_limit:
            common = math.gcd(abs(numerators[0]), denominator)
            return [numerators[0]//common, denominator//common]
    return None


def main():
    training = select_training_points()
    prime_results = [reconstruct_prime(prime, training) for prime in PRIMES]
    rational = []
    for direction in range(3):
        rational.append([
            rational_reconstruct(
                [prime_results[index][0][direction][term] for index in range(len(PRIMES))],
                PRIMES,
            )
            for term in range(len(MONOMIALS))
        ])
    checks = {
        "degree_four_system_is_square": len(training) == len(MONOMIALS) == 15,
        "all_validation_residuals_vanish": all(
            all(value == 0 for value in result[1]) for result in prime_results
        ),
        "all_coefficients_reconstruct_over_Q": all(
            coefficient is not None for direction in rational for coefficient in direction
        ),
    }
    packet = {
        "schema": "marici.cm_cyclic_connection_reconstruction.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "denominator": "s1*s2*s3*Lambda_P",
        "monomial_order": [list(monomial) for monomial in MONOMIALS],
        "training_points": [list(point) for point in training],
        "coefficients_by_direction": rational,
        "validation_points": [list(point) for point in VALIDATION],
        "prime_validation_nonzero_residual_counts": [
            sum(value != 0 for value in result[1]) for result in prime_results
        ],
        "checks": checks,
    }
    output = ROOT / "results" / "cm-cyclic-connection-reconstruction.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": packet["status"],
        "checks": checks,
        "coefficients_by_direction": rational,
    }, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
