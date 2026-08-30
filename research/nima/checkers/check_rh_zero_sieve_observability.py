#!/usr/bin/env python3
"""Finite models for zero propagation and joint faithfulness."""

import json
from pathlib import Path


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def read(row, vector):
    return sum(row[j] * vector[j] for j in range(len(vector)))


readout = (1, 0)
hidden_state = (0, 1)
swap = ((0, 1), (1, 0))
identity = ((1, 0), (0, 1))

# Jointly faithful future probes, but the present zero does not propagate.
assert read(readout, hidden_state) == 0
assert read(readout, mat_vec(swap, hidden_state)) == 1
swap_probe_rows = (readout, tuple(read(readout, column) for column in ((0, 1), (1, 0))))
assert swap_probe_rows == ((1, 0), (0, 1))

# Zero propagation, but no joint faithfulness: the hidden line survives forever.
state = hidden_state
identity_outputs = []
for _ in range(5):
    identity_outputs.append(read(readout, state))
    state = mat_vec(identity, state)
assert identity_outputs == [0] * 5

# If zero propagation and joint faithfulness both hold, a nonzero state cannot
# have zero present readout. This is the direct logical composition of the gates.
both_gates_exclude_hidden_nonzero = True

result = {
    "observability_without_zero_propagation": {
        "present_output": 0,
        "next_output": 1,
        "future_probe_rank": 2,
    },
    "zero_propagation_without_observability": {
        "outputs": identity_outputs,
        "hidden_state_nonzero": True,
    },
    "both_gates_exclude_hidden_nonzero": both_gates_exclude_hidden_nonzero,
    "verdict": (
        "off-seam nonvanishing follows only if a scalar zero generates a stable zero "
        "sieve and the full family of future source probes is jointly faithful"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-zero-sieve-observability.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
