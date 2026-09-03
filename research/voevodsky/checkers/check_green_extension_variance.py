from __future__ import annotations

import json


def main() -> None:
    # Scalar block model: cyclic A>0, auxiliary D>0, coupling C.
    a, c, d = 2.0, 0.5, 1.0
    schur = a - c * c / d
    assert schur > 0

    # Projection (x,u)->x forgets the cross pairing c*u against cyclic vectors.
    projection_form_preserving = c == 0.0
    assert not projection_form_preserving

    # Strict Schur loading preserves positivity but does not force a structured projection.
    normalized_return = c * c / (a * d)
    assert normalized_return < 1.0
    assert c != 0.0

    # If a structured retraction is separately supplied, the extension splits.
    retraction_supplied = True
    section_retraction_identity = True
    ordinary_extension_class = "trivial" if retraction_supplied and section_retraction_identity else "unresolved"
    assert ordinary_extension_class == "trivial"

    result = {
        "schema": "marici.voevodsky.green-extension-variance.v1",
        "status": "enlarged_green_extension_is_an_under_embedding_not_an_over_extension",
        "scalar_falsifier": {
            "A": a,
            "C": c,
            "D": d,
            "Schur_effective_A": schur,
            "normalized_return": normalized_return,
            "strict_loading_passes": True,
            "coordinate_projection_preserves_green_form": projection_form_preserving,
        },
        "declared_arrow": "iota:G_cyc->G_full",
        "variance": "under-category",
        "over_extension_gate": "structured projection pi:G_full->G_cyc with kernel G_aux",
        "split_case": "a supplied retraction makes the ordinary extension class trivial",
        "first_obstruction": "no Green-form-preserving projection or pullback-stable kernel sequence",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
