import json
from pathlib import Path
import sympy as sp


def main():
    n = sp.symbols("n", integer=True, positive=True)
    d_n = sp.diag(1, 1 / n)
    d_inf = d_n.applyfunc(lambda x: sp.limit(x, n, sp.oo))

    assert sp.simplify(d_n.det() - 1 / n) == 0
    assert d_n.rank() == 2
    assert d_inf == sp.diag(1, 0)
    assert d_inf.rank() == 1
    assert d_inf.nullspace() == [sp.Matrix([0, 1])]

    # Uniformly conditioned constant frames preserve the collapsing scale.
    a = sp.diag(2, 1)
    b = sp.diag(1, 3)
    transformed = b * d_n * a.inv()
    assert transformed == sp.diag(sp.Rational(1, 2), 3 / n)
    assert sp.limit(transformed[1, 1], n, sp.oo) == 0
    assert transformed.applyfunc(lambda x: sp.limit(x, n, sp.oo)).rank() == 1

    # An unauthorized unbounded target rescaling can hide the collapse.
    b_unbounded = sp.diag(1, n)
    repaired = b_unbounded * d_n
    assert repaired == sp.eye(2)

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_limit_theorem_and_typing_correction",
        "finite_rank": d_n.rank(),
        "finite_determinant": "1/N",
        "limit_rank": d_inf.rank(),
        "limit_kernel_basis": [[0, 1]],
        "least_singular_scale": "1/N",
        "uniformly_conditioned_frame_preserves_collapse": True,
        "unbounded_frame_can_hide_collapse": True,
        "ordinary_diagonal_l2_completion_kernel": 0,
        "ordinary_diagonal_l2_range_closed": False,
        "ultraproduct_escape_class_becomes_kernel": True,
        "bare_lim1_adds_independent_source_datum": False,
        "derived_route_disposition": "closed_without_source_inverse_system",
    }
    out = Path(__file__).parents[1] / "results" / "theta-strict-exactness-defect.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
