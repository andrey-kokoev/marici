import json


grade_states = {
    "primitive": [1, 0, 0],
    "square": [0, 1, 0],
    "connected": [0, 0, 1],
}


def scalar_readout(state):
    return sum(state)


def deletion_profile(state):
    return [
        scalar_readout([0, state[1], state[2]]),
        scalar_readout([state[0], 0, state[2]]),
        scalar_readout([state[0], state[1], 0]),
    ]


records = []
for grade, state in grade_states.items():
    records.append(
        {
            "grade": grade,
            "state": state,
            "scalar_readout": scalar_readout(state),
            "deletion_profile": deletion_profile(state),
        }
    )

assert all(record["scalar_readout"] == 1 for record in records)
assert len({tuple(record["deletion_profile"]) for record in records}) == 3

# Rank-nullity for q = [1, 1, 1].
scalar_rank = 1
carrier_dimension = 3
kernel_dimension = carrier_dimension - scalar_rank
assert kernel_dimension == 2

result = {
    "schema": "marici.nima.filtered-three-grade-carrier.v1",
    "records": records,
    "carrier_dimension": carrier_dimension,
    "scalar_rank": scalar_rank,
    "scalar_kernel_dimension": kernel_dimension,
    "scalar_readout_is_faithful": False,
    "minimum_state_type": "filtered_relative_determinant_carrier",
    "next_gate": "common_filtered_boundary_lift",
}
print(json.dumps(result, indent=2, sort_keys=True))

