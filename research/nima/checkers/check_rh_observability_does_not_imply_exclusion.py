import json
from pathlib import Path


analysis = ((1, 0), (0, 1))
scalar = (1, 1)
hostile = (1, -1)


def matrix_vector(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


features = matrix_vector(analysis, hostile)
readout = dot(scalar, features)

assert features == hostile
assert hostile != (0, 0)
assert readout == 0

result = {
    "analysis_matrix": analysis,
    "analysis_rank": 2,
    "smallest_singular_value": 1,
    "nonzero_hostile_state": hostile,
    "complete_feature_vector": features,
    "scalar_projection": scalar,
    "scalar_readout": readout,
    "conclusion": "complete linear observability does not imply scalar zero exclusion",
}

output = Path(__file__).parents[1] / "results" / "rh-observability-does-not-imply-exclusion.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

