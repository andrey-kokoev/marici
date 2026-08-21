#!/usr/bin/env python3
"""Exact composition law for five-site mod-two branch norms."""

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/five-site-mod2-branch-norm-composition.json"


def multiply_monomials(a, b):
    return None if a & b else a | b


def main():
    disjoint_checks = 0
    overlap_zero_checks = 0
    for a in range(1, 32):
        for b in range(1, 32):
            product = multiply_monomials(a, b)
            if a & b:
                assert product is None
                overlap_zero_checks += 1
            else:
                assert product == (a | b)
                disjoint_checks += 1
    assert disjoint_checks == 180
    assert overlap_zero_checks == 781

    flag_checks = 0
    flag_profile = {}
    for subset in range(1, 32):
        bits = [i for i in range(5) if subset & (1 << i)]
        count = 0
        for order in itertools.permutations(bits):
            product = 0
            for i in order:
                product = multiply_monomials(product, 1 << i)
                assert product is not None
            assert product == subset
            count += 1
            flag_checks += 1
        assert count == math.factorial(len(bits))
        flag_profile[str(len(bits))] = flag_profile.get(str(len(bits)), 0) + count
    assert flag_checks == 325

    # Repeating any already-used branch generator kills the composite.
    repeated_direction_checks = 0
    for subset in range(1, 32):
        for i in range(5):
            if subset & (1 << i):
                assert multiply_monomials(subset, 1 << i) is None
                repeated_direction_checks += 1
    assert repeated_direction_checks == 80

    result = {
        "schema": "marici.grothendieck.five_site_mod2_branch_norm_composition.v1",
        "ordered_nonempty_pair_checks": 961,
        "disjoint_union_products": disjoint_checks,
        "overlap_zero_products": overlap_zero_checks,
        "ordered_flag_coherence_checks": flag_checks,
        "flag_profile_by_terminal_codimension": flag_profile,
        "repeated_direction_zero_checks": repeated_direction_checks,
        "law": "N_A N_B=N_(A union B) if A intersect B is empty; otherwise N_A N_B=0",
        "classification": "exterior/Stanley-Reisner square-zero branch-incidence shadow over F2",
        "physical_composition_admitted": False,
        "arithmetic_promotion": False,
        "reason": (
            "The algebraic flag products are coherent and order-independent, but no source-derived "
            "composition of physical relative-chain specializations is present."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
