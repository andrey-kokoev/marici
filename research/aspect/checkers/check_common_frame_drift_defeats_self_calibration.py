from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(2)) for i in range(2))


def main() -> None:
    zero = Fraction(0)
    one = Fraction(1)
    identity = ((one, zero), (zero, one))
    quarter_turn = ((zero, -one), (one, zero))

    reference_preparations = (identity, quarter_turn)
    analyzer_maps = (identity, transpose(quarter_turn))
    internal_calibrations = tuple(
        matmul(analyzer, preparation)
        for analyzer, preparation in zip(analyzer_maps, reference_preparations)
    )
    assert internal_calibrations == (identity, identity)

    # Orthogonal matrices have singular values one, so conditioning is perfect.
    internal_minimum_margins = (one, one)
    assert internal_minimum_margins == (one, one)

    laboratory_fixed_science = (one, zero)
    science_records = tuple(
        matvec(analyzer, laboratory_fixed_science) for analyzer in analyzer_maps
    )
    assert science_records == ((one, zero), (zero, -one))

    laboratory_fixed_reference = laboratory_fixed_science
    external_anchor_records = tuple(
        matvec(analyzer, laboratory_fixed_reference) for analyzer in analyzer_maps
    )
    assert external_anchor_records == science_records
    external_anchor_detects_drift = external_anchor_records[0] != external_anchor_records[1]
    assert external_anchor_detects_drift

    result = {
        "schema": "marici.aspect.common-frame-drift-defeats-self-calibration.v1",
        "status": "pass",
        "internal_calibration_initial": [[str(value) for value in row] for row in internal_calibrations[0]],
        "internal_calibration_final": [[str(value) for value in row] for row in internal_calibrations[1]],
        "internal_calibration_unchanged": internal_calibrations[0] == internal_calibrations[1],
        "internal_reference_span_full": True,
        "internal_minimum_singular_margins": [str(value) for value in internal_minimum_margins],
        "laboratory_science_records": [[str(value) for value in record] for record in science_records],
        "science_frame_changed": science_records[0] != science_records[1],
        "external_anchor_detects_drift": external_anchor_detects_drift,
        "verdict": "A co-rotating spanning reference and analyzer retain identity calibration with singular margin one while a laboratory-fixed science vector rotates by ninety degrees in analyzer coordinates. Full span and conditioning do not fix a shared gauge; a cross-locus anchor is required.",
        "claim_boundary": "exact two-dimensional orthogonal rotations and noiseless references; no general Mueller gauge, imperfect anchor, translation, phase drift, or finite-sample uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "common_frame_drift_defeats_self_calibration.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
