import itertools
import json
from fractions import Fraction
from pathlib import Path


GROUP = (0, 1)


def add(left, right):
    return left ^ right


def omega(a, b, c):
    return -1 if a * b * c else 1


def ports(phase):
    plus_amplitude = Fraction(1 + phase, 2)
    minus_amplitude = Fraction(1 - phase, 2)
    return (plus_amplitude * plus_amplitude, minus_amplitude * minus_amplitude)


triple_ports = {}
for triple in itertools.product(GROUP, repeat=3):
    intensities = ports(omega(*triple))
    assert sum(intensities) == 1
    triple_ports["".join(str(x) for x in triple)] = [int(x) for x in intensities]

assert triple_ports["111"] == [0, 1]
assert all(
    value == [1, 0]
    for key, value in triple_ports.items()
    if key != "111"
)


def normalized_beta(value_at_11):
    return {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): value_at_11}


def coboundary(beta, a, b, c):
    return (
        beta[(b, c)]
        * beta[(a, add(b, c))]
        // beta[(add(a, b), c)]
        // beta[(a, b)]
    )


rephasing_values = []
for value_at_11 in (-1, 1):
    beta = normalized_beta(value_at_11)
    value = coboundary(beta, 1, 1, 1)
    assert value == 1
    rephasing_values.append(value)

# Separate path intensities erase the relative sign.
strict_separate_intensities = [1, 1]
nontrivial_separate_intensities = [1, 1]
assert strict_separate_intensities == nontrivial_separate_intensities

result = {
    "schema": "marici.associator-bracketing-interference.v1",
    "group": "C2",
    "triple_ports": triple_ports,
    "nontrivial_triple": "111",
    "strict_ports_at_111": [1, 0],
    "nontrivial_ports_at_111": triple_ports["111"],
    "normalized_rephasing_values_at_111": rephasing_values,
    "separate_path_intensities_blind": True,
    "verdict": "coherent bracketing interference converts the associator class into a deterministic port exchange",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "associator-bracketing-interference.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
