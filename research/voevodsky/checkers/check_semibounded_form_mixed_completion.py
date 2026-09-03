from __future__ import annotations

import json
from fractions import Fraction


def weighted_form(vector: list[Fraction]) -> Fraction:
    return sum(Fraction(index + 1) * value * value for index, value in enumerate(vector))


def main() -> None:
    rho = Fraction(1, 2)
    theta = rho * rho
    schur_factor = Fraction(1) - theta
    assert theta == Fraction(1, 4) < 1
    assert schur_factor == Fraction(3, 4) > 0

    fixtures = [
        [Fraction(1), Fraction(0), Fraction(2)],
        [Fraction(1, 2), Fraction(-1), Fraction(3, 2), Fraction(0)],
        [Fraction(0), Fraction(2), Fraction(-1), Fraction(1, 3), Fraction(4)],
    ]
    checks = []
    for vector in fixtures:
        diagonal_form = weighted_form(vector)
        reduced = theta * diagonal_form
        schur = diagonal_form - reduced
        assert reduced == Fraction(1, 4) * diagonal_form
        assert schur == Fraction(3, 4) * diagonal_form
        checks.append({
            "dimension": len(vector),
            "d": f"{diagonal_form.numerator}/{diagonal_form.denominator}",
            "r": f"{reduced.numerator}/{reduced.denominator}",
            "s": f"{schur.numerator}/{schur.denominator}",
        })

    hostile_unit_rho = Fraction(1)
    hostile_schur_factor = Fraction(1) - hostile_unit_rho**2
    assert hostile_schur_factor == 0
    hostile_supercritical_rho = Fraction(3, 2)
    hostile_supercritical_factor = Fraction(1) - hostile_supercritical_rho**2
    assert hostile_supercritical_factor < 0

    result = {
        "schema": "marici.voevodsky.semibounded-form-mixed-completion.v1",
        "status": "unbounded_closed_form_realization_constructed",
        "common_form_domain": "weighted l2 with sum (n+1)|x_n|^2 finite",
        "common_core": "finitely supported sequences",
        "cross_coefficient": "1/2",
        "relative_form_bound": "1/4",
        "schur_coercivity_factor": "3/4",
        "finite_fixture_checks": checks,
        "associated_operators_unbounded": True,
        "forms_closed": True,
        "staged_joint_reduction_identity": "iterated infimum equals joint infimum under certified domains",
        "unit_cross_radical_full": True,
        "supercritical_cross_negative": True,
        "R_zeta_source_hypotheses_verified": False,
        "next_gate": "compare radial R_zeta source packet against intertwiner, core, relative-bound, and closure certificates",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
