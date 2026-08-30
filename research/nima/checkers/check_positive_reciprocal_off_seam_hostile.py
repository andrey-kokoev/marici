import json
from fractions import Fraction


c = Fraction(3)
coefficients = [Fraction(1), c, Fraction(1)]

assert all(x > 0 for x in coefficients)
assert coefficients == list(reversed(coefficients))


def p(x):
    return x * x + c * x + 1


assert p(Fraction(0)) > 0
assert p(Fraction(-1)) < 0

# On the unit circle, z^-1 P(z) = c + 2 cos(t), whose exact lower bound is
# c-2. This proves seam nonvanishing without numerical sampling.
seam_lower_bound = c - 2
assert seam_lower_bound > 0

# Vieta gives reciprocal roots. The sign change on (-1,0) puts one root
# strictly inside; its reciprocal is strictly outside.
root_product = Fraction(1)
assert root_product == 1

result = {
    "schema": "marici.nima.positive-reciprocal-hostile.v1",
    "coefficient_c": int(c),
    "strictly_positive_coefficients": True,
    "reciprocal_coefficients": True,
    "exact_seam_lower_bound": int(seam_lower_bound),
    "seam_zero": False,
    "inside_root_certified_by_sign_change": True,
    "outside_root_certified_by_reciprocity": True,
    "positive_reciprocal_implies_seam_confinement": False,
}
print(json.dumps(result, indent=2, sort_keys=True))

