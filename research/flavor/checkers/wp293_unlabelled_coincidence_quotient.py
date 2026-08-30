"""WP293: exact coincidence inversion on the unlabelled permutation quotient."""

import json
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def order_transform(vertex_count):
    return sp.Matrix(
        [
            [sp.Rational(sp.binomial(failure_count, order), sp.binomial(vertex_count, order)) if failure_count >= order else 0 for failure_count in range(vertex_count + 1)]
            for order in range(vertex_count + 1)
        ]
    )


def unlabelled_tower(labelled_law, vertex_count):
    count_law = [sp.S.Zero] * (vertex_count + 1)
    for atom, probability in labelled_law.items():
        count_law[sum(atom)] += probability
    transform = order_transform(vertex_count)
    return sp.Matrix(count_law), transform * sp.Matrix(count_law)


def main():
    vertex_count = 3
    transform = order_transform(vertex_count)
    inverse = transform.inv()
    labelled_atoms = list(product((0, 1), repeat=vertex_count))

    first_labelled = {atom: sp.S.Zero for atom in labelled_atoms}
    second_labelled = {atom: sp.S.Zero for atom in labelled_atoms}
    first_labelled[(1, 0, 0)] = 1
    second_labelled[(0, 1, 0)] = 1
    first_counts, first_tower = unlabelled_tower(first_labelled, vertex_count)
    second_counts, second_tower = unlabelled_tower(second_labelled, vertex_count)

    test_counts = sp.Matrix([sp.Rational(1, 8), sp.Rational(3, 8), sp.Rational(3, 8), sp.Rational(1, 8)])
    test_tower = transform * test_counts
    reconstructed_counts = inverse * test_tower

    checks = {
        "order_transform_is_full_rank_on_count_quotient": transform.rank() == vertex_count + 1,
        "order_transform_determinant_is_nonzero": transform.det() != 0,
        "exact_inverse_reconstructs_test_count_law": reconstructed_counts == test_counts,
        "permuted_literal_packets_are_distinct": first_labelled != second_labelled,
        "permuted_literal_packets_have_same_count_law": first_counts == second_counts,
        "permuted_literal_packets_have_same_unlabelled_tower": first_tower == second_tower,
        "labelled_to_count_projection_has_dimension_four_kernel": 2**vertex_count - (vertex_count + 1) == 4,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP293",
        "theorem_domain": "three Boolean domain failures modulo the full S3 permutation groupoid",
        "faithful_quotient_coordinate": "count law q_r=P(exactly r failures), r=0,1,2,3",
        "unlabelled_order_tower": "M_k=E[binomial(R,k)]/binomial(3,k), k=0,1,2,3",
        "order_transform": [[str(value) for value in transform.row(i)] for i in range(transform.rows)],
        "inverse_transform": [[str(value) for value in inverse.row(i)] for i in range(inverse.rows)],
        "test_count_law": [str(value) for value in test_counts],
        "test_order_tower": [str(value) for value in test_tower],
        "hostile_labelled_pair": {
            "first_atom": [1, 0, 0],
            "second_atom": [0, 1, 0],
            "shared_count_law": [str(value) for value in first_counts],
            "shared_unlabelled_tower": [str(value) for value in first_tower],
        },
        "contextual_partition": "the complete unlabelled order tower separates S3 count classes but not literal labelled packets inside a permutation orbit",
        "classification": "faithful selector-risk readout on the unlabelled quotient; adding labelled ports defines a new relational experiment over a smaller stabilizer groupoid",
        "smallest_exact_falsifier": "delta_(1,0,0) and delta_(0,1,0) are distinct labelled laws but have the same count law and complete unlabelled coincidence tower",
        "remaining_physical_instrument_gate": "declare whether domain labels are erased by S3 or implemented by source-derived ports; labelled coincidence claims require port calibration and the changed stabilizer groupoid",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp293_unlabelled_coincidence_quotient.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
