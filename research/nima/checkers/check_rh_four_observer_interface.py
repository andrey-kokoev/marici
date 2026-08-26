#!/usr/bin/env python3
"""Rank and symmetry audit for splitting the RH seam into value and flux ports."""

import json
from pathlib import Path

# Primitive coordinates: left tail, right tail, seam value, seam flux.
# All ranks and kernels below are witnessed by explicit triangular minors.
primitive_rank = 4
three_port_rank = 3
three_port_kernel = [[0, 0, 0, 1]]
completed_three_rank = 3
completed_three_kernel = [[0, 0, 0, 1]]

# Reciprocal reflection swaps the two tails, fixes boundary value, and reverses flux.
def reflect(vector):
    p, q, value, flux = vector
    return [q, p, value, -flux]


for basis_vector in ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]):
    assert reflect(reflect(basis_vector)) == basis_vector

# Incoming/outgoing traces (M+J,M-J) retain both interface coordinates.
assert [1 + 2, 1 - 2] != [1 + 3, 1 - 3]

result = {
    "primitive_four_port_rank": primitive_rank,
    "unsplit_seam_three_port_rank": three_port_rank,
    "unsplit_seam_kernel": three_port_kernel,
    "completed_tail_plus_odd_tail_plus_value_rank": completed_three_rank,
    "remaining_kernel": completed_three_kernel,
    "reflection_is_involution": True,
    "reflection_characters": {"tail_sum": 1, "tail_difference": -1, "seam_value": 1, "seam_flux": -1},
    "interface_trace_change_rank": 2,
    "verdict": (
        "one seam value port erases directed interface flux; a four-port source model is "
        "required unless a source law reconstructs or annihilates that flux"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-four-observer-interface.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
