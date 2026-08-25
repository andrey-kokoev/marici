#!/usr/bin/env python3
"""Exact rational observability, seam repair, and completion-collapse models."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "kitaev" / "results" / "tail-seam-observability.json"


def observability_matrix(A: sp.Matrix, J: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(*[J * (A**k) for k in range(A.rows)])


def main() -> None:
    # Minimal exact PBH obstruction. A=0 makes W(1)=J^T J exactly rational.
    A = sp.zeros(2)
    J_clark = sp.Matrix([[1, 0]])
    J_seam = sp.Matrix([[0, 1]])
    J_full = sp.Matrix.vstack(J_clark, J_seam)
    hidden = sp.Matrix([0, 1])
    sheet = sp.diag(1, -1)

    O_clark = observability_matrix(A, J_clark)
    O_full = observability_matrix(A, J_full)
    W_clark = J_clark.T * J_clark
    W_full = J_full.T * J_full

    assert A * hidden == sp.zeros(2, 1)
    assert J_clark * hidden == sp.zeros(1, 1)
    assert hidden != sp.zeros(2, 1)
    assert O_clark.rank() == 1
    assert W_clark.rank() == 1
    assert O_full.rank() == 2
    assert W_full == sp.eye(2)
    assert J_seam * hidden == sp.ones(1, 1)
    assert sheet * A == A * sheet
    assert sheet * hidden == -hidden
    assert J_clark * sheet == J_clark
    assert J_seam * sheet == -J_seam

    # A symmetry-related duplicate of Clark adds no rank.
    J_clark_sheet_copy = J_clark * sheet
    assert sp.Matrix.vstack(J_clark, J_clark_sheet_copy).rank() == 1

    # Minimality: a rank-zero augmentation cannot repair a one-dimensional
    # unobservable subspace; one row nonzero on it does.
    zero_extra = sp.zeros(1, 2)
    assert observability_matrix(A, sp.Matrix.vstack(J_clark, zero_extra)).rank() == 1
    assert J_seam.rank() == 1

    # Completion hostile family. Every cutoff is observable, but the Clark
    # lower bound is 1/N^2. The seam row restores a uniform lower bound 1.
    hostile = []
    for n in range(1, 9):
        eps = sp.Rational(1, n)
        Jc_n = sp.diag(1, eps)
        Jf_n = sp.Matrix.vstack(Jc_n, J_seam)
        Wc_n = Jc_n.T * Jc_n
        Wf_n = Jf_n.T * Jf_n
        assert Wc_n.det() > 0
        assert Wc_n[1, 1] == sp.Rational(1, n * n)
        assert Wf_n == sp.diag(1, 1 + sp.Rational(1, n * n))
        v = hidden
        assert (Jc_n * v).norm() == eps
        assert (J_seam * v).norm() == 1
        hostile.append({
            "cutoff": n,
            "clark_lambda_min": str(sp.Rational(1, n * n)),
            "full_lambda_min": "1",
            "clark_hidden_sequence_norm": str(eps),
            "seam_hidden_sequence_norm": "1",
        })

    # Candidate current rows are independent only modulo the Clark Krylov row
    # space. A proportional primitive row adds nothing; a square-current row
    # with a seam component repairs in this model. These are typing examples,
    # not theta-source identifications.
    J_primitive_candidate = sp.Matrix([[2, 0]])
    J_square_candidate = sp.Matrix([[1, 1]])
    assert sp.Matrix.vstack(O_clark, J_primitive_candidate).rank() == 1
    assert sp.Matrix.vstack(O_clark, J_square_candidate).rank() == 2

    result = {
        "schema": "marici.kitaev.tail-seam-observability.v1",
        "finite_exact_model": {
            "A": [[0, 0], [0, 0]],
            "J_Clark": [[1, 0]],
            "J_seam": [[0, 1]],
            "hidden_state": [0, 1],
            "PBH_eigenvalue": 0,
            "Clark_observability_rank": 1,
            "full_observability_rank": 2,
            "minimal_additional_row_rank": 1,
            "W_Clark_at_L_1": [[1, 0], [0, 0]],
            "W_full_at_L_1": [[1, 0], [0, 1]],
        },
        "machine_rejection": {
            "code": "clark_feature_pair_not_observable",
            "cutoff": "minimal-2-state",
            "eigenvalue": "0",
            "hidden_state": [0, 1],
            "feature_output": 0,
            "sheet": "C2-odd hidden line",
            "seam_output": 1,
        },
        "C2_action": {
            "R": [[1, 0], [0, -1]],
            "commutes_with_dynamics": True,
            "Clark_output_character": 1,
            "seam_output_character": -1,
            "unobservable_subspace": "preserved as a subspace and sign-reversed pointwise",
            "symmetry_related_Clark_copy_adds_rank": False,
        },
        "completion_hostile_family": {
            "A_N": "0",
            "J_Clark_N": "diag(1,1/N)",
            "J_seam_N": [[0, 1]],
            "every_finite_Clark_pair_observable": True,
            "Clark_uniform_lower_bound": False,
            "Clark_lambda_min": "1/N^2 -> 0",
            "full_uniform_lower_bound": 1,
            "escape_state": [0, 1],
            "samples": hostile,
        },
        "current_channel_rank_test": {
            "criterion": "rank increment modulo the Clark observability/Krylov row space",
            "proportional_primitive_candidate_adds_rank": False,
            "seam-bearing_square_candidate_adds_rank": True,
            "actual_theta_primitive_or_square_rows_derived": False,
        },
        "source_authority_boundary": {
            "control_theorem_derives_required_rank": True,
            "control_theorem_derives_theta_seam_row": False,
            "required_from_Grothendieck": ["A_X", "J_Clark_X", "J_seam_X", "primitive-current row", "square-current row", "cutoff embeddings and topology"],
        },
        "verdict": "Finite feature positivity upgrades to state faithfulness exactly through observability of (A_X,J_X). A one-dimensional Clark-unobservable invariant line needs one independent source row. The rational hostile family proves that finite observability at every cutoff does not imply a completion-stable lower bound; a seam row can restore uniform observability, but only if theta/Tate source data actually derives that row.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
