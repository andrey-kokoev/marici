#!/usr/bin/env python3
"""Verify the source Bezout contraction of the marked-pole Koszul complex."""

import json
from itertools import combinations
from pathlib import Path


P = 32003
NAMES = ("K", "g1", "g2", "g3", "g23", "g31")


def clean(poly):
    return {e: c % P for e, c in poly.items() if c % P}


def add_poly(target, source, scale=1):
    result = dict(target)
    for exponent, coefficient in source.items():
        value = (result.get(exponent, 0) + scale * coefficient) % P
        if value: result[exponent] = value
        else: result.pop(exponent, None)
    return result


def scale_poly(poly, scale):
    return clean({e: scale * c for e, c in poly.items()})


def multiply(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            exponent = (i + k, j + l)
            result[exponent] = (result.get(exponent, 0) + a * b) % P
    return clean(result)


def q_packet(x, y, z):
    return {
        "g1": {(0, 1): 1, (0, 0): -y - z},
        "g2": {(1, 0): 1, (0, 0): -x - z},
        "g3": {(1, 0): 1, (0, 1): 1, (0, 0): z},
        "g23": {(0, 1): 1, (0, 0): -x},
        "g31": {(1, 0): 1, (0, 0): -y},
    }


def k_polynomial(x, y, z):
    energy = x + y + z
    x2, y2, z2, c2 = x * x, y * y, z * z, energy * energy
    return clean({
        (4, 0): x2,
        (2, 2): -(x2 + y2 - z2),
        (0, 4): y2,
        (2, 0): x2 * (x2 - y2 - z2) + c2 * (y2 - x2 - z2),
        (0, 2): y2 * (y2 - x2 - z2) + c2 * (x2 - y2 - z2),
        (0, 0): z2 * c2 * c2 + c2 * z2 * (z2 - x2 - y2) + z2 * x2 * y2,
    })


def wedge_sign(index, subset):
    return -1 if sum(existing < index for existing in subset) % 2 else 1


def differential(vector, factors):
    result = {}
    for subset, coefficient in vector.items():
        for position, index in enumerate(subset):
            target = subset[:position] + subset[position + 1:]
            term = scale_poly(
                multiply(factors[index], coefficient),
                -1 if position % 2 else 1,
            )
            result[target] = add_poly(result.get(target, {}), term)
    return {key: value for key, value in result.items() if value}


def homotopy(vector, bezout):
    result = {}
    for subset, coefficient in vector.items():
        for index, value in bezout.items():
            if index in subset: continue
            target = tuple(sorted((*subset, index)))
            term = scale_poly(coefficient, value * wedge_sign(index, subset))
            result[target] = add_poly(result.get(target, {}), term)
    return {key: value for key, value in result.items() if value}


def compose_sum(vector, factors, bezout):
    first = differential(homotopy(vector, bezout), factors)
    second = homotopy(differential(vector, factors), bezout)
    result = dict(first)
    for subset, poly in second.items():
        result[subset] = add_poly(result.get(subset, {}), poly)
        if not result[subset]: result.pop(subset)
    return result


def run(point):
    x, y, z = point
    q = q_packet(x, y, z)
    c1, c2, c3 = x - y - z, y - x - z, x + y + 3 * z
    factors = [k_polynomial(x, y, z)] + [q[name] for name in NAMES[1:]]
    if c1 % P:
        inverse = pow(c1 % P, -1, P)
        bezout = {1: inverse, 4: -inverse % P}
        patch = "x-y-z"
    elif c2 % P:
        inverse = pow(c2 % P, -1, P)
        bezout = {2: inverse, 5: -inverse % P}
        patch = "y-x-z"
    elif c3 % P:
        inverse = pow(c3 % P, -1, P)
        bezout = {3: inverse, 2: -inverse % P, 1: -inverse % P}
        patch = "x+y+3z"
    else:
        return {"point": list(point), "c1": c1, "c2": c2, "c3": c3, "patch": None}

    failures = 0
    tested = 0
    for degree in range(len(NAMES) + 1):
        for subset in combinations(range(len(NAMES)), degree):
            vector = {subset: {(0, 0): 1}}
            result = compose_sum(vector, factors, bezout)
            expected = {subset: {(0, 0): 1}}
            tested += 1
            if result != expected: failures += 1
    return {
        "point": list(point), "c1": c1, "c2": c2, "c3": c3, "patch": patch,
        "exterior_basis_elements_tested": tested,
        "contraction_failures": failures,
    }


def main():
    runs = [run(point) for point in ((2, 3, 4), (5, 2, 3), (2, 2, 0), (0, 0, 0))]
    checks = {
        "generic_patch_contraction_is_identity": runs[0]["contraction_failures"] == 0,
        "signed_wall_switches_to_second_patch": runs[1]["c1"] == 0 and runs[1]["patch"] == "y-x-z" and runs[1]["contraction_failures"] == 0,
        "soft_diagonal_is_contracted_by_third_patch": runs[2]["patch"] == "x+y+3z" and runs[2]["contraction_failures"] == 0,
        "simultaneous_patch_failure_is_all_soft": runs[3]["patch"] is None and runs[3]["point"] == [0, 0, 0],
    }
    result = {
        "schema": "marici.rank26-marked-pole-bezout-contraction.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "identities": {
            "c1": "q_g1-q_g23=x-y-z",
            "c2": "q_g2-q_g31=y-x-z",
            "c3": "q_g3-q_g2-q_g1=x+y+3z",
            "common_zero": "c1=c2=c3=0 iff x=y=z=0",
        },
        "runs": runs,
        "checks": checks,
        "consequence": "the six-factor multiplication Koszul complex is contractible away from the all-soft origin",
    }
    output = Path(__file__).with_name("rank26-marked-pole-bezout-contraction.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__": main()
