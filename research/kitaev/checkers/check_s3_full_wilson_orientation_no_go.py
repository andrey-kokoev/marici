#!/usr/bin/env python3
"""Full eight-Wilson-packet orientation automorphism and subset no-go."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
MODULAR = K / "results" / "s3-modular-data.json"
SIX = K / "results" / "s3-all-faithful-family-orientation-no-go.json"
OUT = K / "results" / "s3-full-wilson-orientation-no-go.json"


def main() -> None:
    modular = json.loads(MODULAR.read_text(encoding="utf-8"))
    labels = modular["label_order"]
    matrix = [[Fraction(value) for value in row] for row in modular["S_matrix"]]
    eigenvalues = [[matrix[x][a] / matrix[0][a] for a in range(8)] for x in range(8)]
    assert all(value.denominator == 1 for row in eigenvalues for value in row)
    eigenvalues_int = [[int(value) for value in row] for row in eigenvalues]

    sector_permutation = [1, 0, 2, 4, 3, 5, 6, 7]
    coordinate_signs = [-1 if label in ("D", "E") else 1 for label in labels]
    for coordinate in range(8):
        for sector in range(8):
            assert coordinate_signs[coordinate] * eigenvalues_int[coordinate][sector] == \
                eigenvalues_int[coordinate][sector_permutation[sector]]

    faithful = []
    size_census = {str(size): 0 for size in range(1, 9)}
    for size in range(1, 9):
        for subset in itertools.combinations(range(8), size):
            signatures = {
                tuple(eigenvalues_int[coordinate][sector] for coordinate in subset)
                for sector in range(8)
            }
            if len(signatures) != 8:
                continue
            family = "".join(labels[coordinate] for coordinate in subset)
            assert "D" in family or "E" in family
            faithful.append(family)
            size_census[str(size)] += 1
            # Restricting the full-packet automorphism still maps the subset
            # signature of every sector to the permuted sector signature.
            for sector in range(8):
                transformed = tuple(
                    coordinate_signs[coordinate] * eigenvalues_int[coordinate][sector]
                    for coordinate in subset
                )
                target = tuple(
                    eigenvalues_int[coordinate][sector_permutation[sector]]
                    for coordinate in subset
                )
                assert transformed == target
    assert size_census == {"1": 0, "2": 0, "3": 0, "4": 8, "5": 22,
                           "6": 21, "7": 8, "8": 1}
    assert len(faithful) == 60

    six = json.loads(SIX.read_text(encoding="utf-8"))
    assert six["faithful_family_count"] == 15
    result = {
        "schema": "marici.kitaev.s3-full-wilson-orientation-no-go.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (MODULAR, SIX)
        },
        "full_Wilson_eigenvalue_matrix": eigenvalues_int,
        "full_packet_automorphism": {
            "sector_permutation": "(A B)(D E)",
            "coordinate_action": "negate Wilson coordinates D and E; fix A,B,C,F,G,H",
            "A_coordinate": "constant one",
            "B_coordinate_invariant_under_sector_permutation": True,
            "exact_intertwining_verified": True,
        },
        "all_subset_census": {
            "nonempty_subsets_checked": 255,
            "faithful_subsets": len(faithful),
            "faithful_size_census": size_census,
            "every_faithful_subset_contains_D_or_E": True,
            "every_faithful_subset_inherits_orientation_automorphism": True,
        },
        "no_go": {
            "adding_A_or_B_Wilson_coordinates_breaks_orientation": False,
            "any_Wilson_eigenvalue_subset_fixes_absolute_orientation": False,
            "orientation_breaker_must_be_outside_full_Wilson_eigenvalue_packet": True,
        },
        "boundary": {
            "all_functions_of_Wilson_coordinates_classified": False,
            "non_spectral_or_interferometric_observables_classified": False,
            "physical_orientation_constructor_supplied": False,
        },
        "verdict": "The hidden orientation symmetry extends to the full eight-Wilson eigenvalue packet derived from the modular S matrix: negate D and E coordinates while applying (A B)(D E) to sectors. A is constant and B is invariant, so adding them cannot break the symmetry. All 60 faithful subsets among the 255 nonempty Wilson subsets inherit the automorphism. Absolute orientation therefore requires information outside ordinary Wilson eigenvalue coordinates or a constructor that derives an orientation root.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
