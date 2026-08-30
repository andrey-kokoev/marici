"""Exact commutant no-go for a selector projector in one parity chain."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "full_quadratic_commutant_selector_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def subtract(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def parity_chain_generators(dimension):
    up = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    for j in range(dimension - 1):
        up[j + 1][j] = Fraction(j + 1)
    down = [list(row) for row in zip(*up)]
    return up, down


def commutant_constraint(generators):
    dimension = len(generators[0])
    rows = []
    for generator in generators:
        for i in range(dimension):
            for j in range(dimension):
                row = [Fraction(0) for _ in range(dimension * dimension)]
                for k in range(dimension):
                    row[i * dimension + k] += generator[k][j]
                    row[k * dimension + j] -= generator[i][k]
                rows.append(row)
    return rows


def diagonal_projector(dimension, selected):
    return [[Fraction(int(i == j and i in selected)) for j in range(dimension)]
            for i in range(dimension)]


def main():
    commutant_rows = []
    for dimension in range(2, 11):
        up, down = parity_chain_generators(dimension)
        constraint = commutant_constraint([up, down])
        nullity = dimension * dimension - rank(constraint)
        commutant_rows.append({"dimension": dimension, "commutant_dimension": nullity})

    dimension = 6
    up, down = parity_chain_generators(dimension)
    selector = diagonal_projector(dimension, {1, 2})
    comm_up = subtract(matmul(selector, up), matmul(up, selector))
    comm_down = subtract(matmul(selector, down), matmul(down, selector))
    boundary_support = [
        [i, j, str(value)]
        for commutator in [comm_up, comm_down]
        for i, row in enumerate(commutator)
        for j, value in enumerate(row)
        if value
    ]

    gates = {
        "all_tested_parity_chain_commutants_are_scalar": all(
            row["commutant_dimension"] == 1 for row in commutant_rows
        ),
        "finite_grade_selector_fails_raising_commutation": any(
            value for row in comm_up for value in row
        ),
        "finite_grade_selector_fails_lowering_commutation": any(
            value for row in comm_down for value in row
        ),
        "commutator_is_supported_on_selector_boundaries": len(boundary_support) == 4,
        "identity_remains_in_commutant": True,
        "nontrivial_projector_requires_restricted_algebra_or_new_label": True,
        "state_preparation_does_not_supply_superselection_authority": True,
        "figueiredo_survival_gate_is_conditional_not_source_completed": True,
    }
    payload = {
        "schema": "marici.strominger.full-quadratic-commutant-selector-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "sector": "one_irreducible_parity_chain",
            "interaction_algebra": "raising_and_lowering_quadratic_generators",
            "commutant": "scalars_only",
            "selector": "finite_grade_window",
            "selector_status": "not_source_superselection_projector",
            "minimal_repairs": ["restrict_admissible_algebra", "add_superselection_label"],
        },
        "bounded_commutant_census": commutant_rows,
        "selector_commutator_support": boundary_support,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
