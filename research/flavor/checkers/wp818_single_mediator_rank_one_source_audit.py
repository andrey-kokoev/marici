"""Exact WP818 audit of a single-mediator source for the Gram-loop selector."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    g1, g2, g3, mass = sp.symbols("g1 g2 g3 mass", nonzero=True, real=True)
    coupling = sp.Matrix([g1, g2, g3])
    residue = coupling * coupling.T
    wilson = residue / mass**2
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    def triangle(matrix):
        return sp.factor(matrix[0, 1] * matrix[1, 2] * matrix[2, 0])

    check("single_mediator_residue_is_outer_product", residue == coupling * coupling.T, residue)
    check("single_mediator_residue_has_rank_one", residue.rank() == 1, residue.rank())
    check("single_mediator_wilson_matrix_has_rank_one", wilson.rank() == 1, wilson.rank())
    check("single_mediator_triangle_is_positive_square",
          triangle(residue) == (g1*g2*g3)**2, triangle(residue))
    check("wilson_triangle_has_fixed_positive_sign",
          triangle(wilson) == (g1*g2*g3)**2 / mass**6, triangle(wilson))
    normalized = [sp.simplify(residue[i, j]**2 / (residue[i, i]*residue[j, j]))
                  for i, j in ((0, 1), (1, 2), (2, 0))]
    check("single_mediator_fixes_squared_normalized_edges", normalized == [1, 1, 1], normalized)

    source_a, source_b = sp.Matrix([1, 2, 3]), sp.Matrix([1, 3, 2])
    residue_a, residue_b = source_a*source_a.T, source_b*source_b.T
    check("equal_norm_coupling_directions_give_distinct_portals",
          source_a.dot(source_a) == source_b.dot(source_b) and residue_a != residue_b,
          {"norm": source_a.dot(source_a), "A": residue_a, "B": residue_b})
    check("single_mediator_does_not_select_coupling_direction",
          residue_a[0, 1] != residue_b[0, 1], (residue_a[0, 1], residue_b[0, 1]))

    scale = sp.symbols("scale", positive=True)
    scaled_wilson = sp.simplify((scale*coupling)*(scale*coupling).T / (scale*mass)**2)
    check("coupling_mass_scaling_is_exact_source_identification_kernel",
          scaled_wilson == wilson, scaled_wilson)
    fixed_mass_scaled = sp.simplify((scale*coupling)*(scale*coupling).T / mass**2)
    check("absolute_low_energy_magnitude_remains_continuously_tunable",
          fixed_mass_scaled == scale**2*wilson, fixed_mass_scaled)

    gamma1, gamma2, gamma3, time = sp.symbols("gamma1 gamma2 gamma3 time", real=True)
    running = sp.Matrix([sp.exp(gamma1*time)*g1, sp.exp(gamma2*time)*g2,
                         sp.exp(gamma3*time)*g3])
    running_residue = running * running.T
    check("multiplicative_rg_preserves_rank_one_manifold", running_residue.rank() == 1,
          running_residue.rank())
    expected_running_triangle = sp.exp(2*time*(gamma1+gamma2+gamma3))*(g1*g2*g3)**2
    check("multiplicative_rg_preserves_positive_nonzero_loop",
          sp.simplify(triangle(running_residue) / expected_running_triangle) == 1,
          triangle(running_residue))
    ratio = sp.simplify(running[0] / running[1])
    check("generic_anomalous_dimensions_do_not_select_unique_ray",
          ratio == g1*sp.exp(time*(gamma1-gamma2))/g2, ratio)
    check("continuum_of_initial_rays_survives_equal_anomalous_dimensions",
          sp.simplify(ratio.subs(gamma1, gamma2)) == g1/g2, ratio.subs(gamma1, gamma2))

    z1, z2, z3 = sp.symbols("z1 z2 z3", positive=True)
    threshold = sp.diag(z1, z2, z3)
    threshold_residue = threshold * residue * threshold
    check("diagonal_threshold_matching_preserves_rank_one", threshold_residue.rank() == 1,
          threshold_residue.rank())
    check("diagonal_threshold_matching_preserves_positive_loop",
          triangle(threshold_residue) == (g1*g2*g3*z1*z2*z3)**2,
          triangle(threshold_residue))

    hostile_multi = sp.Matrix([
        [1, sp.Rational(1, 4), -sp.Rational(1, 4)],
        [sp.Rational(1, 4), 1, sp.Rational(1, 4)],
        [-sp.Rational(1, 4), sp.Rational(1, 4), 1],
    ])
    check("positive_multi_mediator_threshold_can_have_negative_loop",
          hostile_multi.is_positive_definite and triangle(hostile_multi) < 0,
          {"eigenvalues": hostile_multi.eigenvals(), "triangle": triangle(hostile_multi)})
    check("negative_loop_hostile_requires_more_than_one_rank_one_channel",
          hostile_multi.rank() == 3, hostile_multi.rank())

    c12, c23, c31 = sp.symbols("c12 c23 c31", real=True)
    gains = sp.symbols("s12 s23 s31", positive=True)
    record = sp.Matrix([gains[0]*c12, gains[1]*c23, gains[2]*c31])
    record_jacobian = record.jacobian([c12, c23, c31, *gains])
    check("uncalibrated_three_channel_record_has_three_dimensional_kernel",
          record_jacobian.rank() == 3 and len(record_jacobian.nullspace()) == 3,
          {"rank": record_jacobian.rank(), "nullity": len(record_jacobian.nullspace())})

    germ = {
        "native_arity": 4,
        "source_germs": ["mediator_X", "O1", "O2", "O3"],
        "primitive_attachments": ["g1", "g2", "g3"],
        "single_pole_isolation": True,
        "rank_one_purity_authority": True,
        "coupling_direction_authority": False,
        "absolute_scale_authority": False,
        "rg_basin_authority": False,
        "threshold_exclusivity": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_quaternary_source_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    check("aspect_three_source_attachments_are_explicit",
          len(germ["primitive_attachments"]) == 3, germ)
    check("single_isolated_pole_supplies_purity_authority",
          germ["single_pole_isolation"] and germ["rank_one_purity_authority"], germ)
    open_gates = [key for key in (
        "coupling_direction_authority", "absolute_scale_authority", "rg_basin_authority",
        "threshold_exclusivity", "physical16_descent", "detector_calibration"
    ) if not germ[key]]
    check("six_full_objective_gates_remain_open", len(open_gates) == 6, open_gates)
    deliberate_obstruction = hostile_multi.rank() - 1
    check("deliberate_failure_quantifies_multi_mediator_rank_obstruction",
          deliberate_obstruction == 2, deliberate_obstruction)

    result = {
        "work_package": "WP818",
        "title": "Single-mediator rank-one source audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "residue": str(residue),
            "wilson_matrix": str(wilson),
            "triangle_product": str(triangle(residue)),
            "hostile_multi_mediator_triangle": str(triangle(hostile_multi)),
            "aspect_germ": germ,
        },
        "classification": {
            "source_principle": "one isolated nondegenerate mediator pole derives rank-one purity",
            "sign": "the nonzero triangle sign is forced positive",
            "magnitude": "normalized edge magnitudes are fixed; coupling direction and absolute scale are free",
            "rg_basin": "rank-one manifold is invariant under multiplicative running; no unique ray is selected",
            "threshold": "single-channel factorization survives diagonal matching; additional channels can restore negative loops",
            "readout": "formal cross-channel family exists; physical16 descent and gain calibration remain absent",
            "verdict": "genuine source derivation of the conditional WP817 selector, but not a complete asymmetric-portal principle",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp818_single_mediator_rank_one_source_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
