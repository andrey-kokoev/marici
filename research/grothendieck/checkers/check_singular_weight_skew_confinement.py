#!/usr/bin/env python3
"""Dependency-free witness for weighted skew-adjoint confinement."""


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scale(value, vector):
    return tuple(value * item for item in vector)


def main():
    # Singular P, but the positive-weight state is confined to imaginary z.
    a = ((1j, 0), (0, 0))
    p = ((1, 0), (0, 0))
    psi = (1, 0)
    z = -1j
    assert add(mat_vec(a, psi), scale(z, mat_vec(p, psi))) == (0, 0)
    p_weight = sum(x.conjugate() * y for x, y in zip(psi, mat_vec(p, psi))).real
    assert p_weight == 1 and z.real == 0

    # The strict weight gate is necessary: this null-weight state solves the
    # same pencil for every parameter, including an off-seam one.
    null_state = (0, 1)
    hostile_z = 2 + 3j
    assert add(mat_vec(a, null_state), scale(hostile_z, mat_vec(p, null_state))) == (0, 0)
    assert hostile_z.real != 0

    # The native one-way source incidence is not skew-adjoint.
    forward = ((0, 1), (0, 0))
    forward_adjoint = ((0, 0), (1, 0))
    assert forward != tuple(tuple(-x for x in row) for row in forward_adjoint)

    print("singular_weight=allowed")
    print("positive_weight_state=seam_confined")
    print("null_weight_state=unconfined")
    print("remaining_gate=source_derived_reverse_incidence")


if __name__ == "__main__":
    main()

