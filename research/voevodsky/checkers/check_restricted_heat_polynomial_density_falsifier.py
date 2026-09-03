from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/restricted-heat-polynomial-density-falsifier-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    h, u, t = sp.symbols("h u t", positive=True, real=True)
    qh = sp.sqrt(1 - sp.exp(-h * u**2))
    assert sp.limit(qh / sp.sqrt(h), h, 0, dir="+") == u

    checked_orders = 5
    for k in range(checked_orders):
        finite_difference = (1 - sp.exp(-h * u**2)) ** k / h**k
        assert sp.simplify(sp.limit(finite_difference, h, 0, dir="+") - u ** (2 * k)) == 0
        scaled_test = sp.exp(-t * u**2 / 2) * qh * finite_difference / sp.sqrt(h)
        target = sp.exp(-t * u**2 / 2) * u ** (2 * k + 1)
        assert sp.simplify(sp.limit(scaled_test, h, 0, dir="+") - target) == 0

    # The first correction is controlled on compact u sets and retains Gaussian decay.
    expansion = sp.series(qh / sp.sqrt(h), h, 0, 3).removeO()
    assert sp.simplify(expansion.coeff(h, 0) - u) == 0
    assert sp.simplify(expansion.coeff(h, 1) + u**3 / 4) == 0

    result = {
        "schema":"marici.voevodsky.restricted-heat-polynomial-density-falsifier-check.v1",
        "status":"odd_gaussian_limit_family_verified",
        "qh_scaled_limit":True,
        "finite_difference_orders_checked":checked_orders,
        "combined_odd_gaussian_limits":True,
        "first_correction":"-u^3/4",
        "Schwartz_seminorm_convergence":False,
        "odd_Hermite_weil_determining":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
