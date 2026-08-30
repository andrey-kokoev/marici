import itertools
import json
from pathlib import Path


states = tuple(itertools.product((0, 1), repeat=2))
zero = (0, 0)


def value(state):
    return state[0]


def joint(state):
    return state


def triangular(state):
    value_coordinate, flux = state
    return value_coordinate, value_coordinate ^ flux


def mixing(state):
    value_coordinate, flux = state
    return flux, value_coordinate


def zero_propagates(readout, action, domain):
    zero_record = readout(zero)
    return all(
        readout(action(state)) == zero_record
        for state in domain
        if readout(state) == zero_record
    )


def jointly_faithful(readout, action, domain):
    zero_record = readout(zero)
    return all(
        state == zero
        for state in domain
        if readout(state) == zero_record
        and readout(action(state)) == zero_record
    )


value_kernel = {state for state in states if value(state) == 0}
source_transversal = ((0, 0), (1, 0))

checks = {
    "scalar_value_kernel_is_nontrivial": value_kernel == {(0, 0), (0, 1)},
    "triangular_transport_preserves_value_zero": zero_propagates(
        value, triangular, states
    ),
    "triangular_value_probes_are_not_jointly_faithful": not jointly_faithful(
        value, triangular, states
    ),
    "pure_flux_is_the_invisible_witness": triangular((0, 1)) == (0, 1)
    and value((0, 1)) == 0,
    "mixing_exposes_flux": value(mixing((0, 1))) == 1,
    "mixing_breaks_scalar_zero_propagation": not zero_propagates(
        value, mixing, states
    ),
    "joint_present_record_has_trivial_zero_fiber": {
        state for state in states if joint(state) == joint(zero)
    }
    == {zero},
    "joint_record_satisfies_both_gates": zero_propagates(
        joint, triangular, states
    )
    and jointly_faithful(joint, triangular, states),
    "source_restriction_makes_scalar_zero_fiber_trivial": {
        state for state in source_transversal if value(state) == 0
    }
    == {zero},
    "scalar_gates_hold_on_source_restriction": zero_propagates(
        value, triangular, source_transversal
    )
    and jointly_faithful(value, triangular, source_transversal),
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "value_kernel": [list(state) for state in sorted(value_kernel)],
    "source_transversal": [list(state) for state in source_transversal],
    "classification": {
        "no_go": "global zero propagation plus joint future faithfulness forces a trivial present zero fiber",
        "closed_interface": "sequential bisimulation is sufficient relative to the frozen complete boundary",
        "open_extensions": "environment-complete sequential equivalence is required",
    },
}

output = Path(__file__).parents[1] / "results" / "zero_propagation_observability_no_go.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

