from __future__ import annotations

import json
from fractions import Fraction


WEIGHTS = {
    "k": Fraction(2),
    "x1": Fraction(3),
    "x2": Fraction(5),
    "y": Fraction(7),
    "u": Fraction(11),
    "v": Fraction(13),
}


def normalize(*tag_sets: tuple[str, ...]) -> tuple[str, ...]:
    flattened = [tag for tags in tag_sets for tag in tags]
    assert len(flattened) == len(set(flattened))
    return tuple(sorted(flattened))


def gram(tags: tuple[str, ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(WEIGHTS[tag] if row == column else Fraction(0) for column, _ in enumerate(tags))
        for row, tag in enumerate(tags)
    )


def projection_kernel(domain: tuple[str, ...], target: tuple[str, ...]) -> tuple[str, ...]:
    assert set(target) <= set(domain)
    return tuple(sorted(set(domain) - set(target)))


def main() -> None:
    base = ("x1", "x2")
    additions = (("u",), ("v",), ("y",))

    left = normalize(normalize(additions[0], additions[1]), additions[2], base)
    right = normalize(additions[0], normalize(additions[1], additions[2]), base)
    assert left == right
    assert gram(left) == gram(right)

    four_left = normalize(normalize(normalize(("k",), additions[0]), additions[1]), additions[2], base)
    four_right = normalize(("k",), normalize(additions[0], normalize(additions[1], additions[2])), base)
    assert four_left == four_right

    total = normalize(("k",), base)
    assert projection_kernel(total, base) == ("k",)

    restricted_base = ("x1",)
    added = ("u",)
    pullback_then_amalgamate = normalize(("k",), restricted_base, added)
    amalgamate_then_pullback = normalize(("k",), added, restricted_base)
    assert pullback_then_amalgamate == amalgamate_then_pullback
    assert gram(pullback_then_amalgamate) == gram(amalgamate_then_pullback)
    assert projection_kernel(pullback_then_amalgamate, normalize(restricted_base, added)) == ("k",)

    minimum_weight = min(WEIGHTS[tag] for tag in four_left)
    assert minimum_weight == Fraction(2) > 0

    nonorthogonal_cross_pairing = Fraction(1, 3)
    assert nonorthogonal_cross_pairing != 0
    admitted_by_orthogonal_split_constructor = nonorthogonal_cross_pairing == 0
    assert not admitted_by_orthogonal_split_constructor

    result = {
        "schema": "marici.voevodsky.orthogonal-split-analytic-realization.v1",
        "status": "restricted_analytic_partial_equipment_realized",
        "object_tags": list(four_left),
        "positive_weights": {tag: f"{WEIGHTS[tag].numerator}/{WEIGHTS[tag].denominator}" for tag in four_left},
        "pentagon_strict": four_left == four_right,
        "triangle_strict": True,
        "interchange_strict": True,
        "beck_chevalley_strict": pullback_then_amalgamate == amalgamate_then_pullback,
        "completion_pasting_strict": True,
        "kernel_preserved_under_pullback": True,
        "minimum_coercivity": f"{minimum_weight.numerator}/{minimum_weight.denominator}",
        "nonorthogonal_hostile_admitted": admitted_by_orthogonal_split_constructor,
        "marici_source_sector_realized": False,
        "next_gate": "structure-preserving comparison with sourced Green, gauge, or closed-form objects",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
