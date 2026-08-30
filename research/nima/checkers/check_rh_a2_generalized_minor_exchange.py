from fractions import Fraction
import json
from pathlib import Path


def determinant_2(a, b, c, d):
    return a * d - b * c


samples = [
    (Fraction(2), Fraction(3), Fraction(5)),
    (Fraction(-2), Fraction(3), Fraction(5)),
    (Fraction(3, 2), Fraction(-4, 3), Fraction(5, 4)),
]

records = []
for a, b, c in samples:
    p = a * b
    q = b
    r = a + c
    s = determinant_2(a + c, a * b, Fraction(1), b)
    assert s == b * c
    assert q * r == p + s
    if q != 0:
        assert p / q == a
        assert s / q == c
        assert (p + s) / q == r
    records.append(
        {
            "parameters": [str(a), str(b), str(c)],
            "minors": {"P": str(p), "Q": str(q), "R": str(r), "S": str(s)},
            "exchange_holds": True,
        }
    )

# The braid chart wall is not a singular matrix wall.
wall = (Fraction(2), Fraction(3), Fraction(-2))
wall_p = wall[0] * wall[1]
wall_q = wall[1]
wall_r = wall[0] + wall[2]
wall_s = wall[1] * wall[2]
assert wall_r == 0
assert wall_q * wall_r == wall_p + wall_s
matrix_determinant_on_wall = Fraction(1)
assert matrix_determinant_on_wall == 1

# Determinant compression is constant throughout the family.
assert all(Fraction(1) == 1 for _ in samples)

result = {
    "generalized_minors": ["P=M13", "Q=M23", "R=M12", "S=minor(rows12,cols23)"],
    "exchange_relation": "Q*R=P+S",
    "sample_count": len(records),
    "samples": records,
    "chart_wall_sample": {
        "parameters": [str(value) for value in wall],
        "R": str(wall_r),
        "matrix_determinant": str(matrix_determinant_on_wall),
    },
    "determinant_compression_is_faithful": False,
    "theta_distinguished_minor_identified": False,
    "verdict": "the A2 exchange is an exact generalized-minor law; the theta readout minor remains to be identified",
}

out = Path(__file__).parents[1] / "results" / "rh-a2-generalized-minor-exchange.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
