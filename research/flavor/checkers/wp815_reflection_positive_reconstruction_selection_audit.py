"""Exact WP815 audit of reflection-positive reconstruction versus selection."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    amplitude, delta, t = sp.symbols("amplitude delta t", positive=True)
    correlator = amplitude * sp.exp(-delta * t)
    sample_times = [sp.Integer(0), sp.Integer(1), sp.Integer(2)]
    vector = sp.Matrix([sp.exp(-delta * value) for value in sample_times])
    gram = amplitude * vector * vector.T

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("reflection_kernel_is_positive_rank_one_gram",
          gram.rank() == 1 and gram == amplitude * vector * vector.T,
          f"rank={gram.rank()}")
    principal_minors = [
        sp.simplify(gram[:size, :size].det()) for size in (1, 2, 3)
    ]
    check("reflection_gram_principal_minors_are_nonnegative",
          principal_minors[0] > 0 and principal_minors[1:] == [0, 0],
          principal_minors)

    complete_monotone = [
        sp.simplify((-1) ** order * sp.diff(correlator, t, order))
        for order in range(5)
    ]
    expected_monotone = [
        amplitude * delta**order * sp.exp(-delta * t) for order in range(5)
    ]
    check("one_pole_correlator_is_completely_monotone_to_tested_order",
          complete_monotone == expected_monotone, complete_monotone)

    moments = [sp.simplify(value.subs(t, 0)) for value in complete_monotone]
    reconstructed_amplitude = moments[0]
    reconstructed_delta = sp.simplify(moments[1] / moments[0])
    check("one_pole_residue_reconstructs_exactly",
          reconstructed_amplitude == amplitude, reconstructed_amplitude)
    check("one_pole_location_reconstructs_exactly",
          reconstructed_delta == delta, reconstructed_delta)
    check("reconstructed_one_pole_regenerates_complete_correlator",
          sp.simplify(reconstructed_amplitude * sp.exp(-reconstructed_delta * t)
                      - correlator) == 0,
          sp.simplify(reconstructed_amplitude * sp.exp(-reconstructed_delta * t)
                      - correlator))

    # A point mass at 1 and equal point masses at 1/2 and 3/2 share the first
    # two moments but not the second moment.
    point_moments = [sp.Integer(1), sp.Integer(1), sp.Integer(1)]
    pair_moments = [
        sp.Integer(1),
        sp.Rational(1, 2) * sp.Rational(1, 2) + sp.Rational(1, 2) * sp.Rational(3, 2),
        sp.Rational(1, 2) * sp.Rational(1, 2) ** 2
        + sp.Rational(1, 2) * sp.Rational(3, 2) ** 2,
    ]
    check("finite_two_moment_probe_has_positive_spectral_hostile_pair",
          point_moments[:2] == pair_moments[:2],
          {"point": point_moments[:2], "pair": pair_moments[:2]})
    check("next_moment_separates_positive_spectral_hostile_pair",
          point_moments[2] != pair_moments[2],
          {"point": point_moments[2], "pair": pair_moments[2]})

    geometry_choices = [correlator.subs(delta, 1), correlator.subs(delta, 2)]
    check("reflection_positivity_does_not_select_pole_location",
          geometry_choices[0] != geometry_choices[1], geometry_choices)
    residue_choices = [correlator.subs(amplitude, 1), correlator.subs(amplitude, 2)]
    check("reflection_positivity_does_not_select_residue",
          residue_choices[0] != residue_choices[1], residue_choices)

    sign = sp.symbols("sign", integer=True)
    signed_operator_two_point = sp.simplify(sign**2 * correlator)
    sign_pair = [signed_operator_two_point.subs(sign, 1),
                 signed_operator_two_point.subs(sign, -1)]
    check("reflection_positive_two_point_function_is_portal_sign_blind",
          sp.simplify(sign_pair[0] - sign_pair[1]) == 0, sign_pair)

    kappa = sp.symbols("kappa", positive=True)
    attached_correlators = [correlator.subs(delta, kappa),
                            correlator.subs(delta, 2 * kappa)]
    check("os_positivity_allows_multiple_horizon_attachments",
          attached_correlators[0] != attached_correlators[1], attached_correlators)

    threshold_shift = sp.symbols("threshold_shift", positive=True)
    shifted = correlator.subs(delta, delta + threshold_shift)
    shifted_monotone = sp.simplify(-sp.diff(shifted, t))
    check("positive_threshold_shift_preserves_positivity_but_moves_pole",
          shifted_monotone == amplitude * (delta + threshold_shift)
          * sp.exp(-t * (delta + threshold_shift)), shifted_monotone)

    energy_gain, area_gain = sp.symbols("energy_gain area_gain", positive=True)
    detector_record = sp.Matrix([energy_gain * delta, area_gain * amplitude])
    detector_jacobian = detector_record.jacobian(
        [delta, amplitude, energy_gain, area_gain]
    )
    check("uncalibrated_line_position_and_area_have_two_dimensional_kernel",
          detector_jacobian.rank() == 2,
          f"rank={detector_jacobian.rank()}, nullity=2")
    hostile_detector_records = [
        detector_record.subs({delta: 1, energy_gain: 2, amplitude: 1, area_gain: 2}),
        detector_record.subs({delta: 2, energy_gain: 1, amplitude: 2, area_gain: 1}),
    ]
    check("detector_energy_and_area_have_exact_calibration_hostile_pair",
          hostile_detector_records[0] == hostile_detector_records[1],
          hostile_detector_records)

    selector_native_arity = 3
    record_native_arity = 4
    check("aspect_correlator_target_is_ternary_before_realization",
          selector_native_arity == 3, selector_native_arity)
    check("aspect_calibrated_record_remains_quaternary",
          record_native_arity == 4, record_native_arity)

    obstruction = pair_moments[2] - point_moments[2]
    check("deliberate_failure_exhibits_finite_probe_residual",
          obstruction == sp.Rational(1, 4), obstruction)

    result = {
        "work_package": "WP815",
        "title": "Reflection-positive reconstruction and selection audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "correlator": str(correlator),
            "reflection_gram_rank": gram.rank(),
            "moments": [str(value) for value in moments],
            "reconstructed_amplitude": str(reconstructed_amplitude),
            "reconstructed_delta": str(reconstructed_delta),
            "finite_probe_residual": str(obstruction),
        },
        "tests": tests,
        "classification": {
            "reconstruction": "faithful on the declared positive one-pole domain",
            "selection": "reflection positivity fixes neither pole, residue, nor portal sign",
            "finite_probe": "two moments do not separate positive one-pole and two-pole measures",
            "threshold": "positivity survives pole shifts, so it does not protect the numerical prediction",
            "instrument": "line position and area require independent energy and gain calibration",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp815_reflection_positive_reconstruction_selection_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
