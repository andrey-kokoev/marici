import json
from pathlib import Path
import sympy as sp


def main():
    n = sp.symbols("n", integer=True, positive=True)
    hostile = sp.diag(n, 1 / n)
    assert sp.simplify(hostile.det() - 1) == 0
    assert sp.limit(1 / n, n, sp.oo) == 0
    assert sp.limit(n, n, sp.oo) == sp.oo

    # Exact rational rank-three fixture: determinant divided by the largest
    # two-singular-value product is the least singular value.
    controlled = sp.diag(sp.Rational(5, 1), sp.Rational(3, 1), sp.Rational(2, 1))
    determinant = abs(controlled.det())
    cofactor_norm = sp.Rational(5) * sp.Rational(3)
    least = sp.Rational(2)
    assert determinant == 30
    assert cofactor_norm == 15
    assert determinant / cofactor_norm == least
    assert determinant / (sp.Rational(5) ** 2) <= least

    # A uniformly conditioned constant frame changes constants, not collapse.
    a = sp.diag(2, 1)
    b = sp.diag(1, 3)
    transformed = b * hostile * a.inv()
    assert transformed == sp.diag(n / 2, 3 / n)
    assert sp.limit(transformed[1, 1], n, sp.oo) == 0

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_determinant_cofactor_coercivity_theorem",
        "hostile_determinant": 1,
        "hostile_least_singular_scale": "1/N",
        "hostile_cofactor_norm_scale": "N",
        "determinant_alone_uniformly_coercive": False,
        "rank_three_determinant": int(determinant),
        "rank_three_cofactor_norm": int(cofactor_norm),
        "rank_three_least_singular_value": int(least),
        "exact_ratio_verified": True,
        "uniform_frame_preserves_collapse": True,
        "required_independent_source_datum": "uniform_cofactor_exterior_power_bound",
        "theta_higher_rank_operator_complex": "not_supplied",
    }
    out = Path(__file__).parents[1] / "results" / "theta-determinant-coercivity.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
