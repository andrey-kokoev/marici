#!/usr/bin/env python3
"""Test whether total-energy deformation canonically determines the transverse N2 grade."""

import json
from pathlib import Path

import sympy as sp


tau = sp.symbols("tau")
x1, x2, x3 = sp.symbols("x1 x2 x3", nonzero=True)
a1, a2, a3 = sp.symbols("a1 a2 a3")
xs = (x1, x2, x3)
alphas = (a1, a2, a3)


def coeff2(expression):
    return sp.expand(expression).coeff(tau, 2)


def quadratic_packet(alpha_values):
    nus = [sp.expand((x + a * tau) ** 2 - x**2) for x, a in zip(xs, alpha_values)]
    labels = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
    return [sp.factor(coeff2(nus[i] * nus[j])) for i, j in labels]


def specialize(vector, background):
    substitution = dict(zip(xs, background))
    return [int(sp.expand(value).subs(substitution)) for value in vector]


def quotient_coordinate(quadratic_vector, kernel, prime):
    # Columns 0..2 are first normals and column 3 is nu1^2.  Kernel row r
    # expresses trailing column 4+r in terms of the first four columns.
    coordinate = quadratic_vector[0]
    for trailing_index, value in enumerate(quadratic_vector[1:]):
        coordinate -= kernel[trailing_index][3] * value
    return coordinate % prime


def main():
    diagonal = quadratic_packet((0, 0, 0))
    generic = quadratic_packet(alphas)
    expected = [
        4 * a1**2 * x1**2,
        4 * a2**2 * x2**2,
        4 * a3**2 * x3**2,
        4 * a1 * a2 * x1 * x2,
        4 * a1 * a3 * x1 * x3,
        4 * a2 * a3 * x2 * x3,
    ]
    backgrounds = {
        "A": (2, 3, 4),
        "B": (3, 5, 6),
        "HOMA": (2, 3, 4),
        "SOFT1": (0, 3, 4),
    }
    rank_packet = json.loads(
        (Path(__file__).resolve().parent.parent / "results" / "cm-normal-tower-rank.json").read_text(encoding="utf-8")
    )
    rank_runs = {run["point"]: run for run in rank_packet["runs"]}
    witnesses = {}
    for name, point in backgrounds.items():
        lift = (1, 0, 0) if point[0] != 0 else (0, 1, 0)
        diagonal_vector = specialize(diagonal, point)
        transverse_vector = specialize(quadratic_packet(lift), point)
        rank_run = rank_runs[name]
        witnesses[name] = {
            "diagonal_lift": diagonal_vector,
            "transverse_lift": transverse_vector,
            "lift_parameters": list(lift),
            "prime": rank_run["prime"],
            "diagonal_quotient_coordinate": quotient_coordinate(
                diagonal_vector, rank_run["kernel"], rank_run["prime"]
            ),
            "transverse_quotient_coordinate": quotient_coordinate(
                transverse_vector, rank_run["kernel"], rank_run["prime"]
            ),
        }
    checks = {
        "physical_diagonal_pullback_zero": diagonal == [0] * 6,
        "generic_lift_formula_exact": all(sp.expand(a - b) == 0 for a, b in zip(generic, expected)),
        "every_background_has_nonzero_lift_ambiguity": all(
            witness["diagonal_lift"] != witness["transverse_lift"]
            for witness in witnesses.values()
        ),
        "ambiguity_survives_quadratic_quotient": all(
            witness["diagonal_quotient_coordinate"] == 0
            and witness["transverse_quotient_coordinate"] != 0
            for witness in witnesses.values()
        ),
        # Deliberate-failure witness: lift independence must fail.
        "deliberate_lift_independence_obstruction_nonzero": any(
            any(value != 0 for value in witness["transverse_lift"])
            for witness in witnesses.values()
        ),
    }
    packet = {
        "schema": "marici.total_energy_quadratic_quotient_typing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "normal_coordinates": "nu_i=P_i^2-X_i^2",
        "homogeneous_locus": "P_i=X_i, hence nu_i=0 identically",
        "generic_transverse_lift": "P_i=X_i+alpha_i*tau",
        "quadratic_tau2_coefficients": [str(value) for value in generic],
        "background_witnesses": witnesses,
        "checks": checks,
        "classification": "untyped_reverse_map_with_canonical_zero_pullback",
        "conclusion": (
            "Ordinary source pullback sends every positive nu-grade to zero on the "
            "homogeneous family. A reverse map from the total-energy second grade to "
            "the transverse quadratic quotient depends on arbitrary lift parameters "
            "alpha_i and therefore does not descend without an independently derived splitting."
        ),
    }
    output = Path(__file__).resolve().parent.parent / "results" / "total-energy-quadratic-quotient-typing.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "classification": packet["classification"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
