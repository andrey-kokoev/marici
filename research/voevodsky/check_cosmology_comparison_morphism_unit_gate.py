"""Unit gate for coupling the blow-up exceptional face to Xi_log.

Repeat iteration 3 proves the comparison morphism, if it exists as a chain map
from the exceptional-cell source to the relative residue complex, has no scalar
freedom: closure forces the Xi_log coefficient to equal the exceptional Cech
coefficient.  Since the exceptional coefficient is already a unit, the missing
Xi_log leg must be a unit too.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_comparison_morphism_unit_gate.json"


def load(name: str) -> dict:
    return json.loads((VOEVODSKY_RESULTS / name).read_text(encoding="utf-8"))


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]


def mod(value: int, prime: int) -> int:
    return value % prime


def main() -> None:
    blowup = load("cosmology_blowup_exceptional_cell_gate.json")
    universal = load("cosmology_universal_total_lift_cell.json")
    relative = load("cosmology_relative_residue_cocycle.json")

    assert blowup["passed"] is True
    assert universal["passed"] is True
    assert relative["passed"] is True
    d_residue = relative["differential_to_pair_residues_rows_q1q2_q1q3_q2q3_cols_Xi_minusSigma"]
    assert d_residue == [[1, -1], [-1, 1], [1, -1]]
    assert blowup["exceptional_cell_column_rows_Xi_minusSigma"] == [0, 1]

    # Candidate comparison column from the exceptional source after adding the
    # missing Xi_log leg.  The sourced exceptional face coefficient is fixed at
    # 1; let lambda be the Xi_log coefficient.  D(lambda,1)=0 iff lambda=1.
    candidates = []
    for lam in range(-3, 4):
        column = [lam, 1]
        residue_boundary = mat_vec(d_residue, column)
        closed = residue_boundary == [0, 0, 0]
        candidates.append({
            "xi_log_coefficient": lam,
            "column_rows_Xi_minusSigma": column,
            "residue_boundary": residue_boundary,
            "chain_map_condition": closed,
        })
    assert [item["xi_log_coefficient"] for item in candidates if item["chain_map_condition"]] == [1]

    orientation_reversed_column = [-1, -1]
    assert mat_vec(d_residue, orientation_reversed_column) == [0, 0, 0]

    witnesses = {}
    for prime in (101, 103):
        allowed_lambdas = [lam for lam in range(prime) if all(mod(value, prime) == 0 for value in mat_vec(d_residue, [lam, 1]))]
        assert allowed_lambdas == [1]
        witnesses[str(prime)] = {
            "exceptional_face_coefficient": 1,
            "unique_Xi_log_coefficient_mod_prime": allowed_lambdas[0],
            "chain_column": [1, 1],
            "orientation_reversed_chain_column": [prime - 1, prime - 1],
        }

    result = {
        "schema": "marici.voevodsky.cosmology-comparison-morphism-unit-gate.v1",
        "status": "comparison_if_sourced_is_forced_unit",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_blowup_exceptional_cell_gate.json",
            "research/voevodsky/results/cosmology_universal_total_lift_cell.json",
            "research/voevodsky/results/cosmology_relative_residue_cocycle.json",
        ],
        "residue_differential": d_residue,
        "fixed_exceptional_face_coefficient": 1,
        "candidate_columns_tested_lambda_minus3_to_3": candidates,
        "forced_column": [1, 1],
        "orientation_reversed_forced_column": [-1, -1],
        "finite_field_witnesses": witnesses,
        "meaning": "Once the exceptional face leg is fixed with unit coefficient, the chain-map condition forces the Xi_log comparison coefficient to be the same unit; there is no remaining scalar-fitting freedom.",
        "source_status": "the unit coefficient is forced conditionally, but the comparison morphism from the blow-up source to Xi_log is still not constructed",
        "next_gate": "construct the geometric residue/Gysin comparison sending the exceptional face to Xi_log, then this checker certifies its coefficient must be a unit",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
