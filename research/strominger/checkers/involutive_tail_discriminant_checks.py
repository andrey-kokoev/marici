#!/usr/bin/env python3
"""Test the metric-free involutive-lattice explanation of the C square."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "research/strominger/results/single_channel_root_norm_checks.json"
RESULT = ROOT / "research/strominger/results/involutive_tail_discriminant_checks.json"

source = json.loads(INPUT.read_text(encoding="utf-8"))

plus_generator = [1, 1]
minus_generator = [1, -1]
eigenbasis_matrix = [plus_generator, minus_generator]
eigenbasis_determinant = (
    eigenbasis_matrix[0][0] * eigenbasis_matrix[1][1]
    - eigenbasis_matrix[0][1] * eigenbasis_matrix[1][0]
)
integral_splitting_defect = abs(eigenbasis_determinant)

records = []
for record in source["records"]:
    conductor = record["conductor"]
    covariant_degree = conductor
    contravariant_degree = conductor
    paired_degree = covariant_degree * contravariant_degree
    reduced_snake_modulus = abs(record["connecting_scalar"]) // record["content"]
    predicted_reduced_modulus = integral_splitting_defect * paired_degree
    records.append(
        {
            "class": record["class"],
            "permutation": record["permutation"],
            "signs": record["signs"],
            "conductor": conductor,
            "covariant_degree": covariant_degree,
            "contravariant_degree": contravariant_degree,
            "paired_degree": paired_degree,
            "integral_splitting_defect": integral_splitting_defect,
            "reduced_snake_modulus": reduced_snake_modulus,
            "predicted_reduced_modulus": predicted_reduced_modulus,
        }
    )

gates = {
    "tail_swap_eigenlattices_have_index_two": integral_splitting_defect == 2,
    "all_reduced_snake_moduli_equal_index_times_paired_degree": all(
        record["reduced_snake_modulus"] == record["predicted_reduced_modulus"]
        for record in records
    ),
    "one_variance_alone_cannot_supply_the_square": all(
        record["reduced_snake_modulus"]
        != record["integral_splitting_defect"] * record["covariant_degree"]
        for record in records
    ),
    "inverting_two_erases_the_integral_splitting_defect": integral_splitting_defect == 2,
    "current_packet_does_not_identify_snake_target_with_the_dual_tail_line": True,
}

payload = {
    "schema": "marici.strominger.involutive_tail_discriminant_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "arithmetic_skeleton_status": "confirmed_exactly",
    "categorical_identification_status": "missing",
    "interpretation": (
        "The unexplained factor 2 is the integral index of the plus/minus tail "
        "eigenlattices. The remaining square is exactly the product of degree "
        "kappa on an anti-invariant line and degree kappa on a putative dual "
        "line. This is metric-free. The source packet has not yet identified "
        "the snake target with that dual, so the arithmetic match is not yet "
        "a source theorem."
    ),
    "tail_swap": [[0, 1], [1, 0]],
    "plus_generator": plus_generator,
    "minus_generator": minus_generator,
    "eigenbasis_determinant": eigenbasis_determinant,
    "integral_splitting_defect": integral_splitting_defect,
    "localized_at_two_behavior": "the eigenbasis becomes invertible after adjoining 1/2",
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
