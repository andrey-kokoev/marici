import json
from fractions import Fraction
from pathlib import Path


def matvec(matrix, vector):
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def outer(vector):
    return [
        [left * right for right in vector]
        for left in vector
    ]


def channel_on_scalar(unitary, density):
    return unitary * density * unitary


assert channel_on_scalar(Fraction(1), Fraction(3, 5)) == Fraction(3, 5)
assert channel_on_scalar(Fraction(-1), Fraction(3, 5)) == Fraction(3, 5)

controlled_plus = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
]
controlled_minus = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(-1)],
]
control_plus_state = [Fraction(1), Fraction(1)]

output_plus = matvec(controlled_plus, control_plus_state)
output_minus = matvec(controlled_minus, control_plus_state)
assert output_plus == [Fraction(1), Fraction(1)]
assert output_minus == [Fraction(1), Fraction(-1)]

# Hadamard-port amplitudes, using the common unnormalized convention.
ports_plus = [
    (output_plus[0] + output_plus[1]) / 2,
    (output_plus[0] - output_plus[1]) / 2,
]
ports_minus = [
    (output_minus[0] + output_minus[1]) / 2,
    (output_minus[0] - output_minus[1]) / 2,
]
assert ports_plus == [Fraction(1), Fraction(0)]
assert ports_minus == [Fraction(0), Fraction(1)]

# The output density matrices are orthogonal control records.
density_plus = outer(ports_plus)
density_minus = outer(ports_minus)
assert density_plus != density_minus

result = {
    "schema": "marici.controlled-channel-phase-descent.v1",
    "target_channel_for_plus_one": "identity",
    "target_channel_for_minus_one": "identity",
    "completed_channels_equal": True,
    "controlled_plus_ports": [str(value) for value in ports_plus],
    "controlled_minus_ports": [str(value) for value in ports_minus],
    "controlled_records_distinct": True,
    "controlled_constructor_descends_from_channel_quotient": False,
    "verdict": "coherent control requires a source-derived phase-framed lift before channel quotient",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "controlled-channel-phase-descent.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
