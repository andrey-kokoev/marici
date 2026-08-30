"""Separate the all-soft scale from the exceptional soft-triangle period."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    a, p, t, kappa, xi = sp.symbols("a p t kappa xi", nonzero=True)
    k_exc = (
        a**4
        - (10 + 8 * kappa * xi) * p**2 * a**2
        + (16 * kappa**2 + 40 * kappa * xi + 16 * xi**2 + 9) * p**4
    )
    k_dimensionless = (
        t**4
        - (10 + 8 * kappa * xi) * t**2
        + 16 * kappa**2 + 40 * kappa * xi + 16 * xi**2 + 9
    )
    source_rational = (a + p) / (
        2 * p * (a - p) ** 2 * (a + 3 * p) * (xi + 1)
    )
    # da/sqrt(K_exc) contributes p/p^2 on the chosen scale chart.
    dimensionless_source_without_sqrt = sp.factor(
        p**4 * source_rational.subs(a, p * t) / p
    )
    expected = (t + 1) / (2 * (t - 1) ** 2 * (t + 3) * (xi + 1))

    checks = {
        "kernel_has_weight_four": sp.factor(
            k_exc.subs(a, p * t) - p**4 * k_dimensionless
        ) == 0,
        "source_period_has_scale_weight_minus_four": sp.factor(
            dimensionless_source_without_sqrt - expected
        ) == 0,
        "marked_sections_become_constant": (
            sp.factor((a - p).subs(a, p * t) / p - (t - 1)) == 0
            and sp.factor((a + 3 * p).subs(a, p * t) / p - (t + 3)) == 0
        ),
    }
    if not all(checks.values()):
        raise AssertionError({name: value for name, value in checks.items() if not value})

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-scale-separation.v1",
        "scale_coordinate": "p",
        "dimensionless_fiber_coordinate": "t=a/p",
        "kernel": str(k_dimensionless),
        "marked_sections": ["t=1 (double source pole)", "t=-3", "xi=-1"],
        "source_period_scale_factor": "p^-4",
        "dimensionless_source_rational_factor": str(expected),
        "scale_monodromy": "exp(-8*pi*i)=1",
        "scale_classification": "integral rank-one Tate/Kummer factor supported at existing all-soft p=0",
        "checks": checks,
        "status": "all_soft_scale_separates_as_integral_rank_one_factor",
        "scope": (
            "homogeneity and local scale character only; the all-soft extension, "
            "integral normalization, and dimensionless relative cohomology remain uncomputed"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
