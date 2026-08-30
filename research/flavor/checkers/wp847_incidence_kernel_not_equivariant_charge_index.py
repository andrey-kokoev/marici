"""Exact WP847 audit separating kernel coefficients from equivariant weights."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    B = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    q = sp.Matrix([1, 2, 3])
    Q = sp.diag(1, 2, 3)
    a00, a01, a10, a11 = sp.symbols("a00 a01 a10 a11")
    A = sp.Matrix([[a00, a01], [a10, a11]])
    equations = list(A*B-B*Q)
    solution = sp.solve(equations, [a00, a01, a10, a11], dict=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("primitive_vector_is_incidence_kernel_coefficient",
          B*q == sp.zeros(2, 1), B*q)
    check("weight_operator_sends_kernel_vector_out_of_kernel",
          B*Q*q == sp.Matrix([-2, -6]), B*Q*q)
    check("kernel_line_is_not_charge_operator_invariant",
          Q*q != q and Q*q != 2*q and Q*q != 3*q, Q*q)
    check("no_target_generator_intertwines_incidence_and_charge_action",
          solution == [], solution)
    check("necessary_kernel_invariance_condition_fails",
          B*Q*q != sp.zeros(2, 1), B*Q*q)
    check("incidence_has_rank_two", B.rank() == 2, B.rank())
    check("incidence_kernel_dimension_is_one",
          len(B.nullspace()) == 1, len(B.nullspace()))
    check("incidence_cokernel_dimension_is_zero",
          B.rows-B.rank() == 0, B.rows-B.rank())
    ordinary_index = B.cols-B.rows
    check("ordinary_euler_index_is_one", ordinary_index == 1, ordinary_index)
    z = sp.symbols("z")
    proposed_character = z+z**2+z**3
    check("proposed_three_term_character_is_not_ordinary_index",
          proposed_character != ordinary_index, proposed_character)
    check("kernel_dimension_cannot_encode_three_label_support",
          len(B.nullspace()) == 1 and len([1, 2, 3]) == 3,
          (len(B.nullspace()), 3))
    check("wp846_character_requires_new_equivariant_source_object",
          solution == [] and B*Q*q != sp.zeros(2, 1),
          "kernel coefficients are not admitted representation weights")

    result = {
        "work_package": "WP847",
        "title": "Incidence kernel is not an equivariant charge index",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "incidence": "[[2,-1,0],[3,0,-1]]",
        "kernel_coefficient": "q=(1,2,3), Bq=0",
        "proposed_weight_operator": "Q=diag(1,2,3)",
        "equivariance_obstruction": "BQq=(-2,-6), so no A satisfies AB=BQ",
        "actual_index": "ordinary Euler index dim ker B-dim coker B=1",
        "classification": "negative source-interface theorem; WP820 incidence does not derive WP846 character",
        "smallest_exact_falsifier": "BQq=(-2,-6) != 0",
        "remaining_source_gate": "construct an independently authorized U(1)-equivariant complex whose index character retains the primitive charge support, then threshold sewing and holonomy instrumentation",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp847_incidence_kernel_not_equivariant_charge_index.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
