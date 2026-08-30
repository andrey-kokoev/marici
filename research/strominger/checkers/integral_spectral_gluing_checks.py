#!/usr/bin/env python3
"""Exact integral gluing audit for the parabolic and hyperbolic response planes."""

from __future__ import annotations

import contextlib
from fractions import Fraction
from functools import reduce
import io
import itertools
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

C = source["C"]
multiply = source["multiply"]
I4 = [[int(i == j) for j in range(4)] for i in range(4)]


def add(*matrices):
    return [[sum(A[i][j] for A in matrices) for j in range(4)] for i in range(4)]


def scale(k, A):
    return [[k * A[i][j] for j in range(4)] for i in range(4)]


def determinant(A):
    total = 0
    for p in itertools.permutations(range(len(A))):
        inversions = sum(p[i] > p[j] for i in range(len(A)) for j in range(i + 1, len(A)))
        term = (-1) ** inversions
        for i in range(len(A)):
            term *= A[i][p[i]]
        total += term
    return total


def rational_nullspace(A):
    work = [[Fraction(v) for v in row] for row in A]
    rows, cols = len(work), len(work[0])
    pivots = []
    pivot_row = 0
    for column in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale_value = work[pivot_row][column]
        work[pivot_row] = [v / scale_value for v in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][column]:
                coefficient = work[r][column]
                work[r] = [work[r][j] - coefficient * work[pivot_row][j] for j in range(cols)]
        pivots.append(column)
        pivot_row += 1
    free = [j for j in range(cols) if j not in pivots]
    basis = []
    for f in free:
        vector = [Fraction(0) for _ in range(cols)]
        vector[f] = Fraction(1)
        for r, p in enumerate(pivots):
            vector[p] = -work[r][f]
        denominator = math.lcm(*(v.denominator for v in vector))
        integers = [int(v * denominator) for v in vector]
        content = reduce(math.gcd, (abs(v) for v in integers if v), 0)
        basis.append([v // content for v in integers])
    return basis


def mat_vec(A, v):
    return [sum(A[i][j] * v[j] for j in range(4)) for i in range(4)]


def plucker_content(columns):
    minors = []
    for i, j in itertools.combinations(range(4), 2):
        minors.append(columns[0][i] * columns[1][j] - columns[0][j] * columns[1][i])
    return reduce(math.gcd, (abs(v) for v in minors), 0)


def saturated_basis(columns):
    content = plucker_content(columns)
    candidates = [list(v) for v in columns]
    for denominator in range(2, content + 1):
        if content % denominator:
            continue
        for a in range(denominator):
            for b in range(denominator):
                if a == b == 0:
                    continue
                numerator = [a * columns[0][i] + b * columns[1][i] for i in range(4)]
                if all(v % denominator == 0 for v in numerator):
                    candidate = [v // denominator for v in numerator]
                    divisor = reduce(math.gcd, (abs(v) for v in candidate if v), 0)
                    if divisor:
                        candidate = [v // divisor for v in candidate]
                    if candidate not in candidates and [-v for v in candidate] not in candidates:
                        candidates.append(candidate)
    for left, right in itertools.combinations(candidates, 2):
        if plucker_content([left, right]) == 1:
            return [left, right]
    raise AssertionError("failed to construct saturated rank-two basis")


N = add(C, scale(-1, I4))
parabolic_operator = multiply(N, N)
hyperbolic_operator = add(multiply(C, C), scale(-147458, C), I4)

raw_parabolic_basis = rational_nullspace(parabolic_operator)
raw_hyperbolic_basis = rational_nullspace(hyperbolic_operator)

raw_parabolic_content = plucker_content(raw_parabolic_basis)
raw_hyperbolic_content = plucker_content(raw_hyperbolic_basis)
parabolic_basis = saturated_basis(raw_parabolic_basis)
hyperbolic_basis = saturated_basis(raw_hyperbolic_basis)
parabolic_content = plucker_content(parabolic_basis)
hyperbolic_content = plucker_content(hyperbolic_basis)

combined = [
    [parabolic_basis[0][i], parabolic_basis[1][i],
     hyperbolic_basis[0][i], hyperbolic_basis[1][i]]
    for i in range(4)
]
splitting_index = abs(determinant(combined))

resultant_base = abs(1 - 147458 + 1)
resultant = resultant_base**2


def prime_valuation(value, prime):
    count = 0
    while value and value % prime == 0:
        value //= prime
        count += 1
    return count


prime_support = {
    "2": prime_valuation(resultant, 2),
    "3": prime_valuation(resultant, 3),
}
residual_after_2_3 = resultant // (2**prime_support["2"] * 3**prime_support["3"])
actual_prime_support = {
    "2": prime_valuation(splitting_index, 2),
    "3": prime_valuation(splitting_index, 3),
}
actual_residual_after_2_3 = splitting_index // (
    2**actual_prime_support["2"] * 3**actual_prime_support["3"]
)

gates = {
    "both_rational_spectral_planes_have_rank_two":
        len(parabolic_basis) == 2 and len(hyperbolic_basis) == 2,
    "raw_rref_bases_require_saturation":
        raw_parabolic_content > 1 and raw_hyperbolic_content > 1,
    "displayed_kernel_bases_are_saturated":
        parabolic_content == 1 and hyperbolic_content == 1,
    "basis_vectors_satisfy_exact_factor_kernels":
        all(mat_vec(parabolic_operator, v) == [0] * 4 for v in parabolic_basis)
        and all(mat_vec(hyperbolic_operator, v) == [0] * 4 for v in hyperbolic_basis),
    "rational_planes_fail_to_split_the_integral_lattice": splitting_index > 1,
    "resultant_is_supported_only_at_two_and_three": residual_after_2_3 == 1,
    "actual_gluing_index_divides_the_resultant": resultant % splitting_index == 0,
    "actual_gluing_is_supported_only_at_two":
        actual_prime_support["2"] > 0
        and actual_prime_support["3"] == 0
        and actual_residual_after_2_3 == 1,
}

payload = {
    "schema": "marici.strominger.integral_spectral_gluing_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "parabolic_and_hyperbolic_planes_are_integrally_glued_at_resultant_primes",
    "parabolic_basis": parabolic_basis,
    "hyperbolic_basis": hyperbolic_basis,
    "raw_parabolic_plucker_content": raw_parabolic_content,
    "raw_hyperbolic_plucker_content": raw_hyperbolic_content,
    "parabolic_plucker_content": parabolic_content,
    "hyperbolic_plucker_content": hyperbolic_content,
    "integral_splitting_index": splitting_index,
    "resultant_base": resultant_base,
    "resultant": resultant,
    "resultant_prime_valuations": prime_support,
    "resultant_residual_after_2_3": residual_after_2_3,
    "actual_gluing_prime_valuations": actual_prime_support,
    "actual_gluing_residual_after_2_3": actual_residual_after_2_3,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "After saturation, the rational parabolic and hyperbolic planes do not "
        "sum to the full integral lattice. The resultant permits 2- and 3-primary "
        "gluing, but the actual quotient is supported only at 2. Therefore the "
        "observed 3-adic response jet does not originate in this spectral gluing."
    ),
}
print(json.dumps(payload, indent=2))
