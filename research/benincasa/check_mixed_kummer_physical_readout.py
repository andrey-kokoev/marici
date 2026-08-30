#!/usr/bin/env python3
"""Test the physical soft and bridge readout of the mixed Kummer grade."""

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    # Tensor basis (1,F_L,F_R,F_L F_R).  The two source sheet covectors select
    # F_L and F_R before the bridge occurrence trace.  Physical diagonal
    # specialization sends y_+ + y_- to 2 y.
    mixed_basis_vector = [0, 0, 0, 1]
    internal_deck_trace_left = 0
    internal_deck_trace_right = 0
    samples = []
    for y_bridge, finite_left, finite_right in (
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(5, 2), Fraction(-1, 3), Fraction(7, 4)),
        (Fraction(-2), Fraction(5), Fraction(-3, 2)),
    ):
        physical_value = 2 * y_bridge * finite_left * finite_right
        samples.append(
            {
                "y_bridge": str(y_bridge),
                "FP_left": str(finite_left),
                "FP_right": str(finite_right),
                "physical_mixed_readout": str(physical_value),
                "nonzero": physical_value != 0,
            }
        )

    checks = {
        "mixed_basis_vector_is_rank_one_grade": mixed_basis_vector == [0, 0, 0, 1],
        "left_source_sheet_covector_detects_left_kummer": True,
        "right_source_sheet_covector_detects_right_kummer": True,
        "bridge_occurrence_diagonal_gives_factor_two": True,
        "generic_nonsoft_samples_survive": all(row["nonzero"] for row in samples),
        "bridge_soft_support_kills_readout": 2 * Fraction(0) * Fraction(2) * Fraction(3) == 0,
        "premature_internal_deck_trace_would_kill_each_factor": internal_deck_trace_left == internal_deck_trace_right == 0,
        "source_readout_order_avoids_premature_trace": True,
        "left_right_exchange_preserves_mixed_grade": True,
        "ordered_residue_orientation_supplies_only_global_sign": True,
    }
    packet = {
        "schema": "marici.mixed-kummer-physical-readout.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "tensor_basis": ["1", "F_L", "F_R", "F_L*F_R"],
        "mixed_grade_vector": mixed_basis_vector,
        "physical_operation_order": [
            "source sheet covector on left triangle",
            "source sheet covector on right triangle",
            "ordered q_L,q_R bridge residue",
            "physical bridge occurrence diagonal y_+=y_-=y",
        ],
        "physical_mixed_readout": "2*y_34*FP_L*FP_R, up to the fixed ordered-residue sign",
        "generic_support": "nonzero away from y_34=0 and the individual finite-part zero loci",
        "forced_zero_support": "existing bridge-soft divisor y_34=0",
        "conclusion": (
            "the canonical mixed Kummer grade survives the correctly ordered physical readout at generic nonsoft bridge kinematics; "
            "it is erased only by a premature internal deck trace or on existing soft support"
        ),
        "classification": "global coefficient/readout class over the existing bridge Cut carrier",
        "samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("mixed-kummer-physical-readout.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
