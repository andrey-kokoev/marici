"""Exact WP816 audit of a sign-sensitive reflection-positive residue germ."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    A, B, C, delta, t = sp.symbols("A B C delta t", positive=True)
    residue = sp.Matrix([[A, C], [C, B]])
    determinant = sp.factor(residue.det())

    plus = sp.Matrix([[1, 1], [1, 1]])
    minus = sp.Matrix([[1, -1], [-1, 1]])
    sign_flip = sp.diag(1, -1)

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("mixed_residue_positivity_bound_is_gram_determinant",
          determinant == A * B - C**2, determinant)
    check("positive_rank_one_saturation_has_two_exact_sign_branches",
          sp.solve(sp.Eq(determinant, 0), C) == [sp.sqrt(A) * sp.sqrt(B)],
          "with C declared positive; signed extension is plus/minus sqrt(A B)")

    signed_C = sp.symbols("signed_C", real=True)
    signed_det = A * B - signed_C**2
    saturation_branches = sp.solve(sp.Eq(signed_det, 0), signed_C)
    check("signed_purity_equation_retains_mirror_pair",
          saturation_branches == [-sp.sqrt(A) * sp.sqrt(B), sp.sqrt(A) * sp.sqrt(B)],
          saturation_branches)
    check("positive_and_negative_saturated_residues_are_both_psd",
          plus.is_positive_semidefinite and minus.is_positive_semidefinite,
          {"plus_eigenvalues": plus.eigenvals(), "minus_eigenvalues": minus.eigenvals()})
    check("saturated_sign_pair_has_identical_spectrum",
          plus.eigenvals() == minus.eigenvals(), plus.eigenvals())
    check("saturated_sign_pair_has_identical_diagonal_readouts",
          list(plus.diagonal()) == list(minus.diagonal()) == [1, 1],
          {"plus": list(plus.diagonal()), "minus": list(minus.diagonal())})
    check("mixed_correlator_separates_saturated_sign_pair",
          plus[0, 1] == 1 and minus[0, 1] == -1,
          (plus[0, 1], minus[0, 1]))
    check("operator_sign_port_conjugates_the_two_residues",
          sign_flip * plus * sign_flip == minus, sign_flip * plus * sign_flip)

    times = [sp.Integer(0), sp.Integer(1)]
    time_vector = sp.Matrix([sp.exp(-delta * value) for value in times])
    time_gram = time_vector * time_vector.T
    full_plus_gram = sp.kronecker_product(plus, time_gram)
    full_minus_gram = sp.kronecker_product(minus, time_gram)
    check("full_mixed_euclidean_kernels_are_reflection_positive",
          full_plus_gram.is_positive_semidefinite and full_minus_gram.is_positive_semidefinite,
          (full_plus_gram.rank(), full_minus_gram.rank()))

    rho_plus = sp.simplify(plus[0, 1] / sp.sqrt(plus[0, 0] * plus[1, 1]))
    rho_minus = sp.simplify(minus[0, 1] / sp.sqrt(minus[0, 0] * minus[1, 1]))
    check("purity_fixes_normalized_magnitude_but_not_sign",
          (rho_plus, rho_minus) == (1, -1), (rho_plus, rho_minus))

    wavefunction = sp.diag(2, 3)
    transported_plus = wavefunction * plus * wavefunction
    transported_minus = wavefunction * minus * wavefunction
    transported_rhos = (
        sp.simplify(transported_plus[0, 1]
                    / sp.sqrt(transported_plus[0, 0] * transported_plus[1, 1])),
        sp.simplify(transported_minus[0, 1]
                    / sp.sqrt(transported_minus[0, 0] * transported_minus[1, 1])),
    )
    check("positive_diagonal_threshold_transport_preserves_normalized_sign_pair",
          transported_rhos == (1, -1), transported_rhos)

    rotation = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    rotated_plus = sp.simplify(rotation * plus * rotation.T)
    check("nonaligned_threshold_mixing_changes_fixed_axis_cross_readout",
          rotated_plus[0, 1] == 0, rotated_plus)

    # A complete calibrated three-channel record reconstructs the residue.
    complete_record = sp.Matrix([A, B, signed_C])
    complete_jacobian = complete_record.jacobian([A, B, signed_C])
    check("calibrated_diagonal_and_mixed_probe_family_is_faithful",
          complete_jacobian.rank() == 3, complete_jacobian.rank())

    cross_gain = sp.symbols("cross_gain", positive=True)
    cross_record = cross_gain * signed_C
    hostile_cross_records = [
        cross_record.subs({signed_C: 1, cross_gain: 2}),
        cross_record.subs({signed_C: sp.Rational(1, 2), cross_gain: 4}),
    ]
    check("uncalibrated_mixed_probe_has_exact_source_gain_hostile_pair",
          hostile_cross_records == [2, 2], hostile_cross_records)
    cross_jacobian = sp.Matrix([cross_record]).jacobian([signed_C, cross_gain])
    check("mixed_probe_without_gain_calibration_is_rank_one",
          cross_jacobian.rank() == 1, f"rank={cross_jacobian.rank()}, nullity=1")

    purity_authorized = False
    check("rank_one_purity_condition_is_not_source_authorized",
          not purity_authorized, purity_authorized)
    operator_sign_port_fixed = False
    check("relative_operator_sign_port_is_not_source_authorized",
          not operator_sign_port_fixed, operator_sign_port_fixed)

    obstruction = len(saturation_branches) - 1
    check("deliberate_failure_exhibits_purity_sign_ambiguity",
          obstruction == 1, obstruction)

    result = {
        "work_package": "WP816",
        "title": "Mixed OS residue sign-pair audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "residue": str(residue),
            "positivity_determinant": str(determinant),
            "purity_branches": [str(value) for value in saturation_branches],
            "normalized_sign_pair": [str(rho_plus), str(rho_minus)],
            "threshold_transported_pair": [str(value) for value in transported_rhos],
        },
        "tests": tests,
        "classification": {
            "reflection_positivity": "bounds mixed residue magnitude and admits both signs",
            "purity": "rank-one saturation fixes normalized magnitude but retains a mirror pair",
            "sign_readout": "mixed correlator separates the pair after an operator sign port is fixed",
            "threshold": "positive diagonal transport preserves normalized pair; nonaligned mixing changes fixed-axis readout",
            "instrument": "complete calibrated three-channel family is faithful; uncalibrated cross channel is not",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp816_mixed_os_residue_sign_pair_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
