"""Exact labelled-occurrence audit for a perturbative-mass white site."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    # Before momentum-conservation specialization, the two adjacent labelled
    # edges contribute independent residue factors 1/(2 y_L) and 1/(2 y_R).
    coefficient = Fraction(1, 2) * Fraction(1, 2)
    labelled_exponents = {"y_L": -1, "y_R": -1}

    # Pullback along y_L=y_R=y adds Laurent exponents but retains multiplicity.
    diagonal_exponent = sum(labelled_exponents.values())
    diagonal_coefficient = coefficient

    assert coefficient == Fraction(1, 4)
    assert diagonal_exponent == -2
    assert diagonal_coefficient == Fraction(1, 4)

    # Forgetting either occurrence before specialization incorrectly gives a
    # simple pole and is therefore not the source operation.
    forgotten_occurrence_exponent = labelled_exponents["y_L"]
    assert forgotten_occurrence_exponent == -1

    result = {
        "schema": "marici.mass-insertion-edge-diagonal.v1",
        "resolved_residue": "1/(4*y_L*y_R)",
        "resolved_laurent_exponents": labelled_exponents,
        "source_diagonal": "y_L=y_R=y",
        "diagonal_residue": "1/(4*y^2)",
        "diagonal_pole_order": -diagonal_exponent,
        "pole_order_after_forgetting_one_occurrence": -forgotten_occurrence_exponent,
        "conclusion": (
            "The perturbative-mass double pole is the diagonal image of two "
            "labelled simple edge occurrences; it is not a new primitive wall."
        ),
    }
    out = Path(__file__).with_name("results") / "mass-insertion-edge-diagonal.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
