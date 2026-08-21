"""Exact rational audit of the five-point disk reflection and its pairing."""

from fractions import Fraction as F
import json
from pathlib import Path


def transform(x, y):
    # Reflection (12345)->(15432), followed by the standard gauge fixing.
    return (y - x) / y, (y - x) / (y * (1 - x))


def jacobian(x, y):
    return x * (x - y) / (y**3 * (1 - x) ** 2)


def pt_den(x, y):
    return (-x) * (x - y) * (y - 1)


checks = 0
for den in range(5, 31):
    for ix in range(1, den - 1):
        for iy in range(ix + 1, den):
            x, y = F(ix, den), F(iy, den)
            X, Y = transform(x, y)
            assert 0 < X < Y < 1
            J = jacobian(x, y)
            assert J < 0
            # Pullback PT(15432) / PT(12345).
            ratio = J * pt_den(x, y) / pt_den(X, Y)
            assert ratio == -1
            checks += 3

result = {
    "schema": "marici.string.five_point_reflection_pairing.v1",
    "reflection_map": ["X=(y-x)/y", "Y=(y-x)/(y(1-x))"],
    "jacobian": "x(x-y)/(y^3(1-x)^2) < 0",
    "pulled_back_parke_taylor_ratio": -1,
    "oriented_chamber_character": -1,
    "simultaneously_transported_pairing_character": 1,
    "exact_rational_checks": checks,
    "passed": True,
}
out = Path(__file__).with_name("results") / "five-point-disk-reflection-pairing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
