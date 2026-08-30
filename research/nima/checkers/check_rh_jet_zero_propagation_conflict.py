#!/usr/bin/env python3
"""Exact conflict between zero propagation and observability for native jets."""

import json
from fractions import Fraction
from pathlib import Path


g = Fraction(2)
dg = Fraction(3)
jet = ((g, 0), (dg, g))


def act(matrix, vector):
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def read(covector, vector):
    return covector[0] * vector[0] + covector[1] * vector[1]


value_readout = (Fraction(1), Fraction(0))
hidden_flux = (Fraction(0), Fraction(1))

state = hidden_flux
outputs = []
for _ in range(8):
    outputs.append(read(value_readout, state))
    state = act(jet, state)
assert outputs == [0] * 8
assert state != (0, 0)

# For a general covector (a,b), invariance under a nonconstant jet requires
# b*dg=0. Since dg is nonzero, only the value covector family b=0 propagates zeros.
tested_covectors = []
for a, b in ((1, 0), (1, 1), (0, 1), (2, -1)):
    # Kernel witness for (a,b) when nonzero: (b,-a).
    witness = (Fraction(b), Fraction(-a))
    present = read((Fraction(a), Fraction(b)), witness)
    future = read((Fraction(a), Fraction(b)), act(jet, witness))
    assert present == 0
    propagates_on_witness = future == 0
    tested_covectors.append({"covector": [a, b], "future_on_kernel_witness": str(future), "propagates": propagates_on_witness})
    assert propagates_on_witness == (b == 0)

result = {
    "native_jet": [[str(entry) for entry in row] for row in jet],
    "value_zero_propagates": True,
    "nonzero_flux_state_outputs": [str(value) for value in outputs],
    "future_value_probes_jointly_faithful": False,
    "covector_tests": tested_covectors,
    "verdict": (
        "native lower-triangular jets make value-zero propagation exact but preserve a "
        "hidden flux line, so value probes cannot also be jointly faithful"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-jet-zero-propagation-conflict.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
