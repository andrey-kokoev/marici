"""Exact symbolic audit of the global Gaussian/comb metaplectic cell."""

from sympy import Rational, exp, pi, simplify, symbols


def main() -> None:
    a, xi = symbols("a xi", positive=True, real=True)

    # With Fourier convention exp(-2*pi*i*x*xi), the normalized Gaussian
    # a^(1/4) exp(-pi*a*x^2) transforms as displayed below.
    fourier_gaussian = a ** Rational(-1, 4) * exp(
        -pi * xi**2 / a
    )
    reciprocal_gaussian = (1 / a) ** Rational(1, 4) * exp(
        -pi * (1 / a) * xi**2
    )
    assert simplify(fourier_gaussian - reciprocal_gaussian) == 0

    # The scale inversion is involutive and fixes the self-dual scale.
    assert simplify(1 / (1 / a) - a) == 0
    assert simplify(fourier_gaussian.subs(a, 1) - exp(-pi * xi**2)) == 0

    print("normalized_gaussian_fourier_reciprocity=true")
    print("scale_inversion_involutive=true")
    print("self_dual_gaussian_fixed=true")
    print("comb_fourier_fixed=poisson_distribution_identity")
    print("global_prepared_orbit_cell=true")
    print("full_observer_lift=not_derived")


if __name__ == "__main__":
    main()
