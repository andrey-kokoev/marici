"""Compose the unique six-point loaded lift with eight-point Cut naturality."""

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / "research/nima/checkers"
VOEVODSKY = ROOT / "research/voevodsky"


def main():
    local = json.loads(
        subprocess.check_output(
            [
                sys.executable,
                str(NIMA / "check_tate_loaded_reflection_lift_in_kato_sector.py"),
            ],
            text=True,
        )
    )
    assert local["global_transform_rigid"]
    assert local["mixed_only_homotopy_affine_nullity"] == 0
    assert local["reflection_defect"] == 0

    cut = subprocess.check_output(
        [
            sys.executable,
            str(VOEVODSKY / "check_n8_cut_naturality_after_sheet_transform.py"),
        ],
        text=True,
        cwd=str(VOEVODSKY),
    )
    assert "entry87_PC_homotopy: EXACT_INPUT" in cut
    assert "physical_6x4_cut_orbit: 8" in cut
    assert "transformed_primary_cut_coefficients: +1,+1,+1,+1,+1,+1,+1,+1" in cut
    assert "transformed_nested_crossing_contact_double_residues: ALL_ZERO" in cut
    assert "eight_point_Cut_naturality_fs_Kato: PROVED" in cut

    print(
        json.dumps(
            {
                "status": "proved_scoped_tate_reflection_lift_n8_Cut_naturality",
                "local_loaded_lift_unique": True,
                "physical_cuts": 8,
                "cut_orbit": "one D8 orbit",
                "local_factor": "q4 tensor H6_mark",
                "primary_residue_coefficients": [1] * 8,
                "nested_crossing_contact_double_residues": 0,
                "reflection_defect_after_cut": 0,
                "raw_scheme_statement_claimed": False,
                "conclusion": (
                    "The unique six-point loaded reflection lift is preserved "
                    "on every physical 6x4 Cut of the eight-point PC homotopy "
                    "inside the fs/Kato sector."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
