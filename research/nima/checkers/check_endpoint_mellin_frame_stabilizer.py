from fractions import Fraction
import json
from pathlib import Path


TRANSLATIONS = tuple(Fraction(value, 1) for value in range(-5, 6))


def endpoint_signature(translation: Fraction):
    # Evaluations of the carrier basis (1, q) at q=translation.
    return (Fraction(1, 1), translation)


def main() -> None:
    base = endpoint_signature(Fraction(0, 1))
    stabilizer = [
        translation
        for translation in TRANSLATIONS
        if endpoint_signature(translation) == base
    ]
    assert stabilizer == [Fraction(0, 1)]

    rows = [
        {
            "translation": str(translation),
            "constant_channel_agrees": True,
            "coordinate_channel_agrees": translation == 0,
            "endpoint_incidence_preserved": endpoint_signature(translation) == base,
        }
        for translation in TRANSLATIONS
    ]

    result = {
        "schema": "marici.nima.endpoint-mellin-frame-stabilizer.v1",
        "carrier_basis": ["1", "q"],
        "tested_translation_count": len(TRANSLATIONS),
        "stabilizer": [str(value) for value in stabilizer],
        "endpoint_stabilizer_is_trivial": True,
        "source_specific_separation_still_required": True,
        "rows": rows,
    }
    output = Path(__file__).parents[1] / "results" / "endpoint-mellin-frame-stabilizer.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

