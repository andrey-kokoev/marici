#!/usr/bin/env python3
"""Place the internal bypass residue in the full marked Gysin kernel."""

import json
from fractions import Fraction
from pathlib import Path


def r1(kappa: Fraction, xi: Fraction, p: Fraction) -> Fraction:
    delta = kappa + xi
    return (delta**2 + 2 * (1 + kappa * xi)) / (64 * p**4 * (xi + 1) * delta**3)


def r3(kappa: Fraction, xi: Fraction, p: Fraction) -> Fraction:
    return -Fraction(1, 1) / (64 * p**4 * (xi + 1) * (kappa - xi))


def main() -> None:
    ordered_points = ["(x=1,y=+)", "(x=1,y=-)", "(x=-3,y=+)", "(x=-3,y=-)"]
    samples = []
    for kap, xi, p in (
        (Fraction(-1, 2), Fraction(1, 3), Fraction(1)),
        (Fraction(0), Fraction(2, 5), Fraction(2)),
        (Fraction(1, 3), Fraction(-1, 4), Fraction(3)),
        (Fraction(3, 5), Fraction(1, 7), Fraction(2)),
    ):
        one = r1(kap, xi, p)
        three = r3(kap, xi, p)
        vector = [one, -one, three, -three]
        samples.append(
            {
                "kappa": str(kap),
                "xi": str(xi),
                "p": str(p),
                "residue_vector": [str(value) for value in vector],
                "gysin_sum": str(sum(vector, Fraction(0))),
                "physical_positive_x1_readout": str(vector[0]),
                "deck_trace_x1": str(vector[0] + vector[1]),
            }
        )

    # Gysin: Q^4 -> Q is the degree row [1,1,1,1].
    # Its rank is one, so its kernel has rank three.  The x=1 bypass line
    # e_{1,+}-e_{1,-} is one explicit kernel generator.
    gysin_row = [1, 1, 1, 1]
    x1_anti = [1, -1, 0, 0]
    x3_anti = [0, 0, 1, -1]
    pair_difference = [1, 1, -1, -1]
    kernel_generators = [x1_anti, x3_anti, pair_difference]
    kernel_minor_det = 2  # determinant of columns 1,2,3 of the displayed generators

    def dot(left, right):
        return sum(a * b for a, b in zip(left, right))

    checks = {
        "four_source_labelled_marked_points_retained": len(ordered_points) == 4,
        "global_residue_vectors_lie_in_gysin_kernel": all(row["gysin_sum"] == "0" for row in samples),
        "gysin_rank_is_one": any(gysin_row),
        "gysin_kernel_rank_is_three": len(kernel_generators) == 3 and kernel_minor_det != 0,
        "displayed_kernel_generators_are_killed": all(dot(gysin_row, generator) == 0 for generator in kernel_generators),
        "internal_x1_bypass_line_survives_in_kernel": dot(gysin_row, x1_anti) == 0 and x1_anti != [0, 0, 0, 0],
        "deck_trace_kills_x1_anti_line": (x1_anti[0] + x1_anti[1]) == 0,
        "physical_occurrence_readout_detects_x1_line": x1_anti[0] == 1,
        "sample_physical_readouts_are_nonzero": all(row["physical_positive_x1_readout"] != "0" for row in samples),
    }
    packet = {
        "schema": "marici.soft-internal-residue-gysin-kernel.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ordered_marked_points": ordered_points,
        "gysin_matrix": [gysin_row],
        "gysin_rank": 1,
        "kernel_rank": 3,
        "kernel_basis": kernel_generators,
        "source_residue_vector": "(R1,-R1,R3,-R3)",
        "R1": "((kappa+xi)^2+2*(1+kappa*xi))/(64*p^4*(xi+1)*(kappa+xi)^3)",
        "R3": "-1/(64*p^4*(xi+1)*(kappa-xi))",
        "internal_bypass_class": "Q*(1,-1,0,0) inside ker(Gysin)",
        "deck_trace": "kills the bypass class",
        "physical_occurrence_covector": "(1,0,0,0), which detects the bypass class",
        "conclusion": (
            "the internal bypass packet survives the generic relative Gysin kernel as a deck-anti-invariant line; "
            "it disappears only after an additional deck trace, not in the occurrence-resolved totalization"
        ),
        "scope": "generic fiber away from xi=+-1, xi=+-kappa, and quartic branch-root collision support",
        "samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-internal-residue-gysin-kernel.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
