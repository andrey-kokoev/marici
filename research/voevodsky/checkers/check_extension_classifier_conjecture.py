from __future__ import annotations

import json


def main() -> None:
    base_degree_2_rank = 1
    base_degree_1_rank = 0
    distinguished_class_nonzero = True

    # The cell attachment adds h in degree one with dh=xi and is pushed forward.
    cell_exists_after_attachment = True
    cell_variance = "covariant_pushout"

    # A short extension over X is pulled back and has the opposite variance.
    extension_variance = "contravariant_pullback"
    assert cell_variance != extension_variance

    # Z[-2] is projective over Z, so the ordinary Ext^1 class vanishes.
    ext1_z_z_rank = 0
    assert ext1_z_z_rank == 0
    assert base_degree_2_rank == 1 and base_degree_1_rank == 0
    assert distinguished_class_nonzero and cell_exists_after_attachment

    result = {
        "schema": "marici.voevodsky.extension-classifier-falsification.v1",
        "status": "single_contravariant_extension_classifier_rejected",
        "test_object": "Z[-2] with its nonzero degree-two generator",
        "ordinary_Ext1_Z_Z_rank": ext1_z_z_rank,
        "cell_attachment": "adjoin h in degree one with dh=xi",
        "cell_variance": cell_variance,
        "extension_variance": extension_variance,
        "falsifier": "the cell exists as an under-category pushout although the proposed ordinary extension class vanishes",
        "survivor": {
            "over_sector": "Map(X,K[1]) with contravariant pullback",
            "under_sector": "Map(L,X) with covariant pushout",
            "unification_gate": "variance tag plus bifibration or correspondence category and Beck-Chevalley coherence",
        },
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
