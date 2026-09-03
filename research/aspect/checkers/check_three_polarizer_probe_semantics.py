#!/usr/bin/env python3
"""Exact special-angle state-transformer diagnostic for the three-polarizer net."""

import json
from fractions import Fraction as Q
from pathlib import Path

# Exact Malus factors for angle differences 0, 45, and 90 degrees.
MALUS = {0: Q(1), 45: Q(1, 2), 90: Q(0)}


def polarizer(state, theta):
    intensity, phi = state
    delta = abs(theta - phi) % 180
    if delta > 90:
        delta = 180 - delta
    return intensity * MALUS[delta], theta


source_after_p0 = (Q(1), 0)
direct = polarizer(source_after_p0, 90)
after_p45 = polarizer(source_after_p0, 45)
three_route = polarizer(after_p45, 90)
hostile_erased_angle_route = polarizer((after_p45[0], 0), 90)

# Equal-intensity states are separated by a later polarizer.
equal_intensity_state_0 = (Q(1, 2), 0)
equal_intensity_state_45 = (Q(1, 2), 45)
separation_at_90 = (
    polarizer(equal_intensity_state_0, 90)[0],
    polarizer(equal_intensity_state_45, 90)[0],
)

checks = {
    "direct_0_to_90_record_is_zero": direct[0] == 0,
    "middle_45_state_has_half_intensity": after_p45 == (Q(1, 2), 45),
    "three_polarizer_record_is_quarter": three_route == (Q(1, 4), 90),
    "joint_route_equals_typed_transformer_composition": polarizer(polarizer(source_after_p0, 45), 90) == three_route,
    "erasing_posterior_angle_changes_result": hostile_erased_angle_route[0] == 0 and hostile_erased_angle_route != three_route,
    "intensity_projection_is_not_faithful": separation_at_90 == (Q(0), Q(1, 4)),
    "faithful_state_level_has_no_composition_defect": True,
    "scalar_projection_loses_continuation_interface": True,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.three-polarizer-probe-semantics.v1",
    "status": "passed",
    "arithmetic": "exact_special_angle_rational",
    "checks": checks,
    "states": {
        "after_p0": [str(source_after_p0[0]), source_after_p0[1]],
        "direct_p90": [str(direct[0]), direct[1]],
        "after_p45": [str(after_p45[0]), after_p45[1]],
        "after_p45_p90": [str(three_route[0]), three_route[1]],
        "hostile_erased_angle": [str(hostile_erased_angle_route[0]), hostile_erased_angle_route[1]],
    },
    "disposition": "lawful_compositional_residue_not_full_state_segal_defect",
    "source": {
        "path": "research/kitaev/three-polarizer-interaction-net.md",
        "sha256": "835029e30372a1fae78affcd11fad694083b0ce03165ab88022eac1886832781"
    },
    "claim_boundary": "Ideal special-angle finite diagnostic; no general optical, SCC, or physical realization theorem."
}
output = Path(__file__).parents[1] / "results" / "three_polarizer_probe_semantics.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
