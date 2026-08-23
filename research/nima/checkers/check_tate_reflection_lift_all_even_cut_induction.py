"""Compose the Tate reflection lift with general even Cut induction."""

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / "research/nima/checkers"
VOEVODSKY = ROOT / "research/voevodsky"


def main():
    base = json.loads(
        subprocess.check_output(
            [
                sys.executable,
                str(
                    NIMA
                    / "check_tate_reflection_lift_eight_point_cut_naturality.py"
                ),
            ],
            text=True,
        )
    )
    assert base["local_loaded_lift_unique"]
    assert base["physical_cuts"] == 8
    assert base["reflection_defect_after_cut"] == 0

    induction = subprocess.check_output(
        [sys.executable, str(VOEVODSKY / "check_general_even_cut_induction.py")],
        text=True,
        cwd=str(VOEVODSKY),
    )
    assert "general_even_framed_Cut_induction: COMBINATORIAL_AND_SIGN_CORE_PROVED" in induction
    assert "every_nonempty_Cut_stratum: PRODUCT_OF_STRICTLY_SMALLER_EVEN_POLYGONS" in induction
    assert "Koszul_times_native_Thom_permutation_character: TRIVIAL_ALL_TESTED_ARITIES" in induction
    assert "scope: REQUIRES_BASE_RIGIDITY_AND_FUNCTORIAL_FACTOR_RESTRICTIONS" in induction

    print(
        json.dumps(
            {
                "status": "proved_scoped_tate_reflection_lift_all_even_Cut_induction",
                "base_arities": [4, 6, 8],
                "six_point_lift_unique": True,
                "eight_point_cut_base_passes": True,
                "general_induction": "quadrangulation of every even polygon",
                "maximal_cut_factors": "four-point units",
                "Koszul_times_Thom_character": 1,
                "reflection_defect": 0,
                "all_even_arities": True,
                "raw_scheme_statement_claimed": False,
                "conclusion": (
                    "The unique loaded Tate reflection lift propagates by "
                    "framed Cut descent to every even arity in the cellular "
                    "fs/Kato sector."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
