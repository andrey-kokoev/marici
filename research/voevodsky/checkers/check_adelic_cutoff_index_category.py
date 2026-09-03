from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/adelic-cutoff-index-category-v1.json")
SOURCE = Path("research/grothendieck/adelic-height-supplies-the-canonical-reciprocal-cutoff.md")


def height(value: Fraction) -> int:
    return max(abs(value.numerator), value.denominator)


def fiber(bound: int) -> set[Fraction]:
    values: set[Fraction] = set()
    for denominator in range(1, bound + 1):
        for numerator in range(-bound, bound + 1):
            if numerator:
                value = Fraction(numerator, denominator)
                if height(value) <= bound:
                    values.add(value)
    return values


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "H(1/n)=H(n)=n" in source
    assert "Reciprocal sewing preserves this filtration exactly" in source

    fibers = {bound: fiber(bound) for bound in range(1, 9)}
    for bound, values in fibers.items():
        assert all(height(value) <= bound for value in values)
        assert all(1 / value in values for value in values)
        assert all(height(1 / value) == height(value) for value in values)
        assert Fraction(bound, 1) in values and height(Fraction(bound, 1)) == bound
    for left in range(1, 9):
        for right in range(left, 9):
            assert fibers[left].issubset(fibers[right])
    # Inclusion composition is literal subset composition.
    assert fibers[2].issubset(fibers[5]) and fibers[5].issubset(fibers[8]) and fibers[2].issubset(fibers[8])

    status = contract["status"]
    assert status["index_category"] == "constructed"
    assert status["filler_chain_functor"] == "not supplied"
    result = {
        "schema": "marici.voevodsky.adelic-cutoff-index-category-check.v1",
        "status": "reciprocal_cutoff_index_verified",
        "bounds_checked": 8,
        "nested_label_fibers": True,
        "reciprocal_height_invariance": True,
        "reciprocal_preserves_each_fiber": True,
        "positive_integer_euler_cutoff_recovered": True,
        "inclusion_category_laws": True,
        "filler_chain_functor_supplied": False,
        "completion_verified": False,
        "first_missing_datum": contract["first_missing_datum"],
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
