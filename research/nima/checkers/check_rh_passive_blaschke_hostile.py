import json
from fractions import Fraction
from pathlib import Path


def modulus_squared_pair(x, y, shift):
    return (x + shift) ** 2 + y ** 2


right_half_plane_samples = [
    (Fraction(1, 4), Fraction(0)),
    (Fraction(1, 2), Fraction(3, 2)),
    (Fraction(1), Fraction(0)),
    (Fraction(2), Fraction(5)),
]

passive_rows = []
for x, y in right_half_plane_samples:
    numerator = modulus_squared_pair(x, y, -1)
    denominator = modulus_squared_pair(x, y, 1)
    assert denominator - numerator == 4 * x
    assert numerator < denominator
    passive_rows.append({
        "x": str(x),
        "y": str(y),
        "modulus_squared": str(numerator / denominator),
        "strictly_contractive": True,
    })

seam_samples = [Fraction(-3), Fraction(-1), Fraction(0), Fraction(2), Fraction(7)]
seam_rows = []
for y in seam_samples:
    numerator = modulus_squared_pair(Fraction(0), y, -1)
    denominator = modulus_squared_pair(Fraction(0), y, 1)
    assert numerator == denominator
    seam_rows.append({"y": str(y), "modulus_squared": "1"})

# Algebraic reciprocal identity:
# B(-s)=(-s-1)/(-s+1)=(s+1)/(s-1)=1/B(s).
result = {
    "transfer": "(s-1)/(s+1)",
    "pole": "-1",
    "interior_zero": "1",
    "right_half_plane_analytic": True,
    "passive_samples": passive_rows,
    "lossless_seam_samples": seam_rows,
    "reciprocal_identity": "B(-s)=1/B(s)",
    "pointwise_positive_slice_hostile": {
        "polynomial": "t^2+1",
        "positive_for_real_t": True,
        "complex_zeros": ["i", "-i"],
    },
    "verdict": "passivity, lossless seam sewing, and reciprocity do not imply minimum phase",
}

output = Path(__file__).parents[1] / "results" / "rh-passive-blaschke-hostile.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

