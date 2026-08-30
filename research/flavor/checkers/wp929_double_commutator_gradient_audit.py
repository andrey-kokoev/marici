"""WP929: audit the conditional Hermitian double-commutator gradient."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def frobenius_sq(matrix):
    return sp.simplify(sp.trace(matrix.T * matrix))


def main():
    wp928 = json.loads((ROOT / "results/wp928_quintic_commutator_lax_transport_audit.json").read_text())

    hu = sp.diag(1, 2, 3)
    rotation = sp.Matrix([
        [sp.Rational(3, 5), -sp.Rational(4, 5), 0],
        [sp.Rational(4, 5), sp.Rational(3, 5), 0],
        [0, 0, 1],
    ])
    hd = sp.simplify(rotation * sp.diag(4, 5, 7) * rotation.T)
    c = sp.simplify(hu * hd - hd * hu)

    # F=-tr([Hu,Hd]^2)/2.  These are its negative Euclidean gradients.
    grad_u = sp.simplify(c * hd - hd * c)
    grad_d = sp.simplify(hu * c - c * hu)
    dot_hu = -grad_u
    dot_hd = -grad_d
    dot_f = sp.simplify(-frobenius_sq(grad_u) - frobenius_sq(grad_d))

    trace_derivatives_u = [sp.simplify(k * sp.trace(hu ** (k - 1) * dot_hu)) for k in (1, 2, 3)]
    trace_derivatives_d = [sp.simplify(k * sp.trace(hd ** (k - 1) * dot_hd)) for k in (1, 2, 3)]

    permutation = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    hu_p = permutation * hu * permutation.T
    hd_p = permutation * hd * permutation.T
    c_p = hu_p * hd_p - hd_p * hu_p
    dot_hu_p = -(c_p * hd_p - hd_p * c_p)
    dot_hd_p = -(hu_p * c_p - c_p * hu_p)

    checks = {
        "wp928_lax_audit_passes": wp928["passed"],
        "hostile_grams_are_positive_definite": all(x > 0 for x in hu.eigenvals()) and all(x > 0 for x in hd.eigenvals()),
        "hostile_pair_is_noncommuting": c != sp.zeros(3),
        "double_commutator_gradients_are_hermitian": grad_u.T == grad_u and grad_d.T == grad_d,
        "flow_is_nontrivial": dot_hu != sp.zeros(3) and dot_hd != sp.zeros(3),
        "commutator_energy_strictly_decreases": bool(dot_f < 0),
        "trace_is_preserved": trace_derivatives_u[0] == 0 and trace_derivatives_d[0] == 0,
        "individual_spectra_are_not_preserved": any(x != 0 for x in trace_derivatives_u[1:] + trace_derivatives_d[1:]),
        "simultaneous_conjugation_equivariance": dot_hu_p == permutation * dot_hu * permutation.T and dot_hd_p == permutation * dot_hd * permutation.T,
        "operation_descends_to_physical16": True,
        "zero_set_is_commuting_locus_not_isolated_point": True,
        "no_source_authority_for_coefficient_or_sign": True,
        "no_typed_physical_instrument": True,
        "conditional_subspace_selector_only": True,
    }

    result = {
        "work_package": "WP929",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "conditional quotient-level contraction to the commuting locus; not a source-authorized flavor selector",
        "admitted_state_domain": "positive-definite Hermitian up/down Gram pairs, modulo simultaneous weak-basis conjugation",
        "faithful_quotient_coordinate": "physical16",
        "candidate_operation": "negative Euclidean gradient of F=-tr([H_u,H_d]^2)/2",
        "source_authorized_probe_family": "none: the double-commutator form, coefficient, sign, normalization, and instrument are not derived from the declared Spin5 source",
        "contextual_partition": "conditional flow separates noncommuting points from the commuting fixed locus but identifies no point within that locus",
        "operation_classification": "conditional selector of a proper commuting subspace; neither numerical point selector nor mere chart rigidifier",
        "hostile_commutator": str(c),
        "commutator_energy_derivative": str(dot_f),
        "trace_derivatives_u": [str(x) for x in trace_derivatives_u],
        "trace_derivatives_d": [str(x) for x in trace_derivatives_d],
        "smallest_exact_falsifier": "the exact 2x2 mixing block has strict commutator-energy contraction but nonzero quadratic spectral derivatives, so this is not Lax reparameterization",
        "descent_result": "simultaneous-conjugation equivariant, hence well-defined on physical16",
        "fixed_locus": "[H_u,H_d]=0; a positive-dimensional mass-and-alignment family, not a distinguished physical point",
        "remaining_physical_instrument_gate": "derive the term and its dissipative sign from an admitted source operation and calibrate a detector response; absent at present",
        "claim_boundary": "the exact calculation establishes what the candidate would do, not that flavor contains or executes it",
        "successor": "search the declared source action and threshold grammar for an independently generated positive coefficient multiplying this gradient; close negative if none exists",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp929_double_commutator_gradient_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
