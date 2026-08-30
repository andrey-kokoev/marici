#!/usr/bin/env python3
"""Exact hostile: conservative mate-coherent transport with a cross zero."""


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def transpose(matrix):
    return tuple(zip(*matrix))


def multiply(left, right):
    columns = transpose(right)
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in columns) for row in left)


def main():
    # Exact quarter-turn, avoiding floating-point trigonometry.
    transfer = ((0, -1), (1, 0))
    identity = ((1, 0), (0, 1))
    assert multiply(transpose(transfer), transfer) == identity
    assert transfer[0][0] * transfer[1][1] - transfer[0][1] * transfer[1][0] == 1

    source = (1, 0)
    transported = mat_vec(transfer, source)
    scalar_readout = transported[0]
    assert transported == (0, 1)
    assert scalar_readout == 0

    print("full_transfer=unitary_orientation_preserving")
    print("mate_coherence=standard_positive_pairing")
    print("selected_transmission_coefficient=zero")
    print("missing_rung=source_derived_open_cell_coherence")


if __name__ == "__main__":
    main()

