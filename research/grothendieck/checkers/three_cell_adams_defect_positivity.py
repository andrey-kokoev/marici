"""Exact rational audit of the three-cell defect factorization."""

from fractions import Fraction as F


def determinant(a, b, c):
    return 1 - a * a - b * b - c * c + 2 * a * b * c


def defect_form(a, b, c):
    return (1 - a * a) * (1 - b * b) - (c - a * b) ** 2


tests = [
    (F(1, 2), F(2, 3), F(1, 3)),
    (F(-3, 4), F(-3, 4), F(-3, 4)),
    (F(3, 5), F(4, 5), F(12, 25)),
]
assert all(determinant(*test) == defect_form(*test) for test in tests)

# Exact composition is automatically positive when both edges contract.
a = F(3, 5)
b = F(4, 5)
c = a * b
assert determinant(a, b, c) == (1 - a * a) * (1 - b * b) > 0

# Prior hostile equicorrelation fails precisely through its cycle defect.
a = b = c = F(-3, 4)
assert determinant(a, b, c) == F(-49, 32)
assert (c - a * b) ** 2 > (1 - a * a) * (1 - b * b)

result = {
    "determinant_factorization": "det G=(1-|a|^2)(1-|b|^2)-|c-ab|^2",
    "exact_composition_implies_triangle_positivity": True,
    "hostile_triangle_failure_is_exactly_defect_overrun": True,
    "scalar_adams_gate": "|c_p2-a_p^2| <= 1-|a_p|^2",
    "operator_extension": "Parrott/Schur defect-space contraction",
    "rh_not_proved": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "three-cell-adams-defect-positivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

