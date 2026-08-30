"""Test the universal conductor-difference identity on octahedral faces.

This is a coefficient-complex test only.  It does not construct the
support-changing Beck--Chevalley cells.
"""

from itertools import product
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
HOMOTOPY = ROOT / "research/nima/checkers/check_tate_reflection_discrepancy_homotopy.py"


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def neg(value):
    return tuple(-x for x in value)


def basis(index):
    return tuple(int(i == index) for i in range(3))


def main():
    homotopy = json.loads(
        subprocess.check_output([sys.executable, str(HOMOTOPY)], text=True)
    )
    assert homotopy["mixed_faces_only_h1_with_zero_h2_exists"]
    assert homotopy["mixed_faces_only_solution_integral"]
    assert homotopy["mixed_faces_only_affine_parameter_count"] == 0
    assert homotopy["pure_gauge_h2_vanishes"]

    faces = tuple(product((1, -1), repeat=3))
    pure = tuple(face for face in faces if len(set(face)) == 1)
    mixed = tuple(face for face in faces if len(set(face)) == 2)
    assert len(pure) == 2
    assert len(mixed) == 6

    closures = []
    for signs in mixed:
        minority_sign = -1 if signs.count(-1) == 1 else 1
        minority = signs.index(minority_sign)
        majority = tuple(i for i in range(3) if i != minority)
        a, b = basis(majority[0]), basis(majority[1])
        c = basis(minority)

        # Universal conductor differences on the two cross-sheet edges.
        ac = sub(a, c)
        bc = sub(b, c)
        # The independently supplied same-sheet edge restricts to a-b.
        ab = sub(a, b)
        residual = add(sub(ac, bc), neg(ab))
        assert residual == (0, 0, 0)
        closures.append(residual)

    # A pure face has no cross-sheet edge, hence the universal conductor
    # difference supplies no column there.  This is absence of evidence for a
    # face cell, not a nonexistence theorem for another extraordinary kernel.
    pure_faces_receiving_cross_columns = sum(
        any(signs[i] != signs[j] for i in range(3) for j in range(i + 1, 3))
        for signs in pure
    )
    assert pure_faces_receiving_cross_columns == 0

    print(
        json.dumps(
            {
                "status": "proved_scoped_universal_conductor_mixed_face_identity",
                "octahedral_faces": 8,
                "mixed_faces": 6,
                "pure_faces": 2,
                "mixed_faces_with_exact_difference_identity": len(closures),
                "mixed_coefficient_residual_rank": 0,
                "pure_faces_receiving_conductor_cross_columns": 0,
                "mixed_faces_only_reflection_homotopy_exists": True,
                "mixed_faces_only_reflection_homotopy_integral": True,
                "mixed_faces_only_reflection_homotopy_affine_nullity": 0,
                "reflection_homotopy_H2": 0,
                "extraordinary_face_cells_constructed": False,
                "conclusion": (
                    "The universal conductor difference passes the necessary "
                    "coefficient cancellation on exactly the six mixed faces "
                    "used by the unique constrained reflection homotopy. The "
                    "two pure faces and relative interior are not required in "
                    "this gauge. Six support-changing Beck-Chevalley cells "
                    "remain unconstructed."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
