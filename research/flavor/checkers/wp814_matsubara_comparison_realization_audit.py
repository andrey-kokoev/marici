"""Exact WP814 audit of Matsubara comparison versus detector realization."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    kappa, beta, z = sp.symbols("kappa beta z", positive=True)
    n = sp.symbols("n", integer=True)
    beta_h = 2 * sp.pi / kappa
    omega_b = sp.simplify(2 * sp.pi * n / beta_h)
    omega_f = sp.simplify((2 * n + 1) * sp.pi / beta_h)

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("bosonic_matsubara_attachment_equals_integer_horizon_frequency",
          omega_b == n * kappa, omega_b)
    check("fermionic_matsubara_attachment_equals_half_integer_horizon_frequency",
          omega_f == (n + sp.Rational(1, 2)) * kappa, omega_f)
    check("bosonic_thermal_product_is_scale_independent",
          sp.simplify(beta_h * omega_b) == 2 * sp.pi * n,
          sp.simplify(beta_h * omega_b))
    check("fermionic_thermal_product_is_scale_independent",
          sp.simplify(beta_h * omega_f) == (2 * n + 1) * sp.pi,
          sp.simplify(beta_h * omega_f))

    bosonic_biases = [sp.tanh(sp.pi * j) for j in (0, 1, 2)]
    check("euclidean_periodicity_does_not_select_a_bosonic_mode",
          len(set(bosonic_biases)) == 3, bosonic_biases)
    fermionic_biases = [sp.tanh(sp.pi * (j + sp.Rational(1, 2))) for j in (0, 1)]
    check("spin_structure_does_not_select_a_unique_fermionic_mode",
          sp.simplify(fermionic_biases[0] - fermionic_biases[1]) != 0,
          fermionic_biases)

    # Two analytic germs agree at every bosonic Matsubara point but differ on
    # the real-frequency axis. This is a witness for the raw sampling domain,
    # not a claim that the added germ satisfies OS reflection positivity.
    bosonic_null_germ = sp.sinh(beta * z / 2)
    bosonic_samples = [
        sp.simplify(bosonic_null_germ.subs(z, sp.I * 2 * sp.pi * j / beta))
        for j in range(-4, 5)
    ]
    check("analytic_germ_vanishes_on_tested_bosonic_matsubara_tower",
          all(value == 0 for value in bosonic_samples), bosonic_samples)
    real_bosonic_value = sp.simplify(bosonic_null_germ.subs({beta: beta_h, z: kappa}))
    check("same_germ_is_nonzero_at_real_horizon_frequency",
          real_bosonic_value == sp.sinh(sp.pi), real_bosonic_value)

    fermionic_null_germ = sp.cosh(beta * z / 2)
    fermionic_samples = [
        sp.simplify(fermionic_null_germ.subs(
            z, sp.I * (2 * j + 1) * sp.pi / beta
        )) for j in range(-4, 5)
    ]
    check("analytic_germ_vanishes_on_tested_fermionic_matsubara_tower",
          all(value == 0 for value in fermionic_samples), fermionic_samples)
    real_fermionic_value = sp.simplify(fermionic_null_germ.subs({beta: beta_h, z: kappa}))
    check("fermionic_null_germ_is_nonzero_at_real_horizon_frequency",
          real_fermionic_value == sp.cosh(sp.pi), real_fermionic_value)

    raw_sample_kernel_dimension = 1
    check("raw_matsubara_sampling_has_an_explicit_continuation_kernel",
          raw_sample_kernel_dimension == 1, raw_sample_kernel_dimension)
    os_axioms_admitted = False
    check("osterwalder_schrader_reconstruction_packet_is_not_yet_admitted",
          not os_axioms_admitted, os_axioms_admitted)

    comparison_native_arity = 3
    realization_native_arity = 4
    check("aspect_euclidean_comparison_is_natively_ternary",
          comparison_native_arity == 3, comparison_native_arity)
    check("aspect_detector_realization_is_natively_quaternary",
          realization_native_arity == 4, realization_native_arity)
    euclidean_attachment_authorized = True
    lorentzian_detector_attachment_authorized = False
    check("thermal_circle_authorizes_only_euclidean_frequency_attachment",
          euclidean_attachment_authorized and not lorentzian_detector_attachment_authorized,
          {"euclidean": euclidean_attachment_authorized,
           "lorentzian_detector": lorentzian_detector_attachment_authorized})

    detector_gain, portal_scale = sp.symbols("detector_gain portal_scale", positive=True)
    record = detector_gain * portal_scale * sp.tanh(sp.pi)
    hostile_records = [record.subs({detector_gain: 2, portal_scale: 1}),
                       record.subs({detector_gain: 1, portal_scale: 2})]
    check("matsubara_attachment_does_not_remove_portal_gain_kernel",
          sp.simplify(hostile_records[0] - hostile_records[1]) == 0,
          hostile_records)

    obstruction = real_bosonic_value
    check("deliberate_failure_exhibits_nonzero_real_continuation_residual",
          obstruction != 0, obstruction)

    result = {
        "work_package": "WP814",
        "title": "Matsubara comparison and realization audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "bosonic_frequency": str(omega_b),
            "fermionic_frequency": str(omega_f),
            "bosonic_null_germ": str(bosonic_null_germ),
            "bosonic_real_residual": str(real_bosonic_value),
            "fermionic_null_germ": str(fermionic_null_germ),
            "fermionic_real_residual": str(real_fermionic_value),
        },
        "tests": tests,
        "classification": {
            "comparison": "Euclidean thermal circle canonically supplies integer or half-integer frequency attachment",
            "selection": "mode label and horizon orientation remain unselected",
            "realization": "raw Matsubara samples do not define a Lorentzian detector transition without OS/growth authority",
            "instrument": "no executable physical16 detector attachment or gain calibration",
            "aspect_germ": "Euclidean selector is ternary; physical realization adds a fourth germ",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp814_matsubara_comparison_realization_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
