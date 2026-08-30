import json
from pathlib import Path


def valuation(number: int, prime: int) -> int:
    assert number != 0
    value = 0
    while number % prime == 0:
        number //= prime
        value += 1
    return value


def main() -> None:
    prime = 3
    translation = 2
    left = 1
    right = 2

    assert valuation(left, prime) == valuation(right, prime) == 0
    translated_left = valuation(left + translation, prime)
    translated_right = valuation(right + translation, prime)
    assert translated_left == 1
    assert translated_right == 0
    assert translated_left != translated_right

    # Finite cyclic Weyl phase exponents. The equality represents
    # T_h M_eta = omega^(eta*h) M_eta T_h over Z/prime Z.
    weyl_rows = []
    for h in range(prime):
        for eta in range(prime):
            phase_exponent = (eta * h) % prime
            weyl_rows.append(
                {
                    "translation": h,
                    "character": eta,
                    "phase_exponent": phase_exponent,
                }
            )

    result = {
        "schema": "marici.nima.finite-tate-weyl-non-descent.v1",
        "prime": prime,
        "equal_input_valuation": 0,
        "translated_left_valuation": translated_left,
        "translated_right_valuation": translated_right,
        "additive_translation_descends_to_valuation_shells": False,
        "weyl_phase_requires_additive_character_port": True,
        "valuation_only_seam_incidence_is_sufficient": False,
        "weyl_rows": weyl_rows,
    }
    output = Path(__file__).parents[1] / "results" / "finite-tate-weyl-non-descent.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

