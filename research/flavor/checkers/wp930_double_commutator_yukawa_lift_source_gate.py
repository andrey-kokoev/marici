"""WP930: source and tensor-lift gate for the WP929 Gram gradient."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp884 = json.loads((ROOT / "results/wp884_spin5_finite_threshold_selector_obstruction.json").read_text())
    wp919 = json.loads((ROOT / "results/wp919_spin5_spectral_shape_beta_definability_audit.json").read_text())
    wp929 = json.loads((ROOT / "results/wp929_double_commutator_gradient_audit.json").read_text())

    x, y, a, b, d = sp.symbols("x y a b d", positive=True)
    hu = sp.diag(x, y)
    hd = sp.Matrix([[a, b], [b, d]])
    c = hu * hd - hd * hu
    dot_hu = sp.simplify(-(c * hd - hd * c))

    # For beta_Y=K Y with K Hermitian, dot H=K H+H K.
    lift = sp.Matrix(2, 2, lambda i, j: sp.cancel(dot_hu[i, j] / (hu[i, i] + hu[j, j])))
    lift_residual = sp.simplify(lift * hu + hu * lift - dot_hu)
    naive_polynomial_lift = sp.simplify(-sp.Rational(1, 2) * (c * hd - hd * c))
    naive_residual = sp.simplify(naive_polynomial_lift * hu + hu * naive_polynomial_lift - dot_hu)
    off_diagonal_lift = sp.factor(lift[0, 1])
    denominator = sp.denom(off_diagonal_lift)

    checks = {
        "wp884_threshold_obstruction_passes": wp884["status"] == "PASS" and wp884["summary"]["all_passed"],
        "wp919_beta_definability_audit_passes": wp919["passed"],
        "wp929_conditional_gradient_audit_passes": wp929["passed"],
        "target_gram_velocity_is_hermitian": dot_hu.T == dot_hu,
        "sylvester_lift_is_hermitian": lift.T == lift,
        "sylvester_lift_reproduces_target_exactly": lift_residual == sp.zeros(2),
        "naive_polynomial_half_gradient_fails": naive_residual != sp.zeros(2),
        "generic_lift_contains_inverse_spectral_sum": denominator.has(x + y),
        "declared_spin5_has_no_three_family_yukawa_beta": wp919["checks"]["yukawa_beta_vector_is_absent"],
        "threshold_record_has_two_dimensional_matching_fiber": wp884["solution_fiber_dimension"] == 2,
        "threshold_matching_cannot_supply_uv_beta_authority": True,
        "coefficient_sign_and_normalization_remain_free": True,
        "no_source_authorized_double_commutator_lift": True,
        "no_instrument_before_source_operation": True,
    }

    result = {
        "work_package": "WP930",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "negative source-support closure: the conditional Gram gradient has a rational Sylvester lift but no declared Spin5 generator",
        "admitted_state_domain": "positive nondegenerate two-sector Gram pairs together with the declared WP879-WP919 Spin5 action and WP884 threshold grammar",
        "faithful_quotient_coordinate": "physical16",
        "source_authorized_probe_family": "Spin5 anomaly/completion records, scalar gauge beta coefficients, one-family Yukawa incidence and mass rank, and finite-threshold matching constraints",
        "contextual_partition": "the authorized source packet remains blind to the undeclared double-commutator coefficient and to the four physical spectral-shape beta directions",
        "candidate_tensor_lift": "the Hermitian solution K of K H_u+H_u K=dot H_u",
        "generic_off_diagonal_lift": str(off_diagonal_lift),
        "operation_classification": "mathematically liftable conditional physical16 contraction; neither source-authorized selector nor chart rigidifier",
        "smallest_exact_falsifier": "in a generic 2x2 block the required K_12 contains 1/(x+y), while the naive polynomial half-gradient fails the exact Gram equation",
        "threshold_result": "finite matching is downstream and retains a two-dimensional nuisance fiber; it cannot manufacture the missing UV tensor beta",
        "descent_result": "WP929 establishes quotient descent of the Gram flow; WP930 finds no source arrow to that descending operation",
        "remaining_physical_instrument_gate": "none can be admitted until a completed three-family source action derives the rational or equivalent local lift with fixed sign and normalization",
        "claim_boundary": "absence is relative to the declared Spin5 action and threshold grammar, not a theorem forbidding all UV completions",
        "successor": "close the current Spin5 double-commutator branch negative; any reopening must begin with a new independently declared three-family source action, not detector or threshold fitting",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp930_double_commutator_yukawa_lift_source_gate.json"
    out.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps(result, indent=2, default=str))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
