from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/bernstein-fiber-spread-to-schwarzian-v1.json")
SOURCE = Path("research/grothendieck/theta-bernstein-fiber-spread-deutsch-popper-conjecture.md")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "positive Bernstein measure" in source
    assert "convolution fibers cannot collapse" in source

    mean, variance = sp.symbols("mean variance", positive=True)
    # Laplace tilted moments: f'/f=-mean, f''/f=variance+mean^2.
    curvature = sp.Rational(3, 4) * mean**2 - sp.Rational(1, 2) * (variance + mean**2)
    assert sp.simplify(curvature - (mean**2 - 2 * variance) / 4) == 0

    # For iid T,U and V=T+U:
    # E[V^2]=2 variance+4 mean^2 and Var(V)=2 variance.
    lower_bound = (2 * variance + 4 * mean**2) / 20 + (2 * variance) / 4
    residual = sp.simplify(variance - lower_bound)
    assert residual == sp.Rational(2, 5) * variance - sp.Rational(1, 5) * mean**2
    # residual>=0 is exactly variance>=mean^2/2, hence curvature<=0.
    assert sp.simplify(residual - sp.Rational(2, 5) * (variance - mean**2 / 2)) == 0
    assert sp.simplify(curvature.subs(variance, mean**2 / 2)) == 0

    # Deliberate collapse: a point mass has positive mean and zero variance.
    collapsed_curvature = curvature.subs({mean: 1, variance: 0})
    assert collapsed_curvature == sp.Rational(1, 4) > 0

    status = contract["status"]
    assert status["source_derived_bernstein_measure"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.bernstein-fiber-spread-to-schwarzian-check.v1",
        "status":"fiber_spread_reduction_verified",
        "laplace_curvature_identity":True,
        "total_variance_reduction":True,
        "spread_constant_one_twentieth_sufficient":True,
        "rank_two_schwarzian_consequence":True,
        "collapsed_fiber_deliberate_failure":True,
        "theta_measure_spread_verified":False,
        "all_rank_positivity_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
