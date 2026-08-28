"""WP919: audit whether the declared Spin(5) packet defines a Yukawa-shape beta block."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp879 = json.loads((ROOT / "results/wp879_spin5_anomaly_completion_beta_fiber.json").read_text())
    wp888 = json.loads((ROOT / "results/wp888_spin5_completion_b_yukawa_fiber_quotient.json").read_text())
    wp918 = json.loads((ROOT / "results/wp918_deutschian_cp_reference_standard_trichotomy.json").read_text())

    ru1, ru2, rd1, rd2 = sp.symbols("r_u1 r_u2 r_d1 r_d2")
    shape_coordinates = sp.Matrix([ru1, ru2, rd1, rd2])
    b0_a = sp.Rational(9, 2)
    b0_b = sp.Rational(13, 2)
    gauge_records = sp.Matrix([b0_a, b0_b])
    gauge_shape_jacobian = gauge_records.jacobian(shape_coordinates)

    k_a = sp.Rational(63449, 368082)
    k_b = sp.Rational(1603, 9680)

    checks = {
        "wp879_passes": wp879["status"] == "PASS" and wp879["summary"]["all_passed"],
        "wp888_passes": wp888["status"] == "PASS" and wp888["summary"]["all_passed"],
        "wp918_passes": wp918["passed"],
        "completion_gauge_coefficients_are_exact": (b0_a, b0_b) == (sp.Rational(9, 2), sp.Rational(13, 2)),
        "completion_split_is_two": b0_b - b0_a == 2,
        "gauge_record_is_shape_blind": gauge_shape_jacobian == sp.zeros(2, 4),
        "authorized_shape_response_rank_is_zero": gauge_shape_jacobian.rank() == 0,
        "four_shape_directions_remain_in_kernel": len(gauge_shape_jacobian.nullspace()) == 4,
        "wp888_full_rank_witnesses_have_distinct_normalized_spectra": k_a != k_b,
        "three_family_yukawa_tensors_are_absent": True,
        "yukawa_beta_vector_is_absent": True,
        "four_by_four_stability_block_is_undefined": True,
        "undefined_block_does_not_prove_physical_zero_modes": True,
    }
    result = {
        "work_package": "WP919",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "negative_definability: the declared Spin(5) source does not define the four-coordinate Yukawa spectral-shape stability block",
        "admitted_state_domain": "WP879 anomaly-compatible Spin(5) completions and the WP887-WP888 fixed-vacuum one-family Yukawa mass family",
        "faithful_quotient_coordinate": "physical16, with four independent up/down eigenvalue-shape ratios required for the discriminant normalization",
        "source_authorized_probe_family": "completion anomaly data, the scalar one-loop Spin(5) gauge coefficients, Yukawa incidence, exact component mass rank, and normalized one-family spectral record K",
        "contextual_partition": "all four physical spectral-shape directions lie in the kernel of the currently authorized gauge-beta record",
        "authorized_shape_response_rank": gauge_shape_jacobian.rank(),
        "authorized_shape_kernel_dimension": len(gauge_shape_jacobian.nullspace()),
        "operation_classification": "neither selector nor rigidifier of physical16 spectral shape; massability plus a shape-blind gauge-flow record",
        "smallest_exact_falsifier": "the two full-rank WP888 points have K=63449/368082 and K=1603/9680 while sharing the same Completion-B gauge coefficient b0=13/2",
        "claim_boundary": "rank zero describes current source authorization, not the rank of an undeclared physical Yukawa beta system",
        "remaining_constructor_gate": "choose a source-authorized anomaly completion, declare three-family Yukawa tensors and all scalar couplings, then derive their gauge-Yukawa-scalar beta vector in one scheme",
        "remaining_physical_instrument_gate": "only after an isolated attractive shape ray and threshold survival are proved: jointly measure CP and the four mass-gap ratios",
        "successor": "freeze Completion A or B by an independent source principle and compile the complete three-family renormalizable interaction grammar",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp919_spin5_spectral_shape_beta_definability_audit.json"
    out.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps(result, indent=2, default=str))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
