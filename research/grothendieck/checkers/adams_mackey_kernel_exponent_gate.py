#!/usr/bin/env python3
"""Exact compatibility gate between Adams power maps and finite Mackey legs."""

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/adams-mackey-kernel-exponent-gate.json"


def main():
    coefficient_value_checks = 0
    betti_value_checks = 0
    quotient_index_checks = 0
    compatible_cases = 0
    incompatible_cases = 0

    for order_g in range(1, 13):
        for order_h in range(1, order_g + 1):
            if order_g % order_h:
                continue
            kernel_order = order_g // order_h
            for n in range(1, 13):
                expected = gcd(n, kernel_order) == 1

                # Coefficients: q_! [n]^* versus [n]^* q_!, on delta bases.
                coefficient_equal = True
                for x in range(order_g):
                    for h in range(order_h):
                        lhs = sum(int((n * g) % order_g == x) for g in range(order_g) if g % order_h == h)
                        rhs = int(x % order_h == (n * h) % order_h)
                        coefficient_equal &= lhs == rhs
                        coefficient_value_checks += 1

                # Betti: psi_G^n q^! versus q^! psi_H^n, as multiplicity vectors.
                betti_equal = True
                for h in range(order_h):
                    lhs = [0] * order_g
                    rhs = [0] * order_g
                    for g in range(order_g):
                        if g % order_h == h:
                            lhs[(n * g) % order_g] += 1
                        if g % order_h == (n * h) % order_h:
                            rhs[g] += 1
                    betti_equal &= lhs == rhs
                    betti_value_checks += order_g

                assert coefficient_equal == expected
                assert betti_equal == expected
                quotient_index_checks += 1
                if expected:
                    compatible_cases += 1
                else:
                    incompatible_cases += 1

    five_site = []
    for branch_codimension in range(1, 6):
        kernel_exponent = 2
        survivors = [n for n in range(1, 13) if gcd(n, kernel_exponent) == 1]
        failures = [n for n in range(1, 13) if n not in survivors]
        assert survivors == [1, 3, 5, 7, 9, 11]
        five_site.append({
            "branch_codimension": branch_codimension,
            "kernel": f"(C2)^{branch_codimension}",
            "kernel_exponent": kernel_exponent,
            "compatible_indices": survivors,
            "incompatible_indices": failures,
        })

    result = {
        "schema": "marici.grothendieck.adams_mackey_kernel_exponent_gate.v1",
        "cyclic_quotients": "C_N->C_M for M|N, N<=12",
        "coefficient_value_checks": coefficient_value_checks,
        "betti_value_checks": betti_value_checks,
        "quotient_index_cases": quotient_index_checks,
        "compatible_cases": compatible_cases,
        "incompatible_cases": incompatible_cases,
        "theorem": (
            "For finite abelian q:G->H with kernel K, Adams index n commutes with "
            "coefficient fiber sum and Betti fiber lift iff multiplication by n on K "
            "is bijective, equivalently gcd(n, exp K)=1."
        ),
        "five_site_branch_tower": five_site,
        "consequence": (
            "Every nontrivial five-site branch kernel retains exactly the odd Adams monoid; "
            "even operations fail both Mackey-leg compatibility and physical delta selection."
        ),
        "scope": "Algebraic correspondence theorem; no physical branch-chain map is inferred.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
