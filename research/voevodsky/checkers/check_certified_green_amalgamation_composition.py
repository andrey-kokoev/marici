from __future__ import annotations

import json
from fractions import Fraction


def determinant_3(r12: Fraction, r23: Fraction, r13: Fraction) -> Fraction:
    return 1 + 2 * r12 * r23 * r13 - r12**2 - r23**2 - r13**2


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    r12 = r23 = Fraction(9, 10)
    pair_det = 1 - r12**2
    assert pair_det == Fraction(19, 100)

    omitted_r13 = Fraction(0)
    failed_det = determinant_3(r12, r23, omitted_r13)
    assert failed_det == Fraction(-31, 50)

    coherent_r13 = r12 * r23
    repaired_det = determinant_3(r12, r23, coherent_r13)
    assert repaired_det == Fraction(361, 10000)

    result = {
        "schema": "marici.voevodsky.certified-green-amalgamation-composition.v1",
        "status": "pairwise_certificates_do_not_compose_without_joint_completion_data",
        "adjacent_correlations": [render(r12), render(r23)],
        "adjacent_minor_determinant": render(pair_det),
        "omitted_nonadjacent_correlation": render(omitted_r13),
        "failed_joint_determinant": render(failed_det),
        "coherent_nonadjacent_correlation": render(coherent_r13),
        "repaired_joint_determinant": render(repaired_det),
        "first_missing_datum": "nonadjacent cross pairing plus full positive block-completion witness",
        "beck_chevalley_gate": "comparison of certified joint completions, not pairwise boundary data",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
