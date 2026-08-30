import json
from pathlib import Path


def multiply_complex(left, right):
    a, b = left
    c, d = right
    return (a * c - b * d, a * d + b * c)


def add_complex(left, right):
    return (left[0] + right[0], left[1] + right[1])


def norm_squared(value):
    return value[0] * value[0] + value[1] * value[1]


i = (0, 1)
minus_i = (0, -1)
one = (1, 0)

# Quarter-turn reciprocal transport at t=pi/2.
state = (i, minus_i)
assert all(norm_squared(component) == 1 for component in state)
scalar_readout = add_complex(state[0], state[1])
assert scalar_readout == (0, 0)

# The augmentation covector and its generator image are independent.
augmentation = (1, 1)
augmentation_L = (1, -1)
determinant = augmentation[0] * augmentation_L[1] - augmentation[1] * augmentation_L[0]
assert determinant == -2

# No scalar a satisfies augmentation_L=a*augmentation.
assert augmentation_L[0] * augmentation[1] != augmentation_L[1] * augmentation[0]

# Co-transporting the covector by the inverse quarter turns makes a constant
# pairing, demonstrating that it changes the readout rather than protecting
# the fixed augmentation.
co_covector = (minus_i, i)
co_pairing = add_complex(
    multiply_complex(co_covector[0], state[0]),
    multiply_complex(co_covector[1], state[1]),
)
assert co_pairing == (2, 0)

result = {
    "schema": "marici.rh.source-rotor-readout-no-go.v1",
    "transported_component_norms_squared": [1, 1],
    "fixed_scalar_readout_at_quarter_turn": [0, 0],
    "covector_orbit_rank": 2,
    "eigen_covector_condition": False,
    "covector_co_comparison_pairing": [2, 0],
    "verdict": "invertible labelled spectral comparison does not horizontalize the fixed scalar determinant readout",
}

out = Path(__file__).parents[1] / "results" / "rh-source-rotor-readout-no-go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
