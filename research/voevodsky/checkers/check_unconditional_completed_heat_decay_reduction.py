from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/unconditional-completed-heat-decay-reduction-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    beta, gamma = sp.symbols("beta gamma", real=True)
    rho = beta + sp.I * gamma
    lam = sp.expand(-(rho - sp.Rational(1, 2)) ** 2)
    assert sp.simplify(sp.re(lam) - (gamma**2 - (beta - sp.Rational(1, 2)) ** 2)) == 0

    # Rational off-critical zeros still have positive heat rate under the ordinate gap.
    fixtures = [
        (sp.Rational(1, 3), sp.Rational(3, 2)),
        (sp.Rational(2, 3), sp.Rational(5, 2)),
        (sp.Rational(1, 2), sp.Rational(7, 2)),
    ]
    rates = [sp.simplify(g**2 - (b - sp.Rational(1, 2)) ** 2) for b, g in fixtures]
    assert all(rate > 0 for rate in rates)
    assert all(rate >= g**2 - sp.Rational(1, 4) for rate, (_, g) in zip(rates, fixtures))

    # Exact endpoint/remainder sampled identity on a decaying finite heat sum.
    t, h = sp.symbols("t h", positive=True, real=True)
    n = sp.symbols("n", integer=True, nonnegative=True)
    Y = sp.exp(h / 4)
    s = t + n * h
    H = sum(sp.exp(-rate * s) for rate in rates)
    endpoint = sp.exp(s / 4)
    H_R = H - endpoint
    a_n = sp.simplify(H_R - H_R.subs(n, n + 1))
    c = sp.exp(t / 4) * (Y - 1)
    residual = sp.simplify(Y ** (-n) * (H - H.subs(n, n + 1)))
    assert sp.simplify(a_n / Y**n - c - residual) == 0

    # Each residual term decays geometrically because rate+h-shift is positive.
    residual_terms = [sp.exp(-rate * t) * (1 - sp.exp(-rate * h)) * sp.exp(-n * h * (rate + sp.Rational(1, 4))) for rate in rates]
    assert sp.simplify(residual - sum(residual_terms)) == 0
    assert all(rate + sp.Rational(1, 4) > 0 for rate in rates)

    result = {
        "schema":"marici.voevodsky.unconditional-completed-heat-decay-reduction-check.v1",
        "status":"decay_to_endpoint_asymptotic_bridge_verified",
        "spectral_real_part_identity":True,
        "off_critical_positive_rate_fixtures":len(fixtures),
        "moment_asymptotic_identity":True,
        "finite_heat_residual_decay":True,
        "source_citations_attached":False,
        "exact_general_complex_zero_heat_formula_verified":False,
        "remainder_hankel_PSD":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
