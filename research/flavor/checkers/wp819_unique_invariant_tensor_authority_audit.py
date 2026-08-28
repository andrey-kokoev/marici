"""Exact WP819 audit of unique-invariant-tensor flavor authority."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    identity = sp.eye(3)
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    cycle_projector = sp.simplify((identity + cycle + cycle**2) / 3)
    swap = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    target = sp.Matrix([1, 2, 3])
    target_norm_sq = target.dot(target)
    target_projector = target * target.T / target_norm_sq
    reflection = sp.simplify(2*target_projector - identity)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("cyclic_permutation_is_order_three", cycle**3 == identity, cycle**3)
    check("transitive_cyclic_fixed_space_is_one_dimensional",
          len((cycle - identity).nullspace()) == 1, (cycle - identity).nullspace())
    check("cyclic_group_average_is_rank_one_projector",
          cycle_projector.rank() == 1 and cycle_projector**2 == cycle_projector,
          cycle_projector)
    cyclic_fixed = (cycle - identity).nullspace()[0]
    check("transitive_cyclic_invariant_ray_is_symmetric",
          cyclic_fixed[0] == cyclic_fixed[1] == cyclic_fixed[2], cyclic_fixed)
    check("transitive_invariant_ray_has_zero_component_contrast",
          cyclic_fixed[2] - cyclic_fixed[1] == 0, cyclic_fixed[2] - cyclic_fixed[1])

    check("single_swap_fixed_space_is_two_dimensional",
          len((swap - identity).nullspace()) == 2, (swap - identity).nullspace())
    check("partial_marking_does_not_select_unique_ray",
          (swap - identity).rank() == 1, f"fixed dimension={3-(swap-identity).rank()}")

    check("prescribed_ray_reflection_is_an_involution",
          sp.simplify(reflection**2) == identity, reflection**2)
    check("prescribed_ray_is_fixed_by_constructed_reflection",
          sp.simplify(reflection*target) == target, reflection*target)
    check("constructed_reflection_has_unique_fixed_ray",
          len((reflection - identity).nullspace()) == 1
          and (reflection - identity).nullspace()[0].cross(target) == sp.zeros(3, 1),
          (reflection - identity).nullspace())
    check("constructed_unique_fixed_ray_is_asymmetric",
          target[2] - target[1] == 1, target[2] - target[1])

    a, b, c = sp.symbols("a b c", real=True)
    arbitrary = sp.Matrix([a, b, c])
    arbitrary_norm_sq = sp.expand(arbitrary.dot(arbitrary))
    arbitrary_reflection = 2*arbitrary*arbitrary.T/arbitrary_norm_sq - identity
    check("any_nonzero_prescribed_ray_can_be_made_a_z2_fixed_line",
          sp.simplify(arbitrary_reflection*arbitrary - arbitrary) == sp.zeros(3, 1),
          arbitrary_reflection*arbitrary)
    check("reverse_engineered_symmetry_contains_target_projector_explicitly",
          sp.simplify((reflection + identity)/2) == target_projector,
          (reflection + identity)/2)

    y = sp.symbols("y", nonzero=True, real=True)
    normalized_target = target / sp.sqrt(target_norm_sq)
    coupling = y * normalized_target
    contrast = sp.simplify(coupling[2] - coupling[1])
    check("normalized_invariant_tensor_leaves_overall_coupling_free",
          contrast == y/sp.sqrt(14), contrast)
    check("overall_sign_pair_flips_linear_asymmetric_portal",
          contrast.subs(y, -y) == -contrast, (contrast, contrast.subs(y, -y)))
    residue = coupling * coupling.T
    check("quadratic_residue_is_blind_to_overall_sign",
          residue.subs(y, -y) == residue, residue)

    alpha, beta = sp.symbols("alpha beta", real=True)
    beta_y = alpha*y + beta*y**3
    check("symmetry_allows_arbitrary_scalar_equivariant_beta_function",
          sp.factor(beta_y/y) == alpha + beta*y**2, beta_y)
    check("nonzero_fixed_point_magnitude_depends_on_unfixed_rg_coefficients",
          sp.solve(sp.Eq(alpha + beta*y**2, 0), y**2) == [-alpha/beta],
          sp.solve(sp.Eq(alpha + beta*y**2, 0), y**2))

    z, w = sp.symbols("z w", positive=True)
    equivariant_threshold = sp.simplify(z*target_projector + w*(identity-target_projector))
    check("equivariant_threshold_preserves_invariant_ray",
          sp.simplify(equivariant_threshold*target) == z*target,
          equivariant_threshold*target)
    check("equivariant_threshold_leaves_continuous_magnitude_factor",
          sp.simplify((equivariant_threshold*coupling)[2]
                      - (equivariant_threshold*coupling)[1]) == z*contrast,
          sp.simplify((equivariant_threshold*coupling)[2]
                      - (equivariant_threshold*coupling)[1]))

    gain = sp.symbols("gain", positive=True)
    record = gain * contrast
    hostile_records = [
        record.subs({y: 1, gain: 2}),
        record.subs({y: 2, gain: 1}),
    ]
    check("uncalibrated_linear_readout_has_exact_source_gain_pair",
          hostile_records[0] == hostile_records[1], hostile_records)
    record_jacobian = sp.Matrix([record]).jacobian([y, gain])
    check("linear_readout_has_rank_one_on_source_gain_domain",
          record_jacobian.rank() == 1, record_jacobian.rank())

    germ = {
        "native_arity": 5,
        "source_germs": ["representation", "mediator", "O1", "O2", "O3"],
        "unique_fixed_line": True,
        "independent_representation_authority": False,
        "orientation_authority": False,
        "overall_coupling_authority": False,
        "rg_coefficients_authority": False,
        "threshold_scalar_authority": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_five_object_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    open_gates = [key for key in (
        "independent_representation_authority", "orientation_authority",
        "overall_coupling_authority", "rg_coefficients_authority",
        "threshold_scalar_authority", "physical16_descent", "detector_calibration"
    ) if not germ[key]]
    check("seven_authority_and_realization_gates_remain_open",
          len(open_gates) == 7, open_gates)

    result = {
        "work_package": "WP819",
        "title": "Unique invariant tensor authority audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "cyclic_projector": str(cycle_projector),
            "asymmetric_target": [int(value) for value in target],
            "target_reflection": str(reflection),
            "target_projector_recovered_from_representation": str((reflection+identity)/2),
            "linear_contrast": str(contrast),
            "aspect_germ": germ,
        },
        "classification": {
            "transitive_symmetry": "unique invariant ray exists but is symmetric and has zero portal contrast",
            "partial_symmetry": "admits a multidimensional invariant family",
            "asymmetric_fixed_line": "can be manufactured for any chosen ray, so it needs independent source authority",
            "sign": "the invariant line does not orient itself; quadratic residue is sign blind",
            "magnitude": "tensor normalization leaves an arbitrary interaction coefficient",
            "rg": "equivariance reduces flow to one scalar beta function but does not derive its coefficients",
            "threshold": "equivariant matching preserves direction while rescaling magnitude arbitrarily",
            "readout": "physical16 descent is absent and an uncalibrated linear channel has a source-gain kernel",
            "verdict": "unique invariant tensor is a rigidifier unless the representation and scalar dynamics are independently derived",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp819_unique_invariant_tensor_authority_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
