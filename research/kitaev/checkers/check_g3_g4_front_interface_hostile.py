#!/usr/bin/env python3
"""Finite hostile for differentiated-front G3 versus primitive Green G4.

Dependency-free exact arithmetic.  Passing this checker establishes only that
front-level agreement does not determine a primitive Green form.
"""

from fractions import Fraction
import json
from pathlib import Path


def quadratic(matrix, vector):
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector)))


def matvec(row, vector):
    return sum(row[i] * vector[i] for i in range(len(vector)))


def main():
    # Primitive coordinates (wall/integration constant, differentiated front).
    D = (Fraction(0), Fraction(1))
    G1 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    G2 = ((Fraction(4), Fraction(0)), (Fraction(0), Fraction(1)))

    wall = (Fraction(1), Fraction(0))
    front = (Fraction(0), Fraction(1))
    mixed = (Fraction(1), Fraction(1))

    checks = [
        {
            "name": "same_differentiated_front_map",
            "passed": matvec(D, front) == 1 and matvec(D, wall) == 0,
            "evidence": {"D_front": str(matvec(D, front)), "D_wall": str(matvec(D, wall))},
        },
        {
            "name": "same_front_restricted_green_form",
            "passed": quadratic(G1, front) == quadratic(G2, front) == 1,
            "evidence": {"G1_front": str(quadratic(G1, front)), "G2_front": str(quadratic(G2, front))},
        },
        {
            "name": "primitive_wall_energy_not_determined",
            "passed": quadratic(G1, wall) != quadratic(G2, wall),
            "evidence": {"G1_wall": str(quadratic(G1, wall)), "G2_wall": str(quadratic(G2, wall))},
        },
        {
            "name": "primitive_mixed_state_readback_not_determined",
            "passed": quadratic(G1, mixed) != quadratic(G2, mixed),
            "evidence": {"G1_mixed": str(quadratic(G1, mixed)), "G2_mixed": str(quadratic(G2, mixed))},
        },
    ]

    result = {
        "schema": "marici.kitaev.g3_g4_front_interface_hostile.v1",
        "claim_boundary": "front-level bi-bounded comparison does not determine primitive-window or G4 bulk Green form",
        "checks_passed": sum(c["passed"] for c in checks),
        "checks_total": len(checks),
        "all_passed": all(c["passed"] for c in checks),
        "checks": checks,
        "first_missing_arrow": "source-derived lift or comparison from the primitive ordered-port Green carrier to the differentiated boundary-front seam, retaining the wall/integration-constant sector and proving equality with the G4 cone bulk form",
    }
    out = Path("research/kitaev/results/g3-g4-front-interface-hostile.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
