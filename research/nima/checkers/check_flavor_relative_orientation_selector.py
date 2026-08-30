from fractions import Fraction
import json
from pathlib import Path


quark_magnitude = Fraction(20, 9)
reference_magnitude = Fraction(7, 3)
coupling = Fraction(2, 5)

states = tuple(
    (quark_sign, reference_sign)
    for quark_sign in (-1, 1)
    for reference_sign in (-1, 1)
)


def relative_character(state):
    quark_sign, reference_sign = state
    return quark_sign * reference_sign


def energy(state):
    quark_sign, reference_sign = state
    quark_cubic = quark_sign * quark_magnitude
    reference_cubic = reference_sign * reference_magnitude
    return -coupling * quark_cubic * reference_cubic


aligned = tuple(state for state in states if relative_character(state) == 1)
anti_aligned = tuple(state for state in states if relative_character(state) == -1)
assert len(aligned) == len(anti_aligned) == 2
assert all(energy(state) < energy(other) for state in aligned for other in anti_aligned)

# Simultaneous reflection preserves both the relational character and energy.
for state in states:
    reflected = (-state[0], -state[1])
    assert relative_character(reflected) == relative_character(state)
    assert energy(reflected) == energy(state)

# The relative character is faithful on the quotient by simultaneous flip.
orbits = {
    frozenset((state, (-state[0], -state[1])))
    for state in states
}
assert len(orbits) == 2
assert len({relative_character(next(iter(orbit))) for orbit in orbits}) == 2

# Fixing the reference sign makes the quark sign appear absolute, but this is a
# gauge choice unless the reference orientation has an independent source.
fixed_reference_states = tuple(state for state in states if state[1] == 1)
assert len(fixed_reference_states) == 2

result = {
    "schema": "marici.nima.flavor-relative-orientation-selector.v1",
    "raw_orientation_states": len(states),
    "simultaneous_reflection_orbits": len(orbits),
    "relative_character_classes": 2,
    "positive_coupling_prefers_aligned_relative_orientation": True,
    "simultaneous_reflection_preserves_energy": True,
    "relative_character_faithful_on_global_reflection_quotient": True,
    "absolute_quark_sign_selected": False,
    "verdict": (
        "A cross-sector product of signed cubic moments can select relative "
        "orientation while preserving simultaneous reflection. One relational "
        "signed observer is faithful on the resulting global-reflection "
        "quotient; no absolute charge sign is produced."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-relative-orientation-selector.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
