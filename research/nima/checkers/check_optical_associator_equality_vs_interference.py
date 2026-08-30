import json
from fractions import Fraction
from pathlib import Path


def norm2(z):
    return z[0] * z[0] + z[1] * z[1]


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def subtract(z, w):
    return (z[0] - w[0], z[1] - w[1])


def scale(z, scalar):
    return (z[0] * scalar, z[1] * scalar)


one = (Fraction(1), Fraction(0))
phases = {
    "one": one,
    "minus_one": (Fraction(-1), Fraction(0)),
    "i": (Fraction(0), Fraction(1)),
    "minus_i": (Fraction(0), Fraction(-1)),
}

records = {}
for name, phase in phases.items():
    left_separate_intensity = norm2(one)
    right_separate_intensity = norm2(phase)
    assert left_separate_intensity == right_separate_intensity == 1
    classical_difference = right_separate_intensity - left_separate_intensity
    assert classical_difference == 0

    plus_amplitude = scale(add(one, phase), Fraction(1, 2))
    minus_amplitude = scale(subtract(one, phase), Fraction(1, 2))
    plus_probability = norm2(plus_amplitude)
    minus_probability = norm2(minus_amplitude)
    assert plus_probability + minus_probability == 1

    records[name] = {
        "separate_route_intensities": [1, 1],
        "classical_difference": 0,
        "coherent_control_ports": [
            str(plus_probability),
            str(minus_probability),
        ],
    }

assert records["one"]["coherent_control_ports"] == ["1", "0"]
assert records["minus_one"]["coherent_control_ports"] == ["0", "1"]
assert records["i"]["coherent_control_ports"] == ["1/2", "1/2"]
assert records["minus_i"]["coherent_control_ports"] == ["1/2", "1/2"]

result = {
    "schema": "marici.optical-associator-equality-vs-interference.v1",
    "phases": records,
    "separate_route_design_global_phase_blind": True,
    "coherent_route_control_phase_sensitive": True,
    "current_aspect_type": "completed_channel_equality_tester",
    "withheld_type": "categorical_associator_interferometer",
    "missing_constructor": "coherent controlled routing and route-marker erasure",
    "verdict": "the existing optical design needs coherent route recombination to observe a global associator phase",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "optical-associator-equality-vs-interference.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
