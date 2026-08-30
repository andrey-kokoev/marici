import itertools
import json
from pathlib import Path


ORDER = 4
PHASES = tuple(range(ORDER))


def add(left, right):
    return (left + right) % ORDER


def subtract(left, right):
    return (left - right) % ORDER


flat_count = 0
curved_count = 0
recoveries_checked = 0

for eta_01, eta_12, eta_02 in itertools.product(PHASES, repeat=3):
    indirect = add(eta_01, eta_12)
    curvature = subtract(indirect, eta_02)
    if curvature == 0:
        flat_count += 1
    else:
        curved_count += 1

    for source in PHASES:
        direct_observed = add(source, eta_02)
        indirect_observed = add(source, indirect)
        assert subtract(direct_observed, eta_02) == source
        assert subtract(indirect_observed, indirect) == source
        if curvature:
            assert direct_observed != indirect_observed
        recoveries_checked += 2

assert flat_count == 16
assert curved_count == 48

hostile = {"eta_01": 0, "eta_12": 0, "eta_02": 1, "source": 2}
hostile_indirect = add(hostile["eta_01"], hostile["eta_12"])
hostile_curvature = subtract(hostile_indirect, hostile["eta_02"])
hostile_direct_observed = add(hostile["source"], hostile["eta_02"])
hostile_indirect_observed = add(hostile["source"], hostile_indirect)
assert hostile_curvature == 3
assert hostile_direct_observed != hostile_indirect_observed
assert subtract(hostile_direct_observed, hostile["eta_02"]) == hostile["source"]
assert subtract(hostile_indirect_observed, hostile_indirect) == hostile["source"]

result = {
    "schema": "marici.route-dependent-calibration.v1",
    "phase_group": "C4",
    "connections_checked": 64,
    "flat_connections": flat_count,
    "curved_connections": curved_count,
    "route_recoveries_checked": recoveries_checked,
    "hostile": {
        **hostile,
        "curvature": hostile_curvature,
        "direct_observed": hostile_direct_observed,
        "indirect_observed": hostile_indirect_observed,
        "both_route_corrected_values": [hostile["source"], hostile["source"]],
    },
    "endpoint_erasure_creates_apparent_contradiction": True,
    "verdict": "flatness governs descent to endpoints; curved calibration is lawful only with retained route structure",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "route-dependent-calibration.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
