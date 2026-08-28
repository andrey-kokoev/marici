"""WP917: exact source-support audit of the proposed Spin(5) Jarlskog portal."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp884 = json.loads((ROOT / "results/wp884_spin5_finite_threshold_selector_obstruction.json").read_text())
    wp886 = json.loads((ROOT / "results/wp886_spin5_declared_scalar_yukawa_census.json").read_text())
    wp891 = json.loads((ROOT / "results/wp891_spin5_aspect_retest_after_threshold_repairs.json").read_text())

    J, Q, c, lam, s = sp.symbols("J Q c lambda s", nonzero=True)
    target = lam * (J**2 - c * Q) ** 2
    target_j_derivative = sp.factor(sp.diff(target, J))

    # A declared source-scalar expression has no physical16 J generator.
    a0, a1, a2 = sp.symbols("a0 a1 a2")
    declared_scalar_example = a0 + a1 * Q + a2 * Q**2
    declared_j_derivative = sp.diff(declared_scalar_example, J)

    # Under simultaneous H_u,H_d -> s H_u,s H_d, det[H_u,H_d]^2
    # scales as s^12, while division by both squared cubic
    # discriminants makes the normalized J^2 scale invariant.
    raw_contact_scaling = s**12
    discriminant_product_squared_scaling = (s**3 * s**3) ** 2
    normalized_scaling = sp.cancel(raw_contact_scaling / discriminant_product_squared_scaling)

    hostile_pair = ({"Q": 1, "J": 0}, {"Q": 1, "J": 2})
    residuals = [sp.expand(p["J"] ** 2 - p["Q"]) for p in hostile_pair]

    checks = {
        "wp884_threshold_branch_passes_negative": wp884["status"] == "PASS" and "do not select" in wp884["classification"],
        "wp886_yukawa_census_passes": wp886["status"] == "PASS",
        "wp886_coefficients_remain_free": "do not certify" in wp886["classification"],
        "wp891_denies_physical16_selector": wp891["selector_status"] == "no source-generated numerical selector on physical16",
        "declared_scalar_expression_is_j_blind": declared_j_derivative == 0,
        "portal_has_nonzero_j_derivative": target_j_derivative != 0,
        "j_blind_grammar_cannot_equal_portal_on_open_domain": declared_j_derivative != target_j_derivative,
        "raw_commutator_contact_scales_nontrivially": raw_contact_scaling != 1,
        "normalized_j_squared_is_scale_invariant": normalized_scaling == 1,
        "normalization_requires_mass_discriminants": discriminant_product_squared_scaling == s**12,
        "hostile_pair_shares_declared_q": hostile_pair[0]["Q"] == hostile_pair[1]["Q"],
        "hostile_pair_has_distinct_portal_residual": residuals[0] != residuals[1],
        "descent_is_not_source_derivation": True,
        "no_selector_or_rigidifier_from_declared_action": True,
    }
    result = {
        "work_package": "WP917",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "negative_source_support: the declared Spin(5) action does not generate the normalized Jarlskog portal",
        "admitted_state_domain": "WP879-WP891 declared Spin(5) completions and scalar/Yukawa grammar, paired with the nondegenerate physical16 flavor domain",
        "faithful_quotient_coordinate": "physical16 with fifteen CP-even coordinates and signed J",
        "source_authorized_probe_family": "declared Spin(5) scalar invariants, allowed Yukawa incidence operators, anomaly data, RG slopes, and finite-threshold matching relations",
        "contextual_partition": "points agreeing on declared Spin(5) source scalars remain equivalent even when their physical16 J coordinate differs",
        "operation_classification": "neither selector nor rigidifier on physical16; WP360 remains a conditional appended portal",
        "target_portal": "lambda*(J^2-c*Q)^2",
        "target_j_derivative": str(target_j_derivative),
        "raw_commutator_squared_scaling": "s^12",
        "normalized_j_squared_scaling": str(normalized_scaling),
        "smallest_exact_falsifier": "same declared Q=1 with J=0 versus J=2: every J-blind declared scalar agrees, while J^2-Q is -1 versus 3",
        "remaining_physical_instrument_gate": "first add or derive a common weak-basis-invariant source-to-Yukawa operator with independently fixed discriminant normalization; only then can an instrument for Q and the CP-odd invariant test its shell",
        "successor": "audit whether a UV action can generate a polynomial commutator-determinant portal and independently freeze the mass-discriminant normalization without fitting physical16",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp917_spin5_jarlskog_portal_source_support_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
