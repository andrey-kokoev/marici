"""WP294: exact hostile physical16 pair inside one selected CP branch."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ckm_squared_moduli(s12, c12, s23, c23, s13, c13):
    imaginary = sp.I
    matrix = sp.Matrix(
        [
            [c12 * c13, s12 * c13, -imaginary * s13],
            [-s12 * c23 - imaginary * c12 * s23 * s13, c12 * c23 - imaginary * s12 * s23 * s13, s23 * c13],
            [s12 * s23 - imaginary * c12 * c23 * s13, -c12 * s23 - imaginary * s12 * c23 * s13, c23 * c13],
        ]
    )
    squared = [sp.simplify(sp.expand_complex(value * sp.conjugate(value))) for value in matrix]
    return matrix, squared


def packet(s12, c12):
    s23, c23 = sp.Rational(5, 13), sp.Rational(12, 13)
    s13, c13 = sp.Rational(5, 13), sp.Rational(12, 13)
    matrix, squared = ckm_squared_moduli(s12, c12, s23, c23, s13, c13)
    jarlskog = sp.simplify(c12 * c23 * c13**2 * s12 * s23 * s13)
    masses = [sp.Rational(value) for value in (1, 2, 3, 5, 7, 11)]
    physical16_squared_embedding = masses + squared + [jarlskog]
    return matrix, squared, jarlskog, physical16_squared_embedding


def main():
    first = packet(sp.Rational(3, 5), sp.Rational(4, 5))
    second = packet(sp.Rational(5, 13), sp.Rational(12, 13))
    first_matrix, first_squared, first_j, first_physical = first
    second_matrix, second_squared, second_j, second_physical = second

    first_unitarity = sp.simplify(first_matrix * first_matrix.conjugate().T)
    second_unitarity = sp.simplify(second_matrix * second_matrix.conjugate().T)
    identity = sp.eye(3)
    hostile_difference = [sp.simplify(a - b) for a, b in zip(first_physical, second_physical)]
    shared_branch = 1

    checks = {
        "first_ckm_matrix_is_exactly_unitary": first_unitarity == identity,
        "second_ckm_matrix_is_exactly_unitary": second_unitarity == identity,
        "ordered_mass_packets_are_identical": first_physical[:6] == second_physical[:6],
        "physical16_embeddings_are_distinct": any(value != 0 for value in hostile_difference),
        "both_signed_jarlskog_coordinates_are_positive": first_j > 0 and second_j > 0,
        "jarlskog_magnitudes_are_distinct": first_j != second_j,
        "binary_branch_readout_collapses_hostile_pair": sp.sign(first_j) == sp.sign(second_j) == shared_branch,
        "squared_moduli_rows_normalize": all(sum(squared[3 * row : 3 * row + 3]) == 1 for squared in (first_squared, second_squared) for row in range(3)),
        "squared_moduli_columns_normalize": all(sum(squared[column::3]) == 1 for squared in (first_squared, second_squared) for column in range(3)),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    def serialize(values):
        return [str(value) for value in values]

    result = {
        "work_package": "WP294",
        "admitted_state_domain": "nondegenerate ordered quark masses and exact unitary CKM matrices with positive signed J",
        "faithful_quotient_coordinate": "physical16 = six ordered masses, nine CKM moduli, and signed J; checker uses squared moduli, an equivalent positive embedding",
        "source_operation_under_test": "conditional CP-domain preparation with branch readout sign(J)",
        "hostile_pair": {
            "first_physical16_squared_embedding": serialize(first_physical),
            "second_physical16_squared_embedding": serialize(second_physical),
            "coordinate_difference": serialize(hostile_difference),
            "shared_branch": shared_branch,
        },
        "contextual_partition": "binary branch probes partition physical16 into J-positive and J-negative components, with a separate J=0 boundary; they do not separate points inside a component",
        "descent": "sign(J) is defined from the signed weak-basis invariant already present in physical16, so the readout descends on the nondegenerate J-nonzero domain",
        "classification": "conditional orientation selector if a source-to-sign(J) map is derived; neither a point selector nor a texture rigidifier",
        "smallest_exact_falsifier": "the two exact unitary packets have identical ordered masses and positive J but different CKM moduli and J magnitudes",
        "first_nonfaithful_arrow": "physical16 -> sign(J)",
        "remaining_physical_instrument_gate": "derive the CP-domain branch-to-signed-J map from a flavor source, then add source-authorized magnitude and CP-even probes if selection of a smaller physical16 family is claimed",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp294_branch_to_physical16_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
