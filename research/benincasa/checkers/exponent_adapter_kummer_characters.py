"""Classify the physical and quarter exponent fibers by Kummer inertia."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"


def inertia_character(exponent: Fraction) -> str:
    residue = exponent % 1
    labels = {
        Fraction(0): "+1",
        Fraction(1, 4): "+i",
        Fraction(1, 2): "-1",
        Fraction(3, 4): "-i",
    }
    return labels[residue]


def main() -> None:
    exponents = {
        "physical": Fraction(-1, 2),
        "quarter_minus_five_fourths": Fraction(-5, 4),
        "quarter_minus_seven_fourths": Fraction(-7, 4),
    }
    characters = {name: inertia_character(value) for name, value in exponents.items()}
    assert characters == {
        "physical": "-1",
        "quarter_minus_five_fourths": "-i",
        "quarter_minus_seven_fourths": "+i",
    }

    differences = {
        name: value - exponents["physical"]
        for name, value in exponents.items()
        if name != "physical"
    }
    assert all(value.denominator == 4 for value in differences.values())
    assert all(inertia_character(exponents["physical"] + n) == "-1" for n in range(-8, 9))

    output = {
        "status": "pass",
        "local_inertia_convention": "exp(2*pi*i*gamma) around K=0",
        "characters": characters,
        "differences_from_physical": {
            name: str(value) for name, value in differences.items()
        },
        "integral_shift_preserves_physical_character": True,
        "continuous_parameter_derivative": "d_epsilon K^(epsilon-1/2) = log(K) K^(epsilon-1/2)",
        "logarithmic_generator_in_frozen_rational_complex": False,
        "classification": (
            "The quarter resonances lie in order-four Kummer sectors, while "
            "the physical residue lies in the order-two sector."
        ),
    }
    destination = RESULTS / "exponent_adapter_kummer_characters.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
