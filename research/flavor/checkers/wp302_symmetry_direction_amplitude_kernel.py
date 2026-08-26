"""WP302: exact symmetry-fixed direction with an unfixed selector amplitude."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    curvature, mixing, amplitude = sp.symbols("curvature mixing amplitude", positive=True)
    swap = sp.Matrix([[0, 1], [1, 0]])
    hessian = sp.Matrix([[curvature, mixing], [mixing, curvature]])
    source = amplitude * sp.Matrix([1, 1])
    selected = sp.simplify(hessian.inv() * source)
    expected = sp.Matrix([amplitude / (curvature + mixing)] * 2)
    antisymmetric = sp.Matrix([1, -1])
    symmetric = sp.Matrix([1, 1])

    packet_one = selected.subs({curvature: 2, mixing: 1, amplitude: 3})
    packet_two = selected.subs({curvature: 2, mixing: 1, amplitude: 6})
    zero_source = selected.subs(amplitude, 0)

    checks = {
        "hessian_eigenvalues_are_symmetric_and_antisymmetric_curvatures": set(hessian.eigenvals()) == {curvature + mixing, curvature - mixing},
        "hessian_commutes_with_swap": hessian * swap == swap * hessian,
        "source_is_swap_invariant": swap * source == source,
        "symmetric_direction_is_fixed": swap * symmetric == symmetric,
        "antisymmetric_direction_is_not_fixed": swap * antisymmetric == -antisymmetric,
        "selected_point_has_exact_symmetric_direction": selected == expected,
        "symmetry_forces_equal_components": sp.simplify(selected[0] - selected[1]) == 0,
        "amplitude_remains_free": sp.diff(selected[0], amplitude) != 0,
        "rival_amplitudes_select_distinct_points": packet_one != packet_two,
        "zero_source_selects_origin": zero_source == sp.zeros(2, 1),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP302",
        "theorem_domain": "two invariant quotient coordinates with S2 swap symmetry, positive symmetric Hessian A=[[a,c],[c,a]], and invariant linear source beta(1,1)",
        "fixed_subspace": "span((1,1))",
        "strict_convexity_condition": "a>c>=0",
        "selected_point": [str(value) for value in selected],
        "symmetry_consequence": "x_1=x_2",
        "unfixed_parameter": "beta/(a+c)",
        "rival_packets": [
            {"a": 2, "c": 1, "beta": 3, "selected_point": [str(value) for value in packet_one]},
            {"a": 2, "c": 1, "beta": 6, "selected_point": [str(value) for value in packet_two]},
        ],
        "descent": "the potential is a function of declared quotient coordinates and is S2 invariant",
        "classification": "symmetry rigidifies the selector direction and component ratio but does not select the numerical amplitude",
        "smallest_exact_falsifier": "the same symmetric Hessian selects (1,1) at beta=3 and (2,2) at beta=6",
        "remaining_physical_instrument_gate": "derive the invariant source amplitude and Hessian normalization from UV dynamics; an added norm constraint introduces its own source scale and must be independently authorized",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp302_symmetry_direction_amplitude_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
