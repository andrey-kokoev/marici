import json
from pathlib import Path


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix)))


def multiply(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def subtract(left, right):
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def block(zero, upper, lower):
    return tuple(zero[i] + upper[i] for i in range(3)) + tuple(lower[i] + zero[i] for i in range(3))


I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
Z = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
P = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
PT = transpose(P)

kernel_clockwise = block(Z, P, PT)
kernel_counterclockwise = block(Z, PT, P)
family_swap = block(Z, I, I)

assert transpose(kernel_clockwise) == kernel_clockwise
assert transpose(kernel_counterclockwise) == kernel_counterclockwise
assert multiply(multiply(family_swap, kernel_clockwise), family_swap) == kernel_counterclockwise
assert multiply(family_swap, family_swap) == tuple(
    tuple(1 if i == j else 0 for j in range(6)) for i in range(6)
)

ordered_odd_clockwise = subtract(P, PT)
ordered_odd_counterclockwise = subtract(PT, P)
assert ordered_odd_counterclockwise == tuple(tuple(-x for x in row) for row in ordered_odd_clockwise)

# A frame-transition loop carries C2 holonomy. Even swap parity returns the
# ordered frame; odd parity flips the extracted orientation.
def holonomy(swaps):
    return sum(swaps) % 2


trivial_loop = (1, 1, 0)
flipping_loop = (1, 0, 0)
assert holonomy(trivial_loop) == 0
assert holonomy(flipping_loop) == 1

result = {
    "schema": "marici.nima.flavor-bipartite-orientation-torsor.v1",
    "full_kernels_reciprocal": True,
    "family_swap_involutive": True,
    "family_swap_conjugates_clockwise_to_counterclockwise": True,
    "ordered_odd_channel_flips_sign": True,
    "trivial_loop_holonomy": holonomy(trivial_loop),
    "flipping_loop_holonomy": holonomy(flipping_loop),
    "absolute_orientation_from_unordered_block": False,
    "verdict": (
        "The directed bipartite Flavor channel is a C2 orientation torsor. "
        "A source-calibrated ordered family frame and its transition holonomy "
        "are required before the reversal-odd readout has an absolute sign."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-bipartite-orientation-torsor.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
