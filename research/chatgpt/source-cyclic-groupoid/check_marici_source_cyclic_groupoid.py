#!/usr/bin/env python3
"""Exact audit of a normalized transport infinity-groupoid over a Marici packet.

Python 3.10+; standard library only. Run:
    python check_marici_source_cyclic_groupoid.py --output certificate.json

Source: andrey-kokoev/marici,
research/voevodsky/check_physical_derived_pullback_after_transform.py
Git blob: 7993b2b1bbdba03d05c3f443a45717d7b8efeec5

This audits the extracted chain matrices and the proposed cyclic action and
coherent marking. It does not rerun or certify the upstream geometric pipeline.
The accompanying note gives the all-dimensional proof.
"""
from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path

Vector = tuple[int, ...]
Matrix = tuple[Vector, ...]


def matvec(a: Matrix, v: Vector) -> Vector:
    if any(len(row) != len(v) for row in a):
        raise ValueError("Incompatible matrix/vector dimensions")
    return tuple(sum(x * y for x, y in zip(row, v)) for row in a)


def add(a: Vector, b: Vector) -> Vector:
    if len(a) != len(b):
        raise ValueError("Incompatible vector dimensions")
    return tuple(x + y for x, y in zip(a, b))


def sub(a: Vector, b: Vector) -> Vector:
    return add(a, tuple(-x for x in b))


def scale(k: int, a: Vector) -> Vector:
    return tuple(k * x for x in a)


def basis(n: int) -> tuple[Vector, ...]:
    return tuple(tuple(int(i == j) for i in range(n)) for j in range(n))


def rotate(v: Vector, exponent: int = 1) -> Vector:
    if len(v) < 3:
        return v
    prefix, road = v[:-3], v[-3:]
    for _ in range(exponent % 3):
        road = (road[2], road[0], road[1])
    return prefix + road


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


D1: Matrix = ((1, -1, -1, -1, -1),)
D2: Matrix = (
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 1, 0, -1),
    (0, -1, 1, 0),
    (0, 0, -1, 1),
)
D3: Matrix = ((0,), (1,), (1,), (1,))
Z: Vector = (1, 0, 1, 0, 0)
H: Vector = (0, -1, 0, 0)
K: Vector = (-1,)


def readout(v: Vector) -> int:
    if len(v) != 5:
        raise ValueError("Readout expects a degree-one chain")
    return sum(v[-3:])


def H_g(g: int) -> Vector:
    result: Vector = (0, 0, 0, 0)
    for i in range(g % 3):
        result = add(result, rotate(H, i))
    return result


def K_gh(g: int, h: int) -> int:
    return -((g % 3 + h % 3) // 3)


def boundary_preimage(v: Vector) -> Vector:
    """For a cycle v, solve d2(q) = v - readout(v)*Z integrally.

    The formula is an exact certificate that road augmentation induces an
    isomorphism H1(C) -> Z; it is not a bounded lattice search.
    """
    a, b, p0, p1, p2 = v
    if a - b != p0 + p1 + p2:
        raise ValueError("Input is not a cycle")
    return (b, -p1-p2, -p2, 0)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the JSON certificate")
    args = parser.parse_args()
    checks = 0

    def verify(condition: bool, message: str) -> None:
        nonlocal checks
        check(condition, message)
        checks += 1

    for v in basis(4):
        verify(matvec(D1, matvec(D2, v)) == (0,), "d1 d2")
        verify(rotate(matvec(D2, v)) == matvec(D2, rotate(v)), "cyclic d2")
        verify(readout(matvec(D2, v)) == 0, "readout of boundary")
    verify(matvec(D2, matvec(D3, (1,))) == (0,)*5, "d2 d3")
    verify(rotate(matvec(D3, (1,))) == matvec(D3, (1,)), "cyclic d3")
    for v in basis(5):
        verify(matvec(D1, rotate(v)) == matvec(D1, v), "cyclic d1")
        verify(readout(rotate(v)) == readout(v), "cyclic readout")
        verify(rotate(v, 3) == v, "order three")

    verify(matvec(D1, Z) == (0,), "primitive cycle")
    verify(readout(Z) == 1, "unit normalization")
    verify(matvec(D2, H) == sub(rotate(Z), Z), "one-rotation homotopy")
    norm_h = add(add(H, rotate(H)), rotate(H, 2))
    verify(matvec(D3, K) == norm_h, "three-rotation higher homotopy")
    verify(rotate(K) == K, "next cyclic compatibility")

    # Every cycle is parameterized by (b,p0,p1,p2), with a=b+p0+p1+p2.
    # Verify the linear certificate on this integral basis (therefore on all cycles).
    cycle_basis = (
        (1,1,0,0,0), (1,0,1,0,0), (1,0,0,1,0), (1,0,0,0,1)
    )
    for v in cycle_basis:
        q = boundary_preimage(v)
        verify(matvec(D2, q) == sub(v, scale(readout(v), Z)), "H1 certificate")

    # A direct integral chain contraction of the kernel of the normalized readout.
    # For q=(t,q0,q1,q2), q - s0(d2 q) = d3(q2).
    for q in basis(4):
        v = matvec(D2, q)
        verify(sub(q, boundary_preimage(v)) == matvec(D3, (q[3],)), "H2 certificate")
    verify(matvec(D3, (1,))[1] == 1, "d3 injective, primitive")
    verify(matvec(D1, (1,0,0,0,0)) == (1,), "d1 surjective")

    # Full normalized inhomogeneous bar identities: edges, triangles, tetrahedra.
    for g in range(3):
        verify(matvec(D2, H_g(g)) == sub(rotate(Z,g), Z), "bar edge")
    for g, h in product(range(3), repeat=2):
        delta = sub(add(H_g(g), rotate(H_g(h),g)), H_g((g+h)%3))
        verify(matvec(D3, (K_gh(g,h),)) == delta, "bar triangle")
    for g, h, ell in product(range(3), repeat=3):
        delta = (K_gh(h,ell) - K_gh((g+h)%3,ell)
                 + K_gh(g,(h+ell)%3) - K_gh(g,h))
        verify(delta == 0, "bar tetrahedron")

    # Strict fixed cycles have road vector (m,m,m), hence readout 3m.
    invariant_cycle_basis = ((1,1,0,0,0), (3,0,1,1,1))
    for v in invariant_cycle_basis:
        verify(rotate(v) == v and matvec(D1,v) == (0,), "invariant cycle basis")
    verify(tuple(readout(v) for v in invariant_cycle_basis) == (0,3), "fixed image 3Z")

    # Negative control from ledger 364/1555. The one-dimensional source subcomplex
    # has d(Omega)=c1; it suffices to certify this named class is a boundary, but
    # is not a reconstruction of the full Cousin complex.
    c1 = (1,)*6
    source_d0: Matrix = tuple((1,) for _ in range(6))
    source_d1: Matrix = tuple((0,)*6 for _ in range(3))
    verify(matvec(source_d0,(1,)) == c1, "first residue is a source boundary")
    verify(matvec(source_d1,c1) == (0,0,0), "first residue is closed")

    result = {
        "status": "PASS",
        "exact_checks": checks,
        "source_git_blob": "7993b2b1bbdba03d05c3f443a45717d7b8efeec5",
        "differentials": {"d1": D1, "d2": D2, "d3": D3},
        "homology": {"H0": "0", "H1": "Z", "H2": "0", "H3": "0"},
        "normalized_cycle": Z,
        "one_rotation_homotopy": H,
        "three_rotation_filler": K,
        "bar_triangles_checked": 9,
        "bar_tetrahedra_checked": 27,
        "strict_fixed_readout_image": "3Z",
        "strict_unit_marking": "absent",
        "normalized_marking_space": "contractible (proved in accompanying note)",
        "normalized_homotopy_fixed_space": "contractible (proved in accompanying note)",
        "normalized_transport_quotient": "B(C3) (proved in accompanying note)",
        "first_residue_negative_control": "exact; not a surviving absolute class",
        "scope": "Extracted integral complex and proposed cyclic action; upstream geometry not revalidated",
    }
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text+"\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
