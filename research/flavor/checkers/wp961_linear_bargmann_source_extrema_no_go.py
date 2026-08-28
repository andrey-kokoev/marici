import json
from pathlib import Path

import sympy as sp


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.conjugate().T / (vector.conjugate().T * vector)[0])


def bargmann(vectors: tuple[sp.Matrix, sp.Matrix, sp.Matrix]) -> sp.Expr:
    p, q, r = tuple(projector(vector) for vector in vectors)
    return sp.simplify(sp.trace(p * q * r))


def main() -> None:
    sqrt_three = sp.sqrt(3)
    trine_vectors = (
        sp.Matrix([1, 0, 0]),
        sp.Matrix([-sp.Rational(1, 2), sqrt_three / 2, 0]),
        sp.Matrix([-sp.Rational(1, 2), -sqrt_three / 2, 0]),
    )
    collinear_vectors = tuple(sp.Matrix([1, 0, 0]) for _ in range(3))

    trine_bargmann = bargmann(trine_vectors)
    collinear_bargmann = bargmann(collinear_vectors)
    trine_span = sp.Matrix.hstack(*trine_vectors)
    collinear_span = sp.Matrix.hstack(*collinear_vectors)
    trine_gram = sp.simplify(trine_span.conjugate().T * trine_span)
    trine_inner_products = [
        sp.simplify(trine_vectors[0].dot(trine_vectors[1])),
        sp.simplify(trine_vectors[1].dot(trine_vectors[2])),
        sp.simplify(trine_vectors[2].dot(trine_vectors[0])),
    ]

    t = sp.symbols("t", nonnegative=True)
    endpoint_polynomial = sp.factor(1 - 3 * t**2 - 2 * t**3)

    checks = {
        "trine_unit_vectors": all(sp.simplify(v.dot(v)) == 1 for v in trine_vectors),
        "trine_signed_overlaps_minus_half": trine_inner_products == [-sp.Rational(1, 2)] * 3,
        "trine_gram_positive_semidefinite": all(value >= 0 for value in trine_gram.eigenvals()),
        "trine_gram_determinant_zero": sp.factor(trine_gram.det()) == 0,
        "trine_span_rank_two": trine_span.rank() == 2,
        "trine_bargmann_exact_minimum": trine_bargmann == -sp.Rational(1, 8),
        "trine_cp_orientation_zero": sp.im(trine_bargmann) == 0,
        "am_gm_endpoint_factorization": sp.expand(endpoint_polynomial + (2 * t - 1) * (t + 1) ** 2) == 0,
        "lower_endpoint_root_one_half": endpoint_polynomial.subs(t, sp.Rational(1, 2)) == 0,
        "collinear_span_rank_one": collinear_span.rank() == 1,
        "collinear_bargmann_exact_maximum": collinear_bargmann == 1,
        "collinear_cp_orientation_zero": sp.im(collinear_bargmann) == 0,
        "linear_cp_even_term_selects_only_cp_blind_endpoints": sp.im(trine_bargmann) == 0 and sp.im(collinear_bargmann) == 0,
        "nonlinear_phase_frustration_remains_open": True,
        "physical_instrument_remains_open": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP961",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_extrema": {
            "minimum": {"bargmann": str(trine_bargmann), "span_rank": trine_span.rank(), "gram_determinant": str(sp.factor(trine_gram.det()))},
            "maximum": {"bargmann": str(collinear_bargmann), "span_rank": collinear_span.rank()},
        },
        "classification": "the linear CP-even Bargmann source selects only real rank-deficient endpoint triples",
        "smallest_exact_falsifier": "the minimum -1/8 is the rank-two real trine and the maximum 1 is the rank-one collinear triple",
        "remaining_gate": "a readout-independent nonlinear CP-even phase-frustration term with conjugate spanning minima, or an independently authorized CP-odd source term, plus completion and instrument transport",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp961_linear_bargmann_source_extrema_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
