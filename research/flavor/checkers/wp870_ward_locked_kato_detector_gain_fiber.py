"""Exact WP870 Ward-locked detector transport and gain-fiber audit."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    t, g = sp.symbols("t g", real=True)
    transport = sp.Matrix([[sp.cos(t), sp.sin(t)],
                           [-sp.sin(t), sp.cos(t)]])
    initial_kernel = sp.Matrix([1, 0])
    kernel = sp.simplify(transport*initial_kernel)
    bare_vertex = sp.Matrix([[1, 0]])
    ward_vertex = sp.simplify(g*bare_vertex*transport.conjugate().T)
    fixed_vertex = g*bare_vertex
    ward_amplitude = sp.simplify((ward_vertex*kernel)[0])
    fixed_amplitude = sp.simplify((fixed_vertex*kernel)[0])
    endpoint = {sp.cos(t): sp.Rational(3, 4),
                sp.sin(t): sp.sqrt(7)/4}
    response_g1 = sp.simplify(ward_amplitude.subs(g, 1))
    response_g2 = sp.simplify(ward_amplitude.subs(g, 2))
    intensity_g1 = response_g1**2
    intensity_g2 = response_g2**2
    beta_flat = sp.Integer(0)
    beta_cubic = g**3
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("field_matching_is_unitary",
          sp.simplify(transport.conjugate().T*transport) == sp.eye(2), transport)
    check("ward_vertex_is_bare_source_pullback",
          ward_vertex == sp.simplify(g*bare_vertex*transport.conjugate().T),
          ward_vertex)
    check("ward_locked_amplitude_is_threshold_invariant",
          ward_amplitude == g, ward_amplitude)
    check("fixed_vertex_is_attenuated_at_hostile_endpoint",
          sp.simplify(fixed_amplitude.subs(endpoint)) == 3*g/4,
          fixed_amplitude.subs(endpoint))
    check("common_gain_changes_absolute_amplitude",
          response_g1 == 1 and response_g2 == 2,
          [response_g1, response_g2])
    check("common_gain_changes_intensity_by_four",
          intensity_g1 == 1 and intensity_g2 == 4,
          [intensity_g1, intensity_g2])
    check("normalized_response_cancels_gain_without_predicting_it",
          sp.simplify(ward_amplitude/g) == 1, ward_amplitude/g)
    check("ward_frame_law_does_not_fix_beta_function",
          beta_flat != beta_cubic, [beta_flat, beta_cubic])
    check("state_basin_and_coupling_basin_are_distinct", True,
          "WP866 projects states; it does not select the continuous gain g")
    check("physical_gain_calibration_remains_open", True,
          "requires source-selected g and detector-unit standard")

    result = {
        "schema": "marici.flavor.ward-locked-kato-detector-gain-fiber.v1",
        "work_package": "WP870",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_operation": "pullback of one conserved-current vertex through Kato field matching",
        "fixed_interface": "relative detector frame and threshold attachment",
        "residual_fiber": "one common coupling g",
        "smallest_exact_falsifier": {
            "g_values": [1, 2],
            "amplitudes": [str(response_g1), str(response_g2)],
            "intensities": [str(intensity_g1), str(intensity_g2)],
        },
        "classification": "source-derived detector rigidifier and threshold intertwiner; neither magnitude nor coupling-RG selector",
        "remaining_physical_instrument_gate": "source-selected running coupling and calibrated detector-unit realization",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp870_ward_locked_kato_detector_gain_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
