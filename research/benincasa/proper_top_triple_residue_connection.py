"""Verify the proper-top scalar connection against the triple-residue line."""

from __future__ import annotations

import json


PRIME = 32003
GAMMA = 5
OBSERVATIONS = (
    ((2, 3, 4), (14226, 24891), False),
    ((3, 5, 6), (30862, 14858), False),
    ((2, 4, 8364), (31322, 31384), True),
    ((2, 5, 12859), (24477, 10292), True),
    ((2, 8, 6068), (6296, 7394), True),
)


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def predicted_connection(x: int, y: int, z: int) -> tuple[int, int]:
    energy = x + y + z
    ell_minus = -x + y + z
    ell_plus = x - y + z
    scale = 2 * GAMMA
    return (
        scale * (inverse(energy) - inverse(ell_minus) + inverse(ell_plus)) % PRIME,
        scale * (inverse(energy) + inverse(ell_minus) - inverse(ell_plus)) % PRIME,
    )


def main() -> None:
    rows = []
    for point, observed, on_quartic in OBSERVATIONS:
        predicted = predicted_connection(*point)
        rows.append(
            {
                "kinematics": point,
                "on_generic_quartic_zero_fiber": on_quartic,
                "observed": observed,
                "predicted": predicted,
                "matches": predicted == observed,
            }
        )
    result = {
        "schema": "marici.benincasa.proper-top-triple-residue-connection.v1",
        "prime": PRIME,
        "gamma": GAMMA,
        "triple_residue_factor": "F=E*(-x+y+z)*(x-y+z)",
        "restricted_cayley_menger": "K(P)=F^2",
        "predicted_connection": "2*gamma*dlog(F)",
        "fibers": rows,
        "all_directional_comparisons_match": all(row["matches"] for row in rows),
        "directional_comparisons": 2 * len(rows),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
