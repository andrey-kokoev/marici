#!/usr/bin/env python3
"""Exact rational primal, dual, and infeasibility certificates for 4x4 SDPs."""

import itertools
import json
from fractions import Fraction
from pathlib import Path

F = Fraction
N = 4


def matrix_add(*matrices):
    return tuple(tuple(sum(matrix[i][j] for matrix in matrices) for j in range(N)) for i in range(N))


def matrix_scale(value, matrix):
    return tuple(tuple(value * matrix[i][j] for j in range(N)) for i in range(N))


def trace_product(a, b):
    return sum(a[i][j] * b[j][i] for i in range(N) for j in range(N))


def determinant(matrix):
    size = len(matrix)
    total = F(0)
    for permutation in itertools.permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j] for i in range(size) for j in range(i + 1, size))
        term = F(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def principal_submatrix(matrix, indices):
    return tuple(tuple(matrix[i][j] for j in indices) for i in indices)


def psd(matrix):
    return all(determinant(principal_submatrix(matrix, indices)) >= 0 for size in range(1, N + 1) for indices in itertools.combinations(range(N), size))


I = tuple(tuple(F(1 if i == j else 0) for j in range(N)) for i in range(N))
XX = ((0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0))
YY = ((0, 0, 0, -1), (0, 0, 1, 0), (0, 1, 0, 0), (-1, 0, 0, 0))
ZZ = ((1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, 1))
W = matrix_scale(F(1, 4), matrix_add(I, XX, matrix_scale(-1, YY), ZZ))
A = (XX, YY, ZZ)
lower = (F(4, 5), F(-1), F(4, 5))
upper = (F(1), F(-4, 5), F(1))
alpha = (F(1, 4), F(0), F(1, 4))
beta = (F(0), F(1, 4), F(0))
y = F(1, 4)
slack = matrix_add(W, matrix_scale(-y, I), *(matrix_scale(-alpha[i] + beta[i], A[i]) for i in range(3)))
dual_bound = y + sum(alpha[i] * lower[i] - beta[i] * upper[i] for i in range(3))

rho = matrix_scale(F(1, 4), matrix_add(I, matrix_scale(F(4, 5), XX), matrix_scale(F(-4, 5), YY), matrix_scale(F(4, 5), ZZ)))
primal_expectations = tuple(trace_product(operator, rho) for operator in A)
primal_objective = trace_product(W, rho)

# Infeasible duplicate XX slabs: lower 1 and upper -1.
infeasible_m = matrix_add(XX, matrix_scale(-1, XX))
infeasible_scalar = F(1) - F(-1)

# Corrupt y upward; slack should cease to be PSD.
corrupt_slack = matrix_add(W, matrix_scale(-F(1, 2), I), *(matrix_scale(-alpha[i] + beta[i], A[i]) for i in range(3)))
checks = {
    "dual_multipliers_are_nonnegative": all(value >= 0 for value in alpha + beta),
    "dual_slack_is_exactly_zero": all(entry == 0 for row in slack for entry in row),
    "dual_slack_is_psd": psd(slack),
    "dual_bound_is_seventeen_twentieths": dual_bound == F(17, 20),
    "primal_state_is_psd": psd(rho),
    "primal_state_has_unit_trace": trace_product(I, rho) == 1,
    "primal_expectations_satisfy_slabs": all(lower[i] <= primal_expectations[i] <= upper[i] for i in range(3)),
    "primal_attains_dual_bound": primal_objective == dual_bound,
    "infeasibility_matrix_is_negative_semidefinite": psd(matrix_scale(-1, infeasible_m)),
    "infeasibility_scalar_is_positive": infeasible_scalar == 2,
    "corrupted_certificate_is_rejected": not psd(corrupt_slack),
    "all_certificate_arithmetic_is_rational": all(isinstance(value, Fraction) for value in (dual_bound, primal_objective, infeasible_scalar)),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.exact-rational-sdp-certificates.v1", "status": "passed", "checks": checks, "dual_bound": str(dual_bound), "primal_objective": str(primal_objective), "infeasibility_scalar": str(infeasible_scalar), "corrupted_certificate_psd": psd(corrupt_slack), "claim_boundary": "Exact real-symmetric 4x4 verifier; complex Hermitian certificate support remains unresolved."}
output = Path(__file__).parents[1] / "results" / "exact_rational_sdp_certificates.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "dual_bound": str(dual_bound), "corrupt_rejected": not psd(corrupt_slack)}, sort_keys=True))
