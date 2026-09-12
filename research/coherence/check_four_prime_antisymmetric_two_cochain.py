#!/usr/bin/env python3
"""Construct the source-antisymmetrized window 2-cochain and its 4-cup."""

import json
from fractions import Fraction
from pathlib import Path

PRIMES = (2, 3, 5, 7)
SHIFTS = (1, 2, 3, 4)
N = 30
LEFT_WIDTH = max(SHIFTS)


def add(a, b, sign=1): return [x + sign * y for x, y in zip(a, b)]
def R(a, v): return v[a:] + [0] * a
def S(a, v): return [0] * a + v[:N-a]
def basis(x):
    v = [0] * N; v[x] = 1; return v


def raw_K(q, p, v):
    return add(R(SHIFTS[q], S(SHIFTS[p], v)), S(SHIFTS[p], R(SHIFTS[q], v)), -1)


def F(i, j, v):
    """Canonical alternation K_{j,i}-K_{i,j}; F(j,i)=-F(i,j)."""
    return add(raw_K(j, i, v), raw_K(i, j, v), -1)


def comm_R(i, op, v):
    return add(R(SHIFTS[i], op(v)), op(R(SHIFTS[i], v)), -1)


def bianchi(i, j, k, v):
    return [sum(z) for z in zip(
        comm_R(i, lambda w: F(j, k, w), v),
        comm_R(j, lambda w: F(k, i, w), v),
        comm_R(k, lambda w: F(i, j, w), v),
    )]


def anticomposed(i, j, k, l, v):
    return add(F(i, j, F(k, l, v)), F(k, l, F(i, j, v)))


def cup4(v):
    a = anticomposed(0, 1, 2, 3, v)
    b = anticomposed(0, 2, 1, 3, v)
    c = anticomposed(0, 3, 1, 2, v)
    return [x-y+z for x, y, z in zip(a, b, c)]


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]; r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][col]; a[r] = [x/scale for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                scale = a[i][col]; a[i] = [x-scale*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


def main():
    triples = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
    assert all(not any(bianchi(*t, basis(x))) for t in triples for x in range(N))
    full = [[cup4(basis(x))[y] for x in range(N)] for y in range(N)]
    left = [row[:LEFT_WIDTH] for row in full[:LEFT_WIDTH]]
    result = {
        "schema": "marici.coherence.four-prime-antisymmetric-two-cochain.v1",
        "two_cochain": "F_ij=K_(j,i)-K_(i,j)",
        "antisymmetric": True,
        "all_four_bianchi_residuals_zero": True,
        "four_cup": "{F01,F23}-{F02,F13}+{F03,F12}",
        "four_cup_nonzero": any(any(row) for row in full),
        "left_boundary_width": LEFT_WIDTH,
        "left_boundary_rank": rank(left),
        "left_boundary_matrix": left,
        "full_trace": sum(full[i][i] for i in range(N)),
        "warning": "integer shifts are an exact incidence model; a continuum logarithmic completion remains separate",
    }
    assert result["four_cup_nonzero"] and result["left_boundary_rank"] > 0
    target = Path(__file__).with_name("four-prime-antisymmetric-two-cochain.v1.json")
    target.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("antisymmetric","all_four_bianchi_residuals_zero","four_cup_nonzero","left_boundary_rank","full_trace")}, indent=2))


if __name__ == "__main__": main()
