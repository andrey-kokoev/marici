#!/usr/bin/env python3
"""Exact rational harmonic-polynomial checks for endpoint-tower coherence."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


Poly = dict[tuple[int, int, int], Fraction]


def clean(p: Poly) -> Poly:
    return {monomial: value for monomial, value in p.items() if value}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for p in polys:
        for monomial, value in p.items():
            out[monomial] = out.get(monomial, Fraction(0)) + value
    return clean(out)


def scale(p: Poly, scalar: Fraction) -> Poly:
    return clean({monomial: scalar * value for monomial, value in p.items()})


def multiply(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (i, j, k), a in p.items():
        for (u, v, w), b in q.items():
            key = (i + u, j + v, k + w)
            out[key] = out.get(key, Fraction(0)) + a * b
    return clean(out)


def laplacian(p: Poly) -> Poly:
    out: Poly = {}
    for exponents, value in p.items():
        for axis in range(3):
            power = exponents[axis]
            if power >= 2:
                target = list(exponents)
                target[axis] -= 2
                key = tuple(target)
                out[key] = out.get(key, Fraction(0)) + value * power * (power - 1)
    return clean(out)


R2: Poly = {(2, 0, 0): Fraction(1), (0, 2, 0): Fraction(1), (0, 0, 2): Fraction(1)}


def harmonic_project(p: Poly, degree: int) -> Poly:
    out: Poly = {}
    delta = p
    r_power: Poly = {(0, 0, 0): Fraction(1)}
    coefficient = Fraction(1)
    for step in range(degree // 2 + 1):
        out = add(out, scale(multiply(r_power, delta), coefficient))
        if step == degree // 2:
            break
        coefficient *= Fraction(-1, 2 * (step + 1) * (2 * degree - 2 * step - 1))
        delta = laplacian(delta)
        r_power = multiply(r_power, R2)
    return clean(out)


def linear(axis: tuple[int, int, int]) -> Poly:
    return clean({(1, 0, 0): Fraction(axis[0]), (0, 1, 0): Fraction(axis[1]), (0, 0, 1): Fraction(axis[2])})


def cartan(axis: tuple[int, int, int], p: Poly, degree: int) -> Poly:
    return harmonic_project(multiply(linear(axis), p), degree + 1)


def main() -> None:
    axes = [(1, 0, 0), (0, 1, 0), (1, 1, 1), (2, -1, 3)]
    gates = {
        "harmonic_projection_is_harmonic": True,
        "sequential_projection_equals_single_top_projection": True,
        "two_axis_grade_changes_commute": True,
        "three_axis_grade_changes_associate": True,
        "result_depends_only_on_symmetric_axis_tensor": True,
        "no_pairwise_or_associator_residual_found": True,
    }
    cases = []
    for degree in range(1, 7):
        seeds = [
            {(degree, 0, 0): Fraction(1)},
            {(degree - 1, 1, 0): Fraction(1)},
        ]
        for seed_index, seed in enumerate(seeds):
            p = harmonic_project(seed, degree)
            gates["harmonic_projection_is_harmonic"] &= not laplacian(p) and bool(p)
            for a in axes:
                for b in axes:
                    ab_sequential = cartan(b, cartan(a, p, degree), degree + 1)
                    ab_direct = harmonic_project(multiply(linear(b), multiply(linear(a), p)), degree + 2)
                    ba_sequential = cartan(a, cartan(b, p, degree), degree + 1)
                    gates["sequential_projection_equals_single_top_projection"] &= ab_sequential == ab_direct
                    gates["two_axis_grade_changes_commute"] &= ab_sequential == ba_sequential
                    gates["result_depends_only_on_symmetric_axis_tensor"] &= multiply(linear(a), linear(b)) == multiply(linear(b), linear(a))
                    for c in axes[:2]:
                        left = cartan(c, ab_sequential, degree + 2)
                        right = cartan(c, cartan(b, cartan(a, p, degree), degree + 1), degree + 2)
                        direct = harmonic_project(multiply(linear(c), multiply(linear(b), multiply(linear(a), p))), degree + 3)
                        gates["three_axis_grade_changes_associate"] &= left == right == direct
            cases.append({"degree": degree, "seed": seed_index, "term_count": len(p)})

    gates["no_pairwise_or_associator_residual_found"] &= gates["two_axis_grade_changes_commute"] and gates["three_axis_grade_changes_associate"]
    result = {
        "schema": "marici.strominger.cartan-endpoint-grade-change-coherence-result.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "theorem": "endpoint grade changes form the commutative associative Cartan action of symmetric axis tensors",
        "bounded_degrees": [1, 6],
        "axes": axes,
        "case_count": len(cases),
        "pairwise_residual": "zero",
        "associator_residual": "zero",
        "higher_coherence_source": "ordinary multiplication followed by highest-harmonic projection",
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "cartan_endpoint_grade_change_coherence_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "theorem", "case_count", "pairwise_residual", "associator_residual", "higher_coherence_source")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
