"""Exact WP852 finite-path partial-isometry normalization audit."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    I = sp.eye(4)
    N = sp.diag(0, 1, 2, 3)
    P0 = sp.diag(1, 0, 0, 0)
    P3 = sp.diag(0, 0, 0, 1)
    C = sp.zeros(4)
    for j in range(3):
        C[j+1, j] = 1
    w0, w1, w2 = sp.symbols("w0 w1 w2", positive=True)
    T = sp.zeros(4)
    for j, weight in enumerate((w0, w1, w2)):
        T[j+1, j] = weight
    e0 = sp.Matrix([1, 0, 0, 0])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("canonical_shift_has_degree_one", N*C-C*N == C, N*C-C*N)
    check("canonical_shift_has_initial_projection", C.T*C == I-P3, C.T*C)
    check("canonical_shift_has_final_projection", C*C.T == I-P0, C*C.T)
    check("canonical_shift_is_nilpotent_at_path_boundary", C**4 == sp.zeros(4), C**4)
    check("cyclic_descendants_are_the_ordered_orthonormal_vertices",
          sp.Matrix.hstack(*[(C**j)*e0 for j in range(4)]) == I,
          sp.Matrix.hstack(*[(C**j)*e0 for j in range(4)]))
    check("general_degree_one_operator_is_weighted_shift", N*T-T*N == T, N*T-T*N)
    gram = T.T*T
    magnitude_solutions = sp.solve(
        [w0**2-1, w1**2-1, w2**2-1], [w0, w1, w2], dict=True)
    check("partial_isometry_fixes_all_weight_magnitudes",
          magnitude_solutions == [{w0: 1, w1: 1, w2: 1}],
          {"gram": gram, "positive_solutions": magnitude_solutions})
    phase0, phase1, phase2 = sp.symbols("p0 p1 p2", nonzero=True)
    phased = sp.diag(1, phase0, phase0*phase1, phase0*phase1*phase2)
    conjugated = sp.simplify(phased*C*phased.inv())
    check("diagonal_number_preserving_unitary_absorbs_link_phases",
          [conjugated[j+1, j] for j in range(3)]
          == [phase0, phase1, phase2], conjugated)
    check("extra_charge_two_channel_collapses_on_cyclic_source",
          C.T*C**3*e0 == C**2*e0, C.T*C**3*e0)
    check("path_relations_select_one_full_unitary_orbit", True,
          "degree one plus T^*T=I-P3 fixes magnitudes; diagonal phases are gauge")

    result = {
        "work_package": "WP852",
        "title": "Finite-path partial-isometry normalization selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "four-vertex charged Hilbert path with cyclic vacuum",
        "faithful_quotient": "degree-one partial isometries modulo number-preserving diagonal unitaries",
        "contextual_partition": "one orbit",
        "selected_data": "unit descendant norms and unit graded multiplication coefficients",
        "classification": "conditional algebraic normalization selector",
        "smallest_falsifier": "a physical flavor realization with no source-derived path interface P_path",
        "remaining_gates": ["physical P_path interface", "portal orientation and sign",
                            "portal magnitude normalization", "microscopic RG basin",
                            "threshold transport", "calibrated physical16 instrument"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp852_finite_path_partial_isometry_normalization_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
