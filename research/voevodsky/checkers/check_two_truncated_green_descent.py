from __future__ import annotations

import json
from fractions import Fraction


def equicorrelation_determinant(size: int, correlation: Fraction) -> Fraction:
    return (1 - correlation) ** (size - 1) * (1 + (size - 1) * correlation)


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    correlation = Fraction(-2, 5)
    pair_det = equicorrelation_determinant(2, correlation)
    triple_det = equicorrelation_determinant(3, correlation)
    quadruple_det = equicorrelation_determinant(4, correlation)
    collective_eigenvalue = 1 + 3 * correlation

    assert pair_det == Fraction(21, 25) > 0
    assert triple_det == Fraction(49, 125) > 0
    assert quadruple_det == Fraction(-343, 625) < 0
    assert collective_eigenvalue == Fraction(-1, 5)

    result = {
        "schema": "marici.voevodsky.two-truncated-green-descent.v1",
        "status": "two_truncated_detection_falsified",
        "off_diagonal_pairing": render(correlation),
        "pair_determinant": render(pair_det),
        "triple_determinant": render(triple_det),
        "quadruple_determinant": render(quadruple_det),
        "quadruple_collective_eigenvalue": render(collective_eigenvalue),
        "all_pair_and_triple_restrictions_positive": True,
        "full_four_sector_form_positive": False,
        "first_failed_object": "four-sector principal Gram block",
        "repair_gate": "full joint Gram certificate or source-derived all-size positivity theorem",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
