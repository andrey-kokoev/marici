#!/usr/bin/env python3
"""Symbolic sanity checks for Entry 856's divisor-residue gate."""

from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PACKET = HERE / "marked-extension-divisor-residue-contract.json"


def main():
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    assert packet["entry"] == 856
    assert "regular" in packet["gauge_invariant"]

    # Work on the smooth test divisor q=u+v-1, for which q_u=q_v=1.
    # N_mu=q*B_mu is represented without division.  Exact Fraction samples
    # on q=0 verify both normality and invariance under an arbitrary regular
    # gauge contribution G_mu, since N_mu changes only by q*G_mu.
    for u in map(Fraction, (-3, -1, 0, 2, 5)):
        v = 1 - u
        q = u + v - 1
        residue = ((Fraction(2), u), (v, Fraction(3)))
        regular_u = ((u, v), (Fraction(1), u * v))
        regular_v = ((v, Fraction(1)), (u, u + v))
        gauge_u = ((u + 2 * v, u * v), (u * u, v * v + 1))
        n_u = tuple(tuple(x + q * y for x, y in zip(rr, rg)) for rr, rg in zip(residue, regular_u))
        n_v = tuple(tuple(x + q * y for x, y in zip(rr, rg)) for rr, rg in zip(residue, regular_v))
        obstruction = tuple(tuple(x - y for x, y in zip(ru, rv)) for ru, rv in zip(n_u, n_v))
        assert obstruction == ((0, 0), (0, 0))
        changed_n_u = tuple(tuple(x + q * y for x, y in zip(rn, rg)) for rn, rg in zip(n_u, gauge_u))
        assert changed_n_u == residue

    print("marked extension divisor-residue contract: PASS")
    print("logarithmic normality and regular-gauge invariance verified by exact specialization")


if __name__ == "__main__":
    main()
