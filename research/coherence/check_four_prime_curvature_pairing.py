#!/usr/bin/env python3
"""Construct the antisymmetrized four-axis pairing of mixed curvature faces."""

import json
from pathlib import Path
import check_four_prime_cube_bianchi as cube


def d_axis(v, axis):
    out = [0] * cube.DIM
    a = cube.SHIFTS[axis]
    for mask in range(16):
        for x in range(cube.N):
            value = v[mask * cube.N + x]
            c = cube.creation(axis, mask)
            y = cube.R(a, x)
            if value and c is not None and y is not None:
                sign, target = c
                out[target * cube.N + y] += sign * value
    return out


def h_axis(v, axis):
    out = [0] * cube.DIM
    a = cube.SHIFTS[axis]
    for mask in range(16):
        for x in range(cube.N):
            value = v[mask * cube.N + x]
            i = cube.contraction(axis, mask)
            y = cube.S(a, x)
            if value and i is not None and y is not None:
                sign, target = i
                out[target * cube.N + y] += sign * value
    return out


def sum_vectors(*vectors):
    return [sum(values) for values in zip(*vectors)]


def face_curvature(v, p, q):
    """The complete mixed part of {d_p+d_q,h_p+h_q} on the pq face."""
    return sum_vectors(
        d_axis(h_axis(v, q), p), h_axis(d_axis(v, p), q),
        d_axis(h_axis(v, p), q), h_axis(d_axis(v, q), p),
    )


def four_pairing(v):
    """F01 F23 - F02 F13 + F03 F12: the oriented 4-cell pairing."""
    a = face_curvature(face_curvature(v, 2, 3), 0, 1)
    b = face_curvature(face_curvature(v, 1, 3), 0, 2)
    c = face_curvature(face_curvature(v, 1, 2), 0, 3)
    return [x - y + z for x, y, z in zip(a, b, c)]


def main():
    ordinary_trace = 0
    supertrace = 0
    nonzero_columns = []
    for j in range(cube.DIM):
        value = four_pairing(cube.basis(j))
        if any(value):
            nonzero_columns.append(j)
        diagonal = value[j]
        ordinary_trace += diagonal
        parity = (j // cube.N).bit_count() % 2
        supertrace += (-1 if parity else 1) * diagonal

    assert nonzero_columns
    assert ordinary_trace == 0
    assert supertrace == 0
    result = {
        "schema": "marici.coherence.four-prime-curvature-pairing.v1",
        "pairing": "F01 F23-F02 F13+F03 F12",
        "state_dimension": cube.DIM,
        "operator_nonzero": True,
        "nonzero_basis_columns": nonzero_columns,
        "ordinary_trace": ordinary_trace,
        "supertrace": supertrace,
        "conclusion": "the oriented 4-cell pairing exists operatorially but both naive scalar traces erase it in the finite contractible model",
    }
    target = Path(__file__).with_name("four-prime-curvature-pairing.v1.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
