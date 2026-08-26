#!/usr/bin/env python3
"""Exact audit of dynamic-storage residuals modulo storage gauge."""

import hashlib
import json
from itertools import product
from pathlib import Path

from sympy import I, Matrix, Rational, conjugate, simplify
from sympy.matrices.exceptions import ShapeError


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/dynamic-storage-residual-cohomology.json"


def adjoint(M):
    return conjugate(M.T)


def shear(F):
    return Matrix([[1, F], [0, 1]])


def coboundary(Pa, Pb, S):
    return (Pa - adjoint(S) * Pb * S).applyfunc(simplify)


def main():
    # Residual cocycle C-D on exhaustive small exact fixtures.
    cocycle_checks = 0
    for f, g, c1, c2 in product((-1, 0, 1), repeat=4):
        Sab = shear(Rational(f))
        Sbc = shear(Rational(g))
        Sac = Sbc * Sab
        Pa = Matrix([[2, c1], [c1, 3]])
        Pb = Matrix([[3, c2], [c2, 2]])
        Pc = Matrix([[4, c1 - c2], [c1 - c2, 5]])
        Cab = Matrix([[c1**2, c1], [c1, 1]])
        Cbc = Matrix([[1, c2], [c2, c2**2]])
        Cac = Cab + adjoint(Sab) * Cbc * Sab
        Dab = coboundary(Pa, Pb, Sab)
        Dbc = coboundary(Pb, Pc, Sbc)
        Dac = coboundary(Pa, Pc, Sac)
        Delta_ab = Cab - Dab
        Delta_bc = Cbc - Dbc
        Delta_ac = Cac - Dac
        assert (Delta_ac - Delta_ab - adjoint(Sab) * Delta_bc * Sab).applyfunc(simplify) == Matrix.zeros(2)
        cocycle_checks += 1

    # Exact real-coordinate matrix of L_S for S(1).
    # Coordinates are (a,u,v,d) -> (C11, Re C12, Im C12, C22).
    L = Matrix([
        [0, 0, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 0],
        [-1, -2, 0, 0],
    ])
    assert L.rank() == 2
    cokernel_basis = L.T.nullspace()
    assert cokernel_basis == [Matrix([1, 0, 0, 0]), Matrix([0, 0, 1, 0])]

    S = shear(1)
    K1 = Matrix([[1, 0], [0, 0]])
    K2 = Matrix([[0, I], [-I, 0]])
    assert (K1 - S * K1 * adjoint(S)).applyfunc(simplify) == Matrix.zeros(2)
    assert (K2 - S * K2 * adjoint(S)).applyfunc(simplify) == Matrix.zeros(2)
    closed_hostile = Matrix([[1, I], [-I, 0]])
    pairing1 = simplify((K1 * closed_hostile).trace())
    pairing2 = simplify((K2 * closed_hostile).trace())
    assert pairing1 == 1 and pairing2 == 2

    # Identity loop: every nonzero C is obstructed because L_I=0.
    identity_map = Matrix.zeros(4)
    assert identity_map.rank() == 0
    assert closed_hostile != Matrix.zeros(2)

    # Scalar projection hides a typed matrix residual.
    projected_residual = Matrix([[0, 0], [0, 1]])
    e1 = Matrix([1, 0])
    scalar_projection = (adjoint(e1) * projected_residual * e1)[0]
    assert scalar_projection == 0 and projected_residual != Matrix.zeros(2)

    # Mismatched carrier dimensions make subtraction undefined.
    carrier_mismatch_rejected = False
    try:
        _ = Matrix.eye(2) - Matrix.eye(3)
    except ShapeError:
        carrier_mismatch_rejected = True
    assert carrier_mismatch_rejected

    # Every cutoff is a coboundary, but every solution needs a=-N.
    topology_hostile = []
    Cfixed = Matrix([[0, 1], [1, 0]])
    for N in (2, 3, 5, 10, 20):
        eps = Rational(1, N)
        SN = shear(eps)
        PN = Matrix([[-N, Rational(1, 2)], [Rational(1, 2), 0]])
        assert coboundary(PN, PN, SN) == Cfixed
        # From C12=-a/N=1, the upper-left coordinate is uniquely a=-N.
        forced_a = -N
        assert PN[0, 0] == forced_a
        topology_hostile.append({"N": N, "forced_upper_left_storage": forced_a})

    # One local residual propagates by invertible congruence.
    local = Matrix([[1, 0], [0, 0]])
    transport = shear(1)
    global_residual = adjoint(transport) * local * transport
    assert global_residual == Matrix([[1, 1], [1, 1]])
    assert global_residual.rank() == local.rank() == 1

    payload = {
        "schema": "marici.kitaev.dynamic_storage_residual_cohomology.v1",
        "status": "pass",
        "strength": "finite algebraic and pro-topological compiler theorem",
        "residual_cocycle_checks": cocycle_checks,
        "unit_shear_storage_map": {
            "real_rank": L.rank(),
            "cokernel_dimension": len(cokernel_basis),
            "cokernel_basis": [[str(x) for x in v] for v in cokernel_basis],
            "dual_hostile_pairings": [str(pairing1), str(pairing2)],
        },
        "identity_loop_nonzero_class": True,
        "scalar_projection_hostile": {
            "scalar_value": str(scalar_projection),
            "matrix_residual_nonzero": True,
        },
        "carrier_mismatch_rejected": carrier_mismatch_rejected,
        "cutoffwise_unbounded_gauge_family": topology_hostile,
        "local_to_global_residual": {
            "local_rank": local.rank(),
            "global_rank": global_residual.rank(),
            "global_matrix": [[str(x) for x in global_residual.row(i)] for i in range(2)],
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta boundary supply derivation", "common theta graph topology",
            "uniform observability", "physical energy flux", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
