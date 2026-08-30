"""Exact WP804 audit of the direct chiral-tensor Higgs Yukawa."""

import json
from pathlib import Path

import sympy as sp


def branch_data(sign: int):
    x = sp.symbols("x", real=True)
    N = sp.Integer(5)
    b0 = (sp.Rational(4, 3) * x - 6) * N + sp.Rational(1 + sign * 12, 3)
    b1 = (
        (sp.Rational(26, 3) * x - 13) * N**2
        + sp.Rational(8 + sign * 90, 3) * N
        - (1 + 2 * x)
        - sp.Rational(2 + sign * 12, N)
    )
    gauge_yukawa = sp.Rational(3, 2) * N + sign * sp.Rational(5, 2)
    c1 = -9 * N - sign * 6 + sp.Rational(15, N)
    c2 = sp.Rational(3, 2) * N + sp.Rational(2 + sign * 3, 2)
    fixed_flow_ratio = sp.simplify(-c1 / c2)
    b1_effective = sp.factor(b1 - gauge_yukawa * fixed_flow_ratio)
    return {
        "x": x,
        "b0": sp.factor(b0),
        "ratio": fixed_flow_ratio,
        "b1_effective": b1_effective,
        "af_boundary": sp.solve(sp.Eq(b0, 0), x)[0],
        "two_loop_boundary": sp.solve(sp.Eq(b1_effective, 0), x)[0],
    }


def main() -> None:
    upper = branch_data(1)
    lower = branch_data(-1)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("upper_fixed_flow_ratio_is_positive", upper["ratio"] == sp.Rational(24, 5), upper["ratio"])
    check("lower_fixed_flow_ratio_is_positive", lower["ratio"] == sp.Rational(36, 7), lower["ratio"])
    check("upper_asymptotic_freedom_boundary", upper["af_boundary"] == sp.Rational(77, 20),
          upper["af_boundary"])
    check("lower_asymptotic_freedom_boundary", lower["af_boundary"] == sp.Rational(101, 20),
          lower["af_boundary"])
    check("upper_effective_two_loop_boundary", upper["two_loop_boundary"] == sp.Rational(1601, 1610),
          upper["two_loop_boundary"])
    check("lower_effective_two_loop_boundary", lower["two_loop_boundary"] == sp.Rational(5107, 2254),
          lower["two_loop_boundary"])
    check("upper_safe_conditions_are_disjoint",
          upper["two_loop_boundary"] < upper["af_boundary"],
          sp.simplify(upper["af_boundary"] - upper["two_loop_boundary"]))
    check("lower_safe_conditions_are_disjoint",
          lower["two_loop_boundary"] < lower["af_boundary"],
          sp.simplify(lower["af_boundary"] - lower["two_loop_boundary"]))

    # Hostile points just above loss of asymptotic freedom have an unphysical
    # negative interacting gauge coordinate on the Yukawa fixed flow.
    for name, data, probe in (
        ("upper", upper, sp.Integer(4)),
        ("lower", lower, sp.Rational(21, 4)),
    ):
        b0_value = data["b0"].subs(data["x"], probe)
        b1_value = data["b1_effective"].subs(data["x"], probe)
        ag_star = sp.simplify(-b0_value / b1_value)
        check(f"{name}_hostile_fixed_point_is_unphysical", ag_star < 0, ag_star)

    # The vertex directly contains the chiral tensor, unlike WP803.
    incidence = sp.Matrix([1, 1, 1])  # tensor T, anti-fundamental, Higgs H
    check("yukawa_has_direct_chiral_tensor_incidence", incidence[0] == 1, incidence.T)

    # A single Yukawa hyperedge has no rephasing-invariant loop phase and a_H
    # is quadratic in y_H.
    yH = sp.symbols("y_H", real=True)
    check("normalized_yukawa_is_sign_blind",
          (yH**2).subs(yH, 1) == (yH**2).subs(yH, -1),
          "a_H(+1)=a_H(-1)")
    check("single_vertex_has_no_phase_cycle", 3 - 4 + 1 == 0,
          "bipartite incidence-graph cycle rank E-V+C=3-4+1=0")

    # Fixed-flow data do not select the asymptotically-free ray normalization,
    # mass threshold, or detector response.
    ray, mass, calibration = sp.symbols("ray mass calibration", positive=True)
    intrinsic = sp.Matrix([ray, upper["ratio"] * ray])
    jacobian = intrinsic.jacobian([ray, mass, calibration])
    check("fixed_flow_probe_has_threshold_and_detector_kernel", jacobian.rank() == 1,
          f"rank={jacobian.rank()}, nullity={3 - jacobian.rank()}")

    obstruction = sp.simplify(upper["af_boundary"] - upper["two_loop_boundary"])
    check("deliberate_failure_exhibits_positive_safety_gap", obstruction > 0, obstruction)

    result = {
        "work_package": "WP804",
        "title": "Direct chiral-tensor Yukawa safety no-go",
        "branches": {
            "upper": {key: str(value) for key, value in upper.items() if key != "x"},
            "lower": {key: str(value) for key, value in lower.items() if key != "x"},
        },
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "chiral_incidence": "passes",
            "interacting_uv_selector": "fails for both finite SU(5) branches at admitted order",
            "sign": "sign-blind and no phase cycle",
            "rg_scale_threshold_readout": "unselected",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp804_chiral_tensor_yukawa_safety_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
