"""WP348: exact source-coefficient response of the WP326 capability witness."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    coefficient = sp.symbols("x", real=True)
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [0, 0, 0]])
    vector_r = sp.Matrix([1, sp.I, 1])
    r = sp.simplify(vector_r * vector_r.conjugate().T / 3)
    yukawa_up = identity + p + 2 * q + coefficient * r
    yukawa_down = 2 * identity + 4 * p + q + 5 * r
    hu = sp.simplify(yukawa_up * yukawa_up.conjugate().T)
    hd = sp.simplify(yukawa_down * yukawa_down.conjugate().T)
    commutator = sp.simplify(hu * hd - hd * hu)
    cp_odd = sp.factor(sp.trace(commutator**3))
    up_norm = sp.factor(sp.trace(hu))
    up_determinant = sp.factor(hu.det())
    benchmark = sp.Integer(3)
    responses = {
        "up_norm": sp.factor(sp.diff(up_norm, coefficient).subs(coefficient, benchmark)),
        "up_determinant": sp.factor(sp.diff(up_determinant, coefficient).subs(coefficient, benchmark)),
        "cp_odd": sp.factor(sp.diff(cp_odd, coefficient).subs(coefficient, benchmark)),
    }
    checks = {
        "benchmark_recovers_wp326_cp_value": cp_odd.subs(coefficient, benchmark) == -10900883 * sp.I,
        "cp_polynomial_has_multiple_zero_branches": cp_odd.subs(coefficient, sp.Rational(5, 4)) == 0 and cp_odd.subs(coefficient, 10) == 0,
        "up_norm_responds_at_benchmark": responses["up_norm"] == 10,
        "up_determinant_responds_at_benchmark": responses["up_determinant"] == 100,
        "cp_odd_invariant_responds_at_benchmark": responses["cp_odd"] == -sp.Rational(71353555, 9) * sp.I,
        "physical_response_rank_is_at_least_one": any(value != 0 for value in responses.values()),
        "coefficient_is_not_null_control": all(value != 0 for value in responses.values()),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP348",
        "admitted_state_domain": "the WP326 three-projector family with the up-sector coefficient of R varied as a real source parameter x and all other witness data frozen",
        "faithful_quotient_coordinate": "weak-basis-invariant up norm, up determinant, and cubic CP-odd commutator trace",
        "source_operation": "vary x in Y_u=I+P+2Q+xR while retaining Y_d=2I+4P+Q+5R",
        "up_norm": str(up_norm),
        "up_determinant": str(up_determinant),
        "cp_odd_invariant": str(cp_odd),
        "benchmark_x": int(benchmark),
        "benchmark_responses": {name: str(value) for name, value in responses.items()},
        "contextual_partition": "different x values generically produce different physical invariant packets; x is not erased by weak-basis or detector quotienting",
        "classification": "WP326 is a generic physical16 capability family, not a numerical selector; its displayed flavor packet responds nontrivially to an unselected source coefficient",
        "smallest_exact_falsifier": "at x=3 all three audited physical invariants have nonzero derivative, including CP response -71353555*i/9",
        "remaining_physical_instrument_gate": "derive x and the other affine coefficients from a source action with zero physical response to all unfixed inputs, then test the resulting packet on the complete fitted ensemble",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp348_three_projector_coefficient_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
