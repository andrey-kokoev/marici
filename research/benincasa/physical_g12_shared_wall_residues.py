"""Symbolic shared-wall residues of the source-unsplit q_G12 residue form."""

from __future__ import annotations

import json

def main() -> None:
    # These are direct substitutions into affine-linear source walls.  Keep
    # them explicit so this exact provenance checker has no CAS dependency.
    rows = {
        "q_g1": {
            "orientation": "-da",
            "occurrence_sum_numerator": "a + z - x",
            "occurrence_product": "(y + z - x)*(a - y)",
            "other_shared_product": "(a - x - z)*(a + y + 2*z)",
            "generic_numerator_nonzero": True,
        },
        "q_g2": {
            "orientation": "+db",
            "occurrence_sum_numerator": "b + z - y",
            "occurrence_product": "(b - x)*(x + z - y)",
            "other_shared_product": "(b - y - z)*(x + b + 2*z)",
            "generic_numerator_nonzero": True,
        },
        "q_g3": {
            "orientation": "+db",
            "occurrence_sum_numerator": "-x - y - z",
            "occurrence_product": "(b - x)*(-b - z - y)",
            "other_shared_product": "(b - y - z)*(-b - x - 2*z)",
            "generic_numerator_nonzero": True,
        },
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
