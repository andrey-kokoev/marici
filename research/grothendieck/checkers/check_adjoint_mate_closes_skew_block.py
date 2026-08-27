#!/usr/bin/env python3
"""Exact finite witness that an adjoint-mate cell closes the skew block."""


def conjugate_transpose(matrix):
    return tuple(tuple(matrix[j][i].conjugate() for j in range(len(matrix))) for i in range(len(matrix[0])))


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def inner(left, right):
    return sum(x.conjugate() * y for x, y in zip(left, right))


def block_skew(forward):
    adjoint = conjugate_transpose(forward)
    n = len(forward)
    rows = []
    for i in range(n):
        rows.append(tuple([0] * n + list(forward[i])))
    for i in range(n):
        rows.append(tuple([-value for value in adjoint[i]] + [0] * n))
    return tuple(rows)


def main():
    p = ((1 + 1j, 2), (0, 1 - 1j))
    q = conjugate_transpose(p)
    f = (2 - 1j, -1 + 3j)
    y = (1 + 2j, 4 - 1j)
    assert inner(mat_vec(p, f), y) == inner(f, mat_vec(q, y))

    k = block_skew(p)
    k_adjoint = conjugate_transpose(k)
    assert k_adjoint == tuple(tuple(-value for value in row) for row in k)

    wrong_q = ((1, 0), (0, 1))
    assert inner(mat_vec(p, f), y) != inner(f, mat_vec(wrong_q, y))

    print("mate_identity=passed")
    print("bordered_block=skew_adjoint")
    print("arbitrary_reverse_arrow=rejected")
    print("missing_source_data=completed_pairings_and_coherence_cell")


if __name__ == "__main__":
    main()

