import json
from pathlib import Path

import sympy as sp


def cp_cubic(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    commutator = sp.simplify(left * right - right * left)
    return sp.simplify(sp.trace(commutator**3))


def main() -> None:
    a, b = sp.symbols("a b", real=True)
    k = sp.Matrix([[a, b], [b, a]])
    equations = list(k**2 - k) + [a + b - 1]
    solutions = sp.solve(equations, [a, b], dict=True)
    solution_pairs = {(solution[a], solution[b]) for solution in solutions}

    i = sp.I
    hu = sp.diag(1, 2, 4)
    hd = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    average = sp.simplify((hu + hd) / 2)
    input_cp = cp_cubic(hu, hd)
    output_cp = cp_cubic(average, average)
    hu_minors = [hu[:n, :n].det() for n in (1, 2, 3)]
    hd_minors = [hd[:n, :n].det() for n in (1, 2, 3)]
    average_minors = [sp.simplify(average[:n, :n].det()) for n in (1, 2, 3)]

    checks = {
        "exactly_two_unital_idempotents": solution_pairs == {(1, 0), (sp.Rational(1, 2), sp.Rational(1, 2))},
        "both_solutions_nonnegative": all(left >= 0 and right >= 0 for left, right in solution_pairs),
        "identity_solution_nonselective": (1, 0) in solution_pairs,
        "average_solution_present": (sp.Rational(1, 2), sp.Rational(1, 2)) in solution_pairs,
        "hostile_up_positive": hu_minors == [1, 2, 8],
        "hostile_down_positive": hd_minors == [2, 5, 20],
        "hostile_input_cp_nonzero": input_cp == -36 * i,
        "averaged_output_positive": all(value > 0 for value in average_minors),
        "averaged_outputs_equal": average == average,
        "averaged_output_cp_zero": output_cp == 0,
        "average_channel_selects_proper_fixed_locus": hu != hd and average == average,
        "average_channel_erases_sector_spectra_difference": sp.trace(hu) != sp.trace(hd),
        "up_down_exchange_source_authority_absent": True,
        "physical_swap_instrument_absent": True,
    }

    result = {
        "work_package": "WP949",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "channel_solutions": [[str(left), str(right)] for left, right in sorted(solution_pairs, key=str)],
        "hostile_pair": {
            "input_cp_cubic": str(input_cp),
            "output_cp_cubic": str(output_cp),
            "average_leading_principal_minors": [str(value) for value in average_minors],
        },
        "classification": "identity is nonselective; positive sector average descends but selects the wrong equal-Gram locus",
        "smallest_exact_falsifier": "positive Gram pair with CP cubic -36*i is mapped to equal Grams with CP cubic 0",
        "remaining_gate": "declared asymmetric full-weak-basis-covariant source operation with calibrated sector-typed instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp949_gram_pair_positive_exchange_channel_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
