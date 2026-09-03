from __future__ import annotations

import json
from fractions import Fraction


def main() -> None:
    cyclic = Fraction(2)
    cross = Fraction(1, 2)
    auxiliary = Fraction(1)
    schur = cyclic - cross * cross / auxiliary
    assert schur == Fraction(7, 4) > 0

    # Exhaustive exact sample of nonzero decomposition-preserving diagonal scalings.
    scalars = [Fraction(-3), Fraction(-1), Fraction(1, 2), Fraction(1), Fraction(2)]
    transformed_cross_entries = {
        f"{a}:{b}": a * b * cross
        for a in scalars
        for b in scalars
    }
    assert all(value != 0 for value in transformed_cross_entries.values())

    # The shear that removes the cross block necessarily mixes the summands.
    shear = -cross / auxiliary
    assert shear == Fraction(-1, 2) != 0
    decomposition_preserved_by_shear = shear == 0
    assert not decomposition_preserved_by_shear

    result = {
        "schema": "marici.voevodsky.source-sector-orthogonal-split-comparison.v1",
        "status": "sourced_sectors_not_realized_by_orthogonal_split_model",
        "green_block": [["2/1", "1/2"], ["1/2", "1/1"]],
        "green_schur_complement": "7/4",
        "decomposition_preserving_cross_formula": "a*b/2",
        "sample_nonzero_scaling_pairs": len(transformed_cross_entries),
        "all_sample_transformed_cross_entries_nonzero": True,
        "diagonalizing_shear": "-1/2",
        "diagonalizing_shear_preserves_declared_summands": decomposition_preserved_by_shear,
        "green_structure_preserving_comparison_exists": False,
        "gauge_comparison_gate": "source-derived canonical section and kernel framing absent",
        "closed_form_comparison_gate": "independently derived common-core intertwiner R_zeta absent",
        "next_gate": "nonorthogonal full-Gram certified analytic realization",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
