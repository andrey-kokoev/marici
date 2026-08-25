#!/usr/bin/env python3
"""Exact C2-even/odd decomposition of the D(S3) Wilson diagonal algebra."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
MODULAR = K / "results" / "s3-modular-data.json"
TORSOR = K / "results" / "s3-wilson-orientation-simple-current-torsor.json"
OUT = K / "results" / "s3-wilson-orientation-odd-algebra.json"


def rank(rows: list[list[Fraction]]) -> int:
    work = [row[:] for row in rows]
    result = 0
    for column in range(len(work[0])):
        pivot = next((j for j in range(result, len(work)) if work[j][column]), None)
        if pivot is None:
            continue
        work[result], work[pivot] = work[pivot], work[result]
        scale = work[result][column]
        work[result] = [value/scale for value in work[result]]
        for j in range(len(work)):
            if j != result and work[j][column]:
                factor = work[j][column]
                work[j] = [work[j][k] - factor*work[result][k] for k in range(len(work[j]))]
        result += 1
    return result


def main() -> None:
    modular = json.loads(MODULAR.read_text(encoding="utf-8"))
    labels = modular["label_order"]
    index = {label: j for j, label in enumerate(labels)}
    S = [[Fraction(value) for value in row] for row in modular["S_matrix"]]
    W = [[S[x][a]/S[0][a] for a in range(8)] for x in range(8)]
    permutation = [1, 0, 2, 4, 3, 5, 6, 7]

    even_basis = []
    odd_basis = []
    for a in range(8):
        unit = [Fraction(int(j == a)) for j in range(8)]
        moved = [unit[permutation[j]] for j in range(8)]
        even_basis.append([unit[j] + moved[j] for j in range(8)])
        odd_basis.append([unit[j] - moved[j] for j in range(8)])
    assert rank(even_basis) == 6
    assert rank(odd_basis) == 2

    wd, we = W[index["D"]], W[index["E"]]
    assert all(wd[permutation[a]] == -wd[a] for a in range(8))
    assert all(we[permutation[a]] == -we[a] for a in range(8))
    assert rank([wd, we]) == 2
    q_ab = [Fraction(int(a == index["A"]) - int(a == index["B"])) for a in range(8)]
    q_de = [Fraction(int(a == index["D"]) - int(a == index["E"])) for a in range(8)]
    assert [(wd[a] + we[a])/6 for a in range(8)] == q_ab
    assert [(wd[a] - we[a])/2 for a in range(8)] == q_de
    assert wd[index["A"]] == we[index["A"]] == 3
    assert wd[index["B"]] == we[index["B"]] == -3
    assert 6*S[0][index["D"]] == 6*S[0][index["E"]] == 3

    torsor = json.loads(TORSOR.read_text(encoding="utf-8"))
    assert torsor["simple_current"]["equals_hidden_sector_permutation"] is True
    result = {
        "schema": "marici.kitaev.s3-wilson-orientation-odd-algebra.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (MODULAR, TORSOR)
        },
        "diagonal_algebra_decomposition": {
            "total_dimension": 8,
            "C2_even_dimension": 6,
            "C2_odd_dimension": 2,
            "even_meaning": "functions on the six B-translation orbits",
            "odd_support": ["A/B antisymmetry", "D/E antisymmetry"],
        },
        "Wilson_odd_basis": {
            "basis": ["W_D", "W_E"],
            "rank": 2,
            "Q_A_minus_Q_B": "(W_D+W_E)/6",
            "Q_D_minus_Q_E": "(W_D-W_E)/2",
            "both_change_sign_under_B_translation": True,
        },
        "normalization_origin": {
            "W_D_on_tensor_unit_A": 3,
            "W_E_on_tensor_unit_A": 3,
            "equals_quantum_dimension": True,
            "W_D_on_B": -3,
            "W_E_on_B": -3,
            "vacuum_positive_normalization_selects_C2_sheet": True,
        },
        "repair_criterion": {
            "new_non_Wilson_observable_mathematically_required": False,
            "trusted_sign_normalization_of_one_D_or_E_port_suffices_for_minimum_family": True,
            "codebook_membership_without_sign_root_suffices": False,
            "noncircular_physical_requirement": "derive W_x(A)=d_x>0 from a prepared/identified tensor unit or from the microscopic ribbon constructor",
        },
        "boundary": {
            "tensor_unit_A_operationally_prepared_on_torus": False,
            "microscopic_ribbon_sign_preservation_under_interface_proved": False,
            "fault_tolerant_orientation_calibration_supplied": False,
        },
        "verdict": "The C2-odd diagonal sector is exactly two-dimensional and is already spanned by W_D,W_E. Their sum and difference recover Q_A-Q_B and Q_D-Q_E. Hence no new observable is mathematically needed: a trusted sign for one D/E port fixes the minimum-family orientation. The canonical sign is vacuum normalization W_x(A)=d_x>0. The remaining problem is operational, not algebraic—local torus syndrome does not identify A, and the ququart/binary interface has no proved sign-preserving microscopic constructor.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
