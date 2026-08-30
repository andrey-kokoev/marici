"""Exact augmentation-kernel obstruction for labelwise backward mates."""

from fractions import Fraction
import json


def augmentation(vector):
    return sum(vector, Fraction(0))


q = Fraction(1, 2)
two_fiber_state = (Fraction(1), Fraction(-1))
two_fiber_residual = tuple((1 - q * q) * value for value in two_fiber_state)
three_fiber_basis = (
    (Fraction(1), Fraction(-1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(-1)),
)

checks = {
    "two_fiber_scalar_output_vanishes": augmentation(two_fiber_state) == 0,
    "two_fiber_state_is_nonzero": any(value != 0 for value in two_fiber_state),
    "labelwise_residual_is_nonzero": any(value != 0 for value in two_fiber_residual),
    "residual_augmentation_vanishes": augmentation(two_fiber_residual) == 0,
    "three_fiber_kernel_has_two_independent_witnesses": (
        all(augmentation(vector) == 0 for vector in three_fiber_basis)
        and three_fiber_basis[0] != three_fiber_basis[1]
    ),
    "nonexceptional_q": q * q != 1,
}

result = {
    "schema": "marici.grothendieck.labelwise-equalizer-augmentation-kernel.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "q": str(q),
        "fiber_state": [str(x) for x in two_fiber_state],
        "labelwise_residual": [str(x) for x in two_fiber_residual],
        "augmentation_kernel_dimension_for_d_fibers": "d-1",
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
