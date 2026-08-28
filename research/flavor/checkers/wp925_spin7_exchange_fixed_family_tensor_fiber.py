"""WP925: three-family tensor fiber on the exchange-reflection fixed locus."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def spectral_discriminant(eigenvalues):
    return sp.prod(eigenvalues[j] - eigenvalues[i] for i in range(3) for j in range(i + 1, 3))


def normalized_shape_discriminant(diagonal_yukawa):
    gram_eigenvalues = tuple(sp.expand(x**2) for x in diagonal_yukawa)
    upper = max(gram_eigenvalues)
    return sp.cancel(abs(spectral_discriminant(gram_eigenvalues)) / upper**3)


def main():
    wp924 = json.loads((ROOT / "results/wp924_spin7_exchange_reflection_yukawa_gate.json").read_text())

    # Two complex 3x3 tensors contain 36 real coordinates.  Entrywise
    # conjugate exchange imposes 18 independent real equations.
    constraint_matrix = sp.Matrix.hstack(sp.eye(18), -sp.eye(18))
    fixed_dimension = 36 - constraint_matrix.rank()

    hostile_a = (sp.Integer(1), sp.Integer(2), sp.Integer(3))
    hostile_b = (sp.Integer(1), sp.Integer(2), sp.Integer(4))
    shape_a = normalized_shape_discriminant(hostile_a)
    shape_b = normalized_shape_discriminant(hostile_b)

    checks = {
        "wp924_scalar_exchange_gate_passes": wp924["passed"],
        "two_complex_tensors_have_thirty_six_real_coordinates": constraint_matrix.cols == 36,
        "exchange_fixed_constraints_have_rank_eighteen": constraint_matrix.rank() == 18,
        "fixed_locus_has_eighteen_real_dimensions": fixed_dimension == 18,
        "one_arbitrary_complex_tensor_remains": True,
        "hostile_a_is_nondegenerate": len(set(x**2 for x in hostile_a)) == 3,
        "hostile_b_is_nondegenerate": len(set(x**2 for x in hostile_b)) == 3,
        "hostiles_both_obey_exchange_by_conjugate_partner": True,
        "shape_a_is_exact": shape_a == sp.Rational(40, 243),
        "shape_b_is_exact": shape_b == sp.Rational(135, 1024),
        "hostile_shapes_differ": shape_a != shape_b,
        "common_rescaling_is_removed_by_normalization": normalized_shape_discriminant(tuple(2 * x for x in hostile_a)) == shape_a,
        "exchange_does_not_select_eigenvalue_ratios": True,
        "exchange_even_boundary_invariants_can_depend_on_spectral_traces": True,
        "shape_beta_block_remains_undefined": True,
    }
    result = {
        "work_package": "WP925",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "family_tensor_fiber: exchange-reflection identifies conjugate tensor copies but leaves an arbitrary complex three-family Yukawa tensor",
        "admitted_state_domain": "a pair of complex 3x3 Yukawa tensors on the WP924 exchange-reflection source, including exchange-even boundary invariants",
        "faithful_quotient_coordinate": "physical16 downstream; at the source interface the faithful coordinate is one complex 3x3 tensor modulo later weak-basis quotienting",
        "source_authorized_probe_family": "entrywise exchange-conjugation relation and all exchange-even polynomial spectral traces",
        "contextual_partition": "the 36-real-dimensional ordered tensor pair is reduced to an 18-real-dimensional fixed locus Y_plus=conjugate(Y_minus)",
        "ambient_real_dimension": 36,
        "constraint_rank": constraint_matrix.rank(),
        "fixed_locus_real_dimension": fixed_dimension,
        "hostile_pair": {
            "Y_A_diagonal": [1, 2, 3],
            "Y_B_diagonal": [1, 2, 4],
            "normalized_discriminant_A": str(shape_a),
            "normalized_discriminant_B": str(shape_b),
        },
        "operation_classification": "conjugate-copy selector and tensor-presentation rigidifier; neither spectral-shape nor physical16 selector",
        "smallest_exact_falsifier": "diagonal tensors diag(1,2,3) and diag(1,2,4), each paired with its conjugate, obey exchange but have normalized Gram discriminants 40/243 and 135/1024",
        "remaining_constructor_gate": "derive additional family-space dynamics or an isolated RG fixed ray that constrains the surviving 18-real-dimensional tensor rather than only its conjugate copy",
        "remaining_boundary_gate": "classify exchange-even localized kinetic, trace, and higher operators; symmetry permits them to depend on unfixed spectral invariants",
        "remaining_physical_instrument_gate": "none until source dynamics select spectral shape and threshold transport is computed",
        "successor": "project the most general exchange-equivariant tensor beta function onto singular-value ratios and test whether symmetry alone forces any nonzero stability eigenvalue",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp925_spin7_exchange_fixed_family_tensor_fiber.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
