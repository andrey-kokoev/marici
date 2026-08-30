#!/usr/bin/env python3
"""Distinguish linear kernel completion from C2-torsor origin selection exactly."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
MODULAR = K / "results" / "s3-modular-data.json"
ODD = K / "results" / "s3-wilson-orientation-odd-algebra.json"
OUT = K / "results" / "s3-kernel-reference-typing.json"


def rank(rows: list[list[Fraction]]) -> int:
    work = [row[:] for row in rows]
    result = 0
    for column in range(len(work[0])):
        pivot = next((j for j in range(result, len(work)) if work[j][column]), None)
        if pivot is None:
            continue
        work[result], work[pivot] = work[pivot], work[result]
        scale = work[result][column]
        work[result] = [x / scale for x in work[result]]
        for j in range(len(work)):
            if j != result and work[j][column]:
                factor = work[j][column]
                work[j] = [work[j][k] - factor * work[result][k] for k in range(len(work[j]))]
        result += 1
    return result


def main() -> None:
    modular = json.loads(MODULAR.read_text(encoding="utf-8"))
    labels = modular["label_order"]
    ix = {label: i for i, label in enumerate(labels)}
    permutation = [1, 0, 2, 4, 3, 5, 6, 7]

    q_ab = [Fraction(int(i == ix["A"]) - int(i == ix["B"])) for i in range(8)]
    q_de = [Fraction(int(i == ix["D"]) - int(i == ix["E"])) for i in range(8)]
    odd_basis = [q_ab, q_de]
    assert rank(odd_basis) == 2
    assert all(v[permutation[i]] == -v[i] for v in odd_basis for i in range(8))

    # Evaluation on the tensor unit A sees q_AB but kills q_DE.
    vacuum_row = [[q_ab[ix["A"]], q_de[ix["A"]]]]
    assert rank(vacuum_row) == 1
    assert q_de[ix["A"]] == 0

    # A second independently typed evaluation (here at D) completes the
    # two-dimensional linear kernel.
    two_reference_rows = [
        [q_ab[ix["A"]], q_de[ix["A"]]],
        [q_ab[ix["D"]], q_de[ix["D"]]],
    ]
    assert rank(two_reference_rows) == 2

    # By contrast, each nontrivial orbit of the B-simple-current action is a
    # two-element C2 torsor. One origin bit separates its two points.
    orbits = []
    seen: set[int] = set()
    for i in range(8):
        if i not in seen:
            orbit = sorted({i, permutation[i]})
            seen.update(orbit)
            orbits.append([labels[j] for j in orbit])
    assert sorted(len(o) for o in orbits) == [1, 1, 1, 1, 2, 2]
    nontrivial = [o for o in orbits if len(o) == 2]
    assert nontrivial == [["A", "B"], ["D", "E"]]

    odd = json.loads(ODD.read_text(encoding="utf-8"))
    assert odd["diagonal_algebra_decomposition"]["C2_odd_dimension"] == 2

    result = {
        "schema": "marici.kitaev.s3-kernel-reference-typing.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (MODULAR, ODD)
        },
        "linear_projection": {
            "domain": "eight-dimensional diagonal algebra over Q",
            "map": "C2-even projection (I+sigma)/2",
            "kernel_dimension": 2,
            "kernel_basis": ["Q_A-Q_B", "Q_D-Q_E"],
            "vacuum_evaluation_rank_on_kernel": 1,
            "vacuum_evaluation_kernel_witness": "Q_D-Q_E",
            "vacuum_reference_is_injective_on_linear_kernel": False,
            "two_evaluations_A_and_D_rank_on_kernel": 2,
        },
        "torsor_quotient": {
            "action": "sigma=(A B)(D E)=B tensor -",
            "orbits": orbits,
            "nontrivial_two_point_orbits": nontrivial,
            "one_origin_bit_separates_each_nontrivial_orbit": True,
        },
        "typing_correction": {
            "literal_instance_of_linear_kernel_reference_theorem_with_one_scalar_R": False,
            "valid_instance_of_torsor_section_principle": True,
            "reason": "The additive odd kernel has dimension two, but the unresolved global frame is one C2 group coordinate. Linear reconstruction and torsor-origin selection are different claims.",
        },
        "deliberate_falsifier": {
            "claim": "vacuum evaluation is injective on the full odd linear kernel",
            "counterexample": "(Q_D-Q_E)(A)=0 although Q_D-Q_E is nonzero",
        },
        "verdict": "The vacuum fixes the B-simple-current sheet as a C2-torsor origin, not as a one-scalar completion of the full two-dimensional odd algebra. Applying the linear kernel-reference theorem literally requires two independent reference functionals. The cross-sector analogy survives only after its fiber type is changed from vector-space kernel to torsor.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
