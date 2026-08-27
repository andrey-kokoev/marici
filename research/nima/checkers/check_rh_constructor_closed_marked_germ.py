import json
from pathlib import Path


def target(v):
    return v[0]


def shift(v):
    x, y, z = v
    return (y, z, 0)


def iterate(v, count):
    for _ in range(count):
        v = shift(v)
    return v


x_direction = (1, 0, 0)
y_direction = (0, 1, 0)
z_direction = (0, 0, 1)

assert target(x_direction) == 1
assert target(y_direction) == 0
assert target(z_direction) == 0
assert target(iterate(y_direction, 1)) == 1
assert target(iterate(z_direction, 1)) == 0
assert target(iterate(z_direction, 2)) == 1

directions = [x_direction, y_direction, z_direction]
visibility_words = {
    "x": [target(iterate(x_direction, n)) for n in range(3)],
    "y": [target(iterate(y_direction, n)) for n in range(3)],
    "z": [target(iterate(z_direction, n)) for n in range(3)],
}
assert all(any(target(iterate(direction, n)) != 0 for n in range(3)) for direction in directions)

# The immediate quotient would identify z with zero, but two shifts distinguish
# their representatives, so the constructor does not descend through it.
zero = (0, 0, 0)
assert target(z_direction) == target(zero)
assert target(iterate(z_direction, 2)) != target(iterate(zero, 2))

result = {
    "schema": "marici.rh.constructor-closed-marked-germ.v1",
    "visibility_words": visibility_words,
    "immediate_kernel_dimension": 2,
    "one_step_closed_kernel_dimension": 1,
    "full_constructor_closed_kernel_dimension": 0,
    "premature_quotient_rejected": True,
    "verdict": "target-fiber equivalence must be congruence-closed under every admitted source constructor",
}

out = Path(__file__).parents[1] / "results" / "rh-constructor-closed-marked-germ.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
