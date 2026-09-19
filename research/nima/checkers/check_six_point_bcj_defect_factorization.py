from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
sys.path.insert(0, str(ROOT / "research/nima/checkers"))
import sympy as sp

from check_six_point_bcj_quotient_rank import INDEX, kk_reduce
from check_six_point_nmhv_ordering_relations import sij

RESULT = ROOT / "research/nima/results/six-point-bcj-defect-factorization.json"
REPAIR = ROOT / "research/nima/results/six-point-minimal-bcj-chain-repair.json"


def fixed_leg_worldsheet_relations() -> tuple[list[tuple[int, ...]], sp.Matrix]:
    labels = list(itertools.permutations((2, 3, 4, 5)))
    rows = []
    for p in labels:
        row = [sp.Integer(0)] * 24
        weight = sp.Integer(0)
        for k in range(1, 5):
            weight += sij(1, p[k - 1])
            order = p[:k] + (1,) + p[k:] + (6,)
            for ddm, coefficient in kk_reduce(order).items():
                row[INDEX[ddm]] += weight * coefficient
        rows.append(row)
    return labels, sp.Matrix(rows)


def main() -> None:
    repair = json.loads(REPAIR.read_text(encoding="utf-8"))
    labels, relations = fixed_leg_worldsheet_relations()
    stored_labels = [tuple(row["permutation"]) for row in repair["relation_coordinates"]]
    defects = sp.Matrix([
        [sp.Rational(repair["relation_coordinates"][j]["defect_coordinates"][i]) for j in range(24)]
        for i in range(4)
    ])

    # A linear map from worldsheet relation vectors to defect lifts exists exactly
    # when every dependence among the 24 relation vectors is also a dependence
    # among their four defect-coordinate columns.
    relation_dependencies = relations.T.nullspace()
    violating = next(v for v in relation_dependencies if defects * v != sp.zeros(4, 1))
    support = [i for i, value in enumerate(violating) if value != 0]
    witness = {
        "coefficients": [str(violating[i]) for i in support],
        "relation_indices": support,
        "permutations": [list(labels[i]) for i in support],
        "worldsheet_combination_zero": relations.T * violating == sp.zeros(24, 1),
        "defect_combination": [str(x) for x in defects * violating],
    }

    checks = {
        "labels_match_repair_packet": labels == stored_labels,
        "fixed_leg_worldsheet_relation_rank_six": relations.rank() == 6,
        "repair_defect_rank_four": defects.rank() == 4,
        "relation_dependencies_exist": len(relation_dependencies) == 18,
        "explicit_dependency_violates_defect_assignment":
            witness["worldsheet_combination_zero"]
            and any(sp.Rational(x) != 0 for x in witness["defect_combination"]),
        "no_linear_factorization": relations.col_join(defects).rank() > relations.rank(),
    }
    out = {
        "schema": "marici.nima.six-point-bcj-defect-factorization.result.v1",
        "status": "fixed_cr_defect_repair_does_not_factor_through_worldsheet_bcj_relations"
        if all(checks.values()) else "failed",
        "checks": checks,
        "ranks": {
            "fixed_leg_worldsheet_relations": relations.rank(),
            "repair_defects": defects.rank(),
            "stacked_relation_and_defect_rows": relations.col_join(defects).rank(),
        },
        "dependency_witness": witness,
        "conclusion": "The four freely adjoined CR defect lifts cannot be identified with images of the fixed-leg worldsheet BCJ relation vectors: the proposed assignment fails to preserve linear dependencies. A valid CR-to-Koszul map must change the CR assignment or add source data before the defect projection, not merely rename the existing four repair generators as scattering-equation generators.",
        "claim_boundary": "This is a no-factorization theorem for the fixed 24 abstract-simplex CR chains and their stored four-coordinate repair. It does not obstruct a different CR carrier, a nonlinear construction, or an enlarged source module.",
    }
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
