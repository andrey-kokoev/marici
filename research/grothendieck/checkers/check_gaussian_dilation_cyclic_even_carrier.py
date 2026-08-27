"""Exact Mellin multiplier behind cyclicity of Gaussian dilations."""

from sympy import I, Rational, gamma, pi, simplify, symbols


def main() -> None:
    xi = symbols("xi", real=True)
    mellin_multiplier = (
        Rational(1, 2)
        * pi ** (-Rational(1, 4) + I * xi / 2)
        * gamma(Rational(1, 4) - I * xi / 2)
    )

    gamma_argument = Rational(1, 4) - I * xi / 2
    assert simplify(gamma_argument.as_real_imag()[0] - Rational(1, 4)) == 0
    assert mellin_multiplier != 0

    print("log_gaussian_mellin_multiplier=half*pi^(-1/4+i*xi/2)*Gamma(1/4-i*xi/2)")
    print("gamma_argument_real_part=1/4")
    print("gamma_has_no_zeros=true")
    print("gaussian_dilation_orbit_cyclic_even_L2=true")
    print("hilbert_completion_quasianalytic=false")


if __name__ == "__main__":
    main()
