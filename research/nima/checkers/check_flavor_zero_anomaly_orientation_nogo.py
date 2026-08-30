from fractions import Fraction
import json
from pathlib import Path


q = (Fraction(3), Fraction(2), Fraction(0))


def mean(charges):
    return sum(charges) / len(charges)


def centered_cubic(charges):
    center = mean(charges)
    return sum((charge - center) ** 3 for charge in charges)


def reflect(charges):
    return tuple(-charge for charge in charges)


m3 = centered_cubic(q)
reflected_m3 = centered_cubic(reflect(q))
assert m3 == Fraction(-20, 9)
assert reflected_m3 == -m3

# Cancellation at zero is reflection invariant for an odd functional.
zero_cancellation_q = m3 == 0
zero_cancellation_reflected = reflected_m3 == 0
assert zero_cancellation_q == zero_cancellation_reflected

# An even magnitude equation also retains both sheets.
magnitude_target = m3 * m3
assert m3 * m3 == magnitude_target
assert reflected_m3 * reflected_m3 == magnitude_target

# A nonzero signed target selects one sheet, but the target itself is an
# oriented source datum and cannot be fitted from the desired charge vector.
signed_target = m3
assert m3 == signed_target
assert reflected_m3 != signed_target

# A relational reference restores covariance: simultaneous reflection of the
# charge cubic and reference leaves their equality intact. Fixing the reference
# orientation is a separate source operation.
reference = signed_target
assert m3 == reference
assert reflected_m3 == -reference

result = {
    "schema": "marici.nima.flavor-zero-anomaly-orientation-nogo.v1",
    "target_centered_cubic": str(m3),
    "reflected_centered_cubic": str(reflected_m3),
    "zero_cancellation_same_on_both_sheets": True,
    "magnitude_equation_same_on_both_sheets": True,
    "nonzero_signed_target_selects_one_sheet": True,
    "signed_target_requires_oriented_source": True,
    "relational_reference_preserves_simultaneous_reflection": True,
    "verdict": (
        "Homogeneous anomaly cancellation at zero cannot select charge-line "
        "orientation: its zero locus is reflection invariant. A nonzero signed "
        "target can select a sheet only by importing an independently derived "
        "oriented reference or relative sector."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-zero-anomaly-orientation-nogo.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
