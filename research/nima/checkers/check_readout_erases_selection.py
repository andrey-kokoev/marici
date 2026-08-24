#!/usr/bin/env python3
"""Finite non-descent of selectors through a nonfaithful readout."""

lenses = ("phase_0", "phase_1")


def readout(_lens: str) -> str:
    return "same_equal_time_observable"


selected_outputs = {lens: readout(lens) for lens in lenses}
assert len(set(selected_outputs.values())) == 1

# A left inverse would have to recover both different lenses from one output.
possible_recoveries = {
    candidate: all(candidate == lens for lens in lenses) for candidate in lenses
}
assert not any(possible_recoveries.values())

print("distinct selectors become one readout: yes")
print("common readout has no selector-recovering left inverse: yes")
print("checks: 2/2")
