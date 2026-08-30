#!/usr/bin/env python3
"""Modular minimal recurrence for the flag determinant scalar."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

PRIMES = (1000003, 1000033, 1000037)
TERM_COUNT = 220
TRAIN_COUNT = 150
LAMBDA_TRACE = 147458
S = (
    (1, 1, 0, 1),
    (1, 1, 1, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 0),
)
SI = (
    (0, 0, 0, 1),
    (1, 0, 0, -1),
    (-1, 1, 0, 0),
    (1, -1, 1, -1),
)


def matmul(a, b, p):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) % p
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mod_matrix(a, p):
    return tuple(tuple(x % p for x in row) for row in a)


def inverse_matrix(a, p):
    n = len(a)
    x = [
        [a[i][j] % p for j in range(n)] + [int(i == j) for j in range(n)]
        for i in range(n)
    ]
    for column in range(n):
        pivot = next(r for r in range(column, n) if x[r][column] % p)
        x[column], x[pivot] = x[pivot], x[column]
        scale = pow(x[column][column], -1, p)
        x[column] = [(v * scale) % p for v in x[column]]
        for r in range(n):
            if r != column and x[r][column] % p:
                scale = x[r][column]
                x[r] = [(v - scale * w) % p for v, w in zip(x[r], x[column])]
    return tuple(tuple(row[n:]) for row in x)


def commutator(left, left_i, right, right_i, p):
    return matmul(matmul(matmul(right_i, left_i, p), right, p), left, p)


def det3(a, p):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % p


def scalar_sequence(p):
    C = mod_matrix(source["C"], p)
    Ci = mod_matrix(source["Ci"], p)
    X = mod_matrix(source["X"], p)
    Xi = mod_matrix(source["Xi"], p)
    Z = mod_matrix(source["Z"], p)
    Zi = mod_matrix(source["Zi"], p)
    right = mod_matrix(source["right_block"], p)
    right_i = mod_matrix(source["right_block_i"], p)
    Sm = mod_matrix(S, p)
    Sim = mod_matrix(SI, p)
    U = identity(4)
    V = identity(4)
    answer = []
    for _ in range(TERM_COUNT):
        tail = matmul(U, X, p)
        tail_i = matmul(Xi, V, p)
        left = commutator(Z, Zi, tail, tail_i, p)
        left_i = commutator(tail, tail_i, Z, Zi, p)
        response = commutator(left, left_i, right, right_i, p)
        delta = tuple(
            tuple((response[i][j] - int(i == j)) % p for j in range(4))
            for i in range(4)
        )
        adapted = matmul(matmul(Sim, delta, p), Sm, p)
        k = tuple(tuple(adapted[i][j] for j in range(1, 4)) for i in range(3))
        answer.append(det3(k, p))
        U = matmul(C, U, p)
        V = matmul(Ci, V, p)
    return answer


def berlekamp_massey(sequence, p):
    c = [1]
    b = [1]
    length = 0
    shift = 1
    last = 1
    for n in range(len(sequence)):
        discrepancy = sequence[n] % p
        for i in range(1, length + 1):
            discrepancy = (discrepancy + c[i] * sequence[n - i]) % p
        if discrepancy == 0:
            shift += 1
            continue
        old = c[:]
        scale = discrepancy * pow(last, -1, p) % p
        needed = len(b) + shift
        if len(c) < needed:
            c.extend([0] * (needed - len(c)))
        for j, value in enumerate(b):
            c[j + shift] = (c[j + shift] - scale * value) % p
        if 2 * length <= n:
            length = n + 1 - length
            b = old
            last = discrepancy
            shift = 1
        else:
            shift += 1
    return c[:length + 1]


def recurrence_holds(c, sequence, start, p):
    length = len(c) - 1
    return all(
        sum(c[i] * sequence[n - i] for i in range(length + 1)) % p == 0
        for n in range(max(start, length), len(sequence))
    )


def poly_mul(a, b, p):
    answer = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i + j] = (answer[i + j] + x * y) % p
    return answer


def poly_pow(a, exponent, p):
    answer = [1]
    for _ in range(exponent):
        answer = poly_mul(answer, a, p)
    return answer


def poly_remainder(dividend, divisor, p):
    a = dividend[:]
    while len(a) >= len(divisor):
        if a[-1]:
            scale = a[-1] * pow(divisor[-1], -1, p) % p
            offset = len(a) - len(divisor)
            for i, x in enumerate(divisor):
                a[offset + i] = (a[offset + i] - scale * x) % p
        while a and a[-1] == 0:
            a.pop()
    return a


def envelope(max_mode, p, multiplicity=7):
    answer = poly_pow([p - 1, 1], multiplicity, p)
    s0, s1 = 2 % p, LAMBDA_TRACE % p
    values = [s0, s1]
    for _ in range(1, max_mode):
        values.append((LAMBDA_TRACE * values[-1] - values[-2]) % p)
    for j in range(1, max_mode + 1):
        answer = poly_mul(
            answer,
            poly_pow([1, (-values[j]) % p, 1], multiplicity, p),
            p,
        )
    return answer


records = []
for p in PRIMES:
    sequence = scalar_sequence(p)
    connection = berlekamp_massey(sequence[:TRAIN_COUNT], p)
    characteristic = list(reversed(connection))
    heldout = recurrence_holds(connection, sequence, TRAIN_COUNT, p)
    discriminant_nonzero = (LAMBDA_TRACE * LAMBDA_TRACE - 4) % p != 0
    divides_63 = not poly_remainder(envelope(4, p), characteristic, p)
    divides_49 = not poly_remainder(envelope(3, p), characteristic, p)
    squarefree_degree_9 = characteristic == envelope(4, p, multiplicity=1)
    records.append({
        "prime": p,
        "discriminant_nonzero": discriminant_nonzero,
        "minimal_degree": len(connection) - 1,
        "heldout_terms": TERM_COUNT - TRAIN_COUNT,
        "heldout_passed": heldout,
        "divides_degree_63_envelope": divides_63,
        "divides_degree_49_envelope": divides_49,
        "equals_squarefree_degree_9_envelope": squarefree_degree_9,
        "connection_coefficients": connection,
    })

degrees = {x["minimal_degree"] for x in records}
gates = {
    "all_auxiliary_primes_are_good": all(x["discriminant_nonzero"] for x in records),
    "minimal_degree_is_prime_independent": len(degrees) == 1,
    "all_heldout_terms_pass": all(x["heldout_passed"] for x in records),
    "all_minimal_recurrences_divide_degree_63_envelope":
        all(x["divides_degree_63_envelope"] for x in records),
    "all_minimal_recurrences_equal_squarefree_degree_9_envelope":
        all(x["equals_squarefree_degree_9_envelope"] for x in records),
}
payload = {
    "schema": "marici.strominger.flag_scalar_modular_recurrence_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "term_count": TERM_COUNT,
    "training_terms": TRAIN_COUNT,
    "records": records,
    "common_minimal_degree": next(iter(degrees)) if len(degrees) == 1 else None,
    "degree_49_model_survives": all(x["divides_degree_49_envelope"] for x in records),
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
