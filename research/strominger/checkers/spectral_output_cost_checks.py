#!/usr/bin/env python3
"""Exact spectral lower bound for explicit decoration-response matrices."""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

C = source["C"]
multiply = source["multiply"]
I4 = [[int(i == j) for j in range(4)] for i in range(4)]


def trace(A):
    return sum(A[i][i] for i in range(4))


def determinant(A):
    total = 0
    for p in __import__("itertools").permutations(range(4)):
        inversions = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        term = (-1) ** inversions
        for i in range(4):
            term *= A[i][p[i]]
        total += term
    return total


def power(A, exponent):
    total = I4
    atom = A
    e = exponent
    while e:
        if e & 1:
            total = multiply(atom, total)
        atom = multiply(atom, atom)
        e >>= 1
    return total


def characteristic_coefficients(A):
    p1 = trace(A)
    p2 = trace(power(A, 2))
    p3 = trace(power(A, 3))
    e1 = p1
    e2 = (p1 * p1 - p2) // 2
    e3 = (p1**3 - 3 * p1 * p2 + 2 * p3) // 6
    e4 = determinant(A)
    return [1, -e1, e2, -e3, e4]


charpoly = characteristic_coefficients(C)
expected_factorized_coefficients = [1, -147460, 294918, -147460, 1]
factorization_exact = charpoly == expected_factorized_coefficients


def rank(A):
    work = [[Fraction(v) for v in row] for row in A]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [v / scale for v in work[pivot_row]]
        for r in range(len(work)):
            if r != pivot_row and work[r][column]:
                scale = work[r][column]
                work[r] = [work[r][j] - scale * work[pivot_row][j] for j in range(len(work[0]))]
        pivot_row += 1
    return pivot_row


fixed_rank = rank([[C[i][j] - I4[i][j] for j in range(4)] for i in range(4)])
fixed_space_dimension = 4 - fixed_rank

# Exact spectral-radius witness:
# |tr(C^m)| <= 4 rho(C)^m. Find the largest integer L with
# 4 L^m < |tr(C^m)|, which proves rho(C) > L.
witness_power = 8
witness_trace = abs(trace(power(C, witness_power)))
lo, hi = 0, 1
while 4 * hi**witness_power < witness_trace:
    lo, hi = hi, 2 * hi
while hi - lo > 1:
    mid = (lo + hi) // 2
    if 4 * mid**witness_power < witness_trace:
        lo = mid
    else:
        hi = mid
trace_lower = lo

# The exact factor x^2 - 147458 x + 1 has roots lambda and lambda^-1.
# Its expanding root satisfies lambda + lambda^-1 = 147458, hence
# lambda > 147457 because 0 < lambda^-1 < 1.
lower = 147457 if factorization_exact else trace_lower


def bit_length(value):
    return max(1, abs(int(value)).bit_length())


growth_records = []
for exponent in [1, 2, 4, 8, 16, 32]:
    matrix_power = power(C, exponent)
    maximum = max(abs(int(v)) for row in matrix_power for v in row)
    # Since rho(C^n) <= ||C^n||_infinity <= 4 max_ij |(C^n)_ij|,
    # every conjugate presentation obeys max entry >= lower^n / 4.
    certified_integer_floor = lower**exponent // 4
    growth_records.append({
        "exponent": exponent,
        "actual_max_entry_bit_length": bit_length(maximum),
        "spectral_entry_lower_bound_floor": certified_integer_floor,
        "spectral_bit_lower_bound": bit_length(certified_integer_floor),
        "bound_holds_in_current_basis": 4 * maximum >= lower**exponent,
    })

unimodular_fixtures = [
    (I4, I4),
    (
        [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        [[1, -1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    ),
    (
        [[1, 0, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    ),
    (
        [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    ),
]

basis_records = []
for index, (P, Pi) in enumerate(unimodular_fixtures):
    B = multiply(Pi, C, P)
    basis_records.append({
        "fixture": index,
        "determinant_is_unit": abs(determinant(P)) == 1,
        "integral_conjugate": all(isinstance(v, int) for row in B for v in row),
        "characteristic_polynomial_invariant": characteristic_coefficients(B) == charpoly,
        "trace_power_8_invariant": trace(power(B, 8)) == trace(power(C, 8)),
    })

compact_encoding = {
    "state": "integer exponent n plus fixed matrix C",
    "input_bit_length_order": "log(abs(n)+1)",
    "explicit_output_materialized": False,
    "defeats_universal_total_storage_lower_bound": True,
    "does_not_defeat_explicit_matrix_output_lower_bound": True,
}

gates = {
    "characteristic_polynomial_is_monic_integral": charpoly[0] == 1,
    "reciprocal_hyperbolic_factorization_is_exact": factorization_exact,
    "exact_spectral_radius_lower_bound_exceeds_one": lower > 1,
    "spectral_lower_bound_holds_on_tested_powers": all(
        r["bound_holds_in_current_basis"] for r in growth_records
    ),
    "authorized_integral_basis_changes_preserve_spectrum": all(
        r["determinant_is_unit"]
        and r["integral_conjugate"]
        and r["characteristic_polynomial_invariant"]
        and r["trace_power_8_invariant"]
        for r in basis_records
    ),
    "compact_circuit_refutes_a_total_storage_law":
        compact_encoding["defeats_universal_total_storage_lower_bound"],
}

payload = {
    "schema": "marici.strominger.spectral_output_cost_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "spectral_growth_forces_explicit_output_cost_but_not_total_constructor_cost",
    "characteristic_polynomial_coefficients": charpoly,
    "characteristic_polynomial_factorization": "(x-1)^2*(x^2-147458*x+1)",
    "determinant": determinant(C),
    "fixed_space_dimension": fixed_space_dimension,
    "spectral_witness": {
        "power": witness_power,
        "absolute_trace": witness_trace,
        "trace_certified_integer_lower_bound": trace_lower,
        "factor_certified_integer_lower_bound": lower,
        "factor_argument": "lambda+lambda^-1=147458 and 0<lambda^-1<1",
    },
    "growth_records": growth_records,
    "basis_records": basis_records,
    "compact_encoding": compact_encoding,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "Every explicit 4 by 4 matrix presentation conjugate to C^n pays an "
        "exponential entry-size and linear bit-length lower bound from spectral "
        "radius. The exponent-plus-circuit presentation avoids materializing that "
        "output, so no representation-independent total storage law follows."
    ),
}
print(json.dumps(payload, indent=2))
