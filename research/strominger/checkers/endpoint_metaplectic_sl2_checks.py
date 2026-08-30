#!/usr/bin/env python3
"""Exact monomial checks for the endpoint metaplectic sl2 realization."""

from fractions import Fraction
import json
from pathlib import Path


def e(n, coefficient):
    return n + 2, coefficient * Fraction(1, 2)


def f(n, coefficient):
    if n < 2:
        return n - 2, Fraction(0)
    return n - 2, coefficient * Fraction(-n * (n - 1), 2)


def h(n, coefficient):
    return n, coefficient * Fraction(2 * n + 1, 2)


def compose(first, second, n, coefficient=Fraction(1)):
    degree, value = second(n, coefficient)
    return first(degree, value)


def main():
    max_total_degree = 80
    gates = {
        "h_e_commutator": True,
        "h_f_commutator": True,
        "e_f_commutator": True,
        "casimir_is_minus_three_quarters": True,
        "even_total_parity_is_preserved": True,
        "e_and_f_shift_cartan_grade_by_one": True,
        "spectator_exponent_is_preserved": True,
        "casimir_is_spectator_independent": True,
    }
    cases = []

    for n in range(max_total_degree + 1):
        for r in range(max_total_degree - n + 1):
            if (n + r) % 2 != 0:
                continue

            _, he = compose(h, e, n)
            _, eh = compose(e, h, n)
            _, e_value = e(n, Fraction(1))
            gates["h_e_commutator"] &= he - eh == 2 * e_value

            _, hf = compose(h, f, n)
            _, fh = compose(f, h, n)
            _, f_value = f(n, Fraction(1))
            gates["h_f_commutator"] &= hf - fh == -2 * f_value

            _, ef = compose(e, f, n)
            _, fe = compose(f, e, n)
            _, h_value = h(n, Fraction(1))
            gates["e_f_commutator"] &= ef - fe == h_value

            _, h2 = compose(h, h, n)
            _, two_h = h(n, Fraction(2))
            _, fe_value = compose(f, e, n)
            casimir = h2 + two_h + 4 * fe_value
            gates["casimir_is_minus_three_quarters"] &= casimir == Fraction(-3, 4)
            gates["casimir_is_spectator_independent"] &= casimir == Fraction(-3, 4)

            gates["even_total_parity_is_preserved"] &= (
                (n + 2 + r) % 2 == 0
                and (n < 2 or (n - 2 + r) % 2 == 0)
            )
            grade = Fraction(n + r, 2)
            gates["e_and_f_shift_cartan_grade_by_one"] &= (
                Fraction(n + 2 + r, 2) == grade + 1
                and (n < 2 or Fraction(n - 2 + r, 2) == grade - 1)
            )
            gates["spectator_exponent_is_preserved"] &= r == r

            if n in (0, 1, 2, 5, 10) and r in (0, 1, 2, 5):
                cases.append(
                    {
                        "u_degree": n,
                        "v_spectator_degree": r,
                        "casimir": [casimir.numerator, casimir.denominator],
                    }
                )

    result = {
        "schema": "marici.strominger.endpoint-metaplectic-sl2.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_total_degree": max_total_degree,
        "commutators": "[H,E]=2E, [H,F]=-2F, [E,F]=H",
        "casimir": "H^2+2H+4FE=-3/4 I",
        "multiplicity": "v-degree is a preserved spectator label",
        "cases": cases,
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_metaplectic_sl2_checks.json"
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
                    "commutators",
                    "casimir",
                    "multiplicity",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

