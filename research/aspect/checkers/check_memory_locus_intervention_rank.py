from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def determinant_3(matrix: tuple[tuple[F, F, F], ...]) -> F:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def main() -> None:
    # Columns are source, detector-local, shared-electronics memory.
    signatures = {
        "baseline": (F(1), F(1), F(1)),
        "detector_reset_or_independent_reroute": (F(1), F(0), F(1)),
        "electronics_reset": (F(1), F(1), F(0)),
        "joint_detector_electronics_reset": (F(1), F(0), F(0)),
    }
    identification_matrix = (
        signatures["baseline"],
        signatures["detector_reset_or_independent_reroute"],
        signatures["electronics_reset"],
    )
    rank_witness = determinant_3(identification_matrix)
    assert rank_witness == 1

    source, detector, electronics = F(1, 8), F(1, 16), F(3, 32)
    observed = {
        condition: row[0] * source + row[1] * detector + row[2] * electronics
        for condition, row in signatures.items()
    }
    assert observed == {
        "baseline": F(9, 32),
        "detector_reset_or_independent_reroute": F(7, 32),
        "electronics_reset": F(3, 16),
        "joint_detector_electronics_reset": F(1, 8),
    }

    recovered_detector = observed["baseline"] - observed["detector_reset_or_independent_reroute"]
    recovered_electronics = observed["baseline"] - observed["electronics_reset"]
    recovered_source = (
        observed["detector_reset_or_independent_reroute"]
        + observed["electronics_reset"]
        - observed["baseline"]
    )
    assert (recovered_source, recovered_detector, recovered_electronics) == (
        source, detector, electronics
    )

    predicted_joint_reset = recovered_source
    assert predicted_joint_reset == observed["joint_detector_electronics_reset"]

    # A mismatched joint-reset record falsifies additive independent reset
    # action even though the first three conditions still fit three components.
    hostile_joint_reset = F(5, 32)
    interaction_residual = hostile_joint_reset - predicted_joint_reset
    assert interaction_residual == F(1, 32)
    assert interaction_residual != 0

    result = {
        "schema": "marici.aspect.memory-locus-intervention-rank.v1",
        "status": "pass",
        "memory_loci": ["source", "detector-local", "shared-electronics"],
        "intervention_signatures": {
            key: [str(value) for value in row] for key, row in signatures.items()
        },
        "three_condition_rank_determinant": str(rank_witness),
        "frozen_observed_covariances": {key: str(value) for key, value in observed.items()},
        "recovered_components": {
            "source": str(recovered_source),
            "detector-local": str(recovered_detector),
            "shared-electronics": str(recovered_electronics),
        },
        "joint_reset_is_model_falsifier": True,
        "hostile_joint_reset_interaction_residual": str(interaction_residual),
        "verdict": "Detector and electronics resets give a full-rank three-locus memory design under additive action; the joint reset is an independent falsifier for reset interaction or source disturbance.",
        "claim_boundary": "additive covariance components and ideal locus-specific resets; no reset-induced source change, cross-locus interaction, or higher memory state",
    }
    output = Path(__file__).parents[1] / "results" / "memory_locus_intervention_rank.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
