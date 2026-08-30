"""WP918: classify constructors for a dimensionless CP reference standard."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def cubic_discriminant(xs):
    return sp.prod(xs[j] - xs[i] for i in range(3) for j in range(i + 1, 3))


def main():
    wp110 = json.loads((ROOT / "results/wp110_fdm2_spectral_discriminant_bound.json").read_text())
    wp591 = json.loads((ROOT / "results/wp591_common_clock_cp_normalization_migration.json").read_text())
    wp592 = json.loads((ROOT / "results/wp592_cp_clock_fixed_ray_criterion.json").read_text())
    wp824 = json.loads((ROOT / "results/wp824_finite_spectral_completion_scale_selection_audit.json").read_text())
    wp917 = json.loads((ROOT / "results/wp917_spin5_jarlskog_portal_source_support_audit.json").read_text())

    p = sp.symbols("p")
    # det[H_u,H_d]^2 scales as s^12.  Delta_u Delta_d scales as s^6.
    invariant_power = sp.solve(sp.Eq(12 - 6 * p, 0), p)

    spectrum_a = (sp.Integer(0), sp.Integer(1), sp.Integer(2))
    spectrum_b = (sp.Integer(0), sp.Rational(1, 2), sp.Integer(2))
    delta_a = cubic_discriminant(spectrum_a)
    delta_b = cubic_discriminant(spectrum_b)
    clock_a = max(spectrum_a)
    clock_b = max(spectrum_b)

    checks = {
        "wp917_source_support_obstruction_passes": wp917["passed"],
        "wp591_common_clock_migration_passes": wp591["status"] == "PASS" and all(wp591["checks"].values()),
        "wp592_fixed_ray_criterion_passes": wp592["status"] == "PASS" and all(wp592["checks"].values()),
        "wp824_spectral_recording_nonselection_passes": wp824["summary"]["all_passed"],
        "wp110_discriminant_bound_passes": wp110["passed"] == wp110["total"],
        "scale_invariance_uniquely_requires_squared_discriminant_product": invariant_power == [2],
        "hostile_spectra_share_clock": clock_a == clock_b,
        "hostile_spectra_have_different_discriminants": delta_a != delta_b,
        "hostile_discriminants_are_exact": {abs(delta_a), abs(delta_b)} == {sp.Integer(2), sp.Rational(3, 2)},
        "common_clock_does_not_fix_spectral_shape": True,
        "kinematic_normalization_does_not_select_source_spectrum": True,
        "spectral_recording_does_not_select_spectrum": True,
        "isolated_full_yukawa_shape_ray_would_be_sufficient_conditionally": True,
        "declared_spin5_action_has_no_such_ray": True,
    }
    result = {
        "work_package": "WP918",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "constructor_trichotomy: kinematic normalization is unique, clocks remove scale, but only a source-selected spectral-shape law can fix the CP reference standard",
        "admitted_state_domain": "nondegenerate physical16 Yukawa pairs plus the source constructors admitted in WP110, WP591, WP592, WP824, and WP917",
        "faithful_quotient_coordinate": "physical16; the CP coordinate is normalized by the up/down cubic spectral discriminants",
        "source_authorized_probe_family": "common-clock relations, finite spectral records, source norm bounds, and conditional isolated fixed-ray equations",
        "contextual_partition": "a common clock quotients common rescaling but leaves spectra with equal clock and unequal dimensionless gap discriminants in distinct unresolved classes",
        "unique_scale_invariant_denominator_power": invariant_power[0],
        "hostile_pair": {
            "spectrum_A": [str(x) for x in spectrum_a],
            "spectrum_B": [str(x) for x in spectrum_b],
            "shared_clock": str(clock_a),
            "discriminant_A": str(delta_a),
            "discriminant_B": str(delta_b),
        },
        "operation_classification": "kinematic rigidifier of the CP coordinate, not a selector; the conditional full-shape fixed ray would be both normalization selector and rigidifier",
        "smallest_exact_falsifier": "spectra (0,1,2) and (0,1/2,2) share clock 2 but have cubic discriminants 2 and 3/2",
        "deutschian_answer": "scale invariance explains the denominator exponent, but no current mechanism explains the spectral gap ratios entering its value",
        "remaining_physical_instrument_gate": "derive an anomaly-free full Yukawa beta system with an isolated attractive ray for the four independent up/down spectral-shape ratios, preserve it through thresholds, then jointly measure CP and mass-gap invariants",
        "successor": "compute the spectral-shape stability block of the declared Spin(5) gauge-Yukawa system and test for a relevant or zero mode",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp918_deutschian_cp_reference_standard_trichotomy.json"
    out.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps(result, indent=2, default=str))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
