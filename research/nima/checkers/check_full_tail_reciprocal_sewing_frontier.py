from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/full-tail-reciprocal-sewing-frontier.json"


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def data(path: str) -> dict:
    return json.loads(text(path))


def main() -> None:
    one_sided = data("research/voevodsky/the-mixed-theta-forcing-reservoir-has-an-exact-source-derived-sum-difference-gram-factorization.v1.json")
    five_cell = data("research/voevodsky/correction-the-fixed-forcing-vector-is-only-the-bulk-anchor-the-complete-evans-pair-bridge-is-the-pointed-five-cell-fourier-module.v1.json")
    prime = data("research/aspect/contracts/polarized-prime-cell-required-input.v2.json")
    prime_open = data("research/aspect/contracts/polarized-prime-cell-open-theorem.v2.json")
    wiener = text("research/nima/reciprocal-wiener-hopf-sewing-factors-the-two-height-boundary-through-xi-square.md")
    correction = text("research/nima/correction-global-port-gram-identity-must-retain-the-bulk-state-leg.md")
    equivalent = text("research/nima/complete-sum-difference-port-sewing-on-xi-states-is-rh-equivalent.md")

    checks = {
        "one_sided_full_tail_green_factorization_closed": one_sided["status"] == "one_sided_polarized_conservative_factorization_closed",
        "scalar_reciprocal_forcing_factors_through_xi_square": "F_{\\rm dbl}(w,z)" in wiener and "Xi(z)^2" in wiener,
        "five_cell_linear_fourier_module_typed": five_cell["status"] == "single_anchor_claim_retracted_multi_anchor_linear_bridge_typed",
        "wall_and_odd_columns_fixed": prime["fixed_linear_data"]["even_norm_squared"] == 1 and prime["quadratic_gate"]["parameter_free"],
        "unaugmented_port_equality_retracted": "unaugmented Gram equality retracted" in correction,
        "bulk_state_leg_required": "bulk state leg" in correction,
        "xi_state_complete_port_equality_is_rh_equivalent": "RH-equivalent" in equivalent,
        "quadratic_prime_cell_identity_still_unproved": not prime["claim_boundary"]["quadratic_four_unit_identity_proved"],
        "quadratic_prime_cell_identity_is_optional_single_metric_descent":
            prime_open["classification"] == "optional_single_metric_descent"
            and not prime_open["single_metric_descent"]["required_by_v3"],
    }

    out = {
        "schema": "marici.nima.full-tail-reciprocal-sewing-frontier.v1",
        "status": "scalar_xi_square_sewing_closed_typed_augmented_six_port_identity_open" if all(checks.values()) else "failed",
        "checks": checks,
        "constructed": {
            "one_sided": "full L2 tail-state input-minus-output Green factorization",
            "reciprocal_scalar": "doubled forcing reservoir factors through Xi(z)^2 and conjugate Xi(w)^2",
            "linear_bridge": "five-cell C4 Fourier module with normalized wall, odd endpoint, and two oriented tail columns",
        },
        "not_constructed": {
            "typed_identification": "equality of the Rosenbrock endpoint-plus-difference boundary with the scalar Wiener-Hopf forcing boundary",
            "augmented_colligation": "complete two-height Gram equality retaining the bulk state leg and every arithmetic/wall/linking coordinate",
            "quadratic_local_data": "four parameter-free polarized prime-cell matrix-unit identities remain unproved, but v17 faithful-joint-graph semantics make this optional single-metric descent rather than the active Evans gate",
        },
        "noncircularity": "Complete-port equality imposed only on Xi states is RH-equivalent. The admissible theorem must be an off-divisor augmented two-height identity on arbitrary source histories.",
        "active_vs_optional": {
            "active": "off-divisor augmented two-height comparison placing the Xi/Evans history in the full-tail conservative graph",
            "optional": "collapse of retained Stieltjes and theta-history realizations to one metric via four matrix-unit identities",
        },
        "first_executable_input_needed": [
            "matrices for the complete labelled incoming sum-port map",
            "matrices for the endpoint-plus-difference outgoing map",
            "bulk tail-state feature matrix",
            "common source Gram and variance conventions",
            "an independent Xi/Evans-to-tail state-placement map on the same domain",
        ],
        "finite_test_when_materialized": "R_X(w,z)=I-Theta_X(w)^*Theta_X(z)-(1-conj(lambda(w))*lambda(z))*F_X(w)^*F_X(z); one nonzero labelled entry falsifies the candidate.",
        "claim_boundary": "This is a typing and logical-strength audit. Scalar Xi-square factorization does not prove the absent augmented six-port colligation identity.",
        "rh_implication": False,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
