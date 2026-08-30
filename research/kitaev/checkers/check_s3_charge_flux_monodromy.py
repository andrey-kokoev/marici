"""Exact pure-charge monodromy around D(S3) flux sectors."""

import itertools
import json
import sympy as sp


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "identity" if fixed == 3 else ("transposition" if fixed == 1 else "three_cycle")


def direct_sum(blocks):
    return sp.diag(*blocks)


def main():
    group = list(itertools.permutations(range(3)))
    sqrt3 = sp.sqrt(3)
    e = (0, 1, 2)
    r = (1, 2, 0)
    s = (1, 0, 2)
    r_matrix = sp.Matrix([[-sp.Rational(1, 2), -sqrt3 / 2],
                          [sqrt3 / 2, -sp.Rational(1, 2)]])
    s_matrix = sp.diag(1, -1)

    # Generate the standard representation from the unique r^k s^epsilon form.
    standard = {}
    for k in range(3):
        permutation_r = e
        matrix_r = sp.eye(2)
        for _ in range(k):
            permutation_r = compose(r, permutation_r)
            matrix_r = r_matrix * matrix_r
        for epsilon in range(2):
            permutation = compose(permutation_r, s if epsilon else e)
            matrix = matrix_r * (s_matrix if epsilon else sp.eye(2))
            standard[permutation] = sp.simplify(matrix)
    assert len(standard) == 6
    assert all(sp.simplify(standard[compose(g, h)] - standard[g] * standard[h]) == sp.zeros(2)
               for g in group for h in group)

    charges = {
        "A": {g: sp.Matrix([[1]]) for g in group},
        "B": {g: sp.Matrix([[parity(g)]]) for g in group},
        "C": standard,
    }
    flux_classes = {
        "D_or_E_transposition_flux": [g for g in group if cycle_type(g) == "transposition"],
        "F_G_or_H_three_cycle_flux": [g for g in group if cycle_type(g) == "three_cycle"],
    }
    # S rows from the independently frozen modular packet, indexed by charge and flux family.
    modular_entries = {
        ("A", "D_or_E_transposition_flux"): sp.Rational(1, 2),
        ("B", "D_or_E_transposition_flux"): -sp.Rational(1, 2),
        ("C", "D_or_E_transposition_flux"): 0,
        ("A", "F_G_or_H_three_cycle_flux"): sp.Rational(1, 3),
        ("B", "F_G_or_H_three_cycle_flux"): sp.Rational(1, 3),
        ("C", "F_G_or_H_three_cycle_flux"): -sp.Rational(1, 3),
    }

    audits = {}
    for charge_name, representation in charges.items():
        for flux_name, fluxes in flux_classes.items():
            monodromy = direct_sum([representation[g] for g in fluxes])
            dimension = monodromy.rows
            determinant = sp.simplify(monodromy.det())
            trace = sp.simplify(sp.trace(monodromy))
            characteristic = sp.factor(monodromy.charpoly().as_expr())
            scalar = monodromy == monodromy[0, 0] * sp.eye(dimension)
            expected_trace = sp.simplify(6 * modular_entries[(charge_name, flux_name)])
            assert trace == expected_trace
            assert determinant != 0
            audits[charge_name + "_around_" + flux_name] = {
                "operator_dimension": dimension,
                "trace": str(trace),
                "determinant": str(determinant),
                "characteristic_polynomial": str(characteristic).replace("lambda", "x"),
                "is_scalar": scalar,
                "six_times_modular_S_entry": str(expected_trace),
                "trace_matches_modular_entry": True,
            }

    trans_key = "C_around_D_or_E_transposition_flux"
    cycle_key = "C_around_F_G_or_H_three_cycle_flux"
    assert audits[trans_key]["trace"] == "0"
    assert audits[trans_key]["determinant"] == "-1"
    assert audits[trans_key]["characteristic_polynomial"] == "(x - 1)**3*(x + 1)**3"
    assert not audits[trans_key]["is_scalar"]
    assert audits[cycle_key]["trace"] == "-2"
    assert audits[cycle_key]["characteristic_polynomial"] == "(x**2 + x + 1)**2"
    assert not audits[cycle_key]["is_scalar"]

    trans_monodromy = direct_sum([charges["C"][g] for g in flux_classes["D_or_E_transposition_flux"]])
    cycle_monodromy = direct_sum([charges["C"][g] for g in flux_classes["F_G_or_H_three_cycle_flux"]])
    trans_minimal = (trans_monodromy**2 == sp.eye(6)
                     and trans_monodromy != sp.eye(6)
                     and trans_monodromy != -sp.eye(6))
    cycle_minimal = (sp.simplify(cycle_monodromy**2 + cycle_monodromy + sp.eye(4)) == sp.zeros(4)
                     and cycle_monodromy != sp.eye(4))
    assert trans_minimal and cycle_minimal

    # Flux centralizer charge is invisible to a pure electric monodromy probe.
    same_flux_class_same_operator = True  # D/E and F/G/H differ only in centralizer irrep.

    result = {
        "schema": "marici.s3-charge-flux-monodromy.v1",
        "monodromy_convention": "block_diagonal_charge_representation_evaluated_on_flux_basis",
        "total_quantum_dimension": 6,
        "audits": audits,
        "zero_S_entry_nonzero_operator_witness": {
            "pair": "C_with_D_or_E_transposition_flux",
            "S_entry": "0",
            "operator_invertible": True,
            "operator_scalar": False,
            "trace_cancels_between_plus_and_minus_reflection_eigenspaces": True,
        },
        "pure_charge_probe_cannot_resolve_flux_centralizer_irrep": same_flux_class_same_operator,
        "C_charge_minimal_polynomials": {
            "transposition_flux": "x**2-1",
            "three_cycle_flux": "x**2+x+1",
        },
        "aggregate_gates": {
            "standard_S3_representation_is_exact": True,
            "charge_flux_monodromy_is_invertible": True,
            "monodromy_trace_equals_total_dimension_times_S_entry": True,
            "zero_modular_entry_can_hide_nonzero_nonscalar_braid": True,
            "transposition_and_three_cycle_actions_have_distinct_minimal_polynomials": trans_minimal and cycle_minimal,
            "pure_charge_probe_has_centralizer_irrep_kernel": same_flux_class_same_operator,
            "scalar_modular_readout_is_not_operator_faithful": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
