from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def matvec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(3)) for row in matrix)


def has_revival(sequence):
    return any(later > earlier for earlier, later in zip(sequence, sequence[1:]))


def main() -> None:
    true_contrasts = (Fraction(1), Fraction(1, 2), Fraction(1, 4))
    x_gains = (Fraction(1), Fraction(1), Fraction(4))
    transfers = tuple(
        (
            (gain, Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(1)),
        )
        for gain in x_gains
    )

    x_axis = (Fraction(1), Fraction(0), Fraction(0))
    y_axis = (Fraction(0), Fraction(1), Fraction(0))
    z_axis = (Fraction(0), Fraction(0), Fraction(1))
    raw_science = tuple(matvec(matrix, (contrast, 0, 0))[0] for matrix, contrast in zip(transfers, true_contrasts))
    scalar_z_reference = tuple(matvec(matrix, z_axis)[2] for matrix in transfers)
    scalar_corrected = tuple(value / reference for value, reference in zip(raw_science, scalar_z_reference))

    assert raw_science == (Fraction(1), Fraction(1, 2), Fraction(1))
    assert scalar_z_reference == (Fraction(1), Fraction(1), Fraction(1))
    assert scalar_corrected == raw_science
    assert has_revival(scalar_corrected)

    spanning_outputs = tuple(
        (matvec(matrix, x_axis), matvec(matrix, y_axis), matvec(matrix, z_axis))
        for matrix in transfers
    )
    reconstructed_x_gains = tuple(outputs[0][0] for outputs in spanning_outputs)
    assert reconstructed_x_gains == x_gains
    spanning_corrected = tuple(value / gain for value, gain in zip(raw_science, reconstructed_x_gains))
    assert spanning_corrected == true_contrasts
    assert not has_revival(spanning_corrected)

    result = {
        "schema": "marici.aspect.scalar-reference-blind-to-anisotropic-drift.v1",
        "status": "pass",
        "true_x_science_contrasts": [str(value) for value in true_contrasts],
        "analyzer_x_gains": [str(value) for value in x_gains],
        "raw_x_science_record": [str(value) for value in raw_science],
        "scalar_z_reference_record": [str(value) for value in scalar_z_reference],
        "scalar_reference_appears_stable": len(set(scalar_z_reference)) == 1,
        "scalar_corrected_record": [str(value) for value in scalar_corrected],
        "scalar_corrected_has_false_revival": has_revival(scalar_corrected),
        "spanning_reconstructed_x_gains": [str(value) for value in reconstructed_x_gains],
        "spanning_corrected_record": [str(value) for value in spanning_corrected],
        "spanning_corrected_has_revival": has_revival(spanning_corrected),
        "verdict": "A perfectly stable Z reference misses fourfold X-channel drift and leaves a false science revival unchanged. Spanning X/Y/Z references reconstruct the anisotropic transfer and recover monotone decay exactly; calibration must span the science contrast subspace.",
        "claim_boundary": "exact diagonal transfer matrices and noiseless spanning references; no general rotation, source-reference drift, ill-conditioning, or finite-sample uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "scalar_reference_blind_to_anisotropic_drift.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
