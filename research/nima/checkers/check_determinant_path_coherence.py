import cmath
import itertools


labels = (0, 1, 2, 3, 4)
weights = {
    label: complex(label + 2, 0.25 * (label + 1))
    for label in labels
}


def potential(state: frozenset[int]) -> complex:
    value = 1.0 + 0.0j
    for label in sorted(state):
        value *= weights[label]
    return value


def increment(state: frozenset[int], label: int) -> complex:
    return potential(state | {label}) / potential(state)


def path_product(order: tuple[int, ...]) -> complex:
    state: frozenset[int] = frozenset()
    value = 1.0 + 0.0j
    for label in order:
        value *= increment(state, label)
        state = state | {label}
    return value


products = [path_product(order) for order in itertools.permutations(labels)]
assert len(products) == 120
assert max(abs(value - products[0]) for value in products) < 1e-12

phase = cmath.exp(0.41j)


def hostile_increment(state: frozenset[int], label: int) -> complex:
    value = increment(state, label)
    if state == frozenset({0}) and label == 2:
        value *= phase
    return value


def hostile_path(order: tuple[int, ...]) -> complex:
    state: frozenset[int] = frozenset()
    value = 1.0 + 0.0j
    for label in order:
        value *= hostile_increment(state, label)
        state = state | {label}
    return value


base_square_left = hostile_increment(frozenset(), 0) * hostile_increment(
    frozenset({0}), 1
)
base_square_right = hostile_increment(frozenset(), 1) * hostile_increment(
    frozenset({1}), 0
)
assert abs(base_square_left - base_square_right) < 1e-12

upper_left = hostile_path((0, 2, 1))
upper_right = hostile_path((2, 0, 1))
assert abs(upper_left - upper_right) > 0.1

print("all 120 five-label paths agree when every edge descends from one potential")
print("a base-level square can pass while an untested upper square fails")
print("higher path failure diagnoses incomplete rank-two coverage")
