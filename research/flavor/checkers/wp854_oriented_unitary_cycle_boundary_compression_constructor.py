"""Exact WP854 audit of an oriented unitary-cycle boundary constructor."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    I = sp.eye(4)
    projectors = [sp.diag(*[int(i == j) for i in range(4)]) for j in range(4)]
    P0, P3 = projectors[0], projectors[3]
    U = sp.zeros(4)
    for j in range(4):
        U[(j+1) % 4, j] = 1
    C_left = (I-P0)*U
    C_right = U*(I-P3)
    reverse = (I-P3)*U.T
    current = C_left.T*C_left-C_left*C_left.T
    reverse_current = reverse.T*reverse-reverse*reverse.T
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("closed_cycle_is_lossless_unitary", U.T*U == I and U*U.T == I, U)
    check("left_and_right_boundary_compressions_agree", C_left == C_right, C_left)
    check("compression_derives_initial_projection", C_left.T*C_left == I-P3,
          C_left.T*C_left)
    check("compression_derives_final_projection", C_left*C_left.T == I-P0,
          C_left*C_left.T)
    check("compression_derives_finite_path_nilpotence", C_left**4 == sp.zeros(4),
          C_left**4)
    check("boundary_current_is_oriented_endpoint_difference", current == P0-P3, current)
    check("reversed_cycle_reverses_boundary_current", reverse_current == -current,
          reverse_current)
    check("boundary_defects_are_rank_one",
          (I-C_left.T*C_left).rank() == 1 and (I-C_left*C_left.T).rank() == 1,
          ((I-C_left.T*C_left).rank(), (I-C_left*C_left.T).rank()))
    check("surviving_nonzero_singular_values_are_unit",
          (C_left.T*C_left).eigenvals() == {1: 3, 0: 1},
          (C_left.T*C_left).eigenvals())
    check("uncompressed_cycle_has_no_boundary_current",
          U.T*U-U*U.T == sp.zeros(4), U.T*U-U*U.T)

    result = {
        "work_package": "WP854",
        "title": "Oriented unitary cycle boundary-compression constructor",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_operation": "remove the directed return port e3->e0 from a lossless four-cycle",
        "derived_open_transport": "C=(I-P0)U=U(I-P3)",
        "relative_sign": "J=P0-P3; reversed cycle and port give -J",
        "dimensionless_magnitude": "three surviving singular values and the defect projection have unit normalization",
        "groupoid_change": "closed cyclic transport -> stabilizer of marked source and sink projections",
        "classification": "conditional source-generated relational selector and normalizer",
        "remaining_gates": ["derive the flavor cycle and boundary microscopically",
                            "map defect current to normalized g_n-g_m",
                            "derive RG basin", "intertwine marked ports through thresholds",
                            "calibrate physical16 instrument"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp854_oriented_unitary_cycle_boundary_compression_constructor.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
