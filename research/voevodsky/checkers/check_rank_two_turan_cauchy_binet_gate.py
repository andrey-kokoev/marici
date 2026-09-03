from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/rank-two-turan-cauchy-binet-gate-v1.json")


def d2(weights: list[sp.Expr], bases: list[sp.Expr]) -> sp.Expr:
    moments = [sum(w * y**n for w, y in zip(weights, bases)) for n in range(3)]
    return sp.expand(moments[0] * moments[2] - moments[1] ** 2)


def pair_sum(weights: list[sp.Expr], bases: list[sp.Expr]) -> sp.Expr:
    return sp.expand(sum(weights[j] * weights[k] * (bases[j] - bases[k]) ** 2 for j, k in itertools.combinations(range(len(bases)), 2)))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    weights = [sp.Rational(2), sp.Rational(3), sp.Rational(5)]
    bases = [sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(4, 5)]
    assert sp.simplify(d2(weights, bases) - pair_sum(weights, bases)) == 0
    assert d2(weights, bases) > 0

    u, v, w = sp.symbols("u v w", real=True)
    conjugate_bases = [u + sp.I * v, u - sp.I * v]
    conjugate_weights = [w, w]
    conjugate_minor = sp.simplify(d2(conjugate_weights, conjugate_bases))
    assert conjugate_minor == -4 * v**2 * w**2

    # A sufficiently strong positive real atom can compensate the isolated pair at rank two.
    compensated_weights = [sp.Rational(1), sp.Rational(1), sp.Rational(20)]
    compensated_bases = [sp.Rational(1, 2) + sp.I / 10, sp.Rational(1, 2) - sp.I / 10, sp.Rational(9, 10)]
    compensated_minor = sp.simplify(d2(compensated_weights, compensated_bases))
    assert compensated_minor > 0

    x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
    sampled = (x0 - x1) * (x2 - x3) - (x1 - x2) ** 2
    sampled_moments = [x0 - x1, x1 - x2, x2 - x3]
    assert sp.expand(sampled - (sampled_moments[0] * sampled_moments[2] - sampled_moments[1] ** 2)) == 0

    result = {
        "schema":"marici.voevodsky.rank-two-turan-cauchy-binet-check.v1",
        "status":"rank_two_gate_identity_verified",
        "rank_two_cauchy_binet_identity":True,
        "positive_real_fixture":True,
        "isolated_conjugate_pair_negative":True,
        "cross_compensation_possible":True,
        "sampled_difference_identity":True,
        "certified_endpoint_gamma_prime_D2":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
