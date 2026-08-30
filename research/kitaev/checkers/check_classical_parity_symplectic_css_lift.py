#!/usr/bin/env python3
"""Exact audit of the symplectic typing gate for CSS parity maps."""

import hashlib
import json
from itertools import product
from pathlib import Path

from sympy import Matrix, eye, kronecker_product


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/classical-parity-symplectic-css-lift.json"


def bits(number, width):
    return tuple((number >> i) & 1 for i in range(width))


def matvec(rows, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 2 for row in rows)


def transpose_product(left, right):
    return tuple(tuple(sum(a * b for a, b in zip(lrow, rrow)) % 2 for rrow in right) for lrow in left)


def gf2_rank(rows, n):
    values = [sum(bit << j for j, bit in enumerate(row)) for row in rows]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(values)) if (values[i] >> col) & 1), None)
        if pivot is None:
            continue
        values[rank], values[pivot] = values[pivot], values[rank]
        for i in range(len(values)):
            if i != rank and ((values[i] >> col) & 1):
                values[i] ^= values[rank]
        rank += 1
    return rank


def rowspace(rows, n):
    out = set()
    for mask in range(1 << len(rows)):
        value = [0] * n
        for i, row in enumerate(rows):
            if (mask >> i) & 1:
                value = [a ^ b for a, b in zip(value, row)]
        out.add(tuple(value))
    return out


def syndrome(hx, hz, x, z):
    return matvec(hx, z) + matvec(hz, x)


def systematic_distance(h, n):
    return min(sum(x) + sum(matvec(h, x)) for value in range(1, 1 << n) for x in [bits(value, n)])


def pauli_word(x, z):
    one = eye(2)
    px = Matrix([[0, 1], [1, 0]])
    pz = Matrix([[1, 0], [0, -1]])
    factors = []
    for xb, zb in zip(x, z):
        factors.append((px if xb else one) * (pz if zb else one))
    return kronecker_product(*factors)


def main():
    pairs_checked = 0
    commuting_pairs = 0
    noncommuting_pairs = 0
    quotient_checks = 0
    for n in range(1, 4):
        matrices = []
        for mask in range(1 << (2 * n)):
            matrices.append(tuple(tuple((mask >> (i * n + j)) & 1 for j in range(n)) for i in range(2)))
        for hx, hz in product(matrices, repeat=2):
            residual = transpose_product(hx, hz)
            commutes = not any(any(row) for row in residual)
            sx = rowspace(hx, n)
            sz = rowspace(hz, n)
            repairs = {(x, z) for x in sx for z in sz}
            descends = all(not any(syndrome(hx, hz, x, z)) for x, z in repairs)
            assert commutes == descends
            if commutes:
                centralizer = {
                    (bits(xi, n), bits(zi, n))
                    for xi in range(1 << n) for zi in range(1 << n)
                    if not any(syndrome(hx, hz, bits(xi, n), bits(zi, n)))
                }
                assert repairs <= centralizer
                rx, rz = gf2_rank(hx, n), gf2_rank(hz, n)
                k = n - rx - rz
                assert k >= 0
                assert len(centralizer) // len(repairs) == 1 << (2 * k)
                quotient_checks += 1
                commuting_pairs += 1
            else:
                assert any(any(syndrome(hx, hz, x, z)) for x, z in repairs)
                noncommuting_pairs += 1
            pairs_checked += 1

    hostile = ((1, 0), (0, 1), (1, 1))
    dx = systematic_distance(hostile, 2)
    dz = systematic_distance(hostile, 2)
    hostile_residual = transpose_product(hostile, hostile)
    assert dx == dz == 3
    assert any(any(row) for row in hostile_residual)
    x_check = pauli_word((1, 0), (0, 0))
    z_check = pauli_word((0, 0), (1, 0))
    assert x_check * z_check == -z_check * x_check
    assert x_check * z_check + z_check * x_check == Matrix.zeros(4)
    assert x_check * z_check - z_check * x_check != Matrix.zeros(4)

    payload = {
        "schema": "marici.kitaev.classical_parity_symplectic_css_lift.v1",
        "status": "pass",
        "strength": "finite-cutoff theorem",
        "field": "F2",
        "matrix_pairs_checked": pairs_checked,
        "commuting_pairs": commuting_pairs,
        "noncommuting_pairs": noncommuting_pairs,
        "logical_quotient_cardinality_checks": quotient_checks,
        "hostile_classical_fixture": {
            "H_X": [list(row) for row in hostile],
            "H_Z": [list(row) for row in hostile],
            "component_distances": [dx, dz],
            "commutator_residual": [list(row) for row in hostile_residual],
            "explicit_pauli_anticommutation": True,
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "physical Hamiltonian", "measurement circuit", "decoder",
            "threshold", "subsystem codes", "non-CSS codes"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
