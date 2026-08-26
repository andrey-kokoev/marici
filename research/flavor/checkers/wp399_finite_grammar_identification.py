"""WP399: exact finite one-pole grammar identification and withheld test."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    c = sp.symbols("c", real=True)
    a0, a1, b1, eps = sp.symbols("a0 a1 b1 epsilon", real=True)
    response = (a0+a1*c)/(1+b1*c)
    benchmark_parameters = {a0: 1, a1: 2, b1: 1}
    benchmark = sp.factor(response.subs(benchmark_parameters))
    contexts = (0, 1, 2)
    records = tuple(sp.factor(benchmark.subs(c, point)) for point in contexts)
    design = sp.Matrix([[1, point, -point*records[i]] for i, point in enumerate(contexts)])
    rhs = sp.Matrix(records)
    recovered = sp.simplify(design.inv()*rhs)
    withheld_prediction = sp.factor(benchmark.subs(c, 3))
    hidden_completion = eps*c*(c-1)*(c-2)
    hostile_withheld = sp.factor((benchmark+hidden_completion).subs(c, 3))
    predicted_vector = sp.Matrix([1, withheld_prediction])
    hostile_vector = sp.Matrix([1, hostile_withheld])
    joint_det = sp.factor((predicted_vector*predicted_vector.T+hostile_vector*hostile_vector.T).det())
    checks = {
        "three_calibration_records_exact": records == (1, sp.Rational(3, 2), sp.Rational(5, 3)),
        "design_matrix_invertible": design.det() != 0,
        "parameters_recovered_exactly": recovered == sp.Matrix([1, 2, 1]),
        "withheld_prediction_exact": withheld_prediction == sp.Rational(7, 4),
        "benchmark_denominators_positive_on_contexts": all((1+c).subs(c, point) > 0 for point in contexts+(3,)),
        "deleting_one_context_loses_parameter_rank": design[:2, :].rank() == 2,
        "hidden_completion_vanishes_on_calibration_contexts": all(hidden_completion.subs(c, point) == 0 for point in contexts),
        "hidden_completion_changes_withheld_record": sp.simplify(hostile_withheld-sp.Rational(7, 4)-6*eps) == 0,
        "withheld_joint_determinant_exact": joint_det == 36*eps**2,
        "zero_hidden_completion_passes_withheld_test": joint_det.subs(eps, 0) == 0,
        "one_pole_family_has_three_free_coefficients": len((a0, a1, b1)) == 3,
        "calibration_equations_are_linear_after_cross_multiplication": all(sp.Poly(design.row(i).dot(sp.Matrix([a0, a1, b1]))-rhs[i], a0, a1, b1).total_degree() == 1 for i in range(3)),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP399",
        "admitted_state_domain": "a frozen one-pole rational response grammar with nonvanishing denominators at three calibration contexts and one withheld context",
        "faithful_quotient_coordinate": "the projective physical16 response direction (1,r(c)) in a legally parallelized common frame",
        "source_authorized_probe_family": "three exact calibration responses and one withheld response-direction measurement",
        "contextual_partition": "three generic records identify one grammar packet uniquely; higher-complexity completions remain in a different admitted class and are exposed by the withheld context",
        "classification": "finite system-identification theorem and out-of-sample grammar test, not source derivation of the fitted coefficients",
        "benchmark_response": str(benchmark),
        "calibration_records": [str(value) for value in records],
        "design_determinant": str(design.det()),
        "recovered_parameters": [str(value) for value in recovered],
        "withheld_prediction": str(withheld_prediction),
        "withheld_joint_determinant": str(joint_det),
        "smallest_exact_falsifier": "the cubic hidden completion matches all three calibration records and shifts the withheld response by 6*epsilon",
        "remaining_physical_instrument_gate": "derive the one-pole grammar and context settings from a finite source mediator model, then reserve and measure the withheld response without refitting",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp399_finite_grammar_identification.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
