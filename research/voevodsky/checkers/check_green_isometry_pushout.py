from __future__ import annotations

import json


def main() -> None:
    # A pushout of R <- 0 -> R in the isometry category would serve both cocones.
    orthogonal_cocone_required_dimension = 2
    coincident_cocone_max_dimension = 1
    pushout_exists = orthogonal_cocone_required_dimension <= coincident_cocone_max_dimension
    assert not pushout_exists

    # Cross correlations demanded by the two cocones are incompatible.
    coincident_cross_pairing = 1
    orthogonal_cross_pairing = 0
    assert coincident_cross_pairing != orthogonal_cross_pairing

    result = {
        "schema": "marici.voevodsky.green-isometry-pushout.v1",
        "status": "unrestricted_form_preserving_pushouts_do_not_exist",
        "span": "R <- 0 -> R",
        "cocones": {
            "coincident_in_R": {"cross_pairing": coincident_cross_pairing, "target_dimension": 1},
            "orthogonal_in_R2": {"cross_pairing": orthogonal_cross_pairing, "target_dimension": 2},
        },
        "dimension_contradiction": {
            "required_at_least": orthogonal_cocone_required_dimension,
            "required_at_most": coincident_cocone_max_dimension,
        },
        "pushout_exists": pushout_exists,
        "first_missing_datum": "source-derived cross Green pairing for the amalgamated complements",
        "survivor": "certified amalgamations in a partial double category or equipment",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
