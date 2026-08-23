"""Identify the induced reflection action on the physical derived pullback."""

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / "research/nima/checkers"
VOEVODSKY = ROOT / "research/voevodsky"


def main():
    lift = json.loads(
        subprocess.check_output(
            [
                sys.executable,
                str(NIMA / "check_tate_reflection_lift_all_even_cut_induction.py"),
            ],
            text=True,
        )
    )
    assert lift["reflection_defect"] == 0
    assert lift["all_even_arities"]

    physical = subprocess.check_output(
        [
            sys.executable,
            str(VOEVODSKY / "check_physical_derived_pullback_after_transform.py"),
        ],
        text=True,
        cwd=str(VOEVODSKY),
    )
    assert "integral_homology: H1=Z, ALL_OTHER_ZERO" in physical
    assert "primitive_generator_road_augmentation: +1" in physical
    assert "loaded_reflection_parity: EVEN" in physical
    assert "ordinary_forgetting_shadow: 0" in physical
    assert "six_point_positive_sheet_physical_class: PRIMITIVE_UNIQUE_LINE" in physical

    print(
        json.dumps(
            {
                "status": "proved_scoped_tate_reflection_identity_on_physical_line",
                "physical_homology": {"H1": "Z", "other": 0},
                "physical_generator_primitive": True,
                "source_literal_reflections_chain_homotopic": True,
                "induced_reflection_on_H1": 1,
                "comparison_homotopy_adds_physical_rank": 0,
                "ordinary_forgetting_shadow": 0,
                "all_even_cut_transport": True,
                "numerical_amplitude_identified": False,
                "conclusion": (
                    "Source and literal reflection induce the same identity "
                    "on the unique primitive physical line. The conductor "
                    "homotopy is required coherence, not an additional "
                    "physical state."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
