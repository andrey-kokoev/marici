import json
from fractions import Fraction
from pathlib import Path

a = Fraction(1, 4)


def h(value):
    return (value - a) * (value - (1 - a)) / (a * (1 - a))


samples = [Fraction(-3, 2), Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(1), Fraction(5, 2)]
assert all(h(1 - value) == h(value) for value in samples)
assert h(Fraction(0)) == 1
assert h(Fraction(1)) == 1
roots = [a, 1 - a]
assert all(h(root) == 0 for root in roots)
assert all(root != Fraction(1, 2) for root in roots)


def p(value):
    return value * (value - 1) * (value - Fraction(1, 2)) ** 2


def h_finite_normalization(value):
    return 1 + Fraction(256, 3) * p(value)


checkpoints = [Fraction(0), Fraction(1, 2), Fraction(1)]
assert all(h_finite_normalization(value) == 1 for value in checkpoints)
assert all(h_finite_normalization(root) == 0 for root in roots)
assert all(h_finite_normalization(1 - value) == h_finite_normalization(value) for value in samples)

# The terminal strict two-category has one filler regardless of which external
# scalar section is attached.
terminal_c2 = {
    "objects": 1,
    "one_cells": 1,
    "two_cells": 1,
    "horn_fillers": 1,
}

result = {
    "parameter_a": str(a),
    "central_multiplier": "((s-1/4)(s-3/4))/(3/16)",
    "reciprocal_symmetric": True,
    "endpoint_values": {"s=0": 1, "s=1": 1},
    "off_seam_roots": [str(root) for root in roots],
    "finite_normalization_hostile": {
        "checkpoints": [str(value) for value in checkpoints],
        "values_at_checkpoints": [str(h_finite_normalization(value)) for value in checkpoints],
        "values_at_off_seam_roots": [str(h_finite_normalization(root)) for root in roots],
        "multiplier": "1+(256/3)s(s-1)(s-1/2)^2",
    },
    "terminal_two_category": terminal_c2,
    "fillers_change_after_multiplier": False,
    "scalar_divisor_changes_after_multiplier": True,
    "verdict": "naive C2 fillability is blind to central symmetric divisor insertion",
}

output = Path(__file__).parents[1] / "results" / "rh-c2-central-multiplier-falsifier.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
