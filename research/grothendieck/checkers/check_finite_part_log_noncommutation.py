"""Dependency-free witness that finite part and logarithm do not commute."""

from math import log


def main() -> None:
    finite_scalar = 3.0
    epsilons = (1e-2, 1e-4, 1e-8)

    # Toy source asymptotic Z_e = e^(-1/4) + finite_scalar.
    # Subtracting the boundary gives the finite scalar exactly. Subtracting
    # the divergent part of log Z_e instead gives zero in the limit.
    logarithmic_remainders = []
    for epsilon in epsilons:
        boundary = epsilon ** (-0.25)
        regulated = boundary + finite_scalar
        assert abs((regulated - boundary) - finite_scalar) < 1e-12
        logarithmic_remainders.append(log(regulated) - log(boundary))

    assert logarithmic_remainders[-1] < logarithmic_remainders[0]
    assert logarithmic_remainders[-1] < 0.04
    assert abs(log(finite_scalar)) > 1.0

    print("scalar_finite_part=finite_scalar")
    print("logarithmic_finite_part=boundary_normalization")
    print("finite_part_commutes_with_log=false")
    print("typed_prime_lift_from_scalar_detector=false")
    print("next_gate=scale_valuation_beck_chevalley_square")


if __name__ == "__main__":
    main()
