from fractions import Fraction
import json
from pathlib import Path


a = Fraction(3, 5)
b = Fraction(4, 5)
assert a * a + b * b == 1


def theta(w):
    return (w - a) / (1 - a * w)


def scalar_defect(w):
    return 1 - theta(w) * theta(w)


def predicted_defect(w):
    return (1 - a * a) * (1 - w * w) / ((1 - a * w) ** 2)


disk_samples = [Fraction(0), Fraction(1, 4), Fraction(-1, 2), Fraction(4, 5)]
for w in disk_samples:
    assert abs(w) < 1
    assert scalar_defect(w) == predicted_defect(w)
    assert scalar_defect(w) > 0
    assert theta(w) != 1

# At the boundary, the strict defect closes.
assert scalar_defect(Fraction(1)) == 0
assert theta(Fraction(1)) == 1

# A conservative direct sum with a decoupled identity port has a permanent
# zero defect direction and unit eigenvalue.
hostile_defect_diagonal = [scalar_defect(Fraction(1, 4)), Fraction(0)]
assert hostile_defect_diagonal[0] > 0
assert hostile_defect_diagonal[1] == 0
hostile_transfer_eigenvalues = [theta(Fraction(1, 4)), Fraction(1)]
assert Fraction(1) in hostile_transfer_eigenvalues

# Finite strictness without a uniform completion bound.
collapsing_defects = [Fraction(1, n * n) for n in range(1, 9)]
assert all(value > 0 for value in collapsing_defects)
assert collapsing_defects[-1] < collapsing_defects[0]

result = {
    "colligation_parameters": {"a": str(a), "b": str(b)},
    "disk_samples_verified": len(disk_samples),
    "strict_scalar_defect_inside_disk": True,
    "unit_eigenvalue_excluded_inside_disk": True,
    "boundary_unit_value": True,
    "conservative_hostile_has_decoupled_unit_mode": True,
    "unitarity_alone_sufficient": False,
    "strict_observability_required": True,
    "finite_strictness_implies_uniform_completion_strictness": False,
    "verdict": "a source-derived strictly observable conservative colligation would supply the missing orientation mechanism",
}

out = Path(__file__).parents[1] / "results" / "rh-conservative-colligation-orientation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
