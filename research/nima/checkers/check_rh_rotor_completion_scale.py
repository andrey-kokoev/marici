from fractions import Fraction
import json
from pathlib import Path


def multiply(left, right):
    a, b = left
    c, d = right
    return (a * c - b * d, a * d + b * c)


def norm_squared(value):
    a, b = value
    return a * a + b * b


rotor_a = (Fraction(3, 5), Fraction(4, 5))
rotor_b = (Fraction(5, 13), Fraction(12, 13))
product = multiply(rotor_a, rotor_b)
assert norm_squared(rotor_a) == 1
assert norm_squared(rotor_b) == 1
assert norm_squared(product) == 1

opposite = (-rotor_a[0], -rotor_a[1])
assert (rotor_a[0] + opposite[0], rotor_a[1] + opposite[1]) == (0, 0)

partial = Fraction(1)
paired = Fraction(1)
cutoffs = [2, 4, 8, 16, 32, 64]
rows = []
for n in range(2, max(cutoffs) + 1):
    factor = Fraction(n - 1, n)
    reciprocal = 1 / factor
    partial *= factor
    paired *= factor * reciprocal
    if n in cutoffs:
        assert partial == Fraction(1, n)
        assert paired == 1
        rows.append(
            {
                "cutoff": n,
                "collapsing_sector": str(partial),
                "reciprocal_sector": str(1 / partial),
                "paired_product": str(paired),
            }
        )

result = {
    "schema": "marici.rh.rotor-completion-scale.v1",
    "finite_unit_rotor_product_norm_squared": str(norm_squared(product)),
    "additive_opposite_rotors_cancel": True,
    "finite_factors_all_invertible": True,
    "collapsing_product_at_final_cutoff": str(partial),
    "reciprocal_paired_product": str(paired),
    "sectorwise_collapse_hidden_by_pairing": True,
    "verdict": "rotor nonvanishing requires source-derived completion-stable scale control",
}

out = Path(__file__).parents[1] / "results" / "rh-rotor-completion-scale.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
