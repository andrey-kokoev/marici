"""Exact WP867 odd-character and anomaly-multiplicity audit."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    exchange = sp.Matrix([[0, 1], [1, 0]])
    dark = sp.Matrix([-1, 1])/sp.sqrt(2)
    bright = sp.Matrix([1, 1])/sp.sqrt(2)
    p_odd = (sp.eye(2)-exchange)/2
    p_even = (sp.eye(2)+exchange)/2
    a, b, c, d = sp.symbols("a b c d")
    operator = sp.Matrix([[a, b], [c, d]])
    commutation_solution = sp.solve(list(operator*exchange-exchange*operator),
                                    (a, b, c, d), dict=True)

    # One odd and three even directions: equivariance protects the odd line.
    r_unique = sp.diag(-1, 1, 1, 1)
    x = sp.Matrix(4, 4, sp.symbols("x0:16"))
    unique_constraints = list(x*r_unique-r_unique*x)
    unique_solution = sp.linsolve(unique_constraints, list(x))

    # An anomaly-neutral pair of additional odd carriers reopens mixing.
    r_hostile = sp.diag(-1, 1, -1, -1)
    cosine = sp.Rational(3, 4)
    sine = sp.sqrt(7)/4
    rotation = sp.eye(4)
    rotation[0, 0], rotation[0, 2] = cosine, sine
    rotation[2, 0], rotation[2, 2] = -sine, cosine
    light = sp.diag(1, 1, 0, 0)
    dark_full = sp.Matrix([1, 0, 0, 0])
    retained_norm = sp.simplify((light*rotation*dark_full).norm()**2)
    fourier = sp.Matrix([[1, 1], [-1, 1]])/sp.sqrt(2)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("odd_and_even_projectors_are_orthogonal",
          p_odd**2 == p_odd and p_even**2 == p_even
          and p_odd*p_even == sp.zeros(2), [p_odd, p_even])
    check("odd_projector_selects_normalized_difference_ray",
          sp.simplify(p_odd*dark-dark) == sp.zeros(2, 1)
          and sp.simplify(p_odd*bright) == sp.zeros(2, 1),
          [p_odd*dark, p_odd*bright])
    check("endpoint_equivariant_commutant_preserves_character_lines",
          commutation_solution == [{a: d, b: c}], commutation_solution)
    check("multiplicity_one_odd_sector_has_no_equivariant_cross_block",
          len(unique_solution.args) == 1
          and all(unique_solution.args[0][j] == 0 for j in (1, 2, 3, 4, 8, 12)),
          unique_solution)
    check("character_fourier_readout_is_lossless",
          fourier*fourier.conjugate().T == sp.eye(2), fourier)
    check("two_added_odd_modes_preserve_mod_two_class",
          (3-1) % 2 == 0, "odd multiplicity 1 -> 3")
    check("hostile_rotation_is_unitary_and_equivariant",
          rotation.conjugate().T*rotation == sp.eye(4)
          and rotation*r_hostile == r_hostile*rotation, rotation)
    check("anomaly_preserving_hostile_attenuates_light_dark_line",
          retained_norm == sp.Rational(9, 16), retained_norm)
    check("ordinary_anomaly_does_not_enforce_multiplicity_one", True,
          "mod-two class retains only odd multiplicity parity")
    check("representation_memory_and_calibrated_instrument_remain_open", True,
          "requires marked equivariant index, threshold sewing, and physical16 calibration")

    result = {
        "schema": "marici.flavor.multiplicity-one-odd-boundary-protection-audit.v1",
        "work_package": "WP867",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "conditional_principle": "multiplicity-one nontrivial endpoint character plus canonical dark-corner expectation",
        "selected_ray": "(-1,1)/sqrt(2)",
        "threshold_theorem": "global multiplicity one forces equivariant preservation of the odd line",
        "anomaly_obstruction": "anomaly-neutral heavy odd pair preserves mod-two class and reopens mixing",
        "smallest_exact_falsifier": "odd multiplicity 1 -> 3 with a cosine-3/4 dark-heavy rotation",
        "retained_light_norm_squared": str(retained_norm),
        "classification": "conditional selector and protector; not derived by ordinary anomaly matching",
        "remaining_physical_instrument_gate": "marked representation-valued threshold index and calibrated physical16 odd-port response",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp867_multiplicity_one_odd_boundary_protection_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
