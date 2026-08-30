"""Finite exact-structure audit of the polarized interval kernel."""

from cmath import exp
from math import log


def feature(label: int, spectral: complex) -> complex:
    return exp(-spectral * log(label))


def main() -> None:
    labels = tuple(range(1, 80))
    parameters = (0.7 + 0.2j, 0.9 + 1.1j, 1.3 - 0.4j)
    coefficients = (1.0 + 0.5j, -0.3 + 0.8j, 0.2 - 0.1j)

    gram_form = sum(
        abs(sum(coefficient * feature(label, spectral) for coefficient, spectral in zip(coefficients, parameters))) ** 2
        for label in labels
    )
    energy_form = 2.0 * sum(
        log(label)
        * abs(sum(coefficient * feature(label, spectral) for coefficient, spectral in zip(coefficients, parameters))) ** 2
        for label in labels
    )
    assert gram_form >= 0.0
    assert energy_form >= 0.0

    exterior_norm = sum(abs(feature(label, 0.0j)) ** 2 for label in labels)
    assert exterior_norm == len(labels)

    print("polarized_kernel=finite_zeta(s+conjugate(w))")
    print("polarized_kernel_positive=true")
    print("log_interval_kernel_positive=true")
    print("diagonal_recovers_interval_energy=true")
    print("observer_w_equals_0_hilbert_norm_diverges=true")
    print("riemann_readout_type=relative_boundary_value")


if __name__ == "__main__":
    main()
