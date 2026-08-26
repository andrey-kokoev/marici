"""Directed interval certificate for the first hostile theta cubic gate.

Only the Python standard library is used.  Composite Simpson quadrature is
combined with the already certified interval upper bounds for the fourth
derivatives of u^(2t) Phi(u)/(2t)! on [0, 6].
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from math import factorial

from theta_inner_interval_certificate import I
from theta_moment_fourth_derivative_certificate import phi_derivatives


PANELS = 12000
RIGHT = Decimal(6)
TAIL = Decimal("1e-100")

# Directed bounds printed by theta_moment_fourth_derivative_certificate.py.
# Entries t=2,...,5 bound the Simpson error after division by (2t)!.
NORMALIZED_SIMPSON_ERRORS = {
    2: Decimal("9.488970426228875728652317434e-19"),
    3: Decimal("6.785791514858276807771817418e-21"),
    4: Decimal("3.521670404917476793723542254e-23"),
    5: Decimal("1.400566050139874413357862083e-25"),
}

PRIMITIVE_RAW_SIMPSON_ERRORS = {
    2: Decimal("1.354383940276694194805024757e-13"),
    3: Decimal("6.483304629925451714243393407e-14"),
    4: Decimal("3.825952874725088572684501047e-14"),
    5: Decimal("2.462428024891188106039141770e-14"),
}


def scale_interval(value: I, scalar: Decimal | int) -> I:
    return value * I.point(Decimal(scalar))


def sqrt_interval(value: I) -> I:
    assert value.lo > 0
    with localcontext() as context:
        context.prec = 70
        context.rounding = ROUND_FLOOR
        lo = value.lo.sqrt()
    with localcontext() as context:
        context.prec = 70
        context.rounding = ROUND_CEILING
        hi = value.hi.sqrt()
    return I(lo, hi)


def moments(max_label: int = 10) -> dict[int, I]:
    step = RIGHT / Decimal(PANELS)
    totals = {t: I.point(0) for t in range(2, 6)}
    for index in range(PANELS + 1):
        u = I.point(step * Decimal(index))
        phi = phi_derivatives(
            u,
            max_label=max_label,
            tail=Decimal("1e-100") if max_label == 10 else Decimal(0),
        )[0]
        weight = 1 if index in (0, PANELS) else (4 if index % 2 else 2)
        for t in totals:
            totals[t] = totals[t] + scale_interval(phi * u.power(2 * t), weight)
    factor = I.point(step / Decimal(3))
    enclosed: dict[int, I] = {}
    for t, total in totals.items():
        quadrature = total * factor
        error = (
            NORMALIZED_SIMPSON_ERRORS[t] * Decimal(factorial(2 * t))
            if max_label == 10
            else PRIMITIVE_RAW_SIMPSON_ERRORS[t]
        ) + TAIL
        enclosed[t] = quadrature + I(-error, error)
        assert enclosed[t].lo > 0
    return enclosed


def main() -> None:
    z = moments()
    primitive = moments(max_label=1)
    x3 = z[4] * z[2] / z[3].power(2)
    x4 = z[5] * z[3] / z[4].power(2)
    c3 = I.point(7) - scale_interval(x3, 5)
    c4 = I.point(9) - scale_interval(x4, 7)
    y = sqrt_interval(c3 / I.point(7))

    # The reserve budget has negative sign exactly when this ratio is below 1.
    budget_ratio = (
        scale_interval(I.point(1) + scale_interval(y, 2), 45)
        / (scale_interval((I.point(1) - y) * (I.point(1) + y).power(3), 49))
    )

    secular_gap = c3 * c4 - (
        scale_interval(sqrt_interval(c3), 3)
        - sqrt_interval(scale_interval(c4, 7))
    ).power(2)

    flux_numerator_gap = z[4].power(3) * z[2] - z[5] * z[3].power(3)
    primitive_flux_gap = (
        primitive[4].power(3) * primitive[2]
        - primitive[5] * primitive[3].power(3)
    )
    primitive_to_full_flux_gap_ratio = primitive_flux_gap / flux_numerator_gap

    checks = {
        "positive_moments": all(value.lo > 0 for value in z.values()),
        "physical_reserves": c3.lo > 0 and c4.lo > 0,
        "reserve_below_one": c3.hi < 1,
        "negative_budget_branch": budget_ratio.hi < 1,
        "positive_global_flux": flux_numerator_gap.lo > 0,
        "strict_cubic_lower_gate": secular_gap.lo > 0,
        "primitive_profile_has_positive_flux": primitive_flux_gap.lo > 0,
        "primitive_gap_within_0_01_percent_of_full_gap": primitive_to_full_flux_gap_ratio.lo > Decimal("0.9999"),
    }
    assert all(checks.values())

    def pair(value: I) -> list[str]:
        return [str(value.lo), str(value.hi)]

    print(json.dumps({
        "arithmetic": "70-digit directed Decimal interval arithmetic",
        "quadrature": "12000-panel composite Simpson on [0,6]",
        "theta_label_cutoff": 10,
        "analytic_allowances": {
            "theta_label_tail": "+/-1e-100 inside the derivative enclosure",
            "u_tail": "+/-1e-100 per raw moment",
            "simpson_error_source": "directed fourth-derivative interval enclosure",
        },
        "Z": {str(t): pair(z[t]) for t in z},
        "primitive_Z": {str(t): pair(primitive[t]) for t in primitive},
        "x3": pair(x3),
        "x4": pair(x4),
        "C3": pair(c3),
        "C4": pair(c4),
        "budget_ratio": pair(budget_ratio),
        "flux_numerator_gap": pair(flux_numerator_gap),
        "primitive_flux_gap": pair(primitive_flux_gap),
        "primitive_to_full_flux_gap_ratio": pair(primitive_to_full_flux_gap_ratio),
        "secular_gap": pair(secular_gap),
        "checks": checks,
    }, indent=2))


if __name__ == "__main__":
    main()
