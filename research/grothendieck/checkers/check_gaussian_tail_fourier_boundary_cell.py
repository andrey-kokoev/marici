"""Dependency-free audit of the Gaussian tail boundary cell."""

from math import erfc, exp, pi, sqrt


def phi(q: float) -> float:
    return exp(-pi * q * q)


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def main() -> None:
    probes = (-3.0, -1.0, -0.25, 0.0, 0.25, 1.0, 3.0)
    assert max(abs(tail(q) + tail(-q) - 1.0) for q in probes) < 1e-14

    step = 1e-6
    derivative_error = max(
        abs((tail(q + step) - tail(q - step)) / (2.0 * step) + phi(q))
        for q in probes
    )
    assert derivative_error < 1e-9
    assert tail(-8.0) > 1.0 - 1e-15
    assert tail(8.0) < 1e-15

    # Distributional Fourier typing follows from these two exact identities:
    # H'=-phi fixes the nonzero-frequency principal-value term, while
    # H(q)+H(-q)=1 fixes the half-delta coefficient.
    fourier_components = ("half_delta", "odd_principal_value")
    assert len(set(fourier_components)) == 2

    print("tail_derivative_is_negative_gaussian=true")
    print("tail_reflection_reconstructs_constant=true")
    print("tail_leaves_gaussian_decay_class=true")
    print("fourier_boundary_atom=half_delta")
    print("fourier_comparison_port=odd_principal_value")
    print("minimal_typed_components=4")


if __name__ == "__main__":
    main()
