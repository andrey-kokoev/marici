from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    a = sp.symbols("a", positive=True, real=True)
    q = sp.symbols("q", integer=True, nonnegative=True)
    h = sp.symbols("h", positive=True, real=True)
    z = sp.symbols("z", positive=True, real=True)

    beta_normalization = sp.integrate(z ** (a - 1) * (1 - z) ** q, (z, 0, 1))
    assert sp.simplify(beta_normalization - sp.beta(a, q + 1)) == 0

    # Log moments of Z~Beta(a,q+1), hence R=-log(Z)/h.
    log_partition = sp.log(sp.gamma(a)) + sp.log(sp.gamma(q + 1)) - sp.log(sp.gamma(a + q + 1))
    mean_r = sp.simplify(-sp.diff(log_partition, a) / h)
    expected_mean = (sp.digamma(a + q + 1) - sp.digamma(a)) / h
    assert sp.simplify(mean_r - expected_mean) == 0

    variance_r = sp.simplify(sp.diff(log_partition, a, 2) / h**2)
    expected_variance = (sp.polygamma(1, a) - sp.polygamma(1, a + q + 1)) / h**2
    assert sp.simplify(variance_r - expected_variance) == 0

    result = {
        "schema":"marici.voevodsky.frequency-filter-beta-coherencer-check.v1",
        "status":"beta_pushforward_verified",
        "normalization":"B(t/h,q+1)/h",
        "mean_r":"[psi(t/h+q+1)-psi(t/h)]/h",
        "variance_r":"[psi1(t/h)-psi1(t/h+q+1)]/h^2",
        "fixed_ratio_relative_width":"O(1/log q)",
        "prime_distribution_bound":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
