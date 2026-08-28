"""Exact WP833 test of operator-irreducible anomaly-neutral completion."""

import json
from pathlib import Path
import sympy as sp


def commutant_data(*operators: sp.Matrix):
    n = operators[0].rows
    symbols = sp.symbols(f"x0:{n*n}")
    X = sp.Matrix(n, n, symbols)
    equations = []
    for operator in operators:
        equations.extend(list(X*operator-operator*X))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, symbols)
    nullspace = coefficient_matrix.nullspace()
    return coefficient_matrix.rank(), [vector.reshape(n, n) for vector in nullspace]


def main() -> None:
    Q3 = sp.diag(1, 2, 3)
    D3 = sp.Matrix([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 2]])
    Q5 = sp.diag(1, 2, 3, 1, -1)
    D5 = sp.Matrix([[0, 1, 0, 0, 1],
                    [1, 1, 1, 0, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 1, 3, 1],
                    [1, 0, 0, 1, 4]])
    rank3, commutant3 = commutant_data(Q3, D3)
    rank5, commutant5 = commutant_data(Q5, D5)
    scale = sp.symbols("scale", positive=True, real=True)
    rank5_scaled, commutant5_scaled = commutant_data(Q5, scale*D5)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    linear3 = sum(Q3[i, i] for i in range(3))
    linear5 = sum(Q5[i, i] for i in range(5))
    cubic3 = sum(Q3[i, i]**3 for i in range(3))
    cubic5 = sum(Q5[i, i]**3 for i in range(5))
    check("vectorlike_completion_preserves_linear_charge_sum",
          linear3 == linear5 == 6, (linear3, linear5))
    check("vectorlike_completion_preserves_oriented_cubic_anomaly",
          cubic3 == cubic5 == 36, (cubic3, cubic5))
    index3 = sum(Q3[i, i]**2 for i in range(3))
    index5 = sum(Q5[i, i]**2 for i in range(5))
    check("vectorlike_completion_changes_current_spectral_index",
          index3 == 14 and index5 == 16, (index3, index5))
    check("primitive_portal_charge_contrast_is_retained",
          Q5[2, 2]-Q5[1, 1] == 1, Q5[2, 2]-Q5[1, 1])

    check("base_operator_packet_has_scalar_common_commutant",
          rank3 == 8 and len(commutant3) == 1
          and commutant3[0] == sp.eye(3),
          (rank3, commutant3))
    check("completed_operator_packet_has_scalar_common_commutant",
          rank5 == 24 and len(commutant5) == 1
          and commutant5[0] == sp.eye(5),
          (rank5, commutant5))
    check("completed_mixing_operator_is_nondegenerate",
          D5.det() == -18, D5.det())
    cross_block = D5[:3, 3:]
    check("added_pair_is_mixed_with_base_sector",
          any(value != 0 for value in cross_block), cross_block)
    check("scalar_commutant_irreducibility_survives_free_mass_scale",
          rank5_scaled == 24 and len(commutant5_scaled) == 1
          and commutant5_scaled[0] == sp.eye(5),
          (rank5_scaled, commutant5_scaled))
    check("spectral_scale_remains_continuous_under_irreducibility",
          sp.factor((scale*D5).det()) == -18*scale**5,
          sp.factor((scale*D5).det()))

    hostile_coupling = sp.sqrt(sp.Rational(7, 8))
    check("ward_response_fiber_survives_operator_irreducibility",
          index3 == index5*hostile_coupling**2,
          (index3, index5*hostile_coupling**2))
    check("irreducibility_does_not_select_completion_dimension",
          len(commutant3) == len(commutant5) == 1
          and Q3.rows != Q5.rows,
          (Q3.rows, Q5.rows))

    result = {
        "work_package": "WP833",
        "title": "Operator-irreducible vectorlike-completion no-go",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "operator_packets": {
            "base": {"charge": Q3.tolist(), "mixing": D3.tolist(),
                     "common_commutant_dimension": len(commutant3),
                     "current_index": index3},
            "completed": {"charge": Q5.tolist(), "mixing": D5.tolist(),
                          "common_commutant_dimension": len(commutant5),
                          "mixing_determinant": int(D5.det()),
                          "current_index": index5},
        },
        "classification": {
            "irreducibility_test": "the common commutant of charge and finite mixing operators consists only of scalars",
            "preserved": ["linear charge sum", "oriented cubic anomaly",
                          "primitive portal contrast", "scalar common commutant"],
            "not_selected": ["Hilbert-space dimension", "vectorlike completion",
                             "current spectral index", "finite spectral scale",
                             "threshold coupling"],
            "selector_or_rigidifier": "scalar-commutant irreducibility rejects internal reducing sectors but does not select among irreducible completions",
            "smallest_exact_falsifier": "the irreducible 3-state and irreducible 5-state packets have anomaly 36 and contrast one but indices 14 and 16",
        },
        "claim_boundary": "The displayed mixing is an exact finite operator packet. Full gauge covariance, real structure, grading, first-order condition, positivity, and a physical action are not established; the theorem only refutes scalar-common-commutant irreducibility by itself as a spectrum selector.",
        "remaining_source_gate": "a physical axiom must compare distinct irreducible completions and uniquely select dimension, representations, mixing spectrum, and scale before RG and threshold predictions follow",
        "tests": tests,
    }

    def native(value):
        if isinstance(value, sp.Integer):
            return int(value)
        if isinstance(value, list):
            return [native(item) for item in value]
        if isinstance(value, dict):
            return {key: native(item) for key, item in value.items()}
        return value

    result = native(result)
    output = Path(__file__).parents[1] / "results" / "wp833_operator_irreducible_vectorlike_completion_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
