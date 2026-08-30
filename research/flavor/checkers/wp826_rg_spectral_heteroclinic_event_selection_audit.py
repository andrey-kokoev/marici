"""Exact WP826 audit of an RG-spectral heteroclinic event selector."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    t = sp.symbols("t", real=True)
    modulus = sp.symbols("modulus", positive=True, real=True)
    trajectory = 1/(1+modulus*sp.exp(-t))
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("heteroclinic_solves_autonomous_logistic_rg",
          sp.simplify(sp.diff(trajectory, t)-trajectory*(1-trajectory)) == 0,
          sp.diff(trajectory, t))
    check("heteroclinic_has_uv_ir_endpoint_limits",
          sp.limit(trajectory, t, -sp.oo) == 0
          and sp.limit(trajectory, t, sp.oo) == 1,
          (sp.limit(trajectory, t, -sp.oo), sp.limit(trajectory, t, sp.oo)))
    check("open_interval_is_monotone_basin",
          sp.diff(trajectory, t) > 0, sp.diff(trajectory, t))

    criterion = sp.symbols("criterion", positive=True, real=True)
    crossing_time = sp.log(modulus*criterion/(1-criterion))
    check("general_threshold_crossing_time_is_exact",
          sp.simplify(trajectory.subs(t, crossing_time)-criterion) == 0,
          crossing_time)
    half_crossing = sp.simplify(crossing_time.subs(criterion, sp.Rational(1, 2)))
    check("symmetric_half_threshold_crosses_at_log_modulus",
          half_crossing == sp.log(modulus), half_crossing)
    spectral_path = trajectory-sp.Rational(1, 2)
    crossing_slope = sp.simplify(sp.diff(spectral_path, t).subs(t, half_crossing))
    check("spectral_crossing_is_positive_and_transverse",
          crossing_slope == sp.Rational(1, 4), crossing_slope)
    check("symmetric_spectral_event_fixes_dimensionless_portal_half",
          trajectory.subs(t, half_crossing) == sp.Rational(1, 2),
          trajectory.subs(t, half_crossing))

    shift = sp.symbols("shift", real=True)
    translated = sp.simplify(trajectory.subs(t, t+shift))
    shifted_modulus_trajectory = trajectory.subs(modulus, modulus*sp.exp(-shift))
    check("autonomous_time_translation_moves_modulus",
          sp.simplify(translated-shifted_modulus_trajectory) == 0,
          translated)
    check("all_positive_moduli_obey_same_global_endpoint_regularity",
          sp.limit(trajectory, t, -sp.oo) == 0
          and sp.limit(trajectory, t, sp.oo) == 1,
          "endpoint conditions independent of modulus")

    initial_value = sp.symbols("initial_value", positive=True, real=True)
    boundary_modulus = (1-initial_value)/initial_value
    check("modulus_is_equivalent_to_one_boundary_value",
          sp.simplify(trajectory.subs({t: 0, modulus: boundary_modulus})
                      -initial_value) == 0,
          boundary_modulus)

    reference_scale = sp.symbols("reference_scale", positive=True)
    crossing_scale = sp.simplify(reference_scale*sp.exp(half_crossing))
    check("physical_crossing_scale_retains_translation_modulus",
          crossing_scale == reference_scale*modulus, crossing_scale)
    check("two_global_trajectories_have_different_threshold_scales",
          crossing_scale.subs(modulus, 1) != crossing_scale.subs(modulus, 2),
          (crossing_scale.subs(modulus, 1), crossing_scale.subs(modulus, 2)))

    shifted_criterion_time = sp.simplify(
        crossing_time.subs(criterion, sp.Rational(3, 4)))
    check("threshold_criterion_shift_moves_event_without_changing_orientation",
          sp.simplify(sp.expand_log(
              shifted_criterion_time-half_crossing, force=True)-sp.log(3)) == 0,
          sp.expand_log(shifted_criterion_time-half_crossing, force=True))
    shifted_slope = sp.simplify(
        sp.diff(trajectory-criterion, t).subs(t, crossing_time)
        .subs(criterion, sp.Rational(3, 4)))
    check("shifted_threshold_crossing_remains_positive",
          shifted_slope == sp.Rational(3, 16), shifted_slope)

    # Fixing u(0)=1/2 sets the modulus only after adding a reference-clock
    # condition; it is not implied by endpoint regularity.
    check("reference_clock_condition_sets_modulus_to_one",
          sp.solve(sp.Eq(trajectory.subs(t, 0), sp.Rational(1, 2)), modulus) == [1],
          sp.solve(sp.Eq(trajectory.subs(t, 0), sp.Rational(1, 2)), modulus))

    gain = sp.symbols("gain", positive=True)
    record = gain*crossing_scale
    hostile_record = [
        record.subs({gain: 2, modulus: 1}),
        record.subs({gain: 1, modulus: 2}),
    ]
    check("uncalibrated_event_record_has_modulus_gain_pair",
          hostile_record[0] == hostile_record[1], hostile_record)
    check("event_record_is_rank_one_on_modulus_gain_domain",
          sp.Matrix([record]).jacobian([modulus, gain]).rank() == 1,
          "rank one")

    germ = {
        "native_arity": 9,
        "source_germs": ["oriented_bulk", "rg_vector_field", "spectral_function",
                         "global_endpoint_contract", "reference_clock", "mediator",
                         "threshold_event", "physical16_map", "detector"],
        "orientation_selection": True,
        "dimensionless_magnitude_selection": True,
        "global_open_basin": True,
        "trajectory_phase_selection": False,
        "absolute_event_scale": False,
        "threshold_criterion_authority": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_nine_object_event_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    open_gates = [key for key in (
        "trajectory_phase_selection", "absolute_event_scale",
        "threshold_criterion_authority", "physical16_descent",
        "detector_calibration"
    ) if not germ[key]]
    check("five_event_scale_and_realization_gates_remain_open",
          len(open_gates) == 5, open_gates)

    result = {
        "work_package": "WP826",
        "title": "RG-spectral heteroclinic event-selection audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "trajectory": str(trajectory),
            "half_crossing_time": str(half_crossing),
            "crossing_scale": str(crossing_scale),
            "crossing_slope": str(crossing_slope),
            "aspect_germ": germ,
        },
        "classification": {
            "source_dynamics": "autonomous logistic RG identifies the spectral path with one global heteroclinic orbit",
            "sign": "oriented transverse crossing is positive",
            "dimensionless_magnitude": "symmetric spectral zero fixes u=1/2 conditionally",
            "basin": "the entire open interval flows monotonically from 0 to 1",
            "remaining_modulus": "autonomous time translation moves the physical crossing scale",
            "threshold": "criterion shifts move event scale without changing orientation",
            "readout": "a reference clock can fix the modulus relationally; physical16 descent and detector calibration are absent",
            "verdict": "trajectory coupling closes orientation, dimensionless magnitude, and basin, but not absolute event scale",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp826_rg_spectral_heteroclinic_event_selection_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
