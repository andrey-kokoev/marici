import json
import sympy as sp


g, gp, u0, u1, v0, v1, q = sp.symbols("g gp u0 u1 v0 v1 q")
S = sp.Matrix([[g, 0], [gp, g]])
J = sp.Matrix([[0, 1], [-1, 0]])
u = sp.Matrix([u0, u1])
v = sp.Matrix([v0, v1])

checks = {
    "determinant": sp.simplify(S.det() - g**2) == 0,
    "alternating_form_multiplier": sp.simplify((S.T * J * S - g**2 * J).norm()) == 0,
    "wedge_multiplier": sp.expand(
        sp.Matrix.hstack(S * u, S * v).det()
        - g**2 * sp.Matrix.hstack(u, v).det()
    ) == 0,
}

# The infinite valuation chain gives g=(1-q)^-1.  Its determinant-line
# logarithm has coefficients 2/k.  The first two are the primitive and square
# currents; k>=3 is the determinant-three carrier tail.
log_det_series = sp.series(-2 * sp.log(1 - q), q, 0, 7).removeO()
expected = sum(sp.Rational(2, k) * q**k for k in range(1, 7))
checks["euler_log_coefficients"] = sp.expand(log_det_series - expected) == 0
checks["primitive_coefficient"] = log_det_series.coeff(q, 1) == 2
checks["square_coefficient"] = log_det_series.coeff(q, 2) == 1
checks["tail_starts_at_three"] = all(
    log_det_series.coeff(q, k) == sp.Rational(2, k) for k in range(3, 7)
)

result = {
    "schema": "marici.grothendieck.arithmetic_block_determinant_line_transport.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "transport_matrix": [["g", "0"], ["g'", "g"]],
    "determinant": "g^2",
    "euler_log_determinant_through_q6": str(log_det_series),
    "interpretation": {
        "strict_transport": "g^-1 S has determinant one",
        "coherence_line": "g^2",
        "primitive": "2 q",
        "prime_square": "q^2",
        "connected_tail": "sum_{k>=3} 2 q^k/k",
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
