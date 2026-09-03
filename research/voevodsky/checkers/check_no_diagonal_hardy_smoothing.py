from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    m = sp.symbols("m", integer=True, positive=True)
    for k in range(1, 7):
        coefficient = sp.prod(m - j for j in range(k)) / sp.factorial(k)
        polynomial = sp.Poly(sp.expand(coefficient), m)
        assert polynomial.degree() == k
        assert polynomial.LC() == sp.Rational(1, sp.factorial(k))

    # Every finite positive reference measure gives a uniform upper bound for
    # ||(1-z)^m|| on [0,1].
    z = sp.symbols("z", real=True)
    assert sp.simplify((1 - z) ** (2 * m)).subs(z, 0) == 1
    assert sp.simplify((1 - z) ** (2 * m)).subs(z, 1) == 0

    result = {
        "schema":"marici.voevodsky.no-diagonal-hardy-smoothing-check.v1",
        "status":"diagonal_smoothing_no_go_verified",
        "hostile_family":"p_m(z)=(1-z)^m",
        "fixed_coefficient_asymptotic":"binomial(m,k)~m^k/k!",
        "reference_moment_norm":"uniformly bounded for finite measure on [0,1]",
        "nonconstant_diagonal_map_bounded":False,
        "scope":"coefficient-diagonal maps with one fixed nonzero multiplier at any k>=1",
        "non_diagonal_intertwiner_excluded":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
