"""Exact deck-character audit after the Entry 1273 numerator collapse."""

import itertools
import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
packet_path = ROOT / "research" / "benincasa" / "results" / "five-site-d3-marked-kummer-cover.json"
packet = json.loads(packet_path.read_text(encoding="utf-8"))
forms = list(packet["facet_forms"].values())
assert len(forms) == 26


def value_on_sheet(xs, ys, signs):
    denominator = F(1)
    for form in forms:
        q = sum(F(c) * x for c, x in zip(form["x"], xs))
        q += sum(F(c) * s * y for c, s, y in zip(form["y"], signs, ys))
        assert q != 0
        denominator *= q
    return F(1, denominator)


samples = [
    ([101, 103, 107, 109, 113], [2, 3, 5, 7, 11]),
    ([127, 131, 137, 139, 149], [13, 17, 19, 23, 29]),
]
sheet_signs = list(itertools.product((-1, 1), repeat=5))
nonzero_counts = []
for xs, ys in samples:
    sheet_values = [value_on_sheet(xs, ys, signs) for signs in sheet_signs]
    coefficients = []
    for mask in range(32):
        coefficient = F(0)
        for signs, value in zip(sheet_signs, sheet_values):
            character = 1
            for i in range(5):
                if mask & (1 << i):
                    character *= signs[i]
            coefficient += character * value
        coefficients.append(coefficient)
    nonzero_counts.append(sum(c != 0 for c in coefficients))
    assert all(c != 0 for c in coefficients)

result = {
    "schema": "marici.cosmology.asymmetric_constant_numerator_deck_support.v1",
    "facet_count": 26,
    "sheet_count": 32,
    "exact_samples": len(samples),
    "nonzero_character_counts": nonzero_counts,
    "numerator_character_support": [0],
    "integrand_character_support_size": 32,
    "source_of_nontrivial_characters": "moving marked denominator arrangement",
    "passed": True,
}
out = Path(__file__).with_name("results") / "asymmetric-constant-numerator-deck-support.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
