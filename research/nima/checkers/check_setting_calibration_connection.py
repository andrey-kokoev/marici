import itertools
import json
from pathlib import Path


ORDER = 4
PHASES = tuple(range(ORDER))


def add(left, right):
    return (left + right) % ORDER


def subtract(left, right):
    return (left - right) % ORDER


def observe(source, nuisance):
    return add(source, nuisance)


def transport(nuisance_i, nuisance_j):
    return subtract(nuisance_i, nuisance_j)


assignments_checked = 0
for sources in itertools.product(PHASES, repeat=3):
    for nuisances in itertools.product(PHASES, repeat=3):
        observations = [
            observe(source, nuisance)
            for source, nuisance in zip(sources, nuisances)
        ]
        transports = {
            (i, j): transport(nuisances[i], nuisances[j])
            for i in range(3)
            for j in range(3)
        }
        for i in range(3):
            for j in range(3):
                corrected = subtract(
                    subtract(observations[i], observations[j]),
                    transports[(i, j)],
                )
                assert corrected == subtract(sources[i], sources[j])
                assert add(transports[(i, j)], transports[(j, i)]) == 0
        assert add(transports[(0, 1)], transports[(1, 2)]) == transports[(0, 2)]
        assert add(
            add(transports[(0, 1)], transports[(1, 2)]),
            transports[(2, 0)],
        ) == 0
        assignments_checked += 1

hostile = {(0, 1): 0, (1, 2): 0, (0, 2): 1}
hostile_residual = subtract(
    add(hostile[(0, 1)], hostile[(1, 2)]),
    hostile[(0, 2)],
)
assert hostile_residual != 0

realizations = [
    nuisances
    for nuisances in itertools.product(PHASES, repeat=3)
    if transport(nuisances[0], nuisances[1]) == hostile[(0, 1)]
    and transport(nuisances[1], nuisances[2]) == hostile[(1, 2)]
    and transport(nuisances[0], nuisances[2]) == hostile[(0, 2)]
]
assert realizations == []

result = {
    "schema": "marici.setting-calibration-connection.v1",
    "phase_group": "C4",
    "assignments_checked": assignments_checked,
    "relative_source_correction_exact": True,
    "inverse_law_exact": True,
    "triangle_flatness_exact": True,
    "hostile_connectors": {
        "eta_01": hostile[(0, 1)],
        "eta_12": hostile[(1, 2)],
        "eta_02": hostile[(0, 2)],
    },
    "hostile_triangle_residual": hostile_residual,
    "hostile_frame_realizations": realizations,
    "verdict": "multi-setting calibration is a flat connection, not necessarily equality of nuisance frames",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "setting-calibration-connection.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
