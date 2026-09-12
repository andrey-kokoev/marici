#!/usr/bin/env python3
"""Exact finite-window check of the cube-level Bianchi cancellation."""

import json
from pathlib import Path

PRIMES = (2, 3, 5, 7)
SHIFTS = (1, 2, 3, 4)  # order-preserving discrete proxies for log(p)
N = 17
DIM = 16 * N


def creation(axis, mask):
    if mask & (1 << axis):
        return None
    sign = (-1) ** ((mask & ((1 << axis) - 1)).bit_count())
    return sign, mask | (1 << axis)


def contraction(axis, mask):
    if not mask & (1 << axis):
        return None
    sign = (-1) ** ((mask & ((1 << axis) - 1)).bit_count())
    return sign, mask ^ (1 << axis)


def R(a, x):
    return x + a if x + a < N else None


def S(a, x):
    return x - a if x >= a else None


def apply_D(v):
    out = [0] * DIM
    for mask in range(16):
        for x in range(N):
            value = v[mask * N + x]
            if not value:
                continue
            for axis, a in enumerate(SHIFTS):
                c = creation(axis, mask)
                y = R(a, x)
                if c is not None and y is not None:
                    sign, target = c
                    out[target * N + y] += sign * value
    return out


def apply_H(v):
    out = [0] * DIM
    for mask in range(16):
        for x in range(N):
            value = v[mask * N + x]
            if not value:
                continue
            for axis, a in enumerate(SHIFTS):
                i = contraction(axis, mask)
                y = S(a, x)
                if i is not None and y is not None:
                    sign, target = i
                    out[target * N + y] += sign * value
    return out


def add(a, b, sign=1):
    return [x + sign * y for x, y in zip(a, b)]


def apply_A(v):
    return add(apply_D(apply_H(v)), apply_H(apply_D(v)))


def basis(j):
    v = [0] * DIM
    v[j] = 1
    return v


def main():
    d2_failures = []
    bianchi_failures = []
    nonzero_curvature_columns = 0
    for j in range(DIM):
        v = basis(j)
        d2 = apply_D(apply_D(v))
        if any(d2):
            d2_failures.append(j)
        av = apply_A(v)
        if any(av):
            nonzero_curvature_columns += 1
        bianchi = add(apply_D(av), apply_A(apply_D(v)), sign=-1)
        if any(bianchi):
            bianchi_failures.append(j)

    assert not d2_failures
    assert nonzero_curvature_columns > 0
    assert not bianchi_failures
    result = {
        "schema": "marici.coherence.four-prime-cube-bianchi.v1",
        "primes": PRIMES,
        "discrete_shift_proxies": SHIFTS,
        "finite_seam_window": N,
        "state_dimension": DIM,
        "identity_D_squared_zero": True,
        "curvature_A_equals_DH_plus_HD_nonzero": True,
        "nonzero_curvature_basis_columns": nonzero_curvature_columns,
        "cube_bianchi_DA_minus_AD_zero": True,
        "interpretation": "nonzero square boundary defects form a covariantly closed cube packet",
    }
    target = Path(__file__).with_name("four-prime-cube-bianchi.v1.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
