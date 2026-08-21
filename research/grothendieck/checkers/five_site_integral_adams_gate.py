#!/usr/bin/env python3
"""Exact Adams-operation and physical-selection gate for Z[(C2)^5]."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/five-site-integral-adams-gate.json"
SIZE = 32


def convolution(a, b, modulus=None):
    out = [0] * SIZE
    for g, x in enumerate(a):
        for h, y in enumerate(b):
            out[g ^ h] += x * y
    if modulus:
        out = [x % modulus for x in out]
    return out


def adams(a, n, modulus=None):
    out = [0] * SIZE
    for g, x in enumerate(a):
        target = g if n % 2 else 0
        out[target] += x
    if modulus:
        out = [x % modulus for x in out]
    return out


def power(a, n, modulus):
    result = [1] + [0] * (SIZE - 1)
    base = [x % modulus for x in a]
    while n:
        if n & 1:
            result = convolution(result, base, modulus)
        base = convolution(base, base, modulus)
        n //= 2
    return result


def main():
    ring_hom_checks = 0
    for n in range(1, 13):
        for g in range(SIZE):
            eg = [int(i == g) for i in range(SIZE)]
            for h in range(SIZE):
                eh = [int(i == h) for i in range(SIZE)]
                assert adams(convolution(eg, eh), n) == convolution(adams(eg, n), adams(eh, n))
                ring_hom_checks += 1

    composition_checks = 0
    for m in range(1, 13):
        for n in range(1, 13):
            for g in range(SIZE):
                eg = [int(i == g) for i in range(SIZE)]
                assert adams(adams(eg, n), m) == adams(eg, m * n)
                composition_checks += 1

    vectors = []
    for seed in range(64):
        vectors.append([((seed + 3 * g + (g ^ seed)) % 7) - 3 for g in range(SIZE)])
    frobenius_congruence_checks = 0
    for p in (2, 3, 5, 7):
        for vector in vectors:
            assert adams(vector, p, p) == power(vector, p, p)
            frobenius_congruence_checks += SIZE

    # On coefficients, the dual pullback sends delta_0 to delta_0 for odd n
    # and to the constant-one function for even n.
    physical_selection = []
    for n in range(1, 13):
        pulled_delta = [int((g if n % 2 else 0) == 0) for g in range(SIZE)]
        mismatches = sum(x != int(g == 0) for g, x in enumerate(pulled_delta))
        assert mismatches == (0 if n % 2 else 31)
        physical_selection.append({"n": n, "mismatches": mismatches, "preserved": mismatches == 0})

    result = {
        "schema": "marici.grothendieck.five_site_integral_adams_gate.v1",
        "ring": "Z[(C2)^5] with each deck character declared a line element",
        "ring_homomorphism_checks": ring_hom_checks,
        "adams_composition_checks": composition_checks,
        "frobenius_congruence_checks": frobenius_congruence_checks,
        "physical_selection": physical_selection,
        "algebraic_result": (
            "The canonical representation-ring lambda structure has Adams operations "
            "psi^n(g)=g^n and psi^m psi^n=psi^(mn), with Frobenius congruences."
        ),
        "physical_result": (
            "The dual coefficient identity selection is preserved exactly for odd n; "
            "every even Adams operation changes 31 of 32 sheet values."
        ),
        "scope": (
            "A conditional algebraic lambda-ring on the integral Betti deck lattice, "
            "not a common physical readout lambda-ring and not Carrier-derived arithmetic."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
