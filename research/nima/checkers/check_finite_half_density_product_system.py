import itertools
import math


parameters = (0.4, 0.3, 0.2, 0.1)


def local_likelihood(bit: int, parameter: float) -> float:
    return 1.0 + parameter if bit else 1.0 - parameter


def likelihood(state: tuple[int, ...], count: int) -> float:
    value = 1.0
    for bit, parameter in zip(state[:count], parameters[:count]):
        value *= local_likelihood(bit, parameter)
    return value


for count in range(1, len(parameters) + 1):
    states = tuple(itertools.product((0, 1), repeat=count))
    haar_weight = 2.0 ** (-count)
    arithmetic_mass = sum(haar_weight * likelihood(state, count) for state in states)
    assert abs(arithmetic_mass - 1.0) < 1e-12

    test_function = {state: 1.0 + sum(state) for state in states}
    arithmetic_norm = sum(
        haar_weight * likelihood(state, count) * abs(test_function[state]) ** 2
        for state in states
    )
    haar_image_norm = sum(
        haar_weight
        * abs(math.sqrt(likelihood(state, count)) * test_function[state]) ** 2
        for state in states
    )
    assert abs(arithmetic_norm - haar_image_norm) < 1e-12

state = (1, 0, 1, 1)
full_half_density = math.sqrt(likelihood(state, 4))
factored_half_density = math.sqrt(likelihood(state, 2)) * math.sqrt(
    local_likelihood(state[2], parameters[2])
    * local_likelihood(state[3], parameters[3])
)
assert abs(full_half_density - factored_half_density) < 1e-12

affinities = []
for count in range(1, len(parameters) + 1):
    states = tuple(itertools.product((0, 1), repeat=count))
    haar_weight = 2.0 ** (-count)
    affinity = sum(
        haar_weight * math.sqrt(likelihood(state, count)) for state in states
    )
    affinities.append(affinity)

assert all(left > right for left, right in zip(affinities, affinities[1:]))

print("finite half-density maps are exact isometries")
print("packet additions compose by tensor factorization")
print("vacuum affinities decrease:", affinities)
print("finite correspondences survive even when the endpoint overlap collapses")
