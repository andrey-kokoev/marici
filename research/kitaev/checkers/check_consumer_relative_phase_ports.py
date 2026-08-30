import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


L = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0]])
coordinates = [sp.eye(4).row(i) for i in range(4)]
consumer_rows = [L.row(i) for i in range(L.rows)]


def sufficient(rows):
    if not rows:
        return False
    R = sp.Matrix.vstack(*rows)
    return R.col_join(L).rank() == R.rank()


def minimum(vocabulary):
    for size in range(1, len(vocabulary) + 1):
        winners = []
        for indices in itertools.combinations(range(len(vocabulary)), size):
            if sufficient([vocabulary[i] for i in indices]):
                winners.append(indices)
        if winners:
            return size, winners
    raise AssertionError("no sufficient subset")


coordinate_minimum, coordinate_winners = minimum(coordinates)
expanded = coordinates + consumer_rows
expanded_minimum, expanded_winners = minimum(expanded)

assert L.rank() == 2
assert coordinate_minimum == 3
assert coordinate_winners == [(0, 1, 2)]
assert expanded_minimum == 2
assert (4, 5) in expanded_winners

v = sp.Matrix([0, 1, 0, 0])
R_omit_two = sp.Matrix.vstack(coordinates[0], coordinates[2], coordinates[3])
assert R_omit_two * v == sp.zeros(3, 1)
assert L * v == sp.Matrix([1, 1])

payload = {
    "status": "pass",
    "theorem": "consumer_relative_phase_port_compiler",
    "consumer_rank_lower_bound": L.rank(),
    "coordinate_only_minimum": coordinate_minimum,
    "coordinate_only_winner_zero_based": list(coordinate_winners[0]),
    "authorized_mixture_minimum": expanded_minimum,
    "authorized_consumer_row_winner_zero_based": [4, 5],
    "kernel_witness": [0, 1, 0, 0],
    "kernel_witness_consumer_output": [1, 1],
    "completion_uniformity_required": True,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "consumer-relative-phase-ports.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
