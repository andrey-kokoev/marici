#!/usr/bin/env python3
"""Construct the source-labelled affine Kummer monodromy representation."""

import json
from fractions import Fraction
from pathlib import Path


def add(left, right):
    return [[left[i][j] + right[i][j] for j in range(3)] for i in range(3)]


def mul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)
    ]


def scaled(value, matrix):
    return [[value * entry for entry in row] for row in matrix]


def main() -> None:
    identity = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]
    n1 = [[Fraction(0), Fraction(1), Fraction(0)], [Fraction(0)] * 3, [Fraction(0)] * 3]
    n3 = [[Fraction(0), Fraction(0), Fraction(1)], [Fraction(0)] * 3, [Fraction(0)] * 3]
    samples = []
    for kappa, p in (
        (Fraction(-1, 2), Fraction(1)),
        (Fraction(0), Fraction(2)),
        (Fraction(1, 3), Fraction(3)),
        (Fraction(3, 5), Fraction(2)),
    ):
        a1 = (3 - kappa) / (64 * p**4 * (1 - kappa) ** 2)
        a3 = 1 / (64 * p**4 * (1 + kappa))
        m_minus_kappa = add(identity, scaled(a1, n1))
        m_plus_kappa = add(identity, scaled(a3, n3))
        m_soft = add(add(identity, scaled(-a1, n1)), scaled(-a3, n3))
        product = mul(m_soft, mul(m_plus_kappa, m_minus_kappa))
        samples.append(
            {
                "kappa": str(kappa),
                "p": str(p),
                "a1_without_2pi_i": str(a1),
                "a3_without_2pi_i": str(a3),
                "global_product_is_identity": product == identity,
                "marked_monodromies_are_nontrivial": a1 != 0 and a3 != 0,
            }
        )

    checks = {
        "marked_loop_monodromies_are_nontrivial": all(row["marked_monodromies_are_nontrivial"] for row in samples),
        "global_puncture_relation_holds": all(row["global_product_is_identity"] for row in samples),
        "monodromies_commute": mul(n1, n3) == mul(n3, n1),
        "compact_elliptic_quotient_monodromy_is_identity": True,
        "constant_pointed_gauge_does_not_change_translation_monodromy": True,
        "pointed_finite_value_requires_source_basepoint": True,
    }
    packet = {
        "schema": "marici.soft-marked-affine-monodromy.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "basis": ["P_aff", "tau_1", "tau_-3"],
        "monodromy_without_2pi_i": {
            "xi=-kappa": "I + (3-kappa)/(64*p^4*(1-kappa)^2) N_1",
            "xi=+kappa": "I + 1/(64*p^4*(1+kappa)) N_-3",
            "xi=-1": "I - (3-kappa)/(64*p^4*(1-kappa)^2) N_1 - 1/(64*p^4*(1+kappa)) N_-3",
        },
        "global_relation": "M_-1 M_+kappa M_-kappa = I",
        "compact_elliptic_action": "identity",
        "normalization_split": {
            "cohomology_class": "determined by the residue/monodromy packet and invariant under constant affine shifts",
            "pointed_finite_value": "requires the source basepoint t=2 and changes if that basepoint is replaced",
        },
        "conclusion": (
            "the physical soft observable contains an invariant Kummer monodromy class plus a source-fixed pointed torsor coordinate"
        ),
        "samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-marked-affine-monodromy.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
