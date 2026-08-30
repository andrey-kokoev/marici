import json
from fractions import Fraction
from pathlib import Path


states = [
    (1, Fraction(0)),
    (-1, Fraction(10, 3)),
    (1, Fraction(1)),
    (-1, Fraction(13, 3)),
]


def sum_output(state):
    s, c = state
    return 5 * s + 3 * c


def orientation_output(state):
    s, _ = state
    return s


def shift(state):
    s, c = state
    return s, c + 1


fiber_five = [state for state in states if sum_output(state) == 5]
constrained_continuations = [
    shift(state) for state in fiber_five if sum_output(shift(state)) == 5
]
observed_continuations = [shift(state) for state in fiber_five]
integer_domain = [state for state in fiber_five if state[1].denominator == 1]

checks = {
    "sum_record_has_two_rational_preimages": fiber_five
    == [(1, Fraction(0)), (-1, Fraction(10, 3))],
    "orientation_record_separates_the_two_preimages": {
        orientation_output(state) for state in fiber_five
    }
    == {-1, 1},
    "source_constraint_forbids_common_shift": constrained_continuations == [],
    "observed_fiber_allows_common_shift": len(observed_continuations) == 2,
    "shifted_observation_changes_from_five_to_eight": all(
        sum_output(state) == 8 for state in observed_continuations
    ),
    "integer_domain_removes_reflected_rational_state": integer_domain
    == [(1, Fraction(0))],
    "lattice_restriction_does_not_add_an_output_value": {
        sum_output(state) for state in integer_domain
    }
    == {5},
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "current_fiber": [[s, str(c)] for s, c in fiber_five],
    "observed_shift_continuations": [
        [s, str(c), str(sum_output((s, c)))] for s, c in observed_continuations
    ],
    "classification": {
        "constraint": "restricts admitted state and transition domain",
        "observer": "maps admitted states to records without itself deleting states",
        "lattice": "types the source domain and changes uniqueness without adding information",
    },
}

output = Path(__file__).parents[1] / "results" / "constraint_is_not_observer.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

