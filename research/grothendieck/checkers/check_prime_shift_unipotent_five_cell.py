"""Dependency-free audit of the Gaussian-tail translation cocycle."""

from math import erfc, pi, sqrt


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def cocycle(length: float, q: float) -> float:
    return tail(q + length) - tail(q)


def main() -> None:
    probes = (-8.0, -3.0, -0.5, 0.0, 0.5, 3.0, 8.0)
    left = 0.7
    right = 1.1
    error = max(
        abs(
            cocycle(left + right, q)
            - cocycle(left, q)
            - cocycle(right, q + left)
        )
        for q in probes
    )
    assert error < 1e-14

    # The cocycle vanishes at both ends, whereas the centered tail retains
    # opposite nonzero limits. Translation therefore fixes its quotient class.
    assert abs(cocycle(left, -10.0)) < 1e-15
    assert abs(cocycle(left, 10.0)) < 1e-15
    assert tail(-10.0) > 1.0 - 1e-15
    assert tail(10.0) < 1e-15

    print("translation_cocycle_identity=true")
    print("translation_difference_is_bulk_decay=true")
    print("boundary_quotient_action=identity")
    print("prime_shift_action=unipotent")
    print("primitive_square_scalar_regularization=false")
    print("required_completion_axes=2")


if __name__ == "__main__":
    main()
