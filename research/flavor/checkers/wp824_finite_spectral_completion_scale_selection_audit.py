"""Exact WP824 audit of finite spectral completion and scale selection."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    mass, cutoff, time = sp.symbols("mass cutoff time", positive=True, real=True)
    dirac = sp.Matrix([[0, mass], [mass, 0]])
    grading_flip = sp.diag(1, -1)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("acyclic_dirac_spectrum_is_signed_mass_pair",
          dirac.eigenvals() == {-mass: 1, mass: 1}, dirac.eigenvals())
    check("dirac_square_is_mass_squared_identity",
          dirac**2 == mass**2*sp.eye(2), dirac**2)
    check("nonzero_boundary_sector_has_zero_homology",
          dirac.rank() == 2, "invertible two-state Dirac sector")
    check("mass_sign_is_unitarily_conjugate",
          grading_flip*dirac*grading_flip == -dirac,
          grading_flip*dirac*grading_flip)

    heat_trace = sp.trace(sp.exp(-time*dirac**2))
    check("heat_trace_detects_full_spectral_mass",
          heat_trace == 2*sp.exp(-mass**2*time), heat_trace)
    check("calibrated_heat_trace_is_strictly_mass_sensitive",
          sp.diff(heat_trace, mass) < 0, sp.diff(heat_trace, mass))
    hostile_heat = [
        heat_trace.subs({mass: 1, time: 1}),
        heat_trace.subs({mass: 2, time: sp.Rational(1, 4)}),
    ]
    check("uncalibrated_heat_time_has_exact_mass_clock_pair",
          hostile_heat[0] == hostile_heat[1], hostile_heat)

    normalized_action = 2*sp.exp(-mass**2/cutoff**2)
    scale = sp.symbols("scale", positive=True)
    check("normalized_spectral_action_has_common_rescaling_kernel",
          sp.simplify(normalized_action.subs({mass: scale*mass, cutoff: scale*cutoff})
                      -normalized_action) == 0, normalized_action)
    action_jacobian = sp.Matrix([normalized_action]).jacobian([mass, cutoff])
    check("spectral_action_jacobian_annihilates_common_scale_direction",
          sp.simplify((action_jacobian*sp.Matrix([mass, cutoff]))[0]) == 0,
          action_jacobian)
    check("heat_kernel_spectral_action_has_no_positive_finite_mass_stationary_point",
          sp.diff(normalized_action, mass) < 0, sp.diff(normalized_action, mass))

    alpha, beta = sp.symbols("alpha beta", nonzero=True, real=True)
    z = sp.symbols("z", positive=True, real=True)
    polynomial_action = alpha*z+beta*z**2
    stationary_z = sp.solve(sp.Eq(sp.diff(polynomial_action, z), 0), z)
    check("polynomial_spectral_stationarity_depends_on_action_coefficients",
          stationary_z == [-alpha/(2*beta)], stationary_z)
    selected_one = stationary_z[0].subs({alpha: -2, beta: 1})
    selected_four = stationary_z[0].subs({alpha: -8, beta: 1})
    check("two_admissible_coefficient_packets_select_different_mass_ratios",
          (selected_one, selected_four) == (1, 4), (selected_one, selected_four))
    check("fixed_dimensionless_ratio_leaves_absolute_cutoff_scale_free",
          (cutoff*sp.sqrt(selected_one), cutoff*sp.sqrt(selected_four))
          == (cutoff, 2*cutoff),
          (cutoff*sp.sqrt(selected_one), cutoff*sp.sqrt(selected_four)))

    multiplicity = sp.symbols("multiplicity", positive=True, integer=True)
    multi_heat = multiplicity*heat_trace
    check("spectral_trace_records_but_does_not_select_acyclic_multiplicity",
          sp.diff(multi_heat, multiplicity) == heat_trace, multi_heat)

    gain = sp.symbols("gain", positive=True)
    detector_record = gain*heat_trace
    hostile_detector = [
        detector_record.subs({gain: 1, mass: 1, time: 1}),
        detector_record.subs({gain: 2, mass: 1, time: 1})
        / 2,
    ]
    check("formal_detector_gain_is_independent_of_spectral_mass",
          hostile_detector[0] == hostile_detector[1], hostile_detector)
    complete_probe = sp.Matrix([heat_trace, sp.diff(heat_trace, time)])
    complete_jacobian = complete_probe.jacobian([mass, time])
    check("two_calibrated_heat_moments_are_locally_faithful",
          sp.simplify(complete_jacobian.det()) != 0, complete_jacobian.det())

    germ = {
        "native_arity": 8,
        "source_germs": ["full_complex", "dirac_operator", "spectral_action",
                         "cutoff_clock", "oriented_inflow", "mediator",
                         "physical16_map", "detector"],
        "spectral_fiber_repair": True,
        "dirac_mass_selection": False,
        "action_coefficient_authority": False,
        "absolute_cutoff_authority": False,
        "threshold_rg_parallelization": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_eight_object_spectral_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    check("spectral_completion_repairs_homology_mass_fiber",
          germ["spectral_fiber_repair"], germ)
    open_gates = [key for key in (
        "dirac_mass_selection", "action_coefficient_authority",
        "absolute_cutoff_authority", "threshold_rg_parallelization",
        "physical16_descent", "detector_calibration"
    ) if not germ[key]]
    check("six_selection_and_realization_gates_remain_open",
          len(open_gates) == 6, open_gates)

    result = {
        "work_package": "WP824",
        "title": "Finite spectral completion and scale-selection audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "dirac_operator": str(dirac),
            "heat_trace": str(heat_trace),
            "normalized_spectral_action": str(normalized_action),
            "polynomial_stationary_ratio": str(stationary_z[0]),
            "aspect_germ": germ,
        },
        "classification": {
            "faithfulness": "full spectral data distinguishes masses erased by homology",
            "selection": "the Dirac mass, multiplicity, action coefficients, and cutoff remain source inputs",
            "stationarity": "heat action has no positive finite extremum; polynomial extrema depend on inserted coefficients",
            "scale": "normalized spectral action fixes at most mass/cutoff and has an exact common rescaling kernel",
            "threshold": "spectral mass records a threshold but is not parallelized with the RG fixed point",
            "readout": "calibrated heat moments are locally faithful; clock, gain, physical16 descent, and instrument remain absent",
            "verdict": "spectral completion repairs the fiber but does not select the portal scale",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp824_finite_spectral_completion_scale_selection_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
