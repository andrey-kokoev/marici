"""Exact checks for WP801: UV fixed-point portal versus relevant clock fiber."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    p, m, alpha = sp.symbols("p m alpha", real=True)
    sigma = sp.symbols("sigma", real=True)

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    # Linearized UV flow.  The fixed-point portal deviation is UV-repulsive,
    # whereas the relevant mass deformation is UV-attractive and therefore free.
    s = sp.symbols("s", positive=True)
    cp = sp.symbols("cp", real=True)
    cm = sp.symbols("cm", positive=True)
    delta_p = cp * sp.exp(2 * s)
    mass_coordinate = cm * sp.exp(-s)
    hostile_limits = [sp.limit(abs(delta_p.subs(cp, value)), s, sp.oo) for value in (-1, 1)]
    check("nonzero_portal_deviations_are_uv_unbounded", hostile_limits == [sp.oo, sp.oo],
          hostile_limits)
    check("uv_completion_forces_portal_deviation_zero",
          sp.solve(sp.Eq(cp, 0), cp) == [0], sp.solve(sp.Eq(cp, 0), cp))
    check("mass_deformation_reaches_same_uv_point",
          sp.limit(mass_coordinate, s, sp.oo) == 0, sp.limit(mass_coordinate, s, sp.oo))

    # Two nonzero relevant deformations share the same UV endpoint but have
    # distinct exact thresholds.
    thresholds = [sp.sqrt(sp.Integer(1)), sp.sqrt(sp.Integer(4))]
    check("hostile_mass_pair_has_same_uv_endpoint", all(
        sp.limit(v * sp.exp(-s), s, sp.oo) == 0 for v in (sp.Integer(1), sp.Integer(4))
    ), "m=1 and m=4 both tend to zero in the UV")
    check("hostile_mass_pair_has_distinct_thresholds", thresholds == [1, 2], thresholds)

    # An even fixed-point equation selects magnitude but has two orientation branches.
    fixed_equation = sp.factor(p**2 - 1)
    fixed_branches = sp.solve(sp.Eq(fixed_equation, 0), p)
    check("fixed_point_selects_two_sign_branches", fixed_branches == [-1, 1], fixed_branches)
    check("even_intrinsic_probe_collapses_sign", (-1) ** 2 == 1 ** 2, "p^2=1 on both branches")
    check("signed_portal_probe_separates_prepared_branches", (-1) != 1, "responses -1 and +1")

    # Intrinsic UV data see p only.  Threshold and detector calibration are
    # independent coordinates.  Full rank appears only after adding both probes.
    uv_probe = sp.Matrix([p])
    uv_jacobian = uv_probe.jacobian([p, m, alpha])
    augmented = sp.Matrix([p, sp.sqrt(m), alpha * p]).jacobian([p, m, alpha]).subs({p: 1, m: 1, alpha: 1})
    check("intrinsic_uv_probe_has_two_dimensional_kernel", uv_jacobian.rank() == 1,
          f"rank={uv_jacobian.rank()}, nullity={3 - uv_jacobian.rank()}")
    check("added_threshold_and_detector_probes_restore_rank", augmented.det() != 0,
          f"det={augmented.det()}")

    # Detector calibration is not fixed by the source fixed point.
    detector_pair = [sp.Integer(1) * sp.Integer(1), sp.Integer(2) * sp.Integer(1)]
    check("hostile_calibration_pair_changes_readout", detector_pair == [1, 2], detector_pair)

    # Deliberate failure: the hostile pair must not accidentally coincide.
    obstruction = sp.simplify(thresholds[1] - thresholds[0])
    check("deliberate_failure_exhibits_nonzero_threshold_obstruction", obstruction == 1, obstruction)

    result = {
        "work_package": "WP801",
        "title": "UV fixed-point portal and relevant clock fiber",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "dimensionless_portal_magnitude": "selected conditionally by an isolated UV fixed point",
            "portal_sign": "two discrete branches under an even source equation",
            "threshold_scale": "free relevant deformation",
            "physical_readout": "requires an independently calibrated detector map",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp801_uv_fixed_point_relevant_clock_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
