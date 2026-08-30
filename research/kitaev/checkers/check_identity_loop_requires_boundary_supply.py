#!/usr/bin/env python3
"""Exact audit of dynamic storage and supply cocycles."""

import hashlib
import json
from itertools import product
from pathlib import Path

from sympy import I, Matrix, Rational, conjugate, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/identity-loop-requires-boundary-supply.json"


def adjoint(M):
    return conjugate(M.T)


def shear(F):
    return Matrix([[1, F], [0, 1]])


def defect(Pa, Pb, S):
    return (Pa - adjoint(S) * Pb * S).applyfunc(simplify)


def supply(W, Pa, Pb, S):
    return (W + adjoint(S) * Pb * S - Pa).applyfunc(simplify)


def main():
    cocycle_checks = 0
    values = (-1, 0, 1)
    for f, g in product(values, repeat=2):
        Sab = shear(Rational(f))
        Sbc = shear(Rational(g))
        Sac = Sbc * Sab
        for pa, pb, pc in product(values, repeat=3):
            Pa = Matrix([[2, pa], [pa, 3]])
            Pb = Matrix([[3, pb], [pb, 2]])
            Pc = Matrix([[4, pc], [pc, 5]])
            Dab = defect(Pa, Pb, Sab)
            Dbc = defect(Pb, Pc, Sbc)
            Dac = defect(Pa, Pc, Sac)
            assert (Dac - Dab - adjoint(Sab) * Dbc * Sab).applyfunc(simplify) == Matrix.zeros(2)

            Ja = Matrix([[1, pa]])
            Jb = Matrix([[pb, 1]])
            Wab = adjoint(Ja) * Ja
            Wbc = adjoint(Jb) * Jb
            Wac = Wab + adjoint(Sab) * Wbc * Sab
            Qab = supply(Wab, Pa, Pb, Sab)
            Qbc = supply(Wbc, Pb, Pc, Sbc)
            Qac = supply(Wac, Pa, Pc, Sac)
            assert (Qac - Qab - adjoint(Sab) * Qbc * Sab).applyfunc(simplify) == Matrix.zeros(2)
            assert (Wac - Dac - Qac).applyfunc(simplify) == Matrix.zeros(2)
            cocycle_checks += 1

    # Positive identity-loop energy with equal endpoint storage.
    F = Rational(2, 3) + Rational(1, 2) * I
    S1 = shear(F)
    S2 = shear(-F)
    total = S2 * S1
    assert total == Matrix.eye(2)
    C = Matrix([[1, 0]])
    Wseg = adjoint(C) * C
    Wloop = Wseg + adjoint(S1) * Wseg * S1
    assert simplify(Wloop.det()) == Rational(25, 36)
    assert Wloop[0, 0] > 0 and Wloop.det() > 0

    # Any equal endpoint storage has zero total defect on identity holonomy.
    P = Matrix([[3, 1 + I], [1 - I, 4]])
    Dloop = defect(P, P, total)
    assert Dloop == Matrix.zeros(2)
    assert Wloop != Dloop
    Qloop = supply(Wloop, P, P, total)
    supply_equals_gramian = (Qloop - Wloop).applyfunc(simplify) == Matrix.zeros(2)
    assert supply_equals_gramian
    assert (Wloop - Dloop - Qloop).applyfunc(simplify) == Matrix.zeros(2)

    # Segment supplies compose to the loop supply.
    Pmid = Matrix([[2, I], [-I, 5]])
    Q1 = supply(Wseg, P, Pmid, S1)
    Q2 = supply(Wseg, Pmid, P, S2)
    assert (Qloop - Q1 - adjoint(S1) * Q2 * S1).applyfunc(simplify) == Matrix.zeros(2)

    payload = {
        "schema": "marici.kitaev.identity_loop_requires_boundary_supply.v1",
        "status": "pass",
        "strength": "finite algebraic compiler theorem",
        "storage_and_supply_cocycle_checks": cocycle_checks,
        "identity_loop_hostile": {
            "F": str(F),
            "total_transport": "I_2",
            "path_gramian": [[str(z) for z in Wloop.row(i)] for i in range(2)],
            "gramian_determinant": str(simplify(Wloop.det())),
            "total_storage_defect": [[str(z) for z in Dloop.row(i)] for i in range(2)],
            "required_total_supply_equals_gramian": supply_equals_gramian,
        },
        "segment_supply_composition": "pass",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta boundary supply derivation", "theta sensor rows",
            "uniform lower bound", "physical energy flux", "passivity", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
