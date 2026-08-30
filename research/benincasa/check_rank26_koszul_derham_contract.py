#!/usr/bin/env python3
"""Verify the source identities defining the Koszul--de Rham bicomplex."""

import contextlib
import importlib
import io
import json
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    moving = importlib.import_module("check_rank26_moving_relation_coherence")

base, charts, words = moving.base, moving.charts, moving.words
P = base.PRIME


def clean(poly):
    return {e: c % P for e, c in poly.items() if c % P}


def add(left, right, scale=1):
    result = dict(left)
    for exponent, coefficient in right.items():
        value = (result.get(exponent, 0) + scale * coefficient) % P
        if value: result[exponent] = value
        else: result.pop(exponent, None)
    return result


def multiply(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            exponent = (i + k, j + l)
            result[exponent] = (result.get(exponent, 0) + a * b) % P
    return clean(result)


def derivative(poly, axis):
    result = {}
    for exponent, coefficient in poly.items():
        power = exponent[axis]
        if not power: continue
        shifted = list(exponent); shifted[axis] -= 1
        result[tuple(shifted)] = coefficient * power % P
    return clean(result)


def main():
    point = words.REFERENCE_POINT
    k, q_packet = base.fiber_data(*point)
    factors = [("K", k)] + [(name, q_packet[name]) for name in charts.SOURCE_NAMES]
    probes = [{exponent: 1} for exponent in base.monomials_at_most(5)]

    leibniz_failures = 0
    mixed_partial_failures = 0
    multiplication_failures = 0
    leibniz_tests = 0
    mixed_partial_tests = 0
    multiplication_tests = 0
    for _, factor in factors:
        for probe in probes:
            product_poly = multiply(factor, probe)
            for axis in range(2):
                lhs = derivative(product_poly, axis)
                rhs = add(
                    multiply(derivative(factor, axis), probe),
                    multiply(factor, derivative(probe, axis)),
                )
                leibniz_tests += 1
                if clean(add(lhs, rhs, -1)): leibniz_failures += 1
            route_ab = derivative(derivative(product_poly, 0), 1)
            route_ba = derivative(derivative(product_poly, 1), 0)
            mixed_partial_tests += 1
            if clean(add(route_ab, route_ba, -1)): mixed_partial_failures += 1

    for _, first in factors:
        for _, second in factors:
            for probe in probes:
                route_one = multiply(first, multiply(second, probe))
                route_two = multiply(second, multiply(first, probe))
                multiplication_tests += 1
                if clean(add(route_one, route_two, -1)): multiplication_failures += 1

    checks = {
        "multiplication_routes_commute": multiplication_failures == 0,
        "fiber_derivatives_obey_leibniz": leibniz_failures == 0,
        "fiber_derivatives_commute": mixed_partial_failures == 0,
    }
    result = {
        "schema": "marici.rank26-koszul-derham-contract.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "point": list(point),
        "source_factors": [name for name, _ in factors],
        "probe_monomials": len(probes),
        "test_counts": {
            "multiplication_commutators": multiplication_tests,
            "leibniz_squares": leibniz_tests,
            "mixed_partial_squares": mixed_partial_tests,
        },
        "failure_counts": {
            "multiplication": multiplication_failures,
            "leibniz": leibniz_failures,
            "mixed_partial": mixed_partial_failures,
        },
        "checks": checks,
        "finite_exactness_prediction": (
            "test exactness only in fixed numerator grades separated from "
            "the ambient cutoff by the maximal K shift; absolute finite "
            "homology may live on the truncation boundary"
        ),
    }
    output = Path(__file__).with_name("rank26-koszul-derham-contract.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__": main()
