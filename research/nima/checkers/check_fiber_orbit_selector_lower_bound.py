"""Finite orbit-size and selector distinguishability checks."""

from math import ceil, log2


def required_bits(orbit_size):
    return ceil(log2(orbit_size))


def selector_gate(orbit_size, selector_states):
    if selector_states < orbit_size:
        return {
            "code": "selector_distinguishability_deficit",
            "orbit_size": orbit_size,
            "selector_states": selector_states,
            "minimum_binary_width": required_bits(orbit_size),
        }
    return {
        "status": "information_sufficient_authority_unchecked",
        "orbit_size": orbit_size,
        "selector_states": selector_states,
    }


two_fiber_failure = selector_gate(2, 1)
two_fiber_information_pass = selector_gate(2, 2)
eight_orbit_failure = selector_gate(8, 4)

assert two_fiber_failure["code"] == "selector_distinguishability_deficit"
assert two_fiber_failure["minimum_binary_width"] == 1
assert two_fiber_information_pass["status"] == "information_sufficient_authority_unchecked"
assert eight_orbit_failure["minimum_binary_width"] == 3

print("two-candidate missing-selector witness:", two_fiber_failure)
print("two-state selector result:", two_fiber_information_pass)
print("eight-orbit four-state witness:", eight_orbit_failure)
print("PASS: orbit size lower-bounds selector information but not authority")
