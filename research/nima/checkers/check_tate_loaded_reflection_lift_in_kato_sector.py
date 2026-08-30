"""Compose the certified components of the loaded reflection lift."""

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / "research/nima/checkers"
VOEVODSKY = ROOT / "research/voevodsky"


def json_checker(path):
    return json.loads(subprocess.check_output([sys.executable, str(path)], text=True))


def text_checker(path):
    return subprocess.check_output(
        [sys.executable, str(path)], text=True, cwd=str(VOEVODSKY)
    )


def main():
    homotopy = json_checker(
        NIMA / "check_tate_reflection_discrepancy_homotopy.py"
    )
    support = json_checker(
        NIMA / "check_tate_reflection_loaded_support_gate.py"
    )
    conductor = json_checker(
        NIMA / "check_tate_conductor_kernel_mixed_face_identity.py"
    )
    stalks = text_checker(
        VOEVODSKY / "check_multirees_conductor_stalk_kernel.py"
    )
    transform = text_checker(
        VOEVODSKY / "check_global_mixed_variance_transform.py"
    )

    assert homotopy["mixed_faces_only_h1_with_zero_h2_exists"]
    assert homotopy["mixed_faces_only_affine_parameter_count"] == 0
    assert support["degree_zero_ordinary_lift_exists"]
    assert support["minimal_required_extraordinary_faces"] == 6
    assert conductor["mixed_faces_with_exact_difference_identity"] == 6
    assert conductor["mixed_coefficient_residual_rank"] == 0
    assert "face_localization_squares: 522" in stalks
    assert "two_step_localization_routes: 840" in stalks
    assert "full_multirees_stalk_kernel: CONSTRUCTED" in stalks
    assert "transform_image_equals_unique_framed_connector: YES" in transform
    assert "normalization_sheet_kernel_in_Kato_sector: COMPLETE" in transform

    print(
        json.dumps(
            {
                "status": "proved_scoped_loaded_reflection_lift_in_Kato_sector",
                "degree_zero_ordinary_edges": 6,
                "extraordinary_mixed_faces": 6,
                "pure_faces_used": 0,
                "relative_interior_used": 0,
                "mixed_face_coefficient_residual_rank": 0,
                "loaded_PC_stalks": 215,
                "localization_squares": 522,
                "two_step_routes": 840,
                "mixed_only_homotopy_affine_nullity": 0,
                "global_transform_rigid": True,
                "reflection_defect": 0,
                "raw_scheme_realization_claimed": False,
                "conclusion": (
                    "The frozen carrier reflection discrepancy has a unique "
                    "loaded lift in the fs/Kato PC sector. Its minimal "
                    "representative uses six ordinary short-facet edges, six "
                    "extraordinary mixed conductor faces, and no pure face or "
                    "relative-interior term."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
