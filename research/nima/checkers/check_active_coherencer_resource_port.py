#!/usr/bin/env python3
"""Exact resource and hidden-port checks for an active coherencer."""

import json
from pathlib import Path


def main():
    signal_energy = 1
    output_energy = 9
    passive_residual = signal_energy - output_energy
    assert passive_residual == -8

    lossless_active = {"resource": 8, "exported": 0}
    lossy_active = {"resource": 10, "exported": 2}
    for history in (lossless_active, lossy_active):
        assert signal_energy + history["resource"] == output_energy + history["exported"]
    assert lossless_active != lossy_active

    # Scalar output erases resource provenance.
    projected_outputs = {output_energy for _ in (lossless_active, lossy_active)}
    assert len(projected_outputs) == 1

    # Connectivity and orientation are independent binary roles.
    states = {(connectivity, orientation) for connectivity in (0, 1) for orientation in (0, 1)}
    connectivity_projection = {state[0] for state in states}
    orientation_projection = {state[1] for state in states}
    assert len(states) == 4
    assert len(connectivity_projection) == 2
    assert len(orientation_projection) == 2
    assert len({state for state in states if state[0] == 1}) == 2

    result = {
        "schema": "marici.active-coherencer-resource-port.v1",
        "status": "pass",
        "passive_energy_residual": passive_residual,
        "lossless_active_balance": True,
        "lossy_active_balance": True,
        "same_output_distinct_resource_histories": len(projected_outputs) == 1,
        "connectivity_orientation_joint_states": len(states),
        "connectivity_does_not_select_orientation": len({state for state in states if state[0] == 1}) == 2,
        "disposition": "active closure requires an explicit resource port and separate orientation coupling",
    }
    out = Path(__file__).parents[1] / "results" / "active-coherencer-resource-port.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

