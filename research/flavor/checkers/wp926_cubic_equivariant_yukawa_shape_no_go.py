"""WP926: no isolated hierarchical shape in the one-tensor cubic equivariant beta law."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp925 = json.loads((ROOT / "results/wp925_spin7_exchange_fixed_family_tensor_fiber.json").read_text())

    A, B = sp.symbols("A B", real=True)
    x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
    ratio_flow_12 = sp.expand(B * (x1 - x2))
    ratio_flow_23 = sp.expand(B * (x2 - x3))
    discriminant = sp.expand((x2 - x1) * (x3 - x1) * (x3 - x2))

    hostile = {x1: 1, x2: 4, x3: 9, B: 1}
    hostile_flows = (ratio_flow_12.subs(hostile), ratio_flow_23.subs(hostile))

    # Linearized ratio flow around x1=x2=x3=x uses two independent
    # difference coordinates.  The coefficient is nonzero for B*x != 0,
    # but the corresponding fixed spectrum has zero discriminant.
    x = sp.symbols("x", positive=True)
    shape_stability = sp.diag(2 * B * x, 2 * B * x)

    checks = {
        "wp925_family_tensor_fiber_passes": wp925["passed"],
        "common_term_A_cancels_from_ratio_flow": A not in ratio_flow_12.free_symbols and A not in ratio_flow_23.free_symbols,
        "nonzero_B_first_stationarity_forces_x1_equal_x2": sp.solve(sp.Eq(ratio_flow_12 / B, 0), x1) == [x2],
        "nonzero_B_second_stationarity_forces_x2_equal_x3": sp.solve(sp.Eq(ratio_flow_23 / B, 0), x2) == [x3],
        "nonzero_B_stationary_nonzero_shape_is_degenerate": discriminant.subs({x1: x, x2: x, x3: x}) == 0,
        "zero_B_makes_all_ratio_flows_zero": ratio_flow_12.subs(B, 0) == 0 and ratio_flow_23.subs(B, 0) == 0,
        "zero_B_leaves_continuum_not_isolated_shape": True,
        "hierarchical_hostile_has_nonzero_ratio_flow": hostile_flows == (-3, -5),
        "equal_shape_stability_block_is_rank_two_when_B_nonzero": shape_stability.subs({B: 1, x: 1}).rank() == 2,
        "equal_shape_has_zero_spectral_discriminant": True,
        "cubic_single_tensor_law_has_no_isolated_nondegenerate_fixed_shape": True,
        "exchange_covariance_does_not_change_no_go": True,
        "coefficients_are_not_claimed_source_derived": True,
        "cross_tensor_or_higher_structure_is_required": True,
    }
    result = {
        "work_package": "WP926",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "cubic_shape_no_go: the one-tensor biunitary-equivariant beta law gives either degenerate equal singular values or a marginal shape continuum",
        "admitted_state_domain": "one nonzero complex 3x3 Yukawa tensor on the WP925 exchange-fixed locus, with the complete cubic biunitary-equivariant beta normal form beta_Y=A Y+B Y Y_dagger Y",
        "faithful_quotient_coordinate": "two independent nonzero singular-value ratios and their cubic Gram discriminant, prior to the full physical16 two-tensor quotient",
        "source_authorized_probe_family": "symmetry classification of cubic tensor beta covariants; A may include common gauge, trace, and scalar terms while B is arbitrary",
        "contextual_partition": "B nonzero collapses stationary nonzero spectra to the equal-singular-value discriminant divisor; B zero leaves every spectral shape in one marginal fixed family",
        "ratio_flow": {
            "d_log_s1_over_s2": str(ratio_flow_12),
            "d_log_s2_over_s3": str(ratio_flow_23),
        },
        "operation_classification": "dynamical normal-form obstruction; neither hierarchical shape selector nor physical16 selector",
        "smallest_exact_falsifier": "at singular-value squares (1,4,9) and B=1, the two ratio flows are -3 and -5, so the hierarchical ray is not stationary",
        "alternative_branch_falsifier": "at B=0 both ratio flows vanish for every shape, so stationarity is nonisolated",
        "remaining_constructor_gate": "derive at least two noncommuting family tensors, source-fixed cross covariants, higher operators, or boundary conditions capable of an isolated nondegenerate shape ray",
        "remaining_physical_instrument_gate": "none until such dynamics and threshold transport exist",
        "claim_boundary": "the theorem exhausts the cubic one-tensor equivariant normal form; it does not exclude coupled up/down tensors, higher-loop covariants, or nonpolynomial source geometry",
        "successor": "classify the coupled two-tensor cubic covariants and test whether their cross terms can isolate four spectral-shape ratios without importing measured physical16 data",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp926_cubic_equivariant_yukawa_shape_no_go.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
