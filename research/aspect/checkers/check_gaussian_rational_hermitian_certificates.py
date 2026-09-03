#!/usr/bin/env python3
"""Exact Gaussian-rational Hermitian and SDP certificate checks."""

import itertools
import json
from fractions import Fraction as F
from pathlib import Path

N = 4


def q(re=0, im=0): return F(re), F(im)
def add(x, y): return x[0] + y[0], x[1] + y[1]
def neg(x): return -x[0], -x[1]
def mul(x, y): return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]
def conj(x): return x[0], -x[1]
def scale(r, x): return r * x[0], r * x[1]

def matrix_add(*matrices):
    return tuple(tuple(sum_entry(matrices, i, j) for j in range(N)) for i in range(N))

def sum_entry(matrices, i, j):
    value = q()
    for matrix in matrices: value = add(value, matrix[i][j])
    return value

def matrix_scale(r, matrix): return tuple(tuple(scale(r, matrix[i][j]) for j in range(N)) for i in range(N))
def dagger(matrix): return tuple(tuple(conj(matrix[j][i]) for j in range(N)) for i in range(N))
def hermitian(matrix): return matrix == dagger(matrix)

def determinant(matrix):
    size = len(matrix); total = q()
    for permutation in itertools.permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j] for i in range(size) for j in range(i + 1, size))
        term = q(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation): term = mul(term, matrix[row][column])
        total = add(total, term)
    return total

def principal(matrix, indices): return tuple(tuple(matrix[i][j] for j in indices) for i in indices)
def psd(matrix):
    return hermitian(matrix) and all((det := determinant(principal(matrix, indices)))[1] == 0 and det[0] >= 0 for size in range(1, N + 1) for indices in itertools.combinations(range(N), size))
def trace_product(a, b):
    value = q()
    for i in range(N):
        for j in range(N): value = add(value, mul(a[i][j], b[j][i]))
    return value

def kron(a, b):
    return tuple(tuple(mul(a[i // 2][j // 2], b[i % 2][j % 2]) for j in range(N)) for i in range(N))

I2 = ((q(1), q()), (q(), q(1)))
Y2 = ((q(), q(0, -1)), (q(0, 1), q()))
I = kron(I2, I2)
YI = kron(Y2, I2)
W = YI
A = YI
lower = F(1, 2)
y = F(0)
alpha = F(1)
slack = matrix_add(W, matrix_scale(-y, I), matrix_scale(-alpha, A))
dual_bound = y + alpha * lower
rho = matrix_scale(F(1, 4), matrix_add(I, matrix_scale(F(1, 2), YI)))
expectation = trace_product(YI, rho)
trace = trace_product(I, rho)

corrupt = [list(row) for row in rho]
corrupt[0][2] = add(corrupt[0][2], q(F(1, 100)))
corrupt = tuple(tuple(row) for row in corrupt)
corrupt_slack = matrix_add(W, matrix_scale(F(-3, 4), I), matrix_scale(-alpha, A))
all_paulis_hermitian = hermitian(I) and hermitian(YI)
checks = {
    "identity_and_phase_pauli_are_hermitian": all_paulis_hermitian,
    "phase_pauli_contains_imaginary_entries": any(value[1] != 0 for row in YI for value in row),
    "dual_slack_is_exactly_zero": all(value == q() for row in slack for value in row),
    "dual_slack_is_psd": psd(slack),
    "dual_bound_is_one_half": dual_bound == F(1, 2),
    "complex_primal_state_is_hermitian": hermitian(rho),
    "complex_primal_state_is_psd": psd(rho),
    "complex_primal_has_unit_trace": trace == q(1),
    "complex_primal_attains_bound": expectation == q(F(1, 2)),
    "unpaired_conjugation_corruption_is_rejected": not hermitian(corrupt) and not psd(corrupt),
    "indefinite_complex_slack_is_rejected": not psd(corrupt_slack),
    "all_principal_determinants_are_real": all(determinant(principal(rho, indices))[1] == 0 for size in range(1, N + 1) for indices in itertools.combinations(range(N), size)),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.gaussian-rational-hermitian-certificates.v1", "status": "passed", "checks": checks, "dual_bound": str(dual_bound), "primal_expectation": [str(value) for value in expectation], "claim_boundary": "Exact Q(i) 4x4 verifier; algebraic and transcendental entries remain outside scope."}
output = Path(__file__).parents[1] / "results" / "gaussian_rational_hermitian_certificates.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "dual_bound": str(dual_bound), "complex_entries": True}, sort_keys=True))
