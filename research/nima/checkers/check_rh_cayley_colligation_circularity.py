from fractions import Fraction
import json
from pathlib import Path


def complex_modulus_squared(real, imag):
    return real * real + imag * imag


samples = [
    (Fraction(2), Fraction(3)),
    (Fraction(1, 2), Fraction(-4)),
    (Fraction(-1, 3), Fraction(2)),
    (Fraction(0), Fraction(5)),
]

records = []
for real, imag in samples:
    plus_norm = complex_modulus_squared(real + 1, imag)
    minus_norm = complex_modulus_squared(real - 1, imag)
    assert plus_norm - minus_norm == 4 * real
    if plus_norm != 0:
        theta_norm_squared = minus_norm / plus_norm
        if real > 0:
            assert theta_norm_squared < 1
        elif real < 0:
            assert theta_norm_squared > 1
        else:
            assert theta_norm_squared == 1
        records.append(
            {
                "H": [str(real), str(imag)],
                "theta_modulus_squared": str(theta_norm_squared),
                "real_part_sign": "positive" if real > 0 else "negative" if real < 0 else "zero",
            }
        )

result = {
    "samples_verified": len(records),
    "cayley_identity": "abs(H+1)^2-abs(H-1)^2=4 Re(H)",
    "schur_iff_positive_real": True,
    "posthoc_conservative_realization_is_independent_explanation": False,
    "required_construction_order": [
        "source features",
        "Gram conservation identity",
        "lurking isometry",
        "colligation",
        "transfer",
        "scalar determinant",
    ],
    "verdict": "the colligation route is noncircular only when source conservation constructs the isometry before the scalar transfer exists",
    "records": records,
}

out = Path(__file__).parents[1] / "results" / "rh-cayley-colligation-circularity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
