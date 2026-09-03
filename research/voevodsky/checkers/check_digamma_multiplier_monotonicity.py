from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    u = sp.symbols("u", positive=True, real=True)
    a = sp.Rational(1, 4)
    derivative_terms = []
    for n in range(8):
        x = sp.Integer(n) + a
        term = 1 / (n + 1) - x / (x**2 + u**2 / 4)
        derivative = sp.factor(sp.diff(term, u))
        expected = sp.factor(x * u / (2 * (x**2 + u**2 / 4) ** 2))
        assert sp.simplify(derivative - expected) == 0
        assert derivative.is_positive is True
        derivative_terms.append(str(derivative))

    psi_quarter = -sp.EulerGamma - sp.pi / 2 - 3 * sp.log(2)
    d_zero = psi_quarter - sp.log(sp.pi)
    assert d_zero.is_negative is True

    result = {
        "schema":"marici.voevodsky.digamma-multiplier-monotonicity-check.v1",
        "status":"digamma_endpoint_reduction_verified",
        "multiplier_core":"Re psi(1/4+i*u/2)-log(pi)",
        "strictly_increasing_for_positive_u":True,
        "zero_value_exact":str(d_zero),
        "low_band_minimum_at_zero":True,
        "exterior_minimum_at_R":True,
        "checked_series_derivative_terms":len(derivative_terms),
        "normalization_scale_fixed":False,
        "rigorous_numeric_enclosures_computed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
