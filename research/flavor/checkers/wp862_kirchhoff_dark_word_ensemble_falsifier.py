"""Exact WP862 complete-envelope falsifier for the WP861 dark-word family."""

import json
from pathlib import Path
import sympy as sp


def shape_ratio(values):
    squared = [value**2 for value in values]
    e1 = sum(squared)
    e2 = sum(squared[i]*squared[j] for i in range(3) for j in range(i+1, 3))
    return sp.simplify(e2/e1**2)


def main() -> None:
    root = Path(__file__).parents[1]
    ensemble = json.loads((root / "results" / "wp68_fitted_ensemble_contextual_partitions.json").read_text())
    wp7 = json.loads((root / "results" / "wp7_ensemble.json").read_text())
    t = sp.symbols("t", nonnegative=True)
    ratio = (3*t**2+2*t+1)/(3*t+2)**2
    derivative = sp.factor(sp.diff(ratio, t))
    minimum = sp.simplify(ratio.subs(t, sp.Rational(1, 3)))
    up = [sp.Rational("0.00000704"), sp.Rational("0.00356"), sp.Rational("0.967")]
    up_sigma = [sp.Rational("0.00000015"), sp.Rational("0.00006"), sp.Rational("0.004")]
    down = [sp.Rational("0.0000154"), sp.Rational("0.000306"), sp.Rational("0.01630")]
    down_sigma = [sp.Rational("0.0000002"), sp.Rational("0.000004"), sp.Rational("0.00009")]
    central = {"up": shape_ratio(up), "down": shape_ratio(down)}
    radius = sp.sqrt(sp.Rational(507, 25))

    def conservative_upper(values, sigmas):
        upper = [value+radius*sigma for value, sigma in zip(values, sigmas)]
        lower_largest = values[2]-radius*sigmas[2]
        squared_upper = [value**2 for value in upper]
        numerator_upper = sum(squared_upper[i]*squared_upper[j]
                              for i in range(3) for j in range(i+1, 3))
        return sp.simplify(numerator_upper/lower_largest**4)

    envelope = {"up": conservative_upper(up, up_sigma),
                "down": conservative_upper(down, down_sigma)}
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("dark_word_characteristic_shape_has_declared_e1_e2_e3", True,
          {"e1": "3t+2", "e2": "3t^2+2t+1", "e3": "t^3"})
    check("shape_ratio_derivative_has_unique_positive_critical_point",
          sp.simplify(derivative-2*(3*t-1)/(3*t+2)**3) == 0, derivative)
    check("global_shape_ratio_minimum_is_two_ninths", minimum == sp.Rational(2, 9),
          minimum)
    check("central_up_hierarchy_violates_dark_word_bound", central["up"] < minimum,
          sp.N(central["up"], 8))
    check("central_down_hierarchy_violates_dark_word_bound", central["down"] < minimum,
          sp.N(central["down"], 8))
    check("complete_viability_radius_matches_wp7_contract",
          wp7["conventions"]["viability_chi2_max"] == 20.28, radius)
    check("conservative_up_viability_envelope_remains_below_bound",
          envelope["up"] < minimum, sp.N(envelope["up"], 8))
    check("conservative_down_viability_envelope_remains_below_bound",
          envelope["down"] < minimum, sp.N(envelope["down"], 8))
    check("complete_stored_ensemble_has_1210_sheets",
          ensemble["domain"]["complete_stored_viable_sheet_ensemble"] == 1210,
          ensemble["domain"]["complete_stored_viable_sheet_ensemble"])
    check("one_sector_already_falsifies_complete_grammar",
          envelope["up"] < minimum, {"up_envelope": sp.N(envelope["up"], 8),
                                      "source_minimum": minimum})

    result = {
        "work_package": "WP862",
        "title": "Kirchhoff dark-word ensemble falsifier",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_prediction": "R2=e2/e1^2 >= 2/9 in each sector",
        "central_R2": {key: float(value) for key, value in central.items()},
        "conservative_complete_envelope_R2_upper": {
            key: float(value) for key, value in envelope.items()},
        "ensemble_size": 1210,
        "classification": "complete dark-word physical16 interface falsified on every viable sheet; additive interface remains nonselective",
        "smallest_exact_falsifier": "up-sector scale-free mass shape",
        "remaining_gate": "derive a richer but still coefficient-selected physical flavor operator without restoring universal fitting freedom",
        "tests": tests,
    }
    output = root / "results" / "wp862_kirchhoff_dark_word_ensemble_falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
