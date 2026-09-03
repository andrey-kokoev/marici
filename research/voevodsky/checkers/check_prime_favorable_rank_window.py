from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    t, kappa, ell = sp.symbols("t kappa ell", positive=True, real=True)
    k = sp.symbols("k", positive=True, real=True)
    # Sufficient termwise-prime positivity condition with h=kappa*t:
    # ell^2 > 4(4k+2)t(1+k*kappa).
    polynomial = sp.expand(4 * (4 * k + 2) * t * (1 + k * kappa) - ell**2)
    A = 16 * t * kappa
    B = t * (16 + 8 * kappa)
    C = 8 * t - ell**2
    assert sp.expand(polynomial - (A * k**2 + B * k + C)) == 0

    positive_root = sp.simplify((-B + sp.sqrt(B**2 - 4 * A * C)) / (2 * A))
    assert sp.simplify(A * positive_root**2 + B * positive_root + C) == 0

    # Leading small-t scale of the admissible difference order.
    scaled_limit = sp.simplify(sp.limit(sp.sqrt(t) * positive_root, t, 0, dir="+"))
    assert scaled_limit == ell / (4 * sp.sqrt(kappa))

    # Since k=2m+1, the polynomial degree window has half this leading constant.
    m_scaled_limit = sp.simplify(scaled_limit / 2)
    assert m_scaled_limit == ell / (8 * sp.sqrt(kappa))

    result = {
        "schema":"marici.voevodsky.prime-favorable-rank-window-check.v1",
        "status":"rank_window_derived",
        "condition":"(log 2)^2 > 4(4k+2)t(1+k*kappa)",
        "difference_order_scale":"k < (log 2)/(4 sqrt(kappa t)) asymptotically",
        "polynomial_degree_scale":"m < (log 2)/(8 sqrt(kappa t)) asymptotically",
        "termwise_prime_contribution":"nonnegative inside window",
        "full_hankel_positivity":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
