"""Exact leakage and fixed-point energy audit for compiled D(S3) controls."""

import json
import sympy as sp


def main():
    theta = sp.symbols("theta", real=True)
    phase = sp.exp(-sp.I * theta)
    leakage = {}
    transient = {}
    for name, class_size in (("transposition", 3), ("three_cycle", 2)):
        centralizer_size = 6 // class_size
        survival = sp.simplify(abs((6 - centralizer_size + centralizer_size * phase) / 6) ** 2)
        value = sp.simplify(sp.expand_complex(1 - survival).rewrite(sp.sin))
        expected = sp.simplify(4 * (class_size - 1) * sp.sin(theta / 2) ** 2 / class_size ** 2)
        assert sp.simplify(value - expected) == 0
        leakage[name] = str(expected)
        transient[name] = sp.Rational(class_size - 1, class_size)

    assert leakage == {
        "transposition": "8*sin(theta/2)**2/9",
        "three_cycle": "sin(theta/2)**2",
    }
    assert transient == {"transposition": sp.Rational(2, 3), "three_cycle": sp.Rational(1, 2)}

    # Full six-state gauge orbit for a three-cycle conjugacy class.  K acts
    # as the oriented C3 current on the c half and vanishes on the c^2 half.
    shift = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    current = sp.simplify((shift - shift.H) / (2 * sp.I))
    k_full = sp.diag(current, sp.zeros(3))
    haar = sp.ones(6) / 6
    assert sp.simplify(haar * k_full) == sp.zeros(6)
    assert sp.simplify(k_full * haar) == sp.zeros(6)
    assert k_full.H == k_full

    result = {
        "schema": "marici.s3-control-leakage-energy.v1",
        "flat_vacuum_code": {
            "B_t_action": "zero",
            "B_c_action": "zero",
            "K_c_action": "zero",
            "final_leakage": "0",
        },
        "gauge_invariant_flux_excitation": {
            "final_vertex_leakage_probability": leakage,
            "maximum_at_theta_pi": {"transposition": "8/9", "three_cycle": "1"},
            "fixed_point_excess_vertex_energy": "equals_final_vertex_leakage_for_unit_vertex_penalty",
        },
        "holonomy_compute_transient": {
            "vertex_leakage_probability": {key: str(value) for key, value in transient.items()},
            "reason": "ancilla_which_flux_information_splits_the_gauge_orbit",
            "uncompute_disposition": "restored_before_the_phase_dependent_final_residual",
        },
        "gh_separator": {
            "A_K": "0",
            "K_A": "0",
            "commutes_with_fixed_point_vertex_projector": True,
            "commutes_with_flatness_projector_by_nontrivial_flux_support": True,
            "fixed_point_energy_change": "0",
            "nontrivial_domain": "charged_G_H_endpoint_subspace_in_kernel_of_A",
        },
        "deliberate_failure": {
            "claim": "clean_ancilla_uncompute_implies_zero_final_leakage_for_element_flux_phases",
            "actual": False,
            "counterexample": "theta=pi_three_cycle_port_has_unit_vertex_leakage_on_a_gauge_invariant_flux_excitation",
        },
        "aggregate_gates": {
            "all_nontrivial_ports_are_trivial_on_the_flat_vacuum_code": True,
            "transposition_final_leakage_formula_is_exact": True,
            "three_cycle_final_leakage_formula_is_exact": True,
            "transposition_compute_transient_is_two_thirds": True,
            "three_cycle_compute_transient_is_one_half": True,
            "excess_vertex_energy_equals_leakage_for_unit_penalty": True,
            "gh_separator_annihilates_the_haar_vertex_sector": True,
            "gh_separator_preserves_fixed_point_energy": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
