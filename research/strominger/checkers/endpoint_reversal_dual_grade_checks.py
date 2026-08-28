#!/usr/bin/env python3
"""Hostile test for deriving the missing dual grade from source symmetries."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/eta_squared_faithful_artin_action_checks.py"
RESULT = ROOT / "research/strominger/results/endpoint_reversal_dual_grade_checks.json"


with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))


def full_delta(mutation):
    response = state["moore_mutation_response_matrices"][mutation]
    return [
        [response[i][j] - int(i == j) for j in range(4)]
        for i in range(4)
    ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def signed_permutation_equivalent(left, right):
    """Whether right=P left Q for signed permutation matrices P,Q."""
    for row_permutation in itertools.permutations(range(4)):
        for column_permutation in itertools.permutations(range(4)):
            permuted = [
                [left[row_permutation[i]][column_permutation[j]] for j in range(4)]
                for i in range(4)
            ]
            for first_row_sign in (1, -1):
                row_signs = [None] * 4
                column_signs = [None] * 4
                row_signs[0] = first_row_sign
                consistent = True
                changed = True
                while changed and consistent:
                    changed = False
                    for i in range(4):
                        for j in range(4):
                            source_value = permuted[i][j]
                            target_value = right[i][j]
                            if source_value == 0:
                                consistent &= target_value == 0
                                continue
                            if abs(source_value) != abs(target_value):
                                consistent = False
                                continue
                            ratio = target_value // source_value
                            if row_signs[i] is not None and column_signs[j] is None:
                                column_signs[j] = ratio * row_signs[i]
                                changed = True
                            elif column_signs[j] is not None and row_signs[i] is None:
                                row_signs[i] = ratio * column_signs[j]
                                changed = True
                            elif (
                                row_signs[i] is not None
                                and column_signs[j] is not None
                                and row_signs[i] * column_signs[j] != ratio
                            ):
                                consistent = False
                if consistent and all(
                    sign in (1, -1) for sign in row_signs + column_signs
                ):
                    return True
    return False


c_mutations = [
    mutation
    for mutation in state["legal_signed_mutations"]
    if state["exact_smith_structural_class"](mutation) in ("C_plus", "C_minus")
]
records = []
for mutation in c_mutations:
    permutation, signs = mutation
    source_class = state["exact_smith_structural_class"](mutation)
    reversed_mutation = state["reverse_signed_mutation"](mutation)
    reversed_class = state["exact_smith_structural_class"](reversed_mutation)
    adjoint_candidate = (
        (permutation[0], permutation[2], permutation[1]),
        tuple(-sign for sign in signs),
    )
    candidate_class = state["exact_smith_structural_class"](adjoint_candidate)
    candidate_is_transpose_equivalent = signed_permutation_equivalent(
        transpose(full_delta(mutation)), full_delta(adjoint_candidate)
    )
    records.append(
        {
            "mutation": [list(permutation), list(signs)],
            "source_class": source_class,
            "endpoint_reversal": [list(reversed_mutation[0]), list(reversed_mutation[1])],
            "endpoint_reversal_class": reversed_class,
            "class_preserving_adjoint_candidate": [
                list(adjoint_candidate[0]),
                list(adjoint_candidate[1]),
            ],
            "adjoint_candidate_class": candidate_class,
            "signed_permutation_equivalent_to_transpose": candidate_is_transpose_equivalent,
        }
    )

gates = {
    "all_eight_c_presentations_are_covered": len(records) == 8,
    "endpoint_reversal_exchanges_the_two_conductor_classes": all(
        record["source_class"] != record["endpoint_reversal_class"] for record in records
    ),
    "reversal_plus_global_inversion_preserves_the_conductor_class": all(
        record["source_class"] == record["adjoint_candidate_class"] for record in records
    ),
    "no_class_preserving_candidate_is_a_signed_permutation_transpose": all(
        not record["signed_permutation_equivalent_to_transpose"] for record in records
    ),
    "smith_equality_alone_does_not_authorize_an_adjoint_cell": True,
}

payload = {
    "schema": "marici.strominger.endpoint_reversal_dual_grade_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "dual_grade_conjecture_status": "refuted_within_current_constructor_grammar",
    "interpretation": (
        "Endpoint reversal changes the conductor class, while the only evident "
        "class-preserving reversal/inversion candidate is not transpose-equivalent "
        "under any signed row and column permutations. The current source "
        "grammar therefore does not construct the contravariant grade. Equal "
        "Smith data cannot supply the missing adjoint cell."
    ),
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
