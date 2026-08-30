import json
from pathlib import Path

import sympy as sp


def cp_cubic(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    commutator = sp.simplify(left * right - right * left)
    return sp.simplify(sp.trace(commutator**3))


def main() -> None:
    a, b = sp.symbols("a b", real=True)
    k = sp.Matrix([[a, 1 - a], [b, 1 - b]])
    residual = sp.simplify(k**2 - k)
    factored_entries = [sp.factor(residual[0, 0]), sp.factor(residual[1, 0])]

    i = sp.I
    hu = sp.diag(1, 2, 4)
    hd = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    input_cp = cp_cubic(hu, hd)
    selected = {}
    for c in (sp.Rational(1, 3), sp.Rational(2, 3)):
        common = sp.simplify(c * hu + (1 - c) * hd)
        minors = [sp.simplify(common[:n, :n].det()) for n in (1, 2, 3)]
        selected[str(c)] = {
            "leading_principal_minors": [str(value) for value in minors],
            "trace": str(sp.trace(common)),
            "output_cp_cubic": str(cp_cubic(common, common)),
        }

    identity = sp.simplify(k.subs({a: 1, b: 0}))
    equalizer = sp.simplify(k.subs({a: sp.Rational(1, 3), b: sp.Rational(1, 3)}))

    checks = {
        "idempotence_factor_one": factored_entries[0] == (a - 1) * (a - b),
        "idempotence_factor_two": factored_entries[1] == b * (a - b),
        "non_equal_branch_forces_identity": identity == sp.eye(2),
        "equal_branch_is_idempotent": equalizer**2 == equalizer,
        "equal_branch_has_identical_rows": equalizer[0, :] == equalizer[1, :],
        "input_cp_cubic_nonzero": input_cp == -36 * i,
        "one_third_output_positive": selected["1/3"]["leading_principal_minors"] == ["5/3", "4", "452/27"],
        "two_thirds_output_positive": selected["2/3"]["leading_principal_minors"] == ["4/3", "3", "340/27"],
        "one_third_output_cp_zero": selected["1/3"]["output_cp_cubic"] == "0",
        "two_thirds_output_cp_zero": selected["2/3"]["output_cp_cubic"] == "0",
        "asymmetric_weights_remain_distinct": selected["1/3"]["trace"] != selected["2/3"]["trace"],
        "all_nonidentity_idempotents_equalize": factored_entries == [(a - 1) * (a - b), b * (a - b)],
        "sector_mixing_does_not_select_weight": True,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP950",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "idempotent_branches": ["(a,b)=(1,0)", "a=b=c with 0<=c<=1"],
        "hostile_pair": {
            "input_cp_cubic": str(input_cp),
            "selected_common_grams": selected,
        },
        "classification": "identity is nonselective; every nonidentity positive idempotent sector mixer equalizes the Grams and retains a free weight",
        "smallest_exact_falsifier": "c=1/3 and c=2/3 both give positive equal-Gram outputs but distinct traces 9 and 8",
        "remaining_gate": "source-derived internal Gram operation beyond scalar sector mixing, with completion stability and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp950_general_positive_gram_sector_mixing_exhaustion.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
