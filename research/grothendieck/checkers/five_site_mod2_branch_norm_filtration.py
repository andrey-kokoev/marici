#!/usr/bin/env python3
"""Exact augmentation-filtration model for five-site branch norms mod 2."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/grothendieck/results/five-site-mod2-branch-norm-filtration.json"


def multiply(a, b):
    """Multiply in F2[e1,...,e5]/(e_i^2), using subset masks."""
    out = set()
    for x in a:
        for y in b:
            if x & y:
                continue
            z = x | y
            if z in out:
                out.remove(z)
            else:
                out.add(z)
    return out


def main():
    subset_checks = 0
    annihilator_checks = 0
    square_zero_checks = 0
    strata = []

    for branch in range(1, 32):
        bits = [i for i in range(5) if branch & (1 << i)]
        norm = {0}
        for i in bits:
            norm = multiply(norm, {1 << i})  # 1+g_i = epsilon_i
        # In epsilon coordinates product_i epsilon_i is the single monomial B.
        assert norm == {branch}
        subset_checks += 1
        assert multiply(norm, norm) == set()
        square_zero_checks += 1
        for i in bits:
            assert multiply(norm, {1 << i}) == set()
            annihilator_checks += 1
        strata.append({
            "branch_subset_mask": branch,
            "codimension": len(bits),
            "kernel_order": 1 << len(bits),
            "norm_augmentation_monomial_mask": branch,
            "filtration_degree": len(bits),
            "square_zero": True,
            "annihilated_kernel_generators": len(bits),
        })

    by_codimension = {}
    for row in strata:
        key = str(row["codimension"])
        by_codimension[key] = by_codimension.get(key, 0) + 1
    assert by_codimension == {"1": 5, "2": 10, "3": 10, "4": 5, "5": 1}

    result = {
        "schema": "marici.grothendieck.five_site_mod2_branch_norm_filtration.v1",
        "algebra": "F2[(C2)^5] = F2[epsilon_1,...,epsilon_5]/(epsilon_i^2)",
        "nonempty_branch_subsets": 31,
        "subset_norm_identifications": subset_checks,
        "square_zero_checks": square_zero_checks,
        "kernel_generator_annihilator_checks": annihilator_checks,
        "strata_by_codimension": by_codimension,
        "strata": strata,
        "theorem": (
            "For branch set B, N_B=product_{i in B} epsilon_i is nonzero in "
            "augmentation degree |B|, square-zero, and annihilated by every epsilon_i in B."
        ),
        "interpretation": (
            "The frozen five-site branch codimension is mirrored exactly by mod-2 "
            "augmentation/Loewy degree, conditional on the integral deck lattice."
        ),
        "not_claimed": [
            "physical relative-chain specialization",
            "geometric Frobenius",
            "Carrier-derived prime or arithmetic scheme",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
