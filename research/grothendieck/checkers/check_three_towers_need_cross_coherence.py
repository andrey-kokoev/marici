#!/usr/bin/env python3
"""Exact witness that input, output, and control closure are independent."""


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def norm_squared(vector):
    return sum(value * value for value in vector)


def main():
    state = (1, -1)

    # Input tower: a faithful curvature port detects the packet.
    input_curvature = ((1, 0), (0, 1))
    assert norm_squared(mat_vec(input_curvature, state)) == 2

    # Output tower: scalar aggregation erases it.
    output = state[0] + state[1]
    assert output == 0

    # Control tower: an exact unitary route preserves its norm.
    control = ((0, -1), (1, 0))
    transported = mat_vec(control, state)
    assert norm_squared(transported) == norm_squared(state)

    print("input_tower=faithful_on_state")
    print("output_tower=scalar_null")
    print("control_tower=norm_preserving")
    print("missing_structure=cross_tower_Ward_coherence")


if __name__ == "__main__":
    main()

