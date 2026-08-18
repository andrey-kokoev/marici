"""Symbolic shared-wall residues of the source-unsplit q_G12 residue form."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    a, b, x, y, z = sp.symbols("a b x y z")
    q = {
        "q_g1": b - y - z,
        "q_g2": a - x - z,
        "q_g3": a + b + z,
        "q_g23": b - x,
        "q_g31": a - y,
    }
    walls = {
        "q_g1": ({b: y + z}, "-da", ("q_g2", "q_g3")),
        "q_g2": ({a: x + z}, "+db", ("q_g1", "q_g3")),
        "q_g3": ({a: -b - z}, "+db", ("q_g1", "q_g2")),
    }
    rows = {}
    for wall, (substitution, orientation, shared_remaining) in walls.items():
        occurrence_numerator = sp.factor((q["q_g23"] + q["q_g31"]).subs(substitution))
        occurrence_denominator = sp.factor((q["q_g23"] * q["q_g31"]).subs(substitution))
        remaining_denominator = sp.factor(
            sp.prod(q[name] for name in shared_remaining).subs(substitution)
        )
        rows[wall] = {
            "orientation": orientation,
            "occurrence_sum_numerator": str(occurrence_numerator),
            "occurrence_product": str(occurrence_denominator),
            "other_shared_product": str(remaining_denominator),
            "generic_numerator_nonzero": occurrence_numerator != 0,
        }
    result = {
        "schema": "marici.benincasa.physical-g12-shared-wall-residues.v1",
        "surface_form": "da wedge db / (sqrt(K_E)*q_g1*q_g2*q_g3) * (1/q_g23+1/q_g31)",
        "walls": rows,
        "all_form_level_residues_generically_nonzero": all(
            row["generic_numerator_nonzero"] for row in rows.values()
        ),
        "cohomological_nonvanishing_inferred": False,
        "remaining_test": "normalization/conductor reduction of each wall one-form and their Cech sum",
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
