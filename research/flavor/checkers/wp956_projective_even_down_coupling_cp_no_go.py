import json
from pathlib import Path

import sympy as sp


def main() -> None:
    i = sp.I
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix(
        [[sp.Rational(1, 2), sp.Rational(1, 2), 0],
         [sp.Rational(1, 2), sp.Rational(1, 2), 0],
         [0, 0, 0]]
    )
    vector_r = sp.Matrix([1, i, 1])
    r = sp.simplify(vector_r * vector_r.conjugate().T / 3)
    democratic = sp.simplify(p + q + r)
    b = sp.simplify(p - q)
    b_squared = sp.simplify(b**2)

    yukawa_up = identity + democratic
    yukawa_down_even = 2 * identity + b_squared
    yukawa_down_odd = 2 * identity + b
    hu = sp.simplify(yukawa_up * yukawa_up.conjugate().T)
    hd_even = sp.simplify(yukawa_down_even * yukawa_down_even.conjugate().T)
    hd_odd = sp.simplify(yukawa_down_odd * yukawa_down_odd.conjugate().T)
    commutator_even = sp.simplify(hu * hd_even - hd_even * hu)
    commutator_odd = sp.simplify(hu * hd_odd - hd_odd * hu)

    up_discriminant = sp.factor(sp.discriminant(yukawa_up.charpoly().as_expr()))
    down_even_discriminant = sp.factor(sp.discriminant(yukawa_down_even.charpoly().as_expr()))
    down_odd_discriminant = sp.factor(sp.discriminant(yukawa_down_odd.charpoly().as_expr()))
    even_cp = sp.factor(sp.trace(commutator_even**3))
    odd_cp = sp.factor(sp.trace(commutator_odd**3))

    checks = {
        "b_hermitian": b == b.conjugate().T,
        "b_squared_exact": b_squared == sp.diag(sp.Rational(1, 2), sp.Rational(1, 2), 0),
        "b_minimal_polynomial_relation": sp.simplify(b * (b_squared - sp.Rational(1, 2) * identity)) == sp.zeros(3),
        "even_lift_sign_blind": (-b) ** 2 == b_squared,
        "even_lift_twofold_degenerate": len(b_squared.eigenvals()) == 2 and b_squared.eigenvals()[sp.Rational(1, 2)] == 2,
        "up_discriminant_retained": up_discriminant == sp.Rational(181, 54),
        "even_down_discriminant_zero": down_even_discriminant == 0,
        "odd_down_discriminant_nonzero": down_odd_discriminant == sp.Rational(1, 2),
        "even_commutator_nonzero": commutator_even != sp.zeros(3),
        "even_commutator_rank_two": commutator_even.rank() == 2,
        "even_cp_cubic_zero": even_cp == 0,
        "odd_cp_cubic_nonzero": odd_cp == -sp.Rational(3658, 3) * i,
        "projective_descent_incompatible_with_minimal_cp": even_cp == 0 and odd_cp != 0,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP956",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_comparison": {
            "b_squared": str(b_squared.tolist()),
            "up_discriminant": str(up_discriminant),
            "even_down_discriminant": str(down_even_discriminant),
            "odd_down_discriminant": str(down_odd_discriminant),
            "even_commutator_rank": commutator_even.rank(),
            "even_cp_cubic": str(even_cp),
            "odd_cp_cubic": str(odd_cp),
        },
        "classification": "minimal even projective coupling descends but forces down-sector degeneracy and zero three-family CP",
        "smallest_exact_falsifier": "B^2=diag(1/2,1/2,0) gives down discriminant 0 and CP cubic 0",
        "remaining_gate": "independently sourced second tensor yielding an orientation-insensitive simple-spectrum down operator, plus completion, descent, and instrument authority",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp956_projective_even_down_coupling_cp_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
