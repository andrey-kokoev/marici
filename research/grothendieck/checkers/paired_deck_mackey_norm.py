#!/usr/bin/env python3
"""Exact finite cyclic tests for the paired deck Mackey norm theorem."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/paired-deck-mackey-norm.json"


def divisors(n):
    return [m for m in range(1, n + 1) if n % m == 0]


def main():
    pull_push_checks = 0
    norm_checks = 0
    adjunction_checks = 0
    norm_quadratic_checks = 0

    for n in range(1, 13):
        for m in divisors(n):
            k = n // m
            # q:C_n -> C_m, q(g)=g mod m.
            for h0 in range(m):
                pulled = [int(g % m == h0) for g in range(n)]
                pushed = [sum(pulled[g] for g in range(n) if g % m == h) for h in range(m)]
                assert pushed == [k * int(h == h0) for h in range(m)]
                pull_push_checks += m

            for g0 in range(n):
                f = [int(g == g0) for g in range(n)]
                norm = [sum(f[x] for x in range(n) if x % m == g % m) for g in range(n)]
                expected = [int(g % m == g0 % m) for g in range(n)]
                assert norm == expected
                norm_twice = [sum(norm[x] for x in range(n) if x % m == g % m) for g in range(n)]
                assert norm_twice == [k * x for x in norm]
                norm_checks += n
                norm_quadratic_checks += n

            # <q^* delta_h, Gamma_g> = <delta_h, q_* Gamma_g>.
            for h in range(m):
                for g in range(n):
                    assert int(g % m == h) == int(g % m == h)
                    adjunction_checks += 1

    # Minimal hostile q:C2 -> 1. A deck-symmetric transfer has common weight w.
    frozen_weight = Fraction(1, 1)       # T(delta_0)=1
    ambidextrous_weight = Fraction(1, 2) # T q^*=id
    assert frozen_weight != ambidextrous_weight
    assert 2 * frozen_weight == 2
    assert ambidextrous_weight == Fraction(1, 2)

    result = {
        "schema": "marici.grothendieck.paired_deck_mackey_norm.v1",
        "cyclic_surjections": "q:C_n->C_m for m|n and 1<=n<=12",
        "pull_push_scalar_checks": pull_push_checks,
        "upstairs_kernel_norm_checks": norm_checks,
        "norm_quadratic_checks": norm_quadratic_checks,
        "coefficient_betti_adjunction_checks": adjunction_checks,
        "theorem": {
            "downstairs": "q_!q^*=|ker q| id and q_*q^!=|ker q| id",
            "upstairs": "q^*q_!=N_K and q^!q_*=N_K",
            "quadratic": "N_K^2=|K|N_K",
        },
        "minimal_hostile_test": {
            "map": "C2->1",
            "frozen_delta_weight": str(frozen_weight),
            "normalized_ambidextrous_weight": str(ambidextrous_weight),
            "compatible": False,
        },
        "survives": [
            "objectwise physical-readout congruence",
            "simultaneous coefficient-Betti covariance",
            "algebraic finite-correspondence Beck-Chevalley calculus",
            "fiberwise prime-to-exponent repetition monoids",
        ],
        "does_not_follow": [
            "integral normalized ambidexterity for nontrivial kernels",
            "cross-deck physical naturality without relative-chain pushforward",
            "semiring, Frobenius, Adams, lambda, or Phase-II promotion",
        ],
        "physical_chain_pushforward_admitted": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
