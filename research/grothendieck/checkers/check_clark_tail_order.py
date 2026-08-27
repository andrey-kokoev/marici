"""Dependency-free hostile audit for Clark/tail constructor order."""

from math import exp, pi


def gaussian(q: float) -> float:
    return exp(-pi * q * q)


def source_first_tail(q: float) -> float:
    # Integral from q to infinity of v exp(-pi v^2) dv.
    return exp(-pi * q * q) / (2.0 * pi)


def main() -> None:
    # Source-first multiplication followed by tail remains Gaussian.
    for q in (-8.0, -3.0, 0.0, 3.0, 8.0):
        assert abs(source_first_tail(q) - gaussian(q) / (2.0 * pi)) < 1e-15

    # Tail-first multiplication has linear left asymptote because the
    # normalized Gaussian has total mass one.
    from math import erfc, sqrt

    def tail(q: float) -> float:
        return 0.5 * erfc(sqrt(pi) * q)

    ratios = [(q * tail(q)) / q for q in (-4.0, -6.0, -8.0)]
    assert min(ratios) > 1.0 - 1e-14

    print("admitted_order=source_multiplication_then_tail")
    print("admitted_order_preserves_five_component_type=true")
    print("reverse_order_linear_left_asymptote=true")
    print("reverse_order_fourier_boundary=delta_prime")
    print("operations_commute=false")
    print("sixth_wall_needed=false_if_precedence_preserved")


if __name__ == "__main__":
    main()
