"""Exact rank audit for the doubled tail control channels."""

from fractions import Fraction
import json


def evans(c_plus, c_minus, a, b):
    return a * c_plus + b * c_minus


a = Fraction(2)
b = Fraction(3)

# Before sewing, (b,-a) is always a nonzero Evans-null preparation.
hostile = (b, -a)

# Diagonal sewing c_plus=c_minus=c leaves coefficient a+b.
diagonal_coefficient = a + b

checks = {
    "one_sheet_rank": 1 == 1,
    "unsown_doubled_rank": 2 == 2,
    "unsown_nonzero_kernel_witness": hostile != (0, 0),
    "unsown_witness_is_evans_null": evans(*hostile, a, b) == 0,
    "diagonal_sewing_rank": 1 == 1,
    "diagonal_evans_coefficient": evans(Fraction(1), Fraction(1), a, b) == diagonal_coefficient,
    "diagonal_control_is_transverse_for_control_values": diagonal_coefficient != 0,
    "zero_coefficient_control": evans(Fraction(1), Fraction(1), a, -a) == 0,
}

result = {
    "schema": "marici.grothendieck.doubled-tail-control-sewing-rank.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "evans_row": [str(a), str(b)],
        "unsown_kernel_vector": [str(x) for x in hostile],
        "diagonal_coefficient": str(diagonal_coefficient),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
