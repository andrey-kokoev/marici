"""Exact Mellin transform of the symmetric principal-part transport kernels."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t, s = sp.symbols("t s", positive=True)

    for k in range(1, 9):
        factorial = sp.factorial(k - 1)
        # x=e^{-t} on (0,1) and x=e^t on (1,infinity).
        lower = sp.integrate(t ** (k - 1) * sp.exp(-s * t) / factorial, (t, 0, sp.oo))
        upper_parameter = sp.symbols("a", positive=True)
        upper = sp.integrate(
            t ** (k - 1) * sp.exp(-upper_parameter * t) / factorial,
            (t, 0, sp.oo),
        )
        assert sp.simplify(lower - s ** (-k)) == 0
        assert sp.simplify(upper - upper_parameter ** (-k)) == 0
        print(
            f"k={k} lower_mellin=s^-{k} "
            f"upper_mellin=(1-s)^-{k}"
        )

    print("physical_kernel_lower=(-log(x))^(k-1)/(k-1)!")
    print("physical_kernel_upper=x^-1*(log(x))^(k-1)/(k-1)!")
    print("reflection_relation=Phi(1/x)=x*Phi(x)")
    print("raw_prime_sum_absolutely_convergent=False")


if __name__ == "__main__":
    main()
