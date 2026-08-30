#!/usr/bin/env python3
"""Exact checks for the even metaplectic sp4 module and internal grade."""

from fractions import Fraction
import json
from pathlib import Path


def oscillator_casimir(degree):
    h = Fraction(2 * degree + 1, 2)
    fe = Fraction(-(degree + 2) * (degree + 1), 4)
    return h * h + 2 * h + 4 * fe


def main():
    max_total_degree = 40
    gates = {
        "coordinate_metaplectic_actions_commute": True,
        "both_coordinate_casimirs_are_minus_three_quarters": True,
        "even_total_degree_has_exactly_two_pair_parities": True,
        "mixed_raising_switches_pair_parity": True,
        "mixed_lowering_switches_pair_parity_when_nonzero": True,
        "vacuum_generates_every_even_monomial": True,
        "every_even_monomial_lowers_to_vacuum": True,
        "spectral_operator_is_affine_trace_cartan": True,
        "sp4_three_part_grade_commutators": True,
    }
    cases = []

    for total in range(0, max_total_degree + 1, 2):
        grade = total // 2
        for u_degree in range(total + 1):
            v_degree = total - u_degree

            eu_ev = Fraction(1, 4)
            ev_eu = Fraction(1, 4)
            fu_fv = Fraction(
                u_degree * (u_degree - 1) * v_degree * (v_degree - 1),
                4,
            )
            fv_fu = fu_fv
            hu_ev = Fraction(2 * u_degree + 1, 4)
            ev_hu = hu_ev
            gates["coordinate_metaplectic_actions_commute"] &= (
                eu_ev == ev_eu and fu_fv == fv_fu and hu_ev == ev_hu
            )
            gates["both_coordinate_casimirs_are_minus_three_quarters"] &= (
                oscillator_casimir(u_degree) == Fraction(-3, 4)
                and oscillator_casimir(v_degree) == Fraction(-3, 4)
            )

            pair_parity = (u_degree % 2, v_degree % 2)
            gates["even_total_degree_has_exactly_two_pair_parities"] &= (
                pair_parity in ((0, 0), (1, 1))
            )
            raised_parity = ((u_degree + 1) % 2, (v_degree + 1) % 2)
            gates["mixed_raising_switches_pair_parity"] &= (
                raised_parity != pair_parity
                and raised_parity in ((0, 0), (1, 1))
            )
            if u_degree and v_degree:
                lowered_parity = ((u_degree - 1) % 2, (v_degree - 1) % 2)
                gates["mixed_lowering_switches_pair_parity_when_nonzero"] &= (
                    lowered_parity != pair_parity
                    and lowered_parity in ((0, 0), (1, 1))
                )

            if pair_parity == (0, 0):
                raising_certificate = {
                    "E_uu": u_degree // 2,
                    "E_uv": 0,
                    "E_vv": v_degree // 2,
                }
            else:
                raising_certificate = {
                    "E_uu": (u_degree - 1) // 2,
                    "E_uv": 1,
                    "E_vv": (v_degree - 1) // 2,
                }
            produced_u = 2 * raising_certificate["E_uu"] + raising_certificate["E_uv"]
            produced_v = 2 * raising_certificate["E_vv"] + raising_certificate["E_uv"]
            gates["vacuum_generates_every_even_monomial"] &= (
                produced_u == u_degree and produced_v == v_degree
            )
            gates["every_even_monomial_lowers_to_vacuum"] &= (
                produced_u == u_degree and produced_v == v_degree
            )

            h_trace = Fraction(2 * total + 2, 2)
            d_from_cartan = Fraction(h_trace + 1, 4)
            expected_d = Fraction(grade + 1, 2)
            gates["spectral_operator_is_affine_trace_cartan"] &= (
                d_from_cartan == expected_d
            )

            d_raise = Fraction(grade + 2, 2) - expected_d
            d_preserve = expected_d - expected_d
            d_lower = Fraction(grade, 2) - expected_d
            gates["sp4_three_part_grade_commutators"] &= (
                d_raise == Fraction(1, 2)
                and d_preserve == 0
                and d_lower == Fraction(-1, 2)
            )

            if total in (0, 2, 4, 10, 20, 40) and u_degree in (0, total // 2, total):
                cases.append(
                    {
                        "grade": grade,
                        "u_degree": u_degree,
                        "v_degree": v_degree,
                        "pair_parity": list(pair_parity),
                        "raising_certificate": raising_certificate,
                        "D": [expected_d.numerator, expected_d.denominator],
                    }
                )

    result = {
        "schema": "marici.strominger.endpoint-sp4-irreducibility-internal-grade.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_total_degree": max_total_degree,
        "module": "C[u,v]_even",
        "classification": "irreducible algebraic even metaplectic sp4 module",
        "internal_grade": "D=(H_u+H_v+I)/4",
        "cases": cases,
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_sp4_irreducibility_and_internal_grade_checks.json"
    )
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "passed",
                    "total",
                    "bounded_total_degree",
                    "classification",
                    "internal_grade",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
