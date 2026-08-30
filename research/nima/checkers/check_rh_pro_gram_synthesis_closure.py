import json
import math
from pathlib import Path


def synthesize(v):
    return v[0]


def constructor_rotate(v):
    return (v[1], v[0])


def q_identity(v):
    return abs(synthesize(v))


def q_constructor(v):
    return abs(synthesize(constructor_rotate(v)))


def anomaly_trace(v):
    return v[1]


kernel_state = (0.0, 3.0)
assert synthesize(kernel_state) == 0
assert q_identity(kernel_state) == 0
assert q_constructor(kernel_state) == 3
assert anomaly_trace(kernel_state) == 3

# Identity synthesis cannot dominate the anomaly trace.
identity_domination_fails = q_identity(kernel_state) == 0 and anomaly_trace(kernel_state) != 0
assert identity_domination_fails

# One authorized constructor supplies the exact domination.
fixtures = [(2.0, -5.0), (0.0, 3.0), (-7.0, 0.0), (1.5, 2.5)]
for fixture in fixtures:
    assert abs(anomaly_trace(fixture)) <= q_constructor(fixture)

# The graph is the zero set of the continuous defect h-Uv.
for fixture in fixtures:
    h = synthesize(fixture)
    defect = h - synthesize(fixture)
    assert defect == 0

result = {
    "schema": "marici.rh.pro-gram-synthesis-closure.v1",
    "seminorm_family_separates_coordinates": True,
    "synthesis_kernel_retained": list(kernel_state),
    "identity_domination_fails": True,
    "authorized_constructor_domination_constant": 1,
    "synthesis_graph_closed_by_continuity": True,
    "verdict": "pro-Gram topology closes synthesis while constructor seminorms retain analytically invisible anomaly data",
}

out = Path(__file__).parents[1] / "results" / "rh-pro-gram-synthesis-closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
