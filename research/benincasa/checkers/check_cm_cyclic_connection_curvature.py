#!/usr/bin/env python3
"""Audit curvature of the reconstructed cyclic scalar transport candidate."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "results" / "cm-cyclic-connection-reconstruction.json"
POINTS = ((5, 7, 11), (7, 11, 13))


def polynomial(coefficients, monomials, point):
    return sum(
        coefficient * point[0]**i * point[1]**j * point[2]**k
        for coefficient, (i, j, k) in zip(coefficients, monomials)
    )


def derivative(coefficients, monomials, variable, point):
    value = Fraction(0)
    for coefficient, exponents in zip(coefficients, monomials):
        power = exponents[variable]
        if power == 0:
            continue
        shifted = list(exponents)
        shifted[variable] -= 1
        value += (
            coefficient * power
            * point[0]**shifted[0]
            * point[1]**shifted[1]
            * point[2]**shifted[2]
        )
    return value


def denominator(point):
    s1, s2, s3 = point
    triangle = s1*s1+s2*s2+s3*s3-2*(s1*s2+s1*s3+s2*s3)
    return s1*s2*s3*triangle


def denominator_derivative(variable, point):
    s1, s2, s3 = point
    triangle = s1*s1+s2*s2+s3*s3-2*(s1*s2+s1*s3+s2*s3)
    triangle_derivative = 2*(point[variable]-sum(point[index] for index in range(3) if index != variable))
    product = s1*s2*s3
    return product//point[variable]*triangle + product*triangle_derivative


def main():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    monomials = [tuple(value) for value in source["monomial_order"]]
    coefficients = [
        [Fraction(numerator, denominator) for numerator, denominator in direction]
        for direction in source["coefficients_by_direction"]
    ]
    runs = []
    for point in POINTS:
        den = denominator(point)
        curvatures = {}
        for first, second in ((0, 1), (0, 2), (1, 2)):
            n_first = polynomial(coefficients[first], monomials, point)
            n_second = polynomial(coefficients[second], monomials, point)
            numerator = (
                derivative(coefficients[second], monomials, first, point)*den
                - n_second*denominator_derivative(first, point)
                - derivative(coefficients[first], monomials, second, point)*den
                + n_first*denominator_derivative(second, point)
            )
            curvature = numerator/(den*den)
            curvatures[f"F_{first+1}{second+1}"] = [curvature.numerator, curvature.denominator]
        runs.append({"point": list(point), "curvature": curvatures})
    checks = {
        "reconstructed_scalar_candidate_has_nonzero_curvature": all(
            any(numerator != 0 for numerator, denominator in run["curvature"].values())
            for run in runs
        ),
        "curvature_replication_points_agree_in_sign_pattern": (
            [value[0] > 0 for value in runs[0]["curvature"].values()]
            == [value[0] > 0 for value in runs[1]["curvature"].values()]
        ),
    }
    packet = {
        "schema": "marici.cm_cyclic_connection_curvature.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "runs": runs,
        "checks": checks,
        "conclusion": (
            "The pointwise derivative-closure scalar does not define a flat quotient "
            "connection. Preservation of the first-normal denominator was not proved."
        ),
    }
    output = ROOT / "results" / "cm-cyclic-connection-curvature.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
