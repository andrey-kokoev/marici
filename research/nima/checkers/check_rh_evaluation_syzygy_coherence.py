from fractions import Fraction as F
import json
from pathlib import Path


M = ((F(1), F(0)), (F(0), F(0)))
R = (F(1), F(0))
local_factors = {
    "U": (F(1), F(0)),
    "V": (F(1), F(1)),
    "W": (F(1), F(3)),
}


def row_times_matrix(row, matrix):
    return tuple(sum(row[i] * matrix[i][j] for i in range(2)) for j in range(2))


def subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


for factor in local_factors.values():
    assert row_times_matrix(factor, M) == R

s_uv = subtract(local_factors["V"], local_factors["U"])
s_vw = subtract(local_factors["W"], local_factors["V"])
s_wu = subtract(local_factors["U"], local_factors["W"])
for syzygy in (s_uv, s_vw, s_wu):
    assert row_times_matrix(syzygy, M) == (F(0), F(0))

triangle = tuple(s_uv[i] + s_vw[i] + s_wu[i] for i in range(2))
assert triangle == (F(0), F(0))

result = {
    "schema": "marici.rh-evaluation-syzygy-coherence.v1",
    "bordered_operator": "[[1,0],[0,0]]",
    "carrier_row": "[1,0]",
    "local_factors": {key: [str(x) for x in value] for key, value in local_factors.items()},
    "overlap_syzygies": {
        "UV": [str(x) for x in s_uv],
        "VW": [str(x) for x in s_vw],
        "WU": [str(x) for x in s_wu],
    },
    "triangle_residual": ["0", "0"],
    "higher_cell_independent": False,
    "remaining_gate": "uniform_pro_syzygy_descent_under_completion",
}

out = Path(__file__).parents[1] / "results" / "rh-evaluation-syzygy-coherence.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
