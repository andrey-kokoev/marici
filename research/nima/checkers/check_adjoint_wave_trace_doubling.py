import cmath
import math


positive_events = {
    math.log(2): 1.0 + 0.2j,
    2.0 * math.log(2): 0.5 - 0.1j,
    math.log(3): 0.8 + 0.3j,
}


def reflect(events: dict[float, complex]) -> dict[float, complex]:
    return {-length: coefficient.conjugate() for length, coefficient in events.items()}


completed_events = dict(positive_events)
completed_events.update(reflect(positive_events))
completed_events[0.0] = -0.4 + 0.0j

for length, coefficient in completed_events.items():
    reflected = completed_events.get(-length)
    assert reflected is not None
    assert abs(reflected - coefficient.conjugate()) < 1e-12

one_sided_failures = [
    length for length in positive_events if -length not in positive_events
]
assert len(one_sided_failures) == len(positive_events)

hostile_events = dict(completed_events)
first_length = next(iter(positive_events))
hostile_events[-first_length] *= cmath.exp(0.3j)
assert abs(
    hostile_events[-first_length] - hostile_events[first_length].conjugate()
) > 0.1

eigenvalues = (-1.5, 0.25, 2.0)
weights = (1.0, -0.2, 0.4)


def wave(q: float) -> complex:
    return sum(
        weight * cmath.exp(1j * q * eigenvalue)
        for weight, eigenvalue in zip(weights, eigenvalues)
    )


for q in (0.0, 0.7, 2.1, 5.0):
    assert abs(wave(-q) - wave(q).conjugate()) < 1e-12

print("one-sided prime events fail adjoint trace symmetry")
print("reflected two-sector packet with a real fixed-locus term passes")
print("wrong reflected phase is detected")
print("finite self-adjoint wave trace satisfies the same involution")
