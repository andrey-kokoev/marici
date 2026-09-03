from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/collision-stratified-observer-rkhs-v1.json")


def gaussian_gram(points: list[sp.Expr]) -> sp.Matrix:
    return sp.Matrix([[sp.exp(-(x - y) ** 2) for y in points] for x in points])


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    h = sp.symbols("h", positive=True, real=True)
    gram_two = gaussian_gram([sp.Integer(0), h])
    margin = 1 - sp.exp(-h**2)
    assert sp.simplify(gram_two * sp.Matrix([1, -1]) - margin * sp.Matrix([1, -1])) == sp.zeros(2, 1)
    assert sp.simplify(gram_two * sp.Matrix([1, 1]) - (1 + sp.exp(-h**2)) * sp.Matrix([1, 1])) == sp.zeros(2, 1)
    assert sp.limit(margin / h**2, h, 0, dir="+") == 1
    assert sp.limit(margin, h, 0, dir="+") == 0

    repeated = gaussian_gram([sp.Integer(0), sp.Integer(0)])
    assert repeated.rank() == 1 and repeated.det() == 0

    # Distinct rational labels give strictly positive sampled Gram fixtures.
    sampled_spacings = []
    for spacing in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Integer(1)):
        gram = gaussian_gram([0, spacing, 2 * spacing])
        # Exact Sylvester criterion, avoiding numerical eigenvalue comparisons.
        assert gram[0, 0] == 1
        assert sp.simplify(gram[:2, :2].det()).is_positive
        assert sp.simplify(gram.det()).is_positive
        sampled_spacings.append(str(spacing))

    # For every fixed positive error radius, some distinct h has smaller margin.
    for denominator in range(2, 12):
        delta = sp.Rational(1, denominator)
        h_choice = sp.Rational(1, 2 * denominator)
        assert margin.subs(h, h_choice) < h_choice**2 < delta

    status = contract["status"]
    assert status["source_derived_rh_feature_map"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.collision-stratified-observer-rkhs-check.v1",
        "status":"collision_margin_obstruction_verified",
        "quadratic_margin_limit":True,
        "repeated_label_kernel":True,
        "distinct_three_point_fixtures":len(sampled_spacings),
        "near_collision_defeats_fixed_error":True,
        "sampled_spacings":sampled_spacings,
        "source_derived_rh_feature_map":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
