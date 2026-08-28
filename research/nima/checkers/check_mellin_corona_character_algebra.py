import json
from pathlib import Path


ORDER = 7


def character_product(left: int, right: int) -> int:
    return (left + right) % ORDER


def haar(character: int) -> int:
    return 1 if character % ORDER == 0 else 0


def main() -> None:
    rows = []
    for frequency in range(1, ORDER):
        conjugate = (-frequency) % ORDER
        product = character_product(frequency, conjugate)
        assert haar(frequency) == 0
        assert haar(conjugate) == 0
        assert product == 0
        assert haar(product) == 1
        rows.append(
            {
                "frequency": frequency,
                "conjugate": conjugate,
                "individual_mean": 0,
                "conjugate_product_mean": 1,
            }
        )

    for left in range(ORDER):
        for right in range(ORDER):
            assert character_product(left, right) in range(ORDER)
            assert character_product(left, right) == character_product(right, left)

    result = {
        "schema": "marici.nima.mellin-corona-character-algebra.v1",
        "finite_character_group_order": ORDER,
        "unit_preserved": haar(0) == 1,
        "nontrivial_characters_annihilated": True,
        "conjugate_pair_correlations_preserved": True,
        "haar_state_is_multiplicative": False,
        "character_algebra_closed_under_product": True,
        "character_algebra_closed_under_involution": True,
        "rows": rows,
    }
    output = Path(__file__).parents[1] / "results" / "mellin-corona-character-algebra.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

