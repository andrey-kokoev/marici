"""Exact compiler for quotients/completions preceding partial repairs."""

from __future__ import annotations

from fractions import Fraction
from typing import Any


def rref(matrix: list[list[int | Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return a, []
    rows, cols, pivot_row = len(a), len(a[0]), 0
    pivots: list[int] = []
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return a, pivots


def nullspace(matrix: list[list[int | Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(matrix)
    cols = len(matrix[0]) if matrix else 0
    free = [j for j in range(cols) if j not in pivots]
    basis = []
    for j in free:
        vector = [Fraction(0) for _ in range(cols)]
        vector[j] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][j]
        basis.append(vector)
    return basis


def matvec(matrix: list[list[int | Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((Fraction(x) * y for x, y in zip(row, vector)), Fraction(0)) for row in matrix]


def exact_descent_gate(quotient: list[list[int]], distinction: list[list[int]]) -> dict[str, Any]:
    killed = nullspace(quotient)
    witness = next((v for v in killed if any(matvec(distinction, v))), None)
    return {
        "descends": witness is None,
        "criterion": "ker(quotient) subseteq ker(required_distinction)",
        "killed_dimension": len(killed),
        "witness": [str(x) for x in witness] if witness else None,
        "distinction_image": [str(x) for x in matvec(distinction, witness)] if witness else None,
    }


def compile_contract(contract: dict[str, Any]) -> dict[str, Any]:
    fixtures = {}
    errors: list[str] = []
    for fixture in contract.get("finite_fixtures", []):
        observed = exact_descent_gate(fixture["quotient_matrix"], fixture["required_distinction_matrix"])
        observed["expected_descends"] = fixture["expected_descends"]
        observed["passed"] = observed["descends"] == fixture["expected_descends"]
        fixtures[fixture["fixture_id"]] = observed
        if not observed["passed"]:
            errors.append("finite_fixture_mismatch:" + fixture["fixture_id"])

    theta = contract["theta_application"]
    finite_incidence = theta["finite_incidence"]
    if finite_incidence["P"]["formula"] != "p^(-1/2) delta_(log p)":
        errors.append("primitive_incidence_changed")
    if finite_incidence["Q"]["formula"] != "(1/2)p^(-1) delta_(2 log p)":
        errors.append("square_incidence_changed")
    if theta["completion_classes"]["P"] == theta["completion_classes"]["Q"]:
        errors.append("primitive_square_completion_types_conflated")
    if theta["completed_scalar_readout_authorized"]:
        errors.append("finite_incidence_laundered_to_scalar_completion")
    joint = theta.get("joint_global_completion", {})
    if not joint.get("source_authorized") or joint.get("gradewise_scalar_pushforward"):
        errors.append("global_tate_completion_mistyped")
    if theta.get("operator_lift", {}).get("source_authorized"):
        errors.append("scalar_tate_section_laundered_to_seam_operator")

    sequence_witnesses = {}
    for witness in theta["sequential_hostiles"]:
        valid = witness["quotient_norm_limit"] == "0" and witness["required_distinction_limit"] != "0"
        sequence_witnesses[witness["witness_id"]] = {
            "rejects_continuous_descent": valid,
            "code": "required_distinction_not_continuous_in_quotient_topology" if valid else None,
        }
        if not valid:
            errors.append("invalid_sequential_hostile:" + witness["witness_id"])

    return {
        "schema": "marici.distinction-preserving-completion-result.v1",
        "passed": not errors,
        "errors": errors,
        "theorem": {
            "algebraic": "R factors through Q iff ker(Q) subseteq ker(R)",
            "topological_necessary": "Q(v_n)->0 implies R(v_n)->0",
            "uniform_continuity": "R_N^*R_N <= C^2 Q_N for one cutoff-independent C",
        },
        "finite_fixtures": fixtures,
        "theta": {
            "L_factorization": ["L_finite_incidence", "L_typed_completion", "L_scalar_readout"],
            "finite_incidence_authorized": True,
            "completion_classes": theta["completion_classes"],
            "completed_scalar_readout_authorized": False,
            "joint_global_completion_authorized": True,
            "operator_lift_authorized": False,
            "sequential_hostiles": sequence_witnesses,
            "first_missing_constructor": "functorial operator-valued lift from global Tate-Poisson sewing to tail-seam incidence maps (B_s,C_s)",
        },
    }
