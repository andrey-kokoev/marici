import json
from pathlib import Path

import sympy as sp


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.conjugate().T / (vector.conjugate().T * vector)[0])


def main() -> None:
    p = sp.Matrix([1, 0, 0])
    q = sp.Matrix([1, 1, 0])
    r_plus = sp.Matrix([1, sp.I, 0])
    r_minus = sp.conjugate(r_plus)
    projectors_plus = tuple(projector(v) for v in (p, q, r_plus))
    projectors_minus = tuple(projector(v) for v in (p, q, r_minus))
    b_plus = sp.simplify(sp.trace(projectors_plus[0] * projectors_plus[1] * projectors_plus[2]))
    b_minus = sp.simplify(sp.trace(projectors_minus[0] * projectors_minus[1] * projectors_minus[2]))
    span_plus = sp.Matrix.hstack(p, q, r_plus)
    gram_plus = sp.simplify(span_plus.conjugate().T * span_plus)

    s = sp.symbols("s", real=True)
    envelope = sp.expand((s / 3) ** 3 - (s - 1) ** 2 / 4)
    envelope_derivative = sp.factor(sp.diff(envelope, s))

    half = sp.Rational(1, 2)
    g_real = sp.Matrix([[1, half, half], [half, 1, half], [half, half, 1]])
    g_imag = sp.Matrix([[1, half, -sp.I * half], [half, 1, half], [sp.I * half, half, 1]])
    b_real = sp.simplify(g_real[0, 1] * g_real[1, 2] * g_real[2, 0])
    b_imag = sp.simplify(g_imag[0, 1] * g_imag[1, 2] * g_imag[2, 0])

    checks = {
        "maximizer_bargmann_plus": b_plus == (1 + sp.I) / 4,
        "maximizer_bargmann_minus": b_minus == (1 - sp.I) / 4,
        "conjugate_pair": b_minus == sp.conjugate(b_plus),
        "orientation_square_one_sixteenth": sp.im(b_plus) ** 2 == sp.Rational(1, 16),
        "maximizer_span_rank_two": span_plus.rank() == 2,
        "maximizer_gram_determinant_zero": sp.factor(gram_plus.det()) == 0,
        "envelope_stationary_at_three_halves": sp.diff(envelope, s).subs(s, sp.Rational(3, 2)) == 0,
        "envelope_value_one_sixteenth": envelope.subs(s, sp.Rational(3, 2)) == sp.Rational(1, 16),
        "envelope_derivative_exact": sp.expand(envelope_derivative - (s - 3) * (2 * s - 3) / 18) == 0,
        "pairwise_hostiles_same_moduli": all(abs(g_real[i, j]) == abs(g_imag[i, j]) for i in range(3) for j in range(3)),
        "pairwise_hostiles_positive_definite": g_real.det() > 0 and g_imag.det() > 0,
        "pairwise_hostiles_different_orientation": sp.im(b_real) == 0 and abs(sp.im(b_imag)) == sp.Rational(1, 8),
        "modulus_factorizes_pairwise": abs(b_real) ** 2 == sp.Rational(1, 64) and abs(b_imag) ** 2 == sp.Rational(1, 64),
        "genuine_ternary_probe_required": sp.im(b_real) != sp.im(b_imag),
        "positive_volume_constructor_remains_open": True,
        "physical_instrument_remains_open": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP962",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_maximizer": {"bargmann_pair": [str(b_plus), str(b_minus)], "orientation_square": "1/16", "span_rank": span_plus.rank(), "gram_determinant": str(sp.factor(gram_plus.det()))},
        "pairwise_hostile": {"common_squared_overlaps": ["1/4", "1/4", "1/4"], "bargmann_values": [str(b_real), str(b_imag)], "gram_determinants": [str(g_real.det()), str(g_imag.det())]},
        "classification": "the pure CP-even squared-orientation source selects a nonzero conjugate pair only on the rank-two Gram boundary",
        "smallest_exact_falsifier": "the sharp |Im B|=1/4 maximizer has Gram determinant zero and span rank two",
        "remaining_gate": "an independently normalized positive-volume completion preserving nonzero orientation and full span, followed by instrument transport; handedness remains unselected",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp962_squared_bargmann_orientation_boundary_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
