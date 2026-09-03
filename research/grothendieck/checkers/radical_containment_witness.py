from fractions import Fraction
import json
from pathlib import Path

# Coefficients are low-to-high over Q.
P = [Fraction(1), Fraction(0), Fraction(-2), Fraction(0), Fraction(1)]
P_rad = [Fraction(-1), Fraction(0), Fraction(1)]
D_pass = [Fraction(-1), Fraction(0), Fraction(1)]
D_fail = [Fraction(-1), Fraction(1)]


def evaluate(poly, value):
    total = Fraction(0)
    for coefficient in reversed(poly):
        total = total * value + coefficient
    return total


def multiply(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            result[i + j] += left * right
    return result


roots = (Fraction(-1), Fraction(1))
checks = {
    "scalar_is_square_of_squarefree_part": multiply(P_rad, P_rad) == P,
    "radical_containment_passes": all(evaluate(D_pass, root) == 0 for root in roots),
    "principal_divisibility_is_strictly_stronger": len(D_pass) < len(P),
    "deliberate_missing_root_fails": any(evaluate(D_fail, root) != 0 for root in roots),
    "passing_defect_equals_squarefree_scalar": D_pass == P_rad,
}
assert all(checks.values())
result = {
    "schema": "marici.radical-containment-witness.v1",
    "status": "passed",
    "arithmetic": "exact_rational_polynomial",
    "scalar": "(x^2-1)^2",
    "squarefree_scalar": "x^2-1",
    "passing_defect": "x^2-1",
    "failing_defect": "x-1",
    "checks": checks,
    "scope": "finite polynomial zero-set containment only; no completed analytic promotion",
}
out = Path(__file__).parents[1] / "results" / "radical-containment-witness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}))
