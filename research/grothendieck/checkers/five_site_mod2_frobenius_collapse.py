#!/usr/bin/env python3
"""Hostile Frobenius test on the five-site mod-two deck algebra."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/five-site-mod2-frobenius-collapse.json"


def monomial_product(a, b):
    return None if a & b else a | b


def main():
    basis_square_checks = 0
    for mask in range(32):
        square = monomial_product(mask, mask)
        expected = 0 if mask == 0 else None
        assert square == expected
        basis_square_checks += 1

    # In characteristic two, cross terms in (x+y)^2 cancel pairwise.
    cross_term_cancellation_checks = 0
    for a in range(32):
        for b in range(a + 1, 32):
            ab = monomial_product(a, b)
            ba = monomial_product(b, a)
            assert ab == ba
            # Equal terms occur twice, hence sum to zero in F2.
            cross_term_cancellation_checks += 1
    assert cross_term_cancellation_checks == 496

    branch_norm_frobenius_checks = 0
    for branch in range(1, 32):
        assert monomial_product(branch, branch) is None
        branch_norm_frobenius_checks += 1

    result = {
        "schema": "marici.grothendieck.five_site_mod2_frobenius_collapse.v1",
        "algebra_dimension": 32,
        "basis_square_checks": basis_square_checks,
        "cross_term_cancellation_checks": cross_term_cancellation_checks,
        "branch_norm_frobenius_checks": branch_norm_frobenius_checks,
        "absolute_frobenius_image_dimension": 1,
        "absolute_frobenius_kernel_dimension": 31,
        "reduced_quotient": "A_red=F2 with identity Frobenius",
        "theorem": (
            "Absolute Frobenius x->x^2 is augmentation followed by inclusion of constants; "
            "it kills every positive-degree class and every nonempty branch norm."
        ),
        "consequence": (
            "The conditional V(2) deck algebra supplies nilpotent degeneration but no "
            "nontrivial Frobenius spectrum, closed-point count, or Euler factor."
        ),
        "not_claimed": [
            "geometric Frobenius",
            "physical chain specialization",
            "Carrier-derived arithmetic",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
