"""Exact WP859 positive Kirchhoff selector and two-port instrument audit."""

import json
from pathlib import Path
import sympy as sp


def liouvillian(jump):
    gram = jump.T*jump

    def act(rho):
        return sp.simplify(jump*rho*jump.T-sp.Rational(1, 2)*(gram*rho+rho*gram))

    columns = []
    for i in range(2):
        for j in range(2):
            basis = sp.zeros(2)
            basis[i, j] = 1
            image = act(basis)
            columns.append(sp.Matrix([image[a, b] for a in range(2) for b in range(2)]))
    return sp.Matrix.hstack(*columns), act


def main() -> None:
    z, kappa = sp.symbols("z kappa", nonzero=True, positive=True)
    root2 = sp.sqrt(2)
    common = sp.Matrix([[1, z]])/root2
    common_adjoint = sp.Matrix([1, 1/z])/root2
    gram = common_adjoint*common
    dark = sp.Matrix([-z, 1])/root2
    dark_bra = sp.Matrix([[-1/z, 1]])/root2
    bright = sp.Matrix([z, 1])/root2
    bright_bra = sp.Matrix([[1/z, 1]])/root2
    difference = sp.Matrix([[-1, z]])/root2
    junction = sp.Matrix([[1, z], [-1, z]])/root2
    junction_adjoint = sp.Matrix([[1, -1], [1/z, 1/z]])/root2
    jump = sp.sqrt(kappa)*dark*bright_bra
    superoperator, action = liouvillian(jump.subs(z, 1))
    dark_projector = (dark*dark_bra).subs(z, 1)
    weighted = sp.Matrix([[1, 2]])/sp.sqrt(5)
    weighted_dark = sp.Matrix([-2, 1])/sp.sqrt(5)
    attenuation = sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)],
                             [sp.Rational(1, 4), sp.Rational(3, 4)]])
    a, b = sp.symbols("a b", positive=True)
    reciprocal_weight_solution = sp.solve(
        [a-b, a**2+b**2-1], [a, b], dict=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("Kirchhoff_gram_is_rank_one_projector", gram**2 == gram and gram.rank() == 1,
          gram)
    check("reciprocity_and_normalization_force_equal_primitive_weights",
          reciprocal_weight_solution
          == [{a: 1/sp.sqrt(2), b: 1/sp.sqrt(2)}], reciprocal_weight_solution)
    check("dark_ray_is_unique_zero_mode", gram*dark == sp.zeros(2, 1)
          and len(gram.nullspace()) == 1, gram.nullspace())
    check("bright_ray_has_unit_positive_cost", gram*bright == bright, gram*bright)
    check("lossless_two_port_completion_is_unitary",
          junction_adjoint*junction == sp.eye(2) and junction*junction_adjoint == sp.eye(2),
          junction_adjoint*junction)
    check("selected_ray_is_dark_in_common_port_and_unit_bright_in_difference_port",
          common*dark == sp.zeros(1, 1) and difference*dark == sp.Matrix([[z]]),
          {"common": common*dark, "difference": difference*dark})
    check("lowering_dissipator_has_unique_dark_stationary_state",
          action(dark_projector) == sp.zeros(2) and superoperator.rank() == 3,
          superoperator.nullspace())
    check("lowering_dissipator_has_exact_global_gap",
          superoperator.eigenvals() == {0: 1, -kappa: 1, -kappa/2: 2},
          superoperator.eigenvals())
    check("weighted_positive_junction_selects_different_magnitude_ray",
          weighted*weighted_dark == sp.zeros(1, 1)
          and weighted_dark != dark.subs(z, 1), weighted_dark)
    check("swap_covariant_threshold_preserves_ray_but_halves_amplitude",
          attenuation*dark.subs(z, 1) == dark.subs(z, 1)/2,
          attenuation*dark.subs(z, 1))
    check("attenuation_is_not_isometric", attenuation.T*attenuation != sp.eye(2),
          attenuation.T*attenuation)

    result = {
        "work_package": "WP859",
        "title": "Positive Kirchhoff junction selector and instrument",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_principle": "reciprocal normalized Kirchhoff incidence with positive Gram and lossless two-port completion",
        "selected_ray": "(-z,1)/sqrt(2)",
        "portal_magnitude": "unit component magnitudes 1/sqrt(2)",
        "global_basin": "unique zero-temperature lowering fixed point on normalized two-path density matrices",
        "source_instrument": "common dark port plus complementary unit-bright difference port",
        "smallest_hostiles": ["weighted junction (1,2)/sqrt(5)",
                              "finite-temperature reverse jump", "non-isometric threshold T_3/4"],
        "classification": "conditional selector and executable source-level instrument",
        "remaining_gates": ["microscopic endpoint-reciprocity authority",
                            "flavor-RG identification", "isometric full two-port threshold transport",
                            "calibrated physical16 detector realization"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp859_positive_kirchhoff_junction_selector_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
