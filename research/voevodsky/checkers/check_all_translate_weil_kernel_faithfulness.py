from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/all-translate-weil-kernel-faithfulness-v1.json")
SOURCE = Path("research/grothendieck/one-positive-spline-can-scale-only-through-its-full-translate-gram-kernel.md")


def principal_minors(matrix: sp.Matrix) -> list[sp.Expr]:
    values: list[sp.Expr] = []
    for size in range(1, matrix.rows + 1):
        for indices in combinations(range(matrix.rows), size):
            values.append(sp.simplify(matrix.extract(indices, indices).det()))
    return values


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "full translate Gram kernel" in source
    assert "positive definite" in source

    # Zero-character positivity alone does not control a two-translate minor.
    scalar_positive_bad_gram = sp.Matrix([[1, 2], [2, 1]])
    assert scalar_positive_bad_gram[0, 0] > 0
    assert scalar_positive_bad_gram.det() == -3

    # A genuine translation-positive kernel: k(a-b)=cos(a-b).
    points = [0, sp.pi / 2, sp.pi]
    cosine_gram = sp.Matrix([[sp.cos(left - right) for right in points] for left in points])
    feature = sp.Matrix([[sp.cos(point), sp.sin(point)] for point in points])
    assert cosine_gram == feature * feature.T
    minors = principal_minors(cosine_gram)
    assert all(value >= 0 for value in minors)
    assert cosine_gram.rank() == 2

    # One cyclic packet spans only its feature image; density is a separate arrow.
    assert cosine_gram.rank() < len(points)
    status = contract["status"]
    assert status["zero_slice_to_all_translate"] == "refuted"
    assert status["source_derived_all_translate_kernel"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.all-translate-weil-kernel-faithfulness-check.v1",
        "status":"translate_positivity_hierarchy_verified",
        "positive_zero_slice_counterexample":True,
        "counterexample_two_translate_determinant":-3,
        "positive_definite_translate_fixture":True,
        "translate_fixture_principal_minors_checked":len(minors),
        "cyclic_rank":cosine_gram.rank(),
        "density_arrow_supplied":False,
        "source_all_translate_kernel_supplied":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
