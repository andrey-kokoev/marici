from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def rank_2x2(matrix):
    return 2 if matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] != 0 else 1


def main() -> None:
    scatter_left = Fraction(3, 100)
    scatter_right = Fraction(2, 100)
    reflected = Fraction(16, 25)
    transmitted = Fraction(1, 4)
    absorbed = Fraction(3, 50)
    closure_residual = 1 - reflected - transmitted - absorbed
    assert closure_residual == scatter_left + scatter_right == Fraction(1, 20)

    # Total collection detects and quantifies hidden power but has rank one on
    # a two-channel decomposition.
    total_loading = ((1, 1),)
    assert total_loading[0][0] == total_loading[0][1]
    aliases = (
        (Fraction(3, 100), Fraction(2, 100)),
        (Fraction(1, 100), Fraction(4, 100)),
        (Fraction(0), Fraction(5, 100)),
    )
    assert all(left + right == closure_residual for left, right in aliases)

    # One signed angular contrast supplies an independent loading.
    angular_contrast = scatter_left - scatter_right
    angular_loading = ((1, 1), (1, -1))
    assert rank_2x2(angular_loading) == 2
    recovered_left = (closure_residual + angular_contrast) / 2
    recovered_right = (closure_residual - angular_contrast) / 2
    assert (recovered_left, recovered_right) == (scatter_left, scatter_right)

    # Two detector electronics channels viewing the same integrating-sphere
    # carrier repeat the total loading and do not add physical rank.
    duplicated_loading = ((1, 1), (2, 2))
    assert rank_2x2(duplicated_loading) == 1

    # Spectral separation works only with independently sourced nonproportional
    # channel signatures.
    proportional_spectral_loading = ((1, 1), (3, 3))
    independent_spectral_loading = ((1, 1), (2, 5))
    assert rank_2x2(proportional_spectral_loading) == 1
    assert rank_2x2(independent_spectral_loading) == 2

    result = {
        "schema": "marici.aspect.hidden-scatter-channel-resolution.v1",
        "status": "pass",
        "measured_energy_channels": {
            "reflected": str(reflected),
            "transmitted": str(transmitted),
            "absorbed": str(absorbed),
        },
        "closure_residual": str(closure_residual),
        "total_collection_rank": 1,
        "compatible_hidden_decompositions": [[str(v) for v in pair] for pair in aliases],
        "angular_contrast": str(angular_contrast),
        "total_plus_angular_rank": 2,
        "recovered_scatter_channels": [str(recovered_left), str(recovered_right)],
        "duplicated_total_detector_rank": 1,
        "proportional_spectral_rank": 1,
        "independent_spectral_rank": 2,
        "verdict": "Energy closure detects omitted power, and total scatter collection quantifies it, but neither determines hidden-channel multiplicity or attribution. One independently calibrated angular contrast separates the frozen two-channel model. Spectral scans add rank only when source-derived channel signatures are nonproportional.",
        "claim_boundary": "two frozen nonnegative scatter channels with exact normalized power balance and declared angular or spectral loadings; no unknown extra channel, aperture loss, calibration uncertainty, or continuous angular distribution",
    }
    output = Path(__file__).parents[1] / "results" / "hidden_scatter_channel_resolution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
