from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    separation = Fraction(1, 10)
    two_atom_moments = (
        Fraction(1),
        separation / 2,
        separation**2 / 2,
        separation**3 / 2,
    )
    one_atom_moments = (
        Fraction(1),
        separation / 2,
        (separation / 2) ** 2,
        (separation / 2) ** 3,
    )
    assert two_atom_moments[:2] == one_atom_moments[:2]

    second_moment_gap = two_atom_moments[2] - one_atom_moments[2]
    third_moment_gap = two_atom_moments[3] - one_atom_moments[3]
    assert second_moment_gap == separation**2 / 4 == Fraction(1, 400)
    assert third_moment_gap == 3 * separation**3 / 8 == Fraction(3, 8000)

    hankel_determinant = (
        two_atom_moments[0] * two_atom_moments[2] - two_atom_moments[1] ** 2
    )
    central_variance = (
        two_atom_moments[2] / two_atom_moments[0]
        - (two_atom_moments[1] / two_atom_moments[0]) ** 2
    )
    assert hankel_determinant == central_variance == second_moment_gap

    tight_error = Fraction(1, 500)
    threshold_error = Fraction(1, 400)
    assert not (
        two_atom_moments[2] - tight_error
        <= one_atom_moments[2]
        <= two_atom_moments[2] + tight_error
    )
    assert (
        two_atom_moments[2] - threshold_error
        <= one_atom_moments[2]
        <= two_atom_moments[2] + threshold_error
    )

    # Halving separation quarters the variance witness.
    half_separation_gap = (separation / 2) ** 2 / 4
    assert half_separation_gap == second_moment_gap / 4

    result = {
        "schema": "marici.aspect.noisy-two-atom-resolution.v1",
        "status": "pass",
        "separation": str(separation),
        "two_atom_moments": [str(value) for value in two_atom_moments],
        "centroid_matched_one_atom_moments": [str(value) for value in one_atom_moments],
        "second_moment_gap": str(second_moment_gap),
        "third_moment_gap": str(third_moment_gap),
        "hankel_determinant": str(hankel_determinant),
        "central_variance": str(central_variance),
        "error_below_threshold": str(tight_error),
        "one_atom_excluded_below_threshold": True,
        "error_at_threshold": str(threshold_error),
        "one_atom_compatible_at_threshold": True,
        "half_separation_gap": str(half_separation_gap),
        "verdict": "Exact flat rank distinguishes any nonzero two-atom separation, but bounded second-moment uncertainty of d^2/4 makes the equal two-atom measure compatible with one centroid atom. Resolution therefore scales quadratically with separation in this moment instrument. Halving separation requires fourfold tighter variance accuracy.",
        "claim_boundary": "two equal positive atoms at known one-dimensional separation form versus one centroid atom, exact total and centroid, symmetric bounded error only on the second moment; no diffraction transfer, covariance, unequal weights, or adversarial errors in all moments",
    }
    output = Path(__file__).parents[1] / "results" / "noisy_two_atom_resolution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
