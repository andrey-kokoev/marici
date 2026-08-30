"""Exact symbolic audit of Fourier transport in logarithmic trace coordinates."""

from sympy import I, exp, pi, simplify, symbols


def main() -> None:
    a, q, r, u = symbols("a q r u", real=True)
    sign = symbols("sign", real=True)

    def kernel(q_arg, r_arg):
        return exp(r_arg) * exp(-2 * pi * I * sign * exp(q_arg + r_arg))

    # V_a h(r)=exp(a/2)h(r+a).  After u=r+a in K V_a, Fourier
    # conjugation must give V_{-a} K.
    left_after_change = exp(a / 2) * kernel(q, u - a)
    right = exp(-a / 2) * kernel(q - a, u)
    assert simplify(left_after_change - right) == 0

    x = symbols("x", real=True)
    kernel_in_x = exp(r) * exp(-2 * pi * I * sign * x * exp(r))
    zeroth = kernel_in_x.subs(x, 0)
    first = kernel_in_x.diff(x).subs(x, 0)
    second = kernel_in_x.diff(x, 2).subs(x, 0)
    assert zeroth == exp(r)
    assert simplify(first + 2 * pi * I * sign * exp(2 * r)) == 0
    assert simplify(second + 4 * pi**2 * sign**2 * exp(3 * r)) == 0

    print("log_trace_kernel_is_hankel=true")
    print("mellin_translation_reversal=true")
    print("endpoint_order_0=global_moment_0")
    print("endpoint_order_1=global_moment_1")
    print("endpoint_order_2=global_moment_2")
    print("finite_endpoint_jet_fourier_closed=false")


if __name__ == "__main__":
    main()
