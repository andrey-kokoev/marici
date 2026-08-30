#!/usr/bin/env python3
"""Exact finite witness for the skew-adjoint incidence seam theorem."""


def mat_vec(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a)))


def main():
    # D is real skew-symmetric, hence complex skew-adjoint.
    d = ((0, -1), (1, 0))
    psi_plus = (1, -1j)
    psi_minus = (1, 1j)
    assert mat_vec(d, psi_plus) == tuple(1j * x for x in psi_plus)
    assert mat_vec(d, psi_minus) == tuple(-1j * x for x in psi_minus)
    assert (1j).real == 0 and (-1j).real == 0

    # Scalar nullity by itself can be placed off the seam.
    hostile_zero = 1 + 2j
    scalar = lambda z: z - hostile_zero
    assert scalar(hostile_zero) == 0
    assert hostile_zero.real != 0

    print("operator=skew_adjoint_2x2")
    print("spectral_incidence=imaginary_axis")
    print("scalar_nullity_alone=unconfined")
    print("missing_arrow=null_pullback_to_operator_domain_incidence")


if __name__ == "__main__":
    main()

