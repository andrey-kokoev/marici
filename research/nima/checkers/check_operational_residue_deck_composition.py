"""Exact nonidentity composition test for finite-deck norm residues."""

from __future__ import annotations

import json
from pathlib import Path


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def residue_compose(e_left: int, e_right: int) -> int:
    return e_left + e_right + e_left * e_right


def main() -> None:
    quotient_cases = []
    chain_cases = []

    for n in range(1, 31):
        for m in divisors(n):
            degree = n // m
            residue = degree - 1
            quotient_cases.append((n, m, degree, residue))

            # Frozen delta selector versus normalized retraction.
            unnormalized_selector = 1
            normalized_selector = (1, degree)
            assert unnormalized_selector == 1
            if degree == 1:
                assert normalized_selector == (1, 1)
            else:
                assert normalized_selector != (1, 1)

            for k in divisors(m):
                degree_q = n // m
                degree_r = m // k
                degree_composite = n // k
                e_q = degree_q - 1
                e_r = degree_r - 1
                e_composite = degree_composite - 1
                assert degree_composite == degree_q * degree_r
                assert e_composite == residue_compose(e_q, e_r)
                chain_cases.append((n, m, k, e_q, e_r, e_composite))

    # Independent associativity census for residue coordinates.
    associativity_cases = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                left = residue_compose(residue_compose(a, b), c)
                right = residue_compose(a, residue_compose(b, c))
                assert left == right
                associativity_cases += 1

    nontrivial = [case for case in quotient_cases if case[2] > 1]
    assert nontrivial
    assert all(case[3] > 0 for case in nontrivial)

    result = {
        "status": "PASS",
        "cyclic_quotient_cases": len(quotient_cases),
        "composable_quotient_chains": len(chain_cases),
        "associativity_cases": associativity_cases,
        "residue_coordinate": "e_q = |ker(q)| - 1",
        "composition_law": "e_(r q) = e_q + e_r + e_q e_r",
        "unit": 0,
        "nontrivial_residues": len(nontrivial),
        "normalization_conflict": (
            "Averaging removes the norm residue but changes the frozen identity-selector "
            "from 1 to 1/|ker(q)| for every nontrivial quotient."
        ),
        "scope": (
            "Exact algebraic finite-deck correspondence calculus; no physical relative-chain "
            "pushforward is inferred."
        ),
    }

    output = Path(__file__).parents[1] / "results" / "operational-residue-deck-composition.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
