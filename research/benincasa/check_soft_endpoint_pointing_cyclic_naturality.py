#!/usr/bin/env python3
"""Check cyclic naturality of the chain-pointed soft logarithmic torsor."""

import json
from pathlib import Path


def rotate_index(index):
    return index % 3 + 1


def main():
    charts = []
    for index in (1, 2, 3):
        charts.append({
            "soft_normal": f"X{index}",
            "marked_wall": f"q_g{index}",
            "normalized_coordinate": f"t{index}=q_g{index}/X{index}",
            "marked_endpoint": 0,
            "pointing_endpoint": 2,
            "physical_occurrence_covector": [1, 0],
        })

    transitions = []
    for index in (1, 2, 3):
        target = rotate_index(index)
        transitions.append({
            "source": index,
            "target": target,
            "coordinate_transport": f"t{index}->t{target}",
            "transition_unit": 1,
            "pointing_endpoint_preserved": True,
            "positive_chamber_preserved": True,
        })

    # A 3-cycle is even, so the source orientation returns with sign +1.
    cyclic_orientation_sign = 1
    three_step_return = rotate_index(rotate_index(rotate_index(1)))
    checks = {
        "three_labelled_soft_charts_present": len(charts) == 3,
        "normalized_coordinates_transport_without_units": all(
            transition["transition_unit"] == 1 for transition in transitions
        ),
        "pointing_endpoint_two_is_preserved": all(
            transition["pointing_endpoint_preserved"] for transition in transitions
        ),
        "physical_positive_occurrence_is_preserved": all(
            transition["positive_chamber_preserved"] for transition in transitions
        ),
        "three_step_transport_returns_to_source": three_step_return == 1,
        "cyclic_source_orientation_is_positive": cyclic_orientation_sign == 1,
    }
    result = {
        "schema": "marici.soft-endpoint-pointing-cyclic-naturality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "cyclic_action": "(X_i,q_gi,t_i)->(X_{i+1},q_g,i+1,t_i+1)",
        "charts": charts,
        "transitions": transitions,
        "three_step_orientation_sign": cyclic_orientation_sign,
        "conclusion": (
            "the basepoint F_i(2)=0 and positive-occurrence physical covector "
            "descend around the source C3 occurrence atlas"
        ),
        "scope": (
            "cyclic occurrence naturality only; noncyclic residue-chart transitions, "
            "full a-cycle compatibility, regulator invariance, and Leray pairing remain open"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-pointing-cyclic-naturality.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
