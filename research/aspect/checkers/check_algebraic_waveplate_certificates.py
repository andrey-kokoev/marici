#!/usr/bin/env python3
"""Exact Q(sqrt(2),i) certificates for balanced and quarter-phase analyzers."""

import json
from fractions import Fraction as F
from pathlib import Path


def k(a=0, b=0, c=0, d=0): return F(a), F(b), F(c), F(d)
def add(x, y): return tuple(x[i] + y[i] for i in range(4))
def neg(x): return tuple(-value for value in x)
def scale(r, x): return tuple(r * value for value in x)
def mul(x, y):
    a, b, c, d = x; e, f, g, h = y
    real_a = a * e + 2 * b * f - c * g - 2 * d * h
    real_b = a * f + b * e - c * h - d * g
    imag_a = a * g + 2 * b * h + c * e + 2 * d * f
    imag_b = a * h + b * g + c * f + d * e
    return real_a, real_b, imag_a, imag_b
def conj(x): return x[0], x[1], -x[2], -x[3]

def matmul(a, b):
    return tuple(tuple(sum_k(mul(a[i][r], b[r][j]) for r in range(2)) for j in range(2)) for i in range(2))
def sum_k(values):
    result = k()
    for value in values: result = add(result, value)
    return result
def dagger(a): return tuple(tuple(conj(a[j][i]) for j in range(2)) for i in range(2))
def matscale(r, a): return tuple(tuple(scale(r, value) for value in row) for row in a)
def hermitian(a): return a == dagger(a)
def trace(a): return add(a[0][0], a[1][1])
def determinant(a): return add(mul(a[0][0], a[1][1]), neg(mul(a[0][1], a[1][0])))
def real_sign(x):
    assert x[2] == 0 and x[3] == 0
    a, b = x[0], x[1]
    if b == 0: return (a > 0) - (a < 0)
    if a == 0: return (b > 0) - (b < 0)
    if (a > 0) == (b > 0): return (a > 0) - (a < 0)
    comparison = a * a - 2 * b * b
    if comparison == 0: return 0
    return ((a > 0) - (a < 0)) if comparison > 0 else ((b > 0) - (b < 0))
def psd(a): return hermitian(a) and real_sign(a[0][0]) >= 0 and real_sign(a[1][1]) >= 0 and real_sign(determinant(a)) >= 0

ZERO = k(); ONE = k(1); IUNIT = k(0, 0, 1); INV_SQRT2 = k(0, F(1, 2))
IDENTITY = ((ONE, ZERO), (ZERO, ONE))
H = ((INV_SQRT2, INV_SQRT2), (INV_SQRT2, neg(INV_SQRT2)))
S = ((ONE, ZERO), (ZERO, IUNIT))
X = ((ZERO, ONE), (ONE, ZERO))
Z = ((ONE, ZERO), (ZERO, neg(ONE)))
Y = ((ZERO, neg(IUNIT)), (IUNIT, ZERO))
P0 = ((ONE, ZERO), (ZERO, ZERO))
U = matmul(S, H)
E = matmul(dagger(U), matmul(P0, U))

DEC = k(F(707, 1000))
H_DEC = ((DEC, DEC), (DEC, neg(DEC)))
decimal_norm = matmul(dagger(H_DEC), H_DEC)
checks = {
    "balanced_amplitude_squares_to_one_half": mul(INV_SQRT2, INV_SQRT2) == k(F(1, 2)),
    "balanced_interferometer_is_exactly_unitary": matmul(dagger(H), H) == IDENTITY,
    "quarter_phase_is_exactly_unitary": matmul(dagger(S), S) == IDENTITY,
    "which_path_to_interference_identity": matmul(H, matmul(Z, H)) == X,
    "quarter_phase_rotates_x_to_y": matmul(S, matmul(X, dagger(S))) == Y,
    "analyzer_effect_is_hermitian": hermitian(E),
    "analyzer_effect_is_idempotent": matmul(E, E) == E,
    "analyzer_effect_has_unit_trace": trace(E) == ONE,
    "analyzer_effect_is_positive": psd(E),
    "decimal_substitution_is_not_unitary": decimal_norm != IDENTITY,
    "decimal_norm_residual_is_exact": decimal_norm[0][0] == k(F(999698, 1000000)),
    "algebraic_entries_are_not_coerced_to_decimal": INV_SQRT2 != DEC,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.algebraic-waveplate-certificates.v1", "status": "passed", "checks": checks, "field": "Q(sqrt(2),i)", "decimal_norm": [str(value) for value in decimal_norm[0][0]], "claim_boundary": "Exact balanced and quarter-phase two-mode analyzers; arbitrary angles remain outside scope."}
output = Path(__file__).parents[1] / "results" / "algebraic_waveplate_certificates.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "field": result["field"]}, sort_keys=True))
