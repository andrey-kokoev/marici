from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/schwartz-density-of-heat-polynomial-tests-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    h, x, u, t = sp.symbols("h x u t", positive=True, real=True)
    phi = (1 - sp.exp(-h * x)) / h
    assert sp.limit(phi, h, 0, dir="+") == x
    assert sp.simplify(sp.series(phi, h, 0, 4).removeO() - (x - h*x**2/2 + h**2*x**3/6 - h**3*x**4/24)) == 0

    checked_orders = 5
    derivative_orders = 4
    for k in range(checked_orders):
        positive_half = sp.exp(-t * u**2 / 2) * ((1 - sp.exp(-h * u**2)) / h) ** (sp.Rational(2*k+1, 2))
        target = sp.exp(-t * u**2 / 2) * u ** (2*k+1)
        assert sp.simplify(sp.limit(positive_half, h, 0, dir="+") - target) == 0
        for derivative_order in range(derivative_orders):
            derivative = sp.diff(positive_half, u, derivative_order)
            target_derivative = sp.diff(target, u, derivative_order)
            assert sp.simplify(sp.limit(derivative, h, 0, dir="+") - target_derivative) == 0

    # Exact inequality 0 <= phi_h(x) <= x follows from 1-exp(-z)<=z; fixture checks its scale split.
    for h_value in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)):
        core_boundary = h_value ** sp.Rational(-1, 4)
        scaled_argument = sp.simplify(h_value * core_boundary**2)
        assert scaled_argument == sp.sqrt(h_value)

    result = {
        "schema":"marici.voevodsky.schwartz-density-heat-polynomials-check.v1",
        "status":"finite_derivative_heat_to_hermite_limits_verified",
        "coordinate_series_order":3,
        "monomial_orders_checked":checked_orders,
        "derivative_orders_checked":derivative_orders,
        "core_scaled_argument":"sqrt(h)",
        "full_Schwartz_seminorm_proof_mechanical":False,
        "odd_Hermite_density_source_attached":False,
        "odd_sector_RH_determining":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
