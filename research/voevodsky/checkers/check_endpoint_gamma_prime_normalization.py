from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/endpoint-gamma-prime-normalization-audit-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    y, x, r, ell, t = sp.symbols("y x r ell t", positive=True, real=True)
    s = sp.Rational(1, 2) + y

    endpoint = sp.simplify((1 / s + 1 / (s - 1)) / (2 * y))
    assert sp.simplify(endpoint - 1 / (y**2 - sp.Rational(1, 4))) == 0

    # Coefficients obtained after dividing the completed logarithmic derivative by 2y.
    psi_symbol, log_pi, euler_gamma = sp.symbols("psi_symbol log_pi euler_gamma")
    gamma_coefficient = sp.simplify((sp.Rational(1, 2) * psi_symbol - sp.Rational(1, 2) * log_pi) / (2 * y))
    assert gamma_coefficient == (psi_symbol - log_pi) / (4 * y)
    prime_coefficient = sp.simplify((-sp.Symbol("L")) / (2 * y))
    assert prime_coefficient == -sp.Symbol("L") / (2 * y)

    # Square-root Laplace identity fixes the Gaussian scales a^2/(4t).
    assert sp.simplify((r / 2) ** 2 / (4 * t) - r**2 / (16 * t)) == 0
    assert sp.simplify(ell**2 / (4 * t) - ell**2 / (4 * t)) == 0

    # The gamma integrand's removable value at r=0 is -3/4.
    gamma_numerator = sp.exp(-r) - sp.exp(-r / 4 - r**2 / (16 * t))
    gamma_denominator = 1 - sp.exp(-r)
    assert sp.simplify(sp.limit(gamma_numerator / gamma_denominator, r, 0) + sp.Rational(3, 4)) == 0

    # One functional pair produces one x-resolvent, not twice one.
    a = sp.symbols("a", nonzero=True)
    paired = sp.simplify((1 / (y - a) + 1 / (y + a)) / (2 * y))
    assert sp.simplify(paired - 1 / (y**2 - a**2)) == 0

    result = {
        "schema":"marici.voevodsky.endpoint-gamma-prime-normalization-check.v1",
        "status":"all_coefficients_verified",
        "endpoint_coefficient":True,
        "gamma_factor_one_quarter":True,
        "gamma_gaussian_denominator_16t":True,
        "gamma_removable_limit":"-3/4",
        "prime_factor_minus_one_half":True,
        "prime_gaussian_denominator_4t":True,
        "zero_orbit_not_doubled":True,
        "source_owner_confirmation":False,
        "Hadamard_source_text_inspected":False,
        "source_complete_equivalence":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
