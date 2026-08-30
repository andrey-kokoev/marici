#!/usr/bin/env python3
"""Exact monomial checks for endpoint quadratic-Weyl closure to sp4."""

from fractions import Fraction
import json
from pathlib import Path


def plus(*terms):
    out = {}
    for coefficient, poly in terms:
        for monomial, value in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient * value
            if out[monomial] == 0:
                del out[monomial]
    return out


def e(i, j, poly):
    out = {}
    for powers, coefficient in poly.items():
        target = list(powers)
        target[i] += 1
        target[j] += 1
        target = tuple(target)
        out[target] = out.get(target, 0) + coefficient * Fraction(1, 2)
    return out


def f(i, j, poly):
    out = {}
    for powers, coefficient in poly.items():
        factor = powers[j] * (powers[i] - (1 if i == j else 0))
        if not factor:
            continue
        target = list(powers)
        target[i] -= 1
        target[j] -= 1
        target = tuple(target)
        out[target] = out.get(target, 0) - coefficient * Fraction(factor, 2)
    return out


def h(i, j, poly):
    out = {}
    for powers, coefficient in poly.items():
        if powers[j]:
            target = list(powers)
            target[j] -= 1
            target[i] += 1
            target = tuple(target)
            out[target] = out.get(target, 0) + coefficient * powers[j]
        if i == j:
            out[powers] = out.get(powers, 0) + coefficient * Fraction(1, 2)
    return {key: value for key, value in out.items() if value}


def comm(left, right, poly):
    return plus((1, left(right(poly))), (-1, right(left(poly))))


def d(i, j):
    return Fraction(int(i == j))


def main():
    gates = {
        "generator_count_is_ten": 3 + 3 + 4 == 10,
        "h_h_closure": True,
        "h_e_closure": True,
        "h_f_closure": True,
        "e_f_closure": True,
        "raising_and_lowering_parts_are_abelian": True,
        "horizontal_sl2_and_casimir": True,
        "vertical_sl2_and_casimir": True,
    }

    samples = [
        {(n, total - n): Fraction(1)}
        for total in range(13)
        for n in range(total + 1)
    ]
    pairs = [(0, 0), (0, 1), (1, 1)]

    for poly in samples:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        hij = lambda p, i=i, j=j: h(i, j, p)
                        hkl = lambda p, k=k, l=l: h(k, l, p)
                        eij = lambda p, i=i, j=j: e(i, j, p)
                        ekl = lambda p, k=k, l=l: e(k, l, p)
                        fij = lambda p, i=i, j=j: f(i, j, p)
                        fkl = lambda p, k=k, l=l: f(k, l, p)

                        expected = plus(
                            (d(j, k), h(i, l, poly)),
                            (-d(i, l), h(k, j, poly)),
                        )
                        gates["h_h_closure"] &= comm(hij, hkl, poly) == expected

                        expected = plus(
                            (d(j, k), e(i, l, poly)),
                            (d(j, l), e(i, k, poly)),
                        )
                        gates["h_e_closure"] &= comm(hij, ekl, poly) == expected

                        expected = plus(
                            (-d(i, k), f(j, l, poly)),
                            (-d(i, l), f(j, k, poly)),
                        )
                        gates["h_f_closure"] &= comm(hij, fkl, poly) == expected

                        expected = plus(
                            (d(j, k) * Fraction(1, 4), h(i, l, poly)),
                            (d(i, k) * Fraction(1, 4), h(j, l, poly)),
                            (d(j, l) * Fraction(1, 4), h(i, k, poly)),
                            (d(i, l) * Fraction(1, 4), h(j, k, poly)),
                        )
                        gates["e_f_closure"] &= comm(eij, fkl, poly) == expected

        for i, j in pairs:
            for k, l in pairs:
                eij = lambda p, i=i, j=j: e(i, j, p)
                ekl = lambda p, k=k, l=l: e(k, l, p)
                fij = lambda p, i=i, j=j: f(i, j, p)
                fkl = lambda p, k=k, l=l: f(k, l, p)
                gates["raising_and_lowering_parts_are_abelian"] &= (
                    comm(eij, ekl, poly) == {} and comm(fij, fkl, poly) == {}
                )

        rp = lambda p: h(0, 1, p)
        rm = lambda p: h(1, 0, p)
        r0 = lambda p: plus((1, h(0, 0, p)), (-1, h(1, 1, p)))
        total_degree = sum(next(iter(poly)))
        horizontal_casimir = plus(
            (1, r0(r0(poly))),
            (2, r0(poly)),
            (4, rm(rp(poly))),
        )
        gates["horizontal_sl2_and_casimir"] &= (
            comm(r0, rp, poly) == plus((2, rp(poly)))
            and comm(r0, rm, poly) == plus((-2, rm(poly)))
            and comm(rp, rm, poly) == r0(poly)
            and horizontal_casimir
            == plus((Fraction(total_degree * (total_degree + 2)), poly))
        )

        eu = lambda p: e(0, 0, p)
        fu = lambda p: f(0, 0, p)
        hu = lambda p: h(0, 0, p)
        vertical_casimir = plus(
            (1, hu(hu(poly))),
            (2, hu(poly)),
            (4, fu(eu(poly))),
        )
        gates["vertical_sl2_and_casimir"] &= (
            comm(hu, eu, poly) == plus((2, eu(poly)))
            and comm(hu, fu, poly) == plus((-2, fu(poly)))
            and comm(eu, fu, poly) == hu(poly)
            and vertical_casimir == plus((Fraction(-3, 4), poly))
        )

    result = {
        "schema": "marici.strominger.endpoint-sp4-closure.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_total_degree": 12,
        "lie_algebra": "sp4",
        "dimension": 10,
        "horizontal_casimir": "4l(l+1)",
        "vertical_casimir": "-3/4",
    }
    target = Path(__file__).resolve().parents[1] / "results" / "endpoint_sp4_closure_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

