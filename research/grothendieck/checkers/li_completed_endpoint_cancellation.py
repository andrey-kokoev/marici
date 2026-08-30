"""Exact endpoint cancellation audit for the completed-zeta logarithmic derivative."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s, t = sp.symbols("s t")

    # Use psi(z)=psi(1+z)-1/z so the removable singularity is cancelled
    # algebraically before asking the CAS for a limit.
    zero_pair = sp.simplify(
        1 / s + (sp.polygamma(0, 1 + s / 2) - 2 / s) / 2
    )
    zero_limit = sp.limit(zero_pair, s, 0)
    assert sp.simplify(zero_limit + sp.EulerGamma / 2) == 0

    gamma1, gamma2 = sp.symbols("gamma_1 gamma_2")
    zeta_laurent = 1 / t + sp.EulerGamma - gamma1 * t + gamma2 * t**2 / 2
    zeta_log_derivative = sp.series(
        sp.diff(zeta_laurent, t) / zeta_laurent, t, 0, 3
    ).removeO()
    one_pair = sp.expand(1 / t + zeta_log_derivative)
    one_limit = sp.limit(one_pair, t, 0)
    assert sp.simplify(one_limit - sp.EulerGamma) == 0

    print("endpoint_0_cancellation=1/s+psi(s/2)/2")
    print("endpoint_0_finite_limit=-EulerGamma/2")
    print("endpoint_1_cancellation=1/(s-1)+zeta_prime_over_zeta")
    print("endpoint_1_finite_limit=EulerGamma")
    print("completed_endpoint_coupling_required=True")
    print("prime_dirichlet_series_valid_at_endpoint=False")


if __name__ == "__main__":
    main()
