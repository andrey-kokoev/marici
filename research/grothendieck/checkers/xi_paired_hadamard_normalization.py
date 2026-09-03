"""Exact normalization audit for paired xi zeros and source factors."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    y, x, a, lam, t = sp.symbols("y x a lambda t", positive=True)
    s = sp.Rational(1, 2) + y

    paired_zero = sp.simplify((1 / (y - a) + 1 / (y + a)) / (2 * y))
    assert paired_zero == 1 / (y**2 - a**2)
    assert sp.simplify(paired_zero.subs({y**2: x, a**2: -lam}) - 1 / (x + lam)) == 0

    endpoint = sp.simplify((1 / s + 1 / (s - 1)) / (2 * y))
    assert sp.simplify(endpoint - 1 / (y**2 - sp.Rational(1, 4))) == 0

    q = sp.symbols("q", positive=True)
    basic_laplace = sp.integrate(sp.exp(-q * t), (t, 0, sp.oo))
    assert basic_laplace == 1 / q
    assert sp.simplify(
        sp.exp(-x * t) * sp.exp(t / 4) - sp.exp(-(x - sp.Rational(1, 4)) * t)
    ) == 0
    assert sp.simplify(
        sp.exp(-x * t) * sp.exp(-lam * t) - sp.exp(-(x + lam) * t)
    ) == 0

    result = {
        "schema": "marici.grothendieck.xi-paired-hadamard-normalization.v1",
        "paired_zero_resolvent": "1/(x+lambda_rho)",
        "endpoint_resolvent": "1/(x-1/4)",
        "endpoint_heat": "exp(t/4)",
        "zero_heat": "exp(-t lambda_rho)",
        "functional_pair_counting": "one resolvent term per rho,1-rho pair",
        "passed": True,
    }
    output = Path(__file__).parents[1] / "results" / "xi-paired-hadamard-normalization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
