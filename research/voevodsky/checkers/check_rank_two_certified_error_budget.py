from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/rank-two-certified-error-budget-v1.json")


def determinant(a: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return a[0] * a[2] - a[1] * a[1]


def error_bound(ahat: tuple[Fraction, Fraction, Fraction], eta: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return abs(ahat[2]) * eta[0] + abs(ahat[0]) * eta[2] + 2 * abs(ahat[1]) * eta[1] + eta[0] * eta[2] + eta[1] * eta[1]


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    ahat = (Fraction(3, 2), Fraction(4, 5), Fraction(7, 10))
    eta = (Fraction(1, 1000), Fraction(1, 2000), Fraction(1, 1000))
    bound = error_bound(ahat, eta)

    # Enumerating error-box vertices verifies the multiaffine/quadratic enclosure.
    for signs in ((s0, s1, s2) for s0 in (-1, 1) for s1 in (-1, 1) for s2 in (-1, 1)):
        exact = tuple(ahat[k] + signs[k] * eta[k] for k in range(3))
        assert abs(determinant(exact) - determinant(ahat)) <= bound

    eps = (Fraction(1, 10000), Fraction(2, 10000), Fraction(3, 10000), Fraction(4, 10000))
    induced_eta = tuple(eps[k] + eps[k + 1] for k in range(3))
    for k in range(3):
        for left_sign in (-1, 1):
            for right_sign in (-1, 1):
                difference_error = left_sign * eps[k] - right_sign * eps[k + 1]
                assert abs(difference_error) <= induced_eta[k]

    positive_hat = (Fraction(2), Fraction(1), Fraction(1))
    positive_eta = (Fraction(1, 100),) * 3
    positive_margin = determinant(positive_hat)
    assert positive_margin > error_bound(positive_hat, positive_eta)

    negative_hat = (Fraction(1), Fraction(2), Fraction(1))
    negative_eta = (Fraction(1, 100),) * 3
    negative_margin = determinant(negative_hat)
    assert negative_margin < -error_bound(negative_hat, negative_eta)

    indeterminate_hat = (Fraction(1), Fraction(1), Fraction(10001, 10000))
    indeterminate_eta = (Fraction(1, 1000),) * 3
    indeterminate_margin = determinant(indeterminate_hat)
    assert abs(indeterminate_margin) <= error_bound(indeterminate_hat, indeterminate_eta)

    result = {
        "schema":"marici.voevodsky.rank-two-certified-error-budget-check.v1",
        "status":"rank_two_error_budget_verified",
        "determinant_perturbation_bound":True,
        "sample_difference_bound":True,
        "positive_negative_indeterminate_fixtures":True,
        "prime_tail_formula_recomputed":False,
        "gamma_interval_quadrature":False,
        "source_D2_certification":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
