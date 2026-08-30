#!/usr/bin/env python3
"""Exact bad-prime audit for normalized finite-deck kernel norms."""

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/deck-norm-bad-prime-locus.json"


def primes_through(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def matmul(a, b, modulus=None):
    size = len(a)
    c = [[sum(a[i][t] * b[t][j] for t in range(size)) for j in range(size)] for i in range(size)]
    if modulus:
        c = [[x % modulus for x in row] for row in c]
    return c


def main():
    integral_checks = 0
    good_prime_projector_checks = 0
    bad_prime_nilpotence_checks = 0
    records = []

    for k in range(2, 13):
        # Regular cyclic K action: N_K is the all-ones matrix.
        norm = [[1 for _ in range(k)] for _ in range(k)]
        square = matmul(norm, norm)
        assert square == [[k for _ in range(k)] for _ in range(k)]
        integral_checks += k * k
        bad = []
        good = []
        for p in primes_through(13):
            if k % p == 0:
                n2 = matmul(norm, norm, p)
                assert all(x == 0 for row in n2 for x in row)
                assert any((x % p) != 0 for row in norm for x in row)
                bad_prime_nilpotence_checks += k * k
                bad.append(p)
            else:
                inv = pow(k, -1, p)
                projector = [[inv % p for _ in range(k)] for _ in range(k)]
                assert matmul(projector, projector, p) == projector
                good_prime_projector_checks += k * k
                good.append(p)
        records.append({
            "kernel_order": k,
            "bad_primes": bad,
            "tested_good_primes": good,
            "radical": [p for p in primes_through(k) if k % p == 0],
        })

    # Integral scalar normalization a*N with (a*N)^2=a*N requires ak=1.
    # No integer a exists for k>1; localization at k supplies a=1/k.
    assert all(gcd(k, 1) == 1 and 1 % k != 0 for k in range(2, 13))

    result = {
        "schema": "marici.grothendieck.deck_norm_bad_prime_locus.v1",
        "kernel_orders": "2..12",
        "integral_norm_quadratic_checks": integral_checks,
        "good_prime_projector_checks": good_prime_projector_checks,
        "bad_prime_square_zero_checks": bad_prime_nilpotence_checks,
        "records": records,
        "theorem": (
            "The normalized projector e_K=N_K/|K| exists after inverting |K|; "
            "its integral obstruction is supported on V(|K|), and modulo every "
            "p dividing |K| the nonzero norm satisfies N_K^2=0."
        ),
        "arithmetic_scope": (
            "Derived from an independently integral coefficient lattice and deck multiplicity; "
            "not a derivation of Spec(Z), primes, or arithmetic from the bare Carrier."
        ),
        "physical_scope": "No physical relative-chain pushforward is inferred.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
