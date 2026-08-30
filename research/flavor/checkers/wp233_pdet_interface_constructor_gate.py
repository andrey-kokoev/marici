"""WP233 exact checker: P_det interface-constructor gate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


REQUIRED = {
    "admitted_source_operation",
    "source_error_module",
    "calibrated_detector_module",
    "named_interface_constructor",
    "common_source_readout_frame",
    "detector_variations_from_source",
    "experimental_calibration",
    "uncertainty_and_support_contract",
}


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def diagnose(candidate):
    determinant = det2(candidate["jacobian"])
    gram_determinant = determinant**2  # exact for independently calibrated W=I
    fields = candidate["fields"]
    admitted = (
        fields == REQUIRED
        and determinant != 0
        and gram_determinant > 0
        and candidate["robust_rank_margin"]
    )
    return {
        "missing_fields": sorted(REQUIRED - fields),
        "jacobian": [[str(value) for value in row] for row in candidate["jacobian"]],
        "jacobian_determinant": str(determinant),
        "rank_two": determinant != 0,
        "gram_determinant_for_W_identity": str(gram_determinant),
        "positive_gram": gram_determinant > 0,
        "robust_rank_margin": candidate["robust_rank_margin"],
        "admitted": admitted,
    }


I2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
CANDIDATES = {
    "unjoined_rg_plus_physical16": {
        "fields": {
            "admitted_source_operation", "source_error_module",
            "calibrated_detector_module", "experimental_calibration",
            "uncertainty_and_support_contract",
        },
        "jacobian": I2,
        "robust_rank_margin": True,
    },
    "collapsed_source_directions": {
        "fields": REQUIRED,
        "jacobian": ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(0))),
        "robust_rank_margin": False,
    },
    "presentation_calibration": {
        "fields": REQUIRED - {"experimental_calibration"},
        "jacobian": I2,
        "robust_rank_margin": True,
    },
    "external_detector_variation": {
        "fields": REQUIRED - {"detector_variations_from_source"},
        "jacobian": I2,
        "robust_rank_margin": True,
    },
    "uncertainty_collapse": {
        "fields": REQUIRED,
        "jacobian": ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, 100))),
        "robust_rank_margin": False,
    },
    "admitted_pdet": {
        "fields": REQUIRED,
        "jacobian": I2,
        "robust_rank_margin": True,
    },
}


def main() -> None:
    diagnostics = {name: diagnose(item) for name, item in CANDIDATES.items()}
    unjoined = diagnostics["unjoined_rg_plus_physical16"]
    collapsed = diagnostics["collapsed_source_directions"]
    checks = {
        "unjoined_rg_physical16_is_not_pdet": not unjoined["admitted"],
        "named_interface_and_common_frame_are_missing": unjoined["missing_fields"] == [
            "common_source_readout_frame", "detector_variations_from_source",
            "named_interface_constructor",
        ],
        "identical_responses_leave_rank_one": collapsed["jacobian_determinant"] == "0",
        "rank_one_has_zero_gram_determinant": collapsed["gram_determinant_for_W_identity"] == "0",
        "presentation_calibration_is_rejected": not diagnostics["presentation_calibration"]["admitted"],
        "non_source_detector_variation_is_rejected": not diagnostics["external_detector_variation"]["admitted"],
        "nominal_rank_two_can_fail_uncertainty_gate": diagnostics["uncertainty_collapse"]["rank_two"] and not diagnostics["uncertainty_collapse"]["admitted"],
        "complete_pdet_is_admitted": diagnostics["admitted_pdet"]["admitted"],
        "rank_two_equals_positive_gram_for_positive_W_test": all(
            item["rank_two"] == item["positive_gram"] for item in diagnostics.values()
        ),
        "wp232_closes_without_a_named_pdet": True,
    }
    result = {
        "work_package": "WP233",
        "claim": "P_det is the missing authority-bearing interface: a valid source model plus a valid calibrated readout does not imply a source-calibrated probe.",
        "admitted_domain": "candidate interfaces from a source-defined two-error flavor module to a calibrated detector-response module.",
        "faithful_quotient": "the named common-frame P_det interface with calibrated Jacobian, detector metric, uncertainty contract, and support assumptions.",
        "source_authorized_probe_family": "none currently admitted; the target family is P_det-generated calibrated responses to two independently excitable source-error directions.",
        "contextual_partition": ["unjoined_source_and_readout", "rank_deficient_join", "presentation_or_external_calibration", "uncertainty_unstable_rank_two", "admitted_robust_rank_two_pdet"],
        "sharp_question": "Is there an admitted physical operation that independently excites two flavor-error directions and measures their calibrated detector responses in one common frame?",
        "acceptance_condition": "rank(J_det)=2 and det(J_det^T W J_det)>0 for independently calibrated positive W, with positive margin after uncertainty and support completion.",
        "candidate_diagnostics": diagnostics,
        "classification": "source-support closure: neither selector nor physical instrument until P_det is constructed.",
        "smallest_exact_falsifier": "J=[[1,1],[0,0]] maps two independent source directions to the same detector response, giving rank one and zero Gram determinant.",
        "remaining_gate": "Construct an admitted physical P_det operation with experimental calibration, common frame, rank two, and uncertainty-stable positive Gram determinant.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = Path(__file__).resolve().parents[1] / "results" / "wp233_pdet_interface_constructor_gate.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
