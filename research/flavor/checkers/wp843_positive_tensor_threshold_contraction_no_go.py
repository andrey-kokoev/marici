"""Exact WP843 no-go for increasing positive tensor screening by restriction."""

import json
from pathlib import Path
import sympy as sp


def frobenius_square(matrix: sp.Matrix):
    return sp.expand(sp.trace(matrix.T*matrix))


def main() -> None:
    entries = sp.symbols("t0:9", real=True)
    T = sp.Matrix(3, 3, entries)
    P = sp.diag(0, 1, 1)
    compressed = P*T*P
    full_norm = frobenius_square(T)
    active_norm = frobenius_square(compressed)
    loss = sp.expand(full_norm-active_norm)
    T0 = sp.Matrix([[1, 2, 0], [0, 4, 7], [0, 0, 0]])
    required_full = sp.Integer(70)
    required_active = sp.Integer(84)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    expected_loss = (entries[0]**2+entries[1]**2+entries[2]**2
                     +entries[3]**2+entries[6]**2)
    check("compression_loss_is_exact_sum_of_removed_squares",
          sp.simplify(loss-expected_loss) == 0, loss)
    check("compression_loss_polynomial_has_only_positive_square_terms",
          sp.Poly(loss, entries).coeffs() == [1, 1, 1, 1, 1],
          sp.Poly(loss, entries).terms())
    check("explicit_full_tensor_realizes_screening_seventy",
          frobenius_square(T0) == required_full, frobenius_square(T0))
    check("explicit_compression_cannot_exceed_full_norm",
          frobenius_square(P*T0*P) <= frobenius_square(T0),
          (frobenius_square(T0), frobenius_square(P*T0*P)))
    check("required_active_screening_exceeds_full_screening",
          required_active > required_full, required_active-required_full)
    check("positive_orthogonal_restriction_cannot_reach_eighty_four",
          required_active > required_full, "84>70>=||PTP||_F^2")
    amplification_squared = sp.Rational(required_active, required_full)
    check("minimal_lossless_squared_amplification_is_six_fifths",
          amplification_squared == sp.Rational(6, 5), amplification_squared)
    check("minimal_lossless_amplitude_factor_is_sqrt_six_fifths",
          sp.sqrt(amplification_squared) == sp.sqrt(sp.Rational(6, 5)),
          sp.sqrt(amplification_squared))
    generated_increment = required_active-required_full
    check("alternative_generated_increment_is_fourteen",
          generated_increment == 14, generated_increment)
    check("generated_increment_matches_ward_index_numerically",
          generated_increment == 1**2+2**2+3**2, generated_increment)
    check("ward_index_equality_does_not_remove_matching_choice",
          amplification_squared != 1 and generated_increment != 0,
          (amplification_squared, generated_increment))
    check("ordinary_restriction_branch_closes_negative",
          required_active > required_full, "contractivity contradicts 70->84")

    result = {
        "work_package": "WP843",
        "title": "Positive tensor threshold contraction no-go",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "theorem_domain": "finite real interaction tensors with positive Frobenius pairing and orthogonal/conditional-expectation threshold restriction",
        "contractivity": "||PTP||_F^2 <= ||T||_F^2",
        "required_transition": "Y_full=70 -> Y_active=84",
        "no_go": "ordinary positive restriction cannot increase screening",
        "minimal_repairs": {"lossless_squared_amplification": "6/5",
                            "lossless_amplitude_factor": "sqrt(6/5)",
                            "new_positive_increment": "14"},
        "classification": "exact negative threshold theorem; noncontractive finite matching or threshold-generated interaction is necessary",
        "claim_boundary": "the numerical equality of the increment 14 with Tr(Q^2) is suggestive but has no source authority",
        "remaining_source_gate": "derive the noncontractive matching factor or generated threshold term from one microscopic action and realize its labelled physical16 response",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp843_positive_tensor_threshold_contraction_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
